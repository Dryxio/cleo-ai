# Group Opcodes

> 12 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `062F` | CREATE_GROUP | Creates a new group, which multiple characters can be assigned to, allowing cont |
| `0630` | SET_GROUP_LEADER | Puts the specified character into the group as the leader |
| `0631` | SET_GROUP_MEMBER | Puts the specified character into the group as a member |
| `0632` | REMOVE_GROUP | Releases the group |
| `06AD` | SET_GROUP_DECISION_MAKER | Sets the decision maker for a group of characters |
| `06F0` | SET_GROUP_SEPARATION_RANGE | Sets how far members of the group can be from the leader before they are removed |
| `07B3` | SET_GROUP_DEFAULT_TASK_ALLOCATOR |  |
| `07F6` | GET_GROUP_SIZE |  |
| `07FD` | DOES_GROUP_EXIST | Returns true if the handle is a valid group handle |
| `087D` | SET_GROUP_SEQUENCE | Sets the default task sequence for members of the group |
| `092B` | GET_GROUP_MEMBER | Returns the nth group member |
| `0940` | SET_GROUP_FOLLOW_STATUS | Sets whether the group members enter a car when the leader does |

## Detailed Reference

### `062F` CREATE_GROUP
Creates a new group, which multiple characters can be assigned to, allowing control over all of them as a group

**Class:** `Group.Create`
**Flags:** constructor

**Input:**
- `defaultTaskAllocator: DefaultTaskAllocator`

**Output:**
- `handle: Group (variable)`

---

### `0630` SET_GROUP_LEADER
Puts the specified character into the group as the leader

**Class:** `Group.SetLeader`

**Input:**
- `self: Group`
- `handle: Char`

---

### `0631` SET_GROUP_MEMBER
Puts the specified character into the group as a member

**Class:** `Group.SetMember`

**Input:**
- `self: Group`
- `handle: Char`

**Details:**

This command sets the character as a member of the group. This command is similar to SET_PLAYER_AS_LEADER used in GTA3 and Vice City. The character would follow the leader of the group.

---

### `0632` REMOVE_GROUP
Releases the group

**Class:** `Group.Remove`
**Flags:** destructor

**Input:**
- `self: Group`

---

### `06AD` SET_GROUP_DECISION_MAKER
Sets the decision maker for a group of characters

**Class:** `Group.SetDecisionMaker`

**Input:**
- `self: Group`
- `handleOrTemplate: DecisionMakerGroupTemplate`

---

### `06F0` SET_GROUP_SEPARATION_RANGE
Sets how far members of the group can be from the leader before they are removed from the group

**Class:** `Group.SetSeparationRange`

**Input:**
- `self: Group`
- `range: float`

**Details:**

This command sets the separation range of the group. The distance is how far the members of the group can stray around before getting "lost." If a member strays too far from the leader, the member will no longer belong to the group.

---

### `07B3` SET_GROUP_DEFAULT_TASK_ALLOCATOR

**Class:** `Group.SetDefaultTaskAllocator`

**Input:**
- `self: Group`
- `defaultTaskAllocator: DefaultTaskAllocator`

---

### `07F6` GET_GROUP_SIZE

**Class:** `Group.GetSize`

**Input:**
- `self: Group`

**Output:**
- `numLeaders: int (variable)`
- `numMembers: int (variable)`

---

### `07FD` DOES_GROUP_EXIST
Returns true if the handle is a valid group handle

**Class:** `Group.DoesExist`
**Flags:** condition, static

**Input:**
- `handle: any`

---

### `087D` SET_GROUP_SEQUENCE
Sets the default task sequence for members of the group

**Class:** `Group.SetSequence`

**Input:**
- `self: Group`
- `sequence: Sequence`

---

### `092B` GET_GROUP_MEMBER
Returns the nth group member

**Class:** `Group.GetMember`

**Input:**
- `self: Group`
- `slotId: int`

**Output:**
- `handle: Char (variable)`

---

### `0940` SET_GROUP_FOLLOW_STATUS
Sets whether the group members enter a car when the leader does

**Class:** `Group.SetFollowStatus`

**Input:**
- `self: Group`
- `state: bool`

---
