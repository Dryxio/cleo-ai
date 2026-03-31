# Mouse Opcodes

> 2 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0A4A` | GET_PC_MOUSE_MOVEMENT | Gives the offset of the mouse or right thumbstick movement |
| `0A4C` | IS_MOUSE_USING_VERTICAL_INVERSION | Returns true if the players settings are set to invert the mouse |

## Detailed Reference

### `0A4A` GET_PC_MOUSE_MOVEMENT
Gives the offset of the mouse or right thumbstick movement

**Class:** `Mouse.GetMovement`
**Flags:** static

**Output:**
- `deltaX: float (variable)`
- `deltaY: float (variable)`

---

### `0A4C` IS_MOUSE_USING_VERTICAL_INVERSION
Returns true if the players settings are set to invert the mouse

**Class:** `Mouse.IsUsingVerticalInversion`
**Flags:** condition, static

---
