# Debugger Opcodes

> 5 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0052` | LINE | Displays 6 floating-point values on the screen |
| `00C3` | DEBUG_ON | Activates debug features in this script |
| `00C4` | DEBUG_OFF | Deactivates debug features in this script |
| `05A0` | IS_DEBUG_CAMERA_ON |  |
| `05B6` | SAVE_STRING_TO_DEBUG_FILE | Makes the current script skip the next 128 bytes of the code |

## Detailed Reference

### `0052` LINE
Displays 6 floating-point values on the screen

**Class:** `Debugger.Line`
**Flags:** nop, static

**Input:**
- `f1: float`
- `f2: float`
- `f3: float`
- `f4: float`
- `f5: float`
- `f6: float`

---

### `00C3` DEBUG_ON
Activates debug features in this script

**Class:** `Debugger.Enable`
**Flags:** static

---

### `00C4` DEBUG_OFF
Deactivates debug features in this script

**Class:** `Debugger.Disable`
**Flags:** static

---

### `05A0` IS_DEBUG_CAMERA_ON

**Class:** `Debugger.IsDebugCameraOn`
**Flags:** condition, static

---

### `05B6` SAVE_STRING_TO_DEBUG_FILE
Makes the current script skip the next 128 bytes of the code

**Class:** `Debugger.SaveStringToDebugFile`
**Flags:** static, nop

**Input:**
- `msg: string128`

---
