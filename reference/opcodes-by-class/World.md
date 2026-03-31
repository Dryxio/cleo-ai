# World Opcodes

> 65 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `01EB` | SET_CAR_DENSITY_MULTIPLIER | Sets the quantity of traffic that will spawn in the game |
| `02CE` | GET_GROUND_Z_FOR_3D_COORD | Stores the ground position at the location |
| `02EE` | IS_PROJECTILE_IN_AREA | Returns true if a projectile is in the specified 3D area |
| `031A` | REMOVE_ALL_SCRIPT_FIRES | Removes all script fires (02CF) |
| `0327` | GET_RANDOM_CAR_OF_TYPE_IN_AREA | Returns the handle of a random car with the specified model in the specified 2D  |
| `0339` | IS_AREA_OCCUPIED | Returns true if there is anything with the specified properties within the 3D ar |
| `0356` | IS_EXPLOSION_IN_AREA | Returns true if there is an explosion of the specified type in the 3D area |
| `0363` | SET_VISIBILITY_OF_CLOSEST_OBJECT_OF_TYPE | Sets the visibility of the object closest to the specified coordinates, matching |
| `038A` | IS_POINT_OBSCURED_BY_A_MISSION_ENTITY | Returns true if there is a vehicle in the specified area |
| `0395` | CLEAR_AREA | Clears the area, removing all vehicles and pedestrians that are not marked as ne |
| `03B6` | SWAP_NEAREST_BUILDING_MODEL | Swaps a map model with another map model nearest to the center of the search are |
| `03B7` | SWITCH_WORLD_PROCESSING | Sets whether the game should render the world or only the cutscene objects |
| `03BA` | CLEAR_AREA_OF_CARS | Clears all cars in the specified 3D area |
| `03C5` | CREATE_RANDOM_CAR_FOR_CAR_PARK | Starts spawning random cars at the specified location |
| `03DE` | SET_PED_DENSITY_MULTIPLIER | Sets the quantity of pedestrians to spawn in the game |
| `042B` | CLEAR_AREA_OF_CHARS | Clears all pedestrians from the given area |
| `048C` | IS_ANY_PICKUP_AT_COORDS | Returns true if the pickup at the specified coordinates is available to be picke |
| `04A5` | GET_DEAD_CHAR_PICKUP_COORDS | Returns appropriate coordinates for creating a pickup by a dead character |
| `04C0` | CREATE_SCRIPT_ROADBLOCK | Creates a roadblock in the specified area with the specified type |
| `04C1` | CLEAR_ALL_SCRIPT_ROADBLOCKS | Removes references to all created roadblocks (04C0), freeing game memory |
| `04F8` | ADD_SET_PIECE | Creates a trigger zone for police to appear during chases |
| `04F9` | SET_EXTRA_COLOURS | Sets the extra color of the sky |
| `04FA` | CLEAR_EXTRA_COLOURS | Clears the extra color of the sky |
| `053E` | GET_RANDOM_CAR_OF_TYPE_IN_AREA_NO_SAVE | Loops through the pool of vehicles to retrieve one that matches the specified mo |
| `06BC` | FIRE_SINGLE_BULLET | Creates firearm projectile effect between two coordinates. Leaves visible trace  |
| `06BD` | IS_LINE_OF_SIGHT_CLEAR | Checks if there is something in the range of the two specified points |
| `06C3` | GET_NUMBER_OF_FIRES_IN_RANGE |  |
| `06D9` | DELETE_MISSION_TRAINS | Destroys all script-created trains |
| `06DB` | DELETE_ALL_TRAINS | Destroys all trains, including those that are not created by the script |
| `0702` | GET_PERCENTAGE_TAGGED_IN_AREA | Gets the percentage of the number of tags sprayed in the area |
| `0703` | SET_TAG_STATUS_IN_AREA | Sets whether all tags in the area are sprayed |
| `0716` | IS_CLOSEST_OBJECT_OF_TYPE_SMASHED_OR_DAMAGED |  |
| `072D` | IS_FLAME_IN_ANGLED_AREA_2D | Returns true if there's any fire particles within the specified area |
| `072E` | IS_FLAME_IN_ANGLED_AREA_3D | Returns true if there's any flames within the specified area |
| `073E` | GET_RANDOM_CAR_IN_SPHERE_NO_SAVE |  |
| `073F` | GET_RANDOM_CHAR_IN_SPHERE |  |
| `0786` | GET_NUMBER_OF_FIRES_IN_AREA | Gets the number of fires within the specified area |
| `07A6` | GET_NEAREST_TAG_POSITION |  |
| `07DF` | REMOVE_OIL_PUDDLES_IN_AREA |  |
| `07EF` | GET_CITY_FROM_COORDS | Returns the city the specified location is within |
| `07F0` | HAS_OBJECT_OF_TYPE_BEEN_SMASHED |  |
| `07FB` | SWITCH_ENTRY_EXIT | Locates the enex marker via the specified name and sets whether it is visible an |
| `0810` | GET_PARKING_NODE_IN_AREA | Stores the coordinates of the nearest car park node in the specified area |
| `0814` | ADD_STUNT_JUMP | Creates a trigger for a Unique Jump bonus |
| `0830` | SET_POOL_TABLE_COORDS | Creates a pool collision object |
| `0855` | GET_SOUND_LEVEL_AT_COORDS | Gets the level that the character can hear noise at the specified position |
| `085A` | CREATE_EMERGENCY_SERVICES_CAR | Creates an emergency service vehicle on the closest road to the specified coordi |
| `0866` | GET_CLOSEST_STEALABLE_OBJECT | Gets the closest object which can be stolen for burglary missions |
| `0876` | CREATE_BIRDS | Creates a flock of birds flying in the specified direction |
| `088D` | SET_USES_COLLISION_OF_CLOSEST_OBJECT_OF_TYPE | Toggles collision of the object closest to the given coordinates and matching th |
| `089E` | GET_RANDOM_CHAR_IN_SPHERE_ONLY_DRUGS_BUYERS | Loops through the ped pool and returns the first character that is within the sp |
| `08E5` | GET_RANDOM_CHAR_IN_SPHERE_NO_BRAIN | Finds the nearest character to the specified point, in the specified radius |
| `08E7` | DISABLE_ALL_ENTRY_EXITS | Disables all entry/exit markers |
| `091C` | GET_USER_OF_CLOSEST_MAP_ATTRACTOR | Returns the character using a map attractor with the specified model in the spec |
| `092E` | GET_WATER_HEIGHT_AT_COORDS | Gets the height of the water at the specified 2D coordinates |
| `0971` | SYNC_WATER | Flattens water waves |
| `0980` | EXTINGUISH_FIRE_AT_POINT | Removes all fires within the specified area |
| `0985` | SET_CHAR_USES_COLLISION_CLOSEST_OBJECT_OF_TYPE | Sets whether collision of the object closest to the given coordinates and matchi |
| `0986` | CLEAR_ALL_SCRIPT_FIRE_FLAGS | Marks all fires as no longer needed, allowing them to disappear |
| `09B4` | SET_CLOSEST_ENTRY_EXIT_FLAG | This command is like 098E, except it finds the appropriate enex marker via its p |
| `09C0` | GET_RANDOM_CAR_OF_TYPE_IN_ANGLED_AREA_NO_SAVE |  |
| `09C3` | IS_COP_VEHICLE_IN_AREA_3D_NO_SAVE | Returns true if there's any kind of police vehicle in the specified 3D area |
| `09DA` | IS_MONEY_PICKUP_AT_COORDS | Returns true if a money pickup exists near the specified coordinates |
| `0A3E` | GET_RANDOM_CHAR_IN_AREA_OFFSET_NO_SAVE | Returns the first char in the ped pool within radius of the specified point |
| `0A45` | SET_RAILTRACK_RESISTANCE_MULT | Sets the friction/slowdown rate on all rail tracks |

