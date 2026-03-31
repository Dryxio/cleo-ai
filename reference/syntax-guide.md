# CLEO Script Syntax Guide (Sanny Builder 4)

## File Structure

```
// Header comment
{$CLEO .cs}                    // File type directive (.cs = custom script, .cm = custom mission)

script_name {name} 'mymod'     // Script identifier (max 8 chars)

// Global declarations
const
    MY_CONST = 100
end

// Main logic
wait {time} 0                  // Must wait at least once to let game initialize

while true
    wait {time} 0
    // ... script logic ...
end

terminate_this_custom_script
```

## File Type Directives

| Directive | Extension | Description |
|-----------|-----------|-------------|
| `{$CLEO .cs}` | .cs | Custom script — runs continuously in background |
| `{$CLEO .cm}` | .cm | Custom mission — runs as a mission, one at a time |
| `{$CLEO .cs3}` | .cs3 | Legacy CLEO3 compatibility mode |
| `{$CLEO .cs4}` | .cs4 | Legacy CLEO4 compatibility mode |

## Extension Imports

Use `{$USE}` to import extension libraries (required for their opcodes):

```
{$CLEO .cs}
{$USE CLEO+}               // Import CLEO+ extension opcodes
```

## Variable Types

```
int myVar              // 32-bit integer
float myFloat          // 32-bit float
string myStr           // Short string (8 chars)
longstring myLong      // Long string (16 chars)
int myArray[10]        // Array of 10 ints
```

Use `longString` when storing vehicle names, filenames, or other text returned by opcodes.

## Named Parameters

Sanny Builder 4 supports named parameters with curly braces for clarity. Both forms are valid:

```
// Named parameters (preferred — makes code self-documenting)
wait {time} 1000
create_player {id} 0 {pos} 100.0 200.0 10.0
set_text_colour {rgb} 255 0 0 {alpha} 255

// Positional parameters (also valid — common in simple opcodes)
wait 1000
wait 0
```

## Control Flow

### If/Then/Else
```
if
    condition_opcode args
then
    // true branch
else
    // false branch (optional)
end
```

### Compound Conditions
```
if and                         // ALL conditions must be true
    condition1
    condition2
then
    // ...
end

if or                          // ANY condition must be true
    condition1
    condition2
then
    // ...
end
```

### Negation
```
if
    not is_player_playing $player1
then
    // player is NOT playing
end
```

### While Loop
```
while true
    wait {time} 0              // MUST have wait in loops to prevent freeze
    // ...
end
```

### Repeat/Until
```
repeat
    wait {time} 0
until condition_opcode args
```

### For Loop
```
int i
for i = 0 to 10
    // i goes from 0 to 10 inclusive
end

// With step
for i = 10 to 0 step -1
    // countdown
end
```

### Switch/Case
```
switch myVar
    case 0
        // handle case 0
    case 1
        // handle case 1
    default
        // handle all other values
end
```

### Labels and Goto
```
goto @MY_LABEL

// ... other code ...

:MY_LABEL
// execution continues here
```

### Break and Continue
```
while true
    wait 0

    if
        some_condition
    then
        continue       // skip to next iteration
    end

    if
        done_condition
    then
        break          // exit the loop
    end
end
```

### Logical Return Type
Functions can declare `logical` return type to be used as conditions:
```
function IS_NEAR_LOCATION(x: float, y: float): logical
    if
        locate_char_any_means_2d $scplayer {pos} x y {radius} 5.0 5.0 {drawSphere} false
    then
        cleo_return_with {conditionResult} true
    else
        cleo_return_with {conditionResult} false
    end
end
```

## Functions (CLEO5+)

### Basic function with single return
```
function MY_FUNC(param1: int, param2: float): int
    // function body
    return someValue
end

// Call
int result = MY_FUNC(42, 3.14)
```

### Void function (no return)
```
function DO_SOMETHING(x: float, y: float)
    // ...
end
DO_SOMETHING(1.0, 2.0)
```

