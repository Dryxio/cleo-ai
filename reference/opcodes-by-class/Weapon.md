# Weapon Opcodes

> 2 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0781` | GET_WEAPONTYPE_MODEL | Gets the model ID of the weapon according to the weapon type |
| `0782` | GET_WEAPONTYPE_SLOT |  |

## Detailed Reference

### `0781` GET_WEAPONTYPE_MODEL
Gets the model ID of the weapon according to the weapon type

**Class:** `Weapon.GetModel`
**Flags:** static

**Input:**
- `weaponType: WeaponType`

**Output:**
- `modelId: model_object (variable)`

---

### `0782` GET_WEAPONTYPE_SLOT

**Class:** `Weapon.GetSlot`
**Flags:** static

**Input:**
- `weaponType: WeaponType`

**Output:**
- `slot: WeaponSlot (variable)`

---
