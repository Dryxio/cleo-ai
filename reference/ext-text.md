# text Extension Opcodes

> 10 opcodes

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `2600` | IS_TEXT_EMPTY | Checks if string length is equal to zero |
| `2601` | IS_TEXT_EQUAL | Compares two texts |
| `2602` | IS_TEXT_IN_TEXT | Checks if text contains specified text |
| `2603` | IS_TEXT_PREFIX | Checks if text starts with specified prefix text |
| `2604` | IS_TEXT_SUFFIX | Checks if text ends with specified suffix text |
| `2605` | DISPLAY_TEXT_FORMATTED | Formats args according to the format string then draws text at the specified on- |
| `2606` | LOAD_FXT | Loads GXT texts from selected FXT dictionary file |
| `2607` | UNLOAD_FXT | Unloads GXT labels defined in selected Fxt file |
| `2608` | GET_TEXT_LENGTH | Returns count of characters in the text |
| `2609` | ADD_TEXT_LABEL_FORMATTED | Adds or updates the text associated with the dynamic GXT key. It does nothing if |

## Detailed Reference

### Text

### `2600` IS_TEXT_EMPTY
Checks if string length is equal to zero

**Class:** `Text.IsEmpty`
**Flags:** condition, static

**Input:**
- `string: string`

---

### `2601` IS_TEXT_EQUAL
Compares two texts

**Class:** `Text.IsEqual`
**Flags:** static, condition

**Input:**
- `text: string`
- `another: string`
- `ignoreCase: bool`

---

### `2602` IS_TEXT_IN_TEXT
Checks if text contains specified text

**Class:** `Text.Contains`
**Flags:** static, condition

**Input:**
- `text: string`
- `subText: string`
- `ignoreCase: bool`

---

### `2603` IS_TEXT_PREFIX
Checks if text starts with specified prefix text

**Class:** `Text.StartsWith`
**Flags:** static, condition

**Input:**
- `text: string`
- `prefix: string`
- `ignoreCase: bool`

---

### `2604` IS_TEXT_SUFFIX
Checks if text ends with specified suffix text

**Class:** `Text.EndsWith`
**Flags:** condition, static

**Input:**
- `text: string`
- `suffix: string`
- `ignoreCase: bool`

---

### `2605` DISPLAY_TEXT_FORMATTED
Formats args according to the format string then draws text at the specified on-screen position. See 033E

**Class:** `Text.DisplayFormatted`
**Flags:** static

**Input:**
- `offsetLeft: float`
- `offsetTop: float`
- `format: string`
- `args: arguments`

**Details:**

The message is constructed out of the given string and any extra arguments.  

Common [C++ format specifiers](https://cplusplus.com/reference/cstdio/printf/) starting from `%` are used to define argument type, e.g.:  
* `%d` integer number in decimal form
* `%x` integer number in hex form (lower case letters)
* `%X` integer number in hex form (upper case letters)
* `%f` floating-point number
* `%s` string
* `%p` 8-digit hex number
* `%%` single `%` character
* `%c` single ASCII character specified by number
* `%4d` at least 4 digits wide integer number (padded with spaces)
* `%04d` at least 4 digits wide integer number (padded with zeros)
* `%.2f` floating-point number rounded to 2 digits after decimal point

The format string may contain zero or more specifiers and their count must match the number of arguments.

---

### `2606` LOAD_FXT
Loads GXT texts from selected FXT dictionary file

**Class:** `Text.LoadFxt`
**Flags:** static, condition

**Input:**
- `filepath: string`

---

### `2607` UNLOAD_FXT
Unloads GXT labels defined in selected Fxt file

**Class:** `Text.UnloadFxt`
**Flags:** static, condition

**Input:**
- `filepath: string`

---

### `2608` GET_TEXT_LENGTH
Returns count of characters in the text

**Class:** `Text.GetLength`
**Flags:** static

**Input:**
- `text: string`

**Output:**
- `length: int (variable)`

---

### `2609` ADD_TEXT_LABEL_FORMATTED
Adds or updates the text associated with the dynamic GXT key. It does nothing if the same key is defined in a FXT file

**Class:** `Text.AddLabelFormatted`
**Flags:** static

**Input:**
- `dynamicKey: string`
- `format: string`
- `args: arguments`

**Details:**

The message is constructed out of the given string and any extra arguments.  

Common [C++ format specifiers](https://cplusplus.com/reference/cstdio/printf/) starting from `%` are used to define argument type, e.g.:  
* `%d` integer number in decimal form
* `%x` integer number in hex form (lower case letters)
* `%X` integer number in hex form (upper case letters)
* `%f` floating-point number
* `%s` string
* `%p` 8-digit hex number
* `%%` single `%` character
* `%c` single ASCII character specified by number
* `%4d` at least 4 digits wide integer number (padded with spaces)
* `%04d` at least 4 digits wide integer number (padded with zeros)
* `%.2f` floating-point number rounded to 2 digits after decimal point

The format string may contain zero or more specifiers and their count must match the number of arguments.

---
