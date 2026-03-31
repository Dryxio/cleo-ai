# Task Opcodes

> 97 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `04EB` | TASK_TOGGLE_DUCK | Makes the character crouch |
| `05B9` | TASK_PAUSE | Makes the character pause for the specified amount of time |
| `05BA` | TASK_STAND_STILL | Makes the character stand still |
| `05BB` | TASK_FALL_AND_GET_UP | Makes char fall to the ground and stay there for the specified time |
| `05BC` | TASK_JUMP | Makes the char perform a jump |
| `05BD` | TASK_TIRED | Makes the char stop to regain breath |
| `05BE` | TASK_DIE | Kills the character |
| `05BF` | TASK_LOOK_AT_CHAR | Makes the character look at another character |
| `05C0` | TASK_LOOK_AT_VEHICLE | Makes the char look at the specified vehicle |
| `05C1` | TASK_SAY | Makes the character say a phrase from the specified audio table |
| `05C2` | TASK_SHAKE_FIST | Makes the char lift their hand up in the air angrily |
| `05C3` | TASK_COWER | Makes the char stumble backwards with their arms in front of their face as if he |
| `05C4` | TASK_HANDS_UP | Makes the char put their hands in the air |
| `05C5` | TASK_DUCK | Makes a character duck with their arms over head |
| `05C7` | TASK_USE_ATM | Makes a character use an ATM machine |
| `05C8` | TASK_SCRATCH_HEAD | Makes a character scratch their head while looking around |
| `05C9` | TASK_LOOK_ABOUT | Makes a character look out ahead |
| `05CA` | TASK_ENTER_CAR_AS_PASSENGER | Makes a character approach the car and occupy the specified passenger seat |
| `05CB` | TASK_ENTER_CAR_AS_DRIVER | Makes a character approach the car and occupy the driver seat |
| `05CD` | TASK_LEAVE_CAR | Makes the character exit the specified vehicle, if they are currently in it |
| `05CF` | TASK_LEAVE_CAR_AND_FLEE | Makes the character exit the vehicle and flee to the specified position |
| `05D1` | TASK_CAR_DRIVE_TO_COORD |  |
| `05D2` | TASK_CAR_DRIVE_WANDER | Makes the character drive around aimlessly in a vehicle |
| `05D3` | TASK_GO_STRAIGHT_TO_COORD | Makes the character walk to the specified coordinates |
| `05D4` | TASK_ACHIEVE_HEADING | Rotates a character to the specified angle |
| `05D8` | TASK_FOLLOW_POINT_ROUTE | Makes the character follow the path route |
| `05D9` | TASK_GOTO_CHAR | Approaches the character from any direction within the specified radius |
| `05DA` | TASK_FLEE_POINT | Makes the character run away from a point, scared and often screaming |
| `05DB` | TASK_FLEE_CHAR | Makes the character run away from another character |
| `05DC` | TASK_SMART_FLEE_POINT | Makes the character run away from the specified coordinates |
| `05DD` | TASK_SMART_FLEE_CHAR | Makes the character flee from another character |
| `05DE` | TASK_WANDER_STANDARD | Makes the character walk around the ped path |
| `05E2` | TASK_KILL_CHAR_ON_FOOT | Makes a character attack another character on foot |
| `05F5` | TASK_FOLLOW_PATH_NODES_TO_COORD | Makes the character go to the specified coordinates |
| `0603` | TASK_GO_TO_COORD_ANY_MEANS | Assigns the character the task of getting to the specified coordinates |
| `0605` | TASK_PLAY_ANIM | Makes the character perform an animation |
| `0622` | TASK_LEAVE_CAR_IMMEDIATELY | Makes the character jump out of the vehicle while it is in motion |
| `0633` | TASK_LEAVE_ANY_CAR | Makes the char exit the car, if he is in one |
| `0634` | TASK_KILL_CHAR_ON_FOOT_WHILE_DUCKING |  |
| `0635` | TASK_AIM_GUN_AT_CHAR | Makes a character aim at another character |
| `0637` | TASK_GO_TO_COORD_WHILE_SHOOTING | Makes a character go to the location while shooting at another character |
| `0638` | TASK_STAY_IN_SAME_PLACE | Makes the character stay in the same place |
| `0639` | TASK_TURN_CHAR_TO_FACE_CHAR | Makes a character face another character |
| `0655` | TASK_LOOK_AT_OBJECT | Makes the character look at an object |
| `0667` | TASK_AIM_GUN_AT_COORD | Makes the character aim at the specified coordinates |
| `0668` | TASK_SHOOT_AT_COORD | Makes the character turn round and shoot at the specified coordinates |
| `0672` | TASK_DESTROY_CAR | Makes the character attack a vehicle |
| `0673` | TASK_DIVE_AND_GET_UP | Makes the character perform a dive in the specified direction |
| `0676` | TASK_SHUFFLE_TO_NEXT_CAR_SEAT | Makes the character move to the seat on the right |
| `0677` | TASK_CHAT_WITH_CHAR | Makes the character chat with another character |
| `0688` | TASK_TOGGLE_PED_THREAT_SCANNER |  |
| `06A5` | TASK_DIVE_FROM_ATTACHMENT_AND_GET_UP | Makes character detach from host, perform dive then get up |
| `06A8` | TASK_GOTO_CHAR_OFFSET | Approaches the char at the specified offset, specified by the radius and angle |
| `06A9` | TASK_LOOK_AT_COORD | Makes the char look at the specified coordinates |
| `06B0` | TASK_SIT_DOWN | Makes the char sit down for the specified amount of time |
| `06BA` | TASK_TURN_CHAR_TO_FACE_COORD |  |
| `06BB` | TASK_DRIVE_POINT_ROUTE |  |
| `06C2` | TASK_GO_TO_COORD_WHILE_AIMING |  |
| `06C7` | TASK_CAR_TEMP_ACTION | Makes the AI driver perform the action in the vehicle for the specified period o |
| `06E1` | TASK_CAR_MISSION | Sets the car's current mission with various parameters |
| `06E2` | TASK_GO_TO_OBJECT | Makes the character go to an object |
| `06E3` | TASK_WEAPON_ROLL |  |
| `06E4` | TASK_CHAR_ARREST_CHAR | Makes the character attempt to arrest another character |
| `070A` | TASK_PICK_UP_OBJECT | Attaches the specified char to an object with the optional addition of having it |
| `0713` | TASK_DRIVE_BY |  |
| `0729` | TASK_USE_MOBILE_PHONE | Makes a character pull out a cellphone, answer it, and hold it to their ear |
| `072A` | TASK_WARP_CHAR_INTO_CAR_AS_DRIVER | Warps the character into the specified vehicle's driver seat |
| `072B` | TASK_WARP_CHAR_INTO_CAR_AS_PASSENGER |  |
| `074C` | TASK_USE_ATTRACTOR |  |
| `074D` | TASK_SHOOT_AT_CHAR |  |
| `0751` | TASK_FLEE_CHAR_ANY_MEANS |  |
| `0762` | TASK_DEAD | Kills the character |
| `0772` | TASK_GOTO_CAR |  |
| `078F` | TASK_CLIMB | Makes the character jump and climb on an object |
| `07A3` | TASK_GOTO_CHAR_AIMING |  |
| `07A5` | TASK_KILL_CHAR_ON_FOOT_TIMED | Makes the character attack the specified character |
| `07A7` | TASK_JETPACK |  |
| `07BC` | TASK_SET_CHAR_DECISION_MAKER | Sets the decision maker used by the specified char |
| `07C9` | TASK_COMPLEX_PICKUP_OBJECT | Makes character walk to the object and pick it up |
| `07CD` | TASK_CHAR_SLIDE_TO_COORD |  |
| `07E1` | TASK_SWIM_TO_COORD |  |
| `07E7` | TASK_DRIVE_POINT_ROUTE_ADVANCED |  |
| `0804` | TASK_CHAR_SLIDE_TO_COORD_AND_PLAY_ANIM | Makes a character walk to the specified point, trun to heading, then play an ani |
| `0812` | TASK_PLAY_ANIM_NON_INTERRUPTABLE | Makes the character perform an animation like TASK_PLAY_ANIM, except it will not |
| `0817` | TASK_FOLLOW_PATROL_ROUTE | Assigns the character to the patrol path |
| `0823` | TASK_GREET_PARTNER | Makes a character greet another character with a handshake |
| `0829` | TASK_DIE_NAMED_ANIM | Makes the char perform an animation similarly to 0605 |
| `0850` | TASK_FOLLOW_FOOTSTEPS | Makes one char follow another |
| `0859` | TASK_WALK_ALONGSIDE_CHAR | Makes the character walk alongside the specified character |
| `085B` | TASK_KINDA_STAY_IN_SAME_PLACE | Makes the character stay near their current position |
| `088A` | TASK_PLAY_ANIM_WITH_FLAGS | Makes the char perform an animation |
| `08A0` | TASK_USE_CLOSEST_MAP_ATTRACTOR |  |
| `099F` | TASK_SET_IGNORE_WEAPON_RANGE_FLAG |  |
| `09A0` | TASK_PICK_UP_SECOND_OBJECT |  |
| `0A1A` | TASK_PLAY_ANIM_SECONDARY | Makes a character play an animation that affects only the upper half of their bo |
| `0A1D` | TASK_HAND_GESTURE | Makes a character face the other character and make a gesture |
| `0A2E` | TASK_FOLLOW_PATH_NODES_TO_COORD_WITH_RADIUS | Makes the specified character run in panic to the specified position |

