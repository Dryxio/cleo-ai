# General Opcodes (No Class)

> 1173 opcodes — flow control, variables, comparisons, etc.

## Comparisons

### `0018` IS_INT_VAR_GREATER_THAN_NUMBER
Returns true if the int VAR value is greater than the value

**Operator:** `>`
**Flags:** condition

**Input:**
- `int (global var)`
- `int (literal)`

---

### `0019` IS_INT_LVAR_GREATER_THAN_NUMBER
Returns true if the int LVAR value is greater than the value

**Operator:** `>`
**Flags:** condition

**Input:**
- `int (local var)`
- `int (literal)`

---

### `001A` IS_NUMBER_GREATER_THAN_INT_VAR
Returns true if the value is greater than the int VAR value

**Operator:** `>`
**Flags:** condition

**Input:**
- `int (literal)`
- `int (global var)`

---

### `001B` IS_NUMBER_GREATER_THAN_INT_LVAR
Returns true if the value is greater than the int LVAR value

**Operator:** `>`
**Flags:** condition

**Input:**
- `int (literal)`
- `int (local var)`

---

### `001C` IS_INT_VAR_GREATER_THAN_INT_VAR
Returns true if the int VAR value is greater than the other int VAR value

**Operator:** `>`
**Flags:** condition

**Input:**
- `int (global var)`
- `int (global var)`

---

### `001D` IS_INT_LVAR_GREATER_THAN_INT_LVAR
Returns true if the int LVAR value is greater than the other int LVAR value

**Operator:** `>`
**Flags:** condition

**Input:**
- `int (local var)`
- `int (local var)`

---

### `001E` IS_INT_VAR_GREATER_THAN_INT_LVAR
Returns true if the int VAR value is greater than the int LVAR value

**Operator:** `>`
**Flags:** condition

**Input:**
- `int (global var)`
- `int (local var)`

---

### `001F` IS_INT_LVAR_GREATER_THAN_INT_VAR
Returns true if the int LVAR value is greater than the int VAR value

**Operator:** `>`
**Flags:** condition

**Input:**
- `int (local var)`
- `int (global var)`

---

### `0020` IS_FLOAT_VAR_GREATER_THAN_NUMBER
Returns true if the float VAR value is greater than the float value

**Operator:** `>`
**Flags:** condition

**Input:**
- `float (global var)`
- `float (literal)`

---

### `0021` IS_FLOAT_LVAR_GREATER_THAN_NUMBER
Returns true if the float LVAR value is greater than the float value

**Operator:** `>`
**Flags:** condition

**Input:**
- `float (local var)`
- `float (literal)`

---

### `0022` IS_NUMBER_GREATER_THAN_FLOAT_VAR
Returns true if the float value is greater than the float VAR value

**Operator:** `>`
**Flags:** condition

**Input:**
- `float (literal)`
- `float (global var)`

---

### `0023` IS_NUMBER_GREATER_THAN_FLOAT_LVAR
Returns true if the float value is greater than the float LVAR value

**Operator:** `>`
**Flags:** condition

**Input:**
- `float (literal)`
- `float (local var)`

---

### `0024` IS_FLOAT_VAR_GREATER_THAN_FLOAT_VAR
Returns true if the float VAR value is greater than the other float VAR value

**Operator:** `>`
**Flags:** condition

**Input:**
- `float (global var)`
- `float (global var)`

---

### `0025` IS_FLOAT_LVAR_GREATER_THAN_FLOAT_LVAR
Returns true if the float LVAR value is greater than the other float LVAR value

**Operator:** `>`
**Flags:** condition

**Input:**
- `float (local var)`
- `float (local var)`

---

### `0026` IS_FLOAT_VAR_GREATER_THAN_FLOAT_LVAR
Returns true if the float VAR value is greater than the float LVAR value

**Operator:** `>`
**Flags:** condition

**Input:**
- `float (global var)`
- `float (local var)`

---

### `0027` IS_FLOAT_LVAR_GREATER_THAN_FLOAT_VAR
Returns true if the float LVAR value is greater than the float VAR value

**Operator:** `>`
**Flags:** condition

**Input:**
- `float (local var)`
- `float (global var)`

---

### `0028` IS_INT_VAR_GREATER_OR_EQUAL_TO_NUMBER
Returns true if the int VAR value is greater or equal to the value

**Operator:** `>=`
**Flags:** condition

**Input:**
- `int (global var)`
- `int (literal)`

---

### `0029` IS_INT_LVAR_GREATER_OR_EQUAL_TO_NUMBER
Returns true if the int LVAR value is greater or equal to the value

**Operator:** `>=`
**Flags:** condition

**Input:**
- `int (local var)`
- `int (literal)`

---

### `002A` IS_NUMBER_GREATER_OR_EQUAL_TO_INT_VAR
Returns true if the value is greater or equal to the int VAR value

**Operator:** `>=`
**Flags:** condition

**Input:**
- `int (literal)`
- `int (global var)`

---

### `002B` IS_NUMBER_GREATER_OR_EQUAL_TO_INT_LVAR
Returns true if the value is greater or equal to the int LVAR value

**Operator:** `>=`
**Flags:** condition

**Input:**
- `int (literal)`
- `int (local var)`

---

### `002C` IS_INT_VAR_GREATER_OR_EQUAL_TO_INT_VAR
Returns true if the int VAR value is greater or equal to the other int VAR value

**Operator:** `>=`
**Flags:** condition

**Input:**
- `int (global var)`
- `int (global var)`

---

### `002D` IS_INT_LVAR_GREATER_OR_EQUAL_TO_INT_LVAR
Returns true if the int LVAR value is greater or equal to the other int LVAR value

**Operator:** `>=`
**Flags:** condition

**Input:**
- `int (local var)`
- `int (local var)`

---

### `002E` IS_INT_VAR_GREATER_OR_EQUAL_TO_INT_LVAR
Returns true if the int VAR value is greater or equal to the int LVAR value

**Operator:** `>=`
**Flags:** condition

**Input:**
- `int (global var)`
- `int (local var)`

---

### `002F` IS_INT_LVAR_GREATER_OR_EQUAL_TO_INT_VAR
Returns true if the int LVAR value is greater or equal to the int VAR value

**Operator:** `>=`
**Flags:** condition

**Input:**
- `int (local var)`
- `int (global var)`

---

### `0030` IS_FLOAT_VAR_GREATER_OR_EQUAL_TO_NUMBER
Returns true if the float VAR value is greater or equal to the value

**Operator:** `>=`
**Flags:** condition

**Input:**
- `float (global var)`
- `float (literal)`

---

### `0031` IS_FLOAT_LVAR_GREATER_OR_EQUAL_TO_NUMBER
Returns true if the float LVAR value is greater or equal to the value

**Operator:** `>=`
**Flags:** condition

**Input:**
- `float (local var)`
- `float (literal)`

---

### `0032` IS_NUMBER_GREATER_OR_EQUAL_TO_FLOAT_VAR
Returns true if the value is greater or equal to the float VAR value

**Operator:** `>=`
**Flags:** condition

**Input:**
- `float (literal)`
- `float (global var)`

---

### `0033` IS_NUMBER_GREATER_OR_EQUAL_TO_FLOAT_LVAR
Returns true if the value is greater or equal to the float LVAR value

**Operator:** `>=`
**Flags:** condition

**Input:**
- `float (literal)`
- `float (local var)`

---

### `0034` IS_FLOAT_VAR_GREATER_OR_EQUAL_TO_FLOAT_VAR
Returns true if the float VAR value is greater or equal to the other float VAR value

**Operator:** `>=`
**Flags:** condition

**Input:**
- `float (global var)`
- `float (global var)`

---

### `0035` IS_FLOAT_LVAR_GREATER_OR_EQUAL_TO_FLOAT_LVAR
Returns true if the float LVAR value is greater or equal to the other float LVAR value

**Operator:** `>=`
**Flags:** condition

**Input:**
- `float (local var)`
- `float (local var)`

---

### `0036` IS_FLOAT_VAR_GREATER_OR_EQUAL_TO_FLOAT_LVAR
Returns true if the float VAR value is greater or equal to the LVAR value

**Operator:** `>=`
**Flags:** condition

**Input:**
- `float (global var)`
- `float (local var)`

---

### `0037` IS_FLOAT_LVAR_GREATER_OR_EQUAL_TO_FLOAT_VAR
Returns true if the float LVAR value is greater or equal to the float VAR value

**Operator:** `>=`
**Flags:** condition

**Input:**
- `float (local var)`
- `float (global var)`

---

### `0038` IS_INT_VAR_EQUAL_TO_NUMBER
Returns true if the int VAR value is equal to the value

**Operator:** `==`
**Flags:** condition

**Input:**
- `int (global var)`
- `int (literal)`

---

### `0039` IS_INT_LVAR_EQUAL_TO_NUMBER
Returns true if the int LVAR value is equal to the value

**Operator:** `==`
**Flags:** condition

**Input:**
- `int (local var)`
- `int (literal)`

---

### `003A` IS_INT_VAR_EQUAL_TO_INT_VAR
Returns true if the int VAR value is equal to the other int VAR value

**Operator:** `==`
**Flags:** condition

**Input:**
- `int (global var)`
- `int (global var)`

---

### `003B` IS_INT_LVAR_EQUAL_TO_INT_LVAR
Returns true if the int LVAR value is equal to the other int LVAR value

**Operator:** `==`
**Flags:** condition

**Input:**
- `int (local var)`
- `int (local var)`

---

### `003C` IS_INT_VAR_EQUAL_TO_INT_LVAR
Returns true if the int VAR value is equal to the int LVAR value

**Operator:** `==`
**Flags:** condition

**Input:**
- `int (global var)`
- `int (local var)`

---

### `003D` IS_INT_VAR_NOT_EQUAL_TO_NUMBER

**Flags:** unsupported

---

### `003E` IS_INT_LVAR_NOT_EQUAL_TO_NUMBER

**Flags:** unsupported

---

### `003F` IS_INT_VAR_NOT_EQUAL_TO_INT_VAR

**Flags:** unsupported

---

### `0040` IS_INT_LVAR_NOT_EQUAL_TO_INT_LVAR

**Flags:** unsupported

---

### `0041` IS_INT_VAR_NOT_EQUAL_TO_INT_LVAR

**Flags:** unsupported

---

### `0042` IS_FLOAT_VAR_EQUAL_TO_NUMBER
Returns true if the float VAR value is equal to the value

**Operator:** `==`
**Flags:** condition

**Input:**
- `float (global var)`
- `float (literal)`

---

### `0043` IS_FLOAT_LVAR_EQUAL_TO_NUMBER
Returns true if the float LVAR value is equal to the value

**Operator:** `==`
**Flags:** condition

**Input:**
- `float (local var)`
- `float (literal)`

---

### `0044` IS_FLOAT_VAR_EQUAL_TO_FLOAT_VAR
Returns true if the float VAR value is equal to the other float VAR value

**Operator:** `==`
**Flags:** condition

**Input:**
- `float (global var)`
- `float (global var)`

---

### `0045` IS_FLOAT_LVAR_EQUAL_TO_FLOAT_LVAR
Returns true if the float LVAR value is equal to the other float LVAR value

**Operator:** `==`
**Flags:** condition

**Input:**
- `float (local var)`
- `float (local var)`

---

### `0046` IS_FLOAT_VAR_EQUAL_TO_FLOAT_LVAR
Returns true if the float VAR value is equal to the float LVAR value

**Operator:** `==`
**Flags:** condition

**Input:**
- `float (global var)`
- `float (local var)`

---

### `0047` IS_FLOAT_VAR_NOT_EQUAL_TO_NUMBER

**Flags:** unsupported

---

### `0048` IS_FLOAT_LVAR_NOT_EQUAL_TO_NUMBER

**Flags:** unsupported

---

### `0049` IS_FLOAT_VAR_NOT_EQUAL_TO_FLOAT_VAR

**Flags:** unsupported

---

### `004A` IS_FLOAT_LVAR_NOT_EQUAL_TO_FLOAT_LVAR

**Flags:** unsupported

---

### `004B` IS_FLOAT_VAR_NOT_EQUAL_TO_FLOAT_LVAR

**Flags:** unsupported

---

### `0183` IS_PLAYER_HEALTH_GREATER

**Flags:** unsupported

---

### `04A3` IS_INT_VAR_EQUAL_TO_CONSTANT
Returns true if the value of the global variable is equal to the integer constant

**Operator:** `==`
**Flags:** condition

**Input:**
- `int (global var)`
- `int (literal)`

---

### `04A4` IS_INT_LVAR_EQUAL_TO_CONSTANT
Returns true if the value of the local variable is equal to the integer constant

**Operator:** `==`
**Flags:** condition

**Input:**
- `int (local var)`
- `int (literal)`

---

### `04B0` IS_INT_VAR_GREATER_THAN_CONSTANT
Returns true if the value of the global variable is greater than the integer constant

**Operator:** `>`
**Flags:** condition

**Input:**
- `int (global var)`
- `int (literal)`

---

### `04B1` IS_INT_LVAR_GREATER_THAN_CONSTANT
Returns true if the value of the local variable is greater than the integer constant

**Operator:** `>`
**Flags:** condition

**Input:**
- `int (local var)`
- `int (literal)`

---

### `04B2` IS_CONSTANT_GREATER_THAN_INT_VAR
Returns true if the integer constant is greater than the value of the global variable

**Operator:** `>`
**Flags:** condition

**Input:**
- `int (literal)`
- `int (global var)`

---

### `04B3` IS_CONSTANT_GREATER_THAN_INT_LVAR
Returns true if the integer constant is greater than the value of the local variable

**Operator:** `>`
**Flags:** condition

**Input:**
- `int (literal)`
- `int (local var)`

---

### `04B4` IS_INT_VAR_GREATER_OR_EQUAL_TO_CONSTANT
Returns true if the value of the global variable is equal to or greater than the integer constant 

**Operator:** `>=`
**Flags:** condition

**Input:**
- `int (global var)`
- `int (literal)`

---

### `04B5` IS_INT_LVAR_GREATER_OR_EQUAL_TO_CONSTANT
Returns true if the value of the local variable is greater than or equal to the integer constant 

**Operator:** `>=`
**Flags:** condition

**Input:**
- `int (global var)`
- `int (literal)`

---

### `04B6` IS_CONSTANT_GREATER_OR_EQUAL_TO_INT_VAR
Returns true if the integer constant is equal to or greater than the value of the global variable

**Operator:** `>=`
**Flags:** condition

**Input:**
- `int (literal)`
- `int (global var)`

---

### `04B7` IS_CONSTANT_GREATER_OR_EQUAL_TO_INT_LVAR
Returns true if the integer constant is equal to or greater than the value of the local variable

**Operator:** `>=`
**Flags:** condition

**Input:**
- `int (literal)`
- `int (local var)`

---

### `05AD` IS_VAR_TEXT_LABEL_EQUAL_TO_TEXT_LABEL
Returns true if the two null-terminated strings are equivalent

**Operator:** `==`
**Flags:** condition

**Input:**
- `string (global var)`
- `string`

---

### `05AE` IS_LVAR_TEXT_LABEL_EQUAL_TO_TEXT_LABEL
Returns true if the two null-terminated strings are equivalent

**Operator:** `==`
**Flags:** condition

**Input:**
- `string (local var)`
- `string`

---

### `07D6` IS_INT_LVAR_EQUAL_TO_INT_VAR
Returns true if the integer value of the local variable is equivalent to the integer value of the global variable

**Operator:** `==`
**Flags:** condition

**Input:**
- `int (local var)`
- `int (global var)`

---

### `07D7` IS_FLOAT_LVAR_EQUAL_TO_FLOAT_VAR
Returns true if the float value of the local variable is equivalent to the float value of the global variable

**Operator:** `==`
**Flags:** condition

**Input:**
- `float (local var)`
- `float (global var)`

---

### `07D8` IS_INT_LVAR_NOT_EQUAL_TO_INT_VAR

**Flags:** unsupported

---

### `07D9` IS_FLOAT_LVAR_NOT_EQUAL_TO_FLOAT_VAR

**Flags:** unsupported

---

### `086B` CLEAR_THIS_INTEGER_WATCHPOINT
Does nothing

**Flags:** nop

**Input:**
- `_p1: any`

---

### `086C` CLEAR_THIS_FLOAT_WATCHPOINT
Does nothing

**Flags:** nop

**Input:**
- `_p1: any`

---

### `08F9` IS_VAR_TEXT_LABEL16_EQUAL_TO_TEXT_LABEL
Returns true if the two strings are equivalent

**Operator:** `==`
**Flags:** condition

**Input:**
- `string (global var)`
- `string`

---

### `08FA` IS_LVAR_TEXT_LABEL16_EQUAL_TO_TEXT_LABEL
Returns true if the two strings are equivalent

**Operator:** `==`
**Flags:** condition

**Input:**
- `string (local var)`
- `string`

---

## Flow Control

### `0002` GOTO
Transfers the script execution to the label unconditionally

**Flags:** branch, segment

**Input:**
- `label`

---

### `004C` GOTO_IF_TRUE

**Flags:** unsupported

---

### `004D` GOTO_IF_FALSE
Transfers the script execution to the label if the condition result is false

**Flags:** branch

**Input:**
- `label`

---

### `0050` GOSUB
Transfers the script execution to the label as a subroutine


**Input:**
- `label`

**Details:**

The `gosub` instruction is similar to the `goto` instruction, but it saves the current offset before the jump so that it can be returned to (with the RETURN instruction). The jumped-to offset is equivalent to the start of a subroutine. Execution of this subroutine ends when the `return` instruction is read, at which point execution continues from the instruction after the `gosub`.

