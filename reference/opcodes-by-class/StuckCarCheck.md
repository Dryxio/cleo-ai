# StuckCarCheck Opcodes

> 4 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `03CC` | ADD_STUCK_CAR_CHECK | Adds the vehicle to the stuck cars array |
| `03CD` | REMOVE_STUCK_CAR_CHECK | Removes the vehicle from the stuck cars array |
| `03CE` | IS_CAR_STUCK | Returns true if the car is stuck |
| `072F` | ADD_STUCK_CAR_CHECK_WITH_WARP | Attempts to automatically restore vehicles that get stuck or flipped |

## Detailed Reference

### `03CC` ADD_STUCK_CAR_CHECK
Adds the vehicle to the stuck cars array

**Class:** `StuckCarCheck.Add`
**Flags:** static

**Input:**
- `vehicle: Car`
- `distance: float`
- `time: int`

---

### `03CD` REMOVE_STUCK_CAR_CHECK
Removes the vehicle from the stuck cars array

**Class:** `StuckCarCheck.Remove`
**Flags:** static

**Input:**
- `vehicle: Car`

---

### `03CE` IS_CAR_STUCK
Returns true if the car is stuck

**Class:** `StuckCarCheck.IsCarStuck`
**Flags:** condition, static

**Input:**
- `vehicle: Car`

---

### `072F` ADD_STUCK_CAR_CHECK_WITH_WARP
Attempts to automatically restore vehicles that get stuck or flipped

**Class:** `StuckCarCheck.AddWithWarp`
**Flags:** static

**Input:**
- `vehicle: Car`
- `distance: float`
- `time: int`
- `stuck: bool`
- `flipped: bool`
- `inWater: bool`
- `numNodesToCheck: int`

---
