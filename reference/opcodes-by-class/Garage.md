# Garage Opcodes

> 9 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `021B` | SET_TARGET_CAR_FOR_MISSION_GARAGE | Sets the specified garage to only accept the specified vehicle |
| `0299` | ACTIVATE_GARAGE | Activates the garage |
| `02B9` | DEACTIVATE_GARAGE | Deactivates the garage |
| `02FA` | CHANGE_GARAGE_TYPE | Sets the garage's type |
| `0360` | OPEN_GARAGE | Opens the garage |
| `0361` | CLOSE_GARAGE | Closes the garage |
| `03B0` | IS_GARAGE_OPEN | Returns true if the garage's door is open |
| `03B1` | IS_GARAGE_CLOSED | Returns true if the garage's door is closed |
| `093A` | SET_GARAGE_RESPRAY_FREE |  |

## Detailed Reference

### `021B` SET_TARGET_CAR_FOR_MISSION_GARAGE
Sets the specified garage to only accept the specified vehicle

**Class:** `Garage.SetTargetCarForMission`
**Flags:** static

**Input:**
- `garageName: GarageName`
- `vehicle: Car`

---

### `0299` ACTIVATE_GARAGE
Activates the garage

**Class:** `Garage.Activate`
**Flags:** static

**Input:**
- `garageId: string`

---

### `02B9` DEACTIVATE_GARAGE
Deactivates the garage

**Class:** `Garage.Deactivate`
**Flags:** static

**Input:**
- `garageId: string`

---

### `02FA` CHANGE_GARAGE_TYPE
Sets the garage's type

**Class:** `Garage.ChangeType`
**Flags:** static

**Input:**
- `garageId: string`
- `type: GarageType`

---

### `0360` OPEN_GARAGE
Opens the garage

**Class:** `Garage.Open`
**Flags:** static

**Input:**
- `garageId: string`

---

### `0361` CLOSE_GARAGE
Closes the garage

**Class:** `Garage.Close`
**Flags:** static

**Input:**
- `garageId: string`

---

### `03B0` IS_GARAGE_OPEN
Returns true if the garage's door is open

**Class:** `Garage.IsOpen`
**Flags:** condition, static

**Input:**
- `garageId: string`

---

### `03B1` IS_GARAGE_CLOSED
Returns true if the garage's door is closed

**Class:** `Garage.IsClosed`
**Flags:** condition, static

**Input:**
- `garageId: string`

---

### `093A` SET_GARAGE_RESPRAY_FREE

**Class:** `Garage.SetResprayFree`
**Flags:** static

**Input:**
- `garageId: string`
- `state: bool`

---
