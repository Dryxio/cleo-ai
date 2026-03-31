# Attractor Opcodes

> 3 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `061D` | ADD_ATTRACTOR | Adds a ped attractor |
| `061E` | CLEAR_ATTRACTOR |  |
| `0680` | ADD_PEDTYPE_AS_ATTRACTOR_USER |  |

## Detailed Reference

### `061D` ADD_ATTRACTOR
Adds a ped attractor

**Class:** `Attractor.Add`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `angle: float`
- `_p5: float`
- `sequence: Sequence`

**Output:**
- `handle: Attractor (variable)`

---

### `061E` CLEAR_ATTRACTOR

**Class:** `Attractor.Clear`
**Flags:** destructor

**Input:**
- `self: Attractor`

---

### `0680` ADD_PEDTYPE_AS_ATTRACTOR_USER

**Class:** `Attractor.AddPedTypeAsUser`

**Input:**
- `self: Attractor`
- `pedType: PedType`

---