### Safer input debounce pattern

For menu/input scripts, inlining the release wait is often more reliable than wrapping it in a helper:

```
if
    is_key_pressed {keyCode} KeyCode.F5
then
    // handle key press once
    while is_key_pressed {keyCode} KeyCode.F5
        wait {time} 0
    end
end
```

### Multiple return values
```
function GET_POOL_INFO(address: int): int, int
    int used = read_memory {address} address {size} 4 {vp} false
    int total = read_memory {address} address + 4 {size} 4 {vp} false
    return used total              // return values separated by spaces
end

// Call — assign to multiple variables (comma-separated)
int used, total
used, total = GET_POOL_INFO(0xB74490)
```

### Script-level state vs function-local state

For parser reliability, prefer moving changing state through function parameters and return values instead of mutating outer script variables from inside helpers.

Safer pattern:

```
float posX = 0.0
float posY = 0.0

posX, posY = UPDATE_POS(posX, posY)

function UPDATE_POS(x: float, y: float): float, float
    x += 1.0
    y += 2.0
    return x y
end
```

When you need opcode outputs, store them into locals first:

```
function READ_PLAYER_POS(): float, float, float
    float x, y, z
    x, y, z = get_char_coordinates $scplayer
    return x y z
end
```

This shape is usually more robust than trying to assign directly into outer script variables from inside the helper.

### Conditional return with cleo_return_with
Functions can return a condition result (true/false) along with values. This is used when
a function can fail and the caller needs to check success:

```
function TRY_LOAD_STREAM(path: string): int
    int stream
    if
        stream = load_audio_stream path
    then
        cleo_return_with {conditionResult} true {retArgs} stream
    else
        cleo_return_with {conditionResult} false {retArgs} -1
    end
end

// Call — use in if/then to check success
int myStream
if
    myStream = TRY_LOAD_STREAM("cleo\sound.mp3")
then
    // success, myStream is valid
else
    // failed to load
end
```

### External function declarations (calling game functions directly)
```
// Declare a game function by address with calling convention
function CModelInfo__GetModelInfo<cdecl, 0x00403DA0>(modelIdx: int): int

// Call it like any other function
int info = CModelInfo__GetModelInfo(400)
```

Supported calling conventions: `cdecl`, `stdcall`, `thiscall`, `method`.

### Function Call Edge Cases

These patterns are valid in theory but can still be parser traps in practice depending on how the call is written:

1. Passing enums into your own helper functions can be less robust than passing literal ints or inlining the logic.
2. For input handling, prefer direct `is_key_pressed` checks and inline release loops.
3. When storing strings returned by an opcode, declare the destination first, then assign to it on a separate line.

Example:

```
longString vehicleName = ""
vehicleName = get_name_of_vehicle_model {modelId} modelId
```

4. Use `display_text` only with GXT keys. For arbitrary text, use formatted text commands:

```
display_text_formatted {pos} 320.0 120.0 {format} "Model ID: %d" {args} modelId
display_text_formatted {pos} 320.0 140.0 {format} "%s" {args} vehicleName
```

5. When a helper's signature changes, re-check every call site immediately. Sanny compile errors often surface at the stale caller rather than the function definition.

## Parser Pitfalls

The language supports compact syntax, but parser-safe code is often more verbose.

### Prefer temporaries for arithmetic

Documented operators such as `+=` and `-=` are safest with simple right-hand values.

Safer:

```
float stepX = forwardX
stepX *= moveStep
moveX += stepX
```

Riskier:

```
moveX += forwardX * moveStep
```

If a dense arithmetic line throws parameter-count or directive errors, rewrite it into simple assignments first.

### Prefer locals for multi-return assignment

This pattern is known-good:

```
float x, y, z
x, y, z = get_char_coordinates $scplayer
```

If you need to preserve those values across helper calls, return them from the helper instead of relying on direct mutation of outer state.

### Keep function responsibilities narrow

Helpers that only:
- read values,
- compute values,
- return values

