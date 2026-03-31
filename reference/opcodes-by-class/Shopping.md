# Shopping Opcodes

> 13 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `075D` | LOAD_PRICES |  |
| `075E` | LOAD_SHOP |  |
| `075F` | GET_NUMBER_OF_ITEMS_IN_SHOP |  |
| `0760` | GET_ITEM_IN_SHOP | Returns an identifier for an item associated with the shopping data entry |
| `0761` | GET_PRICE_OF_ITEM |  |
| `0783` | GET_SHOPPING_EXTRA_INFO |  |
| `078C` | GET_NAME_OF_ITEM |  |
| `0790` | BUY_ITEM | Charges the player for the purchase of the item and in many cases, automatically |
| `07B0` | GET_LOADED_SHOP | Returns the name of currently loaded subsection in shopping |
| `087C` | CLEAR_LOADED_SHOP | Releases the loaded shopping data |
| `08C8` | ADD_PRICE_MODIFIER | Sets a new base price for the shopping.dat item |
| `08C9` | REMOVE_PRICE_MODIFIER | Restores the base price for a shopping.dat item altered by ADD_PRICE_MODIFIER |
| `0942` | HAS_PLAYER_BOUGHT_ITEM | Returns true if the shopping item has been bought |

## Detailed Reference

### `075D` LOAD_PRICES

**Class:** `Shopping.LoadPrices`
**Flags:** static

**Input:**
- `sectionName: string`

---

### `075E` LOAD_SHOP

**Class:** `Shopping.Load`
**Flags:** static

**Input:**
- `name: string`

---

### `075F` GET_NUMBER_OF_ITEMS_IN_SHOP

**Class:** `Shopping.GetNumberOfItems`
**Flags:** static

**Output:**
- `numItems: int (variable)`

---

### `0760` GET_ITEM_IN_SHOP
Returns an identifier for an item associated with the shopping data entry

**Class:** `Shopping.GetItem`
**Flags:** static

**Input:**
- `nth: int`

**Output:**
- `id: int (variable)`

---

### `0761` GET_PRICE_OF_ITEM

**Class:** `Shopping.GetPriceOfItem`
**Flags:** static

**Input:**
- `itemId: int`

**Output:**
- `price: int (variable)`

---

### `0783` GET_SHOPPING_EXTRA_INFO

**Class:** `Shopping.GetExtraInfo`
**Flags:** static

**Input:**
- `itemId: int`
- `flag: int`

**Output:**
- `value: int (variable)`

---

### `078C` GET_NAME_OF_ITEM

**Class:** `Shopping.GetNameOfItem`
**Flags:** static

**Input:**
- `itemId: int`

**Output:**
- `name: string (variable)`

---

### `0790` BUY_ITEM
Charges the player for the purchase of the item and in many cases, automatically gives the item to the player

**Class:** `Shopping.BuyItem`
**Flags:** static

**Input:**
- `itemId: int`

---

### `07B0` GET_LOADED_SHOP
Returns the name of currently loaded subsection in shopping

**Class:** `Shopping.GetLoaded`
**Flags:** static

**Output:**
- `name: string (variable)`

---

### `087C` CLEAR_LOADED_SHOP
Releases the loaded shopping data

**Class:** `Shopping.ClearLoaded`
**Flags:** static

---

### `08C8` ADD_PRICE_MODIFIER
Sets a new base price for the shopping.dat item

**Class:** `Shopping.AddPriceModifier`
**Flags:** static

**Input:**
- `itemId: int`
- `price: int`

**Details:**

This command sets a new price for shop items. The price can be saved and remains active until a new price is set, or the override is removed using REMOVE_PRICE_MODIFIER. The game can save only up to 20 custom prices in total.

---

### `08C9` REMOVE_PRICE_MODIFIER
Restores the base price for a shopping.dat item altered by ADD_PRICE_MODIFIER

**Class:** `Shopping.RemovePriceModifier`
**Flags:** static

**Input:**
- `itemId: int`

---

### `0942` HAS_PLAYER_BOUGHT_ITEM
Returns true if the shopping item has been bought

**Class:** `Shopping.HasPlayerBoughtItem`
**Flags:** condition, static

**Input:**
- `itemId: int`

---
