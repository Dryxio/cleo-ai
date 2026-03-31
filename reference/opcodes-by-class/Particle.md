# Particle Opcodes

> 13 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `064B` | CREATE_FX_SYSTEM | Creates a particle effect |
| `064C` | PLAY_FX_SYSTEM | Makes the specified particle visible |
| `064E` | STOP_FX_SYSTEM | Stops the specified particle at the source |
| `064F` | PLAY_AND_KILL_FX_SYSTEM | Starts the particle effect and relinquishes script control over it |
| `0650` | KILL_FX_SYSTEM | Stops the particle and deletes it |
| `0669` | CREATE_FX_SYSTEM_ON_CHAR | Creates a particle attached to a character |
| `066A` | CREATE_FX_SYSTEM_ON_CHAR_WITH_DIRECTION | Creates a particle effect attached to a character |
| `066B` | CREATE_FX_SYSTEM_ON_CAR | Creates a particle effect attached to a vehicle |
| `066C` | CREATE_FX_SYSTEM_ON_CAR_WITH_DIRECTION | Creates a particle and attaches it to the specified vehicle with the specified o |
| `066D` | CREATE_FX_SYSTEM_ON_OBJECT | Creates a particle effect on an object |
| `066E` | CREATE_FX_SYSTEM_ON_OBJECT_WITH_DIRECTION | Creates particle effect on an object |
| `0883` | ATTACH_FX_SYSTEM_TO_CHAR_BONE | Attaches the specified particle to the specified character |
| `0976` | KILL_FX_SYSTEM_NOW | Destroys the specified particle |

## Detailed Reference

### `064B` CREATE_FX_SYSTEM
Creates a particle effect

**Class:** `Particle.Create`
**Flags:** constructor

**Input:**
- `name: string`
- `x: float`
- `y: float`
- `z: float`
- `ignoreBoundingChecks: bool`

**Output:**
- `handle: Particle (variable)`

**Details:**

This creates a particle at the coordinates point. It requires PLAY_FX_SYSTEM in order for it to be visible.

---

### `064C` PLAY_FX_SYSTEM
Makes the specified particle visible

**Class:** `Particle.Play`

**Input:**
- `self: Particle`

---

### `064E` STOP_FX_SYSTEM
Stops the specified particle at the source

**Class:** `Particle.Stop`

**Input:**
- `self: Particle`

---

### `064F` PLAY_AND_KILL_FX_SYSTEM
Starts the particle effect and relinquishes script control over it

**Class:** `Particle.PlayAndKill`

**Input:**
- `self: Particle`

---

### `0650` KILL_FX_SYSTEM
Stops the particle and deletes it

**Class:** `Particle.Kill`
**Flags:** destructor

**Input:**
- `self: Particle`

---

### `0669` CREATE_FX_SYSTEM_ON_CHAR
Creates a particle attached to a character

**Class:** `Particle.CreateOnChar`
**Flags:** constructor

**Input:**
- `name: string`
- `char: Char`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `ignoreBoundingChecks: bool`

**Output:**
- `handle: Particle (variable)`

---

### `066A` CREATE_FX_SYSTEM_ON_CHAR_WITH_DIRECTION
Creates a particle effect attached to a character

**Class:** `Particle.CreateOnCharWithDirection`
**Flags:** constructor

**Input:**
- `name: string`
- `char: Char`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `xDirection: float`
- `yDirection: float`
- `zDirection: float`
- `ignoreBoundingChecks: bool`

**Output:**
- `handle: Particle (variable)`

---

### `066B` CREATE_FX_SYSTEM_ON_CAR
Creates a particle effect attached to a vehicle

**Class:** `Particle.CreateOnCar`
**Flags:** constructor

**Input:**
- `name: string`
- `vehicle: Car`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `ignoreBoundingChecks: bool`

**Output:**
- `handle: Particle (variable)`

---

### `066C` CREATE_FX_SYSTEM_ON_CAR_WITH_DIRECTION
Creates a particle and attaches it to the specified vehicle with the specified offset and direction

**Class:** `Particle.CreateOnCarWithDirection`
**Flags:** constructor

**Input:**
- `name: string`
- `vehicle: Car`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `xDirection: float`
- `yDirection: float`
- `zDirection: float`
- `ignoreBoundingChecks: bool`

**Output:**
- `handle: Particle (variable)`

---

### `066D` CREATE_FX_SYSTEM_ON_OBJECT
Creates a particle effect on an object

**Class:** `Particle.CreateOnObject`
**Flags:** constructor

**Input:**
- `name: string`
- `object: Object`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `ignoreBoundingChecks: bool`

**Output:**
- `handle: Particle (variable)`

---

### `066E` CREATE_FX_SYSTEM_ON_OBJECT_WITH_DIRECTION
Creates particle effect on an object

**Class:** `Particle.CreateOnObjectWithDirection`
**Flags:** constructor

**Input:**
- `name: string`
- `object: Object`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `xDirection: float`
- `yDirection: float`
- `zDirection: float`
- `ignoreBoundingChecks: bool`

**Output:**
- `handle: Particle (variable)`

---

### `0883` ATTACH_FX_SYSTEM_TO_CHAR_BONE
Attaches the specified particle to the specified character

**Class:** `Particle.AttachToCharBone`

**Input:**
- `self: Particle`
- `handle: Char`
- `pedBone: PedBone`

---

### `0976` KILL_FX_SYSTEM_NOW
Destroys the specified particle

**Class:** `Particle.KillNow`
**Flags:** destructor

**Input:**
- `self: Particle`

---
