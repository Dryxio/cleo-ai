# memory Extension Opcodes

> 8 opcodes

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `2400` | COPY_MEMORY | Copies a block of memory from src address to dest address. src and dest regions  |
| `2401` | READ_MEMORY_WITH_OFFSET | Reads a value from the given offset from the memory address (see: 2402) |
| `2402` | WRITE_MEMORY_WITH_OFFSET | Writes the value at the given offset from the memory address (see: 2401) |
| `2403` | FORGET_MEMORY | Makes the memory chunk allocated with 0AC8 persistent across load/start new game |
| `2404` | GET_SCRIPT_STRUCT_JUST_CREATED | Returns the address of a most recently (globally) created script (004F, 00D7, 0A |
| `2405` | IS_SCRIPT_RUNNING | Checks if address points at valid and running script |
| `2407` | IS_MEMORY_EQUAL | Compares two memory blocks |
| `2408` | TERMINATE_SCRIPT | Terminates script pointed by the address |

## Detailed Reference

### Memory

### `2400` COPY_MEMORY
Copies a block of memory from src address to dest address. src and dest regions may overlap (memmove behavior)

**Class:** `Memory.Copy`
**Flags:** static

**Input:**
- `src: int`
- `dest: int`
- `size: int`

---

### `2401` READ_MEMORY_WITH_OFFSET
Reads a value from the given offset from the memory address (see: 2402)

**Class:** `Memory.ReadWithOffset`
**Flags:** static

**Input:**
- `address: int`
- `offset: int`
- `size: int`

**Output:**
- `result: int (variable)`

---

### `2402` WRITE_MEMORY_WITH_OFFSET
Writes the value at the given offset from the memory address (see: 2401)

**Class:** `Memory.WriteWithOffset`
**Flags:** static

**Input:**
- `address: int`
- `offset: int`
- `size: int`
- `value: any`

---

### `2403` FORGET_MEMORY
Makes the memory chunk allocated with 0AC8 persistent across load/start new game events. The memory is still released when game closes causing no leaks

**Class:** `Memory.Forget`
**Flags:** static

**Input:**
- `address: int`

---

### `2404` GET_SCRIPT_STRUCT_JUST_CREATED
Returns the address of a most recently (globally) created script (004F, 00D7, 0A92, 0A94)

**Class:** `Memory.GetScriptStructJustCreated`
**Flags:** static

**Output:**
- `address: int (variable)`

---

### `2405` IS_SCRIPT_RUNNING
Checks if address points at valid and running script

**Class:** `Memory.IsScriptRunning`
**Flags:** static, condition

**Input:**
- `address: int`

---

### `2407` IS_MEMORY_EQUAL
Compares two memory blocks

**Class:** `Memory.IsEqual`
**Flags:** static, condition

**Input:**
- `addressA: int`
- `addressB: int`
- `size: int`

---

### `2408` TERMINATE_SCRIPT
Terminates script pointed by the address


**Input:**
- `address: int`

---
