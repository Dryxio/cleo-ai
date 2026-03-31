# cleo-ai

Create GTA San Andreas mods with AI. Write CLEO5 scripts using an AI coding assistant instead of memorizing thousands of opcodes.

This repo gives AI models (like Claude) everything they need to generate working CLEO scripts — a full opcode reference, annotated examples, and reusable patterns. You describe what you want, the AI writes the code.

## What's inside

| Folder | What it is |
|---|---|
| `reference/` | Full opcode reference (3,700+ opcodes), enums, syntax guide, and SDK docs |
| `examples/` | 20+ annotated example scripts (vehicle spawner, teleporter, skin selector, etc.) |
| `patterns/` | Reusable code patterns (main loop, cheat activation, screen drawing, etc.) |
| `scripts/` | Working scripts (car spawner, mission selector, noclip, time sync) |

## How it works

1. Open this repo with an AI coding assistant (Claude Code, Cursor, etc.)
2. Describe what you want — spawn vehicles, teleport, draw on screen, custom missions, anything
3. The AI looks up the correct opcodes, parameters, and enums from the reference
4. Compile the output with Sanny Builder 4 and drop the `.cs` into your CLEO folder

No need to dig through opcode lists or memorize parameter orders. The AI handles that.

## Requirements

- [CLEO 5](https://cleo.li/) installed in your GTA San Andreas directory
- [Sanny Builder 4](https://sannybuilder.com/) to compile `.txt` scripts into `.cs`

## Updating the reference

The reference is generated from the [Sanny Builder Library](https://github.com/sannybuilder/library):

```bash
python3 generate_reference.py
```
