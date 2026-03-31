# Object Opcodes

> 87 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0107` | CREATE_OBJECT | Creates an object at the specified location, with the specified model |
| `0108` | DELETE_OBJECT | Destroys the object, freeing game memory |
| `0176` | GET_OBJECT_HEADING | Returns the object's heading (z-angle) |
| `0177` | SET_OBJECT_HEADING | Sets the object's heading (z-angle) |
| `01BB` | GET_OBJECT_COORDINATES | Returns the object's coordinates |
| `01BC` | SET_OBJECT_COORDINATES | Puts the object at the specified location |
| `01C4` | MARK_OBJECT_AS_NO_LONGER_NEEDED | Allows the object to be deleted by the game if necessary, and also removes it fr |
| `01C7` | DONT_REMOVE_OBJECT | Removes the object from the mission cleanup list, preventing it from being delet |
| `029B` | CREATE_OBJECT_NO_OFFSET | Creates an object without offset at the location |
| `02CC` | IS_OBJECT_ON_SCREEN | Returns true if the object is visible |
| `034D` | ROTATE_OBJECT | Rotates the object from one angle to another, optionally accounting for a collis |
| `034E` | SLIDE_OBJECT | Animates object movement toward specified coordinates. Returns true if the objec |
| `035C` | PLACE_OBJECT_RELATIVE_TO_CAR | Places the object at an offset from the car |
| `035D` | MAKE_OBJECT_TARGETTABLE | Sets whether the object can be targeted (auto-aimed) or not |
| `0366` | HAS_OBJECT_BEEN_DAMAGED | Returns true if the object is damaged |
| `0381` | SET_OBJECT_VELOCITY | Sets the object's velocity |
| `0382` | SET_OBJECT_COLLISION | Sets the object's collision detection |
| `038C` | ADD_TO_OBJECT_VELOCITY | Adds the given vector to the object's velocity (0381) |
| `0392` | SET_OBJECT_DYNAMIC | Defines whether or not the object is moveable |
| `03CA` | DOES_OBJECT_EXIST | Returns true if the handle is a valid object handle |
| `0400` | GET_OFFSET_FROM_OBJECT_IN_WORLD_COORDS | Returns the object's coordinates with an offset |
| `0418` | SET_OBJECT_DRAW_LAST | Sets the specified object to always draw on top of other objects |
| `0453` | SET_OBJECT_ROTATION | Sets the object rotation along X, Y and Z axis |
| `04D9` | SET_OBJECT_RECORDS_COLLISIONS | Enables the use of collision checking for the object |
| `04DA` | HAS_OBJECT_COLLIDED_WITH_ANYTHING | Returns true if the object has collided |
| `04E5` | LOCATE_OBJECT_2D | Returns true if the object is near the specified coordinates |
| `04E6` | LOCATE_OBJECT_3D | Returns true if the object is near the specified point |
| `04E7` | IS_OBJECT_IN_WATER | Returns true if the object is in water |
| `04E9` | IS_OBJECT_IN_AREA_2D | Returns true if object is in the specified area |
| `04EA` | IS_OBJECT_IN_AREA_3D | Returns true if the object is in the specified area |
| `050E` | SORT_OUT_OBJECT_COLLISION_WITH_CAR | Makes the specified car have no collision with the specified object |
| `0550` | FREEZE_OBJECT_POSITION | Sets whether the object's position remains unchanged |
| `0566` | SET_OBJECT_AREA_VISIBLE | Sets the visibility of the object to the specified interior |
| `059F` | GET_OBJECT_VELOCITY | Returns the object's X, Y, and Z velocity |
| `05A1` | ADD_TO_OBJECT_ROTATION_VELOCITY | Sets the object's rotation velocity from the center of its body |
| `05A2` | SET_OBJECT_ROTATION_VELOCITY | Sets the object's rotation velocity with frame sync applied? |
| `05A3` | IS_OBJECT_STATIC | Returns true if the object is not moving |
| `05A6` | GET_OBJECT_ROTATION_VELOCITY |  |
| `05A7` | ADD_VELOCITY_RELATIVE_TO_OBJECT_VELOCITY | Sets the object's velocity |
| `05A8` | GET_OBJECT_SPEED | Gets the speed of the object |
| `0654` | SET_OBJECT_RENDER_SCORCHED | Makes the object look like it has been burnt |
| `0681` | ATTACH_OBJECT_TO_CAR |  |
| `0682` | DETACH_OBJECT | Detaches the object with optional rotation and force |
| `0685` | IS_OBJECT_ATTACHED |  |
| `069A` | ATTACH_OBJECT_TO_OBJECT |  |
| `069B` | ATTACH_OBJECT_TO_CHAR |  |
| `071E` | GET_OBJECT_HEALTH |  |
| `071F` | SET_OBJECT_HEALTH |  |
| `0723` | BREAK_OBJECT | Smashes the object to pieces |
| `0750` | SET_OBJECT_VISIBLE | Sets whether the object is visible |
| `075A` | PLAY_OBJECT_ANIM | Plays an object animation |
| `0796` | GET_ROPE_HEIGHT_FOR_OBJECT |  |
| `0797` | SET_ROPE_HEIGHT_FOR_OBJECT |  |
| `0798` | GRAB_ENTITY_ON_ROPE_FOR_OBJECT |  |
| `0799` | RELEASE_ENTITY_FROM_ROPE_FOR_OBJECT |  |
| `07C3` | GET_OBJECT_QUATERNION | Gets the object's quaternion |
| `07C4` | SET_OBJECT_QUATERNION | Sets the object's quaternion |
| `07F7` | SET_OBJECT_COLLISION_DAMAGE_EFFECT | Sets whether the object can be destroyed or not |
| `080A` | GET_LEVEL_DESIGN_COORDS_FOR_OBJECT |  |
| `0815` | SET_OBJECT_COORDINATES_AND_VELOCITY | Sets the object's coordinates without affecting the rotation |
| `0827` | CONNECT_LODS | Sets which LOD object should show when the object is being viewed from far away |
| `0833` | HAS_OBJECT_BEEN_PHOTOGRAPHED | Returns true if the object has been photographed |
| `0836` | SET_OBJECT_ANIM_SPEED | Sets the object's animation speed |
| `0837` | IS_OBJECT_PLAYING_ANIM | Returns true if the object is playing the specified animation |
| `0839` | GET_OBJECT_ANIM_CURRENT_TIME | Gets the current progress of the object's animation |
| `083A` | SET_OBJECT_ANIM_CURRENT_TIME | Sets the progress of an animation, with 0 |
| `0875` | SET_OBJECT_ONLY_DAMAGED_BY_PLAYER | Makes the object damageable only by the player |
| `08D2` | SET_OBJECT_SCALE | Sets the scale of the object |
| `08E3` | IS_OBJECT_IN_ANGLED_AREA_2D | Checks if the object is within the angled 2D area |
| `08E4` | IS_OBJECT_IN_ANGLED_AREA_3D | Checks if the object is within the angled 3D area |
| `08E9` | SET_OBJECT_AS_STEALABLE | Sets whether the object can be picked up and carried |
| `08FF` | HAS_OBJECT_BEEN_DAMAGED_BY_WEAPON | Returns true if the object has been damaged by the specified weapon or damage ty |
| `0900` | CLEAR_OBJECT_LAST_WEAPON_DAMAGE | Clears the object's last damaging weapon ID |
| `0905` | LOCK_DOOR | Sets whether the door object is locked at its current rotation and allows it to  |
| `0906` | SET_OBJECT_MASS | Sets the object's mass |
| `0907` | GET_OBJECT_MASS | Returns the object's mass |
| `0908` | SET_OBJECT_TURN_MASS | Sets the object's turn mass |
| `0909` | GET_OBJECT_TURN_MASS | Returns the object's turn mass |
| `0916` | WINCH_CAN_PICK_OBJECT_UP | Sets whether the object can be picked up with the magnocrane |
| `095B` | HAS_OBJECT_BEEN_UPROOTED | Returns true if the object has been made moveable by the 0392 |
| `0977` | IS_OBJECT_WITHIN_BRAIN_ACTIVATION_RANGE | Returns true if the object is within the external script trigger radius |
| `0984` | GET_OBJECT_MODEL | Returns the object's model index |
| `09A2` | REMOVE_OBJECT_ELEGANTLY | Fades the object out of existence, freeing game memory |
| `09CA` | SET_OBJECT_PROOFS | Sets what immunities the object has |
| `09CC` | DOES_OBJECT_HAVE_THIS_MODEL | Returns true if the object's model is the model specified |
| `09FC` | IS_OBJECT_INTERSECTING_WORLD | Appears to return true if something had entered the object's position since it w |
| `0A0A` | ENABLE_DISABLED_ATTRACTORS_ON_OBJECT | Sets whether the object attracts spawned peds to interact with it |

## Detailed Reference

### `0107` CREATE_OBJECT
Creates an object at the specified location, with the specified model

**Class:** `Object.Create`
**Flags:** constructor

**Input:**
- `modelId: model_object`
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `handle: Object (variable)`

**Details:**

This command creates an object at the coordinates point. The z-coordinate uses the base rather than the center of the object's bounding box. Use CREATE_OBJECT_NO_OFFSET to create an object without this offset. It is not required to load the model (like through REQUEST_MODEL) to create the object. The object must already have an entry in the `object.dat` file in order for them to be stable. Without an entry, the object can become unstable and when that happens the game will crash.

---

### `0108` DELETE_OBJECT
Destroys the object, freeing game memory

**Class:** `Object.Delete`
**Flags:** destructor

**Input:**
- `self: Object`

---

### `0176` GET_OBJECT_HEADING
Returns the object's heading (z-angle)

**Class:** `Object.GetHeading`

**Input:**
- `self: Object`

**Output:**
- `heading: float (variable)`

---

### `0177` SET_OBJECT_HEADING
Sets the object's heading (z-angle)

**Class:** `Object.SetHeading`

**Input:**
- `self: Object`
- `heading: float`

---

### `01BB` GET_OBJECT_COORDINATES
Returns the object's coordinates

**Class:** `Object.GetCoordinates`

**Input:**
- `self: Object`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `01BC` SET_OBJECT_COORDINATES
Puts the object at the specified location

**Class:** `Object.SetCoordinates`

**Input:**
- `self: Object`
- `x: float`
- `y: float`
- `z: float`

---

### `01C4` MARK_OBJECT_AS_NO_LONGER_NEEDED
Allows the object to be deleted by the game if necessary, and also removes it from the mission cleanup list, if applicable

**Class:** `Object.MarkAsNoLongerNeeded`

**Input:**
- `self: Object`

---

### `01C7` DONT_REMOVE_OBJECT
Removes the object from the mission cleanup list, preventing it from being deleted when the mission ends

**Class:** `Object.DontRemove`

**Input:**
- `self: Object`

---

### `029B` CREATE_OBJECT_NO_OFFSET
Creates an object without offset at the location

**Class:** `Object.CreateNoOffset`
**Flags:** constructor

**Input:**
- `modelId: model_object`
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `handle: Object (variable)`

---

### `02CC` IS_OBJECT_ON_SCREEN
Returns true if the object is visible

**Class:** `Object.IsOnScreen`
**Flags:** condition

**Input:**
- `self: Object`

---

### `034D` ROTATE_OBJECT
Rotates the object from one angle to another, optionally accounting for a collision during the rotation

**Class:** `Object.Rotate`
**Flags:** condition

**Input:**
- `self: Object`
- `fromAngle: float`
- `toAngle: float`
- `collisionCheck: bool`

---

### `034E` SLIDE_OBJECT
Animates object movement toward specified coordinates. Returns true if the object has finished moving

**Class:** `Object.Slide`
**Flags:** condition

**Input:**
- `self: Object`
- `posX: float`
- `posY: float`
- `posZ: float`
- `speedX: float`
- `speedY: float`
- `speedZ: float`
- `collisionCheck: bool`

---

### `035C` PLACE_OBJECT_RELATIVE_TO_CAR
Places the object at an offset from the car

**Class:** `Object.PlaceRelativeToCar`

**Input:**
- `self: Object`
- `vehicle: Car`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`