Subroutines allow for procedural programming in scripts, which can reduce code repetition, increase readability and reduce size. Subroutines may be called from within other subroutines (like a Matryoshka doll), but nesting more than `8` subroutine calls will crash the game. Procedures are an important part of the structure of mission scripts.

---

### `0051` RETURN
Returns from the current subroutine (0050)


---

### `00C5` RETURN_TRUE

**Flags:** unsupported

---

### `00C6` RETURN_FALSE

**Flags:** unsupported

---

### `00CF` IF_INTERNAL

**Flags:** unsupported

---

### `00D0` IFNOT

**Flags:** unsupported

---

### `00D1` ELSE

**Flags:** unsupported

---

### `00D2` ENDIF

**Flags:** unsupported

---

### `00D6` IF
Begins a conditional statement with the specified number of conditions


**Input:**
- `int`

---

### `01D1` SET_CHAR_OBJ_GOTO_CHAR_ON_FOOT

**Flags:** unsupported

---

### `01D2` SET_CHAR_OBJ_GOTO_PLAYER_ON_FOOT

**Flags:** unsupported

---

### `01DA` SET_CHAR_OBJ_GOTO_AREA_ON_FOOT

**Flags:** unsupported

---

### `01DB` SET_CHAR_OBJ_GOTO_AREA_IN_CAR

**Flags:** unsupported

---

### `0211` SET_CHAR_OBJ_GOTO_COORD_ON_FOOT

**Flags:** unsupported

---

### `0212` SET_CHAR_OBJ_GOTO_COORD_IN_CAR

**Flags:** unsupported

---

### `0265` SET_COLL_OBJ_GOTO_CHAR_ON_FOOT

**Flags:** unsupported

---

### `0266` SET_COLL_OBJ_GOTO_PLAYER_ON_FOOT

**Flags:** unsupported

---

### `026E` SET_COLL_OBJ_GOTO_AREA_ON_FOOT

**Flags:** unsupported

---

### `026F` SET_COLL_OBJ_GOTO_AREA_IN_CAR

**Flags:** unsupported

---

### `0273` SET_COLL_OBJ_GOTO_COORD_ON_FOOT

**Flags:** unsupported

---

### `0274` SET_COLL_OBJ_GOTO_COORD_IN_CAR

**Flags:** unsupported

---

### `029D` SET_CHAR_OBJ_GOTO_AREA_ANY_MEANS

**Flags:** unsupported

---

### `029E` SET_COLL_OBJ_GOTO_AREA_ANY_MEANS

**Flags:** unsupported

---

### `02CD` GOSUB_FILE

**Flags:** unsupported

---

### `030E` REGISTER_JUMP_DISTANCE

**Flags:** unsupported

---

### `030F` REGISTER_JUMP_HEIGHT

**Flags:** unsupported

---

### `0310` REGISTER_JUMP_FLIPS

**Flags:** unsupported

---

### `0311` REGISTER_JUMP_SPINS

**Flags:** unsupported

---

### `0312` REGISTER_JUMP_STUNT

**Flags:** unsupported

---

### `0313` REGISTER_UNIQUE_JUMP_FOUND

**Flags:** unsupported

---

### `0314` SET_UNIQUE_JUMPS_TOTAL

**Flags:** unsupported

---

### `03A0` IS_CRANE_LIFTING_CAR

**Flags:** unsupported

---

### `0401` REGISTER_LIFE_SAVED

**Flags:** unsupported

---

### `0447` IS_PLAYER_LIFTING_A_PHONE

**Flags:** unsupported

---

### `0507` SWITCH_LIFT_CAMERA
Applies a camera overlay

**Flags:** nop

---

### `0558` SET_CHAR_OBJ_GOTO_CAR_ON_FOOT

**Flags:** unsupported

---

### `0577` SET_FADE_AND_JUMPCUT_AFTER_RC_EXPLOSION

**Flags:** unsupported

---

## Other

### `0000` NOP
Has no effect and is commonly used to pad CLEO scripts with extra space to avoid the jump-at-zero-offset bug


---

### `0001` WAIT
Pauses the script execution for specified amount of time in milliseconds


**Input:**
- `time: int`

---

### `0010` MULT_INT_VAR_BY_VAL
Multiplies the int VAR by the value

**Operator:** `*`

**Input:**
- `int (global var)`
- `int (literal)`

---

### `0011` MULT_FLOAT_VAR_BY_VAL
Multiplies the float VAR by the value

**Operator:** `*`

**Input:**
- `float (global var)`
- `float (literal)`

---

### `0012` MULT_INT_LVAR_BY_VAL
Multiplies the int LVAR by the value

**Operator:** `*`

**Input:**
- `int (local var)`
- `int (literal)`

---

### `0013` MULT_FLOAT_LVAR_BY_VAL
Multiplies the float LVAR by the value

**Operator:** `*`

**Input:**
- `float (local var)`
- `float (literal)`

---

### `0014` DIV_INT_VAR_BY_VAL
Divides the int VAR by the value

**Operator:** `/`

**Input:**
- `int (global var)`
- `int (literal)`

---

### `0015` DIV_FLOAT_VAR_BY_VAL
Divides the float VAR by the value

**Operator:** `/`

**Input:**
- `float (global var)`
- `float (literal)`

---

### `0016` DIV_INT_LVAR_BY_VAL
Divides the int LVAR by the value

**Operator:** `/`

**Input:**
- `int (local var)`
- `int (literal)`

---

### `0017` DIV_FLOAT_LVAR_BY_VAL
Divides the float LVAR by the value

**Operator:** `/`

**Input:**
- `float (local var)`
- `float (literal)`

---

### `004E` TERMINATE_THIS_SCRIPT
Ends the current script, preventing further execution

**Flags:** branch

---

### `004F` START_NEW_SCRIPT
Starts a new script at the specified label


**Input:**
- `label`
- `arguments`

---

### `0054` GET_PLAYER_COORDINATES

**Flags:** unsupported

---

### `0055` SET_PLAYER_COORDINATES

**Flags:** unsupported

---

### `0056` IS_PLAYER_IN_AREA_2D

**Flags:** unsupported

---

### `0057` IS_PLAYER_IN_AREA_3D

**Flags:** unsupported

---

### `0058` ADD_INT_VAR_TO_INT_VAR
Adds the int VAR value to the other int VAR

**Operator:** `+`

**Input:**
- `int (global var)`
- `int (global var)`

---

### `0059` ADD_FLOAT_VAR_TO_FLOAT_VAR
Adds the float VAR value to the other float VAR

**Operator:** `+`

**Input:**
- `float (global var)`
- `float (global var)`

---

### `005A` ADD_INT_LVAR_TO_INT_LVAR
Adds the int LVAR value to the other int LVAR

**Operator:** `+`

**Input:**
- `int (local var)`
- `int (local var)`

---

### `005B` ADD_FLOAT_LVAR_TO_FLOAT_LVAR
Adds the float LVAR value to the other float LVAR

**Operator:** `+`

**Input:**
- `float (local var)`
- `float (local var)`

---

### `005C` ADD_INT_VAR_TO_INT_LVAR
Adds the int VAR value to the int LVAR

**Operator:** `+`

**Input:**
- `int (local var)`
- `int (global var)`

---

### `005D` ADD_FLOAT_VAR_TO_FLOAT_LVAR
Adds the float VAR value to the float LVAR

**Operator:** `+`

**Input:**
- `float (local var)`
- `float (global var)`

---

### `005E` ADD_INT_LVAR_TO_INT_VAR
Adds the float LVAR value to the float VAR

**Operator:** `+`

**Input:**
- `int (global var)`
- `int (local var)`

---

### `005F` ADD_FLOAT_LVAR_TO_FLOAT_VAR
Adds the float LVAR value to the float VAR

**Operator:** `+`

**Input:**
- `float (global var)`
- `float (local var)`

---

### `0060` SUB_INT_VAR_FROM_INT_VAR
Subtracts the int VAR value from the int VAR

**Operator:** `-`

**Input:**
- `int (global var)`
- `int (global var)`

---

### `0061` SUB_FLOAT_VAR_FROM_FLOAT_VAR
Subtracts the float VAR value from the float VAR

**Operator:** `-`

**Input:**
- `float (global var)`
- `float (global var)`

---

### `0062` SUB_INT_LVAR_FROM_INT_LVAR
Subtracts the int LVAR value from the int LVAR

**Operator:** `-`

**Input:**
- `int (local var)`
- `int (local var)`

---

### `0063` SUB_FLOAT_LVAR_FROM_FLOAT_LVAR
Subtracts the float LVAR value from the float LVAR

**Operator:** `-`

**Input:**
- `float (local var)`
- `float (local var)`

---

### `0064` SUB_INT_VAR_FROM_INT_LVAR
Subtracts the int VAR value from the int LVAR

**Operator:** `-`

**Input:**
- `int (local var)`
- `int (global var)`

---

### `0065` SUB_FLOAT_VAR_FROM_FLOAT_LVAR
Subtracts the float VAR value from the float LVAR

**Operator:** `-`

**Input:**
- `float (local var)`
- `float (global var)`

---

### `0066` SUB_INT_LVAR_FROM_INT_VAR
Subtracts the float LVAR value from the float VAR

**Operator:** `-`

**Input:**
- `int (global var)`
- `int (local var)`

---

### `0067` SUB_FLOAT_LVAR_FROM_FLOAT_VAR
Subtracts the float LVAR value from the float VAR

**Operator:** `-`

**Input:**
- `float (global var)`
- `float (local var)`

---

### `0068` MULT_INT_VAR_BY_INT_VAR
Multiplies the int VAR value by the int VAR

**Operator:** `*`

**Input:**
- `int (global var)`
- `int (global var)`

---

### `0069` MULT_FLOAT_VAR_BY_FLOAT_VAR
Multiplies the float VAR value by the float VAR

**Operator:** `*`

**Input:**
- `float (global var)`
- `float (global var)`

---

### `006A` MULT_INT_LVAR_BY_INT_LVAR
Multiplies the int LVAR value by the int LVAR

**Operator:** `*`

**Input:**
- `int (local var)`
- `int (local var)`

---

### `006B` MULT_FLOAT_LVAR_BY_FLOAT_LVAR
Multiplies the int LVAR value by the int LVAR

**Operator:** `*`

**Input:**
- `float (local var)`
- `float (local var)`

---

### `006C` MULT_INT_VAR_BY_INT_LVAR
Multiplies the int VAR value by the int LVAR

**Operator:** `*`

**Input:**
- `int (global var)`
- `int (local var)`

---

### `006D` MULT_FLOAT_VAR_BY_FLOAT_LVAR
Multiplies the float VAR value by the float LVAR

**Operator:** `*`

**Input:**
- `float (global var)`
- `float (local var)`

---

### `006E` MULT_INT_LVAR_BY_INT_VAR
Multiplies the int LVAR value by the int VAR

**Operator:** `*`

**Input:**
- `int (local var)`
- `int (global var)`

---

### `006F` MULT_FLOAT_LVAR_BY_FLOAT_VAR
Multiplies the float LVAR value by the float VAR

**Operator:** `*`

**Input:**
- `float (local var)`
- `float (global var)`

---

### `0070` DIV_INT_VAR_BY_INT_VAR
Divides the int VAR value by the int VAR

**Operator:** `/`

**Input:**
- `int (global var)`
- `int (global var)`

---

### `0071` DIV_FLOAT_VAR_BY_FLOAT_VAR
Divides the float VAR value by the float VAR

**Operator:** `/`

**Input:**
- `float (global var)`
- `float (global var)`

---

### `0072` DIV_INT_LVAR_BY_INT_LVAR
Divides the int LVAR by the int LVAR

**Operator:** `/`

**Input:**
- `int (local var)`
- `int (local var)`

---

### `0073` DIV_FLOAT_LVAR_BY_FLOAT_LVAR
Divides the float LVAR by the float LVAR

**Operator:** `/`

**Input:**
- `float (local var)`
- `float (local var)`

---

### `0074` DIV_INT_VAR_BY_INT_LVAR
Divides the int VAR by the int LVAR

**Operator:** `/`

**Input:**
- `int (global var)`
- `int (local var)`

---

### `0075` DIV_FLOAT_VAR_BY_FLOAT_LVAR
Divides the float VAR by the float LVAR

**Operator:** `/`

**Input:**
- `float (global var)`
- `float (local var)`

---

### `0076` DIV_INT_LVAR_BY_INT_VAR
Divides the int LVAR by the int VAR

**Operator:** `/`

**Input:**
- `int (local var)`
- `int (global var)`

---

### `0077` DIV_FLOAT_LVAR_BY_FLOAT_VAR
Divides the float LVAR by the float VAR

**Operator:** `/`

**Input:**
- `float (local var)`
- `float (global var)`

---

### `0078` ADD_TIMED_VAL_TO_FLOAT_VAR
Multiplies the delta time since the last frame by the specified value and adds the result to the specified variable

**Operator:** `+=@`

**Input:**
- `float (global var)`
- `float (literal)`

---

### `0079` ADD_TIMED_VAL_TO_FLOAT_LVAR
Multiplies the delta time since the last frame by the specified value and adds the result to the specified variable

**Operator:** `+=@`

**Input:**
- `float (local var)`
- `float (literal)`

---

### `007A` ADD_TIMED_FLOAT_VAR_TO_FLOAT_VAR
Multiplies the delta time since the last frame by the float value of the specified global variable and adds the result to the specified global variable

**Operator:** `+=@`

**Input:**
- `float (global var)`
- `float (global var)`

---

### `007B` ADD_TIMED_FLOAT_LVAR_TO_FLOAT_LVAR
Multiplies the delta time since the last frame by the float value of the specified local variable and adds the result to the specified local variable

**Operator:** `+=@`

**Input:**
- `float (local var)`
- `float (local var)`

---

### `007C` ADD_TIMED_FLOAT_VAR_TO_FLOAT_LVAR
Multiplies the delta time since the last frame by the float value of the specified global variable and adds the result to the specified local variable

**Operator:** `+=@`

**Input:**
- `float (local var)`
- `float (global var)`

---

### `007D` ADD_TIMED_FLOAT_LVAR_TO_FLOAT_VAR
Multiplies the delta time since the last frame by the float value of the specified local variable and adds the result to the specified global variable

**Operator:** `+=@`

**Input:**
- `float (global var)`
- `float (local var)`

---

### `007E` SUB_TIMED_VAL_FROM_FLOAT_VAR
Multiplies the delta time since the last frame by the specified float value and subtracts the result from the specified global variable

**Operator:** `-=@`

**Input:**
- `float (global var)`
- `float (literal)`

---

### `007F` SUB_TIMED_VAL_FROM_FLOAT_LVAR
Multiplies the delta time since the last frame by the specified value and subtracts the result from the specified local variable

**Operator:** `-=@`

**Input:**
- `float (local var)`
- `float (literal)`

---

### `0080` SUB_TIMED_FLOAT_VAR_FROM_FLOAT_VAR
Multiplies the delta time since the last frame by the value of the specified global variable and subtracts the result from the specified global variable

**Operator:** `-=@`

**Input:**
- `float (global var)`
- `float (global var)`

---

### `0081` SUB_TIMED_FLOAT_LVAR_FROM_FLOAT_LVAR
Multiplies the delta time since the last frame by the value of the specified local variable and adds the result to the specified local variable

**Operator:** `-=@`

**Input:**
- `float (local var)`
- `float (local var)`

---

### `0082` SUB_TIMED_FLOAT_VAR_FROM_FLOAT_LVAR
Multiplies the delta time since the last frame by the value of the specified global variable and subtracts the result from the specified local variable

**Operator:** `-=@`

**Input:**
- `float (local var)`
- `float (global var)`

---

### `0083` SUB_TIMED_FLOAT_LVAR_FROM_FLOAT_VAR
Multiplies the frame delta time (the time in milliseconds that has passed since the last frame) by float stored in the specified local variable

**Operator:** `-=@`

**Input:**
- `float (global var)`
- `float (local var)`

---

### `009C` CHAR_WANDER_DIR

**Flags:** unsupported

---

### `009D` CHAR_WANDER_RANGE

**Flags:** unsupported

---

### `009E` CHAR_FOLLOW_PATH

**Flags:** unsupported

---

### `009F` CHAR_SET_IDLE

**Flags:** unsupported

---

### `00A2` IS_CHAR_STILL_ALIVE

**Flags:** unsupported

---

### `00AC` IS_CAR_STILL_ALIVE

**Flags:** unsupported

---

### `00B2` SPECIAL_0

**Flags:** unsupported

---

### `00B3` SPECIAL_1

**Flags:** unsupported

---

### `00B4` SPECIAL_2

**Flags:** unsupported

---

### `00B5` SPECIAL_3

**Flags:** unsupported

---

### `00B6` SPECIAL_4

**Flags:** unsupported

---

### `00B7` SPECIAL_5

**Flags:** unsupported

---

### `00B8` SPECIAL_6

**Flags:** unsupported

---

### `00B9` SPECIAL_7

**Flags:** unsupported

---

### `00BD` PRINT_SOON

**Flags:** unsupported

---

### `00C7` VAR_INT

**Flags:** unsupported

---

### `00C8` VAR_FLOAT

**Flags:** unsupported

---

### `00C9` LVAR_INT

**Flags:** unsupported

---

### `00CA` LVAR_FLOAT

**Flags:** unsupported

---

### `00CB` {

**Flags:** unsupported

---

### `00CC` }

**Flags:** unsupported

---

### `00D3` WHILE

**Flags:** unsupported

---

### `00D4` WHILENOT

**Flags:** unsupported

---

### `00D5` ENDWHILE

**Flags:** unsupported

---

### `00D7` LAUNCH_MISSION
Launches a submission script


**Input:**
- `label`

---

### `00DA` STORE_CAR_PLAYER_IS_IN

**Flags:** unsupported

---

