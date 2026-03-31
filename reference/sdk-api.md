# CLEO5 SDK API Reference

API reference for CLEO 5 plugin development, derived from `CLEO.h` and `CLEO_Utils.h`.

Current SDK version: **5.3.0**

---

## Table of Contents

- [Types and Enums](#types-and-enums)
  - [eDataType](#edatatype)
  - [eArrayType](#earraytype)
  - [OpcodeResult](#opcoderesult)
  - [eCallbackId](#ecallbackid)
  - [eLogLevel](#eloglevel)
  - [eCLEO_Version](#ecleo_version)
  - [eGameVersion](#egameversion)
  - [eLogicalOperation](#elogicaloperation)
  - [SCRIPT_VAR](#script_var)
  - [CRunningScript](#crunningscript)
  - [StringList](#stringlist)
  - [CustomOpcodeHandler](#customopcodehandler)
- [API Functions](#api-functions)
  - [Version and Game Info](#version-and-game-info)
  - [Opcode and Command Registration](#opcode-and-command-registration)
  - [Callback Registration](#callback-registration)
  - [Script Management](#script-management)
  - [Parameter Reading](#parameter-reading)
  - [Parameter Writing](#parameter-writing)
  - [Parameter Inspection (Peek / Skip)](#parameter-inspection-peek--skip)
  - [Condition and Flow Control](#condition-and-flow-control)
  - [File System and Paths](#file-system-and-paths)
  - [Logging](#logging)
  - [Configuration](#configuration)
  - [Audio](#audio)
  - [Textures](#textures)
  - [Memory / SCM Data](#memory--scm-data)
- [Utility Macros (CLEO_Utils.h)](#utility-macros-cleo_utilsh)
  - [Logging Macros](#logging-macros)
  - [Condition Result](#condition-result)
  - [Parameter Skip / Peek Macros](#parameter-skip--peek-macros)
  - [OPCODE_READ_PARAM_* Macros](#opcode_read_param_-macros)
  - [OPCODE_WRITE_PARAM_* Macros](#opcode_write_param_-macros)
  - [OPCODE_READ_PARAM_OUTPUT_VAR_* Macros](#opcode_read_param_output_var_-macros)
  - [Validation Macros](#validation-macros)
- [Utility Helper Functions (CLEO_Utils.h)](#utility-helper-functions-cleo_utilsh)
  - [String Formatting](#string-formatting)
  - [Error Display](#error-display)
  - [Script Suspension](#script-suspension)
  - [Memory Patching](#memory-patching)
  - [StringList Creation](#stringlist-creation)
- [Plugin Development Pattern](#plugin-development-pattern)
  - [Project Setup](#project-setup)
  - [Plugin Skeleton](#plugin-skeleton)
  - [Registering Opcodes](#registering-opcodes)
  - [Registering Commands by Name](#registering-commands-by-name)
  - [Using Callbacks](#using-callbacks)
  - [Working with Strings](#working-with-strings)
  - [Condition Opcodes](#condition-opcodes)
  - [Variable-Argument Opcodes](#variable-argument-opcodes)

---

## Types and Enums

### eDataType

Operand/parameter types used in the script bytecode. Returned by `CLEO_GetOperandType()` and `thread->PeekDataType()`.

```cpp
enum eDataType : BYTE
{
    DT_END,                  // variable args end marker
    DT_DWORD,                // literal int 32
    DT_VAR,                  // globalVar $
    DT_LVAR,                 // localVar @
    DT_BYTE,                 // literal int 8
    DT_WORD,                 // literal int 16
    DT_FLOAT,                // literal float 32
    DT_VAR_ARRAY,            // globalArr $(,)
    DT_LVAR_ARRAY,           // localArr @(,)
    DT_TEXTLABEL,            // literal string up to 7 chars
    DT_VAR_TEXTLABEL,        // globalVarSString s$
    DT_LVAR_TEXTLABEL,       // localVarSString @s
    DT_VAR_TEXTLABEL_ARRAY,  // globalVarSStringArr s$(,)
    DT_LVAR_TEXTLABEL_ARRAY, // localVarSStringArr @s(,)
    DT_VARLEN_STRING,        // literal vstring ""
    DT_STRING,               // literal string up to 15 chars
    DT_VAR_STRING,           // globalVarVString v$
    DT_LVAR_STRING,          // localVarVString @v
    DT_VAR_STRING_ARRAY,     // globalVarStringArr v$(,)
    DT_LVAR_STRING_ARRAY,    // localVarStringArr @v(,)
    DT_INVALID = 0xFF        // CLEO internal
};
```

**Helper functions for eDataType:**

| Function | Description |
|---|---|
| `IsImmInteger(eDataType)` | True for `DT_BYTE`, `DT_WORD`, `DT_DWORD` |
| `IsImmFloat(eDataType)` | True for `DT_FLOAT` |
| `IsImmString(eDataType)` | True for `DT_STRING`, `DT_TEXTLABEL`, `DT_VARLEN_STRING` |
| `IsVarString(eDataType)` | True for all `DT_*VAR*_TEXTLABEL*` and `DT_*VAR*_STRING*` types |
| `IsVariable(eDataType)` | True for `DT_VAR`, `DT_VAR_ARRAY`, `DT_LVAR`, `DT_LVAR_ARRAY` |
| `IsArray(eDataType)` | True for all array types |
| `ToStr(eDataType)` | Returns short string name for logging (e.g. `"Int32"`, `"GlobVar"`) |
| `ToKindStr(eDataType, eArrayType)` | Returns kind name: `"int"`, `"float"`, `"string"`, or `"variable"` |

### eArrayType

Type of data stored in array variables.

```cpp
enum eArrayType : BYTE
{
    AT_INT,        // variable with integer
    AT_FLOAT,      // variable with float
    AT_TEXTLABEL,  // variable with short string (8 char)
    AT_STRING,     // variable with long string (16 char)
    AT_NONE = 0xFF // CLEO internal
};
```

Note: Array flags byte contains other info. Use `ArrayTypeMask` when reading the type:

```cpp
static const BYTE ArrayTypeMask = AT_INT | AT_FLOAT | AT_TEXTLABEL | AT_STRING;
```

### OpcodeResult

Return value from opcode handler functions.

```cpp
enum OpcodeResult : char
{
    OR_NONE      = -2, // opcode not handled (used in callbacks)
    OR_ERROR     = -1, // error occurred
    OR_CONTINUE  = 0,  // continue script execution
    OR_INTERRUPT = 1,  // interrupt (pause) script execution
};
```

- **OR_CONTINUE** -- The normal return value. Script continues to the next opcode immediately.
- **OR_INTERRUPT** -- Script yields for this frame (e.g. after a wait opcode or on error).
- **OR_ERROR** -- Signals an error.
- **OR_NONE** -- Used in `ScriptOpcodeProcessBefore`/`After` callbacks to indicate the callback did not handle the opcode.

### eCallbackId

Identifiers for registering callbacks with `CLEO_RegisterCallback`.

```cpp
enum class eCallbackId : DWORD
{
    GameBegin              = 0,   // void WINAPI (DWORD saveSlot)
                                  //   -1 if not started from save
    GameProcessBefore      = 1,   // void WINAPI ()
                                  //   once per frame, before game logic
    GameProcessAfter       = 14,  // void WINAPI ()
                                  //   once per frame, after game logic
    GameEnd                = 2,   // void WINAPI ()
    ScriptsLoaded          = 3,   // void WINAPI ()
    ScriptsFinalize        = 4,   // void WINAPI ()
                                  //   called after all scripts deleted;
                                  //   pointers no longer valid
    ScriptRegister         = 5,   // void WINAPI (CRunningScript*)
                                  //   after script creation
    ScriptUnregister       = 6,   // void WINAPI (CRunningScript*)
                                  //   before script deletion
    ScriptProcessBefore    = 7,   // bool WINAPI (CRunningScript*)
                                  //   return false to skip processing
    ScriptProcessAfter     = 15,  // void WINAPI (CRunningScript*)
    ScriptOpcodeProcessBefore = 8,  // OpcodeResult WINAPI (CRunningScript*, DWORD opcode)
                                    //   return non-OR_NONE to signal handled
    ScriptOpcodeProcessAfter  = 9,  // OpcodeResult WINAPI (CRunningScript*, DWORD opcode, OpcodeResult result)
                                    //   return non-OR_NONE to overwrite result
    ScriptDraw             = 10,  // void WINAPI (bool beforeFade)
    DrawingFinished        = 11,  // void WINAPI ()
                                  //   after game rendered, before present
    Log                    = 12,  // void (eLogLevel, const char* msg)
    MainWindowFocus        = 13,  // void WINAPI (bool active)
};
```

### eLogLevel

Log severity levels used by `CLEO_Log` and the Log callback.

```cpp
enum class eLogLevel : DWORD
{
    None,     // no logging
    Debug,    // debug mode / user traces
    Error,    // errors and warnings
    Default   // all log messages
};
```

### eCLEO_Version

Script compatibility version, returned by `CLEO_GetScriptVersion`.

```cpp
enum eCLEO_Version : DWORD
{
    CLEO_VER_3     = 0x03000000,
    CLEO_VER_4_MIN = 0x04000000,
    CLEO_VER_4_2   = 0x04020000,
    CLEO_VER_4_3   = 0x04030000,
    CLEO_VER_4_4   = 0x04040000,
    CLEO_VER_4     = CLEO_VER_4_4,
    CLEO_VER_5     = 0x05000000,
    CLEO_VER_CUR   = CLEO_VERSION   // current build version
};
```

### eGameVersion

Game executable version, returned by `CLEO_GetGameVersion`.

```cpp
enum eGameVersion : int
{
    GV_US10  = 0,  // 1.0 US
    GV_US11  = 1,  // 1.01 US (not supported)
    GV_EU10  = 2,  // 1.0 EU
    GV_EU11  = 3,  // 1.01 EU
    GV_STEAM,
    GV_TOTAL,
    GV_UNK   = -1  // any other
};
```

### eLogicalOperation

Internal condition chaining state (AND/OR logic for compound conditions).

```cpp
enum eLogicalOperation : WORD
{
    NONE   = 0,     // just replace
    ANDS_1 = 1,     // count of 'and' keywords (1..8)
    // ...through ANDS_8, AND_END
    ORS_1  = 21,    // count of 'or' keywords (1..8)
    // ...through ORS_8, OR_END
};
```

### SCRIPT_VAR

Union type representing a single 32-bit script variable. Used in `opcodeParams` array and local variables.

```cpp
union SCRIPT_VAR {
    DWORD  dwParam;   // unsigned 32-bit int
    short  wParam;    // signed 16-bit int
    WORD   usParam;   // unsigned 16-bit int
    BYTE   ucParam;   // unsigned 8-bit int
    char   cParam;    // signed 8-bit int
    bool   bParam;    // boolean
    int    nParam;    // signed 32-bit int
    float  fParam;    // 32-bit float
    void*  pParam;    // pointer
    char*  pcParam;   // char pointer
};
```

### CRunningScript

The core script object (224 bytes / 0xE0). Key fields:

| Offset | Field | Type | Description |
|---|---|---|---|
| 0x00 | `Next` | `CRunningScript*` | Next script in queue |
| 0x04 | `Previous` | `CRunningScript*` | Previous script in queue |
| 0x08 | `Name[8]` | `char[8]` | Script name (set by opcode 03A4) |
| 0x10 | `BaseIP` | `void*` | Pointer to start of script in memory |
| 0x14 | `CurrentIP` | `BYTE*` | Current instruction pointer |
| 0x18 | `Stack[8]` | `BYTE*[8]` | Return stack for gosub/return |
| 0x38 | `SP` | `WORD` | Stack pointer |
| 0x3C | `LocalVar[32]` | `SCRIPT_VAR[32]` | Local variables |
| 0xBC | `Timers[2]` | `DWORD[2]` | Script timers |
| 0xC4 | `bIsActive` | `bool` | Is script active |
| 0xC5 | `bCondResult` | `bool` | Condition result |
| 0xC6 | `bUseMissionCleanup` | `bool` | Clean mission on end |
| 0xC7 | `bIsExternal` | `bool` | From script.img |
| 0xCC | `WakeTime` | `DWORD` | Wake time after wait opcode |
| 0xD0 | `LogicalOp` | `eLogicalOperation` | AND/OR chaining state |
| 0xD2 | `NotFlag` | `bool` | NOT modifier active |
| 0xD9 | `bIsMission` | `bool` | Is this a mission script |
| 0xDD | `ScmFunction` | `WORD` | Previous SCM function id |
| 0xDF | `bIsCustom` | `bool` (bitfield) | Is this a CLEO script |

**Key methods:**

| Method | Description |
|---|---|
| `IsActive()` | Returns `bIsActive` |
| `IsCustom()` | Returns true if this is a CLEO script |
| `IsMission()` | Returns true if this is a mission script |
| `GetName()` | Returns null-terminated script name |
| `GetBasePointer()` | Returns `BaseIP` as `BYTE*` |
| `GetBytePointer()` | Returns `CurrentIP` |
| `SetIp(void*)` | Sets current instruction pointer |
| `Jump(int offset)` | Calls `CLEO_ThreadJumpAtLabelPtr` |
| `PeekDataType()` | Returns `eDataType` of next parameter without advancing |
| `PeekArrayType()` | Returns `eArrayType` of next parameter without advancing |
| `GetConditionResult()` | Returns current condition flag |
| `SetConditionResult(bool)` | Sets condition flag via `CLEO_SetThreadCondResult` |
| `GetVarPtr()` / `GetVarPtr(int)` | Pointer to local variables |
| `GetIntVar(int)` / `SetIntVar(int, int)` | Get/set local variable as int |
| `SetFloatVar(int, float)` | Set local variable as float |

### StringList

Container returned by `CLEO_ListDirectory`. Must be freed with `CLEO_StringListFree`.

```cpp
struct StringList {
    DWORD count;
    char** strings;
};
```

### CustomOpcodeHandler

Function pointer type for opcode handlers.

```cpp
typedef OpcodeResult (__stdcall* CustomOpcodeHandler)(CRunningScript*);
```

---

## API Functions

All functions are declared `extern "C"` with `WINAPI` (__stdcall) calling convention.

### Version and Game Info

```cpp
DWORD WINAPI CLEO_GetVersion();
```
Returns the CLEO version as a packed DWORD: `0x0v0v0v00` (e.g. `0x05030000` for 5.3.0).

```cpp
LPCSTR WINAPI CLEO_GetVersionStr();
```
Returns a human-readable version string, e.g. `"5.0.0-alpha.1"`.

```cpp
eGameVersion WINAPI CLEO_GetGameVersion();
```
Returns the detected game executable version.

### Opcode and Command Registration

```cpp
BOOL WINAPI CLEO_RegisterOpcode(WORD opcode, CustomOpcodeHandler callback);
```
Registers a handler function for the given opcode number. Returns TRUE on success.

```cpp
BOOL WINAPI CLEO_RegisterCommand(const char* commandName, CustomOpcodeHandler callback);
```
Registers a handler by command name. Uses `cleo\.CONFIG\sa.json` to resolve the name to an opcode number.

```cpp
OpcodeResult WINAPI CLEO_CallNativeOpcode(CRunningScript* script, WORD opcode);
```
Calls the original (unhooked) handler for an opcode. Useful when wrapping existing opcodes.

### Callback Registration

```cpp
void WINAPI CLEO_RegisterCallback(eCallbackId id, void* func);
```
Registers a callback function. See [eCallbackId](#ecallbackid) for available events and their signatures.

```cpp
void WINAPI CLEO_UnregisterCallback(eCallbackId id, void* func);
```
Unregisters a previously registered callback.

```cpp
// Legacy delegate API (prefer CLEO_RegisterCallback with ScriptUnregister)
void WINAPI CLEO_AddScriptDeleteDelegate(FuncScriptDeleteDelegateT func);
void WINAPI CLEO_RemoveScriptDeleteDelegate(FuncScriptDeleteDelegateT func);
```
`FuncScriptDeleteDelegateT` is `void (*)(CRunningScript* script)`.

### Script Management

```cpp
BOOL WINAPI CLEO_IsScriptRunning(const CRunningScript* thread);
```
Returns TRUE if the given script is currently active and running.

```cpp
BOOL WINAPI CLEO_IsValidScriptPtr(const CRunningScript* thread);
```
Returns TRUE if the pointer refers to a valid script (main.scm, script.img, or CLEO). The script may be inactive or pending deletion.

```cpp
void WINAPI CLEO_GetScriptInfoStr(CRunningScript* thread, bool currLineInfo,
                                   char* buf, DWORD bufSize);
```
Writes a short human-readable description of the script into `buf` (for error/log messages). If `currLineInfo` is true, includes current line information.

```cpp
void WINAPI CLEO_GetScriptParamInfoStr(int idexOffset, char* buf, DWORD bufSize);
```
Writes info about the parameter at position `lastProcessed + idexOffset` into `buf` (index and name if available).

```cpp
DWORD WINAPI CLEO_GetScriptBaseRelativeOffset(const CRunningScript* script,
                                               const BYTE* codePos);
```
Returns the offset within the script source file for the given code position.

```cpp
eCLEO_Version WINAPI CLEO_GetScriptVersion(const CRunningScript* thread);
```
Returns the compatibility version of the script.

```cpp
void WINAPI CLEO_SetScriptVersion(CRunningScript* thread, eCLEO_Version version);
```
Sets the compatibility version for the script.

```cpp
LPCSTR WINAPI CLEO_GetScriptFilename(const CRunningScript* thread);
```
Returns the filename of the script, or `nullptr` if the script pointer is invalid.

```cpp
LPCSTR WINAPI CLEO_GetScriptWorkDir(const CRunningScript* thread);
```
Returns the current working directory of the script.

```cpp
void WINAPI CLEO_SetScriptWorkDir(CRunningScript* thread, const char* path);
```
Sets the base directory for relative paths used by the script. Supports virtual prefixes like `"cleo:"` or `"user:"`.

```cpp
DWORD WINAPI CLEO_GetCleoCallStackSize(CRunningScript* thread);
```
Returns the depth of the current `cleo_call` chain.

```cpp
void WINAPI CLEO_TerminateScript(CRunningScript* thread);
```
Immediately terminates the given script.

```cpp
CRunningScript* WINAPI CLEO_CreateCustomScript(CRunningScript* fromThread,
                                                const char* filePath, int label);
```
Creates a new custom script from a file. `fromThread` is the parent script, `label` is the entry offset.

```cpp
CRunningScript* WINAPI CLEO_GetLastCreatedCustomScript();
```
Returns the most recently created custom script.

```cpp
CRunningScript* WINAPI CLEO_GetScriptByName(const char* threadName,
                                              BOOL standardScripts,
                                              BOOL customScripts,
                                              DWORD resultIndex = 0);
```
Finds scripts by thread name. Increment `resultIndex` to find additional matches. Returns `nullptr` when no more found.

```cpp
CRunningScript* WINAPI CLEO_GetScriptByFilename(const char* path,
                                                  DWORD resultIndex = 0);
```
Finds scripts by filename (absolute, partial path, or just filename).

```cpp
BOOL WINAPI CLEO_GetScriptDebugMode(const CRunningScript* thread);
void WINAPI CLEO_SetScriptDebugMode(CRunningScript* thread, BOOL enabled);
```
Get or set whether debug mode features are enabled for a given script.

### Parameter Reading

These functions read opcode parameters and advance the script's instruction pointer.

```cpp
int WINAPI CLEO_GetOperandType(const CRunningScript* thread);
```
Peeks at the next parameter's data type without advancing. Returns `eDataType` as int.

```cpp
SCRIPT_VAR* WINAPI CLEO_GetPointerToScriptVariable(CRunningScript* thread);
```
Returns a pointer to the variable's data. Returns `nullptr` if the parameter is not a variable. Advances the script to the next parameter.

```cpp
void WINAPI CLEO_RetrieveOpcodeParams(CRunningScript* thread, int count);
```
Reads `count` parameters into the shared `opcodeParams` array.

```cpp
DWORD WINAPI CLEO_GetIntOpcodeParam(CRunningScript* thread);
```
Reads and returns one integer parameter.

```cpp
float WINAPI CLEO_GetFloatOpcodeParam(CRunningScript* thread);
```
Reads and returns one float parameter.

```cpp
LPCSTR WINAPI CLEO_ReadStringOpcodeParam(CRunningScript* thread,
                                          char* buff = nullptr, int buffSize = 0);
```
Reads a null-terminated string parameter into `buff` (clamped to `buffSize`). If no buffer is provided, an internal shared buffer is used. Returns pointer to the result buffer, or `nullptr` on failure.

```cpp
LPCSTR WINAPI CLEO_ReadStringPointerOpcodeParam(CRunningScript* thread,
                                                  char* buff = nullptr,
                                                  int buffSize = 0);
```
Similar to `CLEO_ReadStringOpcodeParam` but the returned pointer may differ from `buff` and point to the original data source (which can be longer than `buffSize`).

```cpp
void WINAPI CLEO_ReadStringParamWriteBuffer(CRunningScript* thread,
                                             char** outBuf, int* outBufSize,
                                             BOOL* outNeedsTerminator);
```
Gets info about a string parameter's write buffer for deferred writing. Advances to next param.

```cpp
char* WINAPI CLEO_ReadParamsFormatted(CRunningScript* thread, const char* format,
                                       char* buf = nullptr, int bufSize = 0);
```
Reads a format string and all variable arguments, producing formatted text. Consumes all var-arg params and the terminator.

### Parameter Writing

These functions write output values to opcode parameters.

```cpp
void WINAPI CLEO_RecordOpcodeParams(CRunningScript* thread, int count);
```
Writes `count` parameters from the shared `opcodeParams` array to the script's output variables.

```cpp
void WINAPI CLEO_SetIntOpcodeParam(CRunningScript* thread, DWORD value);
```
Writes one integer value to the next output parameter.

```cpp
void WINAPI CLEO_SetFloatOpcodeParam(CRunningScript* thread, float value);
```
Writes one float value to the next output parameter.

```cpp
void WINAPI CLEO_WriteStringOpcodeParam(CRunningScript* thread, const char* str);
```
Writes a string value to the next output parameter.

### Parameter Inspection (Peek / Skip)

```cpp
DWORD WINAPI CLEO_GetVarArgCount(CRunningScript* thread);
```
Returns the number of remaining variable arguments (not counting the terminator).

```cpp
DWORD WINAPI CLEO_PeekIntOpcodeParam(CRunningScript* thread);
```
Reads an integer parameter value without advancing the script position.

```cpp
float WINAPI CLEO_PeekFloatOpcodeParam(CRunningScript* thread);
```
Reads a float parameter value without advancing the script position.

```cpp
SCRIPT_VAR* WINAPI CLEO_PeekPointerToScriptVariable(CRunningScript* thread);
```
Gets pointer to a variable's data without advancing the script.

```cpp
void WINAPI CLEO_SkipOpcodeParams(CRunningScript* thread, int count);
```
Skips `count` parameters without reading them.

```cpp
void WINAPI CLEO_SkipUnusedVarArgs(CRunningScript* thread);
```
Skips all remaining variable arguments and the var-arg terminator. **Must be called** even when all params were read, to consume the terminator.

### Condition and Flow Control

```cpp
void WINAPI CLEO_SetThreadCondResult(CRunningScript* thread, BOOL result);
```
Sets the condition result flag for the script (used by condition opcodes).

```cpp
void WINAPI CLEO_ThreadJumpAtLabelPtr(CRunningScript* thread, int offset);
```
Jumps the script to the given label offset.

### File System and Paths

**Virtual path prefixes:**

| Prefix | Meaning |
|---|---|
| `root:` | Game root directory |
| `user:` | Game save directory |
| `.` | Current script directory |
| `cleo:` | `game\cleo` directory |
| `modules:` | `game\cleo\modules` directory |

```cpp
void WINAPI CLEO_ResolvePath(CRunningScript* thread, char* inOutPath, DWORD pathMaxLen);
```
Converts a virtual/relative path to an absolute filesystem path. Provides ModLoader compatibility. Should always be used when working with files.

```cpp
StringList WINAPI CLEO_ListDirectory(CRunningScript* thread, const char* searchPath,
                                      BOOL listDirs, BOOL listFiles);
```
Lists files/directories matching `searchPath` (supports wildcards). `thread` can be null. Returns a `StringList` that **must** be freed with `CLEO_StringListFree`.

```cpp
void WINAPI CLEO_StringListFree(StringList list);
```
Frees resources used by a `StringList` container.

```cpp
LPCSTR WINAPI CLEO_GetGameDirectory();
```
Returns the absolute game directory path (no trailing separator).

```cpp
LPCSTR WINAPI CLEO_GetUserDirectory();
```
Returns the absolute user files directory path (no trailing separator).

```cpp
LPCSTR WINAPI CLEO_GetLogDirectory();
```
Returns the absolute log files directory path (no trailing separator).

### Logging

```cpp
void WINAPI CLEO_Log(eLogLevel level, const char* msg);
```
Adds a message to the CLEO log file.

### Configuration

Read/write values from the plugin's `.cleo_config.ini` file. All values are stored in the `[Plugins]` section.

```cpp
int   WINAPI CLEO_GetConfigInt(const char* key, int defaultValue);
float WINAPI CLEO_GetConfigFloat(const char* key, float defaultValue);
DWORD WINAPI CLEO_GetConfigText(const char* key, const char* defaultValue,
                                 char* buffer, DWORD bufferSize);

BOOL WINAPI CLEO_SetConfigInt(const char* key, int value);
BOOL WINAPI CLEO_SetConfigFloat(const char* key, float value);
BOOL WINAPI CLEO_SetConfigText(const char* key, const char* value);
```

### Audio

```cpp
DWORD WINAPI CLEO_GetInternalAudioStream(CRunningScript* unused,
                                          DWORD scriptAudioStreamHandle);
```
Returns the BASS library `HSTREAM` handle for the given script audio stream. The `unused` parameter is ignored.

### Textures

```cpp
DWORD WINAPI CLEO_GetScriptTextureById(CRunningScript* thread, int id);
```
Returns an `RwTexture*` (as DWORD) for the texture associated with the given id in the script.

### Memory / SCM Data

```cpp
BYTE* WINAPI CLEO_GetScmMainData();
```
Returns a pointer to the main SCM script block. Supports limit adjusters.

```cpp
SCRIPT_VAR* WINAPI CLEO_GetOpcodeParamsArray();
```
Returns a pointer to the shared `SCRIPT_VAR[32] opcodeParams` array used by `CLEO_RetrieveOpcodeParams` and `CLEO_RecordOpcodeParams`.

```cpp
BYTE WINAPI CLEO_GetParamsHandledCount();
```
Returns the number of parameters already read/written since the current opcode handler was called.

**Global variables (extern):**

```cpp
extern SCRIPT_VAR*      opcodeParams;    // shared param array
extern SCRIPT_VAR*      missionLocals;   // mission local variables
extern CRunningScript*  staticThreads;   // linked list of scripts
```

---

## Utility Macros (CLEO_Utils.h)

`CLEO_Utils.h` provides convenience macros for use inside opcode handler functions. They perform automatic type validation, print warnings, and suspend scripts on critical errors.

**Important:** These macros expand to multiple statements. They cannot be used in single-line contexts without braces (e.g. a bare `if` body).

All macros assume the opcode handler parameter is named `thread` (the `CRunningScript*` argument).

### Logging Macros

```cpp
TRACE(format, ...)
```
Logs a message at `eLogLevel::Default`. Can be displayed on screen via `.cleo_config.ini`.

```cpp
LOG_WARNING(script, format, ...)
```
Logs at `eLogLevel::Error`. Not displayed for scripts in legacy mode.

```cpp
SHOW_ERROR(format, ...)
```
Displays a message box and logs at `eLogLevel::Error`.

### Condition Result

```cpp
OPCODE_CONDITION_RESULT(value)
```
Sets the condition result for the current script. Equivalent to `CLEO_SetThreadCondResult(thread, value)`.

### Parameter Skip / Peek Macros

```cpp
OPCODE_SKIP_PARAMS(count)
```
Skips `count` parameters without reading.

```cpp
OPCODE_SKIP_VARARG_PARAMS()
```
Skips all remaining variable arguments including the terminator.

```cpp
OPCODE_PEEK_PARAM_TYPE()
```
Returns the `eDataType` of the next parameter without advancing. Equivalent to `thread->PeekDataType()`.

```cpp
OPCODE_PEEK_VARARG_COUNT()
```
Returns the count of remaining variable arguments (not including the terminator).

### OPCODE_READ_PARAM_* Macros

Each macro reads one input parameter, validates its type, and suspends the script if the type is wrong.

**Usage pattern:** These macros are used as initializers in variable declarations.

```cpp
auto value = OPCODE_READ_PARAM_INT();
auto flag  = OPCODE_READ_PARAM_BOOL();
auto speed = OPCODE_READ_PARAM_FLOAT();
```

| Macro | C type | Validates as |
|---|---|---|
| `OPCODE_READ_PARAM_BOOL()` | `DWORD` (truthy) | integer |
| `OPCODE_READ_PARAM_INT8()` | `char` | integer |
| `OPCODE_READ_PARAM_UINT8()` | `BYTE` | integer |
| `OPCODE_READ_PARAM_INT16()` | `short` | integer |
| `OPCODE_READ_PARAM_UINT16()` | `WORD` | integer |
| `OPCODE_READ_PARAM_INT()` | `int` | integer |
| `OPCODE_READ_PARAM_UINT()` | `DWORD` | integer |
| `OPCODE_READ_PARAM_FLOAT()` | `float` | float (allows `0` as int) |
| `OPCODE_READ_PARAM_ANY32()` | `SCRIPT_VAR` | int or float |
| `OPCODE_READ_PARAM_PTR()` | `void*` | integer, validates non-null (> 0x10000) |
| `OPCODE_READ_PARAM_OBJECT_HANDLE()` | `DWORD` | integer, validates object pool |
| `OPCODE_READ_PARAM_PED_HANDLE()` | `DWORD` | integer, validates ped pool |
| `OPCODE_READ_PARAM_VEHICLE_HANDLE()` | `DWORD` | integer, validates vehicle pool |
| `OPCODE_READ_PARAM_PLAYER_ID()` | `DWORD` | integer, validates player id (-1, 0, 1) |

**String reading macros** -- these declare new variables:

```cpp
OPCODE_READ_PARAM_STRING(varName)
```
Reads a string parameter and creates a `const char* varName` pointing to a null-terminated string (buffered up to `MAX_STR_LEN` = 255 chars). Returns `OR_INTERRUPT` on failure.

```cpp
OPCODE_READ_PARAM_STRING_LEN(varName, maxLength)
```
Same as above but clamps text to `maxLength`.

```cpp
OPCODE_READ_PARAM_STRING_FORMATTED(varName)
```
Reads a format string argument followed by all var-args. Creates `char varName[]` containing the formatted text and `char* varNameOk` (nullptr on failure). Suspends on invalid format.

```cpp
OPCODE_READ_PARAMS_FORMATTED(format, varName)
```
Like `OPCODE_READ_PARAM_STRING_FORMATTED` but uses an externally provided `format` string. Reads only the var-args.

```cpp
OPCODE_READ_PARAM_FILEPATH(varName)
```
Reads a string, resolves it to an absolute path via `CLEO_ResolvePath`, and validates the path is inside game directories. Creates `const char* varName`. Suspends if path is outside allowed directories.

### OPCODE_WRITE_PARAM_* Macros

Each macro writes one output value to the next parameter and validates the target type.

```cpp
OPCODE_WRITE_PARAM_INT(myResult);
OPCODE_WRITE_PARAM_FLOAT(myFloat);
OPCODE_WRITE_PARAM_STRING(myString);
```

| Macro | Accepts | Validates target as |
|---|---|---|
| `OPCODE_WRITE_PARAM_BOOL(value)` | bool/int | int variable |
| `OPCODE_WRITE_PARAM_INT8(value)` | char | int variable |
| `OPCODE_WRITE_PARAM_UINT8(value)` | BYTE | int variable |
| `OPCODE_WRITE_PARAM_INT16(value)` | short | int variable |
| `OPCODE_WRITE_PARAM_UINT16(value)` | WORD | int variable |
| `OPCODE_WRITE_PARAM_INT(value)` | int | int variable |
| `OPCODE_WRITE_PARAM_UINT(value)` | DWORD | int variable |
| `OPCODE_WRITE_PARAM_FLOAT(value)` | float | float variable |
| `OPCODE_WRITE_PARAM_ANY32(value)` | any 32-bit | int or float variable |
| `OPCODE_WRITE_PARAM_STRING(value)` | `const char*` | string variable/buffer |
| `OPCODE_WRITE_PARAM_VAR_STRING(info, value)` | `StringParamBufferInfo`, `const char*` | pre-read string buffer |
| `OPCODE_WRITE_PARAM_PTR(value)` | pointer | int variable |

### OPCODE_READ_PARAM_OUTPUT_VAR_* Macros

For opcodes where output parameters appear before input arguments. These read the output target variable early so you can write to it later.

```cpp
auto resultVar = OPCODE_READ_PARAM_OUTPUT_VAR_INT();
// ... read input params, compute result ...
*resultVar = computedValue;
```

| Macro | Returns | Validates as |
|---|---|---|
| `OPCODE_READ_PARAM_OUTPUT_VAR_INT()` | `int*` | int variable |
| `OPCODE_READ_PARAM_OUTPUT_VAR_FLOAT()` | `float*` | float variable |
| `OPCODE_READ_PARAM_OUTPUT_VAR_ANY32()` | `SCRIPT_VAR*` | any variable |
| `OPCODE_READ_PARAM_OUTPUT_VAR_STRING()` | `StringParamBufferInfo` | string variable |

The `StringParamBufferInfo` struct:

```cpp
struct StringParamBufferInfo {
    char* data;             // pointer to output buffer
    int   size;             // buffer size
    BOOL  needTerminator;   // whether null terminator is required
};
```

Use `OPCODE_WRITE_PARAM_VAR_STRING(info, value)` to write to it later.

### Validation Macros

```cpp
OPCODE_VALIDATE_POINTER(x)
```
Suspends the script if `x` is at or below `MinValidAddress` (0x10000).

**Script suspension macros (internal use, but available):**

```cpp
SUSPEND(format, ...)         // unconditional: suspend + show error
SUSPEND_COMPAT(format, ...)  // only if StrictValidation=1 and script is not legacy
```

### Helper Functions

```cpp
static bool IsLegacyScript(CRunningScript* script);
```
Returns true if `CLEO_GetScriptVersion(script) < CLEO_VER_5`.

```cpp
static bool IsStrictValidation(CRunningScript* script);
```
Returns true if `StrictValidation=1` in config AND script is not legacy.

```cpp
static bool PluginCheckCleoVersion();
```
Checks that the running CLEO.asi is at least the version the plugin was compiled against. Shows an error and returns false if not. Requires the `TARGET_NAME` preprocessor define.

```cpp
static std::string ScriptInfoStr(CRunningScript* thread);
```
Returns a formatted string with script info (wraps `CLEO_GetScriptInfoStr`).

```cpp
static std::string GetParamInfo(int offset = 0);
```
Returns info about a parameter at position offset from the last processed one.

**Handle validation functions:**

| Function | Description |
|---|---|
| `IsObjectHandleValid(DWORD)` | Validates against the object pool |
| `IsPedHandleValid(DWORD)` | Validates against the ped pool |
| `IsVehicleHandleValid(DWORD)` | Validates against the vehicle pool |
| `IsPlayerIdValid(int)` | Valid ids are -1, 0, 1 |

**Path utility functions:**

| Function | Description |
|---|---|
| `FilepathNormalize(string&)` | Normalizes separators, collapses `..` references |
| `FilepathRemoveParent(string&, string_view)` | Strips a parent prefix from a path |
| `FilepathGetParent(string_view)` | Returns path without last element |
| `FilepathIsSafe(CRunningScript*, const char*)` | Checks path is inside game/user dirs |

---

## Utility Helper Functions (CLEO_Utils.h)

In addition to the macros above, `CLEO_Utils.h` provides standalone helper functions for string formatting, error display, script suspension, and memory patching. These are `static` functions in the `CLEO` namespace.

### String Formatting

```cpp
static std::string StringPrintfV(const char* format, va_list args);
```
Printf-style string formatting using a `va_list`. Internally calls `std::vsnprintf` twice: once to measure the required length, then again to write into a `std::string`. Returns an empty string on encoding error or zero-length result.

```cpp
static std::string StringPrintf(const char* format, ...);
```
Variadic wrapper around `StringPrintfV`. Accepts a printf-style format string and variable arguments, returns the formatted `std::string`.

**Example:**
```cpp
auto msg = CLEO::StringPrintf("Value is %d, name is %s", 42, "test");
// msg == "Value is 42, name is test"
```

### Error Display

```cpp
static void ShowError(const char* format, ...);
```
Formats a message with printf-style arguments, logs it at `eLogLevel::Error` via `TraceVArg`, then displays it in a **system-modal message box** with the caption `"CLEO v<version>"`. If the game is running in fullscreen mode, the window is temporarily minimized before showing the dialog and restored afterward. Use this for critical errors that require user attention.

### Script Suspension

```cpp
static OpcodeResult TrySuspendScript(
    CLEO::CRunningScript* thread,
    bool canBeDisabled,
    const char* format, ...);
```
Attempts to suspend a script that has encountered an error.

- If `thread` is not a valid CLEO script pointer (e.g. an ASI-based script), returns `OR_ERROR` because ASI scripts cannot be suspended.
- Otherwise, formats the error message, appends script info, calls `ShowError`, and sets `thread->WakeTime` to `0xFFFFFFFF` (infinite sleep).
- If `canBeDisabled` is true, appends a hint telling the user how to suppress the error in the future (change extension to `.cs4` for custom scripts, or set `MainScmLegacyMode=4` for main scripts).
- If the script is a mission script, resets the `bAlreadyRunningAMissionScript` flag so the mission can be restarted.
- Returns `OR_INTERRUPT` on success.

### Memory Patching

```cpp
class MemPatch
{
public:
    MemPatch();
    MemPatch(void* src, size_t size);
    void Apply() const;
    void* GetAddress() const;
};
```
Stores a backup of `size` bytes from memory address `src`. Calling `Apply()` restores the original bytes. Used to save original code before patching so it can be reverted later.

```cpp
static MemPatch MemPatchJump(size_t position, void* jumpTarget);
```
Writes a 5-byte **JMP** instruction (`0xE9`) at `position` that redirects execution to `jumpTarget`. Returns a `MemPatch` object containing the original 5 bytes, which can be restored by calling `Apply()`.

```cpp
static void* MemPatchCall(size_t position, void* newFunction);
```
Writes a 5-byte **CALL** instruction (`0xE8`) at `position` that calls `newFunction`. Returns a pointer to the **original** function that was previously called at that address (computed from the existing relative offset). This lets you chain or wrap existing function calls.

**Example:**
```cpp
// Redirect a jump
auto backup = CLEO::MemPatchJump(0x4A5B6C, MyHookFunction);
// Later, restore original code:
backup.Apply();

// Replace a call and keep reference to the original
auto originalFunc = CLEO::MemPatchCall(0x4A5B70, MyReplacementFunction);
```

### StringList Creation

```cpp
template <typename T>
static StringList CreateStringList(const T& container);
```
Converts any iterable container of `std::string` (e.g. `std::vector<std::string>`, `std::set<std::string>`) into a `StringList` struct. Each string is individually `malloc`-allocated (including null terminator), and the pointer array is also `malloc`-allocated. The caller is responsible for freeing the memory. Returns a `StringList` with `count` and `strings` fields set appropriately; returns an empty list (`count=0`, `strings=nullptr`) if the container is empty.

---

## Plugin Development Pattern

### Project Setup

Add to **Additional Include Directories**:

```
$(PLUGIN_SDK_DIR)\plugin_sa\
$(PLUGIN_SDK_DIR)\shared\game\
$(PLUGIN_SDK_DIR)\plugin_sa\game_sa\
```

Add to **Preprocessor Definitions**:

```
GTASA
TARGET_NAME=R"($(TargetName))"
```

Depending on which validation macros you use, you may need to add `CPools.cpp` from the GTA Plugin SDK to your project files.

### Plugin Skeleton

A CLEO plugin is a DLL with a `.cleo` extension. It links against `CLEO.lib` and uses the SDK headers.

```cpp
#include "CLEO.h"
#include "CLEO_Utils.h"

using namespace CLEO;

class MyPlugin
{
public:
    MyPlugin()
    {
        // Verify CLEO version is compatible
        if (!PluginCheckCleoVersion()) return;

        // Register opcodes
        CLEO_RegisterOpcode(0x2100, Opcode_MyCustomOpcode);

        // Register callbacks if needed
        CLEO_RegisterCallback(eCallbackId::ScriptsLoaded, OnScriptsLoaded);
    }

    static OpcodeResult __stdcall Opcode_MyCustomOpcode(CRunningScript* thread)
    {
        // Read input parameters
        auto value = OPCODE_READ_PARAM_INT();

        // Do work...
        int result = value * 2;

        // Write output parameters
        OPCODE_WRITE_PARAM_INT(result);

        return OR_CONTINUE;
    }

    static void WINAPI OnScriptsLoaded()
    {
        TRACE("MyPlugin: Scripts loaded!");
    }
} myPlugin;
```

### Registering Opcodes

**By number:**

```cpp
CLEO_RegisterOpcode(0x2100, MyHandler);
```

Opcode numbers in the range 0x0A8E-0x7FFF are available for plugins.

**By name (preferred for CLEO 5):**

```cpp
CLEO_RegisterCommand("MY_COMMAND", MyHandler);
```

This looks up the opcode number from `cleo\.CONFIG\sa.json` by command name, keeping your plugin independent of specific opcode numbers.

### Registering Commands by Name

When using `CLEO_RegisterCommand`, the command name must match an entry in the CLEO configuration file. This approach is preferred because it decouples plugins from hardcoded opcode numbers and avoids conflicts.

### Using Callbacks

```cpp
// Register
CLEO_RegisterCallback(eCallbackId::GameBegin, OnGameBegin);

// Callback implementation (signature must match the eCallbackId docs)
void WINAPI OnGameBegin(DWORD saveSlot)
{
    if (saveSlot == (DWORD)-1)
        TRACE("New game started");
    else
        TRACE("Game loaded from slot %d", saveSlot);
}

// Unregister when done
CLEO_UnregisterCallback(eCallbackId::GameBegin, OnGameBegin);
```

### Working with Strings

**Reading strings:**

```cpp
static OpcodeResult __stdcall Opcode_PrintString(CRunningScript* thread)
{
    // Creates const char* text pointing to the string value
    OPCODE_READ_PARAM_STRING(text);

    TRACE("Script says: %s", text);
    return OR_CONTINUE;
}
```

**Reading formatted strings (printf-style with var-args):**

```cpp
static OpcodeResult __stdcall Opcode_PrintFormatted(CRunningScript* thread)
{
    // Reads format string + all var-args, produces formatted result
    OPCODE_READ_PARAM_STRING_FORMATTED(text);

    TRACE("Formatted: %s", text);
    return OR_CONTINUE;
}
```

**Writing strings:**

```cpp
static OpcodeResult __stdcall Opcode_GetName(CRunningScript* thread)
{
    const char* name = "Hello";
    OPCODE_WRITE_PARAM_STRING(name);
    return OR_CONTINUE;
}
```

**Deferred string output (output var appears before inputs):**

```cpp
static OpcodeResult __stdcall Opcode_TransformString(CRunningScript* thread)
{
    // Read the output target first
    auto outputInfo = OPCODE_READ_PARAM_OUTPUT_VAR_STRING();

    // Then read input
    OPCODE_READ_PARAM_STRING(input);

    // Compute result
    std::string result = std::string(input) + "_transformed";

    // Write to the previously captured output target
    OPCODE_WRITE_PARAM_VAR_STRING(outputInfo, result.c_str());
    return OR_CONTINUE;
}
```

### Condition Opcodes

Opcodes that set a true/false condition result (used in `if` statements in scripts):

```cpp
static OpcodeResult __stdcall Opcode_IsValuePositive(CRunningScript* thread)
{
    auto value = OPCODE_READ_PARAM_INT();

    OPCODE_CONDITION_RESULT(value > 0);
    return OR_CONTINUE;
}
```

### Variable-Argument Opcodes

When an opcode accepts a variable number of arguments:

```cpp
static OpcodeResult __stdcall Opcode_SumValues(CRunningScript* thread)
{
    int sum = 0;
    DWORD argCount = OPCODE_PEEK_VARARG_COUNT();

    for (DWORD i = 0; i < argCount; i++)
    {
        sum += OPCODE_READ_PARAM_INT();
    }

    // MUST skip remaining var-args even if all were read (consumes terminator)
    OPCODE_SKIP_VARARG_PARAMS();

    OPCODE_WRITE_PARAM_INT(sum);
    return OR_CONTINUE;
}
```

---

## Constants

| Constant | Value | Description |
|---|---|---|
| `MAX_STR_LEN` | 0xFF (255) | Maximum length of a string parameter |
| `MinValidAddress` | 0x10000 | Minimum valid pointer (first 64KB reserved by Windows) |
| `CLEO_VERSION` | `0x05030000` | Current SDK version as packed DWORD |
| `CLEO_VERSION_STR` | `"5.3.0"` | Current SDK version as string |

## Virtual Path Prefixes

| Constant | Prefix | Description |
|---|---|---|
| `DIR_GAME` | `root:` | Game root directory |
| `DIR_USER` | `user:` | Game save/user files directory |
| `DIR_SCRIPT` | `.` | Current script's directory |
| `DIR_CLEO` | `cleo:` | `game\cleo` directory |
| `DIR_MODULES` | `modules:` | `game\cleo\modules` directory |
