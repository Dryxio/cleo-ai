# ScriptFire Opcodes

> 7 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `02CF` | START_SCRIPT_FIRE | Creates a fire at the specified coordinates |
| `02D0` | IS_SCRIPT_FIRE_EXTINGUISHED | Returns true if the script fire has been put out |
| `02D1` | REMOVE_SCRIPT_FIRE | Removes the script fire |
| `0325` | START_CAR_FIRE | Creates a script fire on the vehicle |
| `0326` | START_CHAR_FIRE | Creates a script fire on the character |
| `06F5` | GET_SCRIPT_FIRE_COORDS | Gets the coordinates of the fire |
| `0973` | DOES_SCRIPT_FIRE_EXIST | Returns true if the handle is a valid script fire handle |

## Detailed Reference

### `02CF` START_SCRIPT_FIRE
Creates a fire at the specified coordinates

**Class:** `ScriptFire.Start`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `propagation: int`
- `size: int`

**Output:**
- `handle: ScriptFire (variable)`

---

### `02D0` IS_SCRIPT_FIRE_EXTINGUISHED
Returns true if the script fire has been put out

**Class:** `ScriptFire.IsExtinguished`
**Flags:** condition

**Input:**
- `self: ScriptFire`

---

### `02D1` REMOVE_SCRIPT_FIRE
Removes the script fire

**Class:** `ScriptFire.Remove`
**Flags:** destructor

**Input:**
- `self: ScriptFire`

---

### `0325` START_CAR_FIRE
Creates a script fire on the vehicle

**Class:** `ScriptFire.CreateCarFire`
**Flags:** constructor

**Input:**
- `vehicle: Car`

**Output:**
- `handle: ScriptFire (variable)`

---

### `0326` START_CHAR_FIRE
Creates a script fire on the character

**Class:** `ScriptFire.CreateCharFire`
**Flags:** constructor

**Input:**
- `char: Char`

**Output:**
- `handle: ScriptFire (variable)`

---

### `06F5` GET_SCRIPT_FIRE_COORDS
Gets the coordinates of the fire

**Class:** `ScriptFire.GetCoords`

**Input:**
- `self: ScriptFire`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0973` DOES_SCRIPT_FIRE_EXIST
Returns true if the handle is a valid script fire handle

**Class:** `ScriptFire.DoesExist`
**Flags:** condition, static

**Input:**
- `handle: any`

---