---

### `035D` MAKE_OBJECT_TARGETTABLE
Sets whether the object can be targeted (auto-aimed) or not

**Class:** `Object.MakeTargetable`

**Input:**
- `self: Object`
- `state: bool`

---

### `0366` HAS_OBJECT_BEEN_DAMAGED
Returns true if the object is damaged

**Class:** `Object.HasBeenDamaged`
**Flags:** condition

**Input:**
- `self: Object`

---

### `0381` SET_OBJECT_VELOCITY
Sets the object's velocity

**Class:** `Object.SetVelocity`

**Input:**
- `self: Object`
- `xSpeed: float`
- `ySpeed: float`
- `zSpeed: float`

---

### `0382` SET_OBJECT_COLLISION
Sets the object's collision detection

**Class:** `Object.SetCollision`

**Input:**
- `self: Object`
- `state: bool`

---

### `038C` ADD_TO_OBJECT_VELOCITY
Adds the given vector to the object's velocity (0381)

**Class:** `Object.AddToVelocity`

**Input:**
- `self: Object`
- `x: float`
- `y: float`
- `z: float`

---

### `0392` SET_OBJECT_DYNAMIC
Defines whether or not the object is moveable

**Class:** `Object.SetDynamic`

**Input:**
- `self: Object`
- `state: bool`

