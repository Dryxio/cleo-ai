# KillFrenzy Opcodes

> 3 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `01F9` | START_KILL_FRENZY | Starts a rampage |
| `01FA` | READ_KILL_FRENZY_STATUS | Returns the status of the current rampage |
| `09C2` | FAIL_KILL_FRENZY | Cancels current rampage, setting the rampage status to failed |

## Detailed Reference

### `01F9` START_KILL_FRENZY
Starts a rampage

**Class:** `KillFrenzy.Start`
**Flags:** static

**Input:**
- `text: gxt_key`
- `weaponType: WeaponType`
- `timeInMs: int`
- `targetsNum: int`
- `targetModel1: model_any`
- `targetModel2: model_any`
- `targetModel3: model_any`
- `targetModel4: model_any`
- `betaSoundsAndMessages: bool`

---

### `01FA` READ_KILL_FRENZY_STATUS
Returns the status of the current rampage

**Class:** `KillFrenzy.ReadStatus`
**Flags:** static

**Output:**
- `status: int (variable)`

---

### `09C2` FAIL_KILL_FRENZY
Cancels current rampage, setting the rampage status to failed

**Class:** `KillFrenzy.Fail`
**Flags:** static

---
