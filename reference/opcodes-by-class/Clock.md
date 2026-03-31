# Clock Opcodes

> 10 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `00BF` | GET_TIME_OF_DAY | Returns the number of hours and minutes passed since midnight |
| `00C0` | SET_TIME_OF_DAY | Sets the current in-game time |
| `00C1` | GET_MINUTES_TO_TIME_OF_DAY | Returns the number of minutes left until the clock matches the time specified |
| `015D` | SET_TIME_SCALE | Sets the game to run at the specified speed |
| `01BD` | GET_GAME_TIMER | Returns the time passed in milliseconds since the game started |
| `0253` | STORE_CLOCK | Saves the current time in game |
| `0254` | RESTORE_CLOCK | Restores the game time to the time when it was saved with 0253 |
| `07D0` | GET_CURRENT_DAY_OF_WEEK | Returns an integer representation of the in-game day of the week |
| `0835` | GET_CURRENT_DATE | Returns the in-game day of the month and month of the year |
| `088E` | SET_TIME_ONE_DAY_FORWARD | Progresses the game to the next day |

## Detailed Reference

### `00BF` GET_TIME_OF_DAY
Returns the number of hours and minutes passed since midnight

**Class:** `Clock.GetTimeOfDay`
**Flags:** static

**Output:**
- `hours: int (variable)`
- `minutes: int (variable)`

---

### `00C0` SET_TIME_OF_DAY
Sets the current in-game time

**Class:** `Clock.SetTimeOfDay`
**Flags:** static

**Input:**
- `hours: int`
- `minutes: int`

---

### `00C1` GET_MINUTES_TO_TIME_OF_DAY
Returns the number of minutes left until the clock matches the time specified

**Class:** `Clock.GetMinutesToTimeOfDay`
**Flags:** static

**Input:**
- `hours: int`
- `minutes: int`

**Output:**
- `minutesLeft: int (variable)`

---

### `015D` SET_TIME_SCALE
Sets the game to run at the specified speed

**Class:** `Clock.SetTimeScale`
**Flags:** static

**Input:**
- `scale: float`

---

### `01BD` GET_GAME_TIMER
Returns the time passed in milliseconds since the game started

**Class:** `Clock.GetGameTimer`
**Flags:** static

**Output:**
- `time: int (variable)`

---

### `0253` STORE_CLOCK
Saves the current time in game

**Class:** `Clock.Store`
**Flags:** static

---

### `0254` RESTORE_CLOCK
Restores the game time to the time when it was saved with 0253

**Class:** `Clock.Restore`
**Flags:** static

---

### `07D0` GET_CURRENT_DAY_OF_WEEK
Returns an integer representation of the in-game day of the week

**Class:** `Clock.GetCurrentDayOfWeek`
**Flags:** static

**Output:**
- `day: int (variable)`

---

### `0835` GET_CURRENT_DATE
Returns the in-game day of the month and month of the year

**Class:** `Clock.GetCurrentDate`
**Flags:** static

**Output:**
- `day: int (variable)`
- `month: int (variable)`

---

### `088E` SET_TIME_ONE_DAY_FORWARD
Progresses the game to the next day

**Class:** `Clock.SetTimeOneDayForward`
**Flags:** static

---
