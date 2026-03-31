# CarGenerator Opcodes

> 7 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `014B` | CREATE_CAR_GENERATOR | Initializes a parked car generator (modelId -1 selects a random vehicle from the |
| `014C` | SWITCH_CAR_GENERATOR | Specifies the number of times the car generator spawns a car (101 - infinite) |
| `0732` | SUPPRESS_CAR_MODEL | Prevents the specified car model from spawning for car generators |
| `0733` | DONT_SUPPRESS_CAR_MODEL | Allows the specified car model to spawn for car generators |
| `0734` | DONT_SUPPRESS_ANY_CAR_MODELS | Resets the disabled car model list for car generators |
| `09E2` | CREATE_CAR_GENERATOR_WITH_PLATE | Creates a parked car generator with a number plate (modelId -1 selects a random  |
| `0A17` | SET_HAS_BEEN_OWNED_FOR_CAR_GENERATOR | Sets whether the player will not receive a wanted level when entering a vehicle  |

## Detailed Reference

### `014B` CREATE_CAR_GENERATOR
Initializes a parked car generator (modelId -1 selects a random vehicle from the local popcycle)

**Class:** `CarGenerator.Create`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `heading: float`
- `modelId: model_vehicle`
- `primaryColor: int`
- `secondaryColor: int`
- `forceSpawn: bool`
- `alarmChance: int`
- `doorLockChance: int`
- `minDelay: int`
- `maxDelay: int`

**Output:**
- `handle: CarGenerator (variable)`

---

### `014C` SWITCH_CAR_GENERATOR
Specifies the number of times the car generator spawns a car (101 - infinite)

**Class:** `CarGenerator.Switch`

**Input:**
- `self: CarGenerator`
- `amount: int`

---

### `0732` SUPPRESS_CAR_MODEL
Prevents the specified car model from spawning for car generators

**Class:** `CarGenerator.SuppressCarModel`
**Flags:** static

**Input:**
- `model: model_vehicle`

---

### `0733` DONT_SUPPRESS_CAR_MODEL
Allows the specified car model to spawn for car generators

**Class:** `CarGenerator.DontSuppressCarModel`
**Flags:** static

**Input:**
- `modelId: model_vehicle`

---

### `0734` DONT_SUPPRESS_ANY_CAR_MODELS
Resets the disabled car model list for car generators

**Class:** `CarGenerator.DontSuppressAnyCarModels`
**Flags:** static

---

### `09E2` CREATE_CAR_GENERATOR_WITH_PLATE
Creates a parked car generator with a number plate (modelId -1 selects a random vehicle from the local popcycle)

**Class:** `CarGenerator.CreateWithPlate`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `heading: float`
- `modelId: model_vehicle`
- `primaryColor: int`
- `secondaryColor: int`
- `forceSpawn: bool`
- `alarmChance: int`
- `doorLockChance: int`
- `minDelay: int`
- `maxDelay: int`
- `plateName: string`

**Output:**
- `handle: CarGenerator (variable)`

---

### `0A17` SET_HAS_BEEN_OWNED_FOR_CAR_GENERATOR
Sets whether the player will not receive a wanted level when entering a vehicle from this generator when the police is around

**Class:** `CarGenerator.SetHasBeenOwned`

**Input:**
- `self: CarGenerator`
- `state: bool`

---