## Detailed Reference

### `01EB` SET_CAR_DENSITY_MULTIPLIER
Sets the quantity of traffic that will spawn in the game

**Class:** `World.SetCarDensityMultiplier`
**Flags:** static

**Input:**
- `multiplier: float`

---

### `02CE` GET_GROUND_Z_FOR_3D_COORD
Stores the ground position at the location

**Class:** `World.GetGroundZFor3DCoord`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `groundZ: float (variable)`

---

### `02EE` IS_PROJECTILE_IN_AREA
Returns true if a projectile is in the specified 3D area

**Class:** `World.IsProjectileInArea`
**Flags:** condition, static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`

---

### `031A` REMOVE_ALL_SCRIPT_FIRES
Removes all script fires (02CF)

**Class:** `World.RemoveAllScriptFires`
**Flags:** static

---

### `0327` GET_RANDOM_CAR_OF_TYPE_IN_AREA
Returns the handle of a random car with the specified model in the specified 2D area, or -1 otherwise

**Class:** `World.GetRandomCarOfTypeInArea`
**Flags:** constructor

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `modelId: model_vehicle`

**Output:**
- `handle: Car (variable)`

---

### `0339` IS_AREA_OCCUPIED
Returns true if there is anything with the specified properties within the 3D area

**Class:** `World.IsAreaOccupied`
**Flags:** condition, static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `solid: bool`
- `car: bool`
- `char: bool`
- `object: bool`
- `particle: bool`

---

### `0356` IS_EXPLOSION_IN_AREA
Returns true if there is an explosion of the specified type in the 3D area

**Class:** `World.IsExplosionInArea`
**Flags:** condition, static

**Input:**
- `explosionType: ExplosionType`
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`

