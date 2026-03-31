# Hud Opcodes

> 24 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `014E` | DISPLAY_ONSCREEN_TIMER | Creates a countdown or countup onscreen timer |
| `014F` | CLEAR_ONSCREEN_TIMER | Removes the onscreen timer |
| `0151` | CLEAR_ONSCREEN_COUNTER | Removes the onscreen counter (0150 or 03C4) |
| `02A3` | SWITCH_WIDESCREEN | Enables widescreen |
| `038D` | DRAW_SPRITE | Draws a loaded texture (038F) at the specified on-screen X and Y coordinates, wi |
| `038E` | DRAW_RECT | Draws a box at the specified screen X and Y position, with the specified size an |
| `0396` | FREEZE_ONSCREEN_TIMER | Makes the on-screen timer stop updating |
| `03C3` | DISPLAY_ONSCREEN_TIMER_WITH_STRING | Creates a countdown or countup onscreen timer with the text |
| `03C4` | DISPLAY_ONSCREEN_COUNTER_WITH_STRING | Displays an onscreen counter with the text, either shown in numbers or as a bar |
| `03E3` | SET_SPRITES_DRAW_BEFORE_FADE | Causes the next texture to be drawn (038D) before the fade is drawn |
| `03E7` | FLASH_HUD_OBJECT | Makes a specific part of the HUD disappear and reappear several times |
| `04F7` | DISPLAY_NTH_ONSCREEN_COUNTER_WITH_STRING | Displays an onscreen counter with the text in the specified slot, either shown i |
| `0581` | DISPLAY_RADAR | Displays or hides the radar |
| `059C` | SET_ONSCREEN_COUNTER_FLASH_WHEN_FIRST_DISPLAYED |  |
| `074B` | DRAW_SPRITE_WITH_ROTATION | This is an extended version of 038D with scale and angle parameters |
| `075B` | SET_RADAR_ZOOM |  |
| `0826` | DISPLAY_HUD | Sets whether the HUD displays |
| `0890` | SET_TIMER_BEEP_COUNTDOWN_TIME | Starts a sound when the countdown timer reaches the specified number of seconds |
| `0904` | GET_HUD_COLOUR | Returns the RGBA of the specified HUD color |
| `0937` | DRAW_WINDOW | Draws a black box with styled text from corner A to corner B |
| `09A3` | DRAW_CROSSHAIR | Sets whether the HUD should always display weapon aiming crosshairs, used in the |
| `09B9` | DISPLAY_CAR_NAMES | Sets whether the name of the current vehicle should be displayed |
| `09BA` | DISPLAY_ZONE_NAMES | Sets whether the area text for the current area should show |
| `09EE` | FORCE_BIG_MESSAGE_AND_COUNTER | Prevents timers and big texts from being hidden if there is another conflicting  |

## Detailed Reference

### `014E` DISPLAY_ONSCREEN_TIMER
Creates a countdown or countup onscreen timer

**Class:** `Hud.DisplayTimer`
**Flags:** static

**Input:**
- `timer: int (global var)`
- `direction: TimerDirection`

---

### `014F` CLEAR_ONSCREEN_TIMER
Removes the onscreen timer

**Class:** `Hud.ClearTimer`
**Flags:** static

**Input:**
- `timer: int (global var)`

---

### `0151` CLEAR_ONSCREEN_COUNTER
Removes the onscreen counter (0150 or 03C4)

**Class:** `Hud.ClearCounter`
**Flags:** static

**Input:**
- `counter: int (global var)`

---

### `02A3` SWITCH_WIDESCREEN
Enables widescreen

**Class:** `Hud.SwitchWidescreen`
**Flags:** static

**Input:**
- `state: bool`

---

### `038D` DRAW_SPRITE
Draws a loaded texture (038F) at the specified on-screen X and Y coordinates, with the specified size and RGBA color

**Class:** `Hud.DrawSprite`
**Flags:** static

**Input:**
- `spriteSlot: int`
- `offsetLeft: float`
- `offsetTop: float`
- `width: float`
- `height: float`
- `r: int`
- `g: int`
- `b: int`
- `a: int`

---

### `038E` DRAW_RECT
Draws a box at the specified screen X and Y position, with the specified size and RGBA colors

**Class:** `Hud.DrawRect`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `width: float`
- `height: float`
- `r: int`
- `g: int`
- `b: int`
- `a: int`

---

### `0396` FREEZE_ONSCREEN_TIMER
Makes the on-screen timer stop updating

**Class:** `Hud.FreezeTimer`
**Flags:** static

**Input:**
- `state: bool`

---

### `03C3` DISPLAY_ONSCREEN_TIMER_WITH_STRING
Creates a countdown or countup onscreen timer with the text

