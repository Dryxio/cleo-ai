# CLEO Extension Opcodes

> 92 opcodes

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0A8C` | WRITE_MEMORY | Writes the value at the memory address |
| `0A8D` | READ_MEMORY | Reads a value from the game memory |
| `0A8E` | INT_ADD | Adds together two integer values and writes the result into the variable |
| `0A8F` | INT_SUB | Subtracts the integer value from another integer value and writes the result int |
| `0A90` | INT_MUL | Multiplies two integer values and writes the result into the variable |
| `0A91` | INT_DIV | Divides the integer value by another integer value and writes the result into th |
| `0A92` | STREAM_CUSTOM_SCRIPT | Loads a file with compiled SCM instructions at the given path and runs a new cus |
| `0A93` | TERMINATE_THIS_CUSTOM_SCRIPT | Ends the current custom script, preventing further execution |
| `0A94` | LOAD_AND_LAUNCH_CUSTOM_MISSION |  |
| `0A95` | SAVE_THIS_CUSTOM_SCRIPT | Marks this script to be saved whenever game is saved. After savegame load all lo |
| `0A96` | GET_PED_POINTER | Gets the address of the ped struct in the game memory by its handle |
| `0A97` | GET_VEHICLE_POINTER | Gets the address of the vehicle struct in the game memory by its handle |
| `0A98` | GET_OBJECT_POINTER | Gets the address of the object struct in the game memory by its handle |
| `0A99` | SET_CURRENT_DIRECTORY | Sets the current working directory (cwd) to a predefined location with a value o |
| `0A9A` | OPEN_FILE | Opens the file in the specified mode, sets the condition result to True if the o |
| `0A9B` | CLOSE_FILE | Closes the file and frees the memory |
| `0A9C` | GET_FILE_SIZE | Gets the file size in bytes |
| `0A9D` | READ_FROM_FILE | Reads the specified number of bytes from the opened file and writes them to the  |
| `0A9E` | WRITE_TO_FILE | Copies the specified number of bytes of the memory region starting from the addr |
| `0A9F` | GET_THIS_SCRIPT_STRUCT | Gets the address of the current script structure in the game memory |
| `0AA0` | GOSUB_IF_FALSE | Transfers the script execution to the label as a subroutine if the result of the |
| `0AA1` | RETURN_IF_FALSE | Returns from the current subroutine if the result of the condition is false |
| `0AA2` | LOAD_DYNAMIC_LIBRARY | Loads the specified module (usually a dynamic-link library (DLL)) into the addre |
| `0AA3` | FREE_DYNAMIC_LIBRARY | Frees the loaded dynamic-link library (DLL) module and unloads it from the addre |
| `0AA4` | GET_DYNAMIC_LIBRARY_PROCEDURE | Retrieves the address of an exported function or variable from the specified dyn |
| `0AA5` | CALL_FUNCTION | Calls a function at the address with the given arguments and the calling convent |
| `0AA6` | CALL_METHOD | Calls a method of the object (struct) with the given arguments and the 'thiscall |
| `0AA7` | CALL_FUNCTION_RETURN | Calls a function similarly to 0AA5 and writes the result into the variable follo |
| `0AA8` | CALL_METHOD_RETURN | Calls a method of the object (struct) similarly to 0AA6 and writes the result in |
| `0AA9` | IS_GAME_VERSION_ORIGINAL | Returns true if the game version is vanilla 1.0 |
| `0AAA` | GET_SCRIPT_STRUCT_NAMED | Gets the address of a running script which name matches the given string or 0 ot |
| `0AAB` | DOES_FILE_EXIST | Returns true if a file at the given path exists |
| `0AB0` | IS_KEY_PRESSED | Returns true if the player is pressing a keyboard button with the specified code |
| `0AB1` | CLEO_CALL | Starts the execution of the SCM function with given params, optionally receiving |
| `0AB2` | CLEO_RETURN | Returns the flow of the execution to the last CLEO_CALL instruction, optionally  |
| `0AB3` | SET_CLEO_SHARED_VAR | Sets the value of an element in the global array maintained by CLEO (index is be |
| `0AB4` | GET_CLEO_SHARED_VAR | Reads the value of an element in the global array maintained by CLEO (index is b |
| `0AB5` | STORE_CLOSEST_ENTITIES | Stores the handles of a vehicle and ped closest to the char or -1 otherwise. Ign |
| `0AB6` | GET_TARGET_BLIP_COORDS | Gets the coordinates of the location targeted in the game map |
| `0AB7` | GET_CAR_NUMBER_OF_GEARS | Gets the total number of gears of the vehicle and stores it to the variable |
| `0AB8` | GET_CAR_CURRENT_GEAR | Returns the current gear of the vehicle |
| `0ABA` | TERMINATE_ALL_CUSTOM_SCRIPTS_WITH_THIS_NAME | Ends the custom CLEO scripts with the specified name, freeing game memory |
| `0ABD` | IS_CAR_SIREN_ON |  |
| `0ABE` | IS_CAR_ENGINE_ON |  |
| `0ABF` | CLEO_SET_CAR_ENGINE_ON | Sets whether the vehicle's engine is turned on or off |
| `0AC6` | GET_LABEL_POINTER | Stores the absolute address of a code location marked with the label |
| `0AC7` | GET_VAR_POINTER | Stores the absolute address of the variable |
| `0AC8` | ALLOCATE_MEMORY | Allocates a chunk of memory of the given size and stores its address to the vari |
| `0AC9` | FREE_MEMORY | Frees the memory allocated with 0AC8 |
| `0ACA` | PRINT_HELP_STRING | Displays a custom text (provided as a literal or an address) in a black box simi |
| `0ACB` | PRINT_BIG_STRING | Displays a custom text (provided as a literal or an address) similarly to PRINT_ |
| `0ACC` | PRINT_STRING | Displays a custom text (provided as a literal or an address) similarly to PRINT |
| `0ACD` | PRINT_STRING_NOW | Displays a custom text (provided as a literal or an address) similarly to PRINT_ |
| `0ACE` | PRINT_HELP_FORMATTED | Displays a black text box for a few seconds respecting the format of the String  |
| `0ACF` | PRINT_BIG_FORMATTED | Formats args according to the format string, then displays it similarly to PRINT |
| `0AD0` | PRINT_FORMATTED | Formats args according to the format string, then displays it similarly to PRINT |
| `0AD1` | PRINT_FORMATTED_NOW | Formats args according to the format string, then displays it similarly to PRINT |
| `0AD2` | GET_CHAR_PLAYER_IS_TARGETING |  |
| `0AD3` | STRING_FORMAT | Formats a text according to the format string and given arguments and writes it  |
| `0AD4` | SCAN_STRING | Extracts data from a string using sscanf |
| `0AD5` | FILE_SEEK | Sets the position of the file to the given offset from the origin |
| `0AD6` | IS_END_OF_FILE_REACHED | Returns true if all data has been read or any file error occurred |
| `0AD7` | READ_STRING_FROM_FILE | Reads up to maxLength-1 text characters from the file until the newline or the e |
| `0AD8` | WRITE_STRING_TO_FILE | Copies data from the source string to the file up to but not including the null  |
| `0AD9` | WRITE_FORMATTED_STRING_TO_FILE | Writes a formatted string to the file |
| `0ADA` | SCAN_FILE | Extracts data from a file using fscanf |
| `0ADB` | GET_NAME_OF_VEHICLE_MODEL |  |
| `0ADC` | TEST_CHEAT | Returns true if the specified string of letters has been typed on the keyboard |
| `0ADD` | SPAWN_VEHICLE_BY_CHEATING | Creates a vehicle with the model (no pre-loading needed) in front of the player |
| `0ADE` | GET_TEXT_LABEL_STRING | Returns the text associated with the GXT key |
| `0ADF` | ADD_TEXT_LABEL | Adds or updates the text associated with the dynamic GXT key. It does nothing if |
| `0AE0` | REMOVE_TEXT_LABEL | Deletes the key and associated text created with ADD_TEXT_LABEL or defined in a  |
| `0AE1` | GET_RANDOM_CHAR_IN_SPHERE_NO_SAVE_RECURSIVE |  |
| `0AE2` | GET_RANDOM_CAR_IN_SPHERE_NO_SAVE_RECURSIVE |  |
| `0AE3` | GET_RANDOM_OBJECT_IN_SPHERE_NO_SAVE_RECURSIVE |  |
| `0AE4` | DOES_DIRECTORY_EXIST | Returns true if a directory at the given path exists |
| `0AE5` | CREATE_DIRECTORY | Creates a directory at the given path |
| `0AE6` | FIND_FIRST_FILE | Searches a directory for a file or subdirectory with a name that matches a speci |
| `0AE7` | FIND_NEXT_FILE | Continues a file search from a previous call to 0AE6 |
| `0AE8` | FIND_CLOSE | Closes a file search handle opened by 0AE6 |
| `0AE9` | POP_FLOAT | Returns a floating-point number stored as the result of the function called (0AA |
| `0AEA` | GET_PED_REF | Gets the corresponding handle of the char located at the given address in memory |
| `0AEB` | GET_VEHICLE_REF | Gets the corresponding handle of the vehicle located at the given address in mem |
| `0AEC` | GET_OBJECT_REF | Gets the corresponding handle of the object located at the given address in memo |
| `0AED` | STRING_FLOAT_FORMAT |  |
| `0AEE` | POW | Returns the specified number raised to the specified power |
| `0AEF` | LOG | Returns the logarithm of the specified number in the specified base |
| `0DD5` | GET_PLATFORM | Returns platform type info (device/operating system) |
| `2000` | GET_CLEO_ARG_COUNT | Gets argument count used to call current cleo function (0AB1) |
| `2002` | CLEO_RETURN_WITH | Returns from the current SCM function (0AB1) and sets the condition result to sp |
| `2003` | CLEO_RETURN_FAIL | Returns from the current SCM function (0AB1) and sets the condition result to fa |
| `290B` | FLOAT_MUL | Multiplies two float values and writes the result into the variable |

## Detailed Reference

### Car

### `0AB7` GET_CAR_NUMBER_OF_GEARS
Gets the total number of gears of the vehicle and stores it to the variable

**Class:** `Car.GetNumberOfGears`

**Input:**
- `self: Car`

**Output:**
- `numGear: int (variable)`

---

### `0AB8` GET_CAR_CURRENT_GEAR
Returns the current gear of the vehicle

**Class:** `Car.GetCurrentGear`

**Input:**
- `self: Car`

**Output:**
- `gear: int (variable)`

---

### `0ABD` IS_CAR_SIREN_ON

**Class:** `Car.IsSirenOn`
**Flags:** condition

**Input:**
- `self: Car`

---

### `0ABE` IS_CAR_ENGINE_ON

**Class:** `Car.IsEngineOn`
**Flags:** condition

**Input:**
- `self: Car`

---

### `0ABF` CLEO_SET_CAR_ENGINE_ON
Sets whether the vehicle's engine is turned on or off

**Class:** `Car.CleoSetEngineOn`

**Input:**
- `self: Car`
- `state: bool`

---

### Char

### `0AB5` STORE_CLOSEST_ENTITIES
Stores the handles of a vehicle and ped closest to the char or -1 otherwise. Ignores script created entities

**Class:** `Char.StoreClosestEntities`

**Input:**
- `self: Char`

**Output:**
- `carHandle: Car (variable)`
- `charHandle: Char (variable)`

---

### DynamicLibrary

### `0AA2` LOAD_DYNAMIC_LIBRARY
Loads the specified module (usually a dynamic-link library (DLL)) into the address space of the game

**Class:** `DynamicLibrary.Load`
**Flags:** constructor, condition

**Input:**
- `fileName: string`

**Output:**
- `handle: DynamicLibrary (variable)`

---

### `0AA3` FREE_DYNAMIC_LIBRARY
Frees the loaded dynamic-link library (DLL) module and unloads it from the address space of the game

**Class:** `DynamicLibrary.Free`
**Flags:** destructor

**Input:**
- `self: DynamicLibrary`

---

### `0AA4` GET_DYNAMIC_LIBRARY_PROCEDURE
Retrieves the address of an exported function or variable from the specified dynamic-link library (DLL)

**Class:** `DynamicLibrary.GetProcedure`
**Flags:** condition

**Input:**
- `procName: string`
- `self: DynamicLibrary`

**Output:**
- `address: int (variable)`

---

### File

### `0A9A` OPEN_FILE
Opens the file in the specified mode, sets the condition result to True if the open operation has been successful, or to False otherwise, and writes the file handle to the variable

**Class:** `File.Open`
**Flags:** constructor, condition

**Input:**
- `filePathName: string`
- `mode: FileMode`

**Output:**
- `handle: File (variable)`

---

### `0A9B` CLOSE_FILE
Closes the file and frees the memory

**Class:** `File.Close`
**Flags:** destructor

**Input:**
- `self: File`

---

### `0A9C` GET_FILE_SIZE
Gets the file size in bytes

**Class:** `File.GetSize`

**Input:**
- `self: File`

**Output:**
- `size: int (variable)`

---

### `0A9D` READ_FROM_FILE
Reads the specified number of bytes from the opened file and writes them to the memory region starting from the address of the destination variable

**Class:** `File.Read`

**Input:**
- `self: File`
- `size: int`

**Output:**
- `destination: int (variable)`

---

### `0A9E` WRITE_TO_FILE
Copies the specified number of bytes of the memory region starting from the address of the source variable to the file

**Class:** `File.Write`

**Input:**
- `self: File`
- `size: int`
- `source: int (variable)`

---

### `0AD5` FILE_SEEK
Sets the position of the file to the given offset from the origin

**Class:** `File.Seek`
**Flags:** condition

**Input:**
- `self: File`
- `offset: int`
- `origin: SeekOrigin`

---

### `0AD6` IS_END_OF_FILE_REACHED
Returns true if all data has been read or any file error occurred

**Class:** `File.IsEndReached`
**Flags:** condition

**Input:**
- `self: File`

---

### `0AD7` READ_STRING_FROM_FILE
Reads up to maxLength-1 text characters from the file until the newline or the end-of-file is reached. Result will be null-terminated string

**Class:** `File.ReadString`
**Flags:** condition

**Input:**
- `self: File`
- `storeTo: string`
- `maxLength: int`

---

### `0AD8` WRITE_STRING_TO_FILE
Copies data from the source string to the file up to but not including the null character

**Class:** `File.WriteString`
**Flags:** condition

**Input:**
- `self: File`
- `source: string`

---

### `0AD9` WRITE_FORMATTED_STRING_TO_FILE
Writes a formatted string to the file

**Class:** `File.WriteFormattedString`

**Input:**
- `self: File`
- `format: string`
- `args: arguments`

**Details:**

The output text is constructed out of the given string and any extra arguments.  

Common [C++ format specifiers](https://cplusplus.com/reference/cstdio/printf/) starting from `%` are used to define argument type, e.g.:  
* `%d` integer number in decimal form
* `%x` integer number in hex form (lower case letters)
* `%X` integer number in hex form (upper case letters)
* `%f` floating-point number
* `%s` string
* `%p` 8-digit hex number
* `%%` single `%` character
* `%c` single ASCII character specified by number
* `%4d` at least 4 digits wide integer number (padded with spaces)
* `%04d` at least 4 digits wide integer number (padded with zeros)
* `%.2f` floating-point number rounded to 2 digits after decimal point

The format string may contain zero or more specifiers and their count must match the number of arguments.

---

### `0ADA` SCAN_FILE
Extracts data from a file using fscanf

**Class:** `File.Scan`
**Flags:** condition

**Input:**
- `self: File`
- `format: string`

**Output:**
- `nValues: int (variable)`
- `values: arguments (variable)`

---

### FindFile

### `0AE6` FIND_FIRST_FILE
Searches a directory for a file or subdirectory with a name that matches a specific name (or partial name if wildcards are used)

**Class:** `FindFile.First`
**Flags:** constructor, condition

**Input:**
- `searchMask: string`

**Output:**
- `handle: FindFile (variable)`
- `fileName: string (variable)`

---

### `0AE7` FIND_NEXT_FILE
Continues a file search from a previous call to 0AE6

**Class:** `FindFile.Next`
**Flags:** condition

**Input:**
- `self: FindFile`

**Output:**
- `fileName: string (variable)`

---

### `0AE8` FIND_CLOSE
Closes a file search handle opened by 0AE6

**Class:** `FindFile.Close`

**Input:**
- `self: FindFile`

---

### Fs

### `0A99` SET_CURRENT_DIRECTORY
Sets the current working directory (cwd) to a predefined location with a value of 0 or 1, or to an arbitrary path with a string value

**Class:** `Fs.SetCurrentDirectory`
**Flags:** static

**Input:**
- `path: any`

---

### `0AAB` DOES_FILE_EXIST
Returns true if a file at the given path exists

**Class:** `Fs.DoesFileExist`
**Flags:** static, condition

**Input:**
- `path: string`

---

### `0AE4` DOES_DIRECTORY_EXIST
Returns true if a directory at the given path exists

**Class:** `Fs.DoesDirectoryExist`
**Flags:** condition, static

**Input:**
- `path: string`

---

### `0AE5` CREATE_DIRECTORY
Creates a directory at the given path

**Class:** `Fs.CreateDirectory`
**Flags:** static, condition

**Input:**
- `path: string`

---

### Game

### `0AA9` IS_GAME_VERSION_ORIGINAL
Returns true if the game version is vanilla 1.0

**Class:** `Game.IsVersionOriginal`
**Flags:** condition, static

---

### `0DD5` GET_PLATFORM
Returns platform type info (device/operating system)

**Class:** `Game.GetPlatform`
**Flags:** static

**Output:**
- `platform: Platform (variable)`

---

### Math

### `0AEE` POW
Returns the specified number raised to the specified power

**Class:** `Math.Pow`
**Flags:** static

**Input:**
- `number: float`
- `power: float`

**Output:**
- `result: float (variable)`

---

### `0AEF` LOG
Returns the logarithm of the specified number in the specified base

**Class:** `Math.Log`
**Flags:** static

**Input:**
- `number: float`
- `base: float`

**Output:**
- `result: float (variable)`

---

### Memory

### `0A8C` WRITE_MEMORY
Writes the value at the memory address

**Class:** `Memory.Write`
**Flags:** static

**Input:**
- `address: int`
- `size: int`
- `value: any`
- `vp: bool`

---

### `0A8D` READ_MEMORY
Reads a value from the game memory

**Class:** `Memory.Read`
**Flags:** static

**Input:**
- `address: int`
- `size: int`
- `vp: bool`

**Output:**
- `result: any (variable)`

---

### `0A96` GET_PED_POINTER
Gets the address of the ped struct in the game memory by its handle

**Class:** `Memory.GetPedPointer`
**Flags:** static

**Input:**
- `char: Char`

**Output:**
- `address: int (variable)`

---

### `0A97` GET_VEHICLE_POINTER
Gets the address of the vehicle struct in the game memory by its handle

**Class:** `Memory.GetVehiclePointer`
**Flags:** static

**Input:**
- `handle: Car`

**Output:**
- `address: int (variable)`

---

### `0A98` GET_OBJECT_POINTER
Gets the address of the object struct in the game memory by its handle

**Class:** `Memory.GetObjectPointer`
**Flags:** static

**Input:**
- `object: Object`

**Output:**
- `address: int (variable)`

---

### `0A9F` GET_THIS_SCRIPT_STRUCT
Gets the address of the current script structure in the game memory

**Class:** `Memory.GetThisScriptStruct`
**Flags:** static

**Output:**
- `address: int (variable)`

---

### `0AA5` CALL_FUNCTION
Calls a function at the address with the given arguments and the calling convention defined by the pop parameter where 0 means 'stdcall' and a value equal to numParams means  'cdecl'

**Class:** `Memory.CallFunction`
**Flags:** static

**Input:**
- `address: int`
- `numArgs: int`
- `pop: int`
- `args: arguments`

---

### `0AA6` CALL_METHOD
Calls a method of the object (struct) with the given arguments and the 'thiscall' calling convention (pop is always 0)

**Class:** `Memory.CallMethod`
**Flags:** static

**Input:**
- `address: int`
- `struct: int`
- `numArgs: int`
- `pop: int`
- `args: arguments`

---

### `0AA7` CALL_FUNCTION_RETURN
Calls a function similarly to 0AA5 and writes the result into the variable following the arguments list

**Class:** `Memory.CallFunctionReturn`
**Flags:** static

**Input:**
- `address: int`
- `numArgs: int`
- `pop: int`
- `args: arguments`

**Output:**
- `funcRet: any (variable)`

---

### `0AA8` CALL_METHOD_RETURN
Calls a method of the object (struct) similarly to 0AA6 and writes the result into the variable following the arguments list

**Class:** `Memory.CallMethodReturn`
**Flags:** static

**Input:**
- `address: int`
- `struct: int`
- `numArgs: int`
- `pop: int`
- `args: arguments`

**Output:**
- `funcRet: any (variable)`

---

### `0AAA` GET_SCRIPT_STRUCT_NAMED
Gets the address of a running script which name matches the given string or 0 otherwise

**Class:** `Memory.GetScriptStructNamed`
**Flags:** static

**Input:**
- `scriptName: string`

**Output:**
- `address: int (variable)`

---

### `0AC6` GET_LABEL_POINTER
Stores the absolute address of a code location marked with the label

**Class:** `Memory.GetLabelPointer`
**Flags:** static

**Input:**
- `label`

**Output:**
- `address: int (variable)`

---

### `0AC7` GET_VAR_POINTER
Stores the absolute address of the variable

**Class:** `Memory.GetVarPointer`
**Flags:** static

**Input:**
- `any (variable)`

**Output:**
- `address: int (variable)`

---

### `0AC8` ALLOCATE_MEMORY
Allocates a chunk of memory of the given size and stores its address to the variable

**Class:** `Memory.Allocate`
**Flags:** static, condition

**Input:**
- `size: int`

**Output:**
- `address: int (variable)`

---

### `0AC9` FREE_MEMORY
Frees the memory allocated with 0AC8

**Class:** `Memory.Free`
**Flags:** static

**Input:**
- `address: int`

---

### `0AE9` POP_FLOAT
Returns a floating-point number stored as the result of the function called (0AA5, 0AA6, 0AA7, 0AA8) immediately before this command

**Class:** `Memory.PopFloat`
**Flags:** static

**Output:**
- `number: float (variable)`

---

### `0AEA` GET_PED_REF
Gets the corresponding handle of the char located at the given address in memory

**Class:** `Memory.GetPedRef`
**Flags:** static

**Input:**
- `address: int`

**Output:**
- `handle: Char (variable)`

---

### `0AEB` GET_VEHICLE_REF
Gets the corresponding handle of the vehicle located at the given address in memory

**Class:** `Memory.GetVehicleRef`
**Flags:** static

**Input:**
- `address: int`

**Output:**
- `handle: Car (variable)`

---

### `0AEC` GET_OBJECT_REF
Gets the corresponding handle of the object located at the given address in memory

**Class:** `Memory.GetObjectRef`
**Flags:** static

**Input:**
- `address: int`

**Output:**
- `handle: Object (variable)`

---

### Pad

### `0AB0` IS_KEY_PRESSED
Returns true if the player is pressing a keyboard button with the specified code

**Class:** `Pad.IsKeyPressed`
**Flags:** condition, static

**Input:**
- `keyCode: KeyCode`

---

### `0ADC` TEST_CHEAT
Returns true if the specified string of letters has been typed on the keyboard

**Class:** `Pad.TestCheat`
**Flags:** static, condition

**Input:**
- `input: string`

---

### Player

### `0AD2` GET_CHAR_PLAYER_IS_TARGETING

**Class:** `Player.GetCharIsTargeting`
**Flags:** condition

**Input:**
- `self: Player`

**Output:**
- `handle: Char (variable)`

---

### Streaming

### `0ADB` GET_NAME_OF_VEHICLE_MODEL

**Class:** `Streaming.GetNameOfVehicleModel`
**Flags:** static

**Input:**
- `modelId: model_vehicle`

**Output:**
- `carName: string (variable)`

---

### Text

### `0ACA` PRINT_HELP_STRING
Displays a custom text (provided as a literal or an address) in a black box similarly to PRINT_HELP

**Class:** `Text.PrintHelpString`
**Flags:** static

**Input:**
- `text: string`

---

### `0ACB` PRINT_BIG_STRING
Displays a custom text (provided as a literal or an address) similarly to PRINT_BIG

**Class:** `Text.PrintBigString`
**Flags:** static

**Input:**
- `text: string`
- `time: int`
- `style: TextStyle`

---

### `0ACC` PRINT_STRING
Displays a custom text (provided as a literal or an address) similarly to PRINT

**Class:** `Text.PrintString`
**Flags:** static

**Input:**
- `text: string`
- `time: int`

**Details:**

This command displays an **arbitrary text string** as a subtitle. The message is appended to the end of the game's subtitle queue. It becomes visible only when all previously queued messages have expired, so it has **lower priority** than PRINT_STRING_NOW.

The internal buffer is 400 characters; text longer than 399 characters is silently truncated.

To display a message using a GXT key, use PRINT.

## Queueing behaviour

Messages are placed in a circular queue of 8 slots. Only the first slot (the current message) is visible on screen. Each subsequent message waits until the one before it expires.

If all 8 slots are occupied, the next message is silently discarded.

## Brief History (CLEO 5 only)

- The message is recorded in **Brief** (up to 20 entries) at the moment it becomes the current (visible) message.
- Duplicate text is silently ignored.
- To suppress a single message from Brief, call `ADD_NEXT_MESSAGE_TO_PREVIOUS_BRIEFS false` immediately before `PRINT_STRING`. The flag is consumed and restored to `true` by the command itself.

**CLEO 4 / .cs4 scripts**: the flag and Brief are never modified.

## Disabling Subtitles with ~z~ (CLEO 5 only)

Any text starting with the `~z~` GXT prefix will be hidden from the view and the brief, when the option "Show Subtitles" is disabled in the game settings. It is mainly used for mission dialogue lines.

**CLEO 4 / .cs4 scripts**: the `~z~` prefix has no effect.

---

### `0ACD` PRINT_STRING_NOW
Displays a custom text (provided as a literal or an address) similarly to PRINT_NOW

**Class:** `Text.PrintStringNow`
**Flags:** static

**Input:**
- `text: string`
- `time: int`

**Details:**

This command displays an **arbitrary text string** as a subtitle with **immediate priority**. The message bypasses the queue and is placed at the front of the subtitle display, replacing whatever is currently shown, so it has **higher priority** than PRINT_STRING. 

The internal buffer is 400 characters; text longer than 399 characters is silently truncated.

To display a message using a GXT key, use PRINT_NOW.

## Priority model

Unlike `PRINT_STRING`, this opcode clears any queued messages and places the new message at the front (slot 0) for immediate display. Use this variant when the subtitle must be seen at once, regardless of what else may be in the queue.

## Brief History (CLEO 5 only)

- The message is recorded in **Brief** (up to 20 entries) **immediately**.
- Duplicate text is silently ignored.
- To suppress a single message from Brief, call `ADD_NEXT_MESSAGE_TO_PREVIOUS_BRIEFS false` immediately before `PRINT_STRING_NOW`. The flag is consumed and restored to `true` by the command itself.

**CLEO 4 / .cs4 scripts**: the flag and Brief are never modified.

## Disabling Subtitles with ~z~ (CLEO 5 only)

Any text starting with the `~z~` GXT prefix will be hidden from the view and the brief, when the option "Show Subtitles" is disabled in the game settings. It is mainly used for mission dialogue lines.

**CLEO 4 / .cs4 scripts**: the `~z~` prefix has no effect.

---

### `0ACE` PRINT_HELP_FORMATTED
Displays a black text box for a few seconds respecting the format of the String entered

**Class:** `Text.PrintHelpFormatted`
**Flags:** static

**Input:**
- `text: string`
- `args: arguments`

---

### `0ACF` PRINT_BIG_FORMATTED
Formats args according to the format string, then displays it similarly to PRINT_BIG

**Class:** `Text.PrintBigFormatted`
**Flags:** static

**Input:**
- `format: string`
- `time: int`
- `style: TextStyle`
- `args: arguments`

---

### `0AD0` PRINT_FORMATTED
Formats args according to the format string, then displays it similarly to PRINT

**Class:** `Text.PrintFormatted`
**Flags:** static

**Input:**
- `format: string`
- `time: int`
- `args: arguments`

**Details:**

This command displays a **printf-style formatted text string** as a subtitle. The format string and its arguments are expanded into a final string, which is then appended to the end of the game's subtitle queue. It becomes visible only when all previously queued messages have expired, so it has **lower priority** than `PRINT_FORMATTED_NOW`.

The internal buffer is 400 characters; text longer than 399 characters is silently truncated.

## Supported format specifiers

Common [C++ format specifiers](https://cplusplus.com/reference/cstdio/printf/) starting from `%` are used to define argument type, e.g.:  
* `%d` integer number in decimal form
* `%x` integer number in hex form (lower case letters)
* `%X` integer number in hex form (upper case letters)
* `%f` floating-point number
* `%s` string
* `%p` 8-digit hex number
* `%%` single `%` character
* `%c` single ASCII character specified by number
* `%4d` at least 4 digits wide integer number (padded with spaces)
* `%04d` at least 4 digits wide integer number (padded with zeros)
* `%.2f` floating-point number rounded to 2 digits after decimal point

The format string may contain zero or more specifiers and their count must match the number of arguments.

## Queueing behaviour

Messages are placed in a circular queue of 8 slots. Only the first slot (the current message) is visible on screen. Each subsequent message waits until the one before it expires.

If all 8 slots are occupied, the next message is silently discarded.

## Brief History (CLEO 5 only)

- The message is recorded in **Brief** (up to 20 entries) at the moment it becomes the current (visible) message.
- Duplicate text is silently ignored.
- Formatting is applied at call time; the fully expanded string is what gets displayed and stored in Brief History.
- To suppress a single message from Brief, call `ADD_NEXT_MESSAGE_TO_PREVIOUS_BRIEFS false` immediately before `PRINT_FORMATTED`. The flag is consumed and restored to `true` by the command itself.

**CLEO 4 / .cs4 scripts**: the flag and Brief are never modified.

## Disabling Subtitles with ~z~ (CLEO 5 only)

Any text starting with the `~z~` GXT prefix will be hidden from the view and the brief, when the option "Show Subtitles" is disabled in the game settings. It is mainly used for mission dialogue lines.

**CLEO 4 / .cs4 scripts**: the `~z~` prefix has no effect.

---

### `0AD1` PRINT_FORMATTED_NOW
Formats args according to the format string, then displays it similarly to PRINT_NOW

**Class:** `Text.PrintFormattedNow`
**Flags:** static

**Input:**
- `format: string`
- `time: int`
- `args: arguments`

**Details:**

This command displays a **printf-style formatted text string** as a subtitle with **immediate priority**. The format string and its arguments are expanded into a final string, which is then placed at the front of the subtitle display, bypassing the queue and replacing whatever is currently shown, so it has **higher priority** than PRINT_FORMATTED.

The internal buffer is 400 characters; text longer than 399 characters is silently truncated.

To display a message using a GXT key, use PRINT_NOW.

## Supported format specifiers

Common [C++ format specifiers](https://cplusplus.com/reference/cstdio/printf/) starting from `%` are used to define argument type, e.g.:  
* `%d` integer number in decimal form
* `%x` integer number in hex form (lower case letters)
* `%X` integer number in hex form (upper case letters)
* `%f` floating-point number
* `%s` string
* `%p` 8-digit hex number
* `%%` single `%` character
* `%c` single ASCII character specified by number
* `%4d` at least 4 digits wide integer number (padded with spaces)
* `%04d` at least 4 digits wide integer number (padded with zeros)
* `%.2f` floating-point number rounded to 2 digits after decimal point

The format string may contain zero or more specifiers and their count must match the number of arguments.

## Priority model

Unlike PRINT_FORMATTED, this opcode clears any queued messages and places the new message at the front (slot 0) for immediate display. Use this variant when the subtitle must be seen at once, regardless of what else may be in the queue.

## Brief History (CLEO 5 only)

- The message is recorded in **Brief** (up to 20 entries) **immediately**.
- Duplicate text is silently ignored.
- Formatting is applied at call time; the fully expanded string is what gets displayed and stored in Brief History.
- To suppress a single message from Brief, call `ADD_NEXT_MESSAGE_TO_PREVIOUS_BRIEFS false` immediately before `PRINT_FORMATTED_NOW`. The flag is consumed and restored to `true` by the command itself.

**CLEO 4 / .cs4 scripts**: the flag and Brief are never modified.

## Disabling Subtitles with ~z~ (CLEO 5 only)

Any text starting with the `~z~` GXT prefix will be hidden from the view and the brief, when the option "Show Subtitles" is disabled in the game settings. It is mainly used for mission dialogue lines.

**CLEO 4 / .cs4 scripts**: the `~z~` prefix has no effect.

---

### `0AD3` STRING_FORMAT
Formats a text according to the format string and given arguments and writes it in the result

**Class:** `Text.StringFormat`
**Flags:** static

**Input:**
- `result: string`
- `format: string`
- `args: arguments`

---

### `0AD4` SCAN_STRING
Extracts data from a string using sscanf

**Class:** `Text.ScanString`
**Flags:** static, condition

**Input:**
- `string: string`
- `format: string`

**Output:**
- `nValues: int (variable)`
- `values: arguments (variable)`

---

### `0ADE` GET_TEXT_LABEL_STRING
Returns the text associated with the GXT key

**Class:** `Text.GetLabelString`
**Flags:** static

**Input:**
- `key: gxt_key`

**Output:**
- `text: string (variable)`

---

### `0ADF` ADD_TEXT_LABEL
Adds or updates the text associated with the dynamic GXT key. It does nothing if the same key is defined in a FXT file

**Class:** `Text.AddLabel`
**Flags:** static

**Input:**
- `dynamicKey: gxt_key`
- `text: string`

---

### `0AE0` REMOVE_TEXT_LABEL
Deletes the key and associated text created with ADD_TEXT_LABEL or defined in a FXT file

**Class:** `Text.RemoveLabel`
**Flags:** static

**Input:**
- `key: gxt_key`

---

### `0AED` STRING_FLOAT_FORMAT

**Class:** `Text.StringFloatFormat`
**Flags:** static

**Input:**
- `number: float`
- `format: string`

**Output:**
- `text: string (variable)`

---

### World

### `0AB6` GET_TARGET_BLIP_COORDS
Gets the coordinates of the location targeted in the game map

**Class:** `World.GetTargetCoords`
**Flags:** static, condition

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0ADD` SPAWN_VEHICLE_BY_CHEATING
Creates a vehicle with the model (no pre-loading needed) in front of the player