---

### `0363` SET_VISIBILITY_OF_CLOSEST_OBJECT_OF_TYPE
Sets the visibility of the object closest to the specified coordinates, matching the specified model

**Class:** `World.SetVisibilityOfClosestObjectOfType`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `modelId: model_object`
- `state: bool`

---

### `038A` IS_POINT_OBSCURED_BY_A_MISSION_ENTITY
Returns true if there is a vehicle in the specified area

**Class:** `World.IsPointObscuredByAMissionEntity`
**Flags:** condition, static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radiusX: float`
- `radiusY: float`
- `radiusZ: float`

---

### `0395` CLEAR_AREA
Clears the area, removing all vehicles and pedestrians that are not marked as needed by a mission

**Class:** `World.ClearArea`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `clearParticles: bool`

---

### `03B6` SWAP_NEAREST_BUILDING_MODEL
Swaps a map model with another map model nearest to the center of the search area

**Class:** `World.SwapNearestBuildingModel`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `fromModelId: model_object`
- `toModelId: model_object`

---

### `03B7` SWITCH_WORLD_PROCESSING
Sets whether the game should render the world or only the cutscene objects

**Class:** `World.SwitchProcessing`
**Flags:** static

**Input:**
- `state: bool`

---

### `03BA` CLEAR_AREA_OF_CARS
Clears all cars in the specified 3D area

**Class:** `World.ClearAreaOfCars`
**Flags:** static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`

---

### `03C5` CREATE_RANDOM_CAR_FOR_CAR_PARK
Starts spawning random cars at the specified location

**Class:** `World.CreateRandomCarForCarPark`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `heading: float`

---

### `03DE` SET_PED_DENSITY_MULTIPLIER
Sets the quantity of pedestrians to spawn in the game

**Class:** `World.SetPedDensityMultiplier`
**Flags:** static

**Input:**
- `multiplier: float`

---

### `042B` CLEAR_AREA_OF_CHARS
Clears all pedestrians from the given area

