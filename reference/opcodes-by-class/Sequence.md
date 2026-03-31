# Sequence Opcodes

> 4 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0615` | OPEN_SEQUENCE_TASK | Begins a sequence of up to 8 tasks |
| `0616` | CLOSE_SEQUENCE_TASK | Ends the task sequence |
| `061B` | CLEAR_SEQUENCE_TASK | Clears the task sequence |
| `0643` | SET_SEQUENCE_TO_REPEAT | Sets whether the task sequence repeats continuously |

## Detailed Reference

### `0615` OPEN_SEQUENCE_TASK
Begins a sequence of up to 8 tasks

**Class:** `Sequence.Open`
**Flags:** constructor

**Output:**
- `handle: Sequence (variable)`

**Details:**

This command opens a sequence task. A sequence task is a group of commands between OPEN_SEQUENCE_TASK and CLOSE_SEQUENCE_TASK that can be assigned to a character or multiple characters. 

Use `-1` as the character handle for tasks within the sequence if you want the assigned character to perform the tasks.

---

### `0616` CLOSE_SEQUENCE_TASK
Ends the task sequence

**Class:** `Sequence.Close`

**Input:**
- `self: Sequence`

---

### `061B` CLEAR_SEQUENCE_TASK
Clears the task sequence

**Class:** `Sequence.Clear`
**Flags:** destructor

**Input:**
- `self: Sequence`

---

### `0643` SET_SEQUENCE_TO_REPEAT
Sets whether the task sequence repeats continuously

**Class:** `Sequence.SetToRepeat`

**Input:**
- `self: Sequence`
- `state: bool`

---