**Class:** `World.SpawnVehicleByCheating`
**Flags:** static

**Input:**
- `modelId: model_vehicle`

**Details:**

This command spawns a vehicle in front of the player without requiring the model to be preloaded. Despite its name, using this command does not affect cheat statistics.

Unlike CREATE_CAR, vehicles created with this command are not flagged as owned by the player (`VEHICLEFLAG_HASBEENOWNEDBYPLAYER`). 
As a result, entering such a vehicle for the first time grants a small number of chaos points, which in some cases may be enough to trigger a wanted level.

---

### `0AE1` GET_RANDOM_CHAR_IN_SPHERE_NO_SAVE_RECURSIVE

**Class:** `World.GetRandomCharInSphereNoSaveRecursive`
**Flags:** static, condition

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `findNext: bool`
- `filter: CharSearchFilter`

**Output:**
- `handle: Char (variable)`

---

### `0AE2` GET_RANDOM_CAR_IN_SPHERE_NO_SAVE_RECURSIVE

**Class:** `World.GetRandomCarInSphereNoSaveRecursive`
**Flags:** static, condition

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `findNext: bool`
- `skipWrecked: bool`

**Output:**
- `handle: Car (variable)`

---

### `0AE3` GET_RANDOM_OBJECT_IN_SPHERE_NO_SAVE_RECURSIVE