### `00DC` IS_PLAYER_IN_CAR

**Flags:** unsupported

---

### `00DE` IS_PLAYER_IN_MODEL

**Flags:** unsupported

---

### `00E0` IS_PLAYER_IN_ANY_CAR

**Flags:** unsupported

---

### `00E3` LOCATE_PLAYER_ANY_MEANS_2D

**Flags:** unsupported

---

### `00E4` LOCATE_PLAYER_ON_FOOT_2D

**Flags:** unsupported

---

### `00E5` LOCATE_PLAYER_IN_CAR_2D

**Flags:** unsupported

---

### `00E6` LOCATE_STOPPED_PLAYER_ANY_MEANS_2D

**Flags:** unsupported

---

### `00E7` LOCATE_STOPPED_PLAYER_ON_FOOT_2D

**Flags:** unsupported

---

### `00E8` LOCATE_STOPPED_PLAYER_IN_CAR_2D

**Flags:** unsupported

---

### `00E9` LOCATE_PLAYER_ANY_MEANS_CHAR_2D

**Flags:** unsupported

---

### `00EA` LOCATE_PLAYER_ON_FOOT_CHAR_2D

**Flags:** unsupported

---

### `00EB` LOCATE_PLAYER_IN_CAR_CHAR_2D

**Flags:** unsupported

---

### `00F5` LOCATE_PLAYER_ANY_MEANS_3D

**Flags:** unsupported

---

### `00F6` LOCATE_PLAYER_ON_FOOT_3D

**Flags:** unsupported

---

### `00F7` LOCATE_PLAYER_IN_CAR_3D

**Flags:** unsupported

---

### `00F8` LOCATE_STOPPED_PLAYER_ANY_MEANS_3D

**Flags:** unsupported

---

### `00F9` LOCATE_STOPPED_PLAYER_ON_FOOT_3D

**Flags:** unsupported

---

### `00FA` LOCATE_STOPPED_PLAYER_IN_CAR_3D

**Flags:** unsupported

---

### `00FB` LOCATE_PLAYER_ANY_MEANS_CHAR_3D

**Flags:** unsupported

---

### `00FC` LOCATE_PLAYER_ON_FOOT_CHAR_3D

**Flags:** unsupported

---

### `00FD` LOCATE_PLAYER_IN_CAR_CHAR_3D

**Flags:** unsupported

---

### `010C` GIVE_REMOTE_CONTROLLED_CAR_TO_PLAYER
Gives control of the remote-control vehicle to the player

**Flags:** nop

---

### `0111` SET_DEATHARREST_STATE
Sets the detection of death and arrest during a mission (0112)


**Input:**
- `state: bool`

---

### `0112` HAS_DEATHARREST_BEEN_EXECUTED
Returns true if the player is dead (wasted) or arrested (busted)

**Flags:** condition

---

### `0113` ADD_AMMO_TO_PLAYER

**Flags:** unsupported

---

### `0115` ADD_AMMO_TO_CAR

**Flags:** unsupported

---

### `0116` IS_PLAYER_STILL_ALIVE

**Flags:** unsupported

---

### `011A` SET_CHAR_THREAT_SEARCH

**Flags:** unsupported

---

### `011B` SET_CHAR_THREAT_REACTION

**Flags:** unsupported

---

### `011C` SET_CHAR_OBJ_NO_OBJ

**Flags:** unsupported

---

### `011D` ORDER_DRIVER_OUT_OF_CAR

**Flags:** unsupported

---

### `011E` ORDER_CHAR_TO_DRIVE_CAR

**Flags:** unsupported

---

### `011F` ADD_PATROL_POINT

**Flags:** unsupported

---

### `0120` IS_PLAYER_IN_GANGZONE

**Flags:** unsupported

---

### `0121` IS_PLAYER_IN_ZONE

**Flags:** unsupported

---

### `0123` HAS_CHAR_SPOTTED_PLAYER

**Flags:** unsupported

---

### `0124` ORDER_CHAR_TO_BACKDOOR

**Flags:** unsupported

---

### `0125` ADD_CHAR_TO_GANG

**Flags:** unsupported

---

### `0126` IS_CHAR_OBJECTIVE_PASSED

**Flags:** unsupported

---

### `0127` SET_CHAR_DRIVE_AGGRESSION

**Flags:** unsupported

---

### `0128` SET_CHAR_MAX_DRIVESPEED

**Flags:** unsupported

---

### `012A` WARP_PLAYER_FROM_CAR_TO_COORD

**Flags:** unsupported

---

### `012B` MAKE_CHAR_DO_NOTHING

**Flags:** unsupported

---

### `012C` SET_CHAR_INVINCIBLE

**Flags:** unsupported

---

### `012D` SET_PLAYER_INVINCIBLE

**Flags:** unsupported

---

### `012E` SET_CHAR_GRAPHIC_TYPE

**Flags:** unsupported

---

### `012F` SET_PLAYER_GRAPHIC_TYPE

**Flags:** unsupported

---

### `0130` HAS_PLAYER_BEEN_ARRESTED

**Flags:** unsupported

---

### `0131` STOP_CHAR_DRIVING

**Flags:** unsupported

---

### `0132` KILL_CHAR

**Flags:** unsupported

---

### `0133` SET_FAVOURITE_CAR_MODEL_FOR_CHAR

**Flags:** unsupported

---

### `0134` SET_CHAR_OCCUPATION

**Flags:** unsupported

---

### `0135` CHANGE_CAR_LOCK

**Flags:** unsupported

---

### `0136` SHAKE_CAM_WITH_POINT

**Flags:** unsupported

---

### `0138` IS_CAR_REMAP

**Flags:** unsupported

---

### `0139` HAS_CAR_JUST_SUNK

**Flags:** unsupported

---

### `013A` SET_CAR_NO_COLLIDE

**Flags:** unsupported

---

### `013B` IS_CAR_DEAD_IN_AREA_2D

**Flags:** unsupported

---

### `013C` IS_CAR_DEAD_IN_AREA_3D

**Flags:** unsupported

---

### `013D` IS_TRAILER_ATTACHED

**Flags:** unsupported

---

### `013E` IS_CAR_ON_TRAILER

**Flags:** unsupported

---

### `013F` HAS_CAR_GOT_WEAPON

**Flags:** unsupported

---

### `0140` PARK

**Flags:** unsupported

---

### `0141` HAS_PARK_FINISHED

**Flags:** unsupported

---

### `0142` KILL_ALL_PASSENGERS

**Flags:** unsupported

---

### `0143` SET_CAR_BULLETPROOF

**Flags:** unsupported

---

### `0144` SET_CAR_FLAMEPROOF

**Flags:** unsupported

---

### `0145` SET_CAR_ROCKETPROOF

**Flags:** unsupported

---

### `0146` IS_CARBOMB_ACTIVE

**Flags:** unsupported

---

### `0147` GIVE_CAR_ALARM

**Flags:** unsupported

---

### `0148` PUT_CAR_ON_TRAILER

**Flags:** unsupported

---

### `0149` IS_CAR_CRUSHED

**Flags:** unsupported

---

### `014A` CREATE_GANG_CAR

**Flags:** unsupported

---

### `014D` ADD_PAGER_MESSAGE

**Flags:** unsupported

---

### `0150` DISPLAY_ONSCREEN_COUNTER

**Flags:** unsupported

---

### `0152` SET_ZONE_CAR_INFO

**Flags:** unsupported

---

### `0153` IS_CHAR_IN_GANG_ZONE

**Flags:** unsupported

---

### `0155` SET_CAR_DENSITY

**Flags:** unsupported

---

### `0156` SET_PED_DENSITY

**Flags:** unsupported

---

### `0157` POINT_CAMERA_AT_PLAYER

**Flags:** unsupported

---

### `015C` SET_ZONE_PED_INFO

**Flags:** unsupported

---

### `015E` IS_CAR_IN_AIR

**Flags:** unsupported

---

### `0162` ADD_BLIP_FOR_CHAR_OLD

**Flags:** nop

---

### `0163` ADD_BLIP_FOR_OBJECT_OLD

**Flags:** unsupported

---

### `0166` DIM_BLIP

**Flags:** unsupported

---

### `0170` GET_PLAYER_HEADING

**Flags:** unsupported

---

### `0171` SET_PLAYER_HEADING

**Flags:** unsupported

---

### `0178` IS_PLAYER_TOUCHING_OBJECT

**Flags:** unsupported

---

### `017A` SET_PLAYER_AMMO

**Flags:** unsupported

---

### `017C` SET_CAR_AMMO

**Flags:** unsupported

---

### `017D` LOAD_CAMERA_SPLINE

**Flags:** unsupported

---

### `017E` MOVE_CAMERA_ALONG_SPLINE

**Flags:** unsupported

---

### `017F` GET_CAMERA_POSITION_ALONG_SPLINE

**Flags:** unsupported

---

### `0180` DECLARE_MISSION_FLAG
Links the global variable to the specific hardcoded flag that defines is there an active mission or not


**Input:**
- `flag: int (global var)`

---

### `0181` DECLARE_MISSION_FLAG_FOR_CONTACT

**Flags:** unsupported

---

### `0182` DECLARE_BASE_BRIEF_ID_FOR_CONTACT

**Flags:** unsupported

---

### `0189` ADD_BLIP_FOR_CONTACT_POINT

**Flags:** unsupported

---

### `018D` ADD_CONTINUOUS_SOUND
Creates a continuous sound at the specified coordinates and stores the handle to a variable

**Flags:** nop

**Input:**
- `_p1: any`
- `_p2: any`
- `_p3: any`
- `_p4: any`
- `_p5: any`

---

### `0192` SET_CHAR_OBJ_WAIT_ON_FOOT

**Flags:** unsupported

---

### `0193` SET_CHAR_OBJ_FLEE_ON_FOOT_TILL_SAFE

**Flags:** unsupported

---

### `0194` SET_CHAR_OBJ_GUARD_SPOT

**Flags:** unsupported

---

### `0195` SET_CHAR_OBJ_GUARD_AREA

**Flags:** unsupported

---

### `0196` SET_CHAR_OBJ_WAIT_IN_CAR

**Flags:** unsupported

---

### `0197` IS_PLAYER_IN_AREA_ON_FOOT_2D

**Flags:** unsupported

---

### `0198` IS_PLAYER_IN_AREA_IN_CAR_2D

**Flags:** unsupported

---

### `0199` IS_PLAYER_STOPPED_IN_AREA_2D

**Flags:** unsupported

---

### `019A` IS_PLAYER_STOPPED_IN_AREA_ON_FOOT_2D

**Flags:** unsupported

---

### `019B` IS_PLAYER_STOPPED_IN_AREA_IN_CAR_2D

**Flags:** unsupported

---

### `019C` IS_PLAYER_IN_AREA_ON_FOOT_3D

**Flags:** unsupported

---

### `019D` IS_PLAYER_IN_AREA_IN_CAR_3D

**Flags:** unsupported

---

### `019E` IS_PLAYER_STOPPED_IN_AREA_3D

**Flags:** unsupported

---

### `019F` IS_PLAYER_STOPPED_IN_AREA_ON_FOOT_3D

**Flags:** unsupported

---

### `01A0` IS_PLAYER_STOPPED_IN_AREA_IN_CAR_3D

**Flags:** unsupported

---

### `01B1` GIVE_WEAPON_TO_PLAYER

**Flags:** unsupported

---

### `01B3` GIVE_WEAPON_TO_CAR

**Flags:** unsupported

---

### `01B8` SET_CURRENT_PLAYER_WEAPON

**Flags:** unsupported

---

### `01BA` SET_CURRENT_CAR_WEAPON

**Flags:** unsupported

---

### `01BE` TURN_CHAR_TO_FACE_COORD

**Flags:** unsupported

---

### `01BF` TURN_PLAYER_TO_FACE_COORD

**Flags:** unsupported

---

### `01C6` DONT_REMOVE_CAR

**Flags:** unsupported

---

### `01C9` SET_CHAR_OBJ_KILL_CHAR_ON_FOOT

**Flags:** unsupported

---

### `01CA` SET_CHAR_OBJ_KILL_PLAYER_ON_FOOT

**Flags:** unsupported

---

### `01CB` SET_CHAR_OBJ_KILL_CHAR_ANY_MEANS

**Flags:** unsupported

---

### `01CC` SET_CHAR_OBJ_KILL_PLAYER_ANY_MEANS

**Flags:** unsupported

---

### `01CD` SET_CHAR_OBJ_FLEE_CHAR_ON_FOOT_TILL_SAFE

**Flags:** unsupported

---

### `01CE` SET_CHAR_OBJ_FLEE_PLAYER_ON_FOOT_TILL_SAFE

**Flags:** unsupported

---

### `01CF` SET_CHAR_OBJ_FLEE_CHAR_ON_FOOT_ALWAYS

**Flags:** unsupported

---

### `01D0` SET_CHAR_OBJ_FLEE_PLAYER_ON_FOOT_ALWAYS

**Flags:** unsupported

---

### `01D3` SET_CHAR_OBJ_LEAVE_CAR

**Flags:** unsupported

---

### `01D4` SET_CHAR_OBJ_ENTER_CAR_AS_PASSENGER

**Flags:** unsupported

---

### `01D5` SET_CHAR_OBJ_ENTER_CAR_AS_DRIVER

**Flags:** unsupported

---

### `01D6` SET_CHAR_OBJ_FOLLOW_CAR_IN_CAR

**Flags:** unsupported

---

### `01D7` SET_CHAR_OBJ_FIRE_AT_OBJECT_FROM_VEHICLE

**Flags:** unsupported

---

### `01D8` SET_CHAR_OBJ_DESTROY_OBJECT

**Flags:** unsupported

---

### `01D9` SET_CHAR_OBJ_DESTROY_CAR

**Flags:** unsupported

---

### `01DC` SET_CHAR_OBJ_FOLLOW_CAR_ON_FOOT_WITH_OFFSET

**Flags:** unsupported

---

### `01DD` SET_CHAR_OBJ_GUARD_ATTACK

**Flags:** unsupported

---

### `01DE` SET_CHAR_AS_LEADER

**Flags:** unsupported

---

### `01DF` SET_PLAYER_AS_LEADER

**Flags:** unsupported

---

### `01E0` LEAVE_GROUP

**Flags:** unsupported

---

### `01E1` SET_CHAR_OBJ_FOLLOW_ROUTE

**Flags:** unsupported

---

### `01E2` ADD_ROUTE_POINT

**Flags:** unsupported

---

### `01E6` PRINT_WITH_NUMBER_SOON

**Flags:** unsupported

---

### `01ED` CLEAR_CHAR_THREAT_SEARCH

**Flags:** unsupported

---

### `01EE` ACTIVATE_CRANE

**Flags:** unsupported

---

### `01EF` DEACTIVATE_CRANE

**Flags:** unsupported

---

### `01F1` SAVE_VAR_INT

**Flags:** unsupported

---

### `01F2` SAVE_VAR_FLOAT

**Flags:** unsupported

---

### `01F8` ADD_PAGER_MESSAGE_WITH_NUMBER

**Flags:** unsupported

---

### `01FC` LOCATE_PLAYER_ANY_MEANS_CAR_2D

**Flags:** unsupported

---

### `01FD` LOCATE_PLAYER_ON_FOOT_CAR_2D

**Flags:** unsupported

---

### `01FE` LOCATE_PLAYER_IN_CAR_CAR_2D

**Flags:** unsupported

---

### `01FF` LOCATE_PLAYER_ANY_MEANS_CAR_3D

**Flags:** unsupported

---

### `0200` LOCATE_PLAYER_ON_FOOT_CAR_3D

**Flags:** unsupported

---

### `0201` LOCATE_PLAYER_IN_CAR_CAR_3D

**Flags:** unsupported

---

### `020E` TURN_CHAR_TO_FACE_CHAR

**Flags:** unsupported

---

### `020F` TURN_CHAR_TO_FACE_PLAYER

**Flags:** unsupported

---

### `0210` TURN_PLAYER_TO_FACE_CHAR

**Flags:** unsupported

---

### `0218` PRINT_WITH_NUMBER_BIG_Q

**Flags:** unsupported

---

### `0219` SET_GARAGE

**Flags:** unsupported

---

### `021A` SET_GARAGE_WITH_CAR_MODEL

**Flags:** unsupported

---

### `021C` IS_CAR_IN_MISSION_GARAGE

**Flags:** unsupported

---

### `021D` SET_FREE_BOMBS

**Flags:** unsupported

---

### `021E` SET_POWERPOINT

**Flags:** unsupported

---

### `021F` SET_ALL_TAXI_LIGHTS

**Flags:** unsupported

---

### `0220` IS_CAR_ARMED_WITH_ANY_BOMB

**Flags:** unsupported

---

### `0222` SET_PLAYER_HEALTH

**Flags:** unsupported

---

### `0225` GET_PLAYER_HEALTH

**Flags:** unsupported

---

### `0228` IS_CAR_ARMED_WITH_BOMB

**Flags:** unsupported

---

### `022C` CHAR_LOOK_AT_CHAR_ALWAYS

**Flags:** unsupported

---

### `022D` CHAR_LOOK_AT_PLAYER_ALWAYS

**Flags:** unsupported

---

### `022E` PLAYER_LOOK_AT_CHAR_ALWAYS

**Flags:** unsupported

---

### `022F` STOP_CHAR_LOOKING

**Flags:** unsupported

---

### `0230` STOP_PLAYER_LOOKING

**Flags:** unsupported

---

### `0231` SET_SCRIPT_POLICE_HELI_TO_CHASE_CHAR

**Flags:** unsupported

---

### `0232` SET_GANG_ATTITUDE

**Flags:** unsupported

---

### `0233` SET_GANG_GANG_ATTITUDE

**Flags:** unsupported

---

