# Stat Opcodes

> 26 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `030C` | PLAYER_MADE_PROGRESS | Increases the progress made stat by the specified amount |
| `030D` | SET_PROGRESS_TOTAL | Sets the maximum progress the player can reach |
| `0317` | REGISTER_MISSION_GIVEN | Increments the number of mission attempts stat by one |
| `0318` | REGISTER_MISSION_PASSED | Sets the GXT of the last mission passed |
| `042C` | SET_TOTAL_NUMBER_OF_MISSIONS | Sets the total number of missions that can be completed |
| `042E` | REGISTER_FASTEST_TIME | Updates the stat if the value is lower than the current stat value |
| `0582` | REGISTER_BEST_POSITION | Updates the race best position |
| `058C` | GET_PROGRESS_PERCENTAGE | Gets the progress of completion as a percentage |
| `0595` | REGISTER_ODDJOB_MISSION_PASSED | Sets the latest odd job mission passed |
| `0623` | INCREMENT_INT_STAT | Increases the integer stat by the value given |
| `0624` | INCREMENT_FLOAT_STAT | Increases the float stat by the value specified |
| `0625` | DECREMENT_INT_STAT | Decreases the integer stat by the value given |
| `0626` | DECREMENT_FLOAT_STAT | Decreases the float stat by the value given |
| `0627` | REGISTER_INT_STAT | Updates the specified integer stat |
| `0628` | REGISTER_FLOAT_STAT | Sets the specified stat to the specified value, if the specified value is greate |
| `0629` | SET_INT_STAT | Sets the integer stat to the specified value |
| `062A` | SET_FLOAT_STAT | Sets the float stat to the specified value |
| `0652` | GET_INT_STAT | Returns the value of the specified integer stat |
| `0653` | GET_FLOAT_STAT | Returns the value of the specified float stat |
| `08E1` | FIND_NUMBER_TAGS_TAGGED | Gets the number of spraytags painted over |
| `08E2` | GET_TERRITORY_UNDER_CONTROL_PERCENTAGE |  |
| `08F8` | SHOW_UPDATE_STATS | Displays help boxes indicating that the players stats have been updated |
| `0997` | SET_MISSION_RESPECT_TOTAL | Sets the total value of mission respect points (stat 228) |
| `0998` | AWARD_PLAYER_MISSION_RESPECT | Increments the earned mission respect points (stat 224) by the given value |
| `0A10` | INCREMENT_INT_STAT_NO_MESSAGE | Increases the integer stat by the value given without displaying popup message |
| `0A1F` | INCREMENT_FLOAT_STAT_NO_MESSAGE | Increases the float stat by the value given without displaying popup message |

## Detailed Reference

### `030C` PLAYER_MADE_PROGRESS
Increases the progress made stat by the specified amount

**Class:** `Stat.PlayerMadeProgress`
**Flags:** static

**Input:**
- `progress: int`

---

### `030D` SET_PROGRESS_TOTAL
Sets the maximum progress the player can reach

**Class:** `Stat.SetProgressTotal`
**Flags:** static

**Input:**
- `maxProgress: int`

---

### `0317` REGISTER_MISSION_GIVEN
Increments the number of mission attempts stat by one

**Class:** `Stat.RegisterMissionGiven`
**Flags:** static

---

### `0318` REGISTER_MISSION_PASSED
Sets the GXT of the last mission passed

**Class:** `Stat.RegisterMissionPassed`
**Flags:** static

**Input:**
- `key: gxt_key`

---

### `042C` SET_TOTAL_NUMBER_OF_MISSIONS
Sets the total number of missions that can be completed

**Class:** `Stat.SetTotalNumberOfMissions`
**Flags:** static

**Input:**
- `numMissions: int`

---

### `042E` REGISTER_FASTEST_TIME
Updates the stat if the value is lower than the current stat value

**Class:** `Stat.RegisterFastestTime`
**Flags:** static

**Input:**
- `id: StatId`
- `value: int`

---

### `0582` REGISTER_BEST_POSITION
Updates the race best position

**Class:** `Stat.RegisterBestPosition`
**Flags:** static

**Input:**
- `id: StatId`
- `position: int`

---

### `058C` GET_PROGRESS_PERCENTAGE
Gets the progress of completion as a percentage

**Class:** `Stat.GetProgressPercentage`
**Flags:** static

**Output:**
- `percentage: float (variable)`

---

### `0595` REGISTER_ODDJOB_MISSION_PASSED
Sets the latest odd job mission passed

**Class:** `Stat.RegisterOddjobMissionPassed`
**Flags:** static

---

### `0623` INCREMENT_INT_STAT
Increases the integer stat by the value given