**Class:** `World.ClearAreaOfChars`
**Flags:** static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`

---

### `048C` IS_ANY_PICKUP_AT_COORDS
Returns true if the pickup at the specified coordinates is available to be picked up

**Class:** `World.IsAnyPickupAtCoords`
**Flags:** condition, static

**Input:**
- `x: float`
- `y: float`
- `z: float`

---

### `04A5` GET_DEAD_CHAR_PICKUP_COORDS
Returns appropriate coordinates for creating a pickup by a dead character

**Class:** `World.GetDeadCharPickupCoords`
**Flags:** static

**Input:**
- `char: Char`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `04C0` CREATE_SCRIPT_ROADBLOCK
Creates a roadblock in the specified area with the specified type

**Class:** `World.CreateScriptRoadblock`
**Flags:** static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `type: int`

---

### `04C1` CLEAR_ALL_SCRIPT_ROADBLOCKS
Removes references to all created roadblocks (04C0), freeing game memory

**Class:** `World.ClearAllScriptRoadblocks`
**Flags:** static

---

### `04F8` ADD_SET_PIECE
Creates a trigger zone for police to appear during chases

**Class:** `World.AddSetPiece`
**Flags:** static

**Input:**
- `type: SetPieceType`
- `fromX: float`
- `fromY: float`
- `toX: float`
- `toY: float`
- `spawnPoliceAAtX: float`
- `spawnPoliceAAtY: float`
- `headedTowardsAAtX: float`
- `headedTowardsAAtY: float`
- `spawnPoliceBAtX: float`
- `spawnPoliceBAtY: float`
- `headedTowardsBAtX: float`
- `headedTowardsBAtY: float`

---

### `04F9` SET_EXTRA_COLOURS
Sets the extra color of the sky

**Class:** `World.SetExtraColors`
**Flags:** static

**Input:**
- `color: int`
- `fade: bool`

---

### `04FA` CLEAR_EXTRA_COLOURS
Clears the extra color of the sky

**Class:** `World.ClearExtraColors`
**Flags:** static

**Input:**
- `withFade: bool`

---

### `053E` GET_RANDOM_CAR_OF_TYPE_IN_AREA_NO_SAVE
Loops through the pool of vehicles to retrieve one that matches the specified model in the specified 2D area

**Class:** `World.GetRandomCarOfTypeInAreaNoSave`
**Flags:** static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `modelId: model_vehicle`

**Output:**
- `handle: Car (variable)`

---

### `06BC` FIRE_SINGLE_BULLET
Creates firearm projectile effect between two coordinates. Leaves visible trace and deals damage on hit

**Class:** `World.FireSingleBullet`
**Flags:** static

**Input:**
- `fromX: float`
- `fromY: float`
- `fromZ: float`
- `toX: float`
- `toY: float`
- `toZ: float`
- `damage: int`

---

### `06BD` IS_LINE_OF_SIGHT_CLEAR
Checks if there is something in the range of the two specified points

**Class:** `World.IsLineOfSightClear`
**Flags:** condition, static

**Input:**
- `fromX: float`
- `fromY: float`
- `fromZ: float`
- `toX: float`
- `toY: float`
- `toZ: float`
- `buildings: bool`
- `cars: bool`
- `chars: bool`
- `objects: bool`
- `particles: bool`

---

### `06C3` GET_NUMBER_OF_FIRES_IN_RANGE

**Class:** `World.GetNumberOfFiresInRange`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`

**Output:**
- `numFires: int (variable)`

---

### `06D9` DELETE_MISSION_TRAINS
Destroys all script-created trains

**Class:** `World.DeleteMissionTrains`
**Flags:** static

---

### `06DB` DELETE_ALL_TRAINS
Destroys all trains, including those that are not created by the script

**Class:** `World.DeleteAllTrains`
**Flags:** static

---

### `0702` GET_PERCENTAGE_TAGGED_IN_AREA
Gets the percentage of the number of tags sprayed in the area

**Class:** `World.GetPercentageTaggedInArea`
**Flags:** static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`

**Output:**
- `percent: int (variable)`

---

### `0703` SET_TAG_STATUS_IN_AREA
Sets whether all tags in the area are sprayed

**Class:** `World.SetTagStatusInArea`
**Flags:** static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `percent: int`

---

### `0716` IS_CLOSEST_OBJECT_OF_TYPE_SMASHED_OR_DAMAGED

**Class:** `World.IsClosestObjectOfTypeSmashedOrDamaged`
**Flags:** condition, static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `modelId: model_object`
- `smashed: bool`
- `damaged: bool`

---

### `072D` IS_FLAME_IN_ANGLED_AREA_2D
Returns true if there's any fire particles within the specified area

**Class:** `World.IsFlameInAngledArea2D`
**Flags:** condition, static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `angle: float`
- `drawSphere: bool`

---

### `072E` IS_FLAME_IN_ANGLED_AREA_3D
Returns true if there's any flames within the specified area

**Class:** `World.IsFlameInAngledArea3D`
**Flags:** condition, static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `angle: float`
- `drawSphere: bool`

---

### `073E` GET_RANDOM_CAR_IN_SPHERE_NO_SAVE

**Class:** `World.GetRandomCarInSphereNoSave`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `model: model_vehicle`

**Output:**
- `handle: Car (variable)`

---

### `073F` GET_RANDOM_CHAR_IN_SPHERE

**Class:** `World.GetRandomCharInSphere`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `civilian: bool`
- `gang: bool`
- `criminal: bool`

**Output:**
- `handle: Char (variable)`

---

### `0786` GET_NUMBER_OF_FIRES_IN_AREA
Gets the number of fires within the specified area

**Class:** `World.GetNumberOfFiresInArea`
**Flags:** static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`