### `0234` SET_GANG_PLAYER_ATTITUDE

**Flags:** unsupported

---

### `0235` SET_GANG_PED_MODELS
Sets the models used by members of the specified gang

**Flags:** nop

**Input:**
- `_p1: any`
- `_p2: any`
- `_p3: any`

---

### `0236` SET_GANG_CAR_MODEL
Sets the car used by members of the specified gang

**Flags:** nop

**Input:**
- `_p1: any`
- `_p2: any`

---

### `0238` SET_CHAR_OBJ_RUN_TO_AREA

**Flags:** unsupported

---

### `0239` SET_CHAR_OBJ_RUN_TO_COORD

**Flags:** unsupported

---

### `023A` IS_PLAYER_TOUCHING_OBJECT_ON_FOOT

**Flags:** unsupported

---

### `023E` FLASH_CAR

**Flags:** unsupported

---

### `023F` FLASH_CHAR

**Flags:** unsupported

---

### `0240` FLASH_OBJECT

**Flags:** unsupported

---

### `0242` ARM_CAR_WITH_BOMB

**Flags:** unsupported

---

### `0243` SET_CHAR_PERSONALITY

**Flags:** unsupported

---

### `0246` SET_ANIM_GROUP_FOR_PLAYER

**Flags:** unsupported

---

### `024A` GRAB_PHONE

**Flags:** unsupported

---

### `024B` SET_REPEATED_PHONE_MESSAGE

**Flags:** unsupported

---

### `024C` SET_PHONE_MESSAGE

**Flags:** unsupported

---

### `024D` HAS_PHONE_DISPLAYED_MESSAGE

**Flags:** unsupported

---

### `024E` TURN_PHONE_OFF

**Flags:** unsupported

---

### `0250` DRAW_LIGHT

**Flags:** unsupported

---

### `0251` STORE_WEATHER

**Flags:** unsupported

---

### `0252` RESTORE_WEATHER

**Flags:** unsupported

---

### `0255` RESTART_CRITICAL_MISSION

**Flags:** unsupported

---

### `0257` SET_COLL_OBJ_NO_OBJ

**Flags:** unsupported

---

### `0258` SET_COLL_OBJ_WAIT_ON_FOOT

**Flags:** unsupported

---

### `0259` SET_COLL_OBJ_FLEE_ON_FOOT_TILL_SAFE

**Flags:** unsupported

---

### `025A` SET_COLL_OBJ_GUARD_SPOT

**Flags:** unsupported

---

### `025B` SET_COLL_OBJ_GUARD_AREA

**Flags:** unsupported

---

### `025C` SET_COLL_OBJ_WAIT_IN_CAR

**Flags:** unsupported

---

### `025D` SET_COLL_OBJ_KILL_CHAR_ON_FOOT

**Flags:** unsupported

---

### `025E` SET_COLL_OBJ_KILL_PLAYER_ON_FOOT

**Flags:** unsupported

---

### `025F` SET_COLL_OBJ_KILL_CHAR_ANY_MEANS

**Flags:** unsupported

---

### `0260` SET_COLL_OBJ_KILL_PLAYER_ANY_MEANS

**Flags:** unsupported

---

### `0261` SET_COLL_OBJ_FLEE_CHAR_ON_FOOT_TILL_SAFE

**Flags:** unsupported

---

### `0262` SET_COLL_OBJ_FLEE_PLAYER_ON_FOOT_TILL_SAFE

**Flags:** unsupported

---

### `0263` SET_COLL_OBJ_FLEE_CHAR_ON_FOOT_ALWAYS

**Flags:** unsupported

---

### `0264` SET_COLL_OBJ_FLEE_PLAYER_ON_FOOT_ALWAYS

**Flags:** unsupported

---

### `0267` SET_COLL_OBJ_LEAVE_CAR

**Flags:** unsupported

---

### `0268` SET_COLL_OBJ_ENTER_CAR_AS_PASSENGER

**Flags:** unsupported

---

### `0269` SET_COLL_OBJ_ENTER_CAR_AS_DRIVER

**Flags:** unsupported

---

### `026A` SET_COLL_OBJ_FOLLOW_CAR_IN_CAR

**Flags:** unsupported

---

### `026B` SET_COLL_OBJ_FIRE_AT_OBJECT_FROM_VEHICLE

**Flags:** unsupported

---

### `026C` SET_COLL_OBJ_DESTROY_OBJECT

**Flags:** unsupported

---

### `026D` SET_COLL_OBJ_DESTROY_CAR

**Flags:** unsupported

---

### `0270` SET_COLL_OBJ_FOLLOW_CAR_ON_FOOT_WITH_OFFSET

**Flags:** unsupported

---

### `0271` SET_COLL_OBJ_GUARD_ATTACK

**Flags:** unsupported

---

### `0272` SET_COLL_OBJ_FOLLOW_ROUTE

**Flags:** unsupported

---

### `0275` SET_COLL_OBJ_RUN_TO_AREA

**Flags:** unsupported

---

### `0276` SET_COLL_OBJ_RUN_TO_COORD

**Flags:** unsupported

---

### `0277` ADD_PEDS_IN_AREA_TO_COLL

**Flags:** unsupported

---

### `0278` ADD_PEDS_IN_VEHICLE_TO_COLL

**Flags:** unsupported

---

### `0279` CLEAR_COLL

**Flags:** unsupported

---

### `027A` IS_COLL_IN_CARS

**Flags:** unsupported

---

### `027B` LOCATE_COLL_ANY_MEANS_2D

**Flags:** unsupported

---

### `027C` LOCATE_COLL_ON_FOOT_2D

**Flags:** unsupported

---

### `027D` LOCATE_COLL_IN_CAR_2D

**Flags:** unsupported

---

### `027E` LOCATE_STOPPED_COLL_ANY_MEANS_2D

**Flags:** unsupported

---

### `027F` LOCATE_STOPPED_COLL_ON_FOOT_2D

**Flags:** unsupported

---

### `0280` LOCATE_STOPPED_COLL_IN_CAR_2D

**Flags:** unsupported

---

### `0281` LOCATE_COLL_ANY_MEANS_CHAR_2D

**Flags:** unsupported

---

### `0282` LOCATE_COLL_ON_FOOT_CHAR_2D

**Flags:** unsupported

---

### `0283` LOCATE_COLL_IN_CAR_CHAR_2D

**Flags:** unsupported

---

### `0284` LOCATE_COLL_ANY_MEANS_CAR_2D

**Flags:** unsupported

---

### `0285` LOCATE_COLL_ON_FOOT_CAR_2D

**Flags:** unsupported

---

### `0286` LOCATE_COLL_IN_CAR_CAR_2D

**Flags:** unsupported

---

### `0287` LOCATE_COLL_ANY_MEANS_PLAYER_2D

**Flags:** unsupported

---

### `0288` LOCATE_COLL_ON_FOOT_PLAYER_2D

**Flags:** unsupported

---

### `0289` LOCATE_COLL_IN_CAR_PLAYER_2D

**Flags:** unsupported

---

### `028A` IS_COLL_IN_AREA_2D

**Flags:** unsupported

---

### `028B` IS_COLL_IN_AREA_ON_FOOT_2D

**Flags:** unsupported

---

### `028C` IS_COLL_IN_AREA_IN_CAR_2D

**Flags:** unsupported

---

### `028D` IS_COLL_STOPPED_IN_AREA_2D

**Flags:** unsupported

---

### `028E` IS_COLL_STOPPED_IN_AREA_ON_FOOT_2D

**Flags:** unsupported

---

### `028F` IS_COLL_STOPPED_IN_AREA_IN_CAR_2D

**Flags:** unsupported

---

### `0290` GET_NUMBER_OF_PEDS_IN_COLL

**Flags:** unsupported

---

### `0291` SET_CHAR_HEED_THREATS

**Flags:** unsupported

---

### `0292` SET_PLAYER_HEED_THREATS

**Flags:** unsupported

---

### `0295` IS_TAXI

**Flags:** unsupported

---

### `029A` SWITCH_TAXI_TIMER

**Flags:** unsupported

---

### `029C` IS_BOAT

**Flags:** unsupported

---

### `029F` IS_PLAYER_STOPPED

**Flags:** unsupported

---

### `02A1` MESSAGE_WAIT

**Flags:** unsupported

---

### `02A2` ADD_PARTICLE_EFFECT

**Flags:** unsupported

---

### `02A4` ADD_SPRITE_BLIP_FOR_CAR
Does nothing

**Flags:** nop

---

### `02A5` ADD_SPRITE_BLIP_FOR_CHAR
Does nothing

**Flags:** nop

---

### `02A6` ADD_SPRITE_BLIP_FOR_OBJECT

**Flags:** unsupported

---

### `02AD` IS_PLAYER_IN_ANGLED_AREA_2D

**Flags:** unsupported

---

### `02AE` IS_PLAYER_IN_ANGLED_AREA_ON_FOOT_2D

**Flags:** unsupported

---

### `02AF` IS_PLAYER_IN_ANGLED_AREA_IN_CAR_2D

**Flags:** unsupported

---

### `02B0` IS_PLAYER_STOPPED_IN_ANGLED_AREA_2D

**Flags:** unsupported

---

### `02B1` IS_PLAYER_STOPPED_IN_ANGLED_AREA_ON_FOOT_2D

**Flags:** unsupported

---

### `02B2` IS_PLAYER_STOPPED_IN_ANGLED_AREA_IN_CAR_2D

**Flags:** unsupported

---

### `02B3` IS_PLAYER_IN_ANGLED_AREA_3D

**Flags:** unsupported

---

### `02B4` IS_PLAYER_IN_ANGLED_AREA_ON_FOOT_3D

**Flags:** unsupported

---

### `02B5` IS_PLAYER_IN_ANGLED_AREA_IN_CAR_3D

**Flags:** unsupported

---

### `02B6` IS_PLAYER_STOPPED_IN_ANGLED_AREA_3D

**Flags:** unsupported

---

### `02B7` IS_PLAYER_STOPPED_IN_ANGLED_AREA_ON_FOOT_3D

**Flags:** unsupported

---

### `02B8` IS_PLAYER_STOPPED_IN_ANGLED_AREA_IN_CAR_3D

**Flags:** unsupported

---

### `02BA` GET_NUMBER_OF_CARS_COLLECTED_BY_GARAGE

**Flags:** unsupported

---

### `02BB` HAS_CAR_BEEN_TAKEN_TO_GARAGE

**Flags:** unsupported

---

### `02BC` SET_SWAT_REQUIRED

**Flags:** unsupported

---

### `02BD` SET_FBI_REQUIRED

**Flags:** unsupported

---

### `02BE` SET_ARMY_REQUIRED

**Flags:** unsupported

---

### `02C3` START_PACMAN_RACE

**Flags:** unsupported

---

### `02C4` START_PACMAN_RECORD

**Flags:** unsupported

---

### `02C5` GET_NUMBER_OF_POWER_PILLS_EATEN

**Flags:** unsupported

---

### `02C6` CLEAR_PACMAN

**Flags:** unsupported

---

### `02C7` START_PACMAN_SCRAMBLE

**Flags:** unsupported

---

### `02C8` GET_NUMBER_OF_POWER_PILLS_CARRIED

**Flags:** unsupported

---

### `02C9` CLEAR_NUMBER_OF_POWER_PILLS_CARRIED

**Flags:** unsupported

---

### `02D2` SET_COMEDY_CONTROLS

**Flags:** unsupported

---

### `02D5` IS_PLAYER_SHOOTING_IN_AREA

**Flags:** unsupported

---

### `02D7` IS_CURRENT_PLAYER_WEAPON

**Flags:** unsupported

---

### `02D9` CLEAR_NUMBER_OF_POWER_PILLS_EATEN

**Flags:** unsupported

---

### `02DA` ADD_POWER_PILL

**Flags:** unsupported

---

### `02DC` GET_RANDOM_CHAR_IN_AREA

**Flags:** unsupported

---

### `02DE` IS_PLAYER_IN_TAXI

**Flags:** unsupported

---

### `02DF` IS_PLAYER_SHOOTING

**Flags:** unsupported

---

### `02E5` CREATE_CUTSCENE_OBJECT

**Flags:** nop

---

### `02E6` SET_CUTSCENE_ANIM

**Flags:** nop

---

### `02EC` CREATE_COLLECTABLE1
Does nothing

**Flags:** nop

**Input:**
- `_p1: any`
- `_p2: any`
- `_p3: any`

---

### `02EF` DESTROY_PROJECTILES_IN_AREA

**Flags:** unsupported

---

### `02F0` DROP_MINE

**Flags:** unsupported

---

### `02F1` DROP_NAUTICAL_MINE

**Flags:** unsupported

---

### `02F3` LOAD_SPECIAL_MODEL

**Flags:** nop

---

### `02F4` CREATE_CUTSCENE_HEAD

**Flags:** unsupported

---

### `02F5` SET_CUTSCENE_HEAD_ANIM

**Flags:** unsupported

---

### `02FB` ACTIVATE_CRUSHER_CRANE

**Flags:** unsupported

---

### `02FC` PRINT_WITH_2_NUMBERS

**Flags:** unsupported

---

### `02FE` PRINT_WITH_2_NUMBERS_SOON

**Flags:** unsupported

---

### `0300` PRINT_WITH_3_NUMBERS_NOW

**Flags:** unsupported

---

### `0301` PRINT_WITH_3_NUMBERS_SOON

**Flags:** unsupported

---

### `0304` PRINT_WITH_4_NUMBERS_SOON

**Flags:** unsupported

---

### `0305` PRINT_WITH_5_NUMBERS

**Flags:** unsupported

---

### `0306` PRINT_WITH_5_NUMBERS_NOW

**Flags:** unsupported

---

### `0307` PRINT_WITH_5_NUMBERS_SOON

**Flags:** unsupported

---

### `0309` PRINT_WITH_6_NUMBERS_NOW

**Flags:** unsupported

---

### `030A` PRINT_WITH_6_NUMBERS_SOON

**Flags:** unsupported

---

### `030B` SET_CHAR_OBJ_FOLLOW_CHAR_IN_FORMATION

**Flags:** unsupported

---

### `0315` REGISTER_PASSENGER_DROPPED_OFF_TAXI

**Flags:** unsupported

---

### `0316` REGISTER_MONEY_MADE_TAXI

**Flags:** unsupported

---

### `0319` SET_CHAR_RUNNING

**Flags:** nop

---

### `031B` IS_FIRST_CAR_COLOUR

**Flags:** unsupported

---

### `031C` IS_SECOND_CAR_COLOUR

**Flags:** unsupported

---

### `031F` IS_CHAR_IN_CHARS_GROUP

**Flags:** unsupported

---

### `0320` IS_CHAR_IN_PLAYERS_GROUP

**Flags:** unsupported

---

### `0322` EXPLODE_PLAYER_HEAD

**Flags:** unsupported

---

### `0324` SET_ZONE_GROUP

**Flags:** unsupported

---

### `0328` GET_RANDOM_CAR_OF_TYPE_IN_ZONE

**Flags:** unsupported

---

### `0329` HAS_RESPRAY_HAPPENED
Returns true if the players car has been resprayed by the garage

**Flags:** nop

---

### `032C` SET_CAR_RAM_CAR
Sets the cars goal to ram another car

**Flags:** nop

---

### `032D` SET_CAR_BLOCK_CAR

**Flags:** unsupported

---

### `032E` SET_CHAR_OBJ_CATCH_TRAIN

**Flags:** unsupported

---

### `032F` SET_COLL_OBJ_CATCH_TRAIN

**Flags:** unsupported

---

### `0333` SET_CAR_FUNNY_SUSPENSION

**Flags:** unsupported

---

### `0334` SET_CAR_BIG_WHEELS

**Flags:** unsupported

---

### `0336` SET_PLAYER_VISIBLE

**Flags:** unsupported

---

### `033A` START_DRUG_RUN

**Flags:** unsupported

---

### `033B` HAS_DRUG_RUN_BEEN_COMPLETED

**Flags:** unsupported

---

### `033C` HAS_DRUG_PLANE_BEEN_SHOT_DOWN

**Flags:** unsupported

---

### `033D` SAVE_PLAYER_FROM_FIRES

**Flags:** unsupported

---

### `034A` INDUSTRIAL_PASSED

**Flags:** unsupported

---

### `034B` COMMERCIAL_PASSED

**Flags:** unsupported

---

### `034C` SUBURBAN_PASSED

**Flags:** unsupported

---

### `0351` IS_NASTY_GAME

**Flags:** unsupported

---

### `0352` UNDRESS_CHAR

**Flags:** unsupported

---

### `0353` DRESS_CHAR

**Flags:** unsupported

---

### `0354` START_CHASE_SCENE

**Flags:** unsupported

---

### `0355` STOP_CHASE_SCENE

**Flags:** unsupported

---

### `0357` IS_EXPLOSION_IN_ZONE

**Flags:** unsupported

---

### `0358` START_DRUG_DROP_OFF

**Flags:** unsupported

---

### `0359` HAS_DROP_OFF_PLANE_BEEN_SHOT_DOWN

**Flags:** unsupported

---

### `035A` FIND_DROP_OFF_PLANE_COORDINATES

**Flags:** unsupported

---

### `035B` CREATE_FLOATING_PACKAGE

**Flags:** unsupported

---

### `035E` ADD_ARMOUR_TO_PLAYER

**Flags:** unsupported

---

### `0365` SET_CHAR_OBJ_HAIL_TAXI

**Flags:** unsupported

---

### `0367` START_KILL_FRENZY_HEADSHOT

**Flags:** unsupported

---

### `0368` ACTIVATE_MILITARY_CRANE

**Flags:** unsupported

---

### `0369` WARP_PLAYER_INTO_CAR

**Flags:** unsupported

---

### `036B` SWITCH_CAR_RADIO

