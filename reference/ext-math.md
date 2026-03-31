# math Extension Opcodes

> 13 opcodes

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `2700` | IS_BIT_SET | Checks if n-th bit of the number is set |
| `2701` | SET_BIT | Sets n-th bit of the number |
| `2702` | CLEAR_BIT | Clears n-th bit of the number |
| `2703` | TOGGLE_BIT | Sets state of n-th bit in the number |
| `2704` | IS_TRUTHY | Checks if value contains number different than 0 or not empty string |
| `2705` | PICK_RANDOM_INT | Selects one random integer from provided values |
| `2706` | PICK_RANDOM_FLOAT | Selects one random float from provided values |
| `2707` | PICK_RANDOM_TEXT | Selects one random text from provided values |
| `2708` | RANDOM_CHANCE | Sets random condition result, with percent chance to be true |
| `2709` | FLOAT_ADD | Adds together two float values and writes the result into the variable |
| `270A` | FLOAT_SUB | Subtracts the float value from another float value and writes the result into th |
| `270B` | FLOAT_MUL | Multiplies two float values and writes the result into the variable |
| `270C` | FLOAT_DIV | Divides the float value by another float value and writes the result into the va |

## Detailed Reference

### Math

### `2700` IS_BIT_SET
Checks if n-th bit of the number is set

**Class:** `Math.IsBitSet`
**Flags:** static, condition

**Input:**
- `number: int`
- `bitIndex: int`

---

### `2701` SET_BIT
Sets n-th bit of the number

**Class:** `Math.SetBit`
**Flags:** static

**Input:**
- `number: int (variable)`
- `bitIndex: int`

---

### `2702` CLEAR_BIT
Clears n-th bit of the number

**Class:** `Math.ClearBit`
**Flags:** static

**Input:**
- `number: int (variable)`
- `bitIndex: int`

---

### `2703` TOGGLE_BIT
Sets state of n-th bit in the number

**Class:** `Math.ToggleBit`
**Flags:** static

**Input:**
- `number: int (variable)`
- `bitIndex: int`
- `state: bool`

---

### `2704` IS_TRUTHY
Checks if value contains number different than 0 or not empty string

**Class:** `Math.IsTruthy`
**Flags:** static, condition

**Input:**
- `value: any`

---

### `2705` PICK_RANDOM_INT
Selects one random integer from provided values

**Class:** `Math.RandomPick`
**Flags:** static

**Input:**
- `values: arguments`

**Output:**
- `result: int (variable)`

---

### `2706` PICK_RANDOM_FLOAT
Selects one random float from provided values

**Class:** `Math.RandomPick`
**Flags:** static

**Input:**
- `values: arguments`

**Output:**
- `result: float (variable)`

---

### `2707` PICK_RANDOM_TEXT
Selects one random text from provided values

**Class:** `Math.RandomPick`
**Flags:** static

**Input:**
- `values: arguments`

**Output:**
- `result: string (variable)`

---

### `2708` RANDOM_CHANCE
Sets random condition result, with percent chance to be true

**Class:** `Math.RandomChance`
**Flags:** static, condition

**Input:**
- `percent: float`

---

### `2709` FLOAT_ADD
Adds together two float values and writes the result into the variable

**Operator:** `+`

**Input:**
- `float`
- `float`

**Output:**
- `float (variable)`

---

### `270A` FLOAT_SUB
Subtracts the float value from another float value and writes the result into the variable

**Operator:** `-`

**Input:**
- `float`
- `float`

**Output:**
- `float (variable)`

---

### `270B` FLOAT_MUL
Multiplies two float values and writes the result into the variable

**Operator:** `*`

**Input:**
- `float`
- `float`

**Output:**
- `float (variable)`

---

### `270C` FLOAT_DIV
Divides the float value by another float value and writes the result into the variable

**Operator:** `/`

**Input:**
- `float`
- `float`

**Output:**
- `float (variable)`

---
