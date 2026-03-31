# CLEO5 Script Development Workspace

You are assisting with writing CLEO scripts for GTA San Andreas using CLEO5 and Sanny Builder 4 syntax.

## Critical Rules

1. **NEVER guess opcodes.** Before using ANY opcode, verify it exists by searching `reference/opcode-index.md`. If you cannot find it, tell the user rather than making one up.
2. **ALWAYS check parameter signatures.** After finding an opcode in the index, read the detailed entry in the appropriate file (class file under `reference/opcodes-by-class/` for default opcodes, or `reference/ext-{name}.md` for extension opcodes) to get exact parameter names, types, and order.
3. **Prefer named parameters for clarity.** Sanny Builder 4 supports `{paramName} value` format: `wait {time} 1000`. Positional syntax (`wait 1000`) is also valid and commonly used for simple opcodes.
4. **Every loop MUST contain `wait {time} 0`** (or higher). Loops without wait will freeze the game.
5. **Always clean up models.** After `request_model` + `load_all_models_now`, always call `mark_model_as_no_longer_needed` when done.
6. **Use enums, not magic numbers.** Check `reference/enums.md` for the correct enum values (e.g., `Fade.Out` not `0`, `Font.Menu` not `1`).
   - In raw comparisons and assignments, prefer the verified numeric value if the enum form triggers a parser error (for example `pedTypeId == 6 // PedType.Cop`).
7. **Prefer parser-safe syntax over compact syntax.** If an expression can be written either as one dense line or as 2-4 simple lines with temporaries, prefer the simpler form.
8. **Keep function state explicit.** When helper functions need to update coordinates, counters, or handles, prefer parameters and return values over assigning to script-level variables from inside the function body.
9. **Keep local arrays small.** Large arrays can exceed CLEO's local-variable budget for a scope. If you need more storage, use a smaller fixed buffer or memory-backed storage instead of a large local array.

## How to Look Things Up

### Finding an opcode
1. Search `reference/opcode-index.md` for the opcode name or ID
2. The index tells you which **class** and **extension** it belongs to
3. Read the detailed file:
   - If the Extension column is `default` and Class is filled: read `reference/opcodes-by-class/{ClassName}.md`
   - If the Extension column is `default` and Class is blank: read `reference/opcodes-by-class/_General.md`
   - If the Extension column is anything else (CLEO, audio, file, input, etc.): read `reference/ext-{ExtensionName}.md` (note: CLEO+ maps to `ext-CLEOPlus.md`)

### Finding opcodes by category
- Vehicle operations: `reference/opcodes-by-class/Car.md`
- Character/ped operations: `reference/opcodes-by-class/Char.md`
- Player-specific: `reference/opcodes-by-class/Player.md`
- Camera control: `reference/opcodes-by-class/Camera.md`
- World/environment: `reference/opcodes-by-class/World.md`
- Math functions: `reference/opcodes-by-class/Math.md`
- HUD/display: `reference/opcodes-by-class/Hud.md` and `reference/opcodes-by-class/Text.md`
- Audio: `reference/opcodes-by-class/Audio.md` and `reference/ext-audio.md`
- Objects: `reference/opcodes-by-class/Object.md`
- Tasks/AI: `reference/opcodes-by-class/Task.md`
- Game state: `reference/opcodes-by-class/Game.md`
- Flow control / variables / comparisons: `reference/opcodes-by-class/_General.md`

### CLEO-specific opcodes (0A8C+)
- Core CLEO: `reference/ext-CLEO.md` (memory ops, script loading, dynamic libraries)
- CLEO+: `reference/ext-CLEOPlus.md` (extended opcodes)
- File I/O: `reference/ext-file.md`
- Input: `reference/ext-input.md`
- Audio: `reference/ext-audio.md`
- Text/drawing: `reference/ext-text.md`
- Memory: `reference/ext-memory.md`
- Math: `reference/ext-math.md`
- Debug: `reference/ext-debug.md`
- INI files: `reference/ext-ini.md`
- ImGui: `reference/ext-imgui.md`