**Flags:** unsupported

---

### `036C` SET_AUDIO_STREAM

**Flags:** unsupported

---

### `036E` PRINT_WITH_3_NUMBERS_BIG

**Flags:** unsupported

---

### `036F` PRINT_WITH_4_NUMBERS_BIG

**Flags:** unsupported

---

### `0370` PRINT_WITH_5_NUMBERS_BIG

**Flags:** unsupported

---

### `0371` PRINT_WITH_6_NUMBERS_BIG

**Flags:** unsupported

---

### `0372` SET_CHAR_WAIT_STATE

**Flags:** unsupported

---

### `0374` SET_MOTION_BLUR

**Flags:** unsupported

---

### `0377` SET_CHAR_OBJ_STEAL_ANY_CAR

**Flags:** unsupported

---

### `0378` SET_2_REPEATED_PHONE_MESSAGES

**Flags:** unsupported

---

### `0379` SET_2_PHONE_MESSAGES

**Flags:** unsupported

---

### `037A` SET_3_REPEATED_PHONE_MESSAGES

**Flags:** unsupported

---

### `037B` SET_3_PHONE_MESSAGES

**Flags:** unsupported

---

### `037C` SET_4_REPEATED_PHONE_MESSAGES

**Flags:** unsupported

---

### `037D` SET_4_PHONE_MESSAGES

**Flags:** unsupported

---

### `037E` IS_SNIPER_BULLET_IN_AREA
Returns true if a sniper bullet is in the specified area

**Flags:** nop

---

### `037F` GIVE_PLAYER_DETONATOR

**Flags:** unsupported

---

### `0380` SET_COLL_OBJ_STEAL_ANY_CAR

**Flags:** unsupported

---

### `0383` IS_ICECREAM_JINGLE_ON
Returns true if the vehicles siren is on

**Flags:** nop

---

### `0386` SET_5_REPEATED_PHONE_MESSAGES

**Flags:** unsupported

---

### `0387` SET_5_PHONE_MESSAGES

**Flags:** unsupported

---

### `0388` SET_6_REPEATED_PHONE_MESSAGES

**Flags:** unsupported

---

### `0389` SET_6_PHONE_MESSAGES

**Flags:** unsupported

---

### `0398` SWITCH_PED_ROADS_ON_ANGLED

**Flags:** unsupported

---

### `0399` SWITCH_PED_ROADS_OFF_ANGLED

**Flags:** unsupported

---

### `039A` SWITCH_ROADS_ON_ANGLED

**Flags:** unsupported

---

### `039B` SWITCH_ROADS_OFF_ANGLED

**Flags:** unsupported

---

### `039D` ADD_MOVING_PARTICLE_EFFECT

**Flags:** unsupported

---

### `03A4` SCRIPT_NAME
Assigns a new name to the current script


**Input:**
- `name: string`

---

### `03A5` CHANGE_GARAGE_TYPE_WITH_CAR_MODEL

**Flags:** unsupported

---

### `03A6` FIND_DRUG_PLANE_COORDINATES

**Flags:** unsupported

---

### `03A7` SAVE_INT_TO_DEBUG_FILE
Saves an integer to a debug file

**Flags:** nop

**Input:**
- `_p1: any`

---

### `03A8` SAVE_FLOAT_TO_DEBUG_FILE
Saves a float to the debug file

**Flags:** nop

**Input:**
- `_p1: any`

---

### `03A9` SAVE_NEWLINE_TO_DEBUG_FILE
Writes a newline to the debug file

**Flags:** nop

---

### `03AA` POLICE_RADIO_MESSAGE
Plays police radio message audio reporting the suspect has last been seen in the area specified by the coordinates

**Flags:** nop

**Input:**
- `_p1: any`
- `_p2: any`
- `_p3: any`

---

### `03AC` REMOVE_ROUTE

**Flags:** unsupported

---

### `03AD` SWITCH_RUBBISH
Toggles garbage

**Flags:** nop

**Input:**
- `_p1: any`

---

### `03AE` REMOVE_PARTICLE_EFFECTS_IN_AREA

**Flags:** unsupported

---

### `03B2` START_CATALINA_HELI

**Flags:** unsupported

---

### `03B3` CATALINA_HELI_TAKE_OFF

**Flags:** unsupported

---

### `03B4` REMOVE_CATALINA_HELI

**Flags:** unsupported

---

### `03B5` HAS_CATALINA_HELI_BEEN_SHOT_DOWN

**Flags:** unsupported

---

### `03B8` REMOVE_ALL_PLAYER_WEAPONS

**Flags:** unsupported

---

### `03B9` GRAB_CATALINA_HELI

**Flags:** unsupported

---

### `03BB` SET_ROTATING_GARAGE_DOOR

**Flags:** unsupported

---

### `03BE` CATALINA_HELI_FLY_AWAY

**Flags:** unsupported

---

### `03C1` STORE_CAR_PLAYER_IS_IN_NO_SAVE

**Flags:** unsupported

---

### `03C2` IS_PHONE_DISPLAYING_MESSAGE

**Flags:** unsupported

---

### `03C6` IS_COLLISION_IN_MEMORY

**Flags:** unsupported

---

### `03D4` HAS_IMPORT_GARAGE_SLOT_BEEN_FILLED
Returns true if the import slot has been filled

**Flags:** nop

---

### `03DA` NO_SPECIAL_CAMERA_FOR_THIS_GARAGE

**Flags:** nop

---

### `03DB` ADD_BLIP_FOR_PICKUP_OLD

**Flags:** unsupported

---

### `03DD` ADD_SPRITE_BLIP_FOR_PICKUP

**Flags:** unsupported

---

### `03DF` FORCE_RANDOM_PED_TYPE
Forces a model on all randomly spawning peds

**Flags:** nop

---

### `03E1` GET_COLLECTABLE1S_COLLECTED
Gets the number of collectable1s collected

**Flags:** nop

---

### `03E2` SET_CHAR_OBJ_LEAVE_ANY_CAR

**Flags:** unsupported

---

### `03E8` FLASH_RADAR_BLIP
Does nothing

**Flags:** nop

---

### `03E9` IS_CHAR_IN_CONTROL

**Flags:** unsupported

---

### `03EA` SET_GENERATE_CARS_AROUND_CAMERA

**Flags:** nop

---

### `03EC` HAS_MILITARY_CRANE_COLLECTED_ALL_CARS

**Flags:** unsupported

---

### `03F1` SET_THREAT_FOR_PED_TYPE

**Flags:** unsupported

---

### `03F2` CLEAR_THREAT_FOR_PED_TYPE

**Flags:** unsupported

---

### `03F6` MAKE_PLAYER_UNSAFE

**Flags:** unsupported

---

### `03F7` LOAD_COLLISION

**Flags:** unsupported

---

### `03F8` GET_BODY_CAST_HEALTH

**Flags:** unsupported

---

### `03F9` SET_CHARS_CHATTING

**Flags:** unsupported

---

### `03FA` MAKE_PLAYER_SAFE

**Flags:** unsupported

---

### `03FB` SET_CAR_STAYS_IN_CURRENT_LEVEL

**Flags:** unsupported

---

### `03FC` SET_CHAR_STAYS_IN_CURRENT_LEVEL

**Flags:** unsupported

---

### `03FF` INCREASE_CHAR_MONEY

**Flags:** unsupported

---

### `0402` REGISTER_CRIMINAL_CAUGHT

**Flags:** unsupported

---

### `0403` REGISTER_AMBULANCE_LEVEL

**Flags:** unsupported

---

### `0404` REGISTER_FIRE_EXTINGUISHED

**Flags:** unsupported

---

### `0405` TURN_PHONE_ON

**Flags:** unsupported

---

### `0406` REGISTER_LONGEST_DODO_FLIGHT

**Flags:** unsupported

---

### `0408` SET_TOTAL_NUMBER_OF_KILL_FRENZIES

**Flags:** unsupported

---

### `0409` BLOW_UP_RC_BUGGY

**Flags:** nop

---

### `040A` REMOVE_CAR_FROM_CHASE

**Flags:** unsupported

---

### `040B` IS_FRENCH_GAME
Returns true if the game is in French

**Flags:** nop

---

### `040E` SET_FADE_IN_AFTER_NEXT_ARREST

**Flags:** unsupported

---

### `040F` SET_FADE_IN_AFTER_NEXT_DEATH

**Flags:** unsupported

---

### `0410` SET_GANG_PED_MODEL_PREFERENCE

**Flags:** unsupported

---

### `0411` SET_CHAR_USE_PEDNODE_SEEK

**Flags:** unsupported

---

### `0412` SWITCH_VEHICLE_WEAPONS

**Flags:** unsupported

---

### `0413` SET_GET_OUT_OF_JAIL_FREE

**Flags:** unsupported

---

### `0415` IS_CAR_DOOR_CLOSED

**Flags:** unsupported

---

### `0416` LOAD_AND_LAUNCH_MISSION
Does nothing

**Flags:** nop

---

### `0419` GET_AMMO_IN_PLAYER_WEAPON

**Flags:** unsupported

---

### `041B` REGISTER_KILL_FRENZY_PASSED

**Flags:** unsupported

---

### `041C` SET_CHAR_SAY

**Flags:** unsupported

---

### `041F` OVERRIDE_HOSPITAL_LEVEL

**Flags:** unsupported

---

### `0420` OVERRIDE_POLICE_STATION_LEVEL

**Flags:** unsupported

---

### `0421` FORCE_RAIN

**Flags:** unsupported

---

### `0422` DOES_GARAGE_CONTAIN_CAR

**Flags:** unsupported

---

### `0426` MARK_ROADS_BETWEEN_LEVELS

**Flags:** unsupported

---

### `0427` MARK_PED_ROADS_BETWEEN_LEVELS

**Flags:** unsupported

---

### `0429` SET_CHAR_AVOID_LEVEL_TRANSITIONS

**Flags:** unsupported

---

### `042A` IS_THREAT_FOR_PED_TYPE

**Flags:** unsupported

---

### `042F` REGISTER_HIGHEST_SCORE

**Flags:** nop

---

### `0437` CREATE_SINGLE_PARTICLE

**Flags:** unsupported

---

### `0438` SET_CHAR_IGNORE_LEVEL_TRANSITIONS

**Flags:** unsupported

---

### `0439` GET_CHASE_CAR

**Flags:** unsupported

---

### `043A` START_BOAT_FOAM_ANIMATION

**Flags:** unsupported

---

### `043B` UPDATE_BOAT_FOAM_ANIMATION

**Flags:** unsupported

---

### `043D` SET_INTRO_IS_PLAYING

**Flags:** unsupported

---

### `043E` SET_PLAYER_HOOKER
Does nothing

**Flags:** nop

---

### `043F` PLAY_END_OF_GAME_TUNE
Plays the theme tune

**Flags:** nop

---

### `0440` STOP_END_OF_GAME_TUNE
Stops the theme tune

**Flags:** nop

---

### `0442` IS_PLAYER_SITTING_IN_CAR

**Flags:** unsupported

---

### `0443` IS_PLAYER_SITTING_IN_ANY_CAR

**Flags:** unsupported

---

### `0444` SET_SCRIPT_FIRE_AUDIO

**Flags:** unsupported

---

### `044A` IS_PLAYER_ON_FOOT

**Flags:** unsupported

---

### `044C` LOAD_COLLISION_WITH_SCREEN

**Flags:** unsupported

---

### `044D` LOAD_SPLASH_SCREEN
Loads the specified splash screen

**Flags:** nop

---

### `044E` SET_CAR_IGNORE_LEVEL_TRANSITIONS

**Flags:** unsupported

---

### `044F` MAKE_CRAIGS_CAR_A_BIT_STRONGER

**Flags:** unsupported

---

### `0450` SET_JAMES_CAR_ON_PATH_TO_PLAYER

**Flags:** nop

---

### `0451` LOAD_END_OF_GAME_TUNE
Loads the end of game music

**Flags:** nop

---

### `0452` ENABLE_PLAYER_CONTROL_CAMERA

**Flags:** unsupported

---

### `0455` GET_DEBUG_CAMERA_FRONT_VECTOR

**Flags:** unsupported

---

### `0456` IS_PLAYER_TARGETTING_ANY_CHAR

**Flags:** unsupported

---

### `0459` TERMINATE_ALL_SCRIPTS_WITH_THIS_NAME
Ends any script whose name (03A4) matches the given string


**Input:**
- `name: string`

**Details:**

This command stops the execution of all script s with this name. Scripts can be named through SCRIPT_NAME and more than one scripts can have the same name. Any upper case letters (A-Z) are converted to lower case by the game internally.

Calling this command to terminate custom CLEO scripts may cause undefined behavior and possible crashes. Use TERMINATE_ALL_CUSTOM_SCRIPTS_WITH_THIS_NAME instead.

---

### `045D` GET_CLOSEST_OBJECT_OF_TYPE
Does nothing

**Flags:** nop

---

### `045E` PLACE_OBJECT_RELATIVE_TO_OBJECT

**Flags:** unsupported

---

### `045F` SET_ALL_OCCUPANTS_OF_CAR_LEAVE_CAR

**Flags:** unsupported

---

### `0461` GET_CLOSEST_CAR_NODE_WITH_HEADING_TOWARDS_POINT

**Flags:** unsupported

---

### `0462` GET_CLOSEST_CAR_NODE_WITH_HEADING_AWAY_POINT

**Flags:** unsupported

---

### `0469` GET_RANDOM_COP_IN_AREA
Gets a random law enforcement ped of any of the specified types in the 2D area

**Flags:** nop

---

### `046A` GET_RANDOM_COP_IN_ZONE

**Flags:** unsupported

---

### `046B` SET_CHAR_OBJ_FLEE_CAR

**Flags:** unsupported

---

### `046F` GET_CURRENT_PLAYER_WEAPON

**Flags:** unsupported

---

### `0478` SET_CAR_HANDBRAKE_TURN_RIGHT

**Flags:** unsupported

---

### `0479` SET_CAR_HANDBRAKE_STOP

**Flags:** unsupported

---

### `047B` LOCATE_SNIPER_BULLET_2D

**Flags:** unsupported

---

### `047C` LOCATE_SNIPER_BULLET_3D

**Flags:** unsupported

---

### `047D` GET_NUMBER_OF_SEATS_IN_MODEL

**Flags:** unsupported

---

### `047E` IS_PLAYER_ON_ANY_BIKE

**Flags:** unsupported

---

### `047F` IS_CHAR_LYING_DOWN

**Flags:** unsupported

---

### `0481` SET_ENTER_CAR_RANGE_MULTIPLIER

**Flags:** nop

---

### `0482` SET_THREAT_REACTION_RANGE_MULTIPLIER
Does nothing

**Flags:** nop

---

### `0483` SET_CHAR_CEASE_ATTACK_TIMER

**Flags:** unsupported

---

### `0486` REPLAY

**Flags:** unsupported

---

### `0487` IS_REPLAY_PLAYING

**Flags:** unsupported

---

### `048D` GET_FIRST_PICKUP_COORDS

**Flags:** unsupported

---

### `048E` GET_NEXT_PICKUP_COORDS

**Flags:** unsupported

---

### `0490` HAS_PLAYER_GOT_WEAPON

**Flags:** unsupported

---

### `0492` IS_PLAYER_FACING_CHAR

**Flags:** unsupported

---

### `0493` SET_TANK_DETONATE_CARS

**Flags:** nop

---

### `0497` SET_CAR_DRIVE_STRAIGHT_AHEAD

**Flags:** unsupported

---

### `0498` SET_CAR_WAIT

**Flags:** unsupported

---

### `0499` IS_PLAYER_STANDING_ON_A_VEHICLE

**Flags:** unsupported

---

### `049A` IS_PLAYER_FOOT_DOWN

**Flags:** unsupported

---

### `049B` IS_CHAR_FOOT_DOWN

**Flags:** unsupported

---

### `049C` INITIALISE_OBJECT_PATH

**Flags:** nop

---

### `049D` START_OBJECT_ON_PATH

**Flags:** unsupported

---

### `049E` SET_OBJECT_PATH_SPEED
Does nothing

**Flags:** nop

---

### `049F` SET_OBJECT_PATH_POSITION
Does nothing

**Flags:** nop

---

### `04A0` GET_OBJECT_DISTANCE_ALONG_PATH

**Flags:** unsupported

---

### `04A1` CLEAR_OBJECT_PATH

**Flags:** nop

---

### `04A8` IS_PLAYER_IN_ANY_BOAT

**Flags:** unsupported

---

### `04AA` IS_PLAYER_IN_ANY_HELI

**Flags:** unsupported

---

### `04AC` IS_PLAYER_IN_ANY_PLANE

**Flags:** unsupported

---

### `04BC` SET_CUTSCENE_ANIM_TO_LOOP
Does nothing

**Flags:** nop

---

### `04BE` RESET_HAVOC_CAUSED_BY_PLAYER

**Flags:** nop

---

### `04BF` GET_HAVOC_CAUSED_BY_PLAYER
Does nothing

**Flags:** nop

---

### `04C2` SET_CHAR_OBJ_WALK_TO_CHAR

**Flags:** unsupported

---

### `04C3` IS_PICKUP_IN_ZONE

**Flags:** unsupported

---

### `04C6` SET_CHAR_OBJ_AIM_GUN_AT_CHAR

**Flags:** unsupported

---

### `04C7` SWITCH_SECURITY_CAMERA

**Flags:** nop

---

### `04C9` IS_PLAYER_IN_FLYING_VEHICLE

**Flags:** unsupported

---

### `04CA` HAS_SONY_CD_BEEN_READ

**Flags:** unsupported

---

### `04CB` GET_NUMBER_OF_SONY_CDS_READ

**Flags:** unsupported

---

