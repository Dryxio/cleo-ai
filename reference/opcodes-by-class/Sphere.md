# Sphere Opcodes

> 3 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `03A1` | DRAW_SPHERE | Displays a red cylinder sphere |
| `03BC` | ADD_SPHERE | Creates a static sphere at the location, with the specified radius |
| `03BD` | REMOVE_SPHERE | Destroys a static sphere |

## Detailed Reference

### `03A1` DRAW_SPHERE
Displays a red cylinder sphere

**Class:** `Sphere.Draw`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `diameter: float`

---

### `03BC` ADD_SPHERE
Creates a static sphere at the location, with the specified radius

**Class:** `Sphere.Create`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`

**Output:**
- `handle: Sphere (variable)`

---

### `03BD` REMOVE_SPHERE
Destroys a static sphere

**Class:** `Sphere.Remove`
**Flags:** destructor

**Input:**
- `self: Sphere`

---
