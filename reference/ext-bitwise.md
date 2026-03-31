# bitwise Extension Opcodes

> 15 opcodes

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0B10` | BIT_AND | Returns a result of the bitwise AND operation on the corresponding bits of the f |
| `0B11` | BIT_OR | Returns a result of the bitwise OR operation on the corresponding bits of the fi |
| `0B12` | BIT_XOR | Returns a result of the bitwise XOR operation on the corresponding bits of the f |
| `0B13` | BIT_NOT | Returns a signed number calculated by logical negation of each bit of the input  |
| `0B14` | MOD | Returns the modulo; remainder of a division, after the first number is divided b |
| `0B15` | BIT_SHR | Returns a number calculated by shifting right all the bits of the value by n bit |
| `0B16` | BIT_SHL | Returns a number calculated by shifting left all the bits of the value by n bits |
| `0B17` | BIT_AND_COMPOUND | Reads a value from the variable, performs bitwise AND operation on it and the op |
| `0B18` | BIT_OR_COMPOUND | Reads a value from the variable, performs bitwise OR operation on it and the ope |
| `0B19` | BIT_XOR_COMPOUND | Reads a value from the variable, performs bitwise XOR operation on it and the op |
| `0B1A` | BIT_NOT_COMPOUND | Reads a value from the variable, performs bitwise NOT operation on it (BIT_NOT)  |
| `0B1B` | MOD_COMPOUND | Reads a value from the variable, divides it by the number and stores the remaind |
| `0B1C` | BIT_SHR_COMPOUND | Reads a value from the variable, shifts right by n bits (BIT_SHR) and stores the |
| `0B1D` | BIT_SHL_COMPOUND | Reads a value from the variable, shifts left by n bits (BIT_SHL) and stores the  |
| `0B1E` | SIGN_EXTEND | Extends a 1-, 2- or 3-byte long integer value to a 4-byte (32-bit), while preser |

## Detailed Reference

### Math

### `0B1E` SIGN_EXTEND
Extends a 1-, 2- or 3-byte long integer value to a 4-byte (32-bit), while preserving the sign (+/-)

**Class:** `Math.SignExtend`
**Flags:** static

**Input:**
- `value: int (variable)`
- `fromSize: int`

---

### `0B10` BIT_AND
Returns a result of the bitwise AND operation on the corresponding bits of the first and second operands

**Operator:** `&`

**Input:**
- `int`
- `int`

**Output:**
- `int (variable)`

---

### `0B11` BIT_OR
Returns a result of the bitwise OR operation on the corresponding bits of the first and second operands

**Operator:** `|`

**Input:**
- `int`
- `int`

**Output:**
- `int (variable)`

---

### `0B12` BIT_XOR
Returns a result of the bitwise XOR operation on the corresponding bits of the first and second operands

**Operator:** `^`

**Input:**
- `int`
- `int`

**Output:**
- `int (variable)`

---

### `0B13` BIT_NOT
Returns a signed number calculated by logical negation of each bit of the input value

**Operator:** `~`

**Input:**
- `int`

**Output:**
- `int (variable)`

---

### `0B14` MOD
Returns the modulo; remainder of a division, after the first number is divided by the second number

**Operator:** `%`

**Input:**
- `int`
- `int`

**Output:**
- `int (variable)`

---

### `0B15` BIT_SHR
Returns a number calculated by shifting right all the bits of the value by n bits

**Operator:** `>>`

**Input:**
- `value: int`
- `n: int`

**Output:**
- `int (variable)`

---

### `0B16` BIT_SHL
Returns a number calculated by shifting left all the bits of the value by n bits

**Operator:** `<<`

**Input:**
- `value: int`
- `n: int`

**Output:**
- `int (variable)`

---

### `0B17` BIT_AND_COMPOUND
Reads a value from the variable, performs bitwise AND operation on it and the operand (BIT_AND) and stores the result back to the variable

**Operator:** `&`

**Input:**
- `int (variable)`
- `int`

---

### `0B18` BIT_OR_COMPOUND
Reads a value from the variable, performs bitwise OR operation on it and the operand (BIT_OR) and stores the result back to the variable

**Operator:** `|`

**Input:**
- `int (variable)`
- `int`

---

### `0B19` BIT_XOR_COMPOUND
Reads a value from the variable, performs bitwise XOR operation on it and the operand (BIT_XOR) and stores the result back to the variable

**Operator:** `^`

**Input:**
- `int (variable)`
- `int`

---

### `0B1A` BIT_NOT_COMPOUND
Reads a value from the variable, performs bitwise NOT operation on it (BIT_NOT) and stores the result back to the variable

**Operator:** `~`

**Input:**
- `int (variable)`

---

### `0B1B` MOD_COMPOUND
Reads a value from the variable, divides it by the number and stores the remainder (MOD) back to the variable

**Operator:** `%`

**Input:**
- `int (variable)`
- `number: int`

---

### `0B1C` BIT_SHR_COMPOUND
Reads a value from the variable, shifts right by n bits (BIT_SHR) and stores the result back to the variable

**Operator:** `>>`

**Input:**
- `int (variable)`
- `n: int`

---

### `0B1D` BIT_SHL_COMPOUND
Reads a value from the variable, shifts left by n bits (BIT_SHL) and stores the result back to the variable

**Operator:** `<<`

**Input:**
- `int (variable)`
- `n: int`

---