---

### `03CA` DOES_OBJECT_EXIST
Returns true if the handle is a valid object handle

**Class:** `Object.DoesExist`
**Flags:** condition, static

**Input:**
- `handle: any`

**Details:**

This command checks if the input is a valid object handle. If the handle is not associated with any existing object, the result is false.

Although, this command generally works fine with invalid handles, very large values (e.g. 250000000) may crash the game. To safely check if the handle is valid, use GET_OBJECT_POINTER with CLEO 5:

```
int ptr = get_object_pointer [handle]
if is_truthy ptr
then
// handle valid
end
```

---

### `0400` GET_OFFSET_FROM_OBJECT_IN_WORLD_COORDS
Returns the object's coordinates with an offset

**Class:** `Object.GetOffsetInWorldCoords`

**Input:**
- `self: Object`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0418` SET_OBJECT_DRAW_LAST
Sets the specified object to always draw on top of other objects

**Class:** `Object.SetDrawLast`

**Input:**
- `self: Object`
- `state: bool`

---

### `0453` SET_OBJECT_ROTATION
Sets the object rotation along X, Y and Z axis

**Class:** `Object.SetRotation`

**Input:**
- `self: Object`
- `x: float`
- `y: float`
- `z: float`

---

### `04D9` SET_OBJECT_RECORDS_COLLISIONS
Enables the use of collision checking for the object

**Class:** `Object.SetRecordsCollisions`

**Input:**
- `self: Object`
- `state: bool`

---

### `04DA` HAS_OBJECT_COLLIDED_WITH_ANYTHING
Returns true if the object has collided

**Class:** `Object.HasCollidedWithAnything`
**Flags:** condition

**Input:**
- `self: Object`

---

### `04E5` LOCATE_OBJECT_2D
Returns true if the object is near the specified coordinates

**Class:** `Object.Locate2D`
**Flags:** condition

**Input:**
- `self: Object`
- `x: float`
- `y: float`
- `xRadius: float`
- `yRadius: float`
- `drawSphere: bool`

---

### `04E6` LOCATE_OBJECT_3D
Returns true if the object is near the specified point

**Class:** `Object.Locate3D`
**Flags:** condition

**Input:**
- `self: Object`
- `x: float`
- `y: float`
- `z: float`
- `xRadius: float`
- `yRadius: float`
- `zRadius: float`
- `drawSphere: bool`

---

### `04E7` IS_OBJECT_IN_WATER
Returns true if the object is in water

**Class:** `Object.IsInWater`
**Flags:** condition

**Input:**
- `self: Object`

---

### `04E9` IS_OBJECT_IN_AREA_2D
Returns true if object is in the specified area

**Class:** `Object.IsInArea2D`
**Flags:** condition

**Input:**
- `self: Object`
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `drawSphere: bool`

---

### `04EA` IS_OBJECT_IN_AREA_3D
Returns true if the object is in the specified area

**Class:** `Object.IsInArea3D`
**Flags:** condition

**Input:**
- `self: Object`
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `drawSphere: bool`

---

### `050E` SORT_OUT_OBJECT_COLLISION_WITH_CAR
Makes the specified car have no collision with the specified object

**Class:** `Object.SortOutCollisionWithCar`

**Input:**
- `self: Object`
- `handle: Car`

---

### `0550` FREEZE_OBJECT_POSITION
Sets whether the object's position remains unchanged

**Class:** `Object.FreezePosition`

**Input:**
- `self: Object`
- `state: bool`

---

### `0566` SET_OBJECT_AREA_VISIBLE
Sets the visibility of the object to the specified interior

**Class:** `Object.SetAreaVisible`

**Input:**
- `self: Object`
- `areaId: int`

---

### `059F` GET_OBJECT_VELOCITY
Returns the object's X, Y, and Z velocity

**Class:** `Object.GetVelocity`

**Input:**
- `self: Object`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `05A1` ADD_TO_OBJECT_ROTATION_VELOCITY
Sets the object's rotation velocity from the center of its body

**Class:** `Object.AddToRotationVelocity`

**Input:**
- `self: Object`
- `x: float`
- `y: float`
- `z: float`

---

### `05A2` SET_OBJECT_ROTATION_VELOCITY
Sets the object's rotation velocity with frame sync applied?

**Class:** `Object.SetRotationVelocity`

**Input:**
- `self: Object`
- `x: float`
- `y: float`
- `z: float`

---

### `05A3` IS_OBJECT_STATIC
Returns true if the object is not moving

**Class:** `Object.IsStatic`
**Flags:** condition

**Input:**
- `self: Object`

---

### `05A6` GET_OBJECT_ROTATION_VELOCITY

**Class:** `Object.GetRotationVelocity`

**Input:**
- `self: Object`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `05A7` ADD_VELOCITY_RELATIVE_TO_OBJECT_VELOCITY
Sets the object's velocity

**Class:** `Object.AddVelocityRelative`

**Input:**
- `self: Object`
- `x: float`
- `y: float`
- `z: float`

---

### `05A8` GET_OBJECT_SPEED
Gets the speed of the object

**Class:** `Object.GetSpeed`

**Input:**
- `self: Object`

**Output:**
- `speed: float (variable)`

---

### `0654` SET_OBJECT_RENDER_SCORCHED
Makes the object look like it has been burnt

**Class:** `Object.SetRenderScorched`

**Input:**
- `self: Object`
- `state: bool`

---

### `0681` ATTACH_OBJECT_TO_CAR

**Class:** `Object.AttachToCar`

**Input:**
- `self: Object`
- `handle: Car`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `xRotation: float`
- `yRotation: float`
- `zRotation: float`

---

### `0682` DETACH_OBJECT
Detaches the object with optional rotation and force

**Class:** `Object.Detach`

**Input:**
- `self: Object`
- `pitch: float`
- `heading: float`
- `strength: float`
- `applyTurnForce: bool`

---

### `0685` IS_OBJECT_ATTACHED

**Class:** `Object.IsAttached`
**Flags:** condition

**Input:**
- `self: Object`

---

### `069A` ATTACH_OBJECT_TO_OBJECT

**Class:** `Object.AttachToObject`

**Input:**
- `self: Object`
- `handle: Object`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `xRotation: float`
- `yRotation: float`
- `zRotation: float`

---

### `069B` ATTACH_OBJECT_TO_CHAR

**Class:** `Object.AttachToChar`

**Input:**
- `self: Object`
- `handle: Char`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `xRotation: float`
- `yRotation: float`
- `zRotation: float`

---

### `071E` GET_OBJECT_HEALTH

**Class:** `Object.GetHealth`

**Input:**
- `self: Object`

**Output:**
- `health: int (variable)`

---

### `071F` SET_OBJECT_HEALTH

**Class:** `Object.SetHealth`

**Input:**
- `self: Object`
- `health: int`

---

### `0723` BREAK_OBJECT
Smashes the object to pieces

**Class:** `Object.Break`

**Input:**
- `self: Object`
- `intensity: int`

---

### `0750` SET_OBJECT_VISIBLE
Sets whether the object is visible

**Class:** `Object.SetVisible`

**Input:**
- `self: Object`
- `state: bool`

---

### `075A` PLAY_OBJECT_ANIM
Plays an object animation

**Class:** `Object.PlayAnim`

**Input:**
- `self: Object`
- `animationName: string`
- `animationFile: string`
- `frameDelta: float`
- `lockF: bool`
- `loop: bool`

---

### `0796` GET_ROPE_HEIGHT_FOR_OBJECT

**Class:** `Object.GetRopeHeight`

**Input:**
- `self: Object`

**Output:**
- `height: float (variable)`

---

### `0797` SET_ROPE_HEIGHT_FOR_OBJECT

**Class:** `Object.SetRopeHeight`

**Input:**
- `self: Object`
- `height: float`

---

### `0798` GRAB_ENTITY_ON_ROPE_FOR_OBJECT

**Class:** `Object.GrabEntityOnRope`

**Input:**
- `self: Object`

**Output:**
- `vehicle: Car (variable)`
- `char: Char (variable)`
- `object: Object (variable)`

---

### `0799` RELEASE_ENTITY_FROM_ROPE_FOR_OBJECT

**Class:** `Object.ReleaseEntityFromRope`

**Input:**
- `self: Object`

---

### `07C3` GET_OBJECT_QUATERNION
Gets the object's quaternion

**Class:** `Object.GetQuaternion`

**Input:**
- `self: Object`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`
- `w: float (variable)`

