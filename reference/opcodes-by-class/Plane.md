# Plane Opcodes

> 9 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `04D2` | PLANE_GOTO_COORDS |  |
| `070E` | PLANE_ATTACK_PLAYER | Sets the planes mission to attack the player |
| `070F` | PLANE_FLY_IN_DIRECTION |  |
| `0710` | PLANE_FOLLOW_ENTITY |  |
| `0742` | SET_PLANE_THROTTLE |  |
| `0745` | PLANE_STARTS_IN_AIR | Provides the aircraft with full power so it can start flying mid-air |
| `08A2` | PLANE_ATTACK_PLAYER_USING_DOG_FIGHT | Sets the plane mission to attack the player while maintaining the minimum altitu |
| `08E6` | SET_PLANE_UNDERCARRIAGE_UP | Sets whether the plane's landing wheels are up |
| `091F` | GET_PLANE_UNDERCARRIAGE_POSITION |  |

## Detailed Reference

### `04D2` PLANE_GOTO_COORDS

**Class:** `Plane.GotoCoords`

**Input:**
- `self: Plane`
- `x: float`
- `y: float`
- `z: float`
- `minAltitude: float`
- `maxAltitude: float`

---

### `070E` PLANE_ATTACK_PLAYER
Sets the planes mission to attack the player

**Class:** `Plane.AttackPlayer`

**Input:**
- `self: Plane`
- `handle: Player`
- `radius: float`

---

### `070F` PLANE_FLY_IN_DIRECTION

**Class:** `Plane.FlyInDirection`

**Input:**
- `self: Plane`
- `heading: float`
- `minAltitude: float`
- `maxAltitude: float`

---

### `0710` PLANE_FOLLOW_ENTITY

**Class:** `Plane.FollowEntity`

**Input:**
- `self: Plane`
- `char: Char`
- `vehicle: Car`
- `altitude: float`

---

### `0742` SET_PLANE_THROTTLE

**Class:** `Plane.SetThrottle`

**Input:**
- `self: Plane`
- `throttle: float`

---

### `0745` PLANE_STARTS_IN_AIR
Provides the aircraft with full power so it can start flying mid-air

**Class:** `Plane.StartsInAir`

**Input:**
- `self: Plane`

---

### `08A2` PLANE_ATTACK_PLAYER_USING_DOG_FIGHT
Sets the plane mission to attack the player while maintaining the minimum altitude

**Class:** `Plane.AttackPlayerUsingDogFight`

**Input:**
- `self: Plane`
- `player: Player`
- `altitude: float`

---

### `08E6` SET_PLANE_UNDERCARRIAGE_UP
Sets whether the plane's landing wheels are up

**Class:** `Plane.SetUndercarriageUp`

**Input:**
- `self: Plane`
- `state: bool`

---

### `091F` GET_PLANE_UNDERCARRIAGE_POSITION

**Class:** `Plane.GetUndercarriagePosition`

**Input:**
- `self: Plane`

**Output:**
- `position: float (variable)`

---
