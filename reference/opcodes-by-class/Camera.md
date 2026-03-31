# Camera Opcodes

> 51 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0003` | SHAKE_CAM | Shakes the camera with the given intensity |
| `00C2` | IS_POINT_ON_SCREEN | Returns true if any part of the radius of the specified point is visible on scre |
| `0158` | POINT_CAMERA_AT_CAR | Attaches the camera to the specified vehicle |
| `0159` | POINT_CAMERA_AT_CHAR | Attaches the camera to the specified character |
| `015A` | RESTORE_CAMERA | Restores the camera to its usual position |
| `015F` | SET_FIXED_CAMERA_POSITION | Sets the fixed camera's position and up vector offset |
| `0160` | POINT_CAMERA_AT_POINT | Points the camera at the specified location and applies the position set by 0159 |
| `0169` | SET_FADING_COLOUR | Sets the RGB color of the fade command (016A) |
| `016A` | DO_FADE | Fades the screen for the specified time |
| `016B` | GET_FADING_STATUS | Returns true if the screen is fading (016A) |
| `02EB` | RESTORE_CAMERA_JUMPCUT | Restores the camera, putting it back behind the player |
| `032A` | SET_CAMERA_ZOOM | Sets how far behind the camera is from the player |
| `0373` | SET_CAMERA_BEHIND_PLAYER | Puts the camera behind the player |
| `03C8` | SET_CAMERA_IN_FRONT_OF_PLAYER | Puts the camera in front of the player, pointing towards the player |
| `041D` | SET_NEAR_CLIP | Sets camera minimum drawing distance |
| `0454` | GET_DEBUG_CAMERA_COORDINATES | Returns the debug camera position |
| `0460` | SET_INTERPOLATION_PARAMETERS | Sets how long the camera transition will last |
| `0463` | GET_DEBUG_CAMERA_POINT_AT | Stores the location the debug camera is pointing to |
| `0679` | ATTACH_CAMERA_TO_VEHICLE | Keeps the camera relative to the car with the specified offset |
| `067A` | ATTACH_CAMERA_TO_VEHICLE_LOOK_AT_VEHICLE | Puts the camera on the vehicle like in 0679 |
| `067B` | ATTACH_CAMERA_TO_VEHICLE_LOOK_AT_CHAR | Attaches the camera to the vehicle and points it at the specified character |
| `067C` | ATTACH_CAMERA_TO_CHAR | Keeps the camera relative to the char with the specified offset |
| `067D` | ATTACH_CAMERA_TO_CHAR_LOOK_AT_VEHICLE |  |
| `067E` | ATTACH_CAMERA_TO_CHAR_LOOK_AT_CHAR | Puts the camera on the character like with 067C |
| `068D` | GET_ACTIVE_CAMERA_COORDINATES | Stores the cameras coordinates |
| `068E` | GET_ACTIVE_CAMERA_POINT_AT | Gets the coordinates the camera is pointing to |
| `06E0` | SET_TWO_PLAYER_CAMERA_MODE | Enables the cooperative camera mode |
| `0801` | GET_CAMERA_FOV | Returns the cameras field of view |
| `0822` | SET_FIRST_PERSON_IN_CAR_CAMERA_MODE | Enables vehicle bumper view for the camera |
| `0834` | DO_CAMERA_BUMP | Bumps the camera in the specified direction as if it had collided |
| `0920` | CAMERA_SET_VECTOR_TRACK | Makes the camera point at the first coordinates and then rotate to point at the  |
| `0922` | CAMERA_SET_LERP_FOV | Sets the cameras zoom factors |
| `0924` | SET_DARKNESS_EFFECT | Darkens the game |
| `0925` | CAMERA_RESET_NEW_SCRIPTABLES | Stops the camera propagating, interpolating, shaking and zooming |
| `092F` | CAMERA_PERSIST_TRACK | Locks the camera target point in position after propagating |
| `0930` | CAMERA_PERSIST_POS | Locks the cameras position |
| `0931` | CAMERA_PERSIST_FOV | Locks the zoom level after the camera has finished zooming |
| `0933` | CAMERA_IS_VECTOR_MOVE_RUNNING | Returns true if the camera is moving in position |
| `0934` | CAMERA_IS_VECTOR_TRACK_RUNNING | Returns true if the camera is moving in angle |
| `0936` | CAMERA_SET_VECTOR_MOVE | Puts the camera at the position of the first passed coordinates and moves it to  |
| `093D` | SET_CINEMA_CAMERA | Locks the camera on cinematic vehicle mode |
| `0944` | SET_CAMERA_IN_FRONT_OF_CHAR | Puts the camera in front of the specified character |
| `099C` | CAMERA_SET_SHAKE_SIMULATION_SIMPLE | Jiggles the camera in a variety of different ways |
| `09AD` | SET_PLAYER_IN_CAR_CAMERA_MODE | Changes the camera mode on the current vehicle, just like when the user presses  |
| `09EC` | ALLOW_FIXED_CAMERA_COLLISION | Makes the camera remain behind the player when in any garage |
| `09EF` | SET_VEHICLE_CAMERA_TWEAK | Sets the position the camera automatically moves to while driving a vehicle of t |
| `09F0` | RESET_VEHICLE_CAMERA_TWEAK | Resets any changes made with 09EF |
| `0A1E` | TAKE_PHOTO | Takes a screenshot of the screen without any HUD elements and stores the file in |
| `0A25` | SET_CAMERA_POSITION_UNFIXED | Sets the position of the camera to an offset of the targeted entity |
| `0A2F` | SET_PHOTO_CAMERA_EFFECT | Puts the camera in first-person mode if the player is holding a weapon with a fi |
| `0A39` | GET_PLAYER_IN_CAR_CAMERA_MODE | Gets the players chosen camera mode of the current vehicle |

## Detailed Reference

### `0003` SHAKE_CAM
Shakes the camera with the given intensity

**Class:** `Camera.Shake`
**Flags:** static

**Input:**
- `intensity: int`

---

### `00C2` IS_POINT_ON_SCREEN
Returns true if any part of the radius of the specified point is visible on screen

**Class:** `Camera.IsPointOnScreen`
**Flags:** condition, static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`

