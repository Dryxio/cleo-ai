# file Extension Opcodes

> 12 opcodes

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0B00` | DELETE_FILE | Deletes a file at the given path and returns true if the operation is successful |
| `0B01` | DELETE_DIRECTORY | Deletes a directory at the given path and returns true if the operation is succe |
| `0B02` | MOVE_FILE | Moves an existing file and returns true if the operation is successful |
| `0B03` | MOVE_DIRECTORY | Moves an existing directory and returns true if the operation is successful |
| `0B04` | COPY_FILE | Copies an existing file to a new file and returns true if the operation is succe |
| `0B05` | COPY_DIRECTORY | Copies an existing directory to a new directory and returns true if the operatio |
| `2300` | GET_FILE_POSITION | Gets current offset of read-write carret within the file stream |
| `2301` | READ_BLOCK_FROM_FILE | Reads data from file into buffer at specified address |
| `2302` | WRITE_BLOCK_TO_FILE | Writes data from memory address into file |
| `2303` | RESOLVE_FILEPATH | Resolves absolute filepath. Input path can be relative, starts with 'virtual pat |
| `2304` | GET_SCRIPT_FILENAME | Returns a file name or full file path of a script at the address (0A9F, 0AAA, 24 |
| `2305` | GET_FILE_WRITE_TIME | Gets last modification time of the file. On fail condition result is set to fals |

## Detailed Reference

### File

### `2300` GET_FILE_POSITION
Gets current offset of read-write carret within the file stream

**Class:** `File.GetPosition`

**Input:**
- `self: File`

**Output:**
- `position: int (variable)`

---

### `2301` READ_BLOCK_FROM_FILE
Reads data from file into buffer at specified address

**Class:** `File.ReadBlock`
**Flags:** condition

**Input:**
- `self: File`
- `size: int`
- `address: int`

---

### `2302` WRITE_BLOCK_TO_FILE
Writes data from memory address into file

**Class:** `File.WriteBlock`
**Flags:** condition

**Input:**
- `self: File`
- `size: int`
- `address: int`

---

### Fs

### `0B00` DELETE_FILE
Deletes a file at the given path and returns true if the operation is successful

**Class:** `Fs.DeleteFile`
**Flags:** static, condition

**Input:**
- `path: string`

---

### `0B01` DELETE_DIRECTORY
Deletes a directory at the given path and returns true if the operation is successful

**Class:** `Fs.DeleteDirectory`
**Flags:** static, condition

**Input:**
- `path: string`
- `recursive: bool`

---

### `0B02` MOVE_FILE
Moves an existing file and returns true if the operation is successful

**Class:** `Fs.MoveFile`
**Flags:** static, condition

**Input:**
- `fileName: string`
- `newFileName: string`

---

### `0B03` MOVE_DIRECTORY
Moves an existing directory and returns true if the operation is successful

**Class:** `Fs.MoveDirectory`
**Flags:** static, condition

**Input:**
- `dirPath: string`
- `newDirPath: string`

---

### `0B04` COPY_FILE
Copies an existing file to a new file and returns true if the operation is successful

**Class:** `Fs.CopyFile`
**Flags:** static, condition

**Input:**
- `fileName: string`
- `newFileName: string`

---

### `0B05` COPY_DIRECTORY
Copies an existing directory to a new directory and returns true if the operation is successful

**Class:** `Fs.CopyDirectory`
**Flags:** static, condition

**Input:**
- `dirPath: string`
- `newDirPath: string`

---

### `2303` RESOLVE_FILEPATH
Resolves absolute filepath. Input path can be relative, starts with 'virtual path' prefix or be already absolute filepath

**Class:** `Fs.ResolvePath`
**Flags:** static

**Input:**
- `path: string`

**Output:**
- `resolved: string (variable)`

---

### `2304` GET_SCRIPT_FILENAME
Returns a file name or full file path of a script at the address (0A9F, 0AAA, 2404). If the address is -1 then this script is used. If no script with a given pointer is found, then the condition result is set to false and output argument is not modified

**Class:** `Fs.GetScriptFilename`
**Flags:** static, condition

**Input:**
- `address: int`
- `fullPath: bool`

**Output:**
- `filenameOrPath: string (variable)`

---

### `2305` GET_FILE_WRITE_TIME
Gets last modification time of the file. On fail condition result is set to false, output parameters remain unchanged

**Class:** `Fs.GetFileWriteTime`
**Flags:** static, condition

**Input:**
- `fileName: string`

**Output:**
- `year: int (variable)`
- `month: int (variable)`
- `day: int (variable)`
- `hour: int (variable)`
- `minute: int (variable)`
- `second: int (variable)`
- `milisecond: int (variable)`

---