**Output:**
- `numFires: int (variable)`

---

### `07A6` GET_NEAREST_TAG_POSITION

**Class:** `World.GetNearestTagPosition`
**Flags:** static

**Input:**
- `xCoord: float`
- `yCoord: float`
- `zCoord: float`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `07DF` REMOVE_OIL_PUDDLES_IN_AREA

**Class:** `World.RemoveOilPuddlesInArea`
**Flags:** static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`

---

### `07EF` GET_CITY_FROM_COORDS
Returns the city the specified location is within

**Class:** `World.GetCityFromCoords`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `level: Level (variable)`

---

### `07F0` HAS_OBJECT_OF_TYPE_BEEN_SMASHED

**Class:** `World.HasObjectOfTypeBeenSmashed`
**Flags:** condition, static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `modelId: model_object`

---

### `07FB` SWITCH_ENTRY_EXIT
Locates the enex marker via the specified name and sets whether it is visible and usable

**Class:** `World.SwitchEntryExit`
**Flags:** static

**Input:**
- `interiorName: string`
- `state: bool`

---

### `0810` GET_PARKING_NODE_IN_AREA
Stores the coordinates of the nearest car park node in the specified area

**Class:** `World.GetParkingNodeInArea`
**Flags:** static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0814` ADD_STUNT_JUMP
Creates a trigger for a Unique Jump bonus

**Class:** `World.AddStuntJump`
**Flags:** static

**Input:**
- `startX: float`
- `startY: float`
- `startZ: float`
- `startRadiusX: float`
- `startRadiusY: float`
- `startRadiusZ: float`
- `finishX: float`
- `finishY: float`
- `finishZ: float`
- `finishRadiusX: float`
- `finishRadiusY: float`
- `finishRadiusZ: float`
- `cameraX: float`
- `cameraY: float`
- `cameraZ: float`
- `reward: int`

---

### `0830` SET_POOL_TABLE_COORDS
Creates a pool collision object

**Class:** `World.SetPoolTableCoords`
**Flags:** static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`

---

### `0855` GET_SOUND_LEVEL_AT_COORDS
Gets the level that the character can hear noise at the specified position

**Class:** `World.GetSoundLevelAtCoords`
**Flags:** static

**Input:**
- `handle: Char`
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `level: float (variable)`

---

### `085A` CREATE_EMERGENCY_SERVICES_CAR
Creates an emergency service vehicle on the closest road to the specified coordinates

**Class:** `World.CreateEmergencyServicesCar`
**Flags:** static

**Input:**
- `model: model_vehicle`
- `x: float`
- `y: float`
- `z: float`

---

### `0866` GET_CLOSEST_STEALABLE_OBJECT
Gets the closest object which can be stolen for burglary missions

**Class:** `World.GetClosestStealableObject`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`

**Output:**
- `handle: Object (variable)`

---

### `0876` CREATE_BIRDS
Creates a flock of birds flying in the specified direction

**Class:** `World.CreateBirds`
**Flags:** static

**Input:**
- `xFrom: float`
- `yFrom: float`
- `zFrom: float`
- `xTo: float`
- `yTo: float`
- `zTo: float`
- `quantity: int`
- `type: int`

---

### `088D` SET_USES_COLLISION_OF_CLOSEST_OBJECT_OF_TYPE
Toggles collision of the object closest to the given coordinates and matching the model

**Class:** `World.SetUsesCollisionOfClosestObjectOfType`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `modelId: model_object`
- `state: bool`

---

