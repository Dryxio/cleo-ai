# Player Opcodes

> 66 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0053` | CREATE_PLAYER | Creates a player at the specified location |
| `0109` | ADD_SCORE | Adds to the player's money |
| `010A` | IS_SCORE_GREATER | Returns true if the player's money is over the specified value |
| `010B` | STORE_SCORE | Returns the player's money |
| `010D` | ALTER_WANTED_LEVEL | Sets the player's wanted level |
| `010E` | ALTER_WANTED_LEVEL_NO_DROP | Sets the player's wanted level if the specified level is higher than the current |
| `010F` | IS_WANTED_LEVEL_GREATER | Returns true if the player's wanted level is over the specified value |
| `0110` | CLEAR_WANTED_LEVEL | Clears the player's wanted level |
| `0117` | IS_PLAYER_DEAD | Returns true when player is dead (wasted) |
| `0122` | IS_PLAYER_PRESSING_HORN | Returns true if the player is honking the horn in a car |
| `01B4` | SET_PLAYER_CONTROL | Sets whether player's control is enabled |
| `01C0` | STORE_WANTED_LEVEL | Returns the player's current wanted level |
| `01F5` | GET_PLAYER_CHAR | Gets the character handle for the specified player |
| `0221` | APPLY_BRAKES_TO_PLAYERS_CAR | Applies brakes to the player's car |
| `0241` | IS_PLAYER_IN_REMOTE_MODE | Returns true if the player is controlling a remote-control vehicle |
| `0256` | IS_PLAYER_PLAYING | Returns true if the player hasn't been wasted or busted (the player is still pla |
| `0297` | RESET_NUM_OF_MODELS_KILLED_BY_PLAYER | Resets the count of how many times the player has destroyed a certain model |
| `0298` | GET_NUM_OF_MODELS_KILLED_BY_PLAYER | Returns the number of times the player has destroyed a specific model |
| `0330` | SET_PLAYER_NEVER_GETS_TIRED | Defines whether the player can run fast forever |
| `0331` | SET_PLAYER_FAST_RELOAD | Defines whether the player can reload their gun 4x times faster |
| `03EE` | CAN_PLAYER_START_MISSION | Returns true if the player can move |
| `03EF` | MAKE_PLAYER_SAFE_FOR_CUTSCENE | Makes the player safe, putting the character in a safe location |
| `0414` | SET_FREE_HEALTH_CARE | Sets whether the player loses the cash when gets wasted (works once) |
| `0457` | IS_PLAYER_TARGETTING_CHAR | Returns true if the player is aiming at the specified character |
| `0458` | IS_PLAYER_TARGETTING_OBJECT | Returns true if the player is aiming at the specified object |
| `04E3` | SET_PLAYER_MOOD | Sets the players mood, affecting the dialogue spoken by the player |
| `04FC` | GET_WHEELIE_STATS | Returns the stats of the most recent wheelie or stoppie attempt |
| `0500` | IS_PLAYER_WEARING | Returns true if the player's bodypart has the specified model (0784 or 087B)  |
| `0501` | SET_PLAYER_CAN_DO_DRIVE_BY | Sets the players driveby mode |
| `052C` | SET_PLAYER_DRUNKENNESS | Makes the camera start moving around in a swirling motion with the specified int |
| `055D` | MAKE_PLAYER_FIRE_PROOF | Makes the player immune to fire |
| `055E` | INCREASE_PLAYER_MAX_HEALTH | Increases the player's max health by the specified value and changes current hea |
| `055F` | INCREASE_PLAYER_MAX_ARMOUR | Increases the player's max armor by the specified value and changes current armo |
| `0563` | ENSURE_PLAYER_HAS_DRIVE_BY_WEAPON | Sets the amount of ammo a player has during a driveby |
| `0583` | IS_PLAYER_IN_INFO_ZONE | Returns true if the player is in the specified zone |
| `068C` | IS_PLAYER_TARGETTING_ANYTHING | Returns true if the specified player is auto-aiming at a ped or object |
| `06AF` | DISABLE_PLAYER_SPRINT |  |
| `06DF` | DELETE_PLAYER | Removes the specified player |
| `070D` | BUILD_PLAYER_MODEL | Rebuilds the player model, applying any required texture changes |
| `0784` | GIVE_PLAYER_CLOTHES |  |
| `0793` | STORE_CLOTHES_STATE | Stores the players current clothes to later be restored with 0794 |
| `0794` | RESTORE_CLOTHES_STATE | Restores the players clothes stored with 0793 |
| `07AF` | GET_PLAYER_GROUP |  |
| `07B4` | SET_PLAYER_GROUP_RECRUITMENT | Sets the player's ability to recruit new members to the group |
| `07F1` | IS_PLAYER_PERFORMING_WHEELIE |  |
| `07F2` | IS_PLAYER_PERFORMING_STOPPIE | Returns true if the player is performing a stoppie |
| `0806` | GET_TOTAL_NUMBER_OF_PEDS_KILLED_BY_PLAYER | Returns the number of peds killed by the player since the last reset (0297) |
| `0842` | GET_CITY_PLAYER_IS_IN | Gets the player's current city |
| `0858` | SET_HEADING_FOR_ATTACHED_PLAYER | Sets the view angle for the player attached to an object or vehicle |
| `0861` | IS_ATTACHED_PLAYER_HEADING_ACHIEVED | Returns true if the heading has finished being applied, as started by 0858 |
| `087B` | GIVE_PLAYER_CLOTHES_OUTSIDE_SHOP | Sets the players clothing |
| `08F5` | MAKE_PLAYER_GANG_DISAPPEAR |  |
| `08F6` | MAKE_PLAYER_GANG_REAPPEAR |  |
| `08F7` | GET_CLOTHES_ITEM |  |
| `0945` | GET_PLAYER_MAX_ARMOUR |  |
| `09C7` | SET_PLAYER_MODEL | Changes the player to use the specified model |
| `09D7` | FORCE_INTERIOR_LIGHTING_FOR_PLAYER |  |
| `09D9` | USE_DETONATOR | Detonates all satchel charges and car bombs planted by the player |
| `09E7` | IS_PLAYER_CONTROL_ON | Returns true if the player control hasn't been disabled using 01B4 |
| `09EB` | PLAYER_TAKE_OFF_GOGGLES | Removes the players Goggles and disables night/heat vision |
| `0A0C` | IS_PLAYER_USING_JETPACK | Returns true if player is using a jetpack |
| `0A20` | SET_PLAYER_GROUP_TO_FOLLOW_ALWAYS | Controls the players ability to tell their group to wait and automatically order |
| `0A29` | IS_PLAYER_CLIMBING | Returns true if the player is climbing |
| `0A31` | SET_PLAYER_GROUP_TO_FOLLOW_NEVER | Sets whether the player's group stops following the player, even if the player u |
| `0A3A` | IS_LAST_BUILDING_MODEL_SHOT_BY_PLAYER | Returns true if the player's last shot model is the model specified |
| `0A3B` | CLEAR_LAST_BUILDING_MODEL_SHOT_BY_PLAYER | Resets the status of the last model the player has shot |

## Detailed Reference

### `0053` CREATE_PLAYER
Creates a player at the specified location

**Class:** `Player.Create`
**Flags:** constructor

**Input:**
- `playerIndex: int`
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `handle: Player (variable)`

---

### `0109` ADD_SCORE
Adds to the player's money

**Class:** `Player.AddScore`

**Input:**
- `self: Player`
- `money: int`

**Details:**

This command adds the integer value to the player's current amount of money. A negative value subtracts the player's money. 

SA's upper limit for the money balance is $999,999,999. Negative money balance is possible with the same limit.

---

### `010A` IS_SCORE_GREATER
Returns true if the player's money is over the specified value

**Class:** `Player.IsScoreGreater`
**Flags:** condition

**Input:**
- `self: Player`
- `money: int`

---

### `010B` STORE_SCORE
Returns the player's money

**Class:** `Player.StoreScore`

**Input:**
- `self: Player`

**Output:**
- `money: int (variable)`

---

### `010D` ALTER_WANTED_LEVEL
Sets the player's wanted level

**Class:** `Player.AlterWantedLevel`

**Input:**
- `self: Player`
- `wantedLevel: int`

---

### `010E` ALTER_WANTED_LEVEL_NO_DROP
Sets the player's wanted level if the specified level is higher than the current one

**Class:** `Player.AlterWantedLevelNoDrop`

**Input:**
- `self: Player`
- `wantedLevel: int`

---

### `010F` IS_WANTED_LEVEL_GREATER
Returns true if the player's wanted level is over the specified value

**Class:** `Player.IsWantedLevelGreater`
**Flags:** condition

**Input:**
- `self: Player`
- `wantedLevel: int`

---

### `0110` CLEAR_WANTED_LEVEL
Clears the player's wanted level

**Class:** `Player.ClearWantedLevel`

**Input:**
- `self: Player`

---

### `0117` IS_PLAYER_DEAD
Returns true when player is dead (wasted)

**Class:** `Player.IsDead`
**Flags:** condition

**Input:**
- `self: Player`

---

### `0122` IS_PLAYER_PRESSING_HORN
Returns true if the player is honking the horn in a car

**Class:** `Player.IsPressingHorn`
**Flags:** condition

**Input:**
- `self: Player`

---

### `01B4` SET_PLAYER_CONTROL
Sets whether player's control is enabled

**Class:** `Player.SetControl`

**Input:**
- `self: Player`
- `state: bool`

---

### `01C0` STORE_WANTED_LEVEL
Returns the player's current wanted level

**Class:** `Player.StoreWantedLevel`

**Input:**
- `self: Player`

**Output:**
- `wantedLevel: int (variable)`

---

### `01F5` GET_PLAYER_CHAR
Gets the character handle for the specified player

**Class:** `Player.GetChar`

**Input:**
- `self: Player`

**Output:**
- `handle: Char (variable)`

---

### `0221` APPLY_BRAKES_TO_PLAYERS_CAR
Applies brakes to the player's car

**Class:** `Player.ApplyBrakesToCar`

**Input:**
- `self: Player`
- `state: bool`

---

### `0241` IS_PLAYER_IN_REMOTE_MODE
Returns true if the player is controlling a remote-control vehicle

**Class:** `Player.IsInRemoteMode`
**Flags:** condition

**Input:**
- `self: Player`

---

### `0256` IS_PLAYER_PLAYING
Returns true if the player hasn't been wasted or busted (the player is still playing)

**Class:** `Player.IsPlaying`
**Flags:** condition

**Input:**
- `self: Player`

---

### `0297` RESET_NUM_OF_MODELS_KILLED_BY_PLAYER
Resets the count of how many times the player has destroyed a certain model

**Class:** `Player.ResetNumOfModelsKilled`

**Input:**
- `self: Player`

---

### `0298` GET_NUM_OF_MODELS_KILLED_BY_PLAYER
Returns the number of times the player has destroyed a specific model

**Class:** `Player.GetNumOfModelsKilled`

**Input:**
- `self: Player`
- `modelId: model_any`

**Output:**
- `amount: int (variable)`

---

### `0330` SET_PLAYER_NEVER_GETS_TIRED
Defines whether the player can run fast forever

**Class:** `Player.SetNeverGetsTired`

**Input:**
- `self: Player`
- `state: bool`

---

### `0331` SET_PLAYER_FAST_RELOAD
Defines whether the player can reload their gun 4x times faster

**Class:** `Player.SetFastReload`

**Input:**
- `self: Player`
- `state: bool`

---

### `03EE` CAN_PLAYER_START_MISSION
Returns true if the player can move

**Class:** `Player.CanStartMission`
**Flags:** condition

**Input:**
- `self: Player`

---

### `03EF` MAKE_PLAYER_SAFE_FOR_CUTSCENE
Makes the player safe, putting the character in a safe location

**Class:** `Player.MakeSafeForCutscene`

**Input:**
- `self: Player`

---

### `0414` SET_FREE_HEALTH_CARE
Sets whether the player loses the cash when gets wasted (works once)

**Class:** `Player.SetFreeHealthCare`

**Input:**
- `self: Player`
- `state: bool`

---

### `0457` IS_PLAYER_TARGETTING_CHAR
Returns true if the player is aiming at the specified character

**Class:** `Player.IsTargetingChar`
**Flags:** condition

**Input:**
- `self: Player`
- `handle: Char`

---

### `0458` IS_PLAYER_TARGETTING_OBJECT
Returns true if the player is aiming at the specified object

**Class:** `Player.IsTargetingObject`
**Flags:** condition

**Input:**
- `self: Player`
- `handle: Object`

---

### `04E3` SET_PLAYER_MOOD
Sets the players mood, affecting the dialogue spoken by the player

**Class:** `Player.SetMood`

**Input:**
- `self: Player`
- `mood: PlayerMood`
- `time: int`

---

### `04FC` GET_WHEELIE_STATS
Returns the stats of the most recent wheelie or stoppie attempt

**Class:** `Player.GetWheelieStats`

**Input:**
- `self: Player`

**Output:**
- `twoWheelsTime: int (variable)`
- `twoWheelsDistance: float (variable)`
- `wheelieTime: int (variable)`
- `wheelieDistance: float (variable)`
- `stoppieTime: int (variable)`
- `stoppieDistance: float (variable)`

---

### `0500` IS_PLAYER_WEARING
Returns true if the player's bodypart has the specified model (0784 or 087B) 

**Class:** `Player.IsWearing`
**Flags:** condition

**Input:**
- `self: Player`
- `bodyPart: BodyPart`
- `modelName: string`

---

### `0501` SET_PLAYER_CAN_DO_DRIVE_BY
Sets the players driveby mode

**Class:** `Player.SetCanDoDriveBy`

**Input:**
- `self: Player`
- `state: bool`

---

### `052C` SET_PLAYER_DRUNKENNESS
Makes the camera start moving around in a swirling motion with the specified intensity as if drunk

**Class:** `Player.SetDrunkenness`

**Input:**
- `self: Player`
- `intensity: int`

---

### `055D` MAKE_PLAYER_FIRE_PROOF
Makes the player immune to fire

**Class:** `Player.MakeFireProof`

**Input:**
- `self: Player`
- `state: bool`

---

### `055E` INCREASE_PLAYER_MAX_HEALTH
Increases the player's max health by the specified value and changes current health to the new maximum

**Class:** `Player.IncreaseMaxHealth`

**Input:**
- `self: Player`
- `value: int`

---

### `055F` INCREASE_PLAYER_MAX_ARMOUR
Increases the player's max armor by the specified value and changes current armor to the new maximum

**Class:** `Player.IncreaseMaxArmor`

**Input:**
- `self: Player`
- `value: int`

---

### `0563` ENSURE_PLAYER_HAS_DRIVE_BY_WEAPON
Sets the amount of ammo a player has during a driveby

**Class:** `Player.EnsureHasDriveByWeapon`

**Input:**
- `self: Player`
- `ammo: int`

---

### `0583` IS_PLAYER_IN_INFO_ZONE
Returns true if the player is in the specified zone

**Class:** `Player.IsInInfoZone`
**Flags:** condition

**Input:**
- `self: Player`
- `infoZone: gxt_key`

---

### `068C` IS_PLAYER_TARGETTING_ANYTHING
Returns true if the specified player is auto-aiming at a ped or object

**Class:** `Player.IsTargetingAnything`
**Flags:** condition

**Input:**
- `self: Player`

---

### `06AF` DISABLE_PLAYER_SPRINT

**Class:** `Player.DisableSprint`

**Input:**
- `self: Player`
- `state: bool`

---

### `06DF` DELETE_PLAYER
Removes the specified player

**Class:** `Player.Delete`
**Flags:** destructor

**Input:**
- `self: Player`

---

### `070D` BUILD_PLAYER_MODEL
Rebuilds the player model, applying any required texture changes

**Class:** `Player.BuildModel`

**Input:**
- `self: Player`

---

### `0784` GIVE_PLAYER_CLOTHES

**Class:** `Player.GiveClothes`

**Input:**
- `self: Player`
- `textureHash: int`
- `modelHash: int`
- `bodyPart: BodyPart`

---

### `0793` STORE_CLOTHES_STATE
Stores the players current clothes to later be restored with 0794

**Class:** `Player.StoreClothesState`
**Flags:** static

---

### `0794` RESTORE_CLOTHES_STATE
Restores the players clothes stored with 0793

**Class:** `Player.RestoreClothesState`
**Flags:** static

---

### `07AF` GET_PLAYER_GROUP

**Class:** `Player.GetGroup`

**Input:**
- `self: Player`

**Output:**
- `handle: Group (variable)`

---

### `07B4` SET_PLAYER_GROUP_RECRUITMENT
Sets the player's ability to recruit new members to the group

**Class:** `Player.SetGroupRecruitment`

**Input:**
- `self: Player`
- `state: bool`

---

### `07F1` IS_PLAYER_PERFORMING_WHEELIE

**Class:** `Player.IsPerformingWheelie`
**Flags:** condition

**Input:**
- `self: Player`

**Details:**

This conditional command returns true when the player is performing a wheelie. A wheelie is being performed if only the rear wheel of a motorcycle or bicycle is touching the ground. The body of the bike and the front wheel cannot touch any solid surface.

---

### `07F2` IS_PLAYER_PERFORMING_STOPPIE
Returns true if the player is performing a stoppie

**Class:** `Player.IsPerformingStoppie`
**Flags:** condition

**Input:**
- `self: Player`

**Details:**

This conditional command returns true when the player is performing a stoppie. A stoppie is being performed if only the front wheel of a motorcycle or bicycle is touching the ground. The body of the bike and the rear wheel cannot touch any solid surface.

---

### `0806` GET_TOTAL_NUMBER_OF_PEDS_KILLED_BY_PLAYER
Returns the number of peds killed by the player since the last reset (0297)

**Class:** `Player.GetTotalNumberOfPedsKilled`

**Input:**
- `self: Player`

**Output:**
- `numPeds: int (variable)`

---

### `0842` GET_CITY_PLAYER_IS_IN
Gets the player's current city

**Class:** `Player.GetCityIsIn`

**Input:**
- `self: Player`

**Output:**
- `level: Level (variable)`

---

### `0858` SET_HEADING_FOR_ATTACHED_PLAYER
Sets the view angle for the player attached to an object or vehicle

**Class:** `Player.SetHeadingForAttached`

**Input:**
- `self: Player`
- `heading: float`
- `headingRange: float`

---

### `0861` IS_ATTACHED_PLAYER_HEADING_ACHIEVED
Returns true if the heading has finished being applied, as started by 0858

**Class:** `Player.IsAttachedHeadingAchieved`
**Flags:** condition

**Input:**
- `self: Player`

---

### `087B` GIVE_PLAYER_CLOTHES_OUTSIDE_SHOP
Sets the players clothing

**Class:** `Player.GiveClothesOutsideShop`

**Input:**
- `self: Player`
- `textureName: string`
- `modelName: string`
- `bodyPart: BodyPart`

---

### `08F5` MAKE_PLAYER_GANG_DISAPPEAR

**Class:** `Player.MakeGangDisappear`
**Flags:** static

---

### `08F6` MAKE_PLAYER_GANG_REAPPEAR

**Class:** `Player.MakeGangReappear`
**Flags:** static

---

### `08F7` GET_CLOTHES_ITEM

**Class:** `Player.GetClothesItem`

**Input:**
- `self: Player`
- `bodyPart: BodyPart`

**Output:**
- `textureHash: int (variable)`
- `modelHash: int (variable)`

---

### `0945` GET_PLAYER_MAX_ARMOUR

**Class:** `Player.GetMaxArmor`

**Input:**
- `self: Player`

**Output:**
- `maxArmour: int (variable)`

---

### `09C7` SET_PLAYER_MODEL
Changes the player to use the specified model

**Class:** `Player.SetModel`

**Input:**
- `self: Player`
- `modelId: int`

---

### `09D7` FORCE_INTERIOR_LIGHTING_FOR_PLAYER

**Class:** `Player.ForceInteriorLighting`

**Input:**
- `self: Player`
- `state: bool`

---

### `09D9` USE_DETONATOR
Detonates all satchel charges and car bombs planted by the player

**Class:** `Player.UseDetonator`
**Flags:** static

---

### `09E7` IS_PLAYER_CONTROL_ON
Returns true if the player control hasn't been disabled using 01B4

**Class:** `Player.IsControlOn`
**Flags:** condition

**Input:**
- `self: Player`

---

### `09EB` PLAYER_TAKE_OFF_GOGGLES
Removes the players Goggles and disables night/heat vision

**Class:** `Player.TakeOffGoggles`

**Input:**
- `self: Player`
- `animate: bool`

---

### `0A0C` IS_PLAYER_USING_JETPACK
Returns true if player is using a jetpack

**Class:** `Player.IsUsingJetpack`
**Flags:** condition

**Input:**
- `self: Player`

---

### `0A20` SET_PLAYER_GROUP_TO_FOLLOW_ALWAYS
Controls the players ability to tell their group to wait and automatically orders any group members to continue following

**Class:** `Player.SetGroupToFollowAlways`

**Input:**
- `self: Player`
- `state: bool`

---

### `0A29` IS_PLAYER_CLIMBING
Returns true if the player is climbing

**Class:** `Player.IsClimbing`
**Flags:** condition

**Input:**
- `self: Player`

---

### `0A31` SET_PLAYER_GROUP_TO_FOLLOW_NEVER
Sets whether the player's group stops following the player, even if the player uses the "group follow" button

**Class:** `Player.SetGroupToFollowNever`

**Input:**
- `self: Player`
- `state: bool`

---

### `0A3A` IS_LAST_BUILDING_MODEL_SHOT_BY_PLAYER
Returns true if the player's last shot model is the model specified

**Class:** `Player.IsLastBuildingModelShot`
**Flags:** condition

**Input:**
- `self: Player`
- `modelId: model_any`

---

### `0A3B` CLEAR_LAST_BUILDING_MODEL_SHOT_BY_PLAYER
Resets the status of the last model the player has shot

**Class:** `Player.ClearLastBuildingModelShot`

**Input:**
- `self: Player`

---
