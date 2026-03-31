# Audio Opcodes

> 24 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0394` | PLAY_MISSION_PASSED_TUNE | Plays an audio file with the specified ID from the Audio directory |
| `03CF` | LOAD_MISSION_AUDIO | Loads the file from the audio directory |
| `03D0` | HAS_MISSION_AUDIO_LOADED | Returns true if the mission audio requested with LOAD_MISSION_AUDIO has loaded |
| `03D1` | PLAY_MISSION_AUDIO | Plays the loaded sound (03CF) |
| `03D2` | HAS_MISSION_AUDIO_FINISHED | Returns true if the audio (03CF) is no longer playing |
| `03D7` | SET_MISSION_AUDIO_POSITION | Sets the location of the mission audio (03CF) where it can be heard |
| `040D` | CLEAR_MISSION_AUDIO | Unloads the mission audio (03CF), freeing game memory |
| `041E` | SET_RADIO_CHANNEL | Sets the current radio station that is playing, if the player is in a vehicle |
| `043C` | SET_MUSIC_DOES_FADE | Sets whether sounds should fade along with the screen |
| `051E` | GET_RADIO_CHANNEL | Returns the current radio station that is being played |
| `07B1` | GET_BEAT_PROXIMITY | Returns information about a beat offset from the current playback position of th |
| `0949` | ATTACH_MISSION_AUDIO_TO_CHAR | Sets the loaded audio to play at the char's location |
| `0952` | PRELOAD_BEAT_TRACK | Loads the soundtrack audio that is stored in the audio\streams\BEATS file |
| `0953` | GET_BEAT_TRACK_STATUS | Returns the status of the currenly active beat track (0954) |
| `0954` | PLAY_BEAT_TRACK | Plays the last soundtrack loaded by PRELOAD_BEAT_TRACK |
| `0955` | STOP_BEAT_TRACK | Stops any currently active beat track |
| `097A` | REPORT_MISSION_AUDIO_EVENT_AT_POSITION |  |
| `097B` | REPORT_MISSION_AUDIO_EVENT_AT_OBJECT |  |
| `097C` | ATTACH_MISSION_AUDIO_TO_OBJECT | Sets the loaded audio to play at the object's location |
| `0991` | PAUSE_CURRENT_BEAT_TRACK | Sets whether the loaded soundtrack is paused |
| `09F1` | REPORT_MISSION_AUDIO_EVENT_AT_CHAR |  |
| `09F7` | REPORT_MISSION_AUDIO_EVENT_AT_CAR | Plays the audio event at the car's position |
| `0A16` | ATTACH_MISSION_AUDIO_TO_CAR | Sets the loaded audio to play at the vehicle's location |
| `0A26` | SET_RADIO_TO_PLAYERS_FAVOURITE_STATION | Sets the radio station of the vehicle the player is currently in to the favourit |

## Detailed Reference

### `0394` PLAY_MISSION_PASSED_TUNE
Plays an audio file with the specified ID from the Audio directory

**Class:** `Audio.PlayMissionPassedTune`
**Flags:** static

**Input:**
- `soundId: int`

---

### `03CF` LOAD_MISSION_AUDIO
Loads the file from the audio directory

**Class:** `Audio.LoadMissionAudio`
**Flags:** static

**Input:**
- `slotId: MissionAudioSlot`
- `audioId: int`

**Details:**

This command loads a wav audio generally played during missions. HAS_MISSION_AUDIO_LOADED checks if it has been loaded, PLAY_MISSION_AUDIO plays it, and CLEAR_MISSION_AUDIO clears it.

---

### `03D0` HAS_MISSION_AUDIO_LOADED
Returns true if the mission audio requested with LOAD_MISSION_AUDIO has loaded

**Class:** `Audio.HasMissionAudioLoaded`
**Flags:** condition, static

**Input:**
- `slotId: MissionAudioSlot`

---

### `03D1` PLAY_MISSION_AUDIO
Plays the loaded sound (03CF)

**Class:** `Audio.PlayMissionAudio`
**Flags:** static

**Input:**
- `slotId: MissionAudioSlot`

---

### `03D2` HAS_MISSION_AUDIO_FINISHED
Returns true if the audio (03CF) is no longer playing

**Class:** `Audio.HasMissionAudioFinished`
**Flags:** condition, static

**Input:**
- `slotId: MissionAudioSlot`

---

### `03D7` SET_MISSION_AUDIO_POSITION
Sets the location of the mission audio (03CF) where it can be heard

**Class:** `Audio.SetMissionAudioPosition`
**Flags:** static

**Input:**
- `slotId: MissionAudioSlot`
- `x: float`
- `y: float`
- `z: float`

---

### `040D` CLEAR_MISSION_AUDIO
Unloads the mission audio (03CF), freeing game memory

**Class:** `Audio.ClearMissionAudio`
**Flags:** static

**Input:**
- `slotId: MissionAudioSlot`

---

### `041E` SET_RADIO_CHANNEL
Sets the current radio station that is playing, if the player is in a vehicle

**Class:** `Audio.SetRadioChannel`
**Flags:** static

**Input:**
- `channel: RadioChannel`

---

### `043C` SET_MUSIC_DOES_FADE
Sets whether sounds should fade along with the screen

**Class:** `Audio.SetMusicDoesFade`
**Flags:** static

**Input:**
- `state: bool`

---

### `051E` GET_RADIO_CHANNEL
Returns the current radio station that is being played

**Class:** `Audio.GetRadioChannel`
**Flags:** static

**Output:**
- `channel: RadioChannel (variable)`

---

### `07B1` GET_BEAT_PROXIMITY
Returns information about a beat offset from the current playback position of the active beat track (0954)

**Class:** `Audio.GetBeatProximity`
**Flags:** static

**Input:**
- `offset: int`

**Output:**
- `beatTime: int (variable)`
- `beatType: int (variable)`
- `beatIndex: int (variable)`

---

### `0949` ATTACH_MISSION_AUDIO_TO_CHAR
Sets the loaded audio to play at the char's location

**Class:** `Audio.AttachMissionAudioToChar`
**Flags:** static

**Input:**
- `slotId: MissionAudioSlot`
- `handle: Char`

---

### `0952` PRELOAD_BEAT_TRACK
Loads the soundtrack audio that is stored in the audio\streams\BEATS file

**Class:** `Audio.PreloadBeatTrack`
**Flags:** static

**Input:**
- `trackId: int`

**Details:**

This command loads the soundtrack audio that is stored in the `audio\streams\BEATS` file. The soundtrack can be played using PLAY_BEAT_TRACK and stopped using STOP_BEAT_TRACK. GET_BEAT_TRACK_STATUS gets the status of the soundtrack.

---

### `0953` GET_BEAT_TRACK_STATUS
Returns the status of the currenly active beat track (0954)

**Class:** `Audio.GetBeatTrackStatus`
**Flags:** static

**Output:**
- `status: CutsceneTrackStatus (variable)`

---

### `0954` PLAY_BEAT_TRACK
Plays the last soundtrack loaded by PRELOAD_BEAT_TRACK

**Class:** `Audio.PlayBeatTrack`
**Flags:** static

---

### `0955` STOP_BEAT_TRACK
Stops any currently active beat track

**Class:** `Audio.StopBeatTrack`
**Flags:** static

---

### `097A` REPORT_MISSION_AUDIO_EVENT_AT_POSITION

**Class:** `Audio.ReportMissionAudioEventAtPosition`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `soundId: ScriptSound`

---

### `097B` REPORT_MISSION_AUDIO_EVENT_AT_OBJECT

**Class:** `Audio.ReportMissionAudioEventAtObject`
**Flags:** static

**Input:**
- `handle: Object`
- `soundId: ScriptSound`

---

### `097C` ATTACH_MISSION_AUDIO_TO_OBJECT
Sets the loaded audio to play at the object's location

**Class:** `Audio.AttachMissionAudioToObject`
**Flags:** static

**Input:**
- `slotId: MissionAudioSlot`
- `handle: Object`

---

### `0991` PAUSE_CURRENT_BEAT_TRACK
Sets whether the loaded soundtrack is paused

**Class:** `Audio.PauseCurrentBeatTrack`
**Flags:** static

**Input:**
- `state: bool`

---

### `09F1` REPORT_MISSION_AUDIO_EVENT_AT_CHAR

**Class:** `Audio.ReportMissionAudioEventAtChar`
**Flags:** static

**Input:**
- `handle: Char`
- `soundId: ScriptSound`

---

### `09F7` REPORT_MISSION_AUDIO_EVENT_AT_CAR
Plays the audio event at the car's position

**Class:** `Audio.ReportMissionAudioEventAtCar`
**Flags:** static

**Input:**
- `handle: Car`
- `soundId: ScriptSound`

---

### `0A16` ATTACH_MISSION_AUDIO_TO_CAR
Sets the loaded audio to play at the vehicle's location

**Class:** `Audio.AttachMissionAudioToCar`
**Flags:** static

**Input:**
- `slotId: MissionAudioSlot`
- `handle: Car`

---

### `0A26` SET_RADIO_TO_PLAYERS_FAVOURITE_STATION
Sets the radio station of the vehicle the player is currently in to the favourite station, retrieved from the stats (ID 326)

**Class:** `Audio.SetRadioToPlayersFavouriteStation`
**Flags:** static

---
