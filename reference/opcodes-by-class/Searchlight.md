# Searchlight Opcodes

> 13 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `06B1` | CREATE_SEARCHLIGHT |  |
| `06B2` | DELETE_SEARCHLIGHT |  |
| `06B3` | DOES_SEARCHLIGHT_EXIST | Returns true if the handle is a valid searchlight handle |
| `06B4` | MOVE_SEARCHLIGHT_BETWEEN_COORDS | Makes the specified searchlight travel between the two specified points with the |
| `06B5` | POINT_SEARCHLIGHT_AT_COORD | Makes the searchlight target move/travel to the specified coords |
| `06B6` | POINT_SEARCHLIGHT_AT_CHAR | Makes the searchlight follow the specified char |
| `06B7` | IS_CHAR_IN_SEARCHLIGHT | Returns true if the searchlight has spotted the char |
| `06BF` | POINT_SEARCHLIGHT_AT_VEHICLE |  |
| `06C0` | IS_VEHICLE_IN_SEARCHLIGHT | Returns true if the searchlights light is on the vehicle |
| `06C1` | CREATE_SEARCHLIGHT_ON_VEHICLE | Creates a searchlight-styled light cone on a car with the specified offset and p |
| `06CA` | ATTACH_SEARCHLIGHT_TO_SEARCHLIGHT_OBJECT | Attaches the searchlight to the specified objects |
| `0941` | SET_SEARCHLIGHT_CLIP_IF_COLLIDING |  |
| `0A02` | SWITCH_ON_GROUND_SEARCHLIGHT | Sets whether the searchlight shows a shadow effect on the surface it hits |

## Detailed Reference

### `06B1` CREATE_SEARCHLIGHT

**Class:** `Searchlight.Create`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `xPoint: float`
- `yPoint: float`
- `zPoint: float`
- `radius: float`
- `radiusPoint: float`

**Output:**
- `handle: Searchlight (variable)`

---

### `06B2` DELETE_SEARCHLIGHT

**Class:** `Searchlight.Delete`
**Flags:** destructor

**Input:**
- `self: Searchlight`

---

### `06B3` DOES_SEARCHLIGHT_EXIST
Returns true if the handle is a valid searchlight handle

**Class:** `Searchlight.DoesExist`
**Flags:** condition, static

**Input:**
- `handle: any`

---

### `06B4` MOVE_SEARCHLIGHT_BETWEEN_COORDS
Makes the specified searchlight travel between the two specified points with the specified speed

**Class:** `Searchlight.MoveBetweenCoords`

**Input:**
- `self: Searchlight`
- `fromX: float`
- `fromY: float`
- `fromZ: float`
- `toX: float`
- `toY: float`
- `toZ: float`
- `speed: float`

---

### `06B5` POINT_SEARCHLIGHT_AT_COORD
Makes the searchlight target move/travel to the specified coords

**Class:** `Searchlight.PointAtCoord`

**Input:**
- `self: Searchlight`
- `x: float`
- `y: float`
- `z: float`
- `speed: float`

---

### `06B6` POINT_SEARCHLIGHT_AT_CHAR
Makes the searchlight follow the specified char

**Class:** `Searchlight.PointAtChar`

**Input:**
- `self: Searchlight`
- `handle: Char`
- `speed: float`

---

### `06B7` IS_CHAR_IN_SEARCHLIGHT
Returns true if the searchlight has spotted the char

**Class:** `Searchlight.IsCharIn`
**Flags:** condition

**Input:**
- `self: Searchlight`
- `handle: Char`

---

### `06BF` POINT_SEARCHLIGHT_AT_VEHICLE

**Class:** `Searchlight.PointAtVehicle`

**Input:**
- `self: Searchlight`
- `handle: Car`
- `speed: float`

---

### `06C0` IS_VEHICLE_IN_SEARCHLIGHT
Returns true if the searchlights light is on the vehicle

**Class:** `Searchlight.IsVehicleIn`
**Flags:** condition

**Input:**
- `self: Searchlight`
- `handle: Car`

---

### `06C1` CREATE_SEARCHLIGHT_ON_VEHICLE
Creates a searchlight-styled light cone on a car with the specified offset and points to a certain point

**Class:** `Searchlight.CreateOnVehicle`
**Flags:** constructor

**Input:**
- `vehicle: Car`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `xPoint: float`
- `yPoint: float`
- `zPoint: float`
- `pointRadius: float`
- `radius: float`

**Output:**
- `handle: Searchlight (variable)`

---

### `06CA` ATTACH_SEARCHLIGHT_TO_SEARCHLIGHT_OBJECT
Attaches the searchlight to the specified objects

**Class:** `Searchlight.AttachToObject`

**Input:**
- `self: Searchlight`
- `spotTower: Object`
- `spotHousing: Object`
- `spotBulb: Object`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`

---

### `0941` SET_SEARCHLIGHT_CLIP_IF_COLLIDING

**Class:** `Searchlight.SetClipIfColliding`

**Input:**
- `self: Searchlight`
- `state: bool`

---

### `0A02` SWITCH_ON_GROUND_SEARCHLIGHT
Sets whether the searchlight shows a shadow effect on the surface it hits

**Class:** `Searchlight.SwitchOnGround`

**Input:**
- `self: Searchlight`
- `state: bool`

---
