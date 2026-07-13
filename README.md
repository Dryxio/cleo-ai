# cleo-ai

Create GTA San Andreas mods with AI.

This repo contains a generated opcode reference, compiler-backed validation workflow, examples, and reusable patterns — designed for AI coding assistants that must verify commands instead of guessing them.

## What's inside

| Folder | What it is |
|---|---|
| `reference/` | Full opcode reference (3,700+ opcodes), enums, syntax guide, and SDK docs |
| `examples/` | 20+ annotated example scripts (vehicle spawner, teleporter, skin selector, etc.) |
| `patterns/` | Reusable code patterns (main loop, cheat activation, screen drawing, etc.) |
| `scripts/` | Working scripts (car spawner, mission selector, noclip, time sync) |
| `config/` | Pinned GTA/CLEO/Sanny compatibility policy |
| `evals/` | Stable prompt suite for measuring AI first-pass quality |
| `tools/` | Upstream sync, static validation, and Sanny compilation commands |

## How it works

1. Ask the AI to write a CLEO script
2. It looks up the correct opcodes and parameters from `reference/`
3. It follows the syntax rules from `reference/syntax-guide.md`
4. Run `python3 tools/validate_workspace.py scripts/your_script.txt`
5. Compile the script with Sanny Builder 4 and drop the `.cs` into your CLEO folder

The default profile targets GTA SA PC 1.0, CLEO 5.4, and the plugins bundled with CLEO 5. Third-party extensions such as CLEO+, NewOpcodes, SAMPFUNCS, and ImGui must be explicitly enabled and declared as dependencies.

## Requirements

- [CLEO 5](https://cleo.li/) installed in your GTA San Andreas directory
- [Sanny Builder 4](https://sannybuilder.com/) to compile `.txt` scripts into `.cs`

## Updating the reference

The reference is generated from a pinned commit of the [Sanny Builder Library](https://github.com/sannybuilder/library). The first command is reproducible from a clean clone; the second intentionally updates the pin.

```bash
python3 tools/sync_reference.py
python3 tools/sync_reference.py --latest
```

## Validation

```bash
python3 -m unittest discover -s tests -v
python3 tools/validate_workspace.py
python3 tools/opcode_lookup.py search "vehicle coordinates"
python3 tools/opcode_lookup.py show CREATE_CAR
```

On Windows, compile all sources with a local Sanny Builder installation:

```powershell
./tools/compile_all.ps1 -SannyRoot C:\Tools\SannyBuilder
```

GitHub Actions validates the pinned reference snapshot, runs the static checks, and compiles sources that do not depend on game-directory model aliases using the pinned Sanny Builder archive.

## AI quality benchmark

`evals/prompts.json` contains a stable set of generation tasks covering ordinary scripts, resource cleanup, extension declarations, and deliberately unsupported requests. Score generated scripts by validator success, first-pass compilation, one-repair compilation, and the manual runtime checks described in `evals/README.md`.