### `04CC` ADD_SHORT_RANGE_BLIP_FOR_COORD_OLD

**Flags:** unsupported

---

### `04CD` ADD_SHORT_RANGE_BLIP_FOR_COORD

**Flags:** unsupported

---

### `04CF` ADD_MONEY_SPENT_ON_CLOTHES

**Flags:** unsupported

---

### `04D4` GET_NTH_CLOSEST_CHAR_NODE

**Flags:** unsupported

---

### `04DC` HAS_PHOTOGRAPH_BEEN_TAKEN

**Flags:** unsupported

---

### `04DE` SET_CHAR_ARMOUR

**Flags:** unsupported

---

### `04E2` SHUT_PLAYER_UP
Shuts the player up

**Flags:** nop

**Input:**
- `_p1: any`
- `_p2: any`

---

### `04E8` SET_CHAR_OBJ_STEAL_ANY_CAR_EVEN_MISSION_CAR

**Flags:** unsupported

---

### `04EC` SET_ZONE_CIVILIAN_CAR_INFO

**Flags:** unsupported

---

### `04F2` IS_OBJECT_WAITING_FOR_WORLD_COLLISION

**Flags:** unsupported

---

### `04F3` SET_CHAR_SHUFFLE_INTO_DRIVERS_SEAT

**Flags:** unsupported

---

### `04F5` SET_CHAR_AS_PLAYER_FRIEND

**Flags:** nop

---

### `04F6` DISPLAY_NTH_ONSCREEN_COUNTER

**Flags:** unsupported

---

### `04FB` CLOSE_CAR_BOOT

**Flags:** unsupported

---

### `04FD` DISARM_CHAR

**Flags:** unsupported

---

### `04FF` IS_CHAR_OBJ_NO_OBJ

**Flags:** unsupported

---

### `0502` SET_CHAR_OBJ_SPRINT_TO_COORD

**Flags:** unsupported

---

### `0504` SET_FIRST_PERSON_CONTROL_CAMERA

**Flags:** unsupported

---

### `0505` GET_NEAREST_TYRE_TO_POINT

**Flags:** unsupported

---

### `050B` POP_CAR_BOOT_USING_PHYSICS
Opens the trunk/boot door component of the vehicle

**Flags:** nop

---

### `050C` SET_FIRST_PERSON_WEAPON_CAMERA

**Flags:** unsupported

---

### `050D` IS_CHAR_LEAVING_VEHICLE_TO_DIE

**Flags:** unsupported

---

### `0510` IS_CHAR_WANDER_PATH_CLEAR

**Flags:** unsupported

---

### `0511` PRINT_HELP_WITH_NUMBER

**Flags:** unsupported

---

### `0514` SET_CHAR_CAN_BE_DAMAGED_BY_MEMBERS_OF_GANG

**Flags:** unsupported

---

### `0515` LOAD_AND_LAUNCH_MISSION_EXCLUSIVE
Does nothing

**Flags:** nop

---

### `0516` IS_MISSION_AUDIO_PLAYING

**Flags:** unsupported

---

### `0520` IS_CAR_DROWNING_IN_WATER

**Flags:** unsupported

---

### `0521` IS_CHAR_DROWNING_IN_WATER

**Flags:** nop

---

### `0522` DISABLE_CUTSCENE_SHADOWS
Does nothing

**Flags:** nop

---

### `0523` HAS_GLASS_BEEN_SHATTERED_NEARBY

**Flags:** nop

---

### `0524` ATTACH_CUTSCENE_OBJECT_TO_BONE
Does nothing

**Flags:** nop

---

### `0525` ATTACH_CUTSCENE_OBJECT_TO_COMPONENT

**Flags:** nop

---

### `0527` IS_MISSION_AUDIO_LOADING

**Flags:** unsupported

---

### `0528` ADD_MONEY_SPENT_ON_WEAPONS

**Flags:** unsupported

---

### `0529` ADD_MONEY_SPENT_ON_PROPERTY

**Flags:** unsupported

---

### `052A` ADD_MONEY_SPENT_ON_AUTO_PAINTING

**Flags:** unsupported

---

### `052B` SET_CHAR_ANSWERING_MOBILE

**Flags:** unsupported

---

### `052D` GET_PLAYER_DRUNKENNESS

**Flags:** unsupported

---

### `052E` SET_PLAYER_DRUG_LEVEL

**Flags:** unsupported

---

### `052F` GET_PLAYER_DRUG_LEVEL

**Flags:** unsupported

---

### `0530` ADD_LOAN_SHARK_VISITS

**Flags:** unsupported

---

### `0531` ADD_STORES_KNOCKED_OFF

**Flags:** unsupported

---

### `0532` ADD_MOVIE_STUNTS

**Flags:** unsupported

---

### `0533` ADD_NUMBER_OF_ASSASSINATIONS

**Flags:** unsupported

---

### `0534` ADD_PIZZAS_DELIVERED

**Flags:** unsupported

---

### `0535` ADD_GARBAGE_PICKUPS

**Flags:** unsupported

---

### `0536` ADD_ICE_CREAMS_SOLD

**Flags:** unsupported

---

### `0537` SET_TOP_SHOOTING_RANGE_SCORE

**Flags:** unsupported

---

### `0538` ADD_SHOOTING_RANGE_RANK

**Flags:** unsupported

---

### `0539` ADD_MONEY_SPENT_ON_GAMBLING

**Flags:** unsupported

---

### `053A` ADD_MONEY_WON_ON_GAMBLING

**Flags:** unsupported

---

### `053B` SET_LARGEST_GAMBLING_WIN

**Flags:** unsupported

---

### `053C` SET_CHAR_IN_PLAYERS_GROUP_CAN_FIGHT

**Flags:** unsupported

---

### `053D` CLEAR_CHAR_WAIT_STATE

**Flags:** unsupported

---

### `0540` SET_PLAYER_AUTO_AIM

**Flags:** nop

---

### `0542` SET_PROPERTY_AS_OWNED

**Flags:** unsupported

---

### `0543` ADD_BLOOD_RING_KILLS

**Flags:** unsupported

---

### `0544` SET_LONGEST_TIME_IN_BLOOD_RING

**Flags:** unsupported

---

### `0545` REMOVE_EVERYTHING_FOR_HUGE_CUTSCENE
Does nothing

**Flags:** nop

---

### `0546` IS_PLAYER_TOUCHING_VEHICLE

**Flags:** unsupported

---

### `0548` CHECK_FOR_PED_MODEL_AROUND_PLAYER
Does nothing

**Flags:** nop

---

### `0549` CLEAR_CHAR_FOLLOW_PATH

**Flags:** unsupported

---

### `054B` ATTACH_CUTSCENE_OBJECT_TO_VEHICLE
Does nothing

**Flags:** nop

---

### `054D` SET_TONIGHTS_EVENT
Sets whether to display a message at the stadium

**Flags:** nop

---

### `0551` SET_PLAYER_HAS_MET_DEBBIE_HARRY

**Flags:** nop

---

### `0552` SET_RIOT_INTENSITY

**Flags:** nop

---

### `0553` IS_CAR_IN_ANGLED_AREA_2D

**Flags:** unsupported

---

### `0554` IS_CAR_IN_ANGLED_AREA_3D

**Flags:** unsupported

---

### `0556` SET_UP_TAXI_SHORTCUT

**Flags:** nop

---

### `0557` CLEAR_TAXI_SHORTCUT

**Flags:** nop

---

### `0559` GET_CLOSEST_WATER_NODE

**Flags:** unsupported

---

### `055A` ADD_PORN_LEAFLET_TO_RUBBISH

**Flags:** unsupported

---

### `055B` CREATE_CLOTHES_PICKUP
Does nothing

**Flags:** nop

---

### `055C` CHANGE_BLIP_THRESHOLD

**Flags:** unsupported

---

### `0562` SET_CHAR_IGNORE_THREATS_BEHIND_OBJECTS

**Flags:** unsupported

---

### `0567` WAS_VEHICLE_EVER_POLICE

**Flags:** unsupported

---

### `0569` LOAD_UNCOMPRESSED_ANIM
Does nothing

**Flags:** nop

---

### `056B` SET_CHAR_CROUCH_WHEN_THREATENED

**Flags:** unsupported

---

### `056F` ADD_SHORT_RANGE_BLIP_FOR_CONTACT_POINT

**Flags:** unsupported

---

### `0571` IS_CHAR_STUCK

**Flags:** unsupported

---

### `0573` SET_CHAR_STOP_SHOOT_DONT_SEEK_ENTITY

**Flags:** unsupported

---

### `0576` FREEZE_OBJECT_POSITION_AND_DONT_LOAD_COLLISION

**Flags:** unsupported

---

### `0578` REGISTER_VIGILANTE_LEVEL

**Flags:** unsupported

---

### `0579` CLEAR_ALL_CHAR_ANIMS

**Flags:** unsupported

---

### `057A` SET_MAXIMUM_NUMBER_OF_CARS_IN_GARAGE

**Flags:** unsupported

---

### `057B` WANTED_STARS_ARE_FLASHING
Does nothing

**Flags:** nop

---

### `057C` SET_ALLOW_HURRICANES

**Flags:** unsupported

---

### `057D` PLAY_ANNOUNCEMENT
Plays an announcement audio

**Flags:** nop

---

### `057F` GET_BUS_FARES_COLLECTED_BY_PLAYER
Returns the number of coach passengers

**Flags:** nop

---

### `0580` SET_CHAR_OBJ_BUY_ICE_CREAM

**Flags:** unsupported

---

### `0584` CLEAR_CHAR_ICE_CREAM_PURCHASE

**Flags:** unsupported

---

### `0585` IS_IN_CAR_FIRE_BUTTON_PRESSED
Returns true if the attack button is being pressed

**Flags:** nop

---

### `0586` HAS_CHAR_ATTEMPTED_ATTRACTOR

**Flags:** unsupported

---

### `0589` SET_LOAD_COLLISION_FOR_OBJECT_FLAG

**Flags:** unsupported

---

### `058B` HAS_CHAR_BOUGHT_ICE_CREAM

**Flags:** unsupported

---

### `058D` SET_SHORTCUT_PICKUP_POINT
Does nothing

**Flags:** nop

---

### `058E` SET_SHORTCUT_DROPOFF_POINT_FOR_MISSION

**Flags:** nop

---

### `058F` GET_RANDOM_ICE_CREAM_CUSTOMER_IN_AREA

**Flags:** unsupported

---

### `0590` GET_RANDOM_ICE_CREAM_CUSTOMER_IN_ZONE

**Flags:** unsupported

---

### `0591` UNLOCK_ALL_CAR_DOORS_IN_AREA

**Flags:** nop

---

### `0592` SET_GANG_ATTACK_PLAYER_WITH_COPS

**Flags:** nop

---

### `0593` SET_CHAR_FRIGHTENED_IN_JACKED_CAR

**Flags:** unsupported

---

### `0596` IS_PLAYER_IN_SHORTCUT_TAXI

**Flags:** nop

**Input:**
- `_p1: any`

---

### `0598` CREATE_DUST_EFFECT_FOR_CUTSCENE_HELI

**Flags:** unsupported

---

### `0599` REGISTER_FIRE_LEVEL

**Flags:** unsupported

---

### `059B` DISARM_CAR_BOMB
Does nothing

**Flags:** nop

---

### `05AF` DO_2D_LINES_INTERSECT

**Flags:** unsupported

---

### `05B1` IS_2D_POINT_IN_TRIANGLE
Does nothing

**Flags:** nop

---

### `05B2` IS_2D_POINT_IN_RECTANGLE_ON_LEFT_SIDE_OF_LINE
Does nothing

**Flags:** nop

---

### `05B3` IS_2D_POINT_ON_LEFT_SIDE_OF_2D_LINE
Does nothing

**Flags:** nop

---

### `05B4` CHAR_LOOK_AT_OBJECT_ALWAYS

**Flags:** unsupported

---

### `05B5` APPLY_COLLISION_ON_OBJECT
Does nothing

**Flags:** nop

---

### `05B7` TASK_PLAYER_ON_FOOT
Does nothing

**Flags:** nop

---

### `05B8` TASK_PLAYER_IN_CAR
Does nothing

**Flags:** nop

---

### `05C6` TASK_DETONATE

**Flags:** nop

---

### `05CC` TASK_STEAL_CAR

**Flags:** nop

---

### `05CE` TASK_LEAVE_CAR_AND_DIE
Does nothing

**Flags:** nop

---

### `05D0` TASK_CAR_DRIVE
Does nothing

**Flags:** nop

---

### `05D5` SET_CHAR_IN_DISGUISE

**Flags:** nop

---

### `05DF` TASK_WANDER_COP

**Flags:** nop

---

### `05E0` TASK_WANDER_CRIMINAL
Reads the game memory and stores the result to a variable

**Flags:** nop

---

### `05E1` TASK_FOLLOW_LEADER_IN_FORMATION

**Flags:** nop

---

### `05E3` START_ADDING_STUNT_POINTS

**Flags:** nop

---

### `05E4` ADD_STUNT_POINT

**Flags:** nop

---

### `05E5` START_PLAYING_STUNT
Gets the ID version of the game

**Flags:** nop

---

### `05E6` HAS_STUNT_ENDED
Gets a pointer to the structure of the char on the handle

**Flags:** nop

---

### `05E7` HAS_STUNT_FAILED
Gets a pointer to the structure of the vehicle on the handle

**Flags:** nop

---

### `05E8` START_RECORDING_STUNT
Gets a pointer to the structure of the object on the handle

**Flags:** nop

---

### `05E9` START_RECORDING_CAR
Gets the handle to the char, which is located in the pool of actors

**Flags:** nop

**Input:**
- `_p1: any`
- `_p2: any`

---

### `05EA` STOP_RECORDING_CARS
Gets the handle of a vehicle located in a pool of vehicle

**Flags:** nop

---

### `05EF` SET_CAR_PROTECT_CAR_REAR
Performs a search for an char, which is located in a specified radius around the point

**Flags:** nop

---

### `05F0` SET_CAR_PROTECT_CAR_FRONT
Performs a search for a vehicle, located in a specified radius around the point

**Flags:** nop

---

### `0608` HAVE_PATH_NODES_BEEN_LOADED
Does nothing

**Flags:** nop

---

### `0609` LOAD_ALL_PATH_NODES_FOR_DEBUG
Does nothing

**Flags:** nop

---

### `060C` CLEAR_ALL_DECISION_MAKERS

**Flags:** nop

---

### `0610` SET_HEARING_RANGE
Does nothing

**Flags:** nop

---

### `0617` SCRIPT_EVENT
Does nothing

**Flags:** nop

---

### `061C` CLEAR_ALL_SEQUENCE_TASKS

**Flags:** nop

---

### `061F` CLEAR_ALL_ATTRACTORS
Does nothing

**Flags:** nop

---

### `0620` TASK_PLAY_ANIM_FOR_TIME
Does nothing

**Flags:** nop

---

### `062B` GET_ATTEMPTS_FOR_THIS_MISSION
Does nothing

**Flags:** nop

---

### `062C` REGISTER_THIS_MISSION_HAS_BEEN_ATTEMPTED
Does nothing

**Flags:** nop

---

### `062D` REGISTER_THIS_MISSION_HAS_BEEN_PASSED
Does nothing

**Flags:** nop

---

### `0636` TASK_SIDE_STEP_AND_SHOOT
Does nothing

**Flags:** nop

**Input:**
- `_p1: any`
- `_p2: any`
- `_p3: any`
- `_p4: any`
- `_p5: any`
- `_p6: any`
- `_p7: any`
- `_p8: any`
- `_p9: any`

---

### `063A` OPEN_THREAT_LIST

**Flags:** unsupported

---

### `063B` CLOSE_THREAT_LIST

**Flags:** unsupported

---

### `063C` SET_PEDMODEL_AS_THREAT

**Flags:** unsupported

---

### `063D` SET_CHAR_THREAT_LIST

**Flags:** unsupported

---

### `063E` REMOVE_THREAT_LIST

**Flags:** unsupported

---

### `063F` PERFORM_SEQUENCE_TASK_REPEATEDLY

**Flags:** unsupported

---

### `0640` SET_PEDTYPE_AS_THREAT

**Flags:** unsupported

---

### `0641` CLEAR_CHAR_THREATS

**Flags:** unsupported

---

### `0644` CREATE_PED_GENERATOR

**Flags:** unsupported

---

### `0645` SWITCH_PED_GENERATOR

**Flags:** unsupported

---

### `0649` SET_CHAR_ZONE_DISTANCE

**Flags:** unsupported

---

### `064A` ADD_PEDMODEL_AS_ATTRACTOR_USER
Does nothing

**Flags:** nop

---

### `064D` PAUSE_FX_SYSTEM
Does nothing

**Flags:** nop

---

### `0651` CREATE_FX_SYSTEM_WITH_DIRECTION
Does nothing

**Flags:** nop

---

### `0658` SET_GROUP_DEFAULT_LEADER_TASK

**Flags:** unsupported

---

### `0659` SET_ATTRACTOR_PAIR
Does nothing

**Flags:** nop

---

### `065A` PLACE_CHAR_AT_ATTRACTOR
Does nothing

**Flags:** nop

---

### `065D` VIEW_INTEGER_VARIABLE
Outputs an integer with a string

**Flags:** nop

**Input:**
- `_p1: any`
- `_p2: any`

---

### `065E` VIEW_FLOAT_VARIABLE
Outputs a float with a string

**Flags:** nop

**Input:**
- `_p1: any`
- `_p2: any`

---

### `065F` WATCH_INTEGER_VARIABLE
Does nothing

**Flags:** nop

**Input:**
- `_p1: any`
- `_p2: any`

---

### `0660` WATCH_FLOAT_VARIABLE
Does nothing

**Flags:** nop