---

### `07C4` SET_OBJECT_QUATERNION
Sets the object's quaternion

**Class:** `Object.SetQuaternion`

**Input:**
- `self: Object`
- `x: float`
- `y: float`
- `z: float`
- `w: float`

---

### `07F7` SET_OBJECT_COLLISION_DAMAGE_EFFECT
Sets whether the object can be destroyed or not

**Class:** `Object.SetCollisionDamageEffect`

**Input:**
- `self: Object`
- `state: bool`

---

### `080A` GET_LEVEL_DESIGN_COORDS_FOR_OBJECT

**Class:** `Object.GetLevelDesignCoords`

**Input:**
- `self: Object`
- `nth: int`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0815` SET_OBJECT_COORDINATES_AND_VELOCITY
Sets the object's coordinates without affecting the rotation

**Class:** `Object.SetCoordinatesAndVelocity`

**Input:**
- `self: Object`
- `x: float`
- `y: float`
- `z: float`

---

### `0827` CONNECT_LODS
Sets which LOD object should show when the object is being viewed from far away

**Class:** `Object.ConnectLods`

**Input:**
- `self: Object`
- `lodObject: Object`

**Details:**

This command connects the object to the LOD object. Objects created by the script (e.g. CREATE_OBJECT) do not have an LOD associated to it, even if the object was assigned an LOD in the IPL file. The object is normally the one seen up close and its LOD is normally the one seen far away.  
  
The command adds a new entry to the **TheScripts::ScriptConnectLodsObjects** list. Deleting the object(s) does not remove their record from the list! The list is saved in the save game file and processed after the game loads, causing crashes if the object(s) no longer exists!  
By default, there is no way to remove record from the list. If an object with a registered LOD has to be removed, the **TheScripts::ScriptConnectLodsObjects** list entry must be removed manually with memory commands.

---

### `0833` HAS_OBJECT_BEEN_PHOTOGRAPHED
Returns true if the object has been photographed

**Class:** `Object.HasBeenPhotographed`
**Flags:** condition

**Input:**
- `self: Object`

---

### `0836` SET_OBJECT_ANIM_SPEED
Sets the object's animation speed

**Class:** `Object.SetAnimSpeed`

**Input:**
- `self: Object`
- `animationName: string`
- `speed: float`

---

### `0837` IS_OBJECT_PLAYING_ANIM
Returns true if the object is playing the specified animation

**Class:** `Object.IsPlayingAnim`
**Flags:** condition

**Input:**
- `self: Object`
- `animationName: string`

---

### `0839` GET_OBJECT_ANIM_CURRENT_TIME
Gets the current progress of the object's animation

**Class:** `Object.GetAnimCurrentTime`

**Input:**
- `self: Object`
- `animationName: string`

**Output:**
- `time: float (variable)`

---

### `083A` SET_OBJECT_ANIM_CURRENT_TIME
Sets the progress of an animation, with 0

**Class:** `Object.SetAnimCurrentTime`

**Input:**
- `self: Object`
- `animationName: string`
- `time: float`

---

### `0875` SET_OBJECT_ONLY_DAMAGED_BY_PLAYER
Makes the object damageable only by the player

**Class:** `Object.SetOnlyDamagedByPlayer`

**Input:**
- `self: Object`
- `state: bool`

---

### `08D2` SET_OBJECT_SCALE
Sets the scale of the object

**Class:** `Object.SetScale`

**Input:**
- `self: Object`
- `scale: float`

---

### `08E3` IS_OBJECT_IN_ANGLED_AREA_2D
Checks if the object is within the angled 2D area

**Class:** `Object.IsInAngledArea2D`
**Flags:** condition

**Input:**
- `self: Object`
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `angle: float`
- `drawSphere: bool`

---

### `08E4` IS_OBJECT_IN_ANGLED_AREA_3D
Checks if the object is within the angled 3D area

**Class:** `Object.IsInAngledArea3D`
**Flags:** condition

**Input:**
- `self: Object`
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `angle: float`
- `drawSphere: bool`

---

### `08E9` SET_OBJECT_AS_STEALABLE
Sets whether the object can be picked up and carried

**Class:** `Object.SetAsStealable`

**Input:**
- `self: Object`
- `state: bool`

---

### `08FF` HAS_OBJECT_BEEN_DAMAGED_BY_WEAPON
Returns true if the object has been damaged by the specified weapon or damage type

**Class:** `Object.HasBeenDamagedByWeapon`
**Flags:** condition

**Input:**
- `self: Object`
- `weaponType: WeaponType`

---

### `0900` CLEAR_OBJECT_LAST_WEAPON_DAMAGE
Clears the object's last damaging weapon ID

**Class:** `Object.ClearLastWeaponDamage`

**Input:**
- `self: Object`

---

### `0905` LOCK_DOOR
Sets whether the door object is locked at its current rotation and allows it to be pushed open by entities once

**Class:** `Object.LockDoor`

**Input:**
- `self: Object`
- `state: bool`

---

### `0906` SET_OBJECT_MASS
Sets the object's mass

**Class:** `Object.SetMass`

**Input:**
- `self: Object`
- `mass: float`

---

### `0907` GET_OBJECT_MASS
Returns the object's mass

**Class:** `Object.GetMass`

**Input:**
- `self: Object`

**Output:**
- `mass: float (variable)`

---

### `0908` SET_OBJECT_TURN_MASS
Sets the object's turn mass

**Class:** `Object.SetTurnMass`

**Input:**
- `self: Object`
- `turnMass: float`

---

### `0909` GET_OBJECT_TURN_MASS
Returns the object's turn mass

**Class:** `Object.GetTurnMass`

**Input:**
- `self: Object`

**Output:**
- `turnMass: float (variable)`

---

### `0916` WINCH_CAN_PICK_OBJECT_UP
Sets whether the object can be picked up with the magnocrane

**Class:** `Object.WinchCanPickUp`

**Input:**
- `self: Object`
- `state: bool`

---

### `095B` HAS_OBJECT_BEEN_UPROOTED
Returns true if the object has been made moveable by the 0392

**Class:** `Object.HasBeenUprooted`
**Flags:** condition

**Input:**
- `self: Object`

---

### `0977` IS_OBJECT_WITHIN_BRAIN_ACTIVATION_RANGE
Returns true if the object is within the external script trigger radius

**Class:** `Object.IsWithinBrainActivationRange`
**Flags:** condition

**Input:**
- `self: Object`

---

### `0984` GET_OBJECT_MODEL
Returns the object's model index

**Class:** `Object.GetModel`

**Input:**
- `self: Object`

**Output:**
- `model: int (variable)`

---

### `09A2` REMOVE_OBJECT_ELEGANTLY
Fades the object out of existence, freeing game memory

**Class:** `Object.RemoveElegantly`
**Flags:** destructor

**Input:**
- `self: Object`

---

### `09CA` SET_OBJECT_PROOFS
Sets what immunities the object has

**Class:** `Object.SetProofs`

**Input:**
- `self: Object`
- `bulletProof: bool`
- `fireProof: bool`
- `explosionProof: bool`
- `collisionProof: bool`
- `meleeProof: bool`

---

### `09CC` DOES_OBJECT_HAVE_THIS_MODEL
Returns true if the object's model is the model specified

**Class:** `Object.DoesHaveThisModel`
**Flags:** condition

**Input:**
- `self: Object`
- `modelId: model_any`

---

### `09FC` IS_OBJECT_INTERSECTING_WORLD
Appears to return true if something had entered the object's position since it was created or its position was changed

**Class:** `Object.IsIntersectingWorld`
**Flags:** condition

**Input:**
- `self: Object`

---

### `0A0A` ENABLE_DISABLED_ATTRACTORS_ON_OBJECT
Sets whether the object attracts spawned peds to interact with it

**Class:** `Object.EnableDisabledAttractors`

**Input:**
- `self: Object`
- `state: bool`

---
