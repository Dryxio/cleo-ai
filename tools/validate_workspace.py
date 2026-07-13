#!/usr/bin/env python3
"""Static safety checks for CLEO/Sanny Builder source in this workspace.

This is intentionally conservative. It catches high-value AI failure modes but
does not replace the Sanny Builder compiler or an in-game runtime test.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PROFILE = ROOT / "config" / "target-profile.json"
DEFAULT_CATALOG = ROOT / "source_data" / "sa.json"


LANGUAGE_WORDS = {
    "and",
    "break",
    "case",
    "const",
    "continue",
    "debug_off",
    "debug_on",
    "default",
    "else",
    "end",
    "false",
    "float",
    "for",
    "function",
    "goto",
    "if",
    "int",
    "logical",
    "longstring",
    "not",
    "or",
    "repeat",
    "return",
    "script_name",
    "shortstring",
    "string",
    "switch",
    "then",
    "true",
    "until",
    "while",
}

COMPARISON_OR_ASSIGNMENT = re.compile(r"(?:==|<>|<=|>=|\+=|-=|\*=|/=|(?<![<>=])=(?!=)|<|>)")
SINGLE_ASSIGNMENT = re.compile(r"(?<![<>=+*/-])=(?!=)")
IDENTIFIER = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


@dataclass(frozen=True)
class Opcode:
    name: str
    opcode_id: str
    extension: str
    attrs: dict


@dataclass
class Finding:
    severity: str
    path: Path
    line: int
    message: str

    def render(self) -> str:
        relative = self.path.relative_to(ROOT) if self.path.is_relative_to(ROOT) else self.path
        return f"{self.severity}: {relative}:{self.line}: {self.message}"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_catalog(path: Path) -> dict[str, list[Opcode]]:
    if not path.exists():
        raise FileNotFoundError(
            f"Opcode source is missing: {path}. Run `python3 tools/sync_reference.py` first."
        )
    data = load_json(path)
    catalog: dict[str, list[Opcode]] = defaultdict(list)
    for extension in data["extensions"]:
        extension_name = extension["name"]
        for command in extension["commands"]:
            opcode = Opcode(
                name=command["name"],
                opcode_id=command["id"],
                extension=extension_name,
                attrs=command.get("attrs", {}),
            )
            catalog[opcode.name.lower()].append(opcode)
    return catalog


def source_lines(path: Path) -> list[tuple[int, str]]:
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    if path.suffix.lower() != ".md":
        return list(enumerate(lines, 1))

    output: list[tuple[int, str]] = []
    in_code = False
    for line_number, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            output.append((line_number, line))
    return output


def strip_comment(line: str) -> str:
    in_quote: str | None = None
    index = 0
    while index < len(line) - 1:
        char = line[index]
        if char in {'"', "'"}:
            if in_quote == char:
                in_quote = None
            elif in_quote is None:
                in_quote = char
        if in_quote is None and line[index : index + 2] == "//":
            return line[:index]
        index += 1
    return line


def declared_functions(lines: list[tuple[int, str]]) -> set[str]:
    names = set()
    for _, raw in lines:
        match = re.match(r"\s*function\s+([A-Za-z_][A-Za-z0-9_]*)", raw, re.IGNORECASE)
        if match:
            names.add(match.group(1).lower())
    return names


def imported_extensions(lines: list[tuple[int, str]]) -> set[str]:
    imports = set()
    for _, raw in lines:
        match = re.search(r"\{\$USE\s+([^}]+)\}", raw, re.IGNORECASE)
        if match:
            imports.update(part.strip() for part in match.group(1).split(","))
    return imports


def invocation_candidate(
    code: str,
    catalog: dict[str, list[Opcode]],
    functions: set[str],
) -> tuple[str | None, bool]:
    """Return (candidate, is_definitely_command_shaped)."""
    code = code.strip()
    if not code or code.startswith(("{$", ":")):
        return None, False
    if code.lower().startswith("not "):
        code = code[4:].lstrip()

    first_match = IDENTIFIER.match(code)
    if not first_match:
        return None, False
    first = first_match.group(0).lower()

    if first in LANGUAGE_WORDS or first in functions:
        return None, False
    # Opcodes such as string_format can contain an equals sign later in the line.
    if first in catalog:
        return first, True
    if re.match(r"^[A-Za-z_][A-Za-z0-9_]*\s*\(", code):
        return None, False

    assignment = SINGLE_ASSIGNMENT.search(code)
    if assignment:
        rhs = code[assignment.end() :].strip()
        rhs_match = IDENTIFIER.match(rhs)
        if not rhs_match:
            return None, False
        candidate = rhs_match.group(0).lower()
        if candidate in catalog:
            return candidate, True
        if candidate in functions or re.match(r"^[A-Z_][A-Z0-9_]*\s*\(", rhs):
            return None, False
        # An unknown snake_case call on an assignment RHS is probably hallucinated.
        command_shaped = "_" in candidate and bool(rhs[rhs_match.end() :].strip())
        return (candidate, True) if command_shaped else (None, False)

    # Raw comparisons and variable mutations are not opcode calls.
    if COMPARISON_OR_ASSIGNMENT.search(code):
        return None, False

    # A lowercase bare statement is command-shaped in Sanny source. Variables
    # used in comparisons/assignments were filtered above.
    return (first, True) if first_match.group(0)[0].islower() else (None, False)


def resolve_opcode(
    candidate: str,
    catalog: dict[str, list[Opcode]],
    implicit: set[str],
    imported: set[str],
) -> tuple[Opcode | None, str | None]:
    matches = catalog.get(candidate, [])
    if not matches:
        return None, "unknown opcode name"

    usable = [item for item in matches if item.extension in implicit or item.extension in imported]
    if len(usable) == 1:
        return usable[0], None
    if not usable:
        choices = ", ".join(f"{item.extension}:{item.opcode_id}" for item in matches)
        return None, f"opcode exists but its extension is not enabled ({choices})"
    choices = ", ".join(f"{item.extension}:{item.opcode_id}" for item in usable)
    return None, f"ambiguous opcode across enabled extensions ({choices})"


def validate_loops(path: Path, lines: list[tuple[int, str]]) -> list[Finding]:
    findings: list[Finding] = []
    stack: list[dict] = []

    for line_number, raw in lines:
        code = strip_comment(raw).strip()
        lower = code.lower()
        if not code:
            continue

        if re.match(r"^wait(?:\s|$)", lower):
            for block in stack:
                if block["kind"] in {"while", "repeat"}:
                    block["has_wait"] = True
        if lower == "break" or lower.startswith("break "):
            for block in reversed(stack):
                if block["kind"] in {"while", "repeat"}:
                    block["has_break"] = True
                    break

        if lower.startswith("repeat"):
            stack.append(
                {
                    "kind": "repeat",
                    "line": line_number,
                    "has_wait": False,
                    "has_break": False,
                    "requires_wait": True,
                }
            )
            continue
        if lower.startswith("while "):
            condition = lower[6:].strip()
            bounded = bool(re.search(r"(?:<|>|==|<>)", condition)) or condition.startswith(
                ("get_any_", "find_next_")
            )
            stack.append(
                {
                    "kind": "while",
                    "line": line_number,
                    "has_wait": False,
                    "has_break": False,
                    "requires_wait": not bounded,
                }
            )
            continue
        if lower.startswith(("if", "function ", "for ", "switch ")):
            stack.append({"kind": "block", "line": line_number})
            continue

        if lower.startswith("until "):
            for index in range(len(stack) - 1, -1, -1):
                if stack[index]["kind"] == "repeat":
                    block = stack.pop(index)
                    if not block["has_wait"]:
                        bounded = bool(re.search(r"(?:<|>|==|<>|find_next_)", lower))
                        severity = "WARNING" if bounded else "ERROR"
                        suffix = " (appears bounded; review manually)" if bounded else ""
                        findings.append(
                            Finding(severity, path, block["line"], f"repeat loop has no wait{suffix}")
                        )
                    break
            continue

        if lower == "end":
            if not stack:
                continue
            block = stack.pop()
            if (
                block["kind"] == "while"
                and block["requires_wait"]
                and not block["has_wait"]
            ):
                severity = "WARNING" if block["has_break"] else "ERROR"
                suffix = " (bounded by break; review manually)" if block["has_break"] else ""
                findings.append(
                    Finding(severity, path, block["line"], f"while loop has no wait{suffix}")
                )
    return findings


def validate_file(
    path: Path,
    catalog: dict[str, list[Opcode]],
    profile: dict,
) -> list[Finding]:
    findings: list[Finding] = []
    lines = source_lines(path)
    functions = declared_functions(lines)
    imported = imported_extensions(lines)
    implicit = set(profile["implicit_extensions"])
    max_name = profile["rules"]["script_name_max_length"]

    if path.suffix.lower() != ".md" and not any("{$CLEO" in raw.upper() for _, raw in lines):
        findings.append(Finding("ERROR", path, 1, "script is missing a {$CLEO ...} directive"))

    requested_models: dict[str, int] = {}
    released_models: set[str] = set()

    for line_number, raw in lines:
        code = strip_comment(raw).strip()
        if not code:
            continue

        script_name = re.match(
            r"script_name(?:\s+\{[^}]+\})?\s+['\"]([^'\"]+)['\"]",
            code,
            re.IGNORECASE,
        )
        if script_name and len(script_name.group(1)) > max_name:
            findings.append(
                Finding(
                    "ERROR",
                    path,
                    line_number,
                    f"script name '{script_name.group(1)}' exceeds {max_name} characters",
                )
            )

        request = re.match(
            r"request_model\s+(?:\{[^}]+\}\s+)?([#$A-Za-z0-9_.]+)",
            code,
            re.IGNORECASE,
        )
        if request:
            requested_models.setdefault(request.group(1).lower(), line_number)
        release = re.match(
            r"mark_model_as_no_longer_needed\s+(?:\{[^}]+\}\s+)?([#$A-Za-z0-9_.]+)",
            code,
            re.IGNORECASE,
        )
        if release:
            released_models.add(release.group(1).lower())

        if re.match(r"display_text(?:\s|$)", code, re.IGNORECASE) and re.search(
            r"(?:\{text\}\s*)?['\"]", code, re.IGNORECASE
        ):
            findings.append(
                Finding(
                    "ERROR",
                    path,
                    line_number,
                    "display_text expects a GXT key; use display_text_formatted for literals",
                )
            )

        candidate, command_shaped = invocation_candidate(code, catalog, functions)
        if not candidate:
            continue
        opcode, problem = resolve_opcode(candidate, catalog, implicit, imported)
        if problem:
            if command_shaped:
                findings.append(Finding("ERROR", path, line_number, f"{candidate}: {problem}"))
            continue
        assert opcode is not None
        if profile["rules"]["reject_unsupported_opcodes"] and opcode.attrs.get("is_unsupported"):
            findings.append(
                Finding(
                    "ERROR",
                    path,
                    line_number,
                    f"{opcode.name} ({opcode.opcode_id}) is marked unsupported",
                )
            )
        if profile["rules"]["reject_nop_opcodes"] and opcode.attrs.get("is_nop"):
            findings.append(
                Finding(
                    "ERROR",
                    path,
                    line_number,
                    f"{opcode.name} ({opcode.opcode_id}) is marked NOP",
                )
            )

    for model, line_number in requested_models.items():
        if model not in released_models:
            findings.append(
                Finding(
                    "ERROR",
                    path,
                    line_number,
                    f"requested model {model} is never marked as no longer needed",
                )
            )

    findings.extend(validate_loops(path, lines))
    return findings


def default_paths() -> list[Path]:
    paths = sorted((ROOT / "examples").glob("*.txt"))
    paths.extend(sorted((ROOT / "patterns").glob("*.md")))
    paths.extend(sorted((ROOT / "scripts").glob("*.txt")))
    return paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--profile", type=Path, default=DEFAULT_PROFILE)
    parser.add_argument("--catalog", type=Path, default=DEFAULT_CATALOG)
    parser.add_argument("--strict", action="store_true", help="treat warnings as errors")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        catalog = load_catalog(args.catalog)
        profile = load_json(args.profile)
    except (OSError, ValueError, KeyError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    paths = [path.resolve() for path in args.paths] if args.paths else default_paths()
    findings: list[Finding] = []
    for path in paths:
        if not path.is_file():
            findings.append(Finding("ERROR", path, 1, "file does not exist"))
            continue
        findings.extend(validate_file(path, catalog, profile))

    for finding in findings:
        print(finding.render())

    errors = sum(item.severity == "ERROR" for item in findings)
    warnings = sum(item.severity == "WARNING" for item in findings)
    print(f"Validated {len(paths)} files: {errors} error(s), {warnings} warning(s)")
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
