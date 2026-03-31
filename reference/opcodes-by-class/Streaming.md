# Streaming Opcodes

> 37 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `023C` | LOAD_SPECIAL_CHARACTER | Requests a special character's model to be loaded into the specified slot |
| `023D` | HAS_SPECIAL_CHARACTER_LOADED | Returns true if the special character's model (023C) is available for creation |
| `0247` | REQUEST_MODEL | Requests a new model to load |
| `0248` | HAS_MODEL_LOADED | Returns true if the model is available for creation |
| `0249` | MARK_MODEL_AS_NO_LONGER_NEEDED | Releases the specified model, freeing game memory |
| `0296` | UNLOAD_SPECIAL_CHARACTER | Releases the special character (023C), freeing game memory |
| `038B` | LOAD_ALL_MODELS_NOW | Loads any requested models (0247 or 0353) synchronously |
| `03AF` | SWITCH_STREAMING | Sets the streaming of additional models like peds, cars, and maps |
| `03CB` | LOAD_SCENE | Starts loading a specific location, just like if the player was there, removing  |
| `0488` | IS_MODEL_AVAILABLE | Returns true if the specified model exists in the loaded  |
| `04BB` | SET_AREA_VISIBLE | Sets the visibility of an interior area |
| `04E4` | REQUEST_COLLISION | Reloads the area at the specified coordinates |
| `04ED` | REQUEST_ANIMATION | Loads the specified IFP File |
| `04EE` | HAS_ANIMATION_LOADED | Returns true if the specified IFP file is loaded |
| `04EF` | REMOVE_ANIMATION | Releases the specified IFP file, freeing game memory |
| `06DA` | MARK_MISSION_TRAINS_AS_NO_LONGER_NEEDED | Marks the train as no longer needed by the script, allowing it to be deleted by  |
| `06E6` | GET_VEHICLE_MOD_TYPE | Returns a slot the upgrade model is for |
| `06E9` | REQUEST_VEHICLE_MOD | Loads the upgrade model and any associated models |
| `06EA` | HAS_VEHICLE_MOD_LOADED | Returns true if the vehicle upgrade model has loaded |
| `06EB` | MARK_VEHICLE_MOD_AS_NO_LONGER_NEEDED | Marks the vehicle upgrade model as no longer needed, allowing it to be unloaded  |
| `0771` | CUSTOM_PLATE_DESIGN_FOR_NEXT_CAR | Sets the town ID of the license plate which is created on the specified model, a |
| `0776` | REQUEST_IPL |  |
| `0777` | REMOVE_IPL |  |
| `0778` | REMOVE_IPL_DISCREETLY |  |
| `077E` | GET_AREA_VISIBLE | Gets the current interior ID |
| `07C0` | REQUEST_CAR_RECORDING | Loads the specified car recording |
| `07C1` | HAS_CAR_RECORDING_BEEN_LOADED | Returns true if the car recording has finished loading |
| `07DE` | IS_MODEL_IN_CDIMAGE | Returns true if a file for the model exists |
| `07E4` | GET_MODEL_DIMENSIONS |  |
| `081E` | IS_THIS_MODEL_A_BOAT | Returns true if the model is the model of a boat |
| `081F` | IS_THIS_MODEL_A_PLANE | Returns true if the model is the model of a plane |
| `0820` | IS_THIS_MODEL_A_HELI | Returns true if the model is the model of a helicopter |
| `0873` | REMOVE_CAR_RECORDING | Unloads the car recording |
| `08E8` | ATTACH_ANIMS_TO_MODEL | Sets an animation pack to be loaded along with the specified model |
| `09B2` | GET_RANDOM_CAR_MODEL_IN_MEMORY |  |
| `0A01` | IS_THIS_MODEL_A_CAR | Returns true if a valid car model is passed |
| `0A0B` | LOAD_SCENE_IN_DIRECTION |  |

## Detailed Reference

### `023C` LOAD_SPECIAL_CHARACTER
Requests a special character's model to be loaded into the specified slot

**Class:** `Streaming.LoadSpecialCharacter`
**Flags:** static

**Input:**
- `slotId: int`
- `modelName: string`

---

### `023D` HAS_SPECIAL_CHARACTER_LOADED
Returns true if the special character's model (023C) is available for creation