**Input:**
- `_p1: any`
- `_p2: any`

---

### `0661` BREAKPOINT
Does nothing

**Flags:** nop

**Input:**
- `_p1: any`

---

### `0662` WRITE_DEBUG
Outputs debug text

**Flags:** nop

**Input:**
- `text: string`

---

### `0663` WRITE_DEBUG_WITH_INT
Outputs a string with an integer

**Flags:** nop

**Input:**
- `text: string`
- `number: int`

---

### `0664` WRITE_DEBUG_WITH_FLOAT
Does nothing

**Flags:** nop

**Input:**
- `text: string`
- `number: float`

---

### `0666` IS_CHAR_TOUCHING_ANY_OBJECT
Does nothing

**Flags:** nop

---

### `066F` ADD_QUEUED_DIALOGUE
Does nothing

**Flags:** nop

---

### `0670` IS_DIALOGUE_FINISHED
Does nothing

**Flags:** nop

---

### `0671` IS_DIALOGUE_PLAYING
Does nothing

**Flags:** nop

---

### `0675` CREATE_PED_GENERATOR_AT_ATTRACTOR
Does nothing

**Flags:** nop

---

### `0678` GET_CHAR_AT_SCRIPTED_ATTRACTOR
Does nothing

**Flags:** nop

---

### `068F` GET_CLOSEST_BUYABLE_OBJECT_TO_PLAYER
Does nothing

**Flags:** nop

---

### `0690` OPEN_FRIEND_LIST

**Flags:** unsupported

---

### `0691` CLOSE_FRIEND_LIST

**Flags:** unsupported

---

### `0692` REMOVE_FRIEND_LIST

**Flags:** unsupported

---

### `0693` SET_PEDMODEL_AS_FRIEND

**Flags:** unsupported

---

### `0694` SET_PEDTYPE_AS_FRIEND

**Flags:** unsupported

---

### `0695` CLEAR_CHAR_FRIENDS

**Flags:** unsupported

---

### `0696` SET_CHAR_FRIEND_LIST

**Flags:** unsupported

---

### `069C` ATTACH_CAMERA_TO_OBJECT
Does nothing

**Flags:** nop

---

### `069D` ATTACH_CAMERA_TO_OBJECT_LOOK_AT_VEHICLE
Does nothing

**Flags:** nop

---

### `069E` ATTACH_CAMERA_TO_OBJECT_LOOK_AT_CHAR
Does nothing

**Flags:** nop

---

### `069F` ATTACH_CAMERA_TO_OBJECT_LOOK_AT_OBJECT
Does nothing

**Flags:** nop

---

### `06A0` ATTACH_CAMERA_TO_CHAR_LOOK_AT_OBJECT
Does nothing

**Flags:** nop

---

### `06A1` ATTACH_CAMERA_TO_VEHICLE_LOOK_AT_OBJECT
Does nothing

**Flags:** nop

---

### `06A4` TASK_KILL_THREATS_ON_FOOT_WHILE_DUCKING
Does nothing

**Flags:** nop

---

### `06A6` TASK_PLAY_ANIM_WITH_VELOCITY_EXTRACTION
Does nothing

**Flags:** nop

---

### `06AA` IS_RECORDING_GOING_ON_FOR_CAR
Does nothing

**Flags:** nop

**Input:**
- `_p1: any`

---

### `06B8` SET_GROUP_DEFAULT_TASK

**Flags:** unsupported

---

### `06C6` TASK_OPEN_DRIVER_DOOR
Does nothing

**Flags:** nop

---

### `06CB` SET_VEHICLE_RECORDS_COLLISIONS
Does nothing

**Flags:** nop

---

### `06CC` DRAW_CROSS_IN_FRONT_OF_DEBUG_CAMERA

**Flags:** unsupported

---

### `06CD` DRAW_DEBUG_CUBE

**Flags:** unsupported

---

### `06CE` GET_CAR_LAST_ROUTE_COORDS
Does nothing

**Flags:** nop

---

### `06CF` DISPLAY_TIMER_BARS
Does nothing

**Flags:** nop

**Input:**
- `state: bool`

---

### `06F4` CREATE_SCRIPT_GANG_ROADBLOCK
Does nothing

**Flags:** nop

---

### `06F6` CLEAR_TWO_PLAYER_CAMERA_MODE
Does nothing

**Flags:** nop

---

### `06F7` SET_PLAYER_PASSENGER_CAN_SHOOT
Does nothing

**Flags:** nop

---

### `06F9` GET_HEIGHT_OF_CAR_WHEELS_FROM_GROUND
Does nothing

**Flags:** nop

---

### `06FB` SWITCH_PLAYER_CROSSHAIR
Does nothing

**Flags:** nop

---

### `06FE` GET_CAR_VALUE
Does nothing

**Flags:** nop

---

### `0700` SKIP_CUTSCENE_START
Does nothing

**Flags:** nop

---

### `0701` SKIP_CUTSCENE_END


---

### `0707` SKIP_CUTSCENE_START_INTERNAL
Enables skipping of the current scene


**Input:**
- `label`

---

### `0711` ALLOCATE_SCRIPT_TO_PED_GENERATOR
Does nothing

**Flags:** nop

---

### `0712` ALLOCATE_SCRIPT_TO_RANDOM_PED
Does nothing

**Flags:** nop

---

### `0718` SET_UP_CONVERSATION_NODE
Does nothing

**Flags:** nop

---

### `071B` CLEAR_ALL_CONVERSATIONS
Does nothing

**Flags:** nop

---

### `071C` GET_CHAR_LIGHTING
Does nothing

**Flags:** nop

---

### `071D` SET_CLOSEST_OBJECT_OF_TYPE_RENDER_SCORCHED
Does nothing

**Flags:** nop

---

### `0720` GET_VEHICLE_WHEEL_UPGRADE_CLASS
Does nothing

**Flags:** nop

---

### `0721` GET_NUM_WHEELS_IN_UPGRADE_CLASS
Does nothing

**Flags:** nop

---

### `0722` GET_WHEEL_IN_UPGRADE_CLASS
Does nothing

**Flags:** nop

---

### `0725` HELI_FLY_IN_DIRECTION
Does nothing

**Flags:** nop

---

### `0728` SET_UP_CONVERSATION_END_NODE
Does nothing

**Flags:** nop

---

### `0735` IS_PS2_KEYBOARD_KEY_PRESSED
Does nothing

**Flags:** nop

**Input:**
- `_p1: any`

---

### `0736` IS_PS2_KEYBOARD_KEY_JUST_PRESSED
Does nothing

**Flags:** nop

**Input:**
- `_p1: any`

---

### `0738` SET_ZONE_RADAR_COLOURS
Does nothing

**Flags:** nop

---

### `0739` GIVE_LOWRIDER_SUSPENSION_TO_CAR
Does nothing

**Flags:** nop

---

### `073A` DOES_CAR_HAVE_LOWRIDER_SUSPENSION
Does nothing

**Flags:** nop

---

### `073D` GET_RANDOM_CAR_IN_SPHERE
Does nothing

**Flags:** nop

---

### `0740` GET_COORDS_OF_CLOSEST_COLLECTABLE1
Does nothing

**Flags:** nop

---

### `0744` GET_STAT_CHANGE_AMOUNT
Does nothing

**Flags:** nop

---

### `0748` CLEAR_ALL_RELATIONSHIPS
Does nothing

**Flags:** nop

---

### `0752` STOP_RECORDING_CAR
Does nothing

**Flags:** nop

**Input:**
- `_p1: any`

---

### `0753` SET_ALERTNESS

**Flags:** unsupported

---

### `0756` TASK_GO_ON_PATROL

**Flags:** unsupported

---

### `0757` GET_PATROL_ALERTNESS

**Flags:** unsupported

---

### `0758` SET_CHAR_SPECIAL_EVENT
Does nothing

**Flags:** nop

---

### `0759` SET_ATTRACTOR_AS_COVER_NODE
Does nothing

**Flags:** nop

---

### `0764` IS_SEARCHLIGHT_IN_ANGLED_AREA_2D
Does nothing

**Flags:** nop

---

### `0765` IS_SEARCHLIGHT_IN_ANGLED_AREA_3D
Does nothing

**Flags:** nop

---

### `0766` SWITCH_SEARCHLIGHT_BULB
Does nothing

**Flags:** nop

---

### `0768` SET_ZONE_GANG_CAP

**Flags:** unsupported

---

### `0769` GET_ZONE_GANG_CAP

**Flags:** unsupported

---

### `076E` SET_NO_POLICE_DURING_LA_RIOTS
Does nothing

**Flags:** nop

---

### `0773` CLEAR_HELP_WITH_THIS_LABEL

**Flags:** nop

---

### `0774` IS_SEARCHLIGHT_BULB_ON
Does nothing

**Flags:** nop

---

### `0775` CREATE_OIL_PUDDLE
Does nothing

**Flags:** nop

---

### `0779` TASK_OPEN_PASSENGER_DOOR
Does nothing

**Flags:** nop

---

### `077F` ADD_INT_TO_VAR_CONSOLE
Does nothing

**Flags:** nop

---

### `0785` GIVE_PLAYER_TATTOO
Does nothing

**Flags:** nop

---

### `0787` SET_CHAR_TYRES_CAN_BE_BURST
Does nothing

**Flags:** nop

---

### `078D` ADD_FLOAT_TO_VAR_CONSOLE
Does nothing

**Flags:** nop

---

### `078E` TASK_DRAG_CHAR_FROM_CAR
Does nothing

**Flags:** nop

---

### `0791` BUY_TATTOO
Does nothing

**Flags:** nop

---

### `0795` DELETE_WINCH_FOR_HELI
Does nothing

**Flags:** nop

---

### `079A` ATTACH_CAR_TO_ROPE_FOR_OBJECT
Does nothing

**Flags:** nop

---

### `079B` ATTACH_CHAR_TO_ROPE_FOR_OBJECT
Does nothing

**Flags:** nop

---

### `079C` ATTACH_OBJECT_TO_ROPE_FOR_OBJECT
Does nothing

**Flags:** nop

---

### `07A2` SET_NEXT_EVENT_RESPONSE_SEQUENCE
Does nothing

**Flags:** nop

---

### `07AA` GET_SEARCHLIGHT_COORDS
Does nothing

**Flags:** nop

---

### `07AD` GET_TRAILER_ATTACHED_TO_CAB
Does nothing

**Flags:** nop

---

### `07AE` GET_CAB_ATTACHED_TO_TRAILER
Does nothing

**Flags:** nop

---

### `07B2` SET_BEAT_ZONE_SIZE
Does nothing

**Flags:** nop

---

### `07B5` DISPLAY_TWO_ONSCREEN_COUNTERS
Does nothing

**Flags:** nop

---

### `07B7` DISPLAY_NTH_TWO_ONSCREEN_COUNTERS
Does nothing

**Flags:** nop

---

### `07B9` TASK_KILL_CHAR_ON_FOOT_PATROL

**Flags:** unsupported

---

### `07BA` HELI_AIM_AHEAD_OF_TARGET_ENTITY
Does nothing

**Flags:** nop

---

### `07C2` DISPLAY_PLAYBACK_RECORDED_CAR
Does nothing

**Flags:** nop

---

### `07C8` DISPLAY_DEBUG_MESSAGE
Does nothing

**Flags:** nop

---

### `07CA` TASK_SIMPLE_PUTDOWN_OBJECT
Does nothing

**Flags:** nop

---

### `07CE` SET_BULLET_WHIZZ_BY_DISTANCE
Does nothing

**Flags:** nop

---

### `07CF` SET_TWO_PLAYER_CAM_MODE_SEPARATE_CARS
Does nothing

**Flags:** nop

---

### `07D1` SET_CURRENT_DAY_OF_WEEK
Does nothing

**Flags:** nop

---

### `07D2` ACTIVATE_INTERIORS
Does nothing

**Flags:** nop

---

### `07D4` REGISTER_OBJECT_SCRIPT_BRAIN_FOR_CODE_USE
Does nothing

**Flags:** nop

---

### `07DC` GET_CAR_ROTATION_VELOCITY
Does nothing

**Flags:** nop

---

### `07E2` TASK_GO_STRAIGHT_TO_COORD_WITHOUT_STOPPING
Does nothing

**Flags:** nop

---

### `07E3` GET_BEAT_INFO_FOR_CURRENT_TRACK
Does nothing

**Flags:** nop

---

### `07E9` HAS_CHAR_SPOTTED_CAR
Does nothing

**Flags:** nop

---

### `07EA` SET_ROPE_HEIGHT_FOR_HELI
Does nothing

**Flags:** nop

---

### `07EB` GET_ROPE_HEIGHT_FOR_HELI
Does nothing

**Flags:** nop

---

### `07EC` IS_CAR_LOWRIDER
Does nothing

**Flags:** nop

---

### `07ED` IS_PERFORMANCE_CAR
Does nothing

**Flags:** nop

---

### `07F4` SET_ONSCREEN_TIMER_DISPLAY
Does nothing

**Flags:** nop

---

### `0802` SET_GLOBAL_PED_SEARCH_PARAMS

**Flags:** unsupported

---

### `0805` ALLOCATE_SCRIPT_TO_OBJECT
Does nothing

**Flags:** nop

---

### `0807` SET_TWO_PLAYER_CAM_MODE_SAME_CAR_SHOOTING
Does nothing

**Flags:** nop

---

### `0808` SET_TWO_PLAYER_CAM_MODE_SAME_CAR_NO_SHOOTING
Does nothing

**Flags:** nop

---

### `0809` SET_TWO_PLAYER_CAM_MODE_NOT_BOTH_IN_CAR
Does nothing

**Flags:** nop

---

### `080C` GET_CHAR_BREATH
Does nothing

**Flags:** nop

---

### `080D` SET_CHAR_BREATH
Does nothing

**Flags:** nop

---

### `080F` ARE_PATHS_LOADED_FOR_CAR
Does nothing

**Flags:** nop

---

### `0813` FORCE_NEXT_DIE_ANIM
Does nothing

**Flags:** nop

---

### `081B` ARE_PATHS_LOADED_IN_AREA
Does nothing

**Flags:** nop

---

### `0821` IS_3D_COORD_IN_ZONE
Does nothing

**Flags:** nop

---

### `0824` GET_CLOSEST_PICKUP_COORDS_TO_COORD
Does nothing

**Flags:** nop

---

### `082B` FIND_NEAREST_MULTIBUILDING

**Flags:** unsupported

---

### `082C` SET_MULTIBUILDING_MODEL

**Flags:** unsupported

---

### `082D` GET_NUMBER_MULTIBUILDING_MODELS

**Flags:** unsupported

---

### `082E` GET_MULTIBUILDING_MODEL_INDEX

**Flags:** unsupported

---

### `082F` SET_CURRENT_BUYABLE_PROPERTY

**Flags:** unsupported

---

### `0831` IS_AUDIO_BUILD
Does nothing

**Flags:** nop

---

### `0832` CLEAR_QUEUED_DIALOGUE
Does nothing

**Flags:** nop

---

### `0838` SET_OBJECT_ANIM_PLAYING_FLAG
Does nothing

**Flags:** nop

---

### `083B` GET_OBJECT_ANIM_TOTAL_TIME
Does nothing

**Flags:** nop

---

### `0848` SWITCH

**Flags:** unsupported

---

### `0849` ENDSWITCH

**Flags:** unsupported

---

### `084A` CASE

**Flags:** unsupported

---

### `084B` DEFAULT

**Flags:** unsupported

---

### `084C` BREAK

**Flags:** unsupported

---

### `084F` GET_GROUP_LEADER
Does nothing

**Flags:** nop

---

### `0854` BLOCK_NODES_IN_AREA

**Flags:** unsupported

---

### `0857` SET_WATER_CONFIGURATION
Does nothing

**Flags:** nop

---

### `085C` TASK_USE_ATTRACTOR_ADVANCED
Does nothing

**Flags:** nop

---

### `085D` TASK_FOLLOW_PATH_NODES_TO_COORD_SHOOTING
Does nothing

**Flags:** nop

---

### `085F` START_PLAYBACK_RECORDED_CAR_USING_AI_LOOPED
Does nothing

**Flags:** nop

---

### `0862` GET_MODEL_NAME_FOR_DEBUG_ONLY
Does nothing

**Flags:** nop

---

### `0863` TASK_USE_NEARBY_ENTRY_EXIT
Does nothing

**Flags:** nop

---

### `0865` FREEZE_STATE_OF_INTERIORS

**Flags:** unsupported

---

### `0868` CLEAR_THIS_VIEW_INTEGER_VARIABLE
Does nothing

**Flags:** nop

**Input:**
- `_p1: any`

---

### `0869` CLEAR_THIS_VIEW_FLOAT_VARIABLE
Does nothing

**Flags:** nop

**Input:**
- `_p1: any`

---

### `086A` CLEAR_ALL_VIEW_VARIABLES
Does nothing

**Flags:** nop

---

### `086D` CLEAR_ALL_BREAKPOINTS
Does nothing

**Flags:** nop

---

### `086E` CLEAR_ALL_WATCHPOINTS
Does nothing

**Flags:** nop

---

### `086F` IS_THIS_MODEL_A_TRAIN
Does nothing

**Flags:** nop

---

### `0870` GET_VEHICLE_CHAR_IS_STANDING_ON
Does nothing

**Flags:** nop

---

### `0871` SWITCH_START
Takes an input value and uses it to determine which label to go to in the code


**Input:**
- `caseId: int`
- `numCases: int`
- `hasDefaultCase: bool`
- `defaultLabel: label`
- `caseNum1: int`
- `caseLabel1: label`
- `caseNum2: int`
- `caseLabel2: label`
- `caseNum3: int`
- `caseLabel3: label`
- `caseNum4: int`
- `caseLabel4: label`
- `caseNum5: int`
- `caseLabel5: label`
- `caseNum6: int`
- `caseLabel6: label`
- `caseNum7: int`
- `caseLabel7: label`