### `089E` GET_RANDOM_CHAR_IN_SPHERE_ONLY_DRUGS_BUYERS
Loops through the ped pool and returns the first character that is within the specified radius and has the "buys drugs" flag set in peds

**Class:** `World.GetRandomCharInSphereOnlyDrugsBuyers`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`

**Output:**
- `handle: Char (variable)`

---

### `08E5` GET_RANDOM_CHAR_IN_SPHERE_NO_BRAIN
Finds the nearest character to the specified point, in the specified radius

**Class:** `World.GetRandomCharInSphereNoBrain`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`

**Output:**
- `handle: Char (variable)`

---

### `08E7` DISABLE_ALL_ENTRY_EXITS
Disables all entry/exit markers

**Class:** `World.DisableAllEntryExits`
**Flags:** static

**Input:**
- `state: bool`

**Details:**

This command can disable all interior markers created by the ENEX section of the IPL file. Burglary house markers are also disabled.

---

### `091C` GET_USER_OF_CLOSEST_MAP_ATTRACTOR
Returns the character using a map attractor with the specified model in the specified area

**Class:** `World.GetUserOfClosestMapAttractor`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `modelId: model_object`
- `attractorName: string`

**Output:**
- `handle: Char (variable)`

---

### `092E` GET_WATER_HEIGHT_AT_COORDS
Gets the height of the water at the specified 2D coordinates

**Class:** `World.GetWaterHeightAtCoords`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `waves: bool`

**Output:**
- `height: float (variable)`

---

### `0971` SYNC_WATER
Flattens water waves

**Class:** `World.SyncWater`
**Flags:** static

**Details:**

This commands resets water waves making the water surface flat. For a continuous effect, use the command in a loop.

---

### `0980` EXTINGUISH_FIRE_AT_POINT
Removes all fires within the specified area

**Class:** `World.ExtinguishFireAtPoint`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`

---

### `0985` SET_CHAR_USES_COLLISION_CLOSEST_OBJECT_OF_TYPE
Sets whether collision of the object closest to the given coordinates and matching the model applies to the target character

**Class:** `World.SetCharUsesCollisionClosestObjectOfType`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `modelId: model_object`
- `state: bool`
- `target: Char`

---

### `0986` CLEAR_ALL_SCRIPT_FIRE_FLAGS
Marks all fires as no longer needed, allowing them to disappear

**Class:** `World.ClearAllScriptFireFlags`
**Flags:** static

---

### `09B4` SET_CLOSEST_ENTRY_EXIT_FLAG
This command is like 098E, except it finds the appropriate enex marker via its position instead of its name

**Class:** `World.SetClosestEntryExitFlag`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `radius: float`
- `flag: EntryexitsFlag`
- `state: bool`

---

### `09C0` GET_RANDOM_CAR_OF_TYPE_IN_ANGLED_AREA_NO_SAVE

**Class:** `World.GetRandomCarOfTypeInAngledAreaNoSave`
**Flags:** static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `angle: float`
- `modelId: model_vehicle`

**Output:**
- `vehicle: Car (variable)`

---

### `09C3` IS_COP_VEHICLE_IN_AREA_3D_NO_SAVE
Returns true if there's any kind of police vehicle in the specified 3D area

**Class:** `World.IsCopVehicleInArea3DNoSave`
**Flags:** condition, static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`

---

### `09DA` IS_MONEY_PICKUP_AT_COORDS
Returns true if a money pickup exists near the specified coordinates

**Class:** `World.IsMoneyPickupAtCoords`
**Flags:** condition, static

**Input:**
- `x: float`
- `y: float`
- `z: float`

---

### `0A3E` GET_RANDOM_CHAR_IN_AREA_OFFSET_NO_SAVE
Returns the first char in the ped pool within radius of the specified point

**Class:** `World.GetRandomCharInAreaOffsetNoSave`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radiusX: float`
- `radiusY: float`
- `radiusZ: float`

**Output:**
- `handle: Char (variable)`

---

### `0A45` SET_RAILTRACK_RESISTANCE_MULT
Sets the friction/slowdown rate on all rail tracks

**Class:** `World.SetRailtrackResistanceMult`
**Flags:** static

**Input:**
- `mult: float`

---