**Class:** `Hud.DisplayTimerWithString`
**Flags:** static

**Input:**
- `timer: int (global var)`
- `direction: TimerDirection`
- `text: gxt_key`

---

### `03C4` DISPLAY_ONSCREEN_COUNTER_WITH_STRING
Displays an onscreen counter with the text, either shown in numbers or as a bar

**Class:** `Hud.DisplayCounterWithString`
**Flags:** static

**Input:**
- `counter: int (global var)`
- `display: CounterDisplay`
- `text: gxt_key`

---

### `03E3` SET_SPRITES_DRAW_BEFORE_FADE
Causes the next texture to be drawn (038D) before the fade is drawn

**Class:** `Hud.SetSpritesDrawBeforeFade`
**Flags:** static

**Input:**
- `state: bool`

---

### `03E7` FLASH_HUD_OBJECT
Makes a specific part of the HUD disappear and reappear several times

**Class:** `Hud.FlashObject`
**Flags:** static

**Input:**
- `object: HudObject`

---

### `04F7` DISPLAY_NTH_ONSCREEN_COUNTER_WITH_STRING
Displays an onscreen counter with the text in the specified slot, either shown in numbers or as a bar

**Class:** `Hud.DisplayNthCounterWithString`
**Flags:** static

**Input:**
- `counter: int (global var)`
- `display: CounterDisplay`
- `slot: int`
- `text: gxt_key`

---

### `0581` DISPLAY_RADAR
Displays or hides the radar

**Class:** `Hud.DisplayRadar`
**Flags:** static

**Input:**
- `state: bool`

---

### `059C` SET_ONSCREEN_COUNTER_FLASH_WHEN_FIRST_DISPLAYED

**Class:** `Hud.SetCounterFlashWhenFirstDisplayed`
**Flags:** static

**Input:**
- `counter: int (global var)`
- `state: bool`

---

### `074B` DRAW_SPRITE_WITH_ROTATION
This is an extended version of 038D with scale and angle parameters

**Class:** `Hud.DrawSpriteWithRotation`
**Flags:** static

**Input:**
- `spriteSlot: int`
- `offsetLeft: float`
- `offsetTop: float`
- `width: float`
- `height: float`
- `angle: float`
- `red: int`
- `green: int`
- `blue: int`
- `alpha: int`

---

### `075B` SET_RADAR_ZOOM

**Class:** `Hud.SetRadarZoom`
**Flags:** static

**Input:**
- `zoom: int`

**Details:**

This command zooms in the radar. Using any negative value it will flip the map upside down. The equivalent US v1.0 memory address is `0x0A444A3` (1 byte).

---

### `0826` DISPLAY_HUD
Sets whether the HUD displays

**Class:** `Hud.Display`
**Flags:** static

**Input:**
- `state: bool`

---

### `0890` SET_TIMER_BEEP_COUNTDOWN_TIME
Starts a sound when the countdown timer reaches the specified number of seconds

**Class:** `Hud.SetTimerBeepCountdownTime`
**Flags:** static

**Input:**
- `timer: int (global var)`
- `timeInSec: int`

---

### `0904` GET_HUD_COLOUR
Returns the RGBA of the specified HUD color

**Class:** `Hud.GetColor`
**Flags:** static

**Input:**
- `color: HudColors`

**Output:**
- `red: int (variable)`
- `green: int (variable)`
- `blue: int (variable)`
- `alpha: int (variable)`

---

### `0937` DRAW_WINDOW
Draws a black box with styled text from corner A to corner B

**Class:** `Hud.DrawWindow`
**Flags:** static

**Input:**
- `leftTopX: float`
- `leftTopY: float`
- `rightBottomX: float`
- `rightBottomY: float`
- `header: gxt_key`
- `zIndex: int`

---

### `09A3` DRAW_CROSSHAIR
Sets whether the HUD should always display weapon aiming crosshairs, used in the mission 'Catalyst' where the player must throw crates of ammo to Ryder

**Class:** `Hud.DrawCrosshair`
**Flags:** static

**Input:**
- `state: bool`

---

### `09B9` DISPLAY_CAR_NAMES
Sets whether the name of the current vehicle should be displayed

**Class:** `Hud.DisplayCarNames`
**Flags:** static

**Input:**
- `state: bool`

---

### `09BA` DISPLAY_ZONE_NAMES
Sets whether the area text for the current area should show

**Class:** `Hud.DisplayZoneNames`
**Flags:** static

**Input:**
- `state: bool`

---

### `09EE` FORCE_BIG_MESSAGE_AND_COUNTER
Prevents timers and big texts from being hidden if there is another conflicting type of text on screen

**Class:** `Hud.ForceBigMessageAndCounter`
**Flags:** static

**Input:**
- `state: bool`

---
