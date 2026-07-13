# Weather Opcodes

> 5 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `01B5` | FORCE_WEATHER | Forces the game weather to the specified type |
| `01B6` | FORCE_WEATHER_NOW | Forces the upcoming weather to the specified type |
| `01B7` | RELEASE_WEATHER | Allows the game to continue its usual weather pattern after using 01B5 |
| `08FD` | SET_HEATHAZE_EFFECT | Specifies whether the heat haze effect should be enabled in sunny conditions |
| `0915` | SET_WEATHER_TO_APPROPRIATE_TYPE_NOW | Sets the weather appropriate to the weather region the player is currently in |

## Detailed Reference

### `01B5` FORCE_WEATHER
Forces the game weather to the specified type

**Class:** `Weather.Force`
**Flags:** static

**Input:**
- `type: WeatherType`

---

### `01B6` FORCE_WEATHER_NOW
Forces the upcoming weather to the specified type

**Class:** `Weather.ForceNow`
**Flags:** static

**Input:**
- `type: WeatherType`

---

### `01B7` RELEASE_WEATHER
Allows the game to continue its usual weather pattern after using 01B5

**Class:** `Weather.Release`
**Flags:** static

---

### `08FD` SET_HEATHAZE_EFFECT
Specifies whether the heat haze effect should be enabled in sunny conditions

**Class:** `Weather.SetHeathazeEffect`
**Flags:** static

**Input:**
- `state: bool`

**Details:**

This command sets the heat haze weather effect. A change in weather that has the heat haze effect will enable the effect.

---

### `0915` SET_WEATHER_TO_APPROPRIATE_TYPE_NOW
Sets the weather appropriate to the weather region the player is currently in

**Class:** `Weather.SetToAppropriateTypeNow`
**Flags:** static

---