---

### `0158` POINT_CAMERA_AT_CAR
Attaches the camera to the specified vehicle

**Class:** `Camera.PointAtCar`
**Flags:** static

**Input:**
- `vehicle: Car`
- `mode: CameraMode`
- `switchStyle: SwitchType`

---

### `0159` POINT_CAMERA_AT_CHAR
Attaches the camera to the specified character

**Class:** `Camera.PointAtChar`
**Flags:** static

**Input:**
- `char: Char`
- `mode: CameraMode`
- `switchStyle: SwitchType`

---

### `015A` RESTORE_CAMERA
Restores the camera to its usual position

**Class:** `Camera.Restore`
**Flags:** static

---

### `015F` SET_FIXED_CAMERA_POSITION
Sets the fixed camera's position and up vector offset

**Class:** `Camera.SetFixedPosition`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `upVecOffsetX: float`
- `upVecOffsetY: float`
- `upVecOffsetZ: float`

---

### `0160` POINT_CAMERA_AT_POINT
Points the camera at the specified location and applies the position set by 0159

**Class:** `Camera.PointAtPoint`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `switchStyle: SwitchType`

---

### `0169` SET_FADING_COLOUR
Sets the RGB color of the fade command (016A)

**Class:** `Camera.SetFadingColor`
**Flags:** static

**Input:**
- `r: int`
- `g: int`
- `b: int`

---

### `016A` DO_FADE
Fades the screen for the specified time

**Class:** `Camera.DoFade`
**Flags:** static

**Input:**
- `time: int`
- `direction: Fade`

---

### `016B` GET_FADING_STATUS
Returns true if the screen is fading (016A)

**Class:** `Camera.GetFadingStatus`
**Flags:** condition, static

---

### `02EB` RESTORE_CAMERA_JUMPCUT
Restores the camera, putting it back behind the player

**Class:** `Camera.RestoreJumpcut`
**Flags:** static

---

### `032A` SET_CAMERA_ZOOM
Sets how far behind the camera is from the player

**Class:** `Camera.SetZoom`
**Flags:** static

**Input:**
- `zoom: int`

---

### `0373` SET_CAMERA_BEHIND_PLAYER
Puts the camera behind the player

**Class:** `Camera.SetBehindPlayer`
**Flags:** static

---

### `03C8` SET_CAMERA_IN_FRONT_OF_PLAYER
Puts the camera in front of the player, pointing towards the player

**Class:** `Camera.SetInFrontOfPlayer`
**Flags:** static

---

### `041D` SET_NEAR_CLIP
Sets camera minimum drawing distance

**Class:** `Camera.SetNearClip`
**Flags:** static

**Input:**
- `distance: float`

---

### `0454` GET_DEBUG_CAMERA_COORDINATES
Returns the debug camera position