**Class:** `Streaming.HasSpecialCharacterLoaded`
**Flags:** condition, static

**Input:**
- `slotId: int`

---

### `0247` REQUEST_MODEL
Requests a new model to load

**Class:** `Streaming.RequestModel`
**Flags:** static

**Input:**
- `modelId: model_any`

---

### `0248` HAS_MODEL_LOADED
Returns true if the model is available for creation

**Class:** `Streaming.HasModelLoaded`
**Flags:** condition, static

**Input:**
- `modelId: model_any`

---

### `0249` MARK_MODEL_AS_NO_LONGER_NEEDED
Releases the specified model, freeing game memory

**Class:** `Streaming.MarkModelAsNoLongerNeeded`
**Flags:** static

**Input:**
- `modelId: model_any`

---

### `0296` UNLOAD_SPECIAL_CHARACTER
Releases the special character (023C), freeing game memory

**Class:** `Streaming.UnloadSpecialCharacter`
**Flags:** static

**Input:**
- `slotId: int`

---

### `038B` LOAD_ALL_MODELS_NOW
Loads any requested models (0247 or 0353) synchronously

**Class:** `Streaming.LoadAllModelsNow`
**Flags:** static

---

### `03AF` SWITCH_STREAMING
Sets the streaming of additional models like peds, cars, and maps

**Class:** `Streaming.Switch`
**Flags:** static

**Input:**
- `state: bool`

---

### `03CB` LOAD_SCENE
Starts loading a specific location, just like if the player was there, removing LOD textures

