# Cutscene Opcodes

> 10 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0244` | SET_CUTSCENE_OFFSET | Sets the position for a cutscene |
| `02E4` | LOAD_CUTSCENE | Loads the data for the specified cutscene |
| `02E7` | START_CUTSCENE | Starts the loaded cutscene (02E4) |
| `02E8` | GET_CUTSCENE_TIME | Returns the time in milliseconds passed since the cutscene has started (02E7) |
| `02E9` | HAS_CUTSCENE_FINISHED | Returns true if the cutscene has finished |
| `02EA` | CLEAR_CUTSCENE | Ends the current cutscene, freeing game memory |
| `056A` | WAS_CUTSCENE_SKIPPED | Returns true if the cutscene was skipped |
| `06B9` | HAS_CUTSCENE_LOADED | Returns true if the cutscene has finished loading |
| `08D1` | GET_CUTSCENE_OFFSET | Stores the offset of the currently loaded cutscene |
| `08F0` | APPEND_TO_NEXT_CUTSCENE |  |

## Detailed Reference

### `0244` SET_CUTSCENE_OFFSET
Sets the position for a cutscene

**Class:** `Cutscene.SetOffset`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`

---

### `02E4` LOAD_CUTSCENE
Loads the data for the specified cutscene

**Class:** `Cutscene.Load`
**Flags:** static

**Input:**
- `name: string`

---

### `02E7` START_CUTSCENE
Starts the loaded cutscene (02E4)

**Class:** `Cutscene.Start`
**Flags:** static

---

### `02E8` GET_CUTSCENE_TIME
Returns the time in milliseconds passed since the cutscene has started (02E7)

**Class:** `Cutscene.GetTime`
**Flags:** static

**Output:**
- `time: int (variable)`

---

### `02E9` HAS_CUTSCENE_FINISHED
Returns true if the cutscene has finished

**Class:** `Cutscene.HasFinished`
**Flags:** condition, static

---

### `02EA` CLEAR_CUTSCENE
Ends the current cutscene, freeing game memory

**Class:** `Cutscene.Clear`
**Flags:** static

---

### `056A` WAS_CUTSCENE_SKIPPED
Returns true if the cutscene was skipped

**Class:** `Cutscene.WasSkipped`
**Flags:** condition, static

---

### `06B9` HAS_CUTSCENE_LOADED
Returns true if the cutscene has finished loading

**Class:** `Cutscene.HasLoaded`
**Flags:** condition, static

---

### `08D1` GET_CUTSCENE_OFFSET
Stores the offset of the currently loaded cutscene

**Class:** `Cutscene.GetOffset`
**Flags:** static

**Output:**
- `xOffset: float (variable)`
- `yOffset: float (variable)`
- `zOffset: float (variable)`

---

### `08F0` APPEND_TO_NEXT_CUTSCENE

**Class:** `Cutscene.AppendToNext`
**Flags:** static

**Input:**
- `objectName: string`
- `animName: string`

---
