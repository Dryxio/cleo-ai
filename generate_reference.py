#!/usr/bin/env python3
"""
CLEO Reference Generator
Transforms Sanny Builder Library JSON + upstream docs into AI-friendly markdown reference files.

Usage:
    python3 generate_reference.py [path_to_sa.json] [path_to_enums.json] [path_to_docs_dir]

Defaults to looking in ./source_data/ for sa.json, enums.json, and docs/.
"""

import json
import sys
import os
from collections import defaultdict

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REF_DIR = os.path.join(SCRIPT_DIR, "reference")
CLASS_DIR = os.path.join(REF_DIR, "opcodes-by-class")

# Extensions that map to CLEO5 built-in plugins
CLEO_PLUGIN_EXTENSIONS = {
    "CLEO", "audio", "input", "text", "memory", "file", "math",
    "debug", "ini", "imgui", "bitwise", "clipboard", "Sphere"
}


def load_upstream_docs(docs_dir):
    """Load upstream documentation markdown files.

    Returns two dicts:
      - by exact name (case-sensitive)
      - by uppercase name (for case-insensitive fallback)
    """
    docs_exact = {}
    docs_upper = {}
    if not docs_dir or not os.path.isdir(docs_dir):
        return docs_exact, docs_upper

    for filename in os.listdir(docs_dir):
        if not filename.endswith(".md"):
            continue
        opcode_name = filename[:-3]  # strip .md
        filepath = os.path.join(docs_dir, filename)
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read().strip()
        except OSError as error:
            raise RuntimeError(f"Failed to read upstream documentation: {filepath}") from error
        if content:
            docs_exact[opcode_name] = content
            docs_upper[opcode_name.upper()] = content

    return docs_exact, docs_upper


# Global docs dicts, populated in main()
UPSTREAM_DOCS_EXACT = {}
UPSTREAM_DOCS_UPPER = {}

# Track which opcode IDs have already consumed a doc (prevents duplicate attachment)
DOCS_USED_BY = {}  # doc_name_upper -> first opcode_id that used it


def get_doc_for_opcode(name, opcode_id):
    """Get upstream doc for an opcode, with case-insensitive fallback and dedup."""
    upper = name.upper()

    # Check if this doc was already attached to a different opcode
    if upper in DOCS_USED_BY and DOCS_USED_BY[upper] != opcode_id:
        return None

    # Try exact match first, then case-insensitive
    content = UPSTREAM_DOCS_EXACT.get(name) or UPSTREAM_DOCS_UPPER.get(upper)
    if content:
        DOCS_USED_BY[upper] = opcode_id
    return content


def format_param(p):
    """Format a single parameter for display."""
    name = p.get("name", "")
    ptype = p.get("type", "any")
    source = p.get("source", "")

    parts = []
    if name:
        parts.append(f"{name}: {ptype}")
    else:
        parts.append(ptype)

    if source and source != "any":
        source_label = {
            "var_global": "global var",
            "var_local": "local var",
            "var_any": "variable",
            "literal": "literal"
        }.get(source, source)
        parts.append(f" ({source_label})")
    return "".join(parts)


