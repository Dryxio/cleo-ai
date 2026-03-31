# Car Opcodes

> 196 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `00A5` | CREATE_CAR | Creates a vehicle at the specified location, with the specified model |
| `00A6` | DELETE_CAR | Removes the vehicle from the game |
| `00A7` | CAR_GOTO_COORDINATES | Makes the AI drive to the specified location by any means |
| `00A8` | CAR_WANDER_RANDOMLY | Clears any current tasks the vehicle has and makes it drive around aimlessly |
| `00A9` | CAR_SET_IDLE | Sets the car's mission to idle (MISSION_NONE), stopping any driving activity |
| `00AA` | GET_CAR_COORDINATES | Returns the vehicle's coordinates |
| `00AB` | SET_CAR_COORDINATES | Puts the vehicle at the specified location |
| `00AD` | SET_CAR_CRUISE_SPEED | Sets the vehicle's max speed |
| `00AE` | SET_CAR_DRIVING_STYLE | Sets the behavior of the vehicle's AI driver |
| `00AF` | SET_CAR_MISSION | Sets the mission of the vehicle's AI driver |
| `00B0` | IS_CAR_IN_AREA_2D | Returns true if the vehicle is located within the specified 2D area |
| `00B1` | IS_CAR_IN_AREA_3D | Returns true if the vehicle is located within the specified 3D area |
| `0119` | IS_CAR_DEAD | Returns true if the handle is an invalid vehicle handle or the vehicle has been  |
| `0137` | IS_CAR_MODEL | Returns true if the vehicle has the specified model |
| `0174` | GET_CAR_HEADING | Returns the vehicle's heading (z-angle) |
| `0175` | SET_CAR_HEADING | Sets the vehicle's heading (z-angle) |
| `0185` | IS_CAR_HEALTH_GREATER | Returns true if the car's health is over the specified value |
| `018F` | IS_CAR_STUCK_ON_ROOF | Returns true if the car has been upside down for more than 2 seconds (requires 0 |
| `0190` | ADD_UPSIDEDOWN_CAR_CHECK | Activates upside-down car check for the car |
| `0191` | REMOVE_UPSIDEDOWN_CAR_CHECK | Deactivates upside-down car check (0190) for the car |
| `01AB` | IS_CAR_STOPPED_IN_AREA_2D | Returns true if the car stopped within the specified 2D area |
| `01AC` | IS_CAR_STOPPED_IN_AREA_3D | Returns true if the car stopped within the specified 3D area |
| `01AD` | LOCATE_CAR_2D | Returns true if the car is within the 2D radius of the point |
| `01AE` | LOCATE_STOPPED_CAR_2D | Returns true if the car is stopped within the 2D radius of the point |
| `01AF` | LOCATE_CAR_3D | Returns true if the car is within the 3D radius of the point |
| `01B0` | LOCATE_STOPPED_CAR_3D | Returns true if the car is stopped in the radius of the specified point |
| `01C1` | IS_CAR_STOPPED | Returns true if the vehicle is not moving |
| `01C3` | MARK_CAR_AS_NO_LONGER_NEEDED | Allows the vehicle to be deleted by the game if necessary, and also removes it f |
| `01E9` | GET_NUMBER_OF_PASSENGERS | Returns the number of passengers sitting in the car |
| `01EA` | GET_MAXIMUM_NUMBER_OF_PASSENGERS | Returns the maximum number of passengers that could sit in the car |
| `01EC` | SET_CAR_HEAVY | Sets whether the car is heavy |
| `01F3` | IS_CAR_IN_AIR_PROPER | Returns true if the vehicle is in the air |
| `01F4` | IS_CAR_UPSIDEDOWN | Returns true if the car is upside down |
| `020A` | LOCK_CAR_DOORS | Sets the locked status of the car's doors |
| `020B` | EXPLODE_CAR | Makes the vehicle explode |
| `020D` | IS_CAR_UPRIGHT | Returns true if the vehicle is in the normal position (upright) |
| `0216` | SET_TAXI_LIGHTS | Sets whether the taxi's roof light is on |
| `0224` | SET_CAR_HEALTH | Sets the vehicle's health |
| `0227` | GET_CAR_HEALTH | Returns the vehicle's health |
| `0229` | CHANGE_CAR_COLOUR | Sets the car's primary and secondary colors |
| `0294` | SET_CAN_RESPRAY_CAR | Makes car keep current colors when Pay'n'Spray is used |
| `02AA` | SET_CAR_ONLY_DAMAGED_BY_PLAYER | Makes a vehicle immune to everything except the player |
| `02AC` | SET_CAR_PROOFS | Sets the vehicle's immunities |
| `02BF` | IS_CAR_IN_WATER | Returns true if the vehicle is submerged in water |
| `02C2` | CAR_GOTO_COORDINATES_ACCURATE | Makes the AI drive to the specified location obeying the traffic rules |
| `02CA` | IS_CAR_ON_SCREEN | Returns true if the car is visible |
| `02E3` | GET_CAR_SPEED | Gets the car's speed |
| `02F8` | GET_CAR_FORWARD_X | Returns the X coord of the vehicle's angle |
| `02F9` | GET_CAR_FORWARD_Y | Returns the Y coord of the vehicle's angle |
| `031E` | HAS_CAR_BEEN_DAMAGED_BY_WEAPON | Returns true if the vehicle has been hit by the specified weapon |
| `0338` | SET_CAR_VISIBLE | Sets whether the vehicle is visible or not |
| `0397` | SWITCH_CAR_SIREN | Sets whether the car's alarm can be activated |
| `039C` | SET_CAR_WATERTIGHT | Makes the vehicle watertight, meaning characters inside will not be harmed if th |
| `039F` | TURN_CAR_TO_FACE_COORD | Sets the car's heading so that it is facing the 2D coordinate |
| `03A2` | SET_CAR_STATUS | Sets the car's status |
| `03AB` | SET_CAR_STRONG | Defines whether the car is more resistant to collisions than normal |
| `03C9` | IS_CAR_VISIBLY_DAMAGED | Returns true if any of the car components is visibly damaged or lost |
| `03ED` | SET_UPSIDEDOWN_CAR_NOT_DAMAGED | Disables the car from exploding when it is upside down, as long as the player is |
| `03F3` | GET_CAR_COLOURS | Gets the car's primary and secondary colors |
| `03F5` | SET_CAR_CAN_BE_DAMAGED | Sets whether the car receives damage |
| `0407` | GET_OFFSET_FROM_CAR_IN_WORLD_COORDS | Returns the coordinates of an offset of the vehicle's position, depending on the |
| `0423` | SET_CAR_TRACTION | Overrides the default AI controlled vehicle traction value of 1.0 |
| `0428` | SET_CAR_AVOID_LEVEL_TRANSITIONS | Sets whether the vehicle will avoid paths between levels (0426) |
| `0431` | IS_CAR_PASSENGER_SEAT_FREE | Returns true if the specified car seat is empty |
| `0432` | GET_CHAR_IN_CAR_PASSENGER_SEAT | Returns the handle of a character sitting in the specified car seat |
| `0441` | GET_CAR_MODEL | Returns the car's model id |
| `0466` | SET_CAR_STAY_IN_FAST_LANE |  |
| `0468` | CLEAR_CAR_LAST_WEAPON_DAMAGE | Clears the vehicle's last weapon damage (see 031E) |
| `046C` | GET_DRIVER_OF_CAR | Returns the car's driver handle |
| `0477` | SET_CAR_TEMP_ACTION | Makes the AI driver perform the action in the vehicle for the specified period o |
| `048B` | SET_CAR_RANDOM_ROUTE_SEED | Sets the car on a specific route |
| `0495` | IS_CAR_ON_FIRE | Returns true if the car is burning |
| `0496` | IS_CAR_TYRE_BURST | Returns true if a given tire on the car is deflated |
| `04BA` | SET_CAR_FORWARD_SPEED | Sets the speed of the car |
| `04BD` | MARK_CAR_AS_CONVOY_CAR | Marks the car as being part of a convoy, which seems to follow a path set by 099 |
| `04E0` | SET_CAR_STRAIGHT_LINE_DISTANCE | Sets the minimum distance for the AI driver to start ignoring car paths and go s |
| `04E1` | POP_CAR_BOOT | Opens the car's trunk and keeps it open |
| `04F1` | IS_CAR_WAITING_FOR_WORLD_COLLISION |  |
| `04FE` | BURST_CAR_TYRE | Deflates the car's tire |
| `0506` | SET_CAR_MODEL_COMPONENTS | Sets the variation of the next car to be created |
| `0508` | CLOSE_ALL_CAR_DOORS | Closes all car doors, hoods and boots |
| `0519` | FREEZE_CAR_POSITION | Locks the vehicle's position |
| `051C` | HAS_CAR_BEEN_DAMAGED_BY_CHAR | Returns true if the car has been damaged by the specified char |
| `051D` | HAS_CAR_BEEN_DAMAGED_BY_CAR | Returns true if the vehicle has been damaged by another specified vehicle |
| `053F` | SET_CAN_BURST_CAR_TYRES | Sets whether the car's tires can be deflated |
| `054F` | CLEAR_CAR_LAST_DAMAGE_ENTITY | Clears the car's last damage entity |
| `056E` | DOES_VEHICLE_EXIST | Returns true if the handle is a valid vehicle handle |
| `0574` | FREEZE_CAR_POSITION_AND_DONT_LOAD_COLLISION | Makes the car maintain its position |
| `0587` | SET_LOAD_COLLISION_FOR_CAR_FLAG |  |
| `0594` | SET_VEHICLE_TO_FADE_IN | Sets the alpha transparency of a distant vehicle |
| `05EB` | START_PLAYBACK_RECORDED_CAR | Assigns a car to a path |
| `05EC` | STOP_PLAYBACK_RECORDED_CAR | Stops car from following path |
| `05ED` | PAUSE_PLAYBACK_RECORDED_CAR | Freezes the car on its path |
| `05EE` | UNPAUSE_PLAYBACK_RECORDED_CAR | Unfreezes the vehicle on its path |
| `05F1` | SET_CAR_ESCORT_CAR_LEFT | Makes the vehicle stay on the other vehicle's left side, keeping parallel |
| `05F2` | SET_CAR_ESCORT_CAR_RIGHT | Makes the vehicle stay by the right side of the other vehicle, keeping parallel |
| `05F3` | SET_CAR_ESCORT_CAR_REAR | Makes the vehicle stay behind the other car, keeping parallel |
| `05F4` | SET_CAR_ESCORT_CAR_FRONT | Makes the vehicle stay in front of the other, keeping parallel |
| `060E` | IS_PLAYBACK_GOING_ON_FOR_CAR | Returns true if the car is assigned to a path |
| `0657` | OPEN_CAR_DOOR | Opens the specified car door |
| `0674` | CUSTOM_PLATE_FOR_NEXT_CAR | Sets the numberplate of the next car to be spawned with the specified model |
| `067F` | FORCE_CAR_LIGHTS | Sets an override for the car's lights |
| `0683` | ATTACH_CAR_TO_CAR |  |
| `0684` | DETACH_CAR | Detaches the car with optional rotation and force |
| `0686` | IS_VEHICLE_ATTACHED |  |
| `0689` | POP_CAR_DOOR | Removes the specified car door component from the car |
| `068A` | FIX_CAR_DOOR | Repairs the car door |
| `068B` | TASK_EVERYONE_LEAVE_CAR | Makes all passengers of the car leave it |
| `0697` | POP_CAR_PANEL | Detatches or deletes car's body part |
| `0698` | FIX_CAR_PANEL | Repairs or reinstalls car's body part |
| `0699` | FIX_CAR_TYRE | Repairs a car's tire |
| `06A2` | GET_CAR_SPEED_VECTOR |  |
| `06A3` | GET_CAR_MASS | Returns the vehicle's mass |
| `06BE` | GET_CAR_ROLL | Returns the Y Angle of the vehicle |
| `06C5` | SKIP_TO_END_AND_STOP_PLAYBACK_RECORDED_CAR |  |
| `06E5` | GET_AVAILABLE_VEHICLE_MOD | Returns a model id available for the vehicle's mod slot, or -1 otherwise |
| `06E7` | ADD_VEHICLE_MOD | Adds a new mod with the model to the vehicle |
| `06E8` | REMOVE_VEHICLE_MOD | Removes the vehicle's mod with the specified model |
| `06EC` | GET_NUM_AVAILABLE_PAINTJOBS | Gets the number of possible paintjobs that can be applied to the car |
| `06ED` | GIVE_VEHICLE_PAINTJOB | Sets the car's paintjob |
| `06FC` | DOES_CAR_HAVE_STUCK_CAR_CHECK | Returns true if the car has car stuck check enabled |
| `06FD` | SET_PLAYBACK_SPEED | Sets the playback speed of the car playing a car recording |
| `0704` | CAR_GOTO_COORDINATES_RACING | Makes the AI drive to the destination as fast as possible, trying to overtake ot |
| `0705` | START_PLAYBACK_RECORDED_CAR_USING_AI | Starts the playback of a recorded car with driver AI enabled |
| `0706` | SKIP_IN_PLAYBACK_RECORDED_CAR | Advances the recorded car playback by the specified amount |
| `070C` | EXPLODE_CAR_IN_CUTSCENE | Makes the vehicle explode without affecting its surroundings |
| `0714` | SET_CAR_STAY_IN_SLOW_LANE |  |
| `0730` | DAMAGE_CAR_PANEL | Damages a panel on the car |
| `0731` | SET_CAR_ROLL | Sets the Y Angle of the vehicle to the specified value |
| `073B` | SET_CAR_CAN_GO_AGAINST_TRAFFIC | Sets whether the vehicle will drive the wrong way on roads |
| `073C` | DAMAGE_CAR_DOOR | Damages a component on the vehicle |
| `0763` | SET_CAR_AS_MISSION_CAR | Sets the script as the owner of the vehicle and adds it to the mission cleanup l |
| `077D` | GET_CAR_PITCH | Returns the X Angle of the vehicle |
| `07C5` | GET_VEHICLE_QUATERNION | Gets the quaternion values of the car |
| `07C6` | SET_VEHICLE_QUATERNION | Sets the rotation of a vehicle using quaternion values |
| `07D5` | APPLY_FORCE_TO_CAR | Applies force to car with offset from its center of mass |
| `07DA` | ADD_TO_CAR_ROTATION_VELOCITY |  |
| `07DB` | SET_CAR_ROTATION_VELOCITY |  |
| `07EE` | SET_CAR_ALWAYS_CREATE_SKIDS |  |
| `07F5` | CONTROL_CAR_HYDRAULICS | Changes the car wheels' suspension level |
| `07F8` | SET_CAR_FOLLOW_CAR |  |
| `07FF` | SET_CAR_HYDRAULICS | Enables hydraulic suspension on the car |
| `0803` | DOES_CAR_HAVE_HYDRAULICS | Returns true if the car has hydraulics installed |
| `081D` | SET_CAR_ENGINE_BROKEN | Sets whether the car's engine is broken |
| `083F` | GET_CAR_UPRIGHT_VALUE | Gets the car's vertical angle |
| `0840` | SET_VEHICLE_AREA_VISIBLE |  |
| `0841` | SELECT_WEAPONS_FOR_VEHICLE | Sets the vehicle to use its secondary guns |
| `084E` | SET_VEHICLE_CAN_BE_TARGETTED | Sets whether the vehicle can be targeted |
| `0852` | SET_CAR_CAN_BE_VISIBLY_DAMAGED | Sets whether the vehicle can be visibly damaged |
| `085E` | START_PLAYBACK_RECORDED_CAR_LOOPED | Starts looped playback of a recorded car path |
| `0878` | SET_VEHICLE_DIRT_LEVEL | Sets the dirt level of the car |
| `088B` | SET_VEHICLE_AIR_RESISTANCE_MULTIPLIER | Sets the air resistance for the vehicle |
| `088C` | SET_CAR_COORDINATES_NO_OFFSET | Sets the vehicle coordinates without applying offsets to account for the height  |
| `0897` | IS_VEHICLE_TOUCHING_OBJECT | Returns true if the vehicle is in contact with the object |
| `08A4` | CONTROL_MOVABLE_VEHICLE_PART | Sets the angle of a vehicle's extra |
| `08A5` | WINCH_CAN_PICK_VEHICLE_UP | Sets whether the vehicle can be picked up using the magnocrane |
| `08A6` | OPEN_CAR_DOOR_A_BIT | Sets the angle of a car door |
| `08A7` | IS_CAR_DOOR_FULLY_OPEN |  |
| `08CB` | EXPLODE_CAR_IN_CUTSCENE_SHAKE_AND_BITS | Causes the vehicle to explode, without damage to surrounding entities |
| `08EC` | GET_VEHICLE_CLASS | Returns the vehicle's class as defined in vehicles.ide |
| `08F2` | VEHICLE_CAN_BE_TARGETTED_BY_HS_MISSILE | Sets whether the player can target this vehicle with a heatseeking rocket launch |
| `08F3` | SET_FREEBIES_IN_VEHICLE | Sets whether the player can receive items from this vehicle, such as shotgun amm |
| `0918` | SET_CAR_ENGINE_ON | Sets whether the vehicle's engine is turned on or off |
| `0919` | SET_CAR_LIGHTS_ON | Sets whether the vehicle's lights are on |
| `0939` | ATTACH_CAR_TO_OBJECT | Attaches the car to object with offset and rotation |
| `0957` | VEHICLE_DOES_PROVIDE_COVER | Sets whether characters in combat will choose to use the vehicle as cover from g |
| `095E` | CONTROL_CAR_DOOR | Sets the car's door angle and latch state |
| `095F` | GET_DOOR_ANGLE_RATIO | Gets the specified car doors angle, relative to the hinge |
| `0969` | IS_BIG_VEHICLE | Returns true if the specified vehicle has the 'is big' flag set in vehicles |
| `096B` | STORE_CAR_MOD_STATE |  |
| `096C` | RESTORE_CAR_MOD_STATE |  |
| `096D` | GET_CURRENT_CAR_MOD | Returns the model of the component installed on the specified slot of the vehicl |
| `096E` | IS_CAR_LOW_RIDER | Returns true if the vehicle is a low rider |
| `096F` | IS_CAR_STREET_RACER | Returns true if the vehicle is a street racer |
| `0975` | IS_EMERGENCY_SERVICES_VEHICLE | Returns true if the vehicle is an emergency vehicle |
| `097D` | GET_NUM_CAR_COLOURS | Returns number of color variations defined for the model of this car in carcols. |
| `0987` | GET_CAR_BLOCKING_CAR | Returns a handle of the vehicle preventing this car from getting to its destinat |
| `0988` | GET_CURRENT_VEHICLE_PAINTJOB | Gets the car's paintjob |
| `098D` | GET_CAR_MOVING_COMPONENT_OFFSET | Sets the angle of a vehicle's extra |
| `099A` | SET_CAR_COLLISION |  |
| `099B` | CHANGE_PLAYBACK_TO_USE_AI | Changes vehicle control from playback to AI driven |
| `09AB` | RANDOM_PASSENGER_SAY | Makes a passenger in the vehicle speak from an ambient speech ID, if one exists  |
| `09B0` | SET_VEHICLE_IS_CONSIDERED_BY_PLAYER | Makes player character ignore the car when enter vehicle key is used |
| `09B3` | GET_CAR_DOOR_LOCK_STATUS | Returns the door lock mode of the vehicle |
| `09BB` | IS_CAR_DOOR_DAMAGED | Returns true if the specified vehicle part is visibly damaged |
| `09C4` | SET_PETROL_TANK_WEAKPOINT | Sets whether the car can be blown up by shooting at the petrol tank |
| `09CB` | IS_CAR_TOUCHING_CAR | Returns true if the car is touching the other car |
| `09D0` | IS_VEHICLE_ON_ALL_WHEELS | Returns true if all the vehicle's wheels are touching the ground |
| `09E1` | GET_CAR_MODEL_VALUE | Returns the value of the specified car model |
| `09E9` | GIVE_NON_PLAYER_CAR_NITRO | Makes the car have one nitro |
| `09FE` | RESET_VEHICLE_HYDRAULICS | This resets all the hydraulics on the car, making it "sit" |
| `0A11` | SET_EXTRA_CAR_COLOURS | Sets the car's ternary and quaternary colors. See also 0229 |
| `0A12` | GET_EXTRA_CAR_COLOURS | Returns the car's tertiary and quaternary colors. See also 03F3 |
| `0A15` | HAS_CAR_BEEN_RESPRAYED | Returns true if the vehicle was resprayed in the last frame AND resets the respr |
| `0A21` | IMPROVE_CAR_BY_CHEATING | Sets whether a ped driven vehicle's handling is affected by the 'perfect handlin |
| `0A30` | FIX_CAR | Restores the vehicle to full health and removes the damage |

## Detailed Reference

### `00A5` CREATE_CAR
Creates a vehicle at the specified location, with the specified model

**Class:** `Car.Create`
**Flags:** constructor

**Input:**
- `modelId: model_vehicle`
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `handle: Car (variable)`

**Details:**

This command creates a vehicle at the coordinates point. 
Using this command requires the model to be already loaded, usually through REQUEST_MODEL, or else the game might crash. 
The major script editors like Sanny Builder support using the vehicle's DFF model name and automatically converts those values into integers upon compilation. 
The Enforcer, Police, and Rhino are locked initially (lock state 5) when spawned; they can be unlocked using LOCK_CAR_DOORS or if any driver exits the vehicle. 
All vehicles created by this command outside a mission will become near-permanent in the game until MARK_CAR_AS_NO_LONGER_NEEDED is used to mark it as no longer needed.

Additionally, CREATE_CAR sets the `VEHICLEFLAG_ISLOCKED` flag, which prevents the vehicle from being towed.

---

### `00A6` DELETE_CAR
Removes the vehicle from the game

**Class:** `Car.Delete`
**Flags:** destructor

**Input:**
- `self: Car`

---

### `00A7` CAR_GOTO_COORDINATES
Makes the AI drive to the specified location by any means

**Class:** `Car.GotoCoordinates`

**Input:**
- `self: Car`
- `x: float`
- `y: float`
- `z: float`

---

### `00A8` CAR_WANDER_RANDOMLY
Clears any current tasks the vehicle has and makes it drive around aimlessly

**Class:** `Car.WanderRandomly`

**Input:**
- `self: Car`

---

### `00A9` CAR_SET_IDLE
Sets the car's mission to idle (MISSION_NONE), stopping any driving activity

**Class:** `Car.SetIdle`

**Input:**
- `self: Car`

---

### `00AA` GET_CAR_COORDINATES
Returns the vehicle's coordinates

**Class:** `Car.GetCoordinates`

**Input:**
- `self: Car`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `00AB` SET_CAR_COORDINATES
Puts the vehicle at the specified location

**Class:** `Car.SetCoordinates`

**Input:**
- `self: Car`
- `x: float`
- `y: float`
- `z: float`

---

### `00AD` SET_CAR_CRUISE_SPEED
Sets the vehicle's max speed

**Class:** `Car.SetCruiseSpeed`

**Input:**
- `self: Car`
- `maxSpeed: float`

---

### `00AE` SET_CAR_DRIVING_STYLE
Sets the behavior of the vehicle's AI driver

**Class:** `Car.SetDrivingStyle`

**Input:**
- `self: Car`
- `drivingStyle: DrivingMode`

---

### `00AF` SET_CAR_MISSION
Sets the mission of the vehicle's AI driver

**Class:** `Car.SetMission`

**Input:**
- `self: Car`
- `carMission: CarMission`

---

### `00B0` IS_CAR_IN_AREA_2D
Returns true if the vehicle is located within the specified 2D area

**Class:** `Car.IsInArea2D`
**Flags:** condition

**Input:**
- `self: Car`
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `drawSphere: bool`

---

### `00B1` IS_CAR_IN_AREA_3D
Returns true if the vehicle is located within the specified 3D area

**Class:** `Car.IsInArea3D`
**Flags:** condition

**Input:**
- `self: Car`
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `drawSphere: bool`

---

### `0119` IS_CAR_DEAD
Returns true if the handle is an invalid vehicle handle or the vehicle has been destroyed (wrecked)

**Class:** `Car.IsDead`
**Flags:** condition, static

**Input:**
- `handle: any`

---

### `0137` IS_CAR_MODEL
Returns true if the vehicle has the specified model

**Class:** `Car.IsModel`
**Flags:** condition

**Input:**
- `self: Car`
- `modelId: model_vehicle`

---

### `0174` GET_CAR_HEADING
Returns the vehicle's heading (z-angle)

**Class:** `Car.GetHeading`

**Input:**
- `self: Car`

**Output:**
- `heading: float (variable)`

---

### `0175` SET_CAR_HEADING
Sets the vehicle's heading (z-angle)

**Class:** `Car.SetHeading`

**Input:**
- `self: Car`
- `heading: float`

---

### `0185` IS_CAR_HEALTH_GREATER
Returns true if the car's health is over the specified value

**Class:** `Car.IsHealthGreater`
**Flags:** condition

**Input:**
- `self: Car`
- `health: int`

---

### `018F` IS_CAR_STUCK_ON_ROOF
Returns true if the car has been upside down for more than 2 seconds (requires 0190)

**Class:** `Car.IsStuckOnRoof`
**Flags:** condition

**Input:**
- `self: Car`

---

### `0190` ADD_UPSIDEDOWN_CAR_CHECK
Activates upside-down car check for the car

**Class:** `Car.AddUpsidedownCheck`

**Input:**
- `self: Car`

---

### `0191` REMOVE_UPSIDEDOWN_CAR_CHECK
Deactivates upside-down car check (0190) for the car

**Class:** `Car.RemoveUpsidedownCheck`

**Input:**
- `self: Car`

---

### `01AB` IS_CAR_STOPPED_IN_AREA_2D
Returns true if the car stopped within the specified 2D area

**Class:** `Car.IsStoppedInArea2D`
**Flags:** condition

**Input:**
- `self: Car`
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `drawSphere: bool`

---

### `01AC` IS_CAR_STOPPED_IN_AREA_3D
Returns true if the car stopped within the specified 3D area

**Class:** `Car.IsStoppedInArea3D`
**Flags:** condition

**Input:**
- `self: Car`
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `drawSphere: bool`

---

### `01AD` LOCATE_CAR_2D
Returns true if the car is within the 2D radius of the point

**Class:** `Car.Locate2D`
**Flags:** condition

**Input:**
- `self: Car`
- `x: float`
- `y: float`
- `xRadius: float`
- `yRadius: float`
- `drawSphere: bool`

---

### `01AE` LOCATE_STOPPED_CAR_2D
Returns true if the car is stopped within the 2D radius of the point

**Class:** `Car.LocateStopped2D`
**Flags:** condition

**Input:**
- `self: Car`
- `x: float`
- `y: float`
- `xRadius: float`
- `yRadius: float`
- `drawSphere: bool`

---

### `01AF` LOCATE_CAR_3D
Returns true if the car is within the 3D radius of the point

**Class:** `Car.Locate3D`
**Flags:** condition

**Input:**
- `self: Car`
- `x: float`
- `y: float`
- `z: float`
- `xRadius: float`
- `yRadius: float`
- `zRadius: float`
- `drawSphere: bool`

---

### `01B0` LOCATE_STOPPED_CAR_3D
Returns true if the car is stopped in the radius of the specified point

**Class:** `Car.LocateStopped3D`
**Flags:** condition

**Input:**
- `self: Car`
- `x: float`
- `y: float`
- `z: float`
- `xRadius: float`
- `yRadius: float`
- `zRadius: float`
- `drawSphere: bool`

---

### `01C1` IS_CAR_STOPPED
Returns true if the vehicle is not moving

**Class:** `Car.IsStopped`
**Flags:** condition

**Input:**
- `self: Car`

---

### `01C3` MARK_CAR_AS_NO_LONGER_NEEDED
Allows the vehicle to be deleted by the game if necessary, and also removes it from the mission cleanup list, if applicable

**Class:** `Car.MarkAsNoLongerNeeded`

**Input:**
- `self: Car`

---

### `01E9` GET_NUMBER_OF_PASSENGERS
Returns the number of passengers sitting in the car

**Class:** `Car.GetNumberOfPassengers`

**Input:**
- `self: Car`

**Output:**
- `count: int (variable)`

---

### `01EA` GET_MAXIMUM_NUMBER_OF_PASSENGERS
Returns the maximum number of passengers that could sit in the car

**Class:** `Car.GetMaximumNumberOfPassengers`

**Input:**
- `self: Car`

**Output:**
- `count: int (variable)`

---

### `01EC` SET_CAR_HEAVY
Sets whether the car is heavy

**Class:** `Car.SetHeavy`

**Input:**
- `self: Car`
- `state: bool`

---

### `01F3` IS_CAR_IN_AIR_PROPER
Returns true if the vehicle is in the air

**Class:** `Car.IsInAirProper`
**Flags:** condition

**Input:**
- `self: Car`

---

### `01F4` IS_CAR_UPSIDEDOWN
Returns true if the car is upside down

**Class:** `Car.IsUpsidedown`
**Flags:** condition

**Input:**
- `self: Car`

---

### `020A` LOCK_CAR_DOORS
Sets the locked status of the car's doors

**Class:** `Car.LockDoors`

**Input:**
- `self: Car`
- `lockStatus: CarLock`

---

### `020B` EXPLODE_CAR
Makes the vehicle explode

**Class:** `Car.Explode`

**Input:**
- `self: Car`

---

### `020D` IS_CAR_UPRIGHT
Returns true if the vehicle is in the normal position (upright)

**Class:** `Car.IsUpright`
**Flags:** condition

**Input:**
- `self: Car`

---

### `0216` SET_TAXI_LIGHTS
Sets whether the taxi's roof light is on

**Class:** `Car.SetTaxiLights`

**Input:**
- `self: Car`
- `state: bool`

---

### `0224` SET_CAR_HEALTH
Sets the vehicle's health

**Class:** `Car.SetHealth`

**Input:**
- `self: Car`
- `health: int`

---

### `0227` GET_CAR_HEALTH
Returns the vehicle's health

**Class:** `Car.GetHealth`

**Input:**
- `self: Car`

**Output:**
- `health: int (variable)`

---

### `0229` CHANGE_CAR_COLOUR
Sets the car's primary and secondary colors

**Class:** `Car.ChangeColor`

**Input:**
- `self: Car`
- `color1: int`
- `color2: int`

**Details:**

Below table represents all colors used in the standard `carcols.dat` for GTA San Andreas. Click the color box to copy the id to the clipboard.

<div style="font-size:0">
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>0</sub><br/><span data-copy-text="0" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(0,0,0)" title="#0 black rgb(0,0,0)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>1</sub><br/><span data-copy-text="1" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(245,245,245)" title="#1 white rgb(245,245,245)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>2</sub><br/><span data-copy-text="2" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(42,119,161)" title="#2 police car blue rgb(42,119,161)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>3</sub><br/><span data-copy-text="3" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(132,4,16)" title="#3 cherry red rgb(132,4,16)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>4</sub><br/><span data-copy-text="4" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(38,55,57)" title="#4 midnight blue rgb(38,55,57)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>5</sub><br/><span data-copy-text="5" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(134,68,110)" title="#5 temple curtain purple rgb(134,68,110)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>6</sub><br/><span data-copy-text="6" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(215,142,16)" title="#6 taxi yellow rgb(215,142,16)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>7</sub><br/><span data-copy-text="7" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(76,117,183)" title="#7 striking blue rgb(76,117,183)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>8</sub><br/><span data-copy-text="8" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(189,190,198)" title="#8 light blue grey rgb(189,190,198)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>9</sub><br/><span data-copy-text="9" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(94,112,114)" title="#9 hoods rgb(94,112,114)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>10</sub><br/><span data-copy-text="10" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(70,89,122)" title="#10 saxony blue poly rgb(70,89,122)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>11</sub><br/><span data-copy-text="11" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(101,106,121)" title="#11 concord blue poly rgb(101,106,121)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>12</sub><br/><span data-copy-text="12" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(93,126,141)" title="#12 jasper green poly rgb(93,126,141)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>13</sub><br/><span data-copy-text="13" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(88,89,90)" title="#13 pewter gray poly rgb(88,89,90)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>14</sub><br/><span data-copy-text="14" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(214,218,214)" title="#14 frost white rgb(214,218,214)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>15</sub><br/><span data-copy-text="15" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(156,161,163)" title="#15 silver stone poly rgb(156,161,163)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>16</sub><br/><span data-copy-text="16" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(51,95,63)" title="#16 rio red rgb(51,95,63)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>17</sub><br/><span data-copy-text="17" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(115,14,26)" title="#17 torino red pearl rgb(115,14,26)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>18</sub><br/><span data-copy-text="18" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(123,10,42)" title="#18 formula red rgb(123,10,42)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>19</sub><br/><span data-copy-text="19" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(159,157,148)" title="#19 honey beige poly rgb(159,157,148)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>20</sub><br/><span data-copy-text="20" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(59,78,120)" title="#20 mariner blue rgb(59,78,120)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>21</sub><br/><span data-copy-text="21" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(115,46,62)" title="#21 blaze red rgb(115,46,62)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>22</sub><br/><span data-copy-text="22" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(105,30,59)" title="#22 classic red rgb(105,30,59)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>23</sub><br/><span data-copy-text="23" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(150,145,140)" title="#23 winning silver poly rgb(150,145,140)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>24</sub><br/><span data-copy-text="24" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(81,84,89)" title="#24 steel gray poly rgb(81,84,89)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>25</sub><br/><span data-copy-text="25" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(63,62,69)" title="#25 shadow silver poly rgb(63,62,69)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>26</sub><br/><span data-copy-text="26" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(165,169,167)" title="#26 silver stone poly rgb(165,169,167)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>27</sub><br/><span data-copy-text="27" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(99,92,90)" title="#27 warm grey mica rgb(99,92,90)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>28</sub><br/><span data-copy-text="28" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(61,74,104)" title="#28 harbor blue poly rgb(61,74,104)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>29</sub><br/><span data-copy-text="29" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(151,149,146)" title="#29 porcelain silver poly rgb(151,149,146)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>30</sub><br/><span data-copy-text="30" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(66,31,33)" title="#30 mellow burgundy rgb(66,31,33)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>31</sub><br/><span data-copy-text="31" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(95,39,43)" title="#31 graceful red mica rgb(95,39,43)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>32</sub><br/><span data-copy-text="32" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(132,148,171)" title="#32 currant blue poly rgb(132,148,171)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>33</sub><br/><span data-copy-text="33" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(118,123,124)" title="#33 gray poly rgb(118,123,124)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>34</sub><br/><span data-copy-text="34" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(100,100,100)" title="#34 arctic white rgb(100,100,100)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>35</sub><br/><span data-copy-text="35" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(90,87,82)" title="#35 anthracite gray poly rgb(90,87,82)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>36</sub><br/><span data-copy-text="36" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(37,37,39)" title="#36 black poly rgb(37,37,39)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>37</sub><br/><span data-copy-text="37" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(45,58,53)" title="#37 dark green poly rgb(45,58,53)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>38</sub><br/><span data-copy-text="38" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(147,163,150)" title="#38 seafoam poly rgb(147,163,150)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>39</sub><br/><span data-copy-text="39" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(109,122,136)" title="#39 diamond blue poly rgb(109,122,136)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>40</sub><br/><span data-copy-text="40" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(34,25,24)" title="#40 biston brown poly rgb(34,25,24)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>41</sub><br/><span data-copy-text="41" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(111,103,95)" title="#41 desert taupe poly rgb(111,103,95)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>42</sub><br/><span data-copy-text="42" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(124,28,42)" title="#42 garnet red poly rgb(124,28,42)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>43</sub><br/><span data-copy-text="43" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(95,10,21)" title="#43 desert red rgb(95,10,21)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>44</sub><br/><span data-copy-text="44" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(25,56,38)" title="#44 green rgb(25,56,38)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>45</sub><br/><span data-copy-text="45" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(93,27,32)" title="#45 cabernet red poly rgb(93,27,32)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>46</sub><br/><span data-copy-text="46" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(157,152,114)" title="#46 light ivory rgb(157,152,114)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>47</sub><br/><span data-copy-text="47" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(122,117,96)" title="#47 pueblo beige rgb(122,117,96)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>48</sub><br/><span data-copy-text="48" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(152,149,134)" title="#48 smoke silver poly rgb(152,149,134)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>49</sub><br/><span data-copy-text="49" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(173,176,176)" title="#49 astra silver poly rgb(173,176,176)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>50</sub><br/><span data-copy-text="50" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(132,137,136)" title="#50 ascot gray rgb(132,137,136)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>51</sub><br/><span data-copy-text="51" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(48,79,69)" title="#51 agate green rgb(48,79,69)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>52</sub><br/><span data-copy-text="52" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(77,98,104)" title="#52 petrol blue green poly rgb(77,98,104)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>53</sub><br/><span data-copy-text="53" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(22,34,72)" title="#53 surf blue rgb(22,34,72)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>54</sub><br/><span data-copy-text="54" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(39,47,75)" title="#54 nautical blue poly rgb(39,47,75)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>55</sub><br/><span data-copy-text="55" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(125,98,86)" title="#55 woodrose poly rgb(125,98,86)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>56</sub><br/><span data-copy-text="56" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(158,164,171)" title="#56 crystal blue poly rgb(158,164,171)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>57</sub><br/><span data-copy-text="57" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(156,141,113)" title="#57 bisque frost poly rgb(156,141,113)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>58</sub><br/><span data-copy-text="58" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(109,24,34)" title="#58 currant red solid rgb(109,24,34)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>59</sub><br/><span data-copy-text="59" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(78,104,129)" title="#59 lt.crystal blue poly rgb(78,104,129)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>60</sub><br/><span data-copy-text="60" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(156,156,152)" title="#60 lt.titanium poly rgb(156,156,152)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>61</sub><br/><span data-copy-text="61" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(145,115,71)" title="#61 race yellow solid rgb(145,115,71)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>62</sub><br/><span data-copy-text="62" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(102,28,38)" title="#62 brt.currant red poly rgb(102,28,38)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>63</sub><br/><span data-copy-text="63" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(148,157,159)" title="#63 clear crystal blue frost poly rgb(148,157,159)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>64</sub><br/><span data-copy-text="64" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(164,167,165)" title="#64 silver poly rgb(164,167,165)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>65</sub><br/><span data-copy-text="65" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(142,140,70)" title="#65 pastel alabaster rgb(142,140,70)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>66</sub><br/><span data-copy-text="66" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(52,26,30)" title="#66 mid currant red poly rgb(52,26,30)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>67</sub><br/><span data-copy-text="67" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(106,122,140)" title="#67 med regatta blue poly rgb(106,122,140)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>68</sub><br/><span data-copy-text="68" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(170,173,142)" title="#68 oxford white solid rgb(170,173,142)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>69</sub><br/><span data-copy-text="69" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(171,152,143)" title="#69 alabaster solid rgb(171,152,143)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>70</sub><br/><span data-copy-text="70" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(133,31,46)" title="#70 elec.currant red poly rgb(133,31,46)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>71</sub><br/><span data-copy-text="71" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(111,130,151)" title="#71 spinnaker blue solid rgb(111,130,151)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>72</sub><br/><span data-copy-text="72" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(88,88,83)" title="#72 dk.titanium poly rgb(88,88,83)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>73</sub><br/><span data-copy-text="73" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(154,167,144)" title="#73 pastel alabaster solid rgb(154,167,144)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>74</sub><br/><span data-copy-text="74" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(96,26,35)" title="#74 med.cabernet solid rgb(96,26,35)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>75</sub><br/><span data-copy-text="75" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(32,32,44)" title="#75 twilight blue poly rgb(32,32,44)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>76</sub><br/><span data-copy-text="76" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(164,160,150)" title="#76 titanium frost poly rgb(164,160,150)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>77</sub><br/><span data-copy-text="77" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(170,157,132)" title="#77 sandalwood frost poly rgb(170,157,132)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>78</sub><br/><span data-copy-text="78" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(120,34,43)" title="#78 wild strawberry poly rgb(120,34,43)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>79</sub><br/><span data-copy-text="79" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(14,49,109)" title="#79 ultra blue poly rgb(14,49,109)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>80</sub><br/><span data-copy-text="80" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(114,42,63)" title="#80 vermilion solid rgb(114,42,63)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>81</sub><br/><span data-copy-text="81" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(123,113,94)" title="#81 med.sandalwood poly rgb(123,113,94)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>82</sub><br/><span data-copy-text="82" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(116,29,40)" title="#82 med.red solid rgb(116,29,40)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>83</sub><br/><span data-copy-text="83" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(30,46,50)" title="#83 deep jewel green rgb(30,46,50)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>84</sub><br/><span data-copy-text="84" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(77,50,47)" title="#84 med.woodrose poly rgb(77,50,47)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>85</sub><br/><span data-copy-text="85" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(124,27,68)" title="#85 vermillion solid rgb(124,27,68)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>86</sub><br/><span data-copy-text="86" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(46,91,32)" title="#86 green rgb(46,91,32)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>87</sub><br/><span data-copy-text="87" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(57,90,131)" title="#87 bright blue poly rgb(57,90,131)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>88</sub><br/><span data-copy-text="88" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(109,40,55)" title="#88 bright red rgb(109,40,55)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>89</sub><br/><span data-copy-text="89" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(167,162,143)" title="#89 lt.champagne poly rgb(167,162,143)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>90</sub><br/><span data-copy-text="90" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(175,177,177)" title="#90 silver poly rgb(175,177,177)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>91</sub><br/><span data-copy-text="91" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(54,65,85)" title="#91 steel blue poly rgb(54,65,85)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>92</sub><br/><span data-copy-text="92" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(109,108,110)" title="#92 medium gray poly rgb(109,108,110)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>93</sub><br/><span data-copy-text="93" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(15,106,137)" title="#93 arctic pearl rgb(15,106,137)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>94</sub><br/><span data-copy-text="94" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(32,75,107)" title="#94 nassau blue poly rgb(32,75,107)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>95</sub><br/><span data-copy-text="95" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(43,62,87)" title="#95 med.sapphire blue poly rgb(43,62,87)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>96</sub><br/><span data-copy-text="96" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(155,159,157)" title="#96 silver poly rgb(155,159,157)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>97</sub><br/><span data-copy-text="97" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(108,132,149)" title="#97 lt.sapphire blue poly rgb(108,132,149)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>98</sub><br/><span data-copy-text="98" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(77,93,96)" title="#98 malachite poly rgb(77,93,96)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>99</sub><br/><span data-copy-text="99" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(174,155,127)" title="#99 flax rgb(174,155,127)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>100</sub><br/><span data-copy-text="100" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(64,108,143)" title="#100 med.maui blue poly rgb(64,108,143)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>101</sub><br/><span data-copy-text="101" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(31,37,59)" title="#101 dk.sapphire blue poly rgb(31,37,59)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>102</sub><br/><span data-copy-text="102" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(171,146,118)" title="#102 copper beige rgb(171,146,118)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>103</sub><br/><span data-copy-text="103" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(19,69,115)" title="#103 bright blue poly rgb(19,69,115)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>104</sub><br/><span data-copy-text="104" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(150,129,108)" title="#104 med.flax rgb(150,129,108)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>105</sub><br/><span data-copy-text="105" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(100,104,106)" title="#105 med.gray poly rgb(100,104,106)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>106</sub><br/><span data-copy-text="106" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(16,80,130)" title="#106 bright blue poly rgb(16,80,130)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>107</sub><br/><span data-copy-text="107" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(161,153,131)" title="#107 lt.driftwood poly rgb(161,153,131)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>108</sub><br/><span data-copy-text="108" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(56,86,148)" title="#108 blue rgb(56,86,148)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>109</sub><br/><span data-copy-text="109" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(82,86,97)" title="#109 steel gray poly rgb(82,86,97)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>110</sub><br/><span data-copy-text="110" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(127,105,86)" title="#110 lt.beechwood poly rgb(127,105,86)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>111</sub><br/><span data-copy-text="111" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(140,146,154)" title="#111 slate gray rgb(140,146,154)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>112</sub><br/><span data-copy-text="112" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(89,110,135)" title="#112 lt.sapphire blue poly rgb(89,110,135)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>113</sub><br/><span data-copy-text="113" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(71,53,50)" title="#113 dk.beechwood poly rgb(71,53,50)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>114</sub><br/><span data-copy-text="114" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(68,98,79)" title="#114 torch red rgb(68,98,79)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>115</sub><br/><span data-copy-text="115" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(115,10,39)" title="#115 bright red rgb(115,10,39)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>116</sub><br/><span data-copy-text="116" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(34,52,87)" title="#116 med.sapphire blue firemist rgb(34,52,87)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>117</sub><br/><span data-copy-text="117" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(100,13,27)" title="#117 med.garnet red poly rgb(100,13,27)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>118</sub><br/><span data-copy-text="118" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(163,173,198)" title="#118 white diamond pearl rgb(163,173,198)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>119</sub><br/><span data-copy-text="119" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(105,88,83)" title="#119 dk.sable poly rgb(105,88,83)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>120</sub><br/><span data-copy-text="120" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(155,139,128)" title="#120 antelope beige rgb(155,139,128)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>121</sub><br/><span data-copy-text="121" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(98,11,28)" title="#121 brilliant red poly rgb(98,11,28)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>122</sub><br/><span data-copy-text="122" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(91,93,94)" title="#122 gun metal poly rgb(91,93,94)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>123</sub><br/><span data-copy-text="123" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(98,68,40)" title="#123 med.beechwood poly rgb(98,68,40)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>124</sub><br/><span data-copy-text="124" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(115,24,39)" title="#124 brilliant red poly rgb(115,24,39)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>125</sub><br/><span data-copy-text="125" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(27,55,109)" title="#125 bright blue poly rgb(27,55,109)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>126</sub><br/><span data-copy-text="126" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(236,106,174)" title="#126 pink rgb(236,106,174)"></span></div>
</div>

---

### `0294` SET_CAN_RESPRAY_CAR
Makes car keep current colors when Pay'n'Spray is used

**Class:** `Car.SetCanRespray`

**Input:**
- `self: Car`
- `changeColors: bool`

---

### `02AA` SET_CAR_ONLY_DAMAGED_BY_PLAYER
Makes a vehicle immune to everything except the player

**Class:** `Car.SetOnlyDamagedByPlayer`

**Input:**
- `self: Car`
- `state: bool`

---

### `02AC` SET_CAR_PROOFS
Sets the vehicle's immunities

**Class:** `Car.SetProofs`

**Input:**
- `self: Car`
- `bulletProof: bool`
- `fireProof: bool`
- `explosionProof: bool`
- `collisionProof: bool`
- `meleeProof: bool`

---

### `02BF` IS_CAR_IN_WATER
Returns true if the vehicle is submerged in water

**Class:** `Car.IsInWater`
**Flags:** condition

**Input:**
- `self: Car`

---

### `02C2` CAR_GOTO_COORDINATES_ACCURATE
Makes the AI drive to the specified location obeying the traffic rules

**Class:** `Car.GotoCoordinatesAccurate`

**Input:**
- `self: Car`
- `x: float`
- `y: float`
- `z: float`

---

### `02CA` IS_CAR_ON_SCREEN
Returns true if the car is visible

**Class:** `Car.IsOnScreen`
**Flags:** condition

**Input:**
- `self: Car`

---

### `02E3` GET_CAR_SPEED
Gets the car's speed

**Class:** `Car.GetSpeed`

**Input:**
- `self: Car`

**Output:**
- `speed: float (variable)`

---

### `02F8` GET_CAR_FORWARD_X
Returns the X coord of the vehicle's angle

**Class:** `Car.GetForwardX`

**Input:**
- `self: Car`

**Output:**
- `x: float (variable)`

---

### `02F9` GET_CAR_FORWARD_Y
Returns the Y coord of the vehicle's angle

**Class:** `Car.GetForwardY`

**Input:**
- `self: Car`

**Output:**
- `y: float (variable)`

---

### `031E` HAS_CAR_BEEN_DAMAGED_BY_WEAPON
Returns true if the vehicle has been hit by the specified weapon

**Class:** `Car.HasBeenDamagedByWeapon`
**Flags:** condition

**Input:**
- `self: Car`
- `weaponType: WeaponType`

---

### `0338` SET_CAR_VISIBLE
Sets whether the vehicle is visible or not

**Class:** `Car.SetVisible`

**Input:**
- `self: Car`
- `state: bool`

---

### `0397` SWITCH_CAR_SIREN
Sets whether the car's alarm can be activated

**Class:** `Car.SwitchSiren`

**Input:**
- `self: Car`
- `state: bool`

---

### `039C` SET_CAR_WATERTIGHT
Makes the vehicle watertight, meaning characters inside will not be harmed if the vehicle is submerged in water

**Class:** `Car.SetWatertight`

**Input:**
- `self: Car`
- `state: bool`

---

### `039F` TURN_CAR_TO_FACE_COORD
Sets the car's heading so that it is facing the 2D coordinate

**Class:** `Car.TurnToFaceCoord`

**Input:**
- `self: Car`
- `x: float`
- `y: float`

---

### `03A2` SET_CAR_STATUS
Sets the car's status

**Class:** `Car.SetStatus`

**Input:**
- `self: Car`
- `status: EntityStatus`

---

### `03AB` SET_CAR_STRONG
Defines whether the car is more resistant to collisions than normal

**Class:** `Car.SetStrong`

**Input:**
- `self: Car`
- `state: bool`

---

### `03C9` IS_CAR_VISIBLY_DAMAGED
Returns true if any of the car components is visibly damaged or lost

**Class:** `Car.IsVisiblyDamaged`
**Flags:** condition

**Input:**
- `self: Car`

---

### `03ED` SET_UPSIDEDOWN_CAR_NOT_DAMAGED
Disables the car from exploding when it is upside down, as long as the player is not in the vehicle

**Class:** `Car.SetUpsidedownNotDamaged`

**Input:**
- `self: Car`
- `state: bool`

---

### `03F3` GET_CAR_COLOURS
Gets the car's primary and secondary colors

**Class:** `Car.GetColors`

**Input:**
- `self: Car`

**Output:**
- `color1: int (variable)`
- `color2: int (variable)`

**Details:**

Below table represents all colors used in the standard `carcols.dat` for GTA San Andreas. Click the color box to copy the id to the clipboard.

<div style="font-size:0">
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>0</sub><br/><span data-copy-text="0" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(0,0,0)" title="#0 black rgb(0,0,0)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>1</sub><br/><span data-copy-text="1" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(245,245,245)" title="#1 white rgb(245,245,245)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>2</sub><br/><span data-copy-text="2" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(42,119,161)" title="#2 police car blue rgb(42,119,161)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>3</sub><br/><span data-copy-text="3" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(132,4,16)" title="#3 cherry red rgb(132,4,16)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>4</sub><br/><span data-copy-text="4" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(38,55,57)" title="#4 midnight blue rgb(38,55,57)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>5</sub><br/><span data-copy-text="5" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(134,68,110)" title="#5 temple curtain purple rgb(134,68,110)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>6</sub><br/><span data-copy-text="6" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(215,142,16)" title="#6 taxi yellow rgb(215,142,16)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>7</sub><br/><span data-copy-text="7" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(76,117,183)" title="#7 striking blue rgb(76,117,183)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>8</sub><br/><span data-copy-text="8" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(189,190,198)" title="#8 light blue grey rgb(189,190,198)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>9</sub><br/><span data-copy-text="9" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(94,112,114)" title="#9 hoods rgb(94,112,114)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>10</sub><br/><span data-copy-text="10" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(70,89,122)" title="#10 saxony blue poly rgb(70,89,122)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>11</sub><br/><span data-copy-text="11" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(101,106,121)" title="#11 concord blue poly rgb(101,106,121)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>12</sub><br/><span data-copy-text="12" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(93,126,141)" title="#12 jasper green poly rgb(93,126,141)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>13</sub><br/><span data-copy-text="13" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(88,89,90)" title="#13 pewter gray poly rgb(88,89,90)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>14</sub><br/><span data-copy-text="14" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(214,218,214)" title="#14 frost white rgb(214,218,214)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>15</sub><br/><span data-copy-text="15" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(156,161,163)" title="#15 silver stone poly rgb(156,161,163)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>16</sub><br/><span data-copy-text="16" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(51,95,63)" title="#16 rio red rgb(51,95,63)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>17</sub><br/><span data-copy-text="17" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(115,14,26)" title="#17 torino red pearl rgb(115,14,26)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>18</sub><br/><span data-copy-text="18" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(123,10,42)" title="#18 formula red rgb(123,10,42)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>19</sub><br/><span data-copy-text="19" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(159,157,148)" title="#19 honey beige poly rgb(159,157,148)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>20</sub><br/><span data-copy-text="20" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(59,78,120)" title="#20 mariner blue rgb(59,78,120)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>21</sub><br/><span data-copy-text="21" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(115,46,62)" title="#21 blaze red rgb(115,46,62)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>22</sub><br/><span data-copy-text="22" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(105,30,59)" title="#22 classic red rgb(105,30,59)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>23</sub><br/><span data-copy-text="23" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(150,145,140)" title="#23 winning silver poly rgb(150,145,140)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>24</sub><br/><span data-copy-text="24" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(81,84,89)" title="#24 steel gray poly rgb(81,84,89)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>25</sub><br/><span data-copy-text="25" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(63,62,69)" title="#25 shadow silver poly rgb(63,62,69)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>26</sub><br/><span data-copy-text="26" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(165,169,167)" title="#26 silver stone poly rgb(165,169,167)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>27</sub><br/><span data-copy-text="27" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(99,92,90)" title="#27 warm grey mica rgb(99,92,90)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>28</sub><br/><span data-copy-text="28" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(61,74,104)" title="#28 harbor blue poly rgb(61,74,104)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>29</sub><br/><span data-copy-text="29" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(151,149,146)" title="#29 porcelain silver poly rgb(151,149,146)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>30</sub><br/><span data-copy-text="30" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(66,31,33)" title="#30 mellow burgundy rgb(66,31,33)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>31</sub><br/><span data-copy-text="31" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(95,39,43)" title="#31 graceful red mica rgb(95,39,43)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>32</sub><br/><span data-copy-text="32" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(132,148,171)" title="#32 currant blue poly rgb(132,148,171)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>33</sub><br/><span data-copy-text="33" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(118,123,124)" title="#33 gray poly rgb(118,123,124)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>34</sub><br/><span data-copy-text="34" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(100,100,100)" title="#34 arctic white rgb(100,100,100)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>35</sub><br/><span data-copy-text="35" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(90,87,82)" title="#35 anthracite gray poly rgb(90,87,82)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>36</sub><br/><span data-copy-text="36" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(37,37,39)" title="#36 black poly rgb(37,37,39)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>37</sub><br/><span data-copy-text="37" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(45,58,53)" title="#37 dark green poly rgb(45,58,53)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>38</sub><br/><span data-copy-text="38" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(147,163,150)" title="#38 seafoam poly rgb(147,163,150)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>39</sub><br/><span data-copy-text="39" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(109,122,136)" title="#39 diamond blue poly rgb(109,122,136)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>40</sub><br/><span data-copy-text="40" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(34,25,24)" title="#40 biston brown poly rgb(34,25,24)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>41</sub><br/><span data-copy-text="41" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(111,103,95)" title="#41 desert taupe poly rgb(111,103,95)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>42</sub><br/><span data-copy-text="42" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(124,28,42)" title="#42 garnet red poly rgb(124,28,42)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>43</sub><br/><span data-copy-text="43" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(95,10,21)" title="#43 desert red rgb(95,10,21)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>44</sub><br/><span data-copy-text="44" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(25,56,38)" title="#44 green rgb(25,56,38)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>45</sub><br/><span data-copy-text="45" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(93,27,32)" title="#45 cabernet red poly rgb(93,27,32)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>46</sub><br/><span data-copy-text="46" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(157,152,114)" title="#46 light ivory rgb(157,152,114)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>47</sub><br/><span data-copy-text="47" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(122,117,96)" title="#47 pueblo beige rgb(122,117,96)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>48</sub><br/><span data-copy-text="48" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(152,149,134)" title="#48 smoke silver poly rgb(152,149,134)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>49</sub><br/><span data-copy-text="49" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(173,176,176)" title="#49 astra silver poly rgb(173,176,176)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>50</sub><br/><span data-copy-text="50" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(132,137,136)" title="#50 ascot gray rgb(132,137,136)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>51</sub><br/><span data-copy-text="51" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(48,79,69)" title="#51 agate green rgb(48,79,69)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>52</sub><br/><span data-copy-text="52" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(77,98,104)" title="#52 petrol blue green poly rgb(77,98,104)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>53</sub><br/><span data-copy-text="53" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(22,34,72)" title="#53 surf blue rgb(22,34,72)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>54</sub><br/><span data-copy-text="54" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(39,47,75)" title="#54 nautical blue poly rgb(39,47,75)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>55</sub><br/><span data-copy-text="55" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(125,98,86)" title="#55 woodrose poly rgb(125,98,86)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>56</sub><br/><span data-copy-text="56" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(158,164,171)" title="#56 crystal blue poly rgb(158,164,171)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>57</sub><br/><span data-copy-text="57" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(156,141,113)" title="#57 bisque frost poly rgb(156,141,113)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>58</sub><br/><span data-copy-text="58" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(109,24,34)" title="#58 currant red solid rgb(109,24,34)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>59</sub><br/><span data-copy-text="59" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(78,104,129)" title="#59 lt.crystal blue poly rgb(78,104,129)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>60</sub><br/><span data-copy-text="60" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(156,156,152)" title="#60 lt.titanium poly rgb(156,156,152)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>61</sub><br/><span data-copy-text="61" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(145,115,71)" title="#61 race yellow solid rgb(145,115,71)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>62</sub><br/><span data-copy-text="62" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(102,28,38)" title="#62 brt.currant red poly rgb(102,28,38)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>63</sub><br/><span data-copy-text="63" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(148,157,159)" title="#63 clear crystal blue frost poly rgb(148,157,159)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>64</sub><br/><span data-copy-text="64" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(164,167,165)" title="#64 silver poly rgb(164,167,165)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>65</sub><br/><span data-copy-text="65" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(142,140,70)" title="#65 pastel alabaster rgb(142,140,70)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>66</sub><br/><span data-copy-text="66" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(52,26,30)" title="#66 mid currant red poly rgb(52,26,30)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>67</sub><br/><span data-copy-text="67" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(106,122,140)" title="#67 med regatta blue poly rgb(106,122,140)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>68</sub><br/><span data-copy-text="68" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(170,173,142)" title="#68 oxford white solid rgb(170,173,142)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>69</sub><br/><span data-copy-text="69" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(171,152,143)" title="#69 alabaster solid rgb(171,152,143)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>70</sub><br/><span data-copy-text="70" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(133,31,46)" title="#70 elec.currant red poly rgb(133,31,46)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>71</sub><br/><span data-copy-text="71" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(111,130,151)" title="#71 spinnaker blue solid rgb(111,130,151)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>72</sub><br/><span data-copy-text="72" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(88,88,83)" title="#72 dk.titanium poly rgb(88,88,83)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>73</sub><br/><span data-copy-text="73" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(154,167,144)" title="#73 pastel alabaster solid rgb(154,167,144)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>74</sub><br/><span data-copy-text="74" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(96,26,35)" title="#74 med.cabernet solid rgb(96,26,35)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>75</sub><br/><span data-copy-text="75" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(32,32,44)" title="#75 twilight blue poly rgb(32,32,44)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>76</sub><br/><span data-copy-text="76" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(164,160,150)" title="#76 titanium frost poly rgb(164,160,150)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>77</sub><br/><span data-copy-text="77" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(170,157,132)" title="#77 sandalwood frost poly rgb(170,157,132)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>78</sub><br/><span data-copy-text="78" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(120,34,43)" title="#78 wild strawberry poly rgb(120,34,43)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>79</sub><br/><span data-copy-text="79" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(14,49,109)" title="#79 ultra blue poly rgb(14,49,109)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>80</sub><br/><span data-copy-text="80" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(114,42,63)" title="#80 vermilion solid rgb(114,42,63)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>81</sub><br/><span data-copy-text="81" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(123,113,94)" title="#81 med.sandalwood poly rgb(123,113,94)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>82</sub><br/><span data-copy-text="82" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(116,29,40)" title="#82 med.red solid rgb(116,29,40)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>83</sub><br/><span data-copy-text="83" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(30,46,50)" title="#83 deep jewel green rgb(30,46,50)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>84</sub><br/><span data-copy-text="84" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(77,50,47)" title="#84 med.woodrose poly rgb(77,50,47)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>85</sub><br/><span data-copy-text="85" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(124,27,68)" title="#85 vermillion solid rgb(124,27,68)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>86</sub><br/><span data-copy-text="86" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(46,91,32)" title="#86 green rgb(46,91,32)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>87</sub><br/><span data-copy-text="87" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(57,90,131)" title="#87 bright blue poly rgb(57,90,131)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>88</sub><br/><span data-copy-text="88" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(109,40,55)" title="#88 bright red rgb(109,40,55)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>89</sub><br/><span data-copy-text="89" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(167,162,143)" title="#89 lt.champagne poly rgb(167,162,143)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>90</sub><br/><span data-copy-text="90" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(175,177,177)" title="#90 silver poly rgb(175,177,177)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>91</sub><br/><span data-copy-text="91" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(54,65,85)" title="#91 steel blue poly rgb(54,65,85)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>92</sub><br/><span data-copy-text="92" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(109,108,110)" title="#92 medium gray poly rgb(109,108,110)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>93</sub><br/><span data-copy-text="93" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(15,106,137)" title="#93 arctic pearl rgb(15,106,137)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>94</sub><br/><span data-copy-text="94" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(32,75,107)" title="#94 nassau blue poly rgb(32,75,107)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>95</sub><br/><span data-copy-text="95" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(43,62,87)" title="#95 med.sapphire blue poly rgb(43,62,87)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>96</sub><br/><span data-copy-text="96" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(155,159,157)" title="#96 silver poly rgb(155,159,157)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>97</sub><br/><span data-copy-text="97" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(108,132,149)" title="#97 lt.sapphire blue poly rgb(108,132,149)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>98</sub><br/><span data-copy-text="98" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(77,93,96)" title="#98 malachite poly rgb(77,93,96)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>99</sub><br/><span data-copy-text="99" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(174,155,127)" title="#99 flax rgb(174,155,127)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>100</sub><br/><span data-copy-text="100" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(64,108,143)" title="#100 med.maui blue poly rgb(64,108,143)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>101</sub><br/><span data-copy-text="101" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(31,37,59)" title="#101 dk.sapphire blue poly rgb(31,37,59)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>102</sub><br/><span data-copy-text="102" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(171,146,118)" title="#102 copper beige rgb(171,146,118)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>103</sub><br/><span data-copy-text="103" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(19,69,115)" title="#103 bright blue poly rgb(19,69,115)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>104</sub><br/><span data-copy-text="104" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(150,129,108)" title="#104 med.flax rgb(150,129,108)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>105</sub><br/><span data-copy-text="105" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(100,104,106)" title="#105 med.gray poly rgb(100,104,106)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>106</sub><br/><span data-copy-text="106" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(16,80,130)" title="#106 bright blue poly rgb(16,80,130)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>107</sub><br/><span data-copy-text="107" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(161,153,131)" title="#107 lt.driftwood poly rgb(161,153,131)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>108</sub><br/><span data-copy-text="108" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(56,86,148)" title="#108 blue rgb(56,86,148)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>109</sub><br/><span data-copy-text="109" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(82,86,97)" title="#109 steel gray poly rgb(82,86,97)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>110</sub><br/><span data-copy-text="110" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(127,105,86)" title="#110 lt.beechwood poly rgb(127,105,86)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>111</sub><br/><span data-copy-text="111" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(140,146,154)" title="#111 slate gray rgb(140,146,154)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>112</sub><br/><span data-copy-text="112" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(89,110,135)" title="#112 lt.sapphire blue poly rgb(89,110,135)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>113</sub><br/><span data-copy-text="113" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(71,53,50)" title="#113 dk.beechwood poly rgb(71,53,50)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>114</sub><br/><span data-copy-text="114" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(68,98,79)" title="#114 torch red rgb(68,98,79)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>115</sub><br/><span data-copy-text="115" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(115,10,39)" title="#115 bright red rgb(115,10,39)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>116</sub><br/><span data-copy-text="116" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(34,52,87)" title="#116 med.sapphire blue firemist rgb(34,52,87)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>117</sub><br/><span data-copy-text="117" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(100,13,27)" title="#117 med.garnet red poly rgb(100,13,27)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>118</sub><br/><span data-copy-text="118" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(163,173,198)" title="#118 white diamond pearl rgb(163,173,198)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>119</sub><br/><span data-copy-text="119" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(105,88,83)" title="#119 dk.sable poly rgb(105,88,83)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>120</sub><br/><span data-copy-text="120" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(155,139,128)" title="#120 antelope beige rgb(155,139,128)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>121</sub><br/><span data-copy-text="121" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(98,11,28)" title="#121 brilliant red poly rgb(98,11,28)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>122</sub><br/><span data-copy-text="122" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(91,93,94)" title="#122 gun metal poly rgb(91,93,94)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>123</sub><br/><span data-copy-text="123" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(98,68,40)" title="#123 med.beechwood poly rgb(98,68,40)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>124</sub><br/><span data-copy-text="124" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(115,24,39)" title="#124 brilliant red poly rgb(115,24,39)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>125</sub><br/><span data-copy-text="125" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(27,55,109)" title="#125 bright blue poly rgb(27,55,109)"></span></div>
<div style="display:inline-block;vertical-align:top;margin:0 8px 8px 0;text-align:center;font-size:12px;"><sub>126</sub><br/><span data-copy-text="126" style="display:inline-block;width:18px;height:18px;border:1px solid #ccc;border-radius:2px;background:rgb(236,106,174)" title="#126 pink rgb(236,106,174)"></span></div>
</div>

---

### `03F5` SET_CAR_CAN_BE_DAMAGED
Sets whether the car receives damage

**Class:** `Car.SetCanBeDamaged`

**Input:**
- `self: Car`
- `state: bool`

---

### `0407` GET_OFFSET_FROM_CAR_IN_WORLD_COORDS
Returns the coordinates of an offset of the vehicle's position, depending on the vehicle's rotation

**Class:** `Car.GetOffsetInWorldCoords`

**Input:**
- `self: Car`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0423` SET_CAR_TRACTION
Overrides the default AI controlled vehicle traction value of 1.0

**Class:** `Car.SetTraction`

**Input:**
- `self: Car`
- `traction: float`

---

### `0428` SET_CAR_AVOID_LEVEL_TRANSITIONS
Sets whether the vehicle will avoid paths between levels (0426)

**Class:** `Car.SetAvoidLevelTransitions`

**Input:**
- `self: Car`
- `state: bool`

---

### `0431` IS_CAR_PASSENGER_SEAT_FREE
Returns true if the specified car seat is empty

**Class:** `Car.IsPassengerSeatFree`
**Flags:** condition

**Input:**
- `self: Car`
- `seat: SeatId`

---

### `0432` GET_CHAR_IN_CAR_PASSENGER_SEAT
Returns the handle of a character sitting in the specified car seat

**Class:** `Car.GetCharInPassengerSeat`

**Input:**
- `self: Car`
- `seat: SeatId`

**Output:**
- `handle: Char (variable)`

---

### `0441` GET_CAR_MODEL
Returns the car's model id

**Class:** `Car.GetModel`

**Input:**
- `self: Car`

**Output:**
- `modelId: model_vehicle (variable)`

---

### `0466` SET_CAR_STAY_IN_FAST_LANE

**Class:** `Car.SetStayInFastLane`

**Input:**
- `self: Car`
- `state: bool`

---

### `0468` CLEAR_CAR_LAST_WEAPON_DAMAGE
Clears the vehicle's last weapon damage (see 031E)

**Class:** `Car.ClearLastWeaponDamage`

**Input:**
- `self: Car`

---

### `046C` GET_DRIVER_OF_CAR
Returns the car's driver handle

**Class:** `Car.GetDriver`

**Input:**
- `self: Car`

**Output:**
- `handle: Char (variable)`

---

### `0477` SET_CAR_TEMP_ACTION
Makes the AI driver perform the action in the vehicle for the specified period of time

**Class:** `Car.SetTempAction`

**Input:**
- `self: Car`
- `actionId: TempAction`
- `time: int`

---

### `048B` SET_CAR_RANDOM_ROUTE_SEED
Sets the car on a specific route

**Class:** `Car.SetRandomRouteSeed`

**Input:**
- `self: Car`
- `routeSeed: int`

---

### `0495` IS_CAR_ON_FIRE
Returns true if the car is burning

**Class:** `Car.IsOnFire`
**Flags:** condition

**Input:**
- `self: Car`

---

### `0496` IS_CAR_TYRE_BURST
Returns true if a given tire on the car is deflated

**Class:** `Car.IsTireBurst`
**Flags:** condition

**Input:**
- `self: Car`
- `tireId: WheelId`

---

### `04BA` SET_CAR_FORWARD_SPEED
Sets the speed of the car

**Class:** `Car.SetForwardSpeed`

**Input:**
- `self: Car`
- `forwardSpeed: float`

---

### `04BD` MARK_CAR_AS_CONVOY_CAR
Marks the car as being part of a convoy, which seems to follow a path set by 0994

**Class:** `Car.MarkAsConvoyCar`

**Input:**
- `self: Car`
- `state: bool`

---

### `04E0` SET_CAR_STRAIGHT_LINE_DISTANCE
Sets the minimum distance for the AI driver to start ignoring car paths and go straight to the target

**Class:** `Car.SetStraightLineDistance`

**Input:**
- `self: Car`
- `distance: int`

---

### `04E1` POP_CAR_BOOT
Opens the car's trunk and keeps it open

**Class:** `Car.PopBoot`

**Input:**
- `self: Car`

---

### `04F1` IS_CAR_WAITING_FOR_WORLD_COLLISION

**Class:** `Car.IsWaitingForWorldCollision`
**Flags:** condition

**Input:**
- `self: Car`

---

### `04FE` BURST_CAR_TYRE
Deflates the car's tire

**Class:** `Car.BurstTire`

**Input:**
- `self: Car`
- `tireId: WheelId`

---

### `0506` SET_CAR_MODEL_COMPONENTS
Sets the variation of the next car to be created

**Class:** `Car.SetModelComponents`
**Flags:** static

**Input:**
- `_unused: model_vehicle`
- `component1: int`
- `component2: int`

---

### `0508` CLOSE_ALL_CAR_DOORS
Closes all car doors, hoods and boots

**Class:** `Car.CloseAllDoors`

**Input:**
- `self: Car`

---

### `0519` FREEZE_CAR_POSITION
Locks the vehicle's position

**Class:** `Car.FreezePosition`

**Input:**
- `self: Car`
- `state: bool`

---

### `051C` HAS_CAR_BEEN_DAMAGED_BY_CHAR
Returns true if the car has been damaged by the specified char

**Class:** `Car.HasBeenDamagedByChar`
**Flags:** condition

**Input:**
- `self: Car`
- `handle: Char`

---

### `051D` HAS_CAR_BEEN_DAMAGED_BY_CAR
Returns true if the vehicle has been damaged by another specified vehicle

**Class:** `Car.HasBeenDamagedByCar`
**Flags:** condition

**Input:**
- `self: Car`
- `other: Car`

---

### `053F` SET_CAN_BURST_CAR_TYRES
Sets whether the car's tires can be deflated

**Class:** `Car.SetCanBurstTires`

**Input:**
- `self: Car`
- `state: bool`

---

### `054F` CLEAR_CAR_LAST_DAMAGE_ENTITY
Clears the car's last damage entity

**Class:** `Car.ClearLastDamageEntity`

**Input:**
- `self: Car`

---

### `056E` DOES_VEHICLE_EXIST
Returns true if the handle is a valid vehicle handle

**Class:** `Car.DoesExist`
**Flags:** condition, static

**Input:**
- `handle: any`

---

### `0574` FREEZE_CAR_POSITION_AND_DONT_LOAD_COLLISION
Makes the car maintain its position

**Class:** `Car.FreezePositionAndDontLoadCollision`

**Input:**
- `self: Car`
- `state: bool`

---

### `0587` SET_LOAD_COLLISION_FOR_CAR_FLAG

**Class:** `Car.SetLoadCollisionFlag`

**Input:**
- `self: Car`
- `state: bool`

---

### `0594` SET_VEHICLE_TO_FADE_IN
Sets the alpha transparency of a distant vehicle

**Class:** `Car.SetToFadeIn`

**Input:**
- `self: Car`
- `alpha: int`

---

### `05EB` START_PLAYBACK_RECORDED_CAR
Assigns a car to a path

**Class:** `Car.StartPlayback`

**Input:**
- `self: Car`
- `path: int`

---

### `05EC` STOP_PLAYBACK_RECORDED_CAR
Stops car from following path

**Class:** `Car.StopPlayback`

**Input:**
- `self: Car`

---

### `05ED` PAUSE_PLAYBACK_RECORDED_CAR
Freezes the car on its path

**Class:** `Car.PausePlayback`

**Input:**
- `self: Car`

---

### `05EE` UNPAUSE_PLAYBACK_RECORDED_CAR
Unfreezes the vehicle on its path

**Class:** `Car.UnpausePlayback`

**Input:**
- `self: Car`

---

### `05F1` SET_CAR_ESCORT_CAR_LEFT
Makes the vehicle stay on the other vehicle's left side, keeping parallel

**Class:** `Car.SetEscortCarLeft`

**Input:**
- `self: Car`
- `handle: Car`

---

### `05F2` SET_CAR_ESCORT_CAR_RIGHT
Makes the vehicle stay by the right side of the other vehicle, keeping parallel

**Class:** `Car.SetEscortCarRight`

**Input:**
- `self: Car`
- `handle: Car`

---

### `05F3` SET_CAR_ESCORT_CAR_REAR
Makes the vehicle stay behind the other car, keeping parallel

**Class:** `Car.SetEscortCarRear`

**Input:**
- `self: Car`
- `handle: Car`

---

### `05F4` SET_CAR_ESCORT_CAR_FRONT
Makes the vehicle stay in front of the other, keeping parallel

**Class:** `Car.SetEscortCarFront`

**Input:**
- `self: Car`
- `handle: Car`

---

### `060E` IS_PLAYBACK_GOING_ON_FOR_CAR
Returns true if the car is assigned to a path

**Class:** `Car.IsPlaybackGoingOn`
**Flags:** condition

**Input:**
- `self: Car`

---

### `0657` OPEN_CAR_DOOR
Opens the specified car door

**Class:** `Car.OpenDoor`

**Input:**
- `self: Car`
- `door: CarDoor`

---

### `0674` CUSTOM_PLATE_FOR_NEXT_CAR
Sets the numberplate of the next car to be spawned with the specified model

**Class:** `Car.CustomPlateForNextCar`
**Flags:** static

**Input:**
- `modelId: model_vehicle`
- `text: string`

---

### `067F` FORCE_CAR_LIGHTS
Sets an override for the car's lights

**Class:** `Car.ForceLights`

**Input:**
- `self: Car`
- `lightMode: CarLights`

---

### `0683` ATTACH_CAR_TO_CAR

**Class:** `Car.AttachToCar`

**Input:**
- `self: Car`
- `handle: Car`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `xRotation: float`
- `yRotation: float`
- `zRotation: float`

---

### `0684` DETACH_CAR
Detaches the car with optional rotation and force

**Class:** `Car.Detach`

**Input:**
- `self: Car`
- `pitch: float`
- `heading: float`
- `strength: float`
- `applyTurnForce: bool`

---

### `0686` IS_VEHICLE_ATTACHED

**Class:** `Car.IsAttached`
**Flags:** condition

**Input:**
- `self: Car`

---

### `0689` POP_CAR_DOOR
Removes the specified car door component from the car

**Class:** `Car.PopDoor`

**Input:**
- `self: Car`
- `door: CarDoor`
- `visibility: bool`

---

### `068A` FIX_CAR_DOOR
Repairs the car door

**Class:** `Car.FixDoor`

**Input:**
- `self: Car`
- `door: CarDoor`

---

### `068B` TASK_EVERYONE_LEAVE_CAR
Makes all passengers of the car leave it

**Class:** `Car.TaskEveryoneLeave`

**Input:**
- `self: Car`

---

### `0697` POP_CAR_PANEL
Detatches or deletes car's body part

**Class:** `Car.PopPanel`

**Input:**
- `self: Car`
- `panelId: CarPanel`
- `drop: bool`

---

### `0698` FIX_CAR_PANEL
Repairs or reinstalls car's body part

**Class:** `Car.FixPanel`

**Input:**
- `self: Car`
- `panelId: CarPanel`

---

### `0699` FIX_CAR_TYRE
Repairs a car's tire

**Class:** `Car.FixTire`

**Input:**
- `self: Car`
- `tireId: WheelId`

---

### `06A2` GET_CAR_SPEED_VECTOR

**Class:** `Car.GetSpeedVector`

**Input:**
- `self: Car`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `06A3` GET_CAR_MASS
Returns the vehicle's mass

**Class:** `Car.GetMass`

**Input:**
- `self: Car`

**Output:**
- `mass: float (variable)`

---

### `06BE` GET_CAR_ROLL
Returns the Y Angle of the vehicle

**Class:** `Car.GetRoll`

**Input:**
- `self: Car`

**Output:**
- `angle: float (variable)`

---

### `06C5` SKIP_TO_END_AND_STOP_PLAYBACK_RECORDED_CAR

**Class:** `Car.SkipToEndAndStopPlayback`

**Input:**
- `self: Car`

---

### `06E5` GET_AVAILABLE_VEHICLE_MOD
Returns a model id available for the vehicle's mod slot, or -1 otherwise

**Class:** `Car.GetAvailableMod`

**Input:**
- `self: Car`
- `slotId: ModSlot`

**Output:**
- `modelId: model_object (variable)`

---

### `06E7` ADD_VEHICLE_MOD
Adds a new mod with the model to the vehicle

**Class:** `Car.AddMod`

**Input:**
- `self: Car`
- `modelId: model_object`

**Output:**
- `handle: int (variable)`

---

### `06E8` REMOVE_VEHICLE_MOD
Removes the vehicle's mod with the specified model

**Class:** `Car.RemoveMod`

**Input:**
- `self: Car`
- `modelId: model_object`

---

### `06EC` GET_NUM_AVAILABLE_PAINTJOBS
Gets the number of possible paintjobs that can be applied to the car

**Class:** `Car.GetNumAvailablePaintjobs`

**Input:**
- `self: Car`

**Output:**
- `numPaintjobs: int (variable)`

---

### `06ED` GIVE_VEHICLE_PAINTJOB
Sets the car's paintjob

**Class:** `Car.GivePaintjob`

**Input:**
- `self: Car`
- `paintjobId: int`

---

### `06FC` DOES_CAR_HAVE_STUCK_CAR_CHECK
Returns true if the car has car stuck check enabled

**Class:** `Car.DoesHaveStuckCarCheck`
**Flags:** condition

**Input:**
- `self: Car`

---

### `06FD` SET_PLAYBACK_SPEED
Sets the playback speed of the car playing a car recording

**Class:** `Car.SetPlaybackSpeed`

**Input:**
- `self: Car`
- `speed: float`

---

### `0704` CAR_GOTO_COORDINATES_RACING
Makes the AI drive to the destination as fast as possible, trying to overtake other vehicles

**Class:** `Car.GotoCoordinatesRacing`

**Input:**
- `self: Car`
- `x: float`
- `y: float`
- `z: float`

---

### `0705` START_PLAYBACK_RECORDED_CAR_USING_AI
Starts the playback of a recorded car with driver AI enabled

**Class:** `Car.StartPlaybackUsingAi`

**Input:**
- `self: Car`
- `pathId: int`

---

### `0706` SKIP_IN_PLAYBACK_RECORDED_CAR
Advances the recorded car playback by the specified amount

**Class:** `Car.SkipInPlayback`

**Input:**
- `self: Car`
- `amount: float`

---

### `070C` EXPLODE_CAR_IN_CUTSCENE
Makes the vehicle explode without affecting its surroundings

**Class:** `Car.ExplodeInCutscene`

**Input:**
- `self: Car`

---

### `0714` SET_CAR_STAY_IN_SLOW_LANE

**Class:** `Car.SetStayInSlowLane`

**Input:**
- `self: Car`
- `state: bool`

---

### `0730` DAMAGE_CAR_PANEL
Damages a panel on the car

**Class:** `Car.DamagePanel`

**Input:**
- `self: Car`
- `panelId: int`

---

### `0731` SET_CAR_ROLL
Sets the Y Angle of the vehicle to the specified value

**Class:** `Car.SetRoll`

**Input:**
- `self: Car`
- `yAngle: float`

---

### `073B` SET_CAR_CAN_GO_AGAINST_TRAFFIC
Sets whether the vehicle will drive the wrong way on roads

**Class:** `Car.SetCanGoAgainstTraffic`

**Input:**
- `self: Car`
- `state: bool`

---

### `073C` DAMAGE_CAR_DOOR
Damages a component on the vehicle

**Class:** `Car.DamageDoor`

**Input:**
- `self: Car`
- `door: CarDoor`

---

### `0763` SET_CAR_AS_MISSION_CAR
Sets the script as the owner of the vehicle and adds it to the mission cleanup list

**Class:** `Car.SetAsMissionCar`

**Input:**
- `self: Car`

---

### `077D` GET_CAR_PITCH
Returns the X Angle of the vehicle

**Class:** `Car.GetPitch`

**Input:**
- `self: Car`

**Output:**
- `angle: float (variable)`

---

### `07C5` GET_VEHICLE_QUATERNION
Gets the quaternion values of the car

**Class:** `Car.GetQuaternion`

**Input:**
- `self: Car`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`
- `w: float (variable)`

---

### `07C6` SET_VEHICLE_QUATERNION
Sets the rotation of a vehicle using quaternion values

**Class:** `Car.SetQuaternion`

**Input:**
- `self: Car`
- `x: float`
- `y: float`
- `z: float`
- `w: float`

---

### `07D5` APPLY_FORCE_TO_CAR
Applies force to car with offset from its center of mass

**Class:** `Car.ApplyForce`

**Input:**
- `self: Car`
- `xDir: float`
- `yDir: float`
- `zDir: float`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`

---

### `07DA` ADD_TO_CAR_ROTATION_VELOCITY

**Class:** `Car.AddToRotationVelocity`

**Input:**
- `self: Car`
- `x: float`
- `y: float`
- `z: float`

---

### `07DB` SET_CAR_ROTATION_VELOCITY

**Class:** `Car.SetRotationVelocity`

**Input:**
- `self: Car`
- `x: float`
- `y: float`
- `z: float`

---

### `07EE` SET_CAR_ALWAYS_CREATE_SKIDS

**Class:** `Car.SetAlwaysCreateSkids`

**Input:**
- `self: Car`
- `state: bool`

---

### `07F5` CONTROL_CAR_HYDRAULICS
Changes the car wheels' suspension level

**Class:** `Car.ControlHydraulics`

**Input:**
- `self: Car`
- `frontLeftWheelSuspension: float`
- `rearLeftWheelSuspension: float`
- `frontRightWheelSuspension: float`
- `rearRightWheelSuspension: float`

---

### `07F8` SET_CAR_FOLLOW_CAR

**Class:** `Car.SetFollowCar`

**Input:**
- `self: Car`
- `handle: Car`
- `radius: float`

---

### `07FF` SET_CAR_HYDRAULICS
Enables hydraulic suspension on the car

**Class:** `Car.SetHydraulics`

**Input:**
- `self: Car`
- `state: bool`

---

### `0803` DOES_CAR_HAVE_HYDRAULICS
Returns true if the car has hydraulics installed

**Class:** `Car.DoesHaveHydraulics`
**Flags:** condition

**Input:**
- `self: Car`

---

### `081D` SET_CAR_ENGINE_BROKEN
Sets whether the car's engine is broken

**Class:** `Car.SetEngineBroken`

**Input:**
- `self: Car`
- `state: bool`

---

### `083F` GET_CAR_UPRIGHT_VALUE
Gets the car's vertical angle

**Class:** `Car.GetUprightValue`

**Input:**
- `self: Car`

**Output:**
- `value: float (variable)`

---

### `0840` SET_VEHICLE_AREA_VISIBLE

**Class:** `Car.SetAreaVisible`

**Input:**
- `self: Car`
- `interiorId: int`

---

### `0841` SELECT_WEAPONS_FOR_VEHICLE
Sets the vehicle to use its secondary guns

**Class:** `Car.SelectWeapons`

**Input:**
- `self: Car`
- `weapon: CarWeapon`

---

### `084E` SET_VEHICLE_CAN_BE_TARGETTED
Sets whether the vehicle can be targeted

**Class:** `Car.SetCanBeTargeted`

**Input:**
- `self: Car`
- `state: bool`

---

### `0852` SET_CAR_CAN_BE_VISIBLY_DAMAGED
Sets whether the vehicle can be visibly damaged

**Class:** `Car.SetCanBeVisiblyDamaged`

**Input:**
- `self: Car`
- `state: bool`

---

### `085E` START_PLAYBACK_RECORDED_CAR_LOOPED
Starts looped playback of a recorded car path

**Class:** `Car.StartPlaybackLooped`

**Input:**
- `self: Car`
- `pathId: int`

---

### `0878` SET_VEHICLE_DIRT_LEVEL
Sets the dirt level of the car

**Class:** `Car.SetDirtLevel`

**Input:**
- `self: Car`
- `level: float`

---

### `088B` SET_VEHICLE_AIR_RESISTANCE_MULTIPLIER
Sets the air resistance for the vehicle

**Class:** `Car.SetAirResistanceMultiplier`

**Input:**
- `self: Car`
- `multiplier: float`

---

### `088C` SET_CAR_COORDINATES_NO_OFFSET
Sets the vehicle coordinates without applying offsets to account for the height of the vehicle

**Class:** `Car.SetCoordinatesNoOffset`

**Input:**
- `self: Car`
- `x: float`
- `y: float`
- `z: float`

---

### `0897` IS_VEHICLE_TOUCHING_OBJECT
Returns true if the vehicle is in contact with the object

**Class:** `Car.IsTouchingObject`
**Flags:** condition

**Input:**
- `self: Car`
- `handle: Object`

---

### `08A4` CONTROL_MOVABLE_VEHICLE_PART
Sets the angle of a vehicle's extra

**Class:** `Car.ControlMovablePart`

**Input:**
- `self: Car`
- `range: float`

---

### `08A5` WINCH_CAN_PICK_VEHICLE_UP
Sets whether the vehicle can be picked up using the magnocrane

**Class:** `Car.WinchCanPickUp`

**Input:**
- `self: Car`
- `state: bool`

---

### `08A6` OPEN_CAR_DOOR_A_BIT
Sets the angle of a car door

**Class:** `Car.OpenDoorABit`

**Input:**
- `self: Car`
- `door: CarDoor`
- `value: float`

---

### `08A7` IS_CAR_DOOR_FULLY_OPEN

**Class:** `Car.IsDoorFullyOpen`
**Flags:** condition

**Input:**
- `self: Car`
- `door: CarDoor`

---

### `08CB` EXPLODE_CAR_IN_CUTSCENE_SHAKE_AND_BITS
Causes the vehicle to explode, without damage to surrounding entities

**Class:** `Car.ExplodeInCutsceneShakeAndBits`

**Input:**
- `self: Car`
- `shake: bool`
- `effect: bool`
- `sound: bool`

---

### `08EC` GET_VEHICLE_CLASS
Returns the vehicle's class as defined in vehicles.ide

**Class:** `Car.GetClass`

**Input:**
- `self: Car`

**Output:**
- `class: VehicleClass (variable)`

---

### `08F2` VEHICLE_CAN_BE_TARGETTED_BY_HS_MISSILE
Sets whether the player can target this vehicle with a heatseeking rocket launcher

**Class:** `Car.CanBeTargetedByHsMissile`

**Input:**
- `self: Car`
- `state: bool`

---

### `08F3` SET_FREEBIES_IN_VEHICLE
Sets whether the player can receive items from this vehicle, such as shotgun ammo from a police car and cash from a taxi

**Class:** `Car.SetFreebies`

**Input:**
- `self: Car`
- `state: bool`

---

### `0918` SET_CAR_ENGINE_ON
Sets whether the vehicle's engine is turned on or off

**Class:** `Car.SetEngineOn`

**Input:**
- `self: Car`
- `state: bool`

---

### `0919` SET_CAR_LIGHTS_ON
Sets whether the vehicle's lights are on

**Class:** `Car.SetLightsOn`

**Input:**
- `self: Car`
- `state: bool`

---

### `0939` ATTACH_CAR_TO_OBJECT
Attaches the car to object with offset and rotation

**Class:** `Car.AttachToObject`

**Input:**
- `self: Car`
- `handle: Object`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `xRotation: float`
- `yRotation: float`
- `zRotation: float`

---

### `0957` VEHICLE_DOES_PROVIDE_COVER
Sets whether characters in combat will choose to use the vehicle as cover from gunfire

**Class:** `Car.DoesProvideCover`

**Input:**
- `self: Car`
- `state: bool`

---

### `095E` CONTROL_CAR_DOOR
Sets the car's door angle and latch state

**Class:** `Car.ControlDoor`

**Input:**
- `self: Car`
- `door: CarDoor`
- `state: CarDoorState`
- `angle: float`

---

### `095F` GET_DOOR_ANGLE_RATIO
Gets the specified car doors angle, relative to the hinge

**Class:** `Car.GetDoorAngleRatio`

**Input:**
- `self: Car`
- `door: CarDoor`

**Output:**
- `ratio: float (variable)`

---

### `0969` IS_BIG_VEHICLE
Returns true if the specified vehicle has the 'is big' flag set in vehicles

**Class:** `Car.IsBig`
**Flags:** condition

**Input:**
- `self: Car`

---

### `096B` STORE_CAR_MOD_STATE

**Class:** `Car.StoreModState`
**Flags:** static

---

### `096C` RESTORE_CAR_MOD_STATE

**Class:** `Car.RestoreModState`
**Flags:** static

---

### `096D` GET_CURRENT_CAR_MOD
Returns the model of the component installed on the specified slot of the vehicle, or -1 otherwise

**Class:** `Car.GetCurrentMod`

**Input:**
- `self: Car`
- `slot: ModSlot`

**Output:**
- `modelId: model_object (variable)`

**Details:**

This command stores the model index of the car component in the selected slot of the vehicle. If the slot is not valid, the game will crash.

---

### `096E` IS_CAR_LOW_RIDER
Returns true if the vehicle is a low rider

**Class:** `Car.IsLowRider`
**Flags:** condition

**Input:**
- `self: Car`

---

### `096F` IS_CAR_STREET_RACER
Returns true if the vehicle is a street racer

**Class:** `Car.IsStreetRacer`
**Flags:** condition

**Input:**
- `self: Car`

**Details:**

This conditional command returns true if the vehicle is a street racer, i.e. the STREET_RACER flag is set for this vehicle in the handling.cfg file. By default the game will recognize the following list of vehicles as street racers:

- Elegy
- Jester
- Stratum
- Sultan
- Uranus

---

### `0975` IS_EMERGENCY_SERVICES_VEHICLE
Returns true if the vehicle is an emergency vehicle

**Class:** `Car.IsEmergencyServices`
**Flags:** condition

**Input:**
- `self: Car`

**Details:**

This command checks if the vehicle's model belongs to the emergency vehicle category. The list of emergency vehicles is predefined within the game and includes law enforcement vehicles, ambulances, and firetrucks:

* 407 (#FIRETRUK)
* 416 (#AMBULAN)
* 427 (#ENFORCER)
* 430 (#PREDATOR)
* 432 (#RHINO)
* 433 (#BARRACKS)
* 490 (#FBIRANCH)
* 523 (#COPBIKE)
* 528 (#FBITRUCK)
* 544 (#FIRELA)
* 596 (#COPCARLA)
* 597 (#COPCARSF)
* 598 (#COPCARVG)
* 599 (#COPCARRU)
* 601 (#SWATVAN)

---

### `097D` GET_NUM_CAR_COLOURS
Returns number of color variations defined for the model of this car in carcols.dat

**Class:** `Car.GetNumColors`

**Input:**
- `self: Car`

**Output:**
- `count: int (variable)`

---

### `0987` GET_CAR_BLOCKING_CAR
Returns a handle of the vehicle preventing this car from getting to its destination

**Class:** `Car.GetBlockingCar`

**Input:**
- `self: Car`

**Output:**
- `handle: Car (variable)`

---

### `0988` GET_CURRENT_VEHICLE_PAINTJOB
Gets the car's paintjob

**Class:** `Car.GetCurrentPaintjob`

**Input:**
- `self: Car`

**Output:**
- `paintjobNumber: int (variable)`

---

### `098D` GET_CAR_MOVING_COMPONENT_OFFSET
Sets the angle of a vehicle's extra

**Class:** `Car.GetMovingComponentOffset`

**Input:**
- `self: Car`

**Output:**
- `offset: float (variable)`

---

### `099A` SET_CAR_COLLISION

**Class:** `Car.SetCollision`

**Input:**
- `self: Car`
- `state: bool`

---

### `099B` CHANGE_PLAYBACK_TO_USE_AI
Changes vehicle control from playback to AI driven

**Class:** `Car.ChangePlaybackToUseAi`

**Input:**
- `self: Car`

---

### `09AB` RANDOM_PASSENGER_SAY
Makes a passenger in the vehicle speak from an ambient speech ID, if one exists for the character

**Class:** `Car.RandomPassengerSay`

**Input:**
- `self: Car`
- `phrase: SpeechId`

---

### `09B0` SET_VEHICLE_IS_CONSIDERED_BY_PLAYER
Makes player character ignore the car when enter vehicle key is used

**Class:** `Car.SetIsConsideredByPlayer`

**Input:**
- `self: Car`
- `state: bool`

---

### `09B3` GET_CAR_DOOR_LOCK_STATUS
Returns the door lock mode of the vehicle

**Class:** `Car.GetDoorLockStatus`

**Input:**
- `self: Car`

**Output:**
- `lockStatus: CarLock (variable)`

---

### `09BB` IS_CAR_DOOR_DAMAGED
Returns true if the specified vehicle part is visibly damaged

**Class:** `Car.IsDoorDamaged`
**Flags:** condition

**Input:**
- `self: Car`
- `door: CarDoor`

---

### `09C4` SET_PETROL_TANK_WEAKPOINT
Sets whether the car can be blown up by shooting at the petrol tank

**Class:** `Car.SetPetrolTankWeakpoint`

**Input:**
- `self: Car`
- `state: bool`

---

### `09CB` IS_CAR_TOUCHING_CAR
Returns true if the car is touching the other car

**Class:** `Car.IsTouchingCar`
**Flags:** condition

**Input:**
- `self: Car`
- `handle: Car`

---

### `09D0` IS_VEHICLE_ON_ALL_WHEELS
Returns true if all the vehicle's wheels are touching the ground

**Class:** `Car.IsOnAllWheels`
**Flags:** condition

**Input:**
- `self: Car`

---

### `09E1` GET_CAR_MODEL_VALUE
Returns the value of the specified car model

**Class:** `Car.GetModelValue`
**Flags:** static

**Input:**
- `model: model_vehicle`

**Output:**
- `value: int (variable)`

---

### `09E9` GIVE_NON_PLAYER_CAR_NITRO
Makes the car have one nitro

**Class:** `Car.GiveNonPlayerNitro`

**Input:**
- `self: Car`

---

### `09FE` RESET_VEHICLE_HYDRAULICS
This resets all the hydraulics on the car, making it "sit"

**Class:** `Car.ResetHydraulics`

**Input:**
- `self: Car`

---

### `0A11` SET_EXTRA_CAR_COLOURS
Sets the car's ternary and quaternary colors. See also 0229

**Class:** `Car.SetExtraColors`

**Input:**
- `self: Car`
- `color3: int`
- `color4: int`

---

### `0A12` GET_EXTRA_CAR_COLOURS
Returns the car's tertiary and quaternary colors. See also 03F3

**Class:** `Car.GetExtraColors`

**Input:**
- `self: Car`

**Output:**
- `color3: int (variable)`
- `color4: int (variable)`

---

### `0A15` HAS_CAR_BEEN_RESPRAYED
Returns true if the vehicle was resprayed in the last frame AND resets the resprayed state to false

**Class:** `Car.HasBeenResprayed`
**Flags:** condition

**Input:**
- `self: Car`

---

### `0A21` IMPROVE_CAR_BY_CHEATING
Sets whether a ped driven vehicle's handling is affected by the 'perfect handling' cheat

**Class:** `Car.ImproveByCheating`

**Input:**
- `self: Car`
- `state: bool`

---

### `0A30` FIX_CAR
Restores the vehicle to full health and removes the damage

**Class:** `Car.Fix`

**Input:**
- `self: Car`

**Details:**

This command fixes the vehicle from all damages done to it, including all physical damages like damaged panels or popped tires.

---