**Class:** `Camera.GetDebugCoordinates`
**Flags:** static

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0460` SET_INTERPOLATION_PARAMETERS
Sets how long the camera transition will last

**Class:** `Camera.SetInterpolationParameters`
**Flags:** static

**Input:**
- `interpolationToStopMoving: float`
- `time: int`

---

### `0463` GET_DEBUG_CAMERA_POINT_AT
Stores the location the debug camera is pointing to

**Class:** `Camera.GetDebugPointAt`
**Flags:** static

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0679` ATTACH_CAMERA_TO_VEHICLE
Keeps the camera relative to the car with the specified offset

**Class:** `Camera.AttachToVehicle`
**Flags:** static

**Input:**
- `handle: Car`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `xRotation: float`
- `yRotation: float`
- `zRotation: float`
- `tilt: float`
- `switchStyle: SwitchType`

---

### `067A` ATTACH_CAMERA_TO_VEHICLE_LOOK_AT_VEHICLE
Puts the camera on the vehicle like in 0679

**Class:** `Camera.AttachToVehicleLookAtVehicle`
**Flags:** static

**Input:**
- `handle: Car`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `vehicle: Car`
- `tilt: float`
- `switchStyle: SwitchType`

---

### `067B` ATTACH_CAMERA_TO_VEHICLE_LOOK_AT_CHAR
Attaches the camera to the vehicle and points it at the specified character

**Class:** `Camera.AttachToVehicleLookAtChar`
**Flags:** static

**Input:**
- `car: Car`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `char: Char`
- `tilt: float`
- `switchStyle: SwitchType`

---

### `067C` ATTACH_CAMERA_TO_CHAR
Keeps the camera relative to the char with the specified offset

**Class:** `Camera.AttachToChar`
**Flags:** static

**Input:**
- `handle: Char`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `xRotation: float`
- `yRotation: float`
- `zRotation: float`
- `tilt: float`
- `switchStyle: SwitchType`

---

### `067D` ATTACH_CAMERA_TO_CHAR_LOOK_AT_VEHICLE

**Class:** `Camera.AttachToCharLookAtVehicle`
**Flags:** static

**Input:**
- `char: Char`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `vehicle: Car`
- `tilt: float`
- `switchStyle: SwitchType`

---

### `067E` ATTACH_CAMERA_TO_CHAR_LOOK_AT_CHAR
Puts the camera on the character like with 067C

**Class:** `Camera.AttachToCharLookAtChar`
**Flags:** static

**Input:**
- `handle: Char`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `char: Char`
- `tilt: float`
- `switchStyle: SwitchType`

---

### `068D` GET_ACTIVE_CAMERA_COORDINATES
Stores the cameras coordinates

**Class:** `Camera.GetActiveCoordinates`
**Flags:** static

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `068E` GET_ACTIVE_CAMERA_POINT_AT
Gets the coordinates the camera is pointing to

**Class:** `Camera.GetActivePointAt`
**Flags:** static

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `06E0` SET_TWO_PLAYER_CAMERA_MODE
Enables the cooperative camera mode

**Class:** `Camera.SetTwoPlayerMode`
**Flags:** static

**Input:**
- `state: bool`

---

### `0801` GET_CAMERA_FOV
Returns the cameras field of view

**Class:** `Camera.GetFov`
**Flags:** static

**Output:**
- `fov: float (variable)`

---

### `0822` SET_FIRST_PERSON_IN_CAR_CAMERA_MODE
Enables vehicle bumper view for the camera

**Class:** `Camera.SetFirstPersonInCarMode`
**Flags:** static

**Input:**
- `state: bool`

---

### `0834` DO_CAMERA_BUMP
Bumps the camera in the specified direction as if it had collided

**Class:** `Camera.DoBump`
**Flags:** static

**Input:**
- `xOffset: float`
- `yOffset: float`

---

### `0920` CAMERA_SET_VECTOR_TRACK
Makes the camera point at the first coordinates and then rotate to point at the second coordinates

**Class:** `Camera.SetVectorTrack`
**Flags:** static

**Input:**
- `fromX: float`
- `fromY: float`
- `fromZ: float`
- `toX: float`
- `toY: float`
- `toZ: float`
- `time: int`
- `ease: bool`

---

### `0922` CAMERA_SET_LERP_FOV
Sets the cameras zoom factors

**Class:** `Camera.SetLerpFov`
**Flags:** static

**Input:**
- `from: float`
- `to: float`
- `time: int`
- `ease: bool`

---

### `0924` SET_DARKNESS_EFFECT
Darkens the game

**Class:** `Camera.SetDarknessEffect`
**Flags:** static

