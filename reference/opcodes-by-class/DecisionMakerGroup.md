# DecisionMakerGroup Opcodes

> 4 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `06AE` | LOAD_GROUP_DECISION_MAKER | Creates a decision maker for use on groups of actors |
| `0749` | CLEAR_GROUP_DECISION_MAKER_EVENT_RESPONSE | Resets the task for the event of the specified group decision maker |
| `074A` | ADD_GROUP_DECISION_MAKER_EVENT_RESPONSE | Sets which action should occur according to the event on the following parameter |
| `07E6` | COPY_GROUP_DECISION_MAKER | Creates copy of group decision maker and adds it to mission cleanup list. Otherw |

## Detailed Reference

### `06AE` LOAD_GROUP_DECISION_MAKER
Creates a decision maker for use on groups of actors

**Class:** `DecisionMakerGroup.Load`
**Flags:** constructor

**Input:**
- `type: DecisionMakerGroupType`

**Output:**
- `handle: DecisionMakerGroup (variable)`

---

### `0749` CLEAR_GROUP_DECISION_MAKER_EVENT_RESPONSE
Resets the task for the event of the specified group decision maker

**Class:** `DecisionMakerGroup.ClearEventResponse`

**Input:**
- `self: DecisionMakerGroup`
- `event: Event`

---

### `074A` ADD_GROUP_DECISION_MAKER_EVENT_RESPONSE
Sets which action should occur according to the event on the following parameters

**Class:** `DecisionMakerGroup.AddEventResponse`

**Input:**
- `self: DecisionMakerGroup`
- `event: Event`
- `taskId: TaskId`
- `respect: float`
- `hate: float`
- `like: float`
- `dislike: float`
- `inCar: bool`
- `onFoot: bool`

---

### `07E6` COPY_GROUP_DECISION_MAKER
Creates copy of group decision maker and adds it to mission cleanup list. Otherwise should be released with REMOVE_DECISION_MAKER

**Class:** `DecisionMakerGroup.Copy`
**Flags:** constructor

**Input:**
- `handleOrTemplate: DecisionMakerGroupTemplate`

**Output:**
- `handle: DecisionMakerGroup (variable)`

---
