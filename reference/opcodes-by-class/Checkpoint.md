# Checkpoint Opcodes

> 4 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `06D5` | CREATE_CHECKPOINT | Creates racing/flight style red checkpoint object |
| `06D6` | DELETE_CHECKPOINT |  |
| `07F3` | SET_CHECKPOINT_COORDS |  |
| `0996` | SET_CHECKPOINT_HEADING |  |

## Detailed Reference

### `06D5` CREATE_CHECKPOINT
Creates racing/flight style red checkpoint object

**Class:** `Checkpoint.Create`
**Flags:** constructor

**Input:**
- `type: CheckpointType`
- `x: float`
- `y: float`
- `z: float`
- `pointX: float`
- `pointY: float`
- `pointZ: float`
- `radius: float`

**Output:**
- `handle: Checkpoint (variable)`

---

### `06D6` DELETE_CHECKPOINT

**Class:** `Checkpoint.Delete`
**Flags:** destructor

**Input:**
- `self: Checkpoint`

---

### `07F3` SET_CHECKPOINT_COORDS

**Class:** `Checkpoint.SetCoords`

**Input:**
- `self: Checkpoint`
- `x: float`
- `y: float`
- `z: float`

---

### `0996` SET_CHECKPOINT_HEADING

**Class:** `Checkpoint.SetHeading`

**Input:**
- `self: Checkpoint`
- `heading: float`

---
