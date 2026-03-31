# Crane Opcodes

> 6 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `079D` | PLAYER_ENTERED_DOCK_CRANE | Puts the player in the San Fierro dock crane |
| `079E` | PLAYER_ENTERED_BUILDINGSITE_CRANE | Puts the player in the San Fierro building site crane |
| `079F` | PLAYER_LEFT_CRANE | Removes the player from the current crane |
| `07F9` | PLAYER_ENTERED_QUARRY_CRANE | Puts the player in the crane at the quarry near Las Venturras |
| `07FA` | PLAYER_ENTERED_LAS_VEGAS_CRANE | Puts the player in the crane at the building site in Las Venturras |
| `0898` | ENABLE_CRANE_CONTROLS | Enables/disables individual crane controls |

## Detailed Reference

### `079D` PLAYER_ENTERED_DOCK_CRANE
Puts the player in the San Fierro dock crane

**Class:** `Crane.PlayerEnteredDockCrane`
**Flags:** static

---

### `079E` PLAYER_ENTERED_BUILDINGSITE_CRANE
Puts the player in the San Fierro building site crane

**Class:** `Crane.PlayerEnteredBuildingsiteCrane`
**Flags:** static

---

### `079F` PLAYER_LEFT_CRANE
Removes the player from the current crane

**Class:** `Crane.PlayerLeftCrane`
**Flags:** static

---

### `07F9` PLAYER_ENTERED_QUARRY_CRANE
Puts the player in the crane at the quarry near Las Venturras

**Class:** `Crane.PlayerEnteredQuarryCrane`
**Flags:** static

---

### `07FA` PLAYER_ENTERED_LAS_VEGAS_CRANE
Puts the player in the crane at the building site in Las Venturras

**Class:** `Crane.PlayerEnteredLasVegasCrane`
**Flags:** static

---

### `0898` ENABLE_CRANE_CONTROLS
Enables/disables individual crane controls

**Class:** `Crane.EnableControls`
**Flags:** static

**Input:**
- `up: bool`
- `down: bool`
- `release: bool`

---