### Enum values
- All enums: `reference/enums.md`
- Common ones: `WeaponType`, `PedType`, `KeyCode`, `Font`, `Fade`, `BlipColor`, `CameraMode`, `SwitchType`, `AudioStreamAction`, `BodyPart`, `PickupType`

### Script syntax
- Full syntax reference: `reference/syntax-guide.md`

### SDK/Plugin development
- C++ SDK API: `reference/sdk-api.md`

## Workspace Structure

```
cleo-workspace/
├── CLAUDE.md                    # This file (read first)
├── reference/
│   ├── opcode-index.md          # Searchable index of ALL 3,739 opcodes
│   ├── syntax-guide.md          # CLEO script syntax reference
│   ├── enums.md                 # All 158 enum types with values
│   ├── sdk-api.md               # C++ SDK for plugin developers
│   ├── ext-CLEO.md              # CLEO core extension opcodes
│   ├── ext-CLEOPlus.md          # CLEO+ extension opcodes
│   ├── ext-*.md                 # Other extension opcodes
│   └── opcodes-by-class/        # Opcodes organized by class
│       ├── Car.md               # 196 vehicle opcodes
│       ├── Char.md              # 252 character/ped opcodes
│       ├── Player.md            # 66 player opcodes
│       ├── Camera.md            # 51 camera opcodes
│       ├── Object.md            # 87 object opcodes
│       ├── Task.md              # 97 AI task opcodes
│       ├── World.md             # 65 world opcodes
│       ├── Text.md              # 59 text opcodes
│       ├── Math.md              # 38 math opcodes
│       ├── _General.md          # 1,173 general opcodes (flow, vars, comparisons)
│       └── ... (62 class files total)
├── examples/                    # Annotated example scripts
├── patterns/
│   └── common_patterns.md       # 20 reusable code patterns
├── scripts/                     # User's working scripts go here
├── source_data/                 # Raw JSON source (sa.json, enums.json)
└── generate_reference.py        # Regenerate reference from JSON
```

## Script File Format

CLEO scripts use Sanny Builder 4 syntax:
- File extension: `.cs` (custom script) or `.cm` (custom mission)
- Scripts start with `{$CLEO .cs}` directive
- Named parameters (preferred): `opcode_name {paramName} value` — positional also valid
- See `reference/syntax-guide.md` for complete syntax

## Workspace-Specific Pitfalls

These are common real-world issues in this workspace and toolchain.

1. **Model aliases may not compile on every machine.**
   - Syntax like `#INFERNUS` depends on Sanny Builder being correctly configured with a GTA SA game directory/library.
   - If alias lookup fails, use numeric model IDs instead (for example `411` for Infernus).
2. **Some identifier names are best avoided.**
   - Short names like `car` can collide with reserved words, classes, or parser expectations depending on context.
   - Prefer explicit handles like `carHandle`, `vehicleHandle`, `pedHandle`, `modelId`.
3. **`display_text` is for GXT keys, not arbitrary inline strings.**
   - For literal text or formatted strings, prefer `display_text_formatted`, `print_help_formatted`, or `print_help_string`.
4. **Input-confirm keys can conflict with the game itself.**
   - Avoid using keys like `Enter` for menu confirmation when the action also affects vehicles.
   - Prefer dedicated keys like `E`, `F5`, or another non-conflicting bind.
5. **Vehicle/menu scripts often need explicit camera reset after warp/spawn.**
   - After moving the player between vehicles, `restore_camera_jumpcut` and/or `set_camera_behind_player` may be needed.
6. **The full vehicle range `400..611` includes special cases.**
   - That range contains normal cars, bikes, boats, planes, trains, trailers, and RC-style vehicles.
   - A generic `create_car` menu can browse all of them, but some entries will behave oddly at runtime.
7. **Sanny's parser is stricter than the syntax tables imply.**
   - Operators like `+=` and `-=` are documented, but dense forms such as `x += y * 0.5` may still fail depending on context.
   - Prefer:
     `tmp = y`
     `tmp *= 0.5`
     `x += tmp`
