# cleo-ai

AI-assisted workspace for writing CLEO5 scripts for GTA San Andreas.

This repo contains a complete opcode reference, examples, and reusable patterns — designed to be used with an AI coding assistant (like Claude) that can look up opcodes, check parameter signatures, and generate correct scripts.

## What's inside

| Folder | What it is |
|---|---|
| `reference/` | Full opcode reference (3,700+ opcodes), enums, syntax guide, and SDK docs |
| `examples/` | 20+ annotated example scripts (vehicle spawner, teleporter, skin selector, etc.) |
| `patterns/` | Reusable code patterns (main loop, cheat activation, screen drawing, etc.) |
| `scripts/` | Working scripts (car spawner, mission selector, noclip, time sync) |

## How it works

1. Ask the AI to write a CLEO script
2. It looks up the correct opcodes and parameters from `reference/`
3. It follows the syntax rules from `reference/syntax-guide.md`
4. Compile the script with Sanny Builder 4 and drop the `.cs` into your CLEO folder

## Requirements

- [CLEO 5](https://cleo.li/) installed in your GTA San Andreas directory
- [Sanny Builder 4](https://sannybuilder.com/) to compile `.txt` scripts into `.cs`

## Updating the reference

The reference is generated from the [Sanny Builder Library](https://github.com/sannybuilder/library):

```bash
python3 generate_reference.py
```