## Detailed Reference

### `04EB` TASK_TOGGLE_DUCK
Makes the character crouch

**Class:** `Task.ToggleDuck`
**Flags:** static

**Input:**
- `handle: Char`
- `state: bool`

---

### `05B9` TASK_PAUSE
Makes the character pause for the specified amount of time

**Class:** `Task.Pause`
**Flags:** static

**Input:**
- `handle: Char`
- `time: int`

---

### `05BA` TASK_STAND_STILL
Makes the character stand still

**Class:** `Task.StandStill`
**Flags:** static

**Input:**
- `handle: Char`
- `time: int`

---

### `05BB` TASK_FALL_AND_GET_UP
Makes char fall to the ground and stay there for the specified time

**Class:** `Task.FallAndGetUp`
**Flags:** static

**Input:**
- `handle: Char`
- `fallDown: bool`
- `timeOnGround: int`

---

### `05BC` TASK_JUMP
Makes the char perform a jump

**Class:** `Task.Jump`
**Flags:** static

**Input:**
- `handle: Char`
- `state: bool`

---

### `05BD` TASK_TIRED
Makes the char stop to regain breath

**Class:** `Task.Tired`
**Flags:** static

**Input:**
- `handle: Char`
- `time: int`

---

### `05BE` TASK_DIE
Kills the character

