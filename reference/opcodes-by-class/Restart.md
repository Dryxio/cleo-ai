# Restart Opcodes

> 7 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `016C` | ADD_HOSPITAL_RESTART | Adds a hospital restart, which is where the player will spawn after death (waste |
| `016D` | ADD_POLICE_RESTART | Adds a police restart, which is where the player will spawn after being arrested |
| `016E` | OVERRIDE_NEXT_RESTART | Forces this location to be the next respawn location |
| `01F6` | CANCEL_OVERRIDE_RESTART | Stops the player from spawning at the override location (016E) |
| `08DF` | SET_EXTRA_HOSPITAL_RESTART_POINT |  |
| `08E0` | SET_EXTRA_POLICE_STATION_RESTART_POINT |  |
| `09FF` | SET_RESPAWN_POINT_FOR_DURATION_OF_MISSION | Overrides the respawn point |

## Detailed Reference

### `016C` ADD_HOSPITAL_RESTART
Adds a hospital restart, which is where the player will spawn after death (wasted) if the point is closer than any other hospital restart

**Class:** `Restart.AddHospital`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `heading: float`
- `citiesPassed: int`

---

### `016D` ADD_POLICE_RESTART
Adds a police restart, which is where the player will spawn after being arrested (busted) if the point is closer than any other police restart

**Class:** `Restart.AddPolice`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `heading: float`
- `citiesPassed: int`

---

### `016E` OVERRIDE_NEXT_RESTART
Forces this location to be the next respawn location

**Class:** `Restart.OverrideNext`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `heading: float`

---

### `01F6` CANCEL_OVERRIDE_RESTART
Stops the player from spawning at the override location (016E)

**Class:** `Restart.CancelOverride`
**Flags:** static

---

### `08DF` SET_EXTRA_HOSPITAL_RESTART_POINT

**Class:** `Restart.SetExtraHospitalRestartPoint`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `heading: float`

---

### `08E0` SET_EXTRA_POLICE_STATION_RESTART_POINT

**Class:** `Restart.SetExtraPoliceStationRestartPoint`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `heading: float`

---

### `09FF` SET_RESPAWN_POINT_FOR_DURATION_OF_MISSION
Overrides the respawn point

**Class:** `Restart.SetRespawnPointForDurationOfMission`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`

---
