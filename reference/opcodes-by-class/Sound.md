# Sound Opcodes

> 2 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `018C` | ADD_ONE_OFF_SOUND | Plays a sound with the specified ID at the location |
| `018E` | REMOVE_SOUND | Stops the sound |

## Detailed Reference

### `018C` ADD_ONE_OFF_SOUND
Plays a sound with the specified ID at the location

**Class:** `Sound.AddOneOffSound`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `soundId: ScriptSound`

---

### `018E` REMOVE_SOUND
Stops the sound

**Class:** `Sound.Remove`
**Flags:** nop

**Input:**
- `self: Sound`

---