**Class:** `Task.Die`
**Flags:** static

**Input:**
- `handle: Char`

---

### `05BF` TASK_LOOK_AT_CHAR
Makes the character look at another character

**Class:** `Task.LookAtChar`
**Flags:** static

**Input:**
- `observer: Char`
- `target: Char`
- `time: int`

---

### `05C0` TASK_LOOK_AT_VEHICLE
Makes the char look at the specified vehicle

**Class:** `Task.LookAtVehicle`
**Flags:** static

**Input:**
- `char: Char`
- `vehicle: Car`
- `time: int`

---

### `05C1` TASK_SAY
Makes the character say a phrase from the specified audio table

**Class:** `Task.Say`
**Flags:** static

**Input:**
- `handle: Char`
- `phrase: SpeechId`

---

### `05C2` TASK_SHAKE_FIST
Makes the char lift their hand up in the air angrily

**Class:** `Task.ShakeFist`
**Flags:** static

**Input:**
- `handle: Char`

---

### `05C3` TASK_COWER
Makes the char stumble backwards with their arms in front of their face as if he is backing away from something in fear

**Class:** `Task.Cower`
**Flags:** static

**Input:**
- `handle: Char`

---

### `05C4` TASK_HANDS_UP
Makes the char put their hands in the air

**Class:** `Task.HandsUp`
**Flags:** static

**Input:**
- `handle: Char`
- `time: int`

---

### `05C5` TASK_DUCK
Makes a character duck with their arms over head

**Class:** `Task.Duck`
**Flags:** static

**Input:**
- `handle: Char`
- `time: int`

---

### `05C7` TASK_USE_ATM
Makes a character use an ATM machine

**Class:** `Task.UseAtm`
**Flags:** static

**Input:**
- `handle: Char`

---

### `05C8` TASK_SCRATCH_HEAD
Makes a character scratch their head while looking around

**Class:** `Task.ScratchHead`
**Flags:** static

**Input:**
- `handle: Char`

---

### `05C9` TASK_LOOK_ABOUT
Makes a character look out ahead

**Class:** `Task.LookAbout`
**Flags:** static

**Input:**
- `handle: Char`
- `time: int`

---

### `05CA` TASK_ENTER_CAR_AS_PASSENGER
Makes a character approach the car and occupy the specified passenger seat

**Class:** `Task.EnterCarAsPassenger`
**Flags:** static

