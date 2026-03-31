# Blip Opcodes

> 22 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0161` | ADD_BLIP_FOR_CAR_OLD | Adds a blip with properties to the vehicle |
| `0164` | REMOVE_BLIP | Removes the blip |
| `0165` | CHANGE_BLIP_COLOUR | Sets the blip's color |
| `0167` | ADD_BLIP_FOR_COORD_OLD | Adds a blip with properties at the location |
| `0168` | CHANGE_BLIP_SCALE | Sets the blip's size |
| `0186` | ADD_BLIP_FOR_CAR | Adds a blip and a marker to the vehicle |
| `0187` | ADD_BLIP_FOR_CHAR | Adds a blip and a marker to the character |
| `0188` | ADD_BLIP_FOR_OBJECT | Adds a blip and a marker to the object |
| `018A` | ADD_BLIP_FOR_COORD | Adds a blip to the location |
| `018B` | CHANGE_BLIP_DISPLAY | Changes the display of the specified blip |
| `02A7` | ADD_SPRITE_BLIP_FOR_CONTACT_POINT | Adds a long range sprite blip and sphere to the contact point that is not displa |
| `02A8` | ADD_SPRITE_BLIP_FOR_COORD | Adds a sprite blip to the location |
| `03DC` | ADD_BLIP_FOR_PICKUP | Adds a blip and a marker to the pickup |
| `04CE` | ADD_SHORT_RANGE_SPRITE_BLIP_FOR_COORD | Adds a sprite blip for the specified coordinates |
| `0570` | ADD_SHORT_RANGE_SPRITE_BLIP_FOR_CONTACT_POINT | Adds a short range sprite blip and sphere to the contact point that is not displ |
| `06C4` | ADD_BLIP_FOR_SEARCHLIGHT | Creates a blip indicating the searchlights position on the radar |
| `075C` | DOES_BLIP_EXIST | Returns true if the handle is a valid blip handle |
| `07BF` | SET_BLIP_ALWAYS_DISPLAY_ON_ZOOMED_RADAR | Sets whether the tracking blip will remain regardless of the entities existance |
| `07E0` | SET_BLIP_AS_FRIENDLY |  |
| `0888` | ADD_BLIP_FOR_DEAD_CHAR | Adds a blip and a marker to the character (identical to 0187) |
| `08DC` | SET_BLIP_ENTRY_EXIT | Assigns the blip to the specified entrance/exit marker |
| `08FB` | SET_COORD_BLIP_APPEARANCE | Works similar to 0165, except this command does not work on tracking blips, has  |

## Detailed Reference

### `0161` ADD_BLIP_FOR_CAR_OLD
Adds a blip with properties to the vehicle

**Class:** `Blip.AddForCarOld`
**Flags:** constructor

**Input:**
- `vehicle: Car`
- `color: BlipColor`
- `display: BlipDisplay`

**Output:**
- `handle: Blip (variable)`

---

### `0164` REMOVE_BLIP
Removes the blip

**Class:** `Blip.Remove`
**Flags:** destructor

**Input:**
- `self: Blip`

---

### `0165` CHANGE_BLIP_COLOUR
Sets the blip's color

**Class:** `Blip.ChangeColor`

**Input:**
- `self: Blip`
- `color: BlipColor`

---

### `0167` ADD_BLIP_FOR_COORD_OLD
Adds a blip with properties at the location

**Class:** `Blip.AddForCoordOld`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `colour: BlipColor`
- `display: BlipDisplay`

**Output:**
- `handle: Blip (variable)`

---

### `0168` CHANGE_BLIP_SCALE
Sets the blip's size

**Class:** `Blip.ChangeScale`

**Input:**
- `self: Blip`
- `size: int`

---

### `0186` ADD_BLIP_FOR_CAR
Adds a blip and a marker to the vehicle

**Class:** `Blip.AddForCar`
**Flags:** constructor

**Input:**
- `vehicle: Car`

**Output:**
- `handle: Blip (variable)`

**Details:**

This command adds a square blip in the radar denoting the location of the vehicle and a red marker (arrow) above the vehicle. It is almost equivalent to ADD_BLIP_FOR_CAR_OLD but the properties of the blip are preset. The default properties of the blip, which can be changed using other commands, are:

- Color: 7 (red)
- Scale: 3
- Display: 3 (both blip and marker)

Both the blip and marker can be removed using REMOVE_BLIP.

---

### `0187` ADD_BLIP_FOR_CHAR
Adds a blip and a marker to the character

**Class:** `Blip.AddForChar`
**Flags:** constructor

**Input:**
- `char: Char`

**Output:**
- `handle: Blip (variable)`

**Details:**

This command adds a square blip in the radar denoting the location of the character and a red marker (arrow) above the character. It is almost equivalent to ADD_BLIP_FOR_CHAR_OLD but the properties of the blip are preset. The default properties of the blip, which can be changed using other commands, are:

- Color: 7 (red)
- Scale: 3
- Display: 3 (both blip and marker)

Both the blip and marker can be removed using REMOVE_BLIP.

---

### `0188` ADD_BLIP_FOR_OBJECT
Adds a blip and a marker to the object

**Class:** `Blip.AddForObject`
**Flags:** constructor

**Input:**
- `object: Object`

**Output:**
- `handle: Blip (variable)`

**Details:**

This command adds a square blip in the radar denoting the location of the object and a red marker (arrow) above the object. It is almost equivalent to ADD_BLIP_FOR_OBJECT_OLD but the properties of the blip are preset. The default properties of the blip, which can be changed using other commands, are:

- Color: 1 (green)
- Scale: 3
- Display: 3 (both blip and marker)

Both the blip and marker can be removed using REMOVE_BLIP.

---

### `018A` ADD_BLIP_FOR_COORD
Adds a blip to the location

**Class:** `Blip.AddForCoord`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `handle: Blip (variable)`

---

### `018B` CHANGE_BLIP_DISPLAY
Changes the display of the specified blip

**Class:** `Blip.ChangeDisplay`

**Input:**
- `self: Blip`
- `display: BlipDisplay`

---

### `02A7` ADD_SPRITE_BLIP_FOR_CONTACT_POINT
Adds a long range sprite blip and sphere to the contact point that is not displayed while on mission

**Class:** `Blip.AddSpriteForContactPoint`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `sprite: RadarSprite`

**Output:**
- `handle: Blip (variable)`

---

### `02A8` ADD_SPRITE_BLIP_FOR_COORD
Adds a sprite blip to the location

**Class:** `Blip.AddSpriteForCoord`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `sprite: RadarSprite`

**Output:**
- `handle: Blip (variable)`

---

### `03DC` ADD_BLIP_FOR_PICKUP
Adds a blip and a marker to the pickup

**Class:** `Blip.AddForPickup`
**Flags:** constructor

**Input:**
- `pickup: Pickup`

**Output:**
- `handle: Blip (variable)`

---

### `04CE` ADD_SHORT_RANGE_SPRITE_BLIP_FOR_COORD
Adds a sprite blip for the specified coordinates

**Class:** `Blip.AddShortRangeSpriteForCoord`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `sprite: RadarSprite`

**Output:**
- `handle: Blip (variable)`

---

### `0570` ADD_SHORT_RANGE_SPRITE_BLIP_FOR_CONTACT_POINT
Adds a short range sprite blip and sphere to the contact point that is not displayed while on mission

**Class:** `Blip.AddShortRangeSpriteForContactPoint`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `sprite: RadarSprite`

**Output:**
- `handle: Blip (variable)`

---

### `06C4` ADD_BLIP_FOR_SEARCHLIGHT
Creates a blip indicating the searchlights position on the radar

**Class:** `Blip.AddForSearchlight`
**Flags:** constructor

**Input:**
- `searchlight: Searchlight`

**Output:**
- `handle: Blip (variable)`

---

### `075C` DOES_BLIP_EXIST
Returns true if the handle is a valid blip handle

**Class:** `Blip.DoesExist`
**Flags:** condition, static

**Input:**
- `handle: any`

---

### `07BF` SET_BLIP_ALWAYS_DISPLAY_ON_ZOOMED_RADAR
Sets whether the tracking blip will remain regardless of the entities existance

**Class:** `Blip.SetAlwaysDisplayOnZoomedRadar`

**Input:**
- `self: Blip`
- `state: bool`

---

### `07E0` SET_BLIP_AS_FRIENDLY

**Class:** `Blip.SetAsFriendly`

**Input:**
- `self: Blip`
- `state: bool`

---

### `0888` ADD_BLIP_FOR_DEAD_CHAR
Adds a blip and a marker to the character (identical to 0187)

**Class:** `Blip.AddForDeadChar`
**Flags:** constructor

**Input:**
- `char: Char`

**Output:**
- `handle: Blip (variable)`

---

### `08DC` SET_BLIP_ENTRY_EXIT
Assigns the blip to the specified entrance/exit marker

**Class:** `Blip.SetEntryExit`

**Input:**
- `self: Blip`
- `x: float`
- `y: float`
- `radius: float`

---

### `08FB` SET_COORD_BLIP_APPEARANCE
Works similar to 0165, except this command does not work on tracking blips, has different colors and does not support direct RGBA setting

**Class:** `Blip.SetCoordAppearance`

**Input:**
- `self: Blip`
- `color: CoordAppearance`

---
