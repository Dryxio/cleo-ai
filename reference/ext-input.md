# input Extension Opcodes

> 7 opcodes

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `2080` | IS_KEY_JUST_PRESSED | Returns true if the player has just started to press a specified key this frame |
| `2081` | GET_KEY_PRESSED_IN_RANGE | Gets code of first currently hold down key in range between minKeyCode and maxKe |
| `2082` | GET_KEY_JUST_PRESSED_IN_RANGE | Gets code of first just pressed key in range between minKeyCode and maxKeyCode.  |
| `2083` | EMULATE_KEY_PRESS | Simulates key press event |
| `2084` | EMULATE_KEY_RELEASE | Simulates key release event |
| `2085` | GET_CONTROLLER_KEY | Returns n-th alternate key assigned to pad's action. If no key is bound then ret |
| `2086` | GET_KEY_NAME | Returns keyboard/mouse key name text of specified keyCode. If key code has no na |

## Detailed Reference

### Pad

### `2080` IS_KEY_JUST_PRESSED
Returns true if the player has just started to press a specified key this frame

**Class:** `Pad.IsKeyJustPressed`
**Flags:** static, condition

**Input:**
- `keyCode: KeyCode`

---

### `2081` GET_KEY_PRESSED_IN_RANGE
Gets code of first currently hold down key in range between minKeyCode and maxKeyCode. If no key is pressed return value is unmodified and logical result is set to false

**Class:** `Pad.GetKeyPressedInRange`
**Flags:** condition, static

**Input:**
- `minKeyCode: KeyCode`
- `maxKeyCode: KeyCode`

**Output:**
- `keyCode: KeyCode (variable)`

---

### `2082` GET_KEY_JUST_PRESSED_IN_RANGE
Gets code of first just pressed key in range between minKeyCode and maxKeyCode. If no key was pressed return value is unmodified and logical result is set to false

**Class:** `Pad.GetKeyJustPressedInRange`
**Flags:** static, condition

**Input:**
- `minKeyCode: KeyCode`
- `maxKeyCode: KeyCode`

**Output:**
- `keyCode: KeyCode (variable)`

---

### `2083` EMULATE_KEY_PRESS
Simulates key press event

**Class:** `Pad.EmulateKeyPress`
**Flags:** static

**Input:**
- `keyCode: KeyCode`

---

### `2084` EMULATE_KEY_RELEASE
Simulates key release event

**Class:** `Pad.EmulateKeyRelease`
**Flags:** static

**Input:**
- `keyCode: KeyCode`

---

### `2085` GET_CONTROLLER_KEY
Returns n-th alternate key assigned to pad's action. If no key is bound then return value is unchanged and logical result is false

**Class:** `Pad.GetControllerKey`
**Flags:** static, condition

**Input:**
- `action: ControllerAction`
- `altKey: ControllerAltKey`

**Output:**
- `keyCode: KeyCode (variable)`

---

### `2086` GET_KEY_NAME
Returns keyboard/mouse key name text of specified keyCode. If key code has no name return value is unchanged and logical result is false

**Class:** `Pad.GetKeyName`
**Flags:** static, condition

**Input:**
- `keyCode: KeyCode`

**Output:**
- `name: string (variable)`

---
