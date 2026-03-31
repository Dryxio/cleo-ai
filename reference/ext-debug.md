# debug Extension Opcodes

> 6 opcodes

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0662` | WRITE_DEBUG |  |
| `0663` | WRITE_DEBUG_WITH_INT |  |
| `0664` | WRITE_DEBUG_WITH_FLOAT |  |
| `2100` | BREAKPOINT | Creates a debug breakpoint in script |
| `2101` | TRACE | Prints a debug message on screen and adds it to .cleo.log |
| `2102` | LOG_TO_FILE | Appends new line to file. Timestamp parameter decides if datetime prefix in form |

## Detailed Reference

### Debugger

### `2100` BREAKPOINT
Creates a debug breakpoint in script

**Class:** `Debugger.Breakpoint`
**Flags:** static

**Input:**
- `blocking: bool (literal)`
- `text: string`
- `args: arguments`

**Details:**

This command creates a new debug breakpoint. DEBUG_ON must be used before this command for the breakpoint to be triggered.

If the first argument is not `false`, the entire game will be paused.

Extra arguments can be used to display a formatted message on screen when breakpoint is triggered. Execution can be continued by pressing the key assigned to this breakpoint (F5-F12, depending on the currently triggered breakpoint count)

---

### `2101` TRACE
Prints a debug message on screen and adds it to .cleo.log

**Class:** `Debugger.Trace`
**Flags:** static

**Input:**
- `text: string`
- `args: arguments`

**Details:**

DEBUG_ON must be used, or this command will be ignored. Printing on screen requires the `DebugUtils.ScreenLog.Level` property in `CLEO\.cleo_config.ini` to be `1` or higher.

---

### `2102` LOG_TO_FILE
Appends new line to file. Timestamp parameter decides if datetime prefix in format 'DD/MM/YYYY hh:mm:ss.fraction' will be added. Command is not affected by debug mode status

**Class:** `Debugger.LogLine`
**Flags:** static

**Input:**
- `filename: string`
- `timestamp: bool`
- `text: string`
- `args: arguments`

---

### `0662` WRITE_DEBUG


**Input:**
- `text: string`

---

### `0663` WRITE_DEBUG_WITH_INT


**Input:**
- `text: string`
- `number: int`

---

### `0664` WRITE_DEBUG_WITH_FLOAT


**Input:**
- `text: string`
- `number: float`

---
