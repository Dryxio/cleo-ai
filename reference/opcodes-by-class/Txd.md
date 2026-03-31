# Txd Opcodes

> 3 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `038F` | LOAD_SPRITE | Loads a sprite from the most recently loaded texture dictionary (0390) |
| `0390` | LOAD_TEXTURE_DICTIONARY | Loads the texture dictionary for use in drawing sprites (038D) on the screen |
| `0391` | REMOVE_TEXTURE_DICTIONARY | Unloads all currently loaded textures (038F), as well as texture dictionaries (0 |

## Detailed Reference

### `038F` LOAD_SPRITE
Loads a sprite from the most recently loaded texture dictionary (0390)

**Class:** `Txd.LoadSprite`
**Flags:** static

**Input:**
- `spriteSlot: int`
- `textureName: string`

---

### `0390` LOAD_TEXTURE_DICTIONARY
Loads the texture dictionary for use in drawing sprites (038D) on the screen

**Class:** `Txd.LoadDictionary`
**Flags:** static

**Input:**
- `name: string`

---

### `0391` REMOVE_TEXTURE_DICTIONARY
Unloads all currently loaded textures (038F), as well as texture dictionaries (0390), freeing game memory

**Class:** `Txd.Remove`
**Flags:** static

---