---

### `0872` SWITCH_CONTINUED
Accompanies 0871, increasing the number of possible cases (max 75)


**Input:**
- `caseNum1: int`
- `caseLabel1: label`
- `caseNum2: int`
- `caseLabel2: label`
- `caseNum3: int`
- `caseLabel3: label`
- `caseNum4: int`
- `caseLabel4: label`
- `caseNum5: int`
- `caseLabel5: label`
- `caseNum6: int`
- `caseLabel6: label`
- `caseNum7: int`
- `caseLabel7: label`
- `caseNum8: int`
- `caseLabel8: label`
- `caseNum9: int`
- `caseLabel9: label`

---

### `0877` GET_VEHICLE_DIRT_LEVEL
Does nothing

**Flags:** nop

---

### `0880` DRAW_RECT_WITH_TITLE
Does nothing

**Flags:** nop

---

### `0882` SET_ATTRACTOR_RADIUS
Does nothing

**Flags:** nop

---

### `0885` CONST_INT
Does nothing

**Flags:** nop

---

### `0886` CONST_FLOAT
Does nothing

**Flags:** nop

---

### `088F` SET_TIME_ONE_DAY_BACK
Does nothing

**Flags:** nop

---

### `0891` TASK_SIT_IN_RESTAURANT
Does nothing

**Flags:** nop

---

### `0892` GET_RANDOM_ATTRACTOR_ON_CLOSEST_OBJECT_OF_TYPE
Does nothing

**Flags:** nop

---

### `0894` ADD_INTERESTING_ENTITY_FOR_CHAR
Does nothing

**Flags:** nop

---

### `0895` CLEAR_INTERESTING_ENTITIES_FOR_CHAR
Does nothing

**Flags:** nop

---

### `0896` GET_CLOSEST_ATTRACTOR
Does nothing

**Flags:** nop

---

### `0899` ALLOCATE_SCRIPT_TO_ATTRACTOR
Does nothing

**Flags:** nop

---

### `089A` GET_CLOSEST_ATTRACTOR_WITH_THIS_SCRIPT
Does nothing

**Flags:** nop

---

### `089D` GET_CONVERSATION_STATUS
Does nothing

**Flags:** nop

---

### `08A1` GET_CHAR_MAP_ATTRACTOR_STATUS
Does nothing

**Flags:** nop

---

### `08AA` STREAM_SCRIPT_INTERNAL
Does nothing

**Flags:** nop

---

### `08B0` SET_CAR_PITCH
Does nothing

**Flags:** nop

---

### `08CC` PICK_UP_OBJECT_WITH_WINCH
Does nothing

**Flags:** nop

---

### `08CD` PICK_UP_VEHICLE_WITH_WINCH
Does nothing

**Flags:** nop

---

### `08CE` PICK_UP_CHAR_WITH_WINCH
Does nothing

**Flags:** nop

---

### `08CF` STORE_CAR_IN_NEAREST_IMPOUNDING_GARAGE
Does nothing

**Flags:** nop

---

### `08D5` CONSTANT_INT
Does nothing

**Flags:** nop

---

### `08FC` GET_MENU_POSITION
Does nothing

**Flags:** nop

---

### `0902` SET_OBJECT_BEEN_PHOTOGRAPHED_FLAG
Does nothing

**Flags:** nop

---

### `0903` SET_CHAR_BEEN_PHOTOGRAPHED_FLAG
Does nothing

**Flags:** nop

---

### `090A` IS_PLAYBACK_FOR_CAR_PAUSED
Does nothing

**Flags:** nop

---

### `090B` TRIGGER_PED_BOUNCE
Does nothing

**Flags:** nop

---

### `0911` REGISTER_STREAMED_SCRIPT
Does nothing

**Flags:** nop

---

### `0914` REGISTER_STREAMED_SCRIPT_INTERNAL
Does nothing

**Flags:** nop

**Input:**
- `_p1: any`

---

### `091A` GET_LATEST_CONSOLE_COMMAND
Does nothing

**Flags:** nop

**Output:**
- `_p1: any (variable)`

---

### `091B` RESET_LATEST_CONSOLE_COMMAND
Does nothing

**Flags:** nop

---

### `0921` CAMERA_SET_SHAKE_SIMULATION
Does nothing

**Flags:** nop

---

### `0927` ALLOCATE_STREAMED_SCRIPT_TO_PED_GENERATOR
Does nothing

**Flags:** nop

---

### `092A` SET_PLAYER_CAN_BE_DAMAGED
Does nothing

**Flags:** nop

---

### `092C` GET_PLAYERS_GANG_IN_CAR_ACTIVE
Does nothing

**Flags:** nop

---

### `092D` SET_PLAYERS_GANG_IN_CAR_ACTIVE
Does nothing

**Flags:** nop

---

### `0932` CAMERA_IS_FOV_RUNNING
Does nothing

**Flags:** nop

---

### `0935` CAMERA_IS_SHAKE_RUNNING
Does nothing

**Flags:** nop

---

### `0938` CLEAR_ALL_QUEUED_DIALOGUE
Does nothing

**Flags:** nop

---

### `093C` SET_ONSCREEN_COUNTER_COLOUR
Does nothing

**Flags:** nop

---

### `093E` SET_CHAR_FIRE_DAMAGE_MULTIPLIER
Does nothing

**Flags:** nop

**Input:**
- `_p1: any`
- `_p2: any`

---

### `093F` IS_FIRE_BUTTON_PRESSED
Does nothing

**Flags:** nop

---

### `0943` SET_CAMERA_BEHIND_CHAR
Does nothing

**Flags:** nop

---

### `0962` DOES_CAR_HAVE_ROOF
Does nothing

**Flags:** nop

---

### `0963` SET_BLIP_FADE
Does nothing

**Flags:** nop

---

### `0979` LOAD_SHARED_CHAR_DECISION_MAKER
Does nothing

**Flags:** nop

---

### `097E` IS_POLICE_VEHICLE_IN_PURSUIT
Does nothing

**Flags:** nop

---

### `097F` GET_CAR_COLOUR_FROM_MENU_INDEX
Does nothing

**Flags:** nop

---

### `098F` RADIANS_TO_DEGREES
Does nothing

**Flags:** nop

---

### `0990` DEGREES_TO_RADIANS
Does nothing

**Flags:** nop

---

### `0993` SET_CHAR_AIR_RESISTANCE_MULTIPLIER
Does nothing

**Flags:** nop

---

### `0999` SET_PLAYER_FIRE_WITH_SHOULDER_BUTTON
Does nothing

**Flags:** nop

---

### `09A5` SET_CCTV_EFFECT
Does nothing

**Flags:** nop

---

### `09B1` GET_CPU_LEVEL
Does nothing

**Flags:** nop

---

### `09C6` SET_ALL_CARS_IN_AREA_VISIBLE
Does nothing

**Flags:** nop

---

### `09CD` IS_ITALIAN_GAME

**Flags:** unsupported

---

### `09CE` IS_SPANISH_GAME

**Flags:** unsupported

---

### `09D3` IS_AMBIENT_CRIME_ENABLED
Does nothing

**Flags:** nop

---

### `09D8` DISABLE_2ND_PAD_FOR_DEBUG
Does nothing

**Flags:** nop

**Input:**
- `_p1: any`

---

### `09DC` SET_CHAR_CAN_CLIMB_OUT_WATER
Does nothing

**Flags:** nop

---

### `09DF` RESTORE_PLAYER_AFTER_2P_GAME

**Flags:** unsupported

---

### `09EA` PLAYER_PUT_ON_GOGGLES
Does nothing

**Flags:** nop

---

### `09F3` GET_RANDOM_TRAIN_IN_SPHERE_NO_SAVE
Does nothing

**Flags:** nop

---

### `09F9` SET_MENU_HEADER_ORIENTATION
Does nothing

**Flags:** nop

---

### `0A00` IS_THIS_MODEL_A_BIKE
Does nothing

**Flags:** nop

---

### `0A04` SET_VEHICLE_FIRING_RATE_MULTIPLIER
Does nothing

**Flags:** nop

---

### `0A05` GET_VEHICLE_FIRING_RATE_MULTIPLIER
Does nothing

**Flags:** nop

---

### `0A0D` BLOCK_VEHICLE_MODEL
Does nothing

**Flags:** nop

---

### `0A34` SET_UP_SKIP_TO_BE_FINISHED_BY_SCRIPT
Does nothing

**Flags:** nop

---

### `0A38` SET_RENDER_PLAYER_WEAPON
Does nothing

**Flags:** nop

---

### `0A42` REMOVE_ALLUSER_3D_MARKERS
Does nothing

**Flags:** nop

---

### `0A49` IS_XBOX_VERSION
Returns true for Xbox versions of the game

**Flags:** condition

---

### `0A4D` IS_JAPANESE_VERSION
Returns true for Japanese versions of the game

**Flags:** condition

---

### `0A4E` DO_DEBUG_STUFF
Increments an unused counter, likely used in the debug version of the game


---

## String Operations

### `0346` SET_TEXT_BACKGROUND_COLOUR

**Flags:** unsupported

---

### `0347` SET_TEXT_BACKGROUND_ONLY_TEXT

**Flags:** unsupported

---

### `0375` PRINT_STRING_IN_STRING

**Flags:** unsupported

---

### `0385` PRINT_STRING_IN_STRING_SOON

**Flags:** unsupported

---

### `051F` DISPLAY_TEXT_WITH_3_NUMBERS

**Flags:** unsupported

---

### `05AB` VAR_TEXT_LABEL

**Flags:** unsupported

---

### `05AC` LVAR_TEXT_LABEL

**Flags:** unsupported

---

### `06D3` VAR_TEXT_LABEL16

**Flags:** unsupported

---

### `06D4` LVAR_TEXT_LABEL16

**Flags:** unsupported

---

### `07B6` DISPLAY_TWO_ONSCREEN_COUNTERS_WITH_STRING
Does nothing

**Flags:** nop

---

### `07B8` DISPLAY_NTH_TWO_ONSCREEN_COUNTERS_WITH_STRING
Does nothing

**Flags:** nop

---

### `080B` SAVE_TEXT_LABEL_TO_DEBUG_FILE
Does nothing

**Flags:** nop

**Input:**
- `_p1: any`

---

### `08AE` DRAW_WINDOW_TEXT
Does nothing

**Flags:** nop

---

### `098B` STRING_CAT16
Combines two null-terminated strings and stores the result to a string variable. The final string can not exceed 16 characters

**Operator:** `+`

**Input:**
- `str1: string (variable)`
- `str2: string (variable)`

**Output:**
- `result: string (variable)`

---

### `098C` STRING_CAT8
Combines two null-terminated strings and stores the result to a string variable. The final string can not exceed 8 characters

**Operator:** `+`

**Input:**
- `str1: string (variable)`
- `str2: string (variable)`

**Output:**
- `result: string (variable)`

---

## Variable Operations

### `0004` SET_VAR_INT
Sets the integer value of the VAR

**Operator:** `=`

**Input:**
- `int (global var)`
- `int (literal)`

---

### `0005` SET_VAR_FLOAT
Sets the float value of the VAR

**Operator:** `=`

**Input:**
- `float (global var)`
- `float (literal)`

---

### `0006` SET_LVAR_INT
Sets the integer value of the LVAR

**Operator:** `=`

**Input:**
- `int (local var)`
- `int (literal)`

---

### `0007` SET_LVAR_FLOAT
Sets the float value of the LVAR

**Operator:** `=`

**Input:**
- `float (local var)`
- `float (literal)`

---

### `0008` ADD_VAL_TO_INT_VAR
Adds the value to the value of the int VAR

**Operator:** `+`

**Input:**
- `int (global var)`
- `int (literal)`

---

### `0009` ADD_VAL_TO_FLOAT_VAR
Adds the value to the value of the float VAR

**Operator:** `+`

**Input:**
- `float (global var)`
- `float (literal)`

---

### `000A` ADD_VAL_TO_INT_LVAR
Adds the value to the value of the integer LVAR

**Operator:** `+`

**Input:**
- `int (local var)`
- `int (literal)`

---

### `000B` ADD_VAL_TO_FLOAT_LVAR
Adds the value to the value of the float LVAR

**Operator:** `+`

**Input:**
- `float (local var)`
- `float (literal)`

---

### `000C` SUB_VAL_FROM_INT_VAR
Subtracts the value from the value of the integer VAR

**Operator:** `-`

**Input:**
- `int (global var)`
- `int (literal)`

---

### `000D` SUB_VAL_FROM_FLOAT_VAR
Subtracts the value from the value of the float VAR

**Operator:** `-`

**Input:**
- `float (global var)`
- `float (literal)`

---

### `000E` SUB_VAL_FROM_INT_LVAR
Subtracts the value from the value of the int LVAR

**Operator:** `-`

**Input:**
- `int (local var)`
- `int (literal)`

---

### `000F` SUB_VAL_FROM_FLOAT_LVAR
Subtracts the value from the value of the float LVAR

**Operator:** `-`

**Input:**
- `float (local var)`
- `float (literal)`

---

### `0084` SET_VAR_INT_TO_VAR_INT
Sets the int VAR to the VAR value

**Operator:** `=`

**Input:**
- `int (global var)`
- `int (global var)`

---

### `0085` SET_LVAR_INT_TO_LVAR_INT
Sets the int LVAR to the LVAR value

**Operator:** `=`

**Input:**
- `int (local var)`
- `int (local var)`

---

### `0086` SET_VAR_FLOAT_TO_VAR_FLOAT
Sets the float VAR to the VAR value

**Operator:** `=`

**Input:**
- `float (global var)`
- `float (global var)`

---

### `0087` SET_LVAR_FLOAT_TO_LVAR_FLOAT
Sets the float LVAR to the LVAR value

**Operator:** `=`

**Input:**
- `float (local var)`
- `float (local var)`

---

### `0088` SET_VAR_FLOAT_TO_LVAR_FLOAT
Sets the float VAR to the LVAR value

**Operator:** `=`

**Input:**
- `float (global var)`
- `float (local var)`

---

### `0089` SET_LVAR_FLOAT_TO_VAR_FLOAT
Sets the float LVAR to the VAR value

**Operator:** `=`

**Input:**
- `float (local var)`
- `float (global var)`

---

### `008A` SET_VAR_INT_TO_LVAR_INT
Sets the int VAR to the LVAR value

**Operator:** `=`

**Input:**
- `int (global var)`
- `int (local var)`

---

### `008B` SET_LVAR_INT_TO_VAR_INT
Sets the int LVAR to the VAR value

**Operator:** `=`

**Input:**
- `int (local var)`
- `int (global var)`

---

### `008C` CSET_VAR_INT_TO_VAR_FLOAT
Converts the float in the second global variable to an integer (via flooring) and stores the integer into the first global variable

**Operator:** `=#`

**Input:**
- `int (global var)`
- `float (global var)`

---

### `008D` CSET_VAR_FLOAT_TO_VAR_INT
Converts the integer value of the second global variable to a float and stores the result in the first global variable

**Operator:** `=#`

**Input:**
- `float (global var)`
- `int (global var)`

---

### `008E` CSET_LVAR_INT_TO_VAR_FLOAT
Converts the float value of the global variable to an integer (via flooring) and stores the result into a local variable

**Operator:** `=#`

**Input:**
- `int (local var)`
- `float (global var)`

---

### `008F` CSET_LVAR_FLOAT_TO_VAR_INT
Converts the integer value of the global variable to a float and then stores the result in the local variable

**Operator:** `=#`

**Input:**
- `float (local var)`
- `int (global var)`

---

### `0090` CSET_VAR_INT_TO_LVAR_FLOAT
Converts the float value of the local variable to an integer (via flooring) and stores the result to the global variable

**Operator:** `=#`

**Input:**
- `int (global var)`
- `float (local var)`

---

### `0091` CSET_VAR_FLOAT_TO_LVAR_INT
Converts the integer value of the local variable to a float and stores the result in the global variable

**Operator:** `=#`

**Input:**
- `float (global var)`
- `int (local var)`

---

### `0092` CSET_LVAR_INT_TO_LVAR_FLOAT
Converts a float value to an integer (via truncating)

**Operator:** `=#`

**Input:**
- `int (local var)`
- `float (local var)`

---

### `0093` CSET_LVAR_FLOAT_TO_LVAR_INT
Converts the integer value of the second local variable to a float and stores the result to the first local variable

**Operator:** `=#`

**Input:**
- `float (local var)`
- `int (local var)`

---

### `04AE` SET_VAR_INT_TO_CONSTANT
Assigns the global variable to the integer constant

**Operator:** `=`

**Input:**
- `int (global var)`
- `int (literal)`

---

### `04AF` SET_LVAR_INT_TO_CONSTANT
Assigns the local variable to the integer constant

**Operator:** `=`

**Input:**
- `int (local var)`
- `int (literal)`

---

### `05A9` SET_VAR_TEXT_LABEL
Copies up to 8 characters from src to dest

**Operator:** `=`

**Input:**
- `dest: string (global var)`
- `src: string`

---

### `05AA` SET_LVAR_TEXT_LABEL
Copies up to 8 characters from src to dest

**Operator:** `=`

**Input:**
- `dest: string (local var)`
- `src: string`

---

### `06D1` SET_VAR_TEXT_LABEL16
Copies up to 16 characters from src to dest

**Operator:** `=`

**Input:**
- `dest: string (global var)`
- `src: string`

---

### `06D2` SET_LVAR_TEXT_LABEL16
Copies up to 16 characters from src to dest

**Operator:** `=`

**Input:**
- `dest: string (local var)`
- `src: string`

---
