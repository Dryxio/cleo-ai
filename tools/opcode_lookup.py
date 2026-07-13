#!/usr/bin/env python3
"""Structured opcode search for agents and humans.

Examples:
    python3 tools/opcode_lookup.py search "vehicle coordinates"
    python3 tools/opcode_lookup.py show CREATE_CAR
    python3 tools/opcode_lookup.py show 0F12 --extension CLEO+
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CATALOG = ROOT / "source_data" / "sa.json"


def load_commands(path: Path) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(
            f"Opcode source is missing: {path}. Run `python3 tools/sync_reference.py` first."
        )
    data = json.loads(path.read_text(encoding="utf-8"))
    commands = []
    for extension in data["extensions"]:
        for command in extension["commands"]:
            item = dict(command)
            item["extension"] = extension["name"]
            commands.append(item)
    return commands


def summary(command: dict) -> dict:
    attrs = command.get("attrs", {})
    return {
        "id": command["id"],
        "name": command["name"],
        "class": command.get("class"),
        "member": command.get("member"),
        "extension": command["extension"],
        "params": command.get("num_params", 0),
        "flags": [key.removeprefix("is_") for key, value in attrs.items() if value],
        "description": command.get("short_desc", ""),
    }


def search(commands: list[dict], query: str, limit: int) -> list[dict]:
    terms = query.lower().split()
    ranked = []
    for command in commands:
        name = command["name"].lower()
        haystack = " ".join(
            str(value or "")
            for value in (
                command["id"],
                command["name"],
                command.get("class"),
                command.get("member"),
                command.get("short_desc"),
                command["extension"],
            )
        ).lower()
        if not all(term in haystack for term in terms):
            continue
        score = 0
        normalized_query = query.upper().replace(" ", "_")
        if command["name"] == normalized_query:
            score += 100
        elif name.startswith(query.lower().replace(" ", "_")):
            score += 50
        score += sum(10 for term in terms if term in name)
        if command.get("short_desc"):
            score += 1
        ranked.append((score, command["name"], command["extension"], command))
    ranked.sort(key=lambda item: (-item[0], item[1], item[2]))
    return [summary(item[3]) for item in ranked[:limit]]


def show(commands: list[dict], key: str, extension: str | None) -> list[dict]:
    key_upper = key.upper()
    matches = [
        command
        for command in commands
        if command["name"].upper() == key_upper or command["id"].upper() == key_upper
    ]
    if extension:
        matches = [item for item in matches if item["extension"].lower() == extension.lower()]
    matches.sort(key=lambda item: (item["extension"], item["id"], item["name"]))
    return matches


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    subparsers = parser.add_subparsers(dest="command", required=True)

    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("query")
    search_parser.add_argument("--limit", type=int, default=20)

    show_parser = subparsers.add_parser("show")
    show_parser.add_argument("key")
    show_parser.add_argument("--extension")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        commands = load_commands(args.catalog)
    except (OSError, ValueError, KeyError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    if args.command == "search":
        result = search(commands, args.query, args.limit)
    else:
        result = show(commands, args.key, args.extension)

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result else 1


if __name__ == "__main__":
    raise SystemExit(main())
