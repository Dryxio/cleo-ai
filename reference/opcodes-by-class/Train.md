# Train Opcodes

> 13 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `06D8` | CREATE_MISSION_TRAIN | Creates a script handled train from a predefined type (the type dictates how lon |
| `06DC` | SET_TRAIN_SPEED | Sets the trains acceleration |
| `06DD` | SET_TRAIN_CRUISE_SPEED | Sets the trains speed |
| `06DE` | GET_TRAIN_CABOOSE | Gets the handle of the last carriage (known as the "caboose") |
| `078A` | GET_TRAIN_CARRIAGE | Gets the nth train carriage |
| `07BD` | DELETE_MISSION_TRAIN | Removes the specified script created train |
| `07BE` | MARK_MISSION_TRAIN_AS_NO_LONGER_NEEDED | Removes the specified script created train from the list of trains that the game |
| `07C7` | SET_MISSION_TRAIN_COORDINATES | Puts the train on the rails nearest to the specified coordinates |
| `0981` | HAS_TRAIN_DERAILED | Returns true if the train has derailed (usually from going too fast) |
| `09CF` | SET_TRAIN_FORCED_TO_SLOW_DOWN | Sets whether the train should stop at each station it encounters |
| `09E3` | FIND_TRAIN_DIRECTION | Returns true if the train is travelling clockwise, around San Andreas |
| `0A06` | IS_NEXT_STATION_ALLOWED | Returns true if the next station is accessible (at the start of the game, railro |
| `0A07` | SKIP_TO_NEXT_ALLOWED_STATION | Puts the script created train at the next allowed station |

## Detailed Reference

### `06D8` CREATE_MISSION_TRAIN
Creates a script handled train from a predefined type (the type dictates how long the train is and the varieties of carriages) and sets the direction for the train to head in

**Class:** `Train.Create`
**Flags:** constructor

**Input:**
- `type: int`
- `x: float`
- `y: float`
- `z: float`
- `direction: bool`

**Output:**
- `handle: Train (variable)`

---

### `06DC` SET_TRAIN_SPEED
Sets the trains acceleration

**Class:** `Train.SetSpeed`

**Input:**
- `self: Train`
- `speed: float`

---

### `06DD` SET_TRAIN_CRUISE_SPEED
Sets the trains speed

**Class:** `Train.SetCruiseSpeed`

**Input:**
- `self: Train`
- `speed: float`

---

### `06DE` GET_TRAIN_CABOOSE
Gets the handle of the last carriage (known as the "caboose")

**Class:** `Train.GetCaboose`

**Input:**
- `self: Train`

**Output:**
- `caboose: Car (variable)`

---

### `078A` GET_TRAIN_CARRIAGE
Gets the nth train carriage

**Class:** `Train.GetCarriage`

**Input:**
- `self: Train`
- `number: int`

**Output:**
- `carriage: Car (variable)`

---

### `07BD` DELETE_MISSION_TRAIN
Removes the specified script created train

**Class:** `Train.Delete`
**Flags:** destructor

**Input:**
- `self: Train`

---

### `07BE` MARK_MISSION_TRAIN_AS_NO_LONGER_NEEDED
Removes the specified script created train from the list of trains that the game shouldn't delete

**Class:** `Train.MarkAsNoLongerNeeded`

**Input:**
- `self: Train`

---

### `07C7` SET_MISSION_TRAIN_COORDINATES
Puts the train on the rails nearest to the specified coordinates

**Class:** `Train.SetCoordinates`

**Input:**
- `self: Train`
- `x: float`
- `y: float`
- `z: float`

---

### `0981` HAS_TRAIN_DERAILED
Returns true if the train has derailed (usually from going too fast)

**Class:** `Train.HasDerailed`
**Flags:** condition

**Input:**
- `self: Train`

---

### `09CF` SET_TRAIN_FORCED_TO_SLOW_DOWN
Sets whether the train should stop at each station it encounters

**Class:** `Train.SetForcedToSlowDown`

**Input:**
- `self: Train`
- `state: bool`

---

### `09E3` FIND_TRAIN_DIRECTION
Returns true if the train is travelling clockwise, around San Andreas

**Class:** `Train.FindDirection`
**Flags:** condition

**Input:**
- `self: Train`

---

### `0A06` IS_NEXT_STATION_ALLOWED
Returns true if the next station is accessible (at the start of the game, railroad blocks prevent the player from travelling to stations whose area is not unlocked)

**Class:** `Train.IsNextStationAllowed`
**Flags:** condition

**Input:**
- `self: Train`

---

### `0A07` SKIP_TO_NEXT_ALLOWED_STATION
Puts the script created train at the next allowed station

**Class:** `Train.SkipToNextAllowedStation`

**Input:**
- `self: Train`

---
