# audio Extension Opcodes

> 26 opcodes

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0AAC` | LOAD_AUDIO_STREAM | Loads an audio file and creates a new audio stream (see 0AC1) |
| `0AAD` | SET_AUDIO_STREAM_STATE | Sets the state of the audio stream |
| `0AAE` | REMOVE_AUDIO_STREAM | Unloads the audio stream and frees the memory |
| `0AAF` | GET_AUDIO_STREAM_LENGTH | Gets the audio stream length in seconds |
| `0AB9` | GET_AUDIO_STREAM_STATE | Returns the state of the audio stream |
| `0ABB` | GET_AUDIO_STREAM_VOLUME | Returns the audio stream volume (from 0.0 to 1.0) |
| `0ABC` | SET_AUDIO_STREAM_VOLUME | Sets the audio stream volume (default is 1.0). Pauses/Starts stream playback if  |
| `0AC0` | SET_AUDIO_STREAM_LOOPED | Makes the audio stream repeat endlessly |
| `0AC1` | LOAD_3D_AUDIO_STREAM | Loads an audio file and creates a new 3d audio stream (see 0AAC) |
| `0AC2` | SET_PLAY_3D_AUDIO_STREAM_AT_COORDS | Sets sound source position to specific world location |
| `0AC3` | SET_PLAY_3D_AUDIO_STREAM_AT_OBJECT | Attaches sound source to the object |
| `0AC4` | SET_PLAY_3D_AUDIO_STREAM_AT_CHAR | Attaches sound source to the character |
| `0AC5` | SET_PLAY_3D_AUDIO_STREAM_AT_CAR | Attaches sound source to the vehicle |
| `2500` | IS_AUDIO_STREAM_PLAYING | Checks if audio stream is currently in 'play' state |
| `2501` | GET_AUDIO_STREAM_DURATION | Gets the audio stream total duration considering its speed (see 2505) |
| `2502` | GET_AUDIO_STREAM_SPEED | Gets audio stream playback speed multiplier |
| `2503` | SET_AUDIO_STREAM_SPEED | Sets audio stream playback speed multiplier |
| `2504` | SET_AUDIO_STREAM_VOLUME_WITH_TRANSITION | Changes stream volume with smooth transition |
| `2505` | SET_AUDIO_STREAM_SPEED_WITH_TRANSITION | Changes stream speed with smooth transition. Pauses/Starts stream playback if ne |
| `2506` | SET_AUDIO_STREAM_SOURCE_SIZE | Sets size of 3d audio stream sound source in the world. Volume will not decay wi |
| `2507` | GET_AUDIO_STREAM_PROGRESS | Gets audio stream playback progress as value from 0.0 to 1.0 |
| `2508` | SET_AUDIO_STREAM_PROGRESS | Sets audio stream playback position. Progress range is from 0.0 to 1.0 |
| `2509` | GET_AUDIO_STREAM_TYPE | Returns current volume settings type group of the stream |
| `250A` | SET_AUDIO_STREAM_TYPE | Sets which game's master volume settings the stream should follow |
| `250B` | GET_AUDIO_STREAM_PROGRESS_SECONDS | Returns current playback progress in seconds. Does not take in consideration cur |
| `250C` | SET_AUDIO_STREAM_PROGRESS_SECONDS | Sets current playback progress in seconds. Does not take in consideration curren |

## Detailed Reference

### AudioStream

### `0AAC` LOAD_AUDIO_STREAM
Loads an audio file and creates a new audio stream (see 0AC1)

**Class:** `AudioStream.Load`
**Flags:** constructor, condition

**Input:**
- `audioFileName: string`

**Output:**
- `handle: AudioStream (variable)`

---

### `0AAD` SET_AUDIO_STREAM_STATE
Sets the state of the audio stream

**Class:** `AudioStream.SetState`

**Input:**
- `self: AudioStream`
- `action: AudioStreamAction`

---

### `0AAE` REMOVE_AUDIO_STREAM
Unloads the audio stream and frees the memory

**Class:** `AudioStream.Remove`
**Flags:** destructor

**Input:**
- `self: AudioStream`

---

### `0AAF` GET_AUDIO_STREAM_LENGTH
Gets the audio stream length in seconds

**Class:** `AudioStream.GetLength`

**Input:**
- `self: AudioStream`

**Output:**
- `length: int (variable)`

---

### `0AB9` GET_AUDIO_STREAM_STATE
Returns the state of the audio stream

**Class:** `AudioStream.GetState`

**Input:**
- `self: AudioStream`

**Output:**
- `state: AudioStreamState (variable)`

---

### `0ABB` GET_AUDIO_STREAM_VOLUME
Returns the audio stream volume (from 0.0 to 1.0)

**Class:** `AudioStream.GetVolume`

**Input:**
- `self: AudioStream`

**Output:**
- `volume: float (variable)`

---

### `0ABC` SET_AUDIO_STREAM_VOLUME
Sets the audio stream volume (default is 1.0). Pauses/Starts stream playback if neccesarry

**Class:** `AudioStream.SetVolume`

**Input:**
- `self: AudioStream`
- `volume: float`

---

### `0AC0` SET_AUDIO_STREAM_LOOPED
Makes the audio stream repeat endlessly

**Class:** `AudioStream.SetLooped`

**Input:**
- `self: AudioStream`
- `state: bool`

---

### `2500` IS_AUDIO_STREAM_PLAYING
Checks if audio stream is currently in 'play' state

**Class:** `AudioStream.IsPlaying`
**Flags:** condition

**Input:**
- `self: AudioStream`

---

### `2501` GET_AUDIO_STREAM_DURATION
Gets the audio stream total duration considering its speed (see 2505)

**Class:** `AudioStream.GetDuration`

**Input:**
- `self: AudioStream`

**Output:**
- `seconds: float (variable)`

---

### `2502` GET_AUDIO_STREAM_SPEED
Gets audio stream playback speed multiplier

**Class:** `AudioStream.GetSpeed`

**Input:**
- `self: AudioStream`

**Output:**
- `speed: float (variable)`

---

### `2503` SET_AUDIO_STREAM_SPEED
Sets audio stream playback speed multiplier

**Class:** `AudioStream.SetSpeed`

**Input:**
- `self: AudioStream`
- `speed: float`

---

### `2504` SET_AUDIO_STREAM_VOLUME_WITH_TRANSITION
Changes stream volume with smooth transition

**Class:** `AudioStream.SetVolumeWithTransition`

**Input:**
- `self: AudioStream`
- `volume: float`
- `timeMs: int`

---

### `2505` SET_AUDIO_STREAM_SPEED_WITH_TRANSITION
Changes stream speed with smooth transition. Pauses/Starts stream playback if neccesarry

**Class:** `AudioStream.SetSpeedWithTransition`

**Input:**
- `self: AudioStream`
- `speed: float`
- `timeMs: int`

---

### `2507` GET_AUDIO_STREAM_PROGRESS
Gets audio stream playback progress as value from 0.0 to 1.0

**Class:** `AudioStream.GetProgress`

**Input:**
- `self: AudioStream`

**Output:**
- `progress: float (variable)`

---

### `2508` SET_AUDIO_STREAM_PROGRESS
Sets audio stream playback position. Progress range is from 0.0 to 1.0

**Class:** `AudioStream.SetProgress`

**Input:**
- `self: AudioStream`
- `progress: float`

---

### `2509` GET_AUDIO_STREAM_TYPE
Returns current volume settings type group of the stream

**Class:** `AudioStream.GetType`

**Input:**
- `self: AudioStream`

**Output:**
- `type: AudioStreamType (variable)`

---

### `250A` SET_AUDIO_STREAM_TYPE
Sets which game's master volume settings the stream should follow

**Class:** `AudioStream.SetType`

**Input:**
- `self: AudioStream`
- `type: AudioStreamType`

**Details:**

CLEO5 introduced concept of stream types:
* **None** - no automatic volume or speed corrections are applied (like in CLEO4)
* **Sfx** - automatically corrected by global SFX volume settings and in-game speed changes
* **Music** - automatically corrected by global music volume settings, muted if current in-game speed is not 1.0
* **UserInterface** - automatically corrected by global SFX volume settings, unaffected by in-game speed

New streams default to `UserInterface` type, except in compatibility mode (.cs4 extension) where they default to `None`.

---

### `250B` GET_AUDIO_STREAM_PROGRESS_SECONDS
Returns current playback progress in seconds. Does not take in consideration current stream's playback speed

**Class:** `AudioStream.GetProgressSeconds`

**Input:**
- `self: AudioStream`

**Output:**
- `progress: float (variable)`

---

### `250C` SET_AUDIO_STREAM_PROGRESS_SECONDS
Sets current playback progress in seconds. Does not take in consideration current stream's playback speed

**Class:** `AudioStream.SetProgressSeconds`

**Input:**
- `self: AudioStream`
- `progress: float`

---

### AudioStream3D

### `0AC1` LOAD_3D_AUDIO_STREAM
Loads an audio file and creates a new 3d audio stream (see 0AAC)

**Class:** `AudioStream3D.Load`
**Flags:** constructor, condition

**Input:**
- `audioFileName: string`

**Output:**
- `handle: AudioStream3D (variable)`

---

### `0AC2` SET_PLAY_3D_AUDIO_STREAM_AT_COORDS
Sets sound source position to specific world location

**Class:** `AudioStream3D.SetPlayAtCoords`

**Input:**
- `self: AudioStream3D`
- `x: float`
- `y: float`
- `z: float`

---

### `0AC3` SET_PLAY_3D_AUDIO_STREAM_AT_OBJECT
Attaches sound source to the object

**Class:** `AudioStream3D.SetPlayAtObject`

**Input:**
- `self: AudioStream3D`
- `object: Object`

---

### `0AC4` SET_PLAY_3D_AUDIO_STREAM_AT_CHAR
Attaches sound source to the character

**Class:** `AudioStream3D.SetPlayAtChar`

**Input:**
- `self: AudioStream3D`
- `char: Char`

---

### `0AC5` SET_PLAY_3D_AUDIO_STREAM_AT_CAR
Attaches sound source to the vehicle

**Class:** `AudioStream3D.SetPlayAtCar`

**Input:**
- `self: AudioStream3D`
- `car: Car`

---

### `2506` SET_AUDIO_STREAM_SOURCE_SIZE
Sets size of 3d audio stream sound source in the world. Volume will not decay within the specified distance

**Class:** `AudioStream3D.SetSourceSize`

**Input:**
- `self: AudioStream3D`
- `radius: float`

---
