# DecisionMaker Opcodes

> 2 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `065C` | REMOVE_DECISION_MAKER | Removes the decision maker |
| `09F2` | DOES_DECISION_MAKER_EXIST | Returns true if the handle is a valid decision maker handle |

## Detailed Reference

### `065C` REMOVE_DECISION_MAKER
Removes the decision maker

**Class:** `DecisionMaker.Remove`
**Flags:** destructor

**Input:**
- `self: DecisionMaker`

---

### `09F2` DOES_DECISION_MAKER_EXIST
Returns true if the handle is a valid decision maker handle

**Class:** `DecisionMaker.DoesExist`
**Flags:** condition, static

**Input:**
- `handle: any`

---