**Class:** `Stat.IncrementInt`
**Flags:** static

**Input:**
- `id: StatId`
- `value: int`

---

### `0624` INCREMENT_FLOAT_STAT
Increases the float stat by the value specified

**Class:** `Stat.IncrementFloat`
**Flags:** static

**Input:**
- `id: StatId`
- `value: float`

---

### `0625` DECREMENT_INT_STAT
Decreases the integer stat by the value given

**Class:** `Stat.DecrementInt`
**Flags:** static

**Input:**
- `id: StatId`
- `value: int`

---

### `0626` DECREMENT_FLOAT_STAT
Decreases the float stat by the value given

**Class:** `Stat.DecrementFloat`
**Flags:** static

**Input:**
- `id: StatId`
- `value: float`

---

### `0627` REGISTER_INT_STAT
Updates the specified integer stat

**Class:** `Stat.RegisterInt`
**Flags:** static

**Input:**
- `id: StatId`
- `value: int`

---

### `0628` REGISTER_FLOAT_STAT
Sets the specified stat to the specified value, if the specified value is greater than the current stat value

**Class:** `Stat.RegisterFloat`
**Flags:** static

**Input:**
- `id: StatId`
- `value: float`

---

### `0629` SET_INT_STAT
Sets the integer stat to the specified value

**Class:** `Stat.SetInt`
**Flags:** static

**Input:**
- `id: StatId`
- `value: int`

---

### `062A` SET_FLOAT_STAT
Sets the float stat to the specified value

**Class:** `Stat.SetFloat`
**Flags:** static

**Input:**
- `id: StatId`
- `value: float`

---

### `0652` GET_INT_STAT
Returns the value of the specified integer stat

**Class:** `Stat.GetInt`
**Flags:** static

**Input:**
- `id: StatId`

**Output:**
- `value: int (variable)`

---

### `0653` GET_FLOAT_STAT
Returns the value of the specified float stat

**Class:** `Stat.GetFloat`
**Flags:** static

**Input:**
- `id: StatId`

**Output:**
- `value: float (variable)`

---

### `08E1` FIND_NUMBER_TAGS_TAGGED
Gets the number of spraytags painted over

**Class:** `Stat.FindNumberTagsTagged`
**Flags:** static

**Output:**
- `numTags: int (variable)`

---

### `08E2` GET_TERRITORY_UNDER_CONTROL_PERCENTAGE

**Class:** `Stat.GetTerritoryUnderControlPercentage`
**Flags:** static

**Output:**
- `percentage: int (variable)`

---

### `08F8` SHOW_UPDATE_STATS
Displays help boxes indicating that the players stats have been updated

**Class:** `Stat.ShowUpdateStats`
**Flags:** static

**Input:**
- `state: bool`

---

### `0997` SET_MISSION_RESPECT_TOTAL
Sets the total value of mission respect points (stat 228)

**Class:** `Stat.SetMissionRespectTotal`
**Flags:** static

**Input:**
- `value: int`

**Details:**

This command modifies a value stored in stat `228` (StatId.RespectMissionTotal). This value affects how the player's respect is changed after awarding new mission respect points. See AWARD_PLAYER_MISSION_RESPECT for more information.

The original script sets the total number of mission respect points to `1339`. This is the exact sum of all points awarded after completing all missions. 

Failing to call this command or using a low value will cause the player's respect to skyrocket when new mission respect points are awarded.

---

### `0998` AWARD_PLAYER_MISSION_RESPECT
Increments the earned mission respect points (stat 224) by the given value

**Class:** `Stat.AwardPlayerMissionRespect`
**Flags:** static

**Input:**
- `value: int`

**Details:**

This command behaves similarly to INCREMENT_INT_STAT_NO_MESSAGE where stat id is `224` (StatId.RespectMission).

Awarded mission points affect player's respect. With each awarded point the respect gets increased by `360/x` where `x` is a total number of mission points set with SET_MISSION_RESPECT_TOTAL. The game ensures `x` is never less than `1`.

For example, if there are `1339` points in total, calling `AWARD_PLAYER_MISSION_RESPECT 5` increases the respect by `1.344` (because `360 / 1339 * 5 = 1.344`).

---

### `0A10` INCREMENT_INT_STAT_NO_MESSAGE
Increases the integer stat by the value given without displaying popup message

**Class:** `Stat.IncrementIntNoMessage`
**Flags:** static

**Input:**
- `id: StatId`
- `value: int`

---

### `0A1F` INCREMENT_FLOAT_STAT_NO_MESSAGE
Increases the float stat by the value given without displaying popup message

**Class:** `Stat.IncrementFloatNoMessage`
**Flags:** static

**Input:**
- `id: StatId`
- `value: float`

---
