# DecisionMakerChar Opcodes

> 5 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `060A` | LOAD_CHAR_DECISION_MAKER | Creates a decision maker with the specified type and adds it to mission cleanup  |
| `0708` | CLEAR_CHAR_DECISION_MAKER_EVENT_RESPONSE | Resets the task for the event of the specified decision maker |
| `0709` | ADD_CHAR_DECISION_MAKER_EVENT_RESPONSE | Sets which action should occur according to the event on the following parameter |
| `07E5` | COPY_CHAR_DECISION_MAKER | Copies a decision makers data to another decision maker |
| `0978` | COPY_SHARED_CHAR_DECISION_MAKER | Creates decision maker instance based on template. Adds itself to mission cleanu |

## Detailed Reference

### `060A` LOAD_CHAR_DECISION_MAKER
Creates a decision maker with the specified type and adds it to mission cleanup list. Otherwise should be released with REMOVE_DECISION_MAKER

**Class:** `DecisionMakerChar.Load`
**Flags:** constructor

**Input:**
- `type: DecisionMakerType`

**Output:**
- `handle: DecisionMakerChar (variable)`

---

### `0708` CLEAR_CHAR_DECISION_MAKER_EVENT_RESPONSE
Resets the task for the event of the specified decision maker

**Class:** `DecisionMakerChar.ClearEventResponse`

**Input:**
- `self: DecisionMakerChar`
- `event: Event`

---

### `0709` ADD_CHAR_DECISION_MAKER_EVENT_RESPONSE
Sets which action should occur according to the event on the following parameters

**Class:** `DecisionMakerChar.AddEventResponse`

**Input:**
- `self: DecisionMakerChar`
- `event: Event`
- `taskId: TaskId`
- `respect: float`
- `hate: float`
- `like: float`
- `dislike: float`
- `inCar: bool`
- `onFoot: bool`

**Details:**

This command defines how a ped should react to a specific event by adding a **weighted** response option to its decision maker.

Each call adds one possible task for that event. Up to `6` responses can be added per event.

The four float parameters (respect, hate, like, dislike) are weights, not percentages. All weights for the event are summed and normalized internally to determine the final probability of each response. A higher weight results in a higher chance of that task being chosen. Weights may exceed 100.0, only their relative values matter.

If only one response is defined for an event, it will always be chosen (100%). The selected task replaces the ped's currently active task.

The two boolean parameters (inCar, onFoot) specify when this response is valid based on the ped's state (whether the ped is on foot or in a vehicle).

---

### `07E5` COPY_CHAR_DECISION_MAKER
Copies a decision makers data to another decision maker

**Class:** `DecisionMakerChar.Copy`
**Flags:** constructor

**Input:**
- `handleOrTemplate: DecisionMakerCharTemplate`

**Output:**
- `handle: DecisionMakerChar (variable)`

---

### `0978` COPY_SHARED_CHAR_DECISION_MAKER
Creates decision maker instance based on template. Adds itself to mission cleanup list. Otherwise should be released with REMOVE_DECISION_MAKER

**Class:** `DecisionMakerChar.CopyShared`
**Flags:** constructor

**Input:**
- `template: DecisionMakerCharTemplate`

**Output:**
- `handle: DecisionMakerChar (variable)`

---