**Input:**
- `char: Char`
- `vehicle: Car`
- `time: int`
- `seat: SeatId`

---

### `05CB` TASK_ENTER_CAR_AS_DRIVER
Makes a character approach the car and occupy the driver seat

**Class:** `Task.EnterCarAsDriver`
**Flags:** static

**Input:**
- `char: Char`
- `vehicle: Car`
- `time: int`

---

### `05CD` TASK_LEAVE_CAR
Makes the character exit the specified vehicle, if they are currently in it

**Class:** `Task.LeaveCar`
**Flags:** static

**Input:**
- `char: Char`
- `vehicle: Car`

---

### `05CF` TASK_LEAVE_CAR_AND_FLEE
Makes the character exit the vehicle and flee to the specified position

**Class:** `Task.LeaveCarAndFlee`
**Flags:** static

**Input:**
- `char: Char`
- `vehicle: Car`
- `x: float`
- `y: float`
- `z: float`

---

### `05D1` TASK_CAR_DRIVE_TO_COORD

**Class:** `Task.CarDriveToCoord`
**Flags:** static

**Input:**
- `driver: Char`
- `vehicle: Car`
- `x: float`
- `y: float`
- `z: float`
- `speed: float`
- `driveStyle: DriveMode`
- `modelId: model_vehicle`
- `drivingStyle: DrivingMode`

---

### `05D2` TASK_CAR_DRIVE_WANDER
Makes the character drive around aimlessly in a vehicle

**Class:** `Task.CarDriveWander`
**Flags:** static

**Input:**
- `char: Char`
- `vehicle: Car`
- `speed: float`
- `drivingMode: DrivingMode`

---

### `05D3` TASK_GO_STRAIGHT_TO_COORD
Makes the character walk to the specified coordinates

**Class:** `Task.GoStraightToCoord`
**Flags:** static

**Input:**
- `handle: Char`
- `x: float`
- `y: float`
- `z: float`
- `speed: MoveState`
- `time: int`

---

### `05D4` TASK_ACHIEVE_HEADING
Rotates a character to the specified angle

**Class:** `Task.AchieveHeading`
**Flags:** static

**Input:**
- `handle: Char`
- `heading: float`

---

### `05D8` TASK_FOLLOW_POINT_ROUTE
Makes the character follow the path route

**Class:** `Task.FollowPointRoute`
**Flags:** static

**Input:**
- `handle: Char`
- `speed: MoveState`
- `mode: RouteMode`

---

### `05D9` TASK_GOTO_CHAR
Approaches the character from any direction within the specified radius

**Class:** `Task.GotoChar`
**Flags:** static

**Input:**
- `walking: Char`
- `target: Char`
- `time: int`
- `radius: float`

---

### `05DA` TASK_FLEE_POINT
Makes the character run away from a point, scared and often screaming

**Class:** `Task.FleePoint`
**Flags:** static

**Input:**
- `handle: Char`
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `time: int`

---

### `05DB` TASK_FLEE_CHAR
Makes the character run away from another character

**Class:** `Task.FleeChar`
**Flags:** static

**Input:**
- `handle: Char`
- `threat: Char`
- `radius: float`
- `time: int`

---

### `05DC` TASK_SMART_FLEE_POINT
Makes the character run away from the specified coordinates

**Class:** `Task.SmartFleePoint`
**Flags:** static

**Input:**
- `handle: Char`
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `time: int`

---

### `05DD` TASK_SMART_FLEE_CHAR
Makes the character flee from another character

**Class:** `Task.SmartFleeChar`
**Flags:** static

**Input:**
- `handle: Char`
- `threat: Char`
- `radius: float`
- `time: int`

---

### `05DE` TASK_WANDER_STANDARD
Makes the character walk around the ped path

**Class:** `Task.WanderStandard`
**Flags:** static

**Input:**
- `handle: Char`

---

### `05E2` TASK_KILL_CHAR_ON_FOOT
Makes a character attack another character on foot

**Class:** `Task.KillCharOnFoot`
**Flags:** static

**Input:**
- `killer: Char`
- `target: Char`

---

### `05F5` TASK_FOLLOW_PATH_NODES_TO_COORD
Makes the character go to the specified coordinates

**Class:** `Task.FollowPathNodesToCoord`
**Flags:** static

**Input:**
- `handle: Char`
- `x: float`
- `y: float`
- `z: float`
- `speed: MoveState`
- `time: int`

---

### `0603` TASK_GO_TO_COORD_ANY_MEANS
Assigns the character the task of getting to the specified coordinates

