# Rc Opcodes

> 6 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `046E` | GIVE_REMOTE_CONTROLLED_MODEL_TO_PLAYER | Puts the player in control of a remote-control vehicle |
| `0484` | GET_REMOTE_CONTROLLED_CAR | Returns the player's radio-controlled vehicle (alts:00D9,03C0,0811) |
| `048A` | SET_ENABLE_RC_DETONATE | Enables a remote-control vehicle detonation |
| `04D6` | SET_ENABLE_RC_DETONATE_ON_CONTACT | Sets whether RC Bandits detonate on contact with the wheels of any four-wheeled  |
| `04DB` | REMOVE_RC_BUGGY | Exits remote-control mode |
| `0715` | TAKE_REMOTE_CONTROL_OF_CAR | Puts the specified player in control of a remote-control vehicle |

## Detailed Reference

### `046E` GIVE_REMOTE_CONTROLLED_MODEL_TO_PLAYER
Puts the player in control of a remote-control vehicle

**Class:** `Rc.GiveModelToPlayer`
**Flags:** static

**Input:**
- `handle: Player`
- `x: float`
- `y: float`
- `z: float`
- `angle: float`
- `modelId: model_vehicle`

---

### `0484` GET_REMOTE_CONTROLLED_CAR
Returns the player's radio-controlled vehicle (alts:00D9,03C0,0811)

**Class:** `Rc.GetCar`
**Flags:** static

**Input:**
- `player: Player`

**Output:**
- `car: Car (variable)`

---

### `048A` SET_ENABLE_RC_DETONATE
Enables a remote-control vehicle detonation

**Class:** `Rc.SetEnableDetonate`
**Flags:** static

**Input:**
- `state: bool`

---

### `04D6` SET_ENABLE_RC_DETONATE_ON_CONTACT
Sets whether RC Bandits detonate on contact with the wheels of any four-wheeled vehicles

**Class:** `Rc.SetEnableDetonateOnContact`
**Flags:** static

**Input:**
- `state: bool`

---

### `04DB` REMOVE_RC_BUGGY
Exits remote-control mode

**Class:** `Rc.RemoveBuggy`
**Flags:** static

---

### `0715` TAKE_REMOTE_CONTROL_OF_CAR
Puts the specified player in control of a remote-control vehicle

**Class:** `Rc.TakeCar`
**Flags:** static

**Input:**
- `player: Player`
- `vehicle: Car`

---
