# Fx Opcodes

> 11 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `016F` | DRAW_SHADOW | Draws a shadow in the current frame |
| `020C` | ADD_EXPLOSION | Creates an explosion at the point |
| `024F` | DRAW_CORONA | Displays a corona with fade in-out effect at the specified location |
| `04D5` | DRAW_WEAPONSHOP_CORONA | Displays a corona with the lowered draw distance at the specified coordinates |
| `0565` | ADD_EXPLOSION_NO_SOUND | Creates an explosion with no sound |
| `058A` | ADD_BIG_GUN_FLASH | Creates a gun flash particle effect |
| `08EB` | ADD_SPARKS | Creates single burst of spark particles |
| `0948` | ADD_EXPLOSION_VARIABLE_SHAKE | Creates an explosion at the specified coordinates |
| `095C` | ADD_SMOKE_PARTICLE |  |
| `09B8` | ADD_BLOOD | Creates blood spray and ground splatter effects |
| `09E5` | DRAW_LIGHT_WITH_RANGE | Draws colored light in radius of the specified point |

## Detailed Reference

### `016F` DRAW_SHADOW
Draws a shadow in the current frame

**Class:** `Fx.DrawShadow`
**Flags:** static

**Input:**
- `textureType: ShadowTextureType`
- `x: float`
- `y: float`
- `z: float`
- `angle: float`
- `length: float`
- `intensity: int`
- `r: int`
- `g: int`
- `b: int`

---

### `020C` ADD_EXPLOSION
Creates an explosion at the point

**Class:** `Fx.AddExplosion`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `type: ExplosionType`

---

### `024F` DRAW_CORONA
Displays a corona with fade in-out effect at the specified location

**Class:** `Fx.DrawCorona`
**Flags:** static, positional

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `size: float`
- `coronaType: CoronaType`
- `flareType: FlareType`
- `r: int`
- `g: int`
- `b: int`

---

### `04D5` DRAW_WEAPONSHOP_CORONA
Displays a corona with the lowered draw distance at the specified coordinates

**Class:** `Fx.DrawWeaponshopCorona`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `size: float`
- `coronaType: CoronaType`
- `flareType: FlareType`
- `r: int`
- `g: int`
- `b: int`

---

### `0565` ADD_EXPLOSION_NO_SOUND
Creates an explosion with no sound

**Class:** `Fx.AddExplosionNoSound`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `type: ExplosionType`

---

### `058A` ADD_BIG_GUN_FLASH
Creates a gun flash particle effect

**Class:** `Fx.AddBigGunFlash`
**Flags:** static

**Input:**
- `fromX: float`
- `fromY: float`
- `fromZ: float`
- `toX: float`
- `toY: float`
- `toZ: float`

---

### `08EB` ADD_SPARKS
Creates single burst of spark particles

**Class:** `Fx.AddSparks`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `velocityX: float`
- `velocityY: float`
- `velocityZ: float`
- `density: int`

---

### `0948` ADD_EXPLOSION_VARIABLE_SHAKE
Creates an explosion at the specified coordinates

**Class:** `Fx.AddExplosionVariableShake`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `type: int`
- `shake: float`

---

### `095C` ADD_SMOKE_PARTICLE

**Class:** `Fx.AddSmokeParticle`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `velocityX: float`
- `velocityY: float`
- `velocityZ: float`
- `red: float`
- `green: float`
- `blue: float`
- `alpha: float`
- `size: float`
- `lastFactor: float`

---

### `09B8` ADD_BLOOD
Creates blood spray and ground splatter effects

**Class:** `Fx.AddBlood`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `velocityX: float`
- `velocityY: float`
- `velocityZ: float`
- `density: int`
- `handle: Char`

---

### `09E5` DRAW_LIGHT_WITH_RANGE
Draws colored light in radius of the specified point

**Class:** `Fx.DrawLightWithRange`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `red: int`
- `green: int`
- `blue: int`
- `radius: float`

---
