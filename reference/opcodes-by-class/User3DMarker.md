# User3DMarker Opcodes

> 2 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0A40` | CREATE_USER_3D_MARKER | Creates a marker similar to the yellow enex markers |
| `0A41` | REMOVE_USER_3D_MARKER | Destroys a marker created with 0A40 |

## Detailed Reference

### `0A40` CREATE_USER_3D_MARKER
Creates a marker similar to the yellow enex markers

**Class:** `User3DMarker.Create`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `color: HudColors`

**Output:**
- `handle: User3DMarker (variable)`

**Details:**

This command spawns a 3d marker into the world. The marker is typically used to denote interior access but it does not create access to the actual interior. The number of 3d markers created with this command is limited to five. Unlike most positioning commands, using `-100.0` as the z-coordinate to detect ground z does not work. The 3d marker can be removed using REMOVE_USER_3D_MARKER. It can be seen during replays.

---

### `0A41` REMOVE_USER_3D_MARKER
Destroys a marker created with 0A40

**Class:** `User3DMarker.Remove`
**Flags:** destructor

**Input:**
- `self: User3DMarker`

---