8. **Multi-return assignment is safest with local variables.**
   - Patterns like `x, y, z = get_char_coordinates $scplayer` are fine for locals declared in the same scope.
   - If you need to persist those values across helper calls, store them in locals first and return them explicitly from functions.
9. **Refactors that change helper signatures must be followed by call-site checks.**
   - After changing a function's parameters or return values, search the workspace for every call site before considering the edit done.
   - A practical pattern is to `rg` the function name immediately after the change.
10. **Helper functions do not reliably share outer local state.**
   - A helper may compile-fail if it reads or writes locals declared in the main script scope.
   - Pass counters, handles, and coordinates as parameters, or keep the stateful loop inline in the main body.
11. **Enums are less reliable in raw expressions than in opcode parameters.**
   - Forms like `set_text_font {font} Font.Menu` are usually fine.
   - Forms like `myValue == PedType.Cop` can fail in some parser contexts; use the verified numeric value there if needed.
12. **Large local arrays can fail at compile time even when syntax is correct.**
   - Errors like `Not enough memory to allocate a local variable ...` usually mean the scope exceeded the local-variable budget, not that the array syntax itself is wrong.

## AI-Specific Workflow Rules

These rules are aimed at agents working without a live compiler or runtime.

1. **Bias toward simple statements.**
   - Prefer one operation per line over compound expressions inside assignments or conditions.
2. **Prefer pure-ish helper functions.**
   - A helper that takes values and returns updated values is safer than a helper that mutates outer script state.
3. **Use local temporaries for opcode outputs.**
   - Especially for multi-return opcodes and formatted string building.
4. **Treat parser errors as syntax/shape problems first.**
   - Errors like `Unknown directive ...`, `Too many actual parameters ...`, and `Not enough actual parameters ...` often mean the line shape confused the parser rather than the opcode being missing.
5. **After any signature change, re-scan call sites.**
   - This catches stale no-arg or wrong-arg calls before the next compile.
6. **When in doubt, mirror existing examples.**
   - If a pattern already appears in `examples/` or `scripts/`, prefer the documented house style over a novel but denser construction.
7. **Treat scope-related compile errors literally.**
   - Errors such as `Function X is not found in the current scope` after referencing a variable inside a helper often mean the parser rejected an outer local in that scope.
8. **Treat local-memory errors as storage-shape problems first.**
   - If a local array declaration fails, reduce the buffer size or redesign the storage before questioning the opcode logic.

## Examples and Patterns

- See `examples/` for complete working scripts
- See `patterns/common_patterns.md` for reusable code snippets
- Key patterns: main loop, cheat activation, vehicle spawn, vehicle menu, teleport, screen drawing, audio

## Common Mistakes to Avoid

1. Using opcodes that don't exist (always verify in opcode-index.md)
2. Wrong parameter order (always check the class reference file)
3. Forgetting `wait` in loops (game will freeze)
4. Not loading models before using them (`request_model` + `load_all_models_now`)
5. Not cleaning up models (`mark_model_as_no_longer_needed`)
6. Using wrong variable types (int vs float - some opcodes are type-specific)
7. Forgetting `{$CLEO .cs}` header
8. Script names longer than 8 characters
9. Using magic numbers instead of enum values
10. Not checking `is_player_playing` before player operations
11. Assuming model aliases like `#INFERNUS` will always resolve
12. Using `display_text` for raw strings instead of `display_text_formatted`
13. Reusing gameplay keys like `Enter` for menu confirmation in vehicle scripts
14. Writing dense arithmetic like `x += y * speed` when a temporary variable would be parser-safer
15. Mutating script-level state from helper functions when parameters/returns would be clearer
16. Refactoring a helper signature without updating every call site
17. Using enum members directly in raw comparisons when the parser only accepts the numeric value in that context
18. Allocating oversized local arrays in a single scope

## Updating the Reference

To regenerate reference files from the latest Sanny Builder Library data:

```bash
# Update source_data/sa.json and enums.json from:
# https://github.com/sannybuilder/library/tree/master/sa
# Then run:
python3 generate_reference.py
```
