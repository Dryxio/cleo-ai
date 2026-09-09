# CLEO AI

Create GTA San Andreas mods with your AI.

This repo contains a generated opcode reference, compiler-backed validation workflow, examples, and reusable patterns — designed for AI coding assistants that must verify commands instead of guessing them.

## Get started with your AI

**Give your AI this repo and tell it what you want to do.** It can check your setup, install the tools it needs, and walk you through anything that needs your help.

**Before you start:** this is a free tool for an AI coding agent. Your agent must be able to read and write files and run commands on your computer. A chat that only gives you instructions cannot complete the workflow for you. Your AI provider may charge separately.

Copy this into your agent:

> Help me set up https://github.com/Dryxio/cleo-ai. Read the README and agent guide, check my GTA San Andreas version and installed tools, and help me set up the required CLEO and Sanny Builder versions. Then make a simple mod that spawns a car near the player when I press F5. Check the script, compile it, and show me how to install and try it in game.

You'll need your own GTA San Andreas PC 1.0 installation. The default setup uses CLEO 5.4 and Sanny Builder 4; your agent can check compatibility before getting started.

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

## Manual setup

Prefer to install it yourself? Expand the instructions below.

<details>
<summary>Manual installation, configuration and examples</summary>

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

</details>

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