**Class:** `World.GetRandomObjectInSphereNoSaveRecursive`
**Flags:** static, condition

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `findNext: bool`

**Output:**
- `handle: Object (variable)`

---

### `0A8E` INT_ADD
Adds together two integer values and writes the result into the variable

**Operator:** `+`

**Input:**
- `int`
- `int`

**Output:**
- `int (variable)`

---

### `0A8F` INT_SUB
Subtracts the integer value from another integer value and writes the result into the variable

**Operator:** `-`

**Input:**
- `int`
- `int`

**Output:**
- `int (variable)`

---

### `0A90` INT_MUL
Multiplies two integer values and writes the result into the variable

**Operator:** `*`

**Input:**
- `int`
- `int`

**Output:**
- `int (variable)`

---

### `0A91` INT_DIV
Divides the integer value by another integer value and writes the result into the variable

**Operator:** `/`

**Input:**
- `int`
- `int`

**Output:**
- `int (variable)`

---

### `0A92` STREAM_CUSTOM_SCRIPT
Loads a file with compiled SCM instructions at the given path and runs a new custom script


**Input:**
- `scriptFileName: string`
- `args: arguments`

---

### `0A93` TERMINATE_THIS_CUSTOM_SCRIPT
Ends the current custom script, preventing further execution

**Flags:** branch

