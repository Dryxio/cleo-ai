# Heli Opcodes

> 18 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `04A2` | HELI_GOTO_COORDS | Makes the helicopter fly to the specified location, keeping a specific Z height/ |
| `04D0` | SET_HELI_ORIENTATION | Forces the heli rotation relative to the north |
| `04D1` | CLEAR_HELI_ORIENTATION | Resets the heli rotation set with 04D0 |
| `04DF` | SET_HELI_STABILISER | Limits the amount a helicopter can tilt |
| `0541` | FIRE_HUNTER_GUN | Makes the Hunter helicopter fire cannon gun |
| `0564` | MAKE_HELI_COME_CRASHING_DOWN | Makes helicopter simulate crash landing, exploding on the way if high up |
| `0724` | HELI_ATTACK_PLAYER | Makes the heli follow and attack the current player in the given radius |
| `0726` | HELI_FOLLOW_ENTITY | Makes the heli follow the specified char or vehicle in the air |
| `0727` | POLICE_HELI_CHASE_ENTITY | Makes the helicopter hunt down the character or the vehicle within the specified |
| `0743` | HELI_LAND_AT_COORDS |  |
| `0780` | HELI_KEEP_ENTITY_IN_VIEW |  |
| `0788` | ATTACH_WINCH_TO_HELI |  |
| `0789` | RELEASE_ENTITY_FROM_WINCH |  |
| `078B` | GRAB_ENTITY_ON_WINCH | Retrieves the entity attached to the heli's magnet and returns to specific varia |
| `07BB` | ACTIVATE_HELI_SPEED_CHEAT | Provides the heli with extra thrust power |
| `0825` | SET_HELI_BLADES_FULL_SPEED | Makes the helicopter rotor spin at full speed instantly |
| `0853` | SET_HELI_REACHED_TARGET_DISTANCE |  |
| `0A1C` | DISABLE_HELI_AUDIO | Sets whether the helicopter sound is muted |

## Detailed Reference

### `04A2` HELI_GOTO_COORDS
Makes the helicopter fly to the specified location, keeping a specific Z height/altitude

**Class:** `Heli.GotoCoords`

**Input:**
- `self: Heli`
- `x: float`
- `y: float`
- `z: float`
- `minAltitude: float`
- `maxAltitude: float`

---

### `04D0` SET_HELI_ORIENTATION
Forces the heli rotation relative to the north

**Class:** `Heli.SetOrientation`

**Input:**
- `self: Heli`
- `angle: float`

---

### `04D1` CLEAR_HELI_ORIENTATION
Resets the heli rotation set with 04D0

**Class:** `Heli.ClearOrientation`

**Input:**
- `self: Heli`

---

### `04DF` SET_HELI_STABILISER
Limits the amount a helicopter can tilt

**Class:** `Heli.SetStabiliser`

**Input:**
- `self: Heli`
- `state: bool`

---

### `0541` FIRE_HUNTER_GUN
Makes the Hunter helicopter fire cannon gun

**Class:** `Heli.FireHunterGun`

**Input:**
- `self: Heli`

**Details:**

This command is normally used to fire the guns on the Hunter and Sea Sparrow but the command can be used on any vehicles. All vehicles have a vehicle-mounted gun but the gun is situated too low for any practical use on land vehicles. It is much more useful on airborne vehicles. The gun can do damage and can alert the police. The command doesn't control vehicle-mounted rockets.

Using the command once will fire one bullet. It has to be in a loop in order to fire constantly. In San Andreas, it will fire like a Hunter but the firing sound will not go away until the vehicle is gone.

---

### `0564` MAKE_HELI_COME_CRASHING_DOWN
Makes helicopter simulate crash landing, exploding on the way if high up

**Class:** `Heli.MakeComeCrashingDown`

**Input:**
- `self: Heli`

---

### `0724` HELI_ATTACK_PLAYER
Makes the heli follow and attack the current player in the given radius

**Class:** `Heli.AttackPlayer`

**Input:**
- `self: Heli`
- `handle: Player`
- `radius: float`

---

### `0726` HELI_FOLLOW_ENTITY
Makes the heli follow the specified char or vehicle in the air

**Class:** `Heli.FollowEntity`

**Input:**
- `self: Heli`
- `char: Char`
- `vehicle: Car`
- `radius: float`

---

### `0727` POLICE_HELI_CHASE_ENTITY
Makes the helicopter hunt down the character or the vehicle within the specified radius

**Class:** `Heli.ChaseEntity`

**Input:**
- `self: Heli`
- `char: Char`
- `vehicle: Car`
- `radius: float`

---

### `0743` HELI_LAND_AT_COORDS

**Class:** `Heli.LandAtCoords`

**Input:**
- `self: Heli`
- `x: float`
- `y: float`
- `z: float`
- `minAltitude: float`
- `maxAltitude: float`

---

### `0780` HELI_KEEP_ENTITY_IN_VIEW

**Class:** `Heli.KeepEntityInView`

**Input:**
- `self: Heli`
- `char: Char`
- `vehicle: Car`
- `minAltitude: float`
- `maxAltitude: float`

---

### `0788` ATTACH_WINCH_TO_HELI

**Class:** `Heli.AttachWinch`

**Input:**
- `self: Heli`
- `state: bool`

---

### `0789` RELEASE_ENTITY_FROM_WINCH

**Class:** `Heli.ReleaseEntityFromWinch`

**Input:**
- `self: Heli`

---

### `078B` GRAB_ENTITY_ON_WINCH
Retrieves the entity attached to the heli's magnet and returns to specific variables depending on the entities type

**Class:** `Heli.GrabEntityOnWinch`

**Input:**
- `self: Heli`

**Output:**
- `char: Char (variable)`
- `vehicle: Car (variable)`
- `object: Object (variable)`

---

### `07BB` ACTIVATE_HELI_SPEED_CHEAT
Provides the heli with extra thrust power

**Class:** `Heli.ActivateSpeedCheat`

**Input:**
- `self: Heli`
- `power: int`

---

### `0825` SET_HELI_BLADES_FULL_SPEED
Makes the helicopter rotor spin at full speed instantly

**Class:** `Heli.SetBladesFullSpeed`

**Input:**
- `self: Heli`

**Details:**

This command instantly starts the rotor of a helicopter so you don't need to wait for it to start. You cannot use this command on any other vehicles.

---

### `0853` SET_HELI_REACHED_TARGET_DISTANCE

**Class:** `Heli.SetReachedTargetDistance`

**Input:**
- `self: Heli`
- `distance: int`

---

### `0A1C` DISABLE_HELI_AUDIO
Sets whether the helicopter sound is muted

**Class:** `Heli.DisableAudio`

**Input:**
- `self: Heli`
- `state: bool`

---
