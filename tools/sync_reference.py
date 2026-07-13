#!/usr/bin/env python3
"""Fetch a pinned Sanny Builder Library snapshot and regenerate references.

By default this script uses the commit recorded in
reference/upstream-manifest.json, making clean-clone regeneration reproducible.
Use --latest only when intentionally updating the pinned snapshot.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "reference" / "upstream-manifest.json"
SOURCE_DIR = ROOT / "source_data"
DEFAULT_REPOSITORY = "https://github.com/sannybuilder/library.git"


def run(*args: str, cwd: Path | None = None) -> str:
    result = subprocess.run(
        args,
        cwd=cwd,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.strip()


def load_manifest() -> dict:
    if not MANIFEST_PATH.exists():
        return {}
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def clone_repository(repository: str, ref: str, destination: Path) -> Path:
    run("git", "clone", "--quiet", "--filter=blob:none", repository, str(destination))
    if ref != "HEAD":
        try:
            run("git", "checkout", "--quiet", ref, cwd=destination)
        except subprocess.CalledProcessError:
            run("git", "fetch", "--quiet", "--depth", "1", "origin", ref, cwd=destination)
            run("git", "checkout", "--quiet", "FETCH_HEAD", cwd=destination)
    return destination


def copy_sources(library_root: Path) -> dict:
    upstream_sa = library_root / "sa"
    sa_path = upstream_sa / "sa.json"
    enums_path = upstream_sa / "enums.json"
    docs_path = upstream_sa / "docs"
    if not sa_path.is_file() or not enums_path.is_file() or not docs_path.is_dir():
        raise RuntimeError(f"Not a Sanny Builder Library checkout: {library_root}")

    data = json.loads(sa_path.read_text(encoding="utf-8"))
    SOURCE_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(sa_path, SOURCE_DIR / "sa.json")
    shutil.copy2(enums_path, SOURCE_DIR / "enums.json")

    destination_docs = SOURCE_DIR / "docs"
    if destination_docs.exists():
        shutil.rmtree(destination_docs)
    shutil.copytree(docs_path, destination_docs)
    return data


def write_manifest(library_root: Path, repository: str, data: dict) -> None:
    commit = run("git", "rev-parse", "HEAD", cwd=library_root)
    commit_date = run("git", "show", "-s", "--format=%cI", "HEAD", cwd=library_root)
    meta = data.get("meta", {})
    manifest = {
        "repository": repository,
        "commit": commit,
        "commit_date": commit_date,
        "game": "sa",
        "library_version": meta.get("version"),
        "library_last_update": meta.get("last_update"),
    }
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--latest",
        action="store_true",
        help="update from the repository's current default branch and repin it",
    )
    parser.add_argument("--ref", help="specific branch, tag, or commit to use")
    parser.add_argument(
        "--source",
        type=Path,
        help="use an existing local Sanny Builder Library checkout",
    )
    parser.add_argument("--no-generate", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    pinned = load_manifest()
    repository = pinned.get("repository", DEFAULT_REPOSITORY)

    if args.ref:
        ref = args.ref
    elif args.latest:
        ref = "HEAD"
    else:
        ref = pinned.get("commit")
        if not ref:
            print("No pinned commit found; pass --latest or --ref.", file=sys.stderr)
            return 2

    with tempfile.TemporaryDirectory(prefix="cleo-reference-") as tmp:
        if args.source:
            library_root = args.source.resolve()
        else:
            library_root = clone_repository(repository, ref, Path(tmp) / "library")

        data = copy_sources(library_root)
        write_manifest(library_root, repository, data)

    if not args.no_generate:
        subprocess.run([sys.executable, str(ROOT / "generate_reference.py")], check=True)

    manifest = load_manifest()
    print(
        "Synced Sanny Builder Library "
        f"{manifest.get('library_version')} at {manifest.get('commit', '')[:12]}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