are usually easier for Sanny to parse and easier to refactor safely than helpers that both mutate outer state and perform gameplay opcodes.

## Error Cookbook

These compile errors are often parser-shape problems rather than missing opcodes.

### `Unknown directive ...`

Usually means the current line was not parsed as a valid opcode or assignment.

Common causes:
- assigning to a name that is not valid in that scope
- using a line shape the parser does not accept in that context
- carrying over an old variable name after a refactor

First response:
- compare the line against an existing example
- simplify it into smaller statements
- move values through locals or function returns

### `Too many actual parameters. Expected N params.`

Usually means the parser interpreted a dense expression as a call with extra arguments.

Common causes:
- compound arithmetic on the right-hand side of `+=`, `-=`, `*=`, `/=`
- a helper call written in a context the parser does not like

First response:
- break the expression into temporaries
- verify whether the failing line is truly the opcode line or just the next line after a malformed one

### `Not enough actual parameters. Expected N params.`

Usually means the call site no longer matches the helper or opcode signature.

Common causes:
- refactored helper signature with stale callers
- named-parameter grouping that does not match the opcode's true arity
- calling a helper without passing the state it now expects

First response:
- check the function definition
- search all call sites
- compare against the opcode reference signature

## Operators

| Operator | Example | Description |
|----------|---------|-------------|
| `=` | `x = 5` | Assignment |
| `+=` | `x += 1` | Add |
| `-=` | `x -= 1` | Subtract |
| `*=` | `x *= 2` | Multiply |
| `/=` | `x /= 2` | Divide |
| `=#` | `x =# y` | Cast int to float |
| `+=@` | `x +=@ y` | FPS-consistent addition (delta-time) |
| `-=@` | `x -=@ y` | FPS-consistent subtraction |

## Comparison Operators

| Operator | Description |
|----------|-------------|
| `==` | Equal |
| `<>` | Not equal |
| `>` | Greater than |
| `>=` | Greater or equal |
| `<` | Less than |
| `<=` | Less or equal |

## Special Variables

| Variable | Description |
|----------|-------------|
| `$player1` | Player handle (global) |
| `$scplayer` | Player character (ped) handle |
| `TimerA` | Auto-incrementing timer A (milliseconds) |
| `TimerB` | Auto-incrementing timer B (milliseconds) |

## Constants and Enums

```
// Using enum values
set_text_font {font} Font.Menu
do_fade {time} 500 {direction} Fade.Out

// Using model names (requires Sanny Builder / GTA SA library setup)
request_model #INFERNUS
request_model #M4

// Numeric model IDs are the fallback when aliases don't resolve
request_model 411         // Infernus

// Hex values
write_memory {address} 0x006D5410 {size} 1 {value} 0xFF {vp} false
```

## Text Drawing Notes

```
// GXT key
display_text {pos} 320.0 120.0 {text} "M_PASS_1"

// Arbitrary inline text
display_text_formatted {pos} 320.0 140.0 {format} "Vehicle Spawner"

// Arbitrary inline text with arguments
display_text_formatted {pos} 320.0 160.0 {format} "Vehicle %d / 212" {args} index
```

Use `display_text_formatted` by default unless you intentionally want a GXT entry.

## Common Patterns

### Wait for Game Load
```
wait {time} 0
wait {time} 0
```

### Safe Loop Pattern
```
while true
    wait {time} 0              // CRITICAL: always wait in loops
    // logic here
end
```

### Model Loading Pattern
```
request_model #INFERNUS
load_all_models_now
// ... use model ...
mark_model_as_no_longer_needed #INFERNUS
```

### Screen Coordinate System
- Screen width: 640.0 (left=0, right=640)
- Screen height: 448.0 (top=0, bottom=448)
- Origin: top-left corner

## Script Naming Convention
- Script names are max 8 characters (internal buffer is `char Name[8]`)
- Use lowercase abbreviations
- Examples: `mymod`, `train_sp`, `pckp_cl`, `homiehlp`