**Class:** `Task.GoToCoordAnyMeans`
**Flags:** static

**Input:**
- `char: Char`
- `x: float`
- `y: float`
- `z: float`
- `speed: MoveState`
- `vehicle: Car`

---

### `0605` TASK_PLAY_ANIM
Makes the character perform an animation

**Class:** `Task.PlayAnim`
**Flags:** static

**Input:**
- `handle: Char`
- `animationName: string`
- `animationFile: string`
- `blendSpeed: float`
- `loop: bool`
- `lockX: bool`
- `lockY: bool`
- `keepLastFrame: bool`
- `time: int`

---

### `0622` TASK_LEAVE_CAR_IMMEDIATELY
Makes the character jump out of the vehicle while it is in motion

**Class:** `Task.LeaveCarImmediately`
**Flags:** static

**Input:**
- `char: Char`
- `vehicle: Car`

---

### `0633` TASK_LEAVE_ANY_CAR
Makes the char exit the car, if he is in one

**Class:** `Task.LeaveAnyCar`
**Flags:** static

**Input:**
- `handle: Char`

---

### `0634` TASK_KILL_CHAR_ON_FOOT_WHILE_DUCKING

**Class:** `Task.KillCharOnFootWhileDucking`
**Flags:** static

**Input:**
- `char: Char`
- `target: Char`
- `flags: int`
- `actionDelay: int`
- `actionChance: int`

---

### `0635` TASK_AIM_GUN_AT_CHAR
Makes a character aim at another character

**Class:** `Task.AimGunAtChar`
**Flags:** static

**Input:**
- `char: Char`
- `target: Char`
- `time: int`

---

### `0637` TASK_GO_TO_COORD_WHILE_SHOOTING
Makes a character go to the location while shooting at another character

**Class:** `Task.GoToCoordWhileShooting`
**Flags:** static

**Input:**
- `char: Char`
- `x: float`
- `y: float`
- `z: float`
- `speed: MoveState`
- `turnRadius: float`
- `stopRadius: float`
- `target: Char`

---

### `0638` TASK_STAY_IN_SAME_PLACE
Makes the character stay in the same place

**Class:** `Task.StayInSamePlace`
**Flags:** static

**Input:**
- `handle: Char`
- `state: bool`

---

### `0639` TASK_TURN_CHAR_TO_FACE_CHAR
Makes a character face another character

**Class:** `Task.TurnCharToFaceChar`
**Flags:** static

**Input:**
- `char: Char`
- `target: Char`

---

### `0655` TASK_LOOK_AT_OBJECT
Makes the character look at an object

**Class:** `Task.LookAtObject`
**Flags:** static

**Input:**
- `char: Char`
- `object: Object`
- `time: any`

---

### `0667` TASK_AIM_GUN_AT_COORD
Makes the character aim at the specified coordinates

**Class:** `Task.AimGunAtCoord`
**Flags:** static

**Input:**
- `handle: Char`
- `x: float`
- `y: float`
- `z: float`
- `time: int`

---

### `0668` TASK_SHOOT_AT_COORD
Makes the character turn round and shoot at the specified coordinates

**Class:** `Task.ShootAtCoord`
**Flags:** static

**Input:**
- `handle: Char`
- `x: float`
- `y: float`
- `z: float`
- `time: int`

---

### `0672` TASK_DESTROY_CAR
Makes the character attack a vehicle

**Class:** `Task.DestroyCar`
**Flags:** static

**Input:**
- `char: Char`
- `vehicle: Car`

---

### `0673` TASK_DIVE_AND_GET_UP
Makes the character perform a dive in the specified direction

**Class:** `Task.DiveAndGetUp`
**Flags:** static

**Input:**
- `handle: Char`
- `directionX: float`
- `directionY: float`
- `timeOnGround: int`

---

### `0676` TASK_SHUFFLE_TO_NEXT_CAR_SEAT
Makes the character move to the seat on the right

**Class:** `Task.ShuffleToNextCarSeat`
**Flags:** static

**Input:**
- `char: Char`
- `vehicle: Car`

---

### `0677` TASK_CHAT_WITH_CHAR
Makes the character chat with another character

**Class:** `Task.ChatWithChar`
**Flags:** static

**Input:**
- `char: Char`
- `other: Char`
- `leadSpeaker: bool`
- `_p4: int`

---

### `0688` TASK_TOGGLE_PED_THREAT_SCANNER

