# Trailer Opcodes

> 3 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `07AB` | IS_TRAILER_ATTACHED_TO_CAB | Returns true if CAR A has CAR B attached to it like a trailer |
| `07AC` | DETACH_TRAILER_FROM_CAB | Detaches the trailer from the car which it is attached to |
| `0893` | ATTACH_TRAILER_TO_CAB |  |

## Detailed Reference

### `07AB` IS_TRAILER_ATTACHED_TO_CAB
Returns true if CAR A has CAR B attached to it like a trailer

**Class:** `Trailer.IsAttachedToCab`
**Flags:** condition

**Input:**
- `self: Trailer`
- `cab: Car`

---

### `07AC` DETACH_TRAILER_FROM_CAB
Detaches the trailer from the car which it is attached to

**Class:** `Trailer.DetachFromCab`

**Input:**
- `self: Trailer`
- `cab: Car`

---

### `0893` ATTACH_TRAILER_TO_CAB

**Class:** `Trailer.AttachToCab`

**Input:**
- `self: Trailer`
- `cab: Car`

---