def format_opcode_entry(cmd):
    """Format a single opcode as a markdown entry."""
    lines = []

    opcode_id = cmd["id"]
    name = cmd["name"]
    desc = cmd.get("short_desc", "")

    # Header line
    lines.append(f"### `{opcode_id}` {name}")
    if desc:
        lines.append(f"{desc}")
    lines.append("")

    # Class/member info
    cls = cmd.get("class", "")
    member = cmd.get("member", "")
    if cls and member:
        lines.append(f"**Class:** `{cls}.{member}`")

    # Operator
    op = cmd.get("operator", "")
    if op:
        lines.append(f"**Operator:** `{op}`")

    # Attributes
    attrs = cmd.get("attrs", {})
    flags = [k.replace("is_", "") for k, v in attrs.items() if v]
    if flags:
        lines.append(f"**Flags:** {', '.join(flags)}")

    # Input parameters
    inputs = cmd.get("input", [])
    if inputs:
        lines.append("")
        lines.append("**Input:**")
        for i, p in enumerate(inputs):
            lines.append(f"- `{format_param(p)}`")

    # Output parameters
    outputs = cmd.get("output", [])
    if outputs:
        lines.append("")
        lines.append("**Output:**")
        for p in outputs:
            lines.append(f"- `{format_param(p)}`")

    # Upstream detailed documentation (deduplicated, case-insensitive)
    doc_content = get_doc_for_opcode(name, opcode_id)
    if doc_content:
        lines.append("")
        lines.append("**Details:**")
        lines.append("")
        lines.append(doc_content)

    lines.append("")
    return "\n".join(lines)