**Class:** `Task.TogglePedThreatScanner`
**Flags:** static

**Input:**
- `handle: Char`
- `onFoot: bool`
- `inCar: bool`
- `duringScriptTask: bool`

---

### `06A5` TASK_DIVE_FROM_ATTACHMENT_AND_GET_UP
Makes character detach from host, perform dive then get up

**Class:** `Task.DiveFromAttachmentAndGetUp`
**Flags:** static

**Input:**
- `handle: Char`
- `timeOnGround: int`

---

### `06A8` TASK_GOTO_CHAR_OFFSET
Approaches the char at the specified offset, specified by the radius and angle

**Class:** `Task.GotoCharOffset`
**Flags:** static

**Input:**
- `char: Char`
- `target: Char`
- `time: int`
- `radius: float`
- `heading: float`

---

### `06A9` TASK_LOOK_AT_COORD
Makes the char look at the specified coordinates

**Class:** `Task.LookAtCoord`
**Flags:** static

**Input:**
- `handle: Char`
- `x: float`
- `y: float`
- `z: float`
- `time: int`

---

### `06B0` TASK_SIT_DOWN
Makes the char sit down for the specified amount of time

**Class:** `Task.SitDown`
**Flags:** static

**Input:**
- `handle: Char`
- `time: int`

---

### `06BA` TASK_TURN_CHAR_TO_FACE_COORD

**Class:** `Task.TurnCharToFaceCoord`
**Flags:** static

**Input:**
- `handle: Char`
- `x: float`
- `y: float`
- `z: float`

---

### `06BB` TASK_DRIVE_POINT_ROUTE

**Class:** `Task.DrivePointRoute`
**Flags:** static

**Input:**
- `char: Char`
- `vehicle: Car`
- `speed: int`

---

### `06C2` TASK_GO_TO_COORD_WHILE_AIMING

**Class:** `Task.GoToCoordWhileAiming`
**Flags:** static