**Input:**
- `enable: bool`
- `pitchBlack: int`

---

### `0925` CAMERA_RESET_NEW_SCRIPTABLES
Stops the camera propagating, interpolating, shaking and zooming

**Class:** `Camera.ResetNewScriptables`
**Flags:** static

---

### `092F` CAMERA_PERSIST_TRACK
Locks the camera target point in position after propagating

**Class:** `Camera.PersistTrack`
**Flags:** static

**Input:**
- `state: bool`

---

### `0930` CAMERA_PERSIST_POS
Locks the cameras position

**Class:** `Camera.PersistPos`
**Flags:** static

**Input:**
- `state: bool`

---

### `0931` CAMERA_PERSIST_FOV
Locks the zoom level after the camera has finished zooming

**Class:** `Camera.PersistFov`
**Flags:** static

**Input:**
- `state: bool`

---

### `0933` CAMERA_IS_VECTOR_MOVE_RUNNING
Returns true if the camera is moving in position

**Class:** `Camera.IsVectorMoveRunning`
**Flags:** condition, static

---

### `0934` CAMERA_IS_VECTOR_TRACK_RUNNING
Returns true if the camera is moving in angle

**Class:** `Camera.IsVectorTrackRunning`
**Flags:** condition, static

---

### `0936` CAMERA_SET_VECTOR_MOVE
Puts the camera at the position of the first passed coordinates and moves it to the second passed coordinates

**Class:** `Camera.SetVectorMove`
**Flags:** static

**Input:**
- `fromX: float`
- `fromY: float`
- `fromZ: float`
- `toX: float`
- `toY: float`
- `toZ: float`
- `time: int`
- `ease: bool`

---

### `093D` SET_CINEMA_CAMERA
Locks the camera on cinematic vehicle mode

**Class:** `Camera.SetCinema`
**Flags:** static

**Input:**
- `state: bool`

---

### `0944` SET_CAMERA_IN_FRONT_OF_CHAR
Puts the camera in front of the specified character

**Class:** `Camera.SetInFrontOfChar`
**Flags:** static

**Input:**
- `handle: Char`

---

### `099C` CAMERA_SET_SHAKE_SIMULATION_SIMPLE
Jiggles the camera in a variety of different ways

**Class:** `Camera.SetShakeSimulationSimple`
**Flags:** static

**Input:**
- `type: int`
- `timeInMs: float`
- `intensity: float`

---

### `09AD` SET_PLAYER_IN_CAR_CAMERA_MODE
Changes the camera mode on the current vehicle, just like when the user presses the 'change view' key

**Class:** `Camera.SetPlayerInCarMode`
**Flags:** static

**Input:**
- `mode: int`

---

### `09EC` ALLOW_FIXED_CAMERA_COLLISION
Makes the camera remain behind the player when in any garage

**Class:** `Camera.AllowFixedCollision`
**Flags:** static

**Input:**
- `state: bool`

---

### `09EF` SET_VEHICLE_CAMERA_TWEAK
Sets the position the camera automatically moves to while driving a vehicle of the specified type

**Class:** `Camera.SetVehicleTweak`
**Flags:** static

**Input:**
- `modelId: model_vehicle`
- `distance: float`
- `altitude: float`
- `angle: float`

---

### `09F0` RESET_VEHICLE_CAMERA_TWEAK
Resets any changes made with 09EF

**Class:** `Camera.ResetVehicleTweak`
**Flags:** static

---

### `0A1E` TAKE_PHOTO
Takes a screenshot of the screen without any HUD elements and stores the file in the "GTA San Andreas User FilesGallery" folder

**Class:** `Camera.TakePhoto`
**Flags:** static

**Input:**
- `_p1: bool`

---

### `0A25` SET_CAMERA_POSITION_UNFIXED
Sets the position of the camera to an offset of the targeted entity

**Class:** `Camera.SetPositionUnfixed`
**Flags:** static

**Input:**
- `xOffset: float`
- `yOffset: float`

---

### `0A2F` SET_PHOTO_CAMERA_EFFECT
Puts the camera in first-person mode if the player is holding a weapon with a first-person shooting mode (such as a sniper rifle or camera)

**Class:** `Camera.SetPhotoEffect`
**Flags:** static

**Input:**
- `state: bool`

---

### `0A39` GET_PLAYER_IN_CAR_CAMERA_MODE
Gets the players chosen camera mode of the current vehicle

**Class:** `Camera.GetPlayerInCarMode`
**Flags:** static

**Output:**
- `mode: int (variable)`

---
