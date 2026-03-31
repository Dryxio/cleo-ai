# Boat Opcodes

> 4 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `02D3` | BOAT_GOTO_COORDS | Makes the boat sail to the location |
| `02D4` | BOAT_STOP | Turns off the car's engine |
| `02DB` | SET_BOAT_CRUISE_SPEED | Sets the boat's max speed |
| `0323` | ANCHOR_BOAT | Makes the boat stay motionless in the water |

## Detailed Reference

### `02D3` BOAT_GOTO_COORDS
Makes the boat sail to the location

**Class:** `Boat.Goto`

**Input:**
- `self: Boat`
- `x: float`
- `y: float`
- `z: float`

---

### `02D4` BOAT_STOP
Turns off the car's engine

**Class:** `Boat.Stop`

**Input:**
- `self: Boat`

---

### `02DB` SET_BOAT_CRUISE_SPEED
Sets the boat's max speed

**Class:** `Boat.SetCruiseSpeed`

**Input:**
- `self: Boat`
- `maxSpeed: float`

---

### `0323` ANCHOR_BOAT
Makes the boat stay motionless in the water

**Class:** `Boat.Anchor`

**Input:**
- `self: Boat`
- `state: bool`

---
