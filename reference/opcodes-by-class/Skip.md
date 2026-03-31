# Skip Opcodes

> 6 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0950` | SET_UP_SKIP | Fades out the screen and teleports the player to the specified coordinates and a |
| `0951` | CLEAR_SKIP |  |
| `09AF` | SET_UP_SKIP_AFTER_MISSION | Fades the screen out and teleports the player to the specified coordinates and a |
| `09E0` | SET_UP_SKIP_FOR_SPECIFIC_VEHICLE | Teleports the player to the specified coordinates and sets the specified angle w |
| `0A35` | SET_UP_SKIP_FOR_VEHICLE_FINISHED_BY_SCRIPT | Teleports the player to the specified coordinates and sets the specified angle w |
| `0A36` | IS_SKIP_WAITING_FOR_SCRIPT_TO_FADE_IN | Returns true if the trip skip created with 0A35 has finished teleporting the veh |

## Detailed Reference

### `0950` SET_UP_SKIP
Fades out the screen and teleports the player to the specified coordinates and angle

**Class:** `Skip.SetUp`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `heading: float`

---

### `0951` CLEAR_SKIP

**Class:** `Skip.Clear`
**Flags:** static

---

### `09AF` SET_UP_SKIP_AFTER_MISSION
Fades the screen out and teleports the player to the specified coordinates and angle

**Class:** `Skip.SetUpAfterMission`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `heading: float`

---

### `09E0` SET_UP_SKIP_FOR_SPECIFIC_VEHICLE
Teleports the player to the specified coordinates and sets the specified angle when in the specified car

**Class:** `Skip.SetUpForSpecificVehicle`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `heading: float`
- `handle: Car`

---

### `0A35` SET_UP_SKIP_FOR_VEHICLE_FINISHED_BY_SCRIPT
Teleports the player to the specified coordinates and sets the specified angle with the screen fading in when in the specified car

**Class:** `Skip.SetUpForVehicleFinishedByScript`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `heading: float`
- `vehicle: Car`

---

### `0A36` IS_SKIP_WAITING_FOR_SCRIPT_TO_FADE_IN
Returns true if the trip skip created with 0A35 has finished teleporting the vehicle and is ready to allow the script to fade in

**Class:** `Skip.IsWaitingForScriptToFadeIn`
**Flags:** condition, static

---