**Input:**
- `char: Char`
- `x: float`
- `y: float`
- `z: float`
- `speed: MoveState`
- `turnRadius: float`
- `stopRadius: float`
- `target: Char`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`

---

### `06C7` TASK_CAR_TEMP_ACTION
Makes the AI driver perform the action in the vehicle for the specified period of time

**Class:** `Task.CarTempAction`
**Flags:** static

**Input:**
- `char: Char`
- `vehicle: Car`
- `actionId: TempAction`
- `time: int`

---

### `06E1` TASK_CAR_MISSION
Sets the car's current mission with various parameters

**Class:** `Task.CarMission`
**Flags:** static

**Input:**
- `char: Char`
- `vehicle: Car`
- `targetVehicle: Car`
- `missionId: CarMission`
- `cruiseSpeed: float`
- `drivingStyle: DrivingMode`

---

### `06E2` TASK_GO_TO_OBJECT
Makes the character go to an object

**Class:** `Task.GoToObject`
**Flags:** static

**Input:**
- `char: Char`
- `object: Object`
- `time: int`
- `radius: float`

---

### `06E3` TASK_WEAPON_ROLL

**Class:** `Task.WeaponRoll`
**Flags:** static

**Input:**
- `handle: Char`
- `direction: bool`

---

### `06E4` TASK_CHAR_ARREST_CHAR
Makes the character attempt to arrest another character

**Class:** `Task.CharArrestChar`
**Flags:** static

**Input:**
- `char: Char`
- `target: Char`

---

### `070A` TASK_PICK_UP_OBJECT
Attaches the specified char to an object with the optional addition of having it perform an animation

**Class:** `Task.PickUpObject`
**Flags:** static

**Input:**
- `char: Char`
- `object: Object`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `bone: PedBoneId`
- `orientation: HoldOrientation`
- `animationName: string`
- `animationFile: string`
- `time: int`

---

### `0713` TASK_DRIVE_BY

**Class:** `Task.DriveBy`
**Flags:** static

**Input:**
- `handle: Char`
- `targetChar: Char`
- `targetVehicle: Car`
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `type: DriveByType`
- `rightHandCarSeat: bool`
- `fireRate: int`

---

### `0729` TASK_USE_MOBILE_PHONE
Makes a character pull out a cellphone, answer it, and hold it to their ear

**Class:** `Task.UseMobilePhone`
**Flags:** static

**Input:**
- `handle: Char`
- `start: bool`

---

### `072A` TASK_WARP_CHAR_INTO_CAR_AS_DRIVER
Warps the character into the specified vehicle's driver seat

**Class:** `Task.WarpCharIntoCarAsDriver`
**Flags:** static

**Input:**
- `char: Char`
- `vehicle: Car`

---

### `072B` TASK_WARP_CHAR_INTO_CAR_AS_PASSENGER

**Class:** `Task.WarpCharIntoCarAsPassenger`
**Flags:** static

**Input:**
- `char: Char`
- `vehicle: Car`
- `seatId: SeatId`

---

### `074C` TASK_USE_ATTRACTOR

**Class:** `Task.UseAttractor`
**Flags:** static

**Input:**
- `char: Char`
- `attractor: Attractor`

---

### `074D` TASK_SHOOT_AT_CHAR

**Class:** `Task.ShootAtChar`
**Flags:** static

**Input:**
- `handle: Char`
- `target: Char`
- `time: int`

---

### `0751` TASK_FLEE_CHAR_ANY_MEANS

**Class:** `Task.FleeCharAnyMeans`
**Flags:** static

**Input:**
- `handle: Char`
- `threat: Char`
- `safeDist: float`
- `time: int`
- `shoot: bool`
- `shootTime: int`
- `shootCooldownTime: int`
- `stealCarDist: float`

---

### `0762` TASK_DEAD
Kills the character

**Class:** `Task.Dead`
**Flags:** static

**Input:**
- `handle: Char`

---

### `0772` TASK_GOTO_CAR

**Class:** `Task.GotoCar`
**Flags:** static

**Input:**
- `char: Char`
- `vehicle: Car`
- `time: int`
- `radius: float`

---

### `078F` TASK_CLIMB
Makes the character jump and climb on an object

**Class:** `Task.Climb`
**Flags:** static

**Input:**
- `handle: Char`
- `flag: bool`

---

### `07A3` TASK_GOTO_CHAR_AIMING

**Class:** `Task.GotoCharAiming`
**Flags:** static

**Input:**
- `handle: Char`
- `target: Char`
- `radiusFrom: float`
- `radiusTo: float`

---

### `07A5` TASK_KILL_CHAR_ON_FOOT_TIMED
Makes the character attack the specified character

**Class:** `Task.KillCharOnFootTimed`
**Flags:** static

**Input:**
- `handle: Char`
- `target: Char`
- `time: int`

---

### `07A7` TASK_JETPACK

**Class:** `Task.Jetpack`
**Flags:** static

**Input:**
- `handle: Char`

---

### `07BC` TASK_SET_CHAR_DECISION_MAKER
Sets the decision maker used by the specified char

**Class:** `Task.SetCharDecisionMaker`
**Flags:** static

**Input:**
- `char: Char`
- `handleOrTemplate: DecisionMakerCharTemplate`

---

### `07C9` TASK_COMPLEX_PICKUP_OBJECT
Makes character walk to the object and pick it up

**Class:** `Task.ComplexPickupObject`
**Flags:** static

**Input:**
- `char: Char`
- `object: Object`

---

### `07CD` TASK_CHAR_SLIDE_TO_COORD

**Class:** `Task.CharSlideToCoord`
**Flags:** static

**Input:**
- `handle: Char`
- `x: float`
- `y: float`
- `z: float`
- `angle: float`
- `slideSpeed: float`

---

### `07E1` TASK_SWIM_TO_COORD

**Class:** `Task.SwimToCoord`
**Flags:** static

**Input:**
- `handle: Char`
- `x: float`
- `y: float`
- `z: float`

---

### `07E7` TASK_DRIVE_POINT_ROUTE_ADVANCED

**Class:** `Task.DrivePointRouteAdvanced`
**Flags:** static

**Input:**
- `char: Char`
- `vehicle: Car`
- `speed: float`
- `driveStyle: DriveMode`
- `modelId: model_vehicle`
- `drivingStyle: DrivingMode`

---

### `0804` TASK_CHAR_SLIDE_TO_COORD_AND_PLAY_ANIM
Makes a character walk to the specified point, trun to heading, then play an animation

**Class:** `Task.CharSlideToCoordAndPlayAnim`
**Flags:** static

**Input:**
- `handle: Char`
- `x: float`
- `y: float`
- `z: float`
- `heading: float`
- `slideSpeed: float`
- `animationName: string`
- `animationFile: string`
- `blendSpeed: float`
- `loop: bool`
- `lockX: bool`
- `lockY: bool`
- `keepLastFrame: bool`
- `time: int`

---

### `0812` TASK_PLAY_ANIM_NON_INTERRUPTABLE
Makes the character perform an animation like TASK_PLAY_ANIM, except it will not be disturbed by any events

**Class:** `Task.PlayAnimNonInterruptable`
**Flags:** static

**Input:**
- `handle: Char`
- `animationName: string`
- `animationFile: string`
- `blendSpeed: float`
- `loop: bool`
- `lockX: bool`
- `lockY: bool`
- `keepLastFrame: bool`
- `time: int`

---

### `0817` TASK_FOLLOW_PATROL_ROUTE
Assigns the character to the patrol path

**Class:** `Task.FollowPatrolRoute`
**Flags:** static

**Input:**
- `handle: Char`
- `speed: MoveState`
- `mode: RouteMode`

---

### `0823` TASK_GREET_PARTNER
Makes a character greet another character with a handshake

**Class:** `Task.GreetPartner`
**Flags:** static

**Input:**
- `handle: Char`
- `partner: Char`
- `approachRatio: float`
- `greetStyle: int`

---

### `0829` TASK_DIE_NAMED_ANIM
Makes the char perform an animation similarly to 0605

**Class:** `Task.DieNamedAnim`
**Flags:** static

**Input:**
- `handle: Char`
- `animationName: string`
- `animationFile: string`
- `blendSpeed: float`
- `time: int`

---

### `0850` TASK_FOLLOW_FOOTSTEPS
Makes one char follow another

**Class:** `Task.FollowFootsteps`
**Flags:** static

**Input:**
- `handle: Char`
- `target: Char`

---

### `0859` TASK_WALK_ALONGSIDE_CHAR
Makes the character walk alongside the specified character

**Class:** `Task.WalkAlongsideChar`
**Flags:** static

**Input:**
- `handle: Char`
- `target: Char`

---

### `085B` TASK_KINDA_STAY_IN_SAME_PLACE
Makes the character stay near their current position

**Class:** `Task.KindaStayInSamePlace`
**Flags:** static

**Input:**
- `handle: Char`
- `state: bool`

---

### `088A` TASK_PLAY_ANIM_WITH_FLAGS
Makes the char perform an animation

**Class:** `Task.PlayAnimWithFlags`
**Flags:** static

**Input:**
- `handle: Char`
- `animationName: string`
- `animationFile: string`
- `frameDelta: float`
- `loop: bool`
- `lockX: bool`
- `lockY: bool`
- `lockF: bool`
- `time: int`
- `disableForce: bool`
- `disableLockZ: bool`

---

### `08A0` TASK_USE_CLOSEST_MAP_ATTRACTOR

**Class:** `Task.UseClosestMapAttractor`
**Flags:** static

**Input:**
- `handle: Char`
- `radius: float`
- `modelId: model_object`
- `fromX: float`
- `fromY: float`
- `fromZ: float`
- `name: string`

---

### `099F` TASK_SET_IGNORE_WEAPON_RANGE_FLAG

**Class:** `Task.SetIgnoreWeaponRangeFlag`
**Flags:** static

**Input:**
- `handle: Char`
- `state: bool`

---

### `09A0` TASK_PICK_UP_SECOND_OBJECT

**Class:** `Task.PickUpSecondObject`
**Flags:** static

**Input:**
- `char: Char`
- `object: Object`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `boneId: PedBoneId`
- `orientation: HoldOrientation`
- `animationName: string`
- `animationFile: string`
- `time: int`

---

### `0A1A` TASK_PLAY_ANIM_SECONDARY
Makes a character play an animation that affects only the upper half of their body

**Class:** `Task.PlayAnimSecondary`
**Flags:** static

**Input:**
- `handle: Char`
- `animationName: string`
- `animationFile: string`
- `blendSpeed: float`
- `loop: bool`
- `lockX: bool`
- `lockY: bool`
- `keepLastFrame: bool`
- `time: int`

---

### `0A1D` TASK_HAND_GESTURE
Makes a character face the other character and make a gesture

**Class:** `Task.HandGesture`
**Flags:** static

**Input:**
- `handle: Char`
- `target: Char`

---

### `0A2E` TASK_FOLLOW_PATH_NODES_TO_COORD_WITH_RADIUS
Makes the specified character run in panic to the specified position

**Class:** `Task.FollowPathNodesToCoordWithRadius`
**Flags:** static

**Input:**
- `handle: Char`
- `x: float`
- `y: float`
- `z: float`
- `speed: MoveState`
- `time: int`
- `radius: float`

---