def generate_class_files(commands_by_class):
    """Generate one markdown file per class."""
    os.makedirs(CLASS_DIR, exist_ok=True)

    generated_files = []
    for class_name, commands in sorted(commands_by_class.items()):
        filename = f"{class_name}.md"
        filepath = os.path.join(CLASS_DIR, filename)

        lines = [f"# {class_name} Opcodes", ""]
        lines.append(f"> {len(commands)} opcodes in this class")
        lines.append("")

        # Quick reference table
        lines.append("## Quick Reference")
        lines.append("")
        lines.append("| Opcode | Name | Description |")
        lines.append("|--------|------|-------------|")
        for cmd in commands:
            desc_short = cmd.get("short_desc", "")[:80]
            lines.append(f"| `{cmd['id']}` | {cmd['name']} | {desc_short} |")
        lines.append("")

        # Detailed entries
        lines.append("## Detailed Reference")
        lines.append("")
        for cmd in commands:
            lines.append(format_opcode_entry(cmd))
            lines.append("---")
            lines.append("")

        with open(filepath, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        generated_files.append((class_name, len(commands), filename))

    return generated_files


def generate_unclassed_file(commands):
    """Generate file for opcodes without a class."""
    if not commands:
        return None

    filepath = os.path.join(CLASS_DIR, "_General.md")

    lines = ["# General Opcodes (No Class)", ""]
    lines.append(f"> {len(commands)} opcodes — flow control, variables, comparisons, etc.")
    lines.append("")

    # Group by rough category based on name patterns
    categories = defaultdict(list)
    for cmd in commands:
        name = cmd["name"]
        if any(x in name for x in ["GOTO", "JUMP", "GOSUB", "RETURN", "IF", "ELSE"]):
            categories["Flow Control"].append(cmd)
        elif any(x in name for x in ["SET_VAR", "SET_LVAR", "ADD_VAL", "SUB_VAL", "MULT_VAL", "DIV_VAL"]):
            categories["Variable Operations"].append(cmd)
        elif any(x in name for x in ["IS_INT", "IS_FLOAT", "GREATER", "EQUAL"]):
            categories["Comparisons"].append(cmd)
        elif "STRING" in name or "TEXT" in name:
            categories["String Operations"].append(cmd)
        else:
            categories["Other"].append(cmd)

    for cat_name, cat_cmds in sorted(categories.items()):
        lines.append(f"## {cat_name}")
        lines.append("")
        for cmd in cat_cmds:
            lines.append(format_opcode_entry(cmd))
            lines.append("---")
            lines.append("")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return ("_General", len(commands), "_General.md")


def generate_extension_file(ext_name, commands):
    """Generate a file for a specific extension."""
    safe_name = ext_name.replace("+", "Plus").replace(" ", "_")
    filepath = os.path.join(REF_DIR, f"ext-{safe_name}.md")

    lines = [f"# {ext_name} Extension Opcodes", ""]
    lines.append(f"> {len(commands)} opcodes")
    lines.append("")

    # Quick reference table
    lines.append("## Quick Reference")
    lines.append("")
    lines.append("| Opcode | Name | Description |")
    lines.append("|--------|------|-------------|")
    for cmd in commands:
        desc_short = cmd.get("short_desc", "")[:80]
        lines.append(f"| `{cmd['id']}` | {cmd['name']} | {desc_short} |")
    lines.append("")

    # Detailed entries
    lines.append("## Detailed Reference")
    lines.append("")

    # Group by class within extension
    by_class = defaultdict(list)
    for cmd in commands:
        cls = cmd.get("class", "_General")
        by_class[cls].append(cmd)

    for cls_name, cls_cmds in sorted(by_class.items()):
        if cls_name != "_General":
            lines.append(f"### {cls_name}")
            lines.append("")
        for cmd in cls_cmds:
            lines.append(format_opcode_entry(cmd))
            lines.append("---")
            lines.append("")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return safe_name, len(commands)


def generate_enums(enums_data):
    """Generate enums reference file."""
    filepath = os.path.join(REF_DIR, "enums.md")

    lines = ["# CLEO Enums Reference", ""]
    lines.append(f"> {len(enums_data)} enum types")
    lines.append("")

    # Table of contents
    lines.append("## Index")
    lines.append("")
    for name in sorted(enums_data.keys()):
        count = len(enums_data[name])
        lines.append(f"- [{name}](#{name.lower()}) ({count} values)")
    lines.append("")

    # Each enum
    for name in sorted(enums_data.keys()):
        values = enums_data[name]
        lines.append(f"## {name}")
        lines.append("")
        lines.append("| Name | Value |")
        lines.append("|------|-------|")
        for val_name, val in values.items():
            val_display = str(val) if val is not None else "null"
            lines.append(f"| {val_name} | {val_display} |")
        lines.append("")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return len(enums_data)


    # NOTE: syntax-guide.md is maintained manually — no generate function here

def generate_opcode_index(all_commands, meta):
    """Generate a searchable opcode index with full descriptions."""
    filepath = os.path.join(REF_DIR, "opcode-index.md")

    # Sort by opcode ID
    sorted_cmds = sorted(all_commands, key=lambda c: c["_sort_id"])

    lines = ["# Opcode Index", ""]
    lines.append("Searchable index of all opcodes. Use Ctrl+F / grep to find opcodes by ID or name.")
    if meta:
        lines.append(
            f"Source: Sanny Builder Library `{meta.get('version', 'unknown')}`. "
            "See `reference/upstream-manifest.json` for the pinned commit."
        )
    lines.append("")
    lines.append("| Opcode | Name | Class | Extension | Params | Flags | Description |")
    lines.append("|--------|------|-------|-----------|--------|-------|-------------|")

    for cmd in sorted_cmds:
        opcode = cmd["id"]
        name = cmd["name"]
        cls = cmd.get("class", "")
        ext = cmd.get("_extension", "default")
        num_params = cmd.get("num_params", 0)
        attrs = cmd.get("attrs", {})
        flags = ", ".join(key.replace("is_", "") for key, value in attrs.items() if value)
        # Full description - no truncation. Pipe chars escaped for markdown table.
        desc = cmd.get("short_desc", "").replace("|", "\\|")
        lines.append(
            f"| `{opcode}` | {name} | {cls} | {ext} | {num_params} | {flags} | {desc} |"
        )

    lines.append("")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return len(sorted_cmds)


def main():
    global UPSTREAM_DOCS_EXACT, UPSTREAM_DOCS_UPPER

    # Resolve input paths
    source_dir = os.path.join(SCRIPT_DIR, "source_data")
    if len(sys.argv) >= 3:
        sa_path = sys.argv[1]
        enums_path = sys.argv[2]
        docs_dir = sys.argv[3] if len(sys.argv) >= 4 else os.path.join(source_dir, "docs")
    else:
        sa_path = os.path.join(source_dir, "sa.json")
        enums_path = os.path.join(source_dir, "enums.json")
        docs_dir = os.path.join(source_dir, "docs")

    print(f"Loading {sa_path}...")
    with open(sa_path, encoding="utf-8") as f:
        sa_data = json.load(f)

    print(f"Loading {enums_path}...")
    with open(enums_path, encoding="utf-8") as f:
        enums_data = json.load(f)

    # Load upstream detailed docs
    print(f"Loading upstream docs from {docs_dir}...")
    UPSTREAM_DOCS_EXACT, UPSTREAM_DOCS_UPPER = load_upstream_docs(docs_dir)
    print(f"  Loaded {len(UPSTREAM_DOCS_EXACT)} doc files")

    os.makedirs(CLASS_DIR, exist_ok=True)

    # Process all extensions
    # Process default extension FIRST so its opcodes claim docs before extensions
    # (prevents e.g. debug BREAKPOINT doc from attaching to default's nop BREAKPOINT)
    all_commands = []
    default_by_class = defaultdict(list)
    default_unclassed = []
    extension_files = []

    # Find default extension and process it first
    default_ext = None
    other_exts = []
    for ext in sa_data["extensions"]:
        if ext["name"] == "default":
            default_ext = ext
        else:
            other_exts.append(ext)

    # Process non-default extensions first so their specialized docs attach correctly
    for ext in other_exts:
        ext_name = ext["name"]
        commands = ext["commands"]

        for cmd in commands:
            cmd["_extension"] = ext_name
            cmd["_sort_id"] = cmd["id"]
            all_commands.append(cmd)

        info = generate_extension_file(ext_name, commands)
        extension_files.append((ext_name, info[1]))

    # Process default extension second (its generic opcodes won't steal specialized docs)
    if default_ext:
        for cmd in default_ext["commands"]:
            cmd["_extension"] = "default"
            cmd["_sort_id"] = cmd["id"]
            all_commands.append(cmd)

            cls = cmd.get("class")
            if cls:
                default_by_class[cls].append(cmd)
            else:
                default_unclassed.append(cmd)

    # Generate class files for default extension
    print("Generating class files...")
    class_files = generate_class_files(default_by_class)

    # Generate general (unclassed) file
    general_info = generate_unclassed_file(default_unclassed)

    # Generate enums
    print("Generating enums reference...")
    enum_count = generate_enums(enums_data)

    # Generate opcode index
    print("Generating opcode index...")
    index_count = generate_opcode_index(all_commands, sa_data.get("meta", {}))

    # NOTE: syntax-guide.md is maintained manually, not regenerated

    # Report unmatched docs
    matched = set(DOCS_USED_BY.keys())
    all_doc_names = set(UPSTREAM_DOCS_UPPER.keys())
    unmatched = all_doc_names - matched
    if unmatched:
        print(f"\n  Warning: {len(unmatched)} doc files had no matching opcode:")
        for name in sorted(unmatched):
            print(f"    {name}")

    # Print summary
    print(f"\n{'='*60}")
    print("GENERATION COMPLETE")
    print(f"{'='*60}")
    print(f"\nClass files ({len(class_files)} classes):")
    for name, count, fname in sorted(class_files):
        print(f"  {fname:<30} {count:>4} opcodes")
    if general_info:
        print(f"  {'_General.md':<30} {general_info[1]:>4} opcodes")

    print(f"\nExtension files ({len(extension_files)} extensions):")
    for name, count in sorted(extension_files):
        print(f"  ext-{name:<25} {count:>4} opcodes")

    print(f"\nEnums: {enum_count} types")
    print(f"Upstream docs merged: {len(DOCS_USED_BY)} entries (of {len(UPSTREAM_DOCS_EXACT)} available)")
    print(f"Total opcodes indexed: {index_count}")
    print(f"\nOutput directory: {REF_DIR}")


if __name__ == "__main__":
    main()
