# Pickup Opcodes

> 14 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0213` | CREATE_PICKUP | Creates a pickup with the given model and type |
| `0214` | HAS_PICKUP_BEEN_COLLECTED | Returns true if specified pickup has been collected |
| `0215` | REMOVE_PICKUP | Destroys the specified pickup, freeing game memory |
| `02E1` | CREATE_MONEY_PICKUP | Creates a money pickup with the specified cash value |
| `032B` | CREATE_PICKUP_WITH_AMMO | Creates a weapon pickup, giving the player the specified amount of ammo when the |
| `04A6` | CREATE_PROTECTION_PICKUP | Creates an asset revenue pickup |
| `0517` | CREATE_LOCKED_PROPERTY_PICKUP | Creates an asset icon for an asset that is not for sale |
| `0518` | CREATE_FORSALE_PROPERTY_PICKUP | Creates an asset pickup for an asset which can be bought |
| `065B` | GET_PICKUP_COORDINATES | Returns the X, Y and Z coordinates of the pickup |
| `094A` | UPDATE_PICKUP_MONEY_PER_DAY |  |
| `0958` | CREATE_SNAPSHOT_PICKUP | Creates a collectible snapshot at the specified coordinates |
| `0959` | CREATE_HORSESHOE_PICKUP | Creates a collectible horseshoe at the specified coordinates |
| `095A` | CREATE_OYSTER_PICKUP | Creates a collectible oyster at the specified coordinates |
| `09D1` | DOES_PICKUP_EXIST | Returns true if the handle is a valid pickup handle |

## Detailed Reference

### `0213` CREATE_PICKUP
Creates a pickup with the given model and type

**Class:** `Pickup.Create`
**Flags:** constructor

**Input:**
- `modelId: model_object`
- `pickupType: PickupType`
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `handle: Pickup (variable)`

---

### `0214` HAS_PICKUP_BEEN_COLLECTED
Returns true if specified pickup has been collected

**Class:** `Pickup.HasBeenCollected`
**Flags:** condition

**Input:**
- `self: Pickup`

---

### `0215` REMOVE_PICKUP
Destroys the specified pickup, freeing game memory

**Class:** `Pickup.Remove`
**Flags:** destructor

**Input:**
- `self: Pickup`

---

### `02E1` CREATE_MONEY_PICKUP
Creates a money pickup with the specified cash value

**Class:** `Pickup.CreateMoney`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `cashAmount: int`
- `permanent: bool`

**Output:**
- `handle: Pickup (variable)`

---

### `032B` CREATE_PICKUP_WITH_AMMO
Creates a weapon pickup, giving the player the specified amount of ammo when they pick it up

**Class:** `Pickup.CreateWithAmmo`
**Flags:** constructor

**Input:**
- `modelId: model_object`
- `pickupType: PickupType`
- `ammo: int`
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `handle: Pickup (variable)`

---

### `04A6` CREATE_PROTECTION_PICKUP
Creates an asset revenue pickup

**Class:** `Pickup.CreateProtection`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `revenueLimit: int`
- `revenueRate: int`

**Output:**
- `handle: Pickup (variable)`

---

### `0517` CREATE_LOCKED_PROPERTY_PICKUP
Creates an asset icon for an asset that is not for sale

**Class:** `Pickup.CreateLockedProperty`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `message: gxt_key`

**Output:**
- `handle: Pickup (variable)`

---

### `0518` CREATE_FORSALE_PROPERTY_PICKUP
Creates an asset pickup for an asset which can be bought

**Class:** `Pickup.CreateForSaleProperty`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `price: int`
- `message: gxt_key`

**Output:**
- `handle: Pickup (variable)`

---

### `065B` GET_PICKUP_COORDINATES
Returns the X, Y and Z coordinates of the pickup

**Class:** `Pickup.GetCoordinates`

**Input:**
- `self: Pickup`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `094A` UPDATE_PICKUP_MONEY_PER_DAY

**Class:** `Pickup.UpdateMoneyPerDay`

**Input:**
- `self: Pickup`
- `value: int`

---

### `0958` CREATE_SNAPSHOT_PICKUP
Creates a collectible snapshot at the specified coordinates

**Class:** `Pickup.CreateSnapshot`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `handle: Pickup (variable)`

**Details:**

This creates a photo op pickup. The pickup can only be seen through a camera and it glows at night time without the camera. The only way to "pick" this up is to take a picture of it with a camera. The pickup will disappear after that and it gets recorded in stat 231. The total amount of snapshots taken depends on the amount of pickups you have placed. Taking a photo of one pickup gives you $100. Taking a photo of all the pickups will give you $10000. You can only take a picture of one pickup at a time. If the pickups are too close to each other, it will take the closest one.

---

### `0959` CREATE_HORSESHOE_PICKUP
Creates a collectible horseshoe at the specified coordinates

**Class:** `Pickup.CreateHorseshoe`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `handle: Pickup (variable)`

**Details:**

This command creates a horseshoe pickup. Like most pickups, it spins and can be "picked up" by walking through it. Horseshoes are recorded in stat 241. The total amount of horseshoes depends on the amount of pickups you have placed. Picking up a horseshoe gives you $100. Picking up all the horseshoes will give you $10,000. The pickup uses the model `cj_horse_shoe.dff` to create the pickup so the model has to be at least defined somewhere in an IDE file for the command to work.

---

### `095A` CREATE_OYSTER_PICKUP
Creates a collectible oyster at the specified coordinates

**Class:** `Pickup.CreateOyster`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `handle: Pickup (variable)`

---

### `09D1` DOES_PICKUP_EXIST
Returns true if the handle is a valid pickup handle

**Class:** `Pickup.DoesExist`
**Flags:** condition, static

**Input:**
- `handle: any`

---