---

### `0A94` LOAD_AND_LAUNCH_CUSTOM_MISSION


**Input:**
- `scriptFileName: string`
- `args: arguments`

---

### `0A95` SAVE_THIS_CUSTOM_SCRIPT
Marks this script to be saved whenever game is saved. After savegame load all local variables are restored and execution continues from saved position


---

### `0AA0` GOSUB_IF_FALSE
Transfers the script execution to the label as a subroutine if the result of the condition is false

**Flags:** branch

**Input:**
- `label`

---

### `0AA1` RETURN_IF_FALSE
Returns from the current subroutine if the result of the condition is false

**Flags:** branch

---

### `0AB1` CLEO_CALL
Starts the execution of the SCM function with given params, optionally receiving one or more numbers as the result. Return from function is performed with 0051, 0AB2, or 2002


**Input:**
- `label`
- `numArgs: int`
- `args: arguments`

---

### `0AB2` CLEO_RETURN
Returns the flow of the execution to the last CLEO_CALL instruction, optionally returning one or more numbers as the result


**Input:**
- `numRet: int`
- `retParams: arguments`

---

### `0AB3` SET_CLEO_SHARED_VAR
Sets the value of an element in the global array maintained by CLEO (index is between 0-1023)


**Input:**
- `index: int`
- `value: any`

---

### `0AB4` GET_CLEO_SHARED_VAR
Reads the value of an element in the global array maintained by CLEO (index is between 0-1023)


**Input:**
- `index: int`

**Output:**
- `result: any (variable)`

---

### `0ABA` TERMINATE_ALL_CUSTOM_SCRIPTS_WITH_THIS_NAME
Ends the custom CLEO scripts with the specified name, freeing game memory


**Input:**
- `name: string`

---

### `2000` GET_CLEO_ARG_COUNT
Gets argument count used to call current cleo function (0AB1)


**Output:**
- `count: int (variable)`

---

### `2002` CLEO_RETURN_WITH
Returns from the current SCM function (0AB1) and sets the condition result to specified value

**Flags:** condition

**Input:**
- `conditionResult: bool`
- `retArgs: arguments`

---

### `2003` CLEO_RETURN_FAIL
Returns from the current SCM function (0AB1) and sets the condition result to false, skipping variables in 0AB1

**Flags:** condition

**Input:**
- `arguments`

---

### `290B` FLOAT_MUL
Multiplies two float values and writes the result into the variable

**Operator:** `*`

**Input:**
- `float`
- `float`

**Output:**
- `float (variable)`

---
