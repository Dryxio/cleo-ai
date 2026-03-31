# Pad Opcodes

> 13 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `00E1` | IS_BUTTON_PRESSED | Returns true if the pad's button has been pressed |
| `00E2` | GET_PAD_STATE | Stores the status of the specified key into a variable |
| `015B` | SHAKE_PAD | Shakes the player's joypad at the specified intensity for the specified time |
| `0293` | GET_CONTROLLER_MODE | Returns the controller mode |
| `03FD` | SET_DRUNK_INPUT_DELAY | Affects the delay to the left and right steering while driving |
| `0494` | GET_POSITION_OF_ANALOGUE_STICKS | Returns the offset of the specified Left/Right, Up/Down, Look Left/Look Right an |
| `07CC` | SET_PLAYER_ENTER_CAR_BUTTON | Sets whether the player can enter and exit vehicles |
| `082A` | SET_PLAYER_DUCK_BUTTON | Sets whether the player can use the crouch button |
| `0881` | SET_PLAYER_FIRE_BUTTON | Sets whether the player is able to use weapons |
| `08D0` | IS_SKIP_CUTSCENE_BUTTON_PRESSED | Returns true if the player is pressing a key used to skip cutscenes or the game  |
| `0901` | SET_PLAYER_JUMP_BUTTON | Sets whether the player can jump |
| `0960` | SET_PLAYER_DISPLAY_VITAL_STATS_BUTTON | Sets whether a player can use the ACTION key to display their stats |
| `0992` | SET_PLAYER_CYCLE_WEAPON_BUTTON |  |

## Detailed Reference

### `00E1` IS_BUTTON_PRESSED
Returns true if the pad's button has been pressed

**Class:** `Pad.IsButtonPressed`
**Flags:** condition, static

**Input:**
- `pad: PadId`
- `buttonId: Button`

---

### `00E2` GET_PAD_STATE
Stores the status of the specified key into a variable

**Class:** `Pad.GetState`
**Flags:** static

**Input:**
- `pad: PadId`
- `buttonId: Button`

**Output:**
- `state: int (variable)`

---

### `015B` SHAKE_PAD
Shakes the player's joypad at the specified intensity for the specified time

**Class:** `Pad.Shake`
**Flags:** static

**Input:**
- `pad: PadId`
- `time: int`
- `intensity: int`

---

### `0293` GET_CONTROLLER_MODE
Returns the controller mode

**Class:** `Pad.GetControllerMode`
**Flags:** static

**Output:**
- `mode: ControllerMode (variable)`

---

### `03FD` SET_DRUNK_INPUT_DELAY
Affects the delay to the left and right steering while driving

**Class:** `Pad.SetDrunkInputDelay`
**Flags:** static

**Input:**
- `pad: PadId`
- `delay: int`

---

### `0494` GET_POSITION_OF_ANALOGUE_STICKS
Returns the offset of the specified Left/Right, Up/Down, Look Left/Look Right and Look Up/Look Down keys

**Class:** `Pad.GetPositionOfAnalogueSticks`
**Flags:** static

**Input:**
- `pad: PadId`

**Output:**
- `leftStickX: int (variable)`
- `leftStickY: int (variable)`
- `rightStickX: int (variable)`
- `rightStickY: int (variable)`

---

### `07CC` SET_PLAYER_ENTER_CAR_BUTTON
Sets whether the player can enter and exit vehicles

**Class:** `Pad.SetPlayerEnterCarButton`
**Flags:** static

**Input:**
- `playerId: Player`
- `enabled: bool`

---

### `082A` SET_PLAYER_DUCK_BUTTON
Sets whether the player can use the crouch button

**Class:** `Pad.SetPlayerDuckButton`
**Flags:** static

**Input:**
- `playerId: Player`
- `enabled: bool`

---

### `0881` SET_PLAYER_FIRE_BUTTON
Sets whether the player is able to use weapons

**Class:** `Pad.SetPlayerFireButton`
**Flags:** static

**Input:**
- `playerId: Player`
- `enabled: bool`

---

### `08D0` IS_SKIP_CUTSCENE_BUTTON_PRESSED
Returns true if the player is pressing a key used to skip cutscenes or the game has been minimised

**Class:** `Pad.IsSkipCutsceneButtonPressed`
**Flags:** condition, static

---

### `0901` SET_PLAYER_JUMP_BUTTON
Sets whether the player can jump

**Class:** `Pad.SetPlayerJumpButton`
**Flags:** static

**Input:**
- `playerId: Player`
- `enabled: bool`

---

### `0960` SET_PLAYER_DISPLAY_VITAL_STATS_BUTTON
Sets whether a player can use the ACTION key to display their stats

**Class:** `Pad.SetPlayerDisplayVitalStatsButton`
**Flags:** static

**Input:**
- `playerId: Player`
- `enabled: bool`

---

### `0992` SET_PLAYER_CYCLE_WEAPON_BUTTON

**Class:** `Pad.SetPlayerCycleWeaponButton`
**Flags:** static

**Input:**
- `playerId: Player`
- `enabled: bool`

---
