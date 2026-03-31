# Menu Opcodes

> 13 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `08D4` | CREATE_MENU | Creates the specified panel on the screen with basic settings |
| `08D6` | SET_MENU_COLUMN_ORIENTATION |  |
| `08D7` | GET_MENU_ITEM_SELECTED | Returns the currently highlighted row in a panel |
| `08D8` | GET_MENU_ITEM_ACCEPTED | Returns the last row of a panel selected with the sprint key |
| `08D9` | ACTIVATE_MENU_ITEM |  |
| `08DA` | DELETE_MENU | Removes the specified panel from the screen |
| `08DB` | SET_MENU_COLUMN |  |
| `08EE` | SET_MENU_ITEM_WITH_NUMBER | Sets the numbered GXT of the specified panel row |
| `08EF` | SET_MENU_ITEM_WITH_2_NUMBERS |  |
| `090E` | SET_ACTIVE_MENU_ITEM |  |
| `09DB` | SET_MENU_COLUMN_WIDTH | Sets the width of the specified menu column |
| `0A22` | CHANGE_CAR_COLOUR_FROM_MENU |  |
| `0A23` | HIGHLIGHT_MENU_ITEM | Highlights the menu item - used to indicate an owned shopping item |

## Detailed Reference

### `08D4` CREATE_MENU
Creates the specified panel on the screen with basic settings

**Class:** `Menu.Create`
**Flags:** constructor

**Input:**
- `header: gxt_key`
- `topLeftX: float`
- `topLeftY: float`
- `width: float`
- `numColumns: int`
- `interactive: bool`
- `background: bool`
- `alignment: Align`

**Output:**
- `handle: Menu (variable)`

---

### `08D6` SET_MENU_COLUMN_ORIENTATION

**Class:** `Menu.SetColumnOrientation`

**Input:**
- `self: Menu`
- `column: int`
- `alignment: Align`

---

### `08D7` GET_MENU_ITEM_SELECTED
Returns the currently highlighted row in a panel

**Class:** `Menu.GetItemSelected`

**Input:**
- `self: Menu`

**Output:**
- `row: int (variable)`

---

### `08D8` GET_MENU_ITEM_ACCEPTED
Returns the last row of a panel selected with the sprint key

**Class:** `Menu.GetItemAccepted`

**Input:**
- `self: Menu`

**Output:**
- `row: int (variable)`

---

### `08D9` ACTIVATE_MENU_ITEM

**Class:** `Menu.ActivateItem`

**Input:**
- `self: Menu`
- `row: int`
- `state: bool`

---

### `08DA` DELETE_MENU
Removes the specified panel from the screen

**Class:** `Menu.Delete`
**Flags:** destructor

**Input:**
- `self: Menu`

---

### `08DB` SET_MENU_COLUMN

**Class:** `Menu.SetColumn`

**Input:**
- `self: Menu`
- `column: int`
- `title: gxt_key`
- `row0: gxt_key`
- `row1: gxt_key`
- `row2: gxt_key`
- `row3: gxt_key`
- `row4: gxt_key`
- `row5: gxt_key`
- `row6: gxt_key`
- `row7: gxt_key`
- `row8: gxt_key`
- `row9: gxt_key`
- `row10: gxt_key`
- `row11: gxt_key`

---

### `08EE` SET_MENU_ITEM_WITH_NUMBER
Sets the numbered GXT of the specified panel row

**Class:** `Menu.SetItemWithNumber`

**Input:**
- `self: Menu`
- `column: int`
- `row: int`
- `gxt: gxt_key`
- `number: int`

---

### `08EF` SET_MENU_ITEM_WITH_2_NUMBERS

**Class:** `Menu.SetItemWith2Numbers`

**Input:**
- `self: Menu`
- `column: int`
- `row: int`
- `gxt: gxt_key`
- `number1: int`
- `number2: int`

---

### `090E` SET_ACTIVE_MENU_ITEM

**Class:** `Menu.SetActiveItem`

**Input:**
- `self: Menu`
- `row: int`

---

### `09DB` SET_MENU_COLUMN_WIDTH
Sets the width of the specified menu column

**Class:** `Menu.SetColumnWidth`

**Input:**
- `self: Menu`
- `column: int`
- `width: int`

---

### `0A22` CHANGE_CAR_COLOUR_FROM_MENU

**Class:** `Menu.ChangeCarColor`

**Input:**
- `self: Menu`
- `vehicle: Car`
- `colorSlot: int`
- `row: int`

---

### `0A23` HIGHLIGHT_MENU_ITEM
Highlights the menu item - used to indicate an owned shopping item

**Class:** `Menu.HighlightItem`

**Input:**
- `self: Menu`
- `row: int`
- `state: bool`

---
