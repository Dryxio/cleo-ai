# clipboard Extension Opcodes

> 2 opcodes

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0B20` | READ_CLIPBOARD_DATA | Copies the specified number of bytes of text from the clipboard to the address |
| `0B21` | WRITE_CLIPBOARD_DATA | Copies  the specified number of bytes of text from the address to the clipboard |

## Detailed Reference

### Clipboard

### `0B20` READ_CLIPBOARD_DATA
Copies the specified number of bytes of text from the clipboard to the address

**Class:** `Clipboard.ReadData`
**Flags:** static

**Input:**
- `address: int`
- `number: int`

---

### `0B21` WRITE_CLIPBOARD_DATA
Copies  the specified number of bytes of text from the address to the clipboard

**Class:** `Clipboard.WriteData`
**Flags:** static

**Input:**
- `address: int`
- `number: int`

---
