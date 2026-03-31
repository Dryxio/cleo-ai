# ini Extension Opcodes

> 8 opcodes

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0AF0` | READ_INT_FROM_INI_FILE | Reads an integer value from the ini file |
| `0AF1` | WRITE_INT_TO_INI_FILE | Writes the integer value to the ini file |
| `0AF2` | READ_FLOAT_FROM_INI_FILE | Reads a floating-point value from the ini file |
| `0AF3` | WRITE_FLOAT_TO_INI_FILE | Writes the floating-point value to the ini file |
| `0AF4` | READ_STRING_FROM_INI_FILE | Reads a string value from the ini file |
| `0AF5` | WRITE_STRING_TO_INI_FILE | Writes the string value to the ini file |
| `2800` | DELETE_SECTION_FROM_INI_FILE | Deletes the section from the ini file |
| `2801` | DELETE_KEY_FROM_INI_FILE | Deletes the key from the ini file |

## Detailed Reference

### IniFile

### `0AF0` READ_INT_FROM_INI_FILE
Reads an integer value from the ini file

**Class:** `IniFile.ReadInt`
**Flags:** static, condition

**Input:**
- `path: string`
- `section: string`
- `key: string`

**Output:**
- `value: int (variable)`

---

### `0AF1` WRITE_INT_TO_INI_FILE
Writes the integer value to the ini file

**Class:** `IniFile.WriteInt`
**Flags:** static, condition

**Input:**
- `value: int`
- `path: string`
- `section: string`
- `key: string`

---

### `0AF2` READ_FLOAT_FROM_INI_FILE
Reads a floating-point value from the ini file

**Class:** `IniFile.ReadFloat`
**Flags:** static, condition

**Input:**
- `path: string`
- `section: string`
- `key: string`

**Output:**
- `value: float (variable)`

---

### `0AF3` WRITE_FLOAT_TO_INI_FILE
Writes the floating-point value to the ini file

**Class:** `IniFile.WriteFloat`
**Flags:** static, condition

**Input:**
- `value: float`
- `path: string`
- `section: string`
- `key: string`

---

### `0AF4` READ_STRING_FROM_INI_FILE
Reads a string value from the ini file

**Class:** `IniFile.ReadString`
**Flags:** static, condition

**Input:**
- `path: string`
- `section: string`
- `key: string`

**Output:**
- `value: string (variable)`

---

### `0AF5` WRITE_STRING_TO_INI_FILE
Writes the string value to the ini file

**Class:** `IniFile.WriteString`
**Flags:** static, condition

**Input:**
- `value: string`
- `path: string`
- `section: string`
- `key: string`

---

### `2800` DELETE_SECTION_FROM_INI_FILE
Deletes the section from the ini file

**Class:** `IniFile.DeleteSection`
**Flags:** condition, static

**Input:**
- `path: string`
- `section: string`

---

### `2801` DELETE_KEY_FROM_INI_FILE
Deletes the key from the ini file

**Class:** `IniFile.DeleteKey`
**Flags:** condition, static

**Input:**
- `path: string`
- `section: string`
- `key: string`

---