**Class:** `Streaming.LoadScene`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`

---

### `0488` IS_MODEL_AVAILABLE
Returns true if the specified model exists in the loaded 

**Class:** `Streaming.IsModelAvailable`
**Flags:** condition, static

**Input:**
- `modelId: model_any`

---

### `04BB` SET_AREA_VISIBLE
Sets the visibility of an interior area

**Class:** `Streaming.SetAreaVisible`
**Flags:** static

**Input:**
- `areaId: int`

---

### `04E4` REQUEST_COLLISION
Reloads the area at the specified coordinates

**Class:** `Streaming.RequestCollision`
**Flags:** static

**Input:**
- `x: float`
- `y: float`

---

### `04ED` REQUEST_ANIMATION
Loads the specified IFP File

**Class:** `Streaming.RequestAnimation`
**Flags:** static

**Input:**
- `animationFile: string`

---

### `04EE` HAS_ANIMATION_LOADED
Returns true if the specified IFP file is loaded

**Class:** `Streaming.HasAnimationLoaded`
**Flags:** condition, static

**Input:**
- `animationFile: string`

---

### `04EF` REMOVE_ANIMATION
Releases the specified IFP file, freeing game memory

**Class:** `Streaming.RemoveAnimation`
**Flags:** static

**Input:**
- `animationFile: string`

---

### `06DA` MARK_MISSION_TRAINS_AS_NO_LONGER_NEEDED
Marks the train as no longer needed by the script, allowing it to be deleted by the game

**Class:** `Streaming.MarkMissionTrainsAsNoLongerNeeded`
**Flags:** static

---

### `06E6` GET_VEHICLE_MOD_TYPE
Returns a slot the upgrade model is for

**Class:** `Streaming.GetVehicleModType`
**Flags:** static

**Input:**
- `modelId: model_object`

**Output:**
- `slotId: ModSlot (variable)`

---

### `06E9` REQUEST_VEHICLE_MOD
Loads the upgrade model and any associated models

**Class:** `Streaming.RequestVehicleMod`
**Flags:** static

**Input:**
- `modelId: model_object`

---

### `06EA` HAS_VEHICLE_MOD_LOADED
Returns true if the vehicle upgrade model has loaded

**Class:** `Streaming.HasVehicleModLoaded`
**Flags:** condition, static

**Input:**
- `modelId: model_object`

---

### `06EB` MARK_VEHICLE_MOD_AS_NO_LONGER_NEEDED
Marks the vehicle upgrade model as no longer needed, allowing it to be unloaded by the streamer

**Class:** `Streaming.MarkVehicleModAsNoLongerNeeded`
**Flags:** static

**Input:**
- `modelId: model_object`

---

### `0771` CUSTOM_PLATE_DESIGN_FOR_NEXT_CAR
Sets the town ID of the license plate which is created on the specified model, affecting which texture is chosen for the plate

**Class:** `Streaming.CustomPlateDesignForNextCar`
**Flags:** static

**Input:**
- `modelId: model_vehicle`
- `design: CarPlateDesign`

---

### `0776` REQUEST_IPL

**Class:** `Streaming.RequestIpl`
**Flags:** static

**Input:**
- `iplName: string`

---

### `0777` REMOVE_IPL

**Class:** `Streaming.RemoveIpl`
**Flags:** static

**Input:**
- `iplName: string`

**Details:**

This command can make a group of objects defined in a binary IPL file to disappear in the game. To make it reappear, use REQUEST_IPL.

---

### `0778` REMOVE_IPL_DISCREETLY

**Class:** `Streaming.RemoveIplDiscreetly`
**Flags:** static

**Input:**
- `iplName: string`

---

### `077E` GET_AREA_VISIBLE
Gets the current interior ID

**Class:** `Streaming.GetAreaVisible`
**Flags:** static

**Output:**
- `areaId: int (variable)`

---

### `07C0` REQUEST_CAR_RECORDING
Loads the specified car recording

**Class:** `Streaming.RequestCarRecording`
**Flags:** static

**Input:**
- `pathId: int`

**Details:**

This command requests the car recording from the `carrec.img` file.

---

### `07C1` HAS_CAR_RECORDING_BEEN_LOADED
Returns true if the car recording has finished loading

**Class:** `Streaming.HasCarRecordingBeenLoaded`
**Flags:** condition, static

**Input:**
- `pathId: int`

---

### `07DE` IS_MODEL_IN_CDIMAGE
Returns true if a file for the model exists

**Class:** `Streaming.IsModelInCdimage`
**Flags:** condition, static

**Input:**
- `modelId: model_any`

---

### `07E4` GET_MODEL_DIMENSIONS

**Class:** `Streaming.GetModelDimensions`
**Flags:** static

**Input:**
- `modelId: model_any`

**Output:**
- `leftBottomBackX: float (variable)`
- `leftBottomBackY: float (variable)`
- `leftBottomBackZ: float (variable)`
- `rightTopFrontX: float (variable)`
- `rightTopFrontY: float (variable)`
- `rightTopFrontZ: float (variable)`

---

### `081E` IS_THIS_MODEL_A_BOAT
Returns true if the model is the model of a boat

**Class:** `Streaming.IsThisModelABoat`
**Flags:** condition, static

**Input:**
- `modelId: model_any`

---

### `081F` IS_THIS_MODEL_A_PLANE
Returns true if the model is the model of a plane

**Class:** `Streaming.IsThisModelAPlane`
**Flags:** condition, static

**Input:**
- `modelId: model_any`

---

### `0820` IS_THIS_MODEL_A_HELI
Returns true if the model is the model of a helicopter

**Class:** `Streaming.IsThisModelAHeli`
**Flags:** condition, static

**Input:**
- `modelId: model_any`

---

### `0873` REMOVE_CAR_RECORDING
Unloads the car recording

**Class:** `Streaming.RemoveCarRecording`
**Flags:** static

**Input:**
- `pathId: int`

---

### `08E8` ATTACH_ANIMS_TO_MODEL
Sets an animation pack to be loaded along with the specified model

**Class:** `Streaming.AttachAnimsToModel`
**Flags:** static

**Input:**
- `pedModelId: int`
- `animationFile: string`

---

### `09B2` GET_RANDOM_CAR_MODEL_IN_MEMORY

**Class:** `Streaming.GetRandomCarModelInMemory`
**Flags:** static

**Input:**
- `normalOnly: bool`

**Output:**
- `modelId: model_vehicle (variable)`
- `class: int (variable)`

---

### `0A01` IS_THIS_MODEL_A_CAR
Returns true if a valid car model is passed

**Class:** `Streaming.IsThisModelACar`
**Flags:** condition, static

**Input:**
- `modelId: model_any`

---

### `0A0B` LOAD_SCENE_IN_DIRECTION

**Class:** `Streaming.LoadSceneInDirection`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `heading: float`

---
