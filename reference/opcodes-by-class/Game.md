# Game Opcodes

> 83 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `01F0` | SET_MAX_WANTED_LEVEL | Sets the maximum wanted level the player can receive |
| `01F7` | SET_POLICE_IGNORE_PLAYER | Sets whether cops should ignore the player regardless of wanted level |
| `02ED` | SET_COLLECTABLE1_TOTAL | Sets the total number of hidden packages to collect |
| `0335` | SET_FREE_RESPRAYS | Defines whether the player can respray their car for free |
| `03BF` | SET_EVERYONE_IGNORE_PLAYER | Makes pedestrians pay no attention to the player |
| `03C7` | SET_WANTED_MULTIPLIER | Sets sensitivity to crime, changing how many crimes a player can commit before p |
| `03D8` | ACTIVATE_SAVE_MENU | Schedules save game menu to be displayed on next render frame |
| `03D9` | HAS_SAVE_GAME_FINISHED | Returns false if save game menu was requested with activate_save_menu command, b |
| `03F4` | SET_ALL_CARS_CAN_BE_DAMAGED | Sets whether all cars receive damage |
| `040C` | IS_GERMAN_GAME | Returns true if the game language is set to German |
| `0424` | ARE_MEASUREMENTS_IN_METRES | Returns true if the game uses metric measurements (meters instead of feet) |
| `0445` | ARE_ANY_CAR_CHEATS_ACTIVATED | Returns true if the player has used any of the cheats |
| `0485` | IS_PC_VERSION | Returns true on PC versions of the game |
| `050F` | GET_MAX_WANTED_LEVEL | Gets the maximum wanted level the player can receive |
| `0572` | SET_ALL_TAXIS_HAVE_NITRO | Toggles whether all taxis have nitrous |
| `057E` | SET_PLAYER_IS_IN_STADIUM | Greys out the radar |
| `059A` | IS_AUSTRALIAN_GAME | Returns true if the current game is an Australian release |
| `06C8` | SET_LA_RIOTS | Enables the LS Riots, making smoke appear on houses, random car fires occur, ped |
| `06D0` | SWITCH_EMERGENCY_SERVICES | Sets whether emergency traffic spawns |
| `06D7` | SWITCH_RANDOM_TRAINS | Sets whether trains are generated |
| `06F1` | LIMIT_TWO_PLAYER_DISTANCE | Sets how far apart players can get on 2-player mode |
| `06F2` | RELEASE_TWO_PLAYER_DISTANCE | Releases the distance limit set by LIMIT_TWO_PLAYER_DISTANCE |
| `06F3` | SET_PLAYER_PLAYER_TARGETTING | Enables each player to target the other player |
| `06FA` | SET_PLAYERS_CAN_BE_IN_SEPARATE_CARS | Sets whether the players can be in separate cars during a 2-player mission |
| `072C` | SWITCH_COPS_ON_BIKES | Disables the game from creating police bikes and their riders on the roads |
| `0746` | SET_RELATIONSHIP | Sets the attitude of peds with one pedtype towards peds of another pedtype |
| `0747` | CLEAR_RELATIONSHIP |  |
| `07A8` | SET_AREA51_SAM_SITE | Enables or disables the SAM site at the Area 51 |
| `07E8` | IS_RELATIONSHIP_SET | Returns true if the specified relationship between ped types is set |
| `0800` | IS_2PLAYER_GAME_GOING_ON | Returns true if the game is in 2-player mode |
| `0828` | SET_MAX_FIRE_GENERATIONS | Sets the limit on how many fires can be created from other fires when "propagati |
| `084D` | ACTIVATE_INTERIOR_PEDS | Enables ped spawning in interiors |
| `0864` | ENABLE_ENTRY_EXIT_PLAYER_GROUP_WARPING | Enables the entry/exit marker in the specified radius of the coordinates |
| `0867` | IS_PROCEDURAL_INTERIOR_ACTIVE | Returns true in interactive interiors |
| `0879` | SET_GANG_WARS_ACTIVE | Sets whether gang wars can be started by the player or enemy gangs |
| `087A` | IS_GANG_WAR_GOING_ON | Returns true if there is a gang war happening |
| `08A3` | CAN_TRIGGER_GANG_WAR_WHEN_ON_A_MISSION | Allows the player to provoke turf wars while a mission is active |
| `08A8` | SET_ALWAYS_DRAW_3D_MARKERS | Enables an increase in the distance that markers hovering above entities can be  |
| `08AC` | SET_GANG_WARS_TRAINING_MISSION | Disables highlighting of gang territory on the map and radar |
| `08B1` | SET_NIGHT_VISION | Enables night vision effects |
| `08B2` | SET_INFRARED_VISION | Enables thermal vision effects |
| `08DD` | SWITCH_DEATH_PENALTIES | Sets whether or not the player loses their weapons and inventory when taken to h |
| `08DE` | SWITCH_ARREST_PENALTIES | Sets whether or not the player loses their weapons and inventory when busted |
| `08EA` | SET_CREATE_RANDOM_GANG_MEMBERS | Sets whether gang members will spawn |
| `08F4` | SET_SCRIPT_LIMIT_TO_GANG_SIZE | Sets the maximum number of members that the player can recruit |
| `090D` | CLEAR_SPECIFIC_ZONES_TO_TRIGGER_GANG_WAR | Enables turf wars to be provoked in all zones |
| `0923` | SWITCH_AMBIENT_PLANES | Enables or disables planes |
| `0956` | FIND_MAX_NUMBER_OF_GROUP_MEMBERS | Returns a number of group members the player can recruit with the current respec |
| `096A` | SWITCH_POLICE_HELIS | Sets whether ghetto birds spawn |
| `0970` | FORCE_DEATH_RESTART | Triggers usual after player death game bahavior (respawn in front of the hospita |
| `0974` | RESET_STUFF_UPON_RESURRECTION | Emulates the shared effects of being wasted or busted |
| `0983` | SET_ONLY_CREATE_GANG_MEMBERS | Sets whether gangs appear everywhere, like when "Gangs control the streets" chea |
| `098A` | SET_GUNSHOT_SENSE_RANGE_FOR_RIOT2 |  |
| `098E` | SET_NAMED_ENTRY_EXIT_FLAG | Sets the specified enex flag |
| `099D` | IS_NIGHT_VISION_ACTIVE | Returns true if night vision is active |
| `099E` | SET_CREATE_RANDOM_COPS |  |
| `09A6` | SHOW_BLIPS_ON_ALL_LEVELS | Enables entity blips showing on the radar and map while in interiors |
| `09AC` | HIDE_ALL_FRONTEND_BLIPS |  |
| `09BD` | SET_MINIGAME_IN_PROGRESS | Disables displaying help messages in other scripts |
| `09BE` | IS_MINIGAME_IN_PROGRESS | Returns true if 09BD has been used in any script to disable help messages |
| `09BF` | SET_FORCE_RANDOM_CAR_MODEL | Forces all cars spawned to be of the specified model |
| `09C8` | ARE_SUBTITLES_SWITCHED_ON | Returns true if subtitles are switched on in the settings menu |
| `09D2` | ENABLE_AMBIENT_CRIME | Sets whether cops will chase and kill criminals when their task is 'TASK_COMPLEX |
| `09D4` | CLEAR_WANTED_LEVEL_IN_GARAGE | Suspends the current players wanted level |
| `09DD` | MAKE_ROOM_IN_PLAYER_GANG_FOR_MISSION_PEDS | Ensures there is x amount of space for new members to be added to the players ga |
| `09E4` | SET_AIRCRAFT_CARRIER_SAM_SITE | Enables missiles to be fired from the aircraft carrier by Easter Bay Naval Stati |
| `09E6` | ENABLE_BURGLARY_HOUSES | Switches enex markers used for burglary missions on or off |
| `09F5` | SHUT_ALL_CHARS_UP | Prevents all peds from attempting to start conversations with the player |
| `09F8` | DO_WEAPON_STUFF_AT_START_OF_2P_GAME | Gives all the weapons of player 1 to player 2 during a cooperative mission |
| `09FA` | HAS_GAME_JUST_RETURNED_FROM_FRONTEND | Returns true if the player just exited the menu on the last frame |
| `09FB` | GET_CURRENT_LANGUAGE | Returns the current language set in the menu language settings |
| `0A03` | IS_GANG_WAR_FIGHTING_GOING_ON | Returns true if the player provoked a gang war or is defending territory |
| `0A0F` | HAS_LANGUAGE_CHANGED | Returns true if the current language set is different from the previous language |
| `0A13` | MANAGE_ALL_POPULATION | Deletes distant, no longer needed, objects and world dummy objects |
| `0A14` | SET_NO_RESPRAYS | Disables respray garages from opening for the player |
| `0A2B` | IS_WIDESCREEN_ON_IN_OPTIONS | Returns true if widescreen is switched on in the display settings |
| `0A37` | FORCE_ALL_VEHICLE_LIGHTS_OFF | Disables all vehicle lights from being rendered if enabled |
| `0A3D` | ACTIVATE_PIMP_CHEAT | Sets whether sleeping with a prostitute earns you money instead of taking it awa |
| `0A3F` | SET_SCRIPT_COOP_GAME | Sets an unused flag at address 0x96A8A8 |
| `0A43` | GET_RID_OF_PLAYER_PROSTITUTE | Cancels any prostitute invitations received in-game and makes any current prosti |
| `0A46` | SWITCH_OBJECT_BRAINS | Enables or disables all object triggers with the specified grouping id (set with |
| `0A48` | ALLOW_PAUSE_IN_WIDESCREEN | Enables the player to access the pause menu while widescreen is enabled |
| `0A4B` | IS_PC_USING_JOYPAD | Returns true if players controls are set to joystick and not mouse+keyboard |

## Detailed Reference

### `01F0` SET_MAX_WANTED_LEVEL
Sets the maximum wanted level the player can receive

**Class:** `Game.SetMaxWantedLevel`
**Flags:** static

**Input:**
- `wantedLevel: int`

**Details:**

In San Andreas, cheats increasing wanted level also change the maximum wanted level.

---

### `01F7` SET_POLICE_IGNORE_PLAYER
Sets whether cops should ignore the player regardless of wanted level

**Class:** `Game.SetPoliceIgnorePlayer`
**Flags:** static

**Input:**
- `player: Player`
- `state: bool`

---

### `02ED` SET_COLLECTABLE1_TOTAL
Sets the total number of hidden packages to collect

**Class:** `Game.SetCollectableTotal`
**Flags:** static

**Input:**
- `amount: int`

---

### `0335` SET_FREE_RESPRAYS
Defines whether the player can respray their car for free

**Class:** `Game.SetFreeResprays`
**Flags:** static

**Input:**
- `state: bool`

---

### `03BF` SET_EVERYONE_IGNORE_PLAYER
Makes pedestrians pay no attention to the player

**Class:** `Game.SetEveryoneIgnorePlayer`
**Flags:** static

**Input:**
- `player: Player`
- `state: bool`

---

### `03C7` SET_WANTED_MULTIPLIER
Sets sensitivity to crime, changing how many crimes a player can commit before police begin to pursue

**Class:** `Game.SetWantedMultiplier`
**Flags:** static

**Input:**
- `multiplier: float`

---

### `03D8` ACTIVATE_SAVE_MENU
Schedules save game menu to be displayed on next render frame

**Class:** `Game.ActivateSaveMenu`
**Flags:** static

---

### `03D9` HAS_SAVE_GAME_FINISHED
Returns false if save game menu was requested with activate_save_menu command, but not displayed yet

**Class:** `Game.HasSaveGameFinished`
**Flags:** condition, static

---

### `03F4` SET_ALL_CARS_CAN_BE_DAMAGED
Sets whether all cars receive damage

**Class:** `Game.SetAllCarsCanBeDamaged`
**Flags:** static

**Input:**
- `state: bool`

---

### `040C` IS_GERMAN_GAME
Returns true if the game language is set to German

**Class:** `Game.IsGerman`
**Flags:** condition, static

---

### `0424` ARE_MEASUREMENTS_IN_METRES
Returns true if the game uses metric measurements (meters instead of feet)

**Class:** `Game.AreMeasurementsInMeters`
**Flags:** condition, static

---

### `0445` ARE_ANY_CAR_CHEATS_ACTIVATED
Returns true if the player has used any of the cheats

**Class:** `Game.AreAnyCarCheatsActivated`
**Flags:** condition, static

---

### `0485` IS_PC_VERSION
Returns true on PC versions of the game

**Class:** `Game.IsPcVersion`
**Flags:** condition, static

---

### `050F` GET_MAX_WANTED_LEVEL
Gets the maximum wanted level the player can receive

**Class:** `Game.GetMaxWantedLevel`
**Flags:** static

**Output:**
- `level: int (variable)`

---

### `0572` SET_ALL_TAXIS_HAVE_NITRO
Toggles whether all taxis have nitrous

**Class:** `Game.SetAllTaxisHaveNitro`
**Flags:** static

**Input:**
- `state: bool`

**Details:**

This command activates both the taxi's boost jump and nitrous. Boost jump replaces the horn, which can be activated by pressing button `18` (HORN key). The value set with this opcode is saved in block 0 of the save file. This only works on the player's taxi. It recognizes the following as taxis:

| **Id** | **Name** |
| ------ | -------- |
| 420    | Taxi     |
| 438    | Cabbie   |

---

### `057E` SET_PLAYER_IS_IN_STADIUM
Greys out the radar

**Class:** `Game.SetIsInStadium`
**Flags:** static

**Input:**
- `state: bool`

**Details:**

This opcode greys the "radar" mini-map on the bottom left corner of the HUD. It is usually used to cover up the mini-map without disabling it. The color of grey is `204,204,204` in RGB or `#CCCCCC` in hexadecimal.

---

### `059A` IS_AUSTRALIAN_GAME
Returns true if the current game is an Australian release

**Class:** `Game.IsAustralian`
**Flags:** condition, static

---

### `06C8` SET_LA_RIOTS
Enables the LS Riots, making smoke appear on houses, random car fires occur, peds stealing things and attacking each other in a frenzy

**Class:** `Game.SetLaRiots`
**Flags:** static

**Input:**
- `state: bool`

---

### `06D0` SWITCH_EMERGENCY_SERVICES
Sets whether emergency traffic spawns

**Class:** `Game.SwitchEmergencyServices`
**Flags:** static

**Input:**
- `state: bool`

---

### `06D7` SWITCH_RANDOM_TRAINS
Sets whether trains are generated

**Class:** `Game.SwitchRandomTrains`
**Flags:** static

**Input:**
- `state: bool`

---

### `06F1` LIMIT_TWO_PLAYER_DISTANCE
Sets how far apart players can get on 2-player mode

**Class:** `Game.LimitTwoPlayerDistance`
**Flags:** static

**Input:**
- `distance: float`

---

### `06F2` RELEASE_TWO_PLAYER_DISTANCE
Releases the distance limit set by LIMIT_TWO_PLAYER_DISTANCE

**Class:** `Game.ReleaseTwoPlayerDistance`
**Flags:** static

---

### `06F3` SET_PLAYER_PLAYER_TARGETTING
Enables each player to target the other player

**Class:** `Game.SetPlayerPlayerTargeting`
**Flags:** static

**Input:**
- `state: bool`

---

### `06FA` SET_PLAYERS_CAN_BE_IN_SEPARATE_CARS
Sets whether the players can be in separate cars during a 2-player mission

**Class:** `Game.SetPlayersCanBeInSeparateCars`
**Flags:** static

**Input:**
- `state: bool`

---

### `072C` SWITCH_COPS_ON_BIKES
Disables the game from creating police bikes and their riders on the roads

**Class:** `Game.SwitchCopsOnBikes`
**Flags:** static

**Input:**
- `state: bool`

**Details:**

This command sets cops on the bikes to patrol the streets. It does not affect any other kinds of the police patrols.

---

### `0746` SET_RELATIONSHIP
Sets the attitude of peds with one pedtype towards peds of another pedtype

**Class:** `Game.SetRelationship`
**Flags:** static

**Input:**
- `relationshipType: RelationshipType`
- `ofPedType: PedType`
- `toPedType: PedType`

---

### `0747` CLEAR_RELATIONSHIP

**Class:** `Game.ClearRelationship`
**Flags:** static

**Input:**
- `relationshipType: RelationshipType`
- `ofPedType: PedType`
- `toPedType: PedType`

---

### `07A8` SET_AREA51_SAM_SITE
Enables or disables the SAM site at the Area 51

**Class:** `Game.SetArea51SamSite`
**Flags:** static

**Input:**
- `state: bool`

---

### `07E8` IS_RELATIONSHIP_SET
Returns true if the specified relationship between ped types is set

**Class:** `Game.IsRelationshipSet`
**Flags:** condition, static

**Input:**
- `relationshipType: RelationshipType`
- `ofPedType: PedType`
- `toPedType: PedType`

---

### `0800` IS_2PLAYER_GAME_GOING_ON
Returns true if the game is in 2-player mode

**Class:** `Game.Is2PlayerGameGoingOn`
**Flags:** condition, static

---

### `0828` SET_MAX_FIRE_GENERATIONS
Sets the limit on how many fires can be created from other fires when "propagation" was enabled on 02CF

**Class:** `Game.SetMaxFireGenerations`
**Flags:** static

**Input:**
- `limit: int`

---

### `084D` ACTIVATE_INTERIOR_PEDS
Enables ped spawning in interiors

**Class:** `Game.ActivateInteriorPeds`
**Flags:** static

**Input:**
- `state: bool`

---

### `0864` ENABLE_ENTRY_EXIT_PLAYER_GROUP_WARPING
Enables the entry/exit marker in the specified radius of the coordinates

**Class:** `Game.EnableEntryExitPlayerGroupWarping`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `radius: float`
- `state: bool`

---

### `0867` IS_PROCEDURAL_INTERIOR_ACTIVE
Returns true in interactive interiors

**Class:** `Game.IsProceduralInteriorActive`
**Flags:** condition, static

**Input:**
- `areaId: int`

---

### `0879` SET_GANG_WARS_ACTIVE
Sets whether gang wars can be started by the player or enemy gangs

**Class:** `Game.SetGangWarsActive`
**Flags:** static

**Input:**
- `state: bool`

---

### `087A` IS_GANG_WAR_GOING_ON
Returns true if there is a gang war happening

**Class:** `Game.IsGangWarGoingOn`
**Flags:** condition, static

---

### `08A3` CAN_TRIGGER_GANG_WAR_WHEN_ON_A_MISSION
Allows the player to provoke turf wars while a mission is active

**Class:** `Game.CanTriggerGangWarWhenOnAMission`
**Flags:** static

**Input:**
- `state: bool`

---

### `08A8` SET_ALWAYS_DRAW_3D_MARKERS
Enables an increase in the distance that markers hovering above entities can be seen from

**Class:** `Game.SetAlwaysDraw3DMarkers`
**Flags:** static

**Input:**
- `state: bool`

---

### `08AC` SET_GANG_WARS_TRAINING_MISSION
Disables highlighting of gang territory on the map and radar

**Class:** `Game.SetGangWarsTrainingMission`
**Flags:** static

**Input:**
- `state: bool`

---

### `08B1` SET_NIGHT_VISION
Enables night vision effects

**Class:** `Game.SetNightVision`
**Flags:** static

**Input:**
- `state: bool`

---

### `08B2` SET_INFRARED_VISION
Enables thermal vision effects

**Class:** `Game.SetInfraredVision`
**Flags:** static

**Input:**
- `state: bool`

**Details:**

This command sets infrared vision. It is the same effect as wearing the thermal goggles.

---

### `08DD` SWITCH_DEATH_PENALTIES
Sets whether or not the player loses their weapons and inventory when taken to hospital

**Class:** `Game.SwitchDeathPenalties`
**Flags:** static

**Input:**
- `state: bool`

---

### `08DE` SWITCH_ARREST_PENALTIES
Sets whether or not the player loses their weapons and inventory when busted

**Class:** `Game.SwitchArrestPenalties`
**Flags:** static

**Input:**
- `state: bool`

---

### `08EA` SET_CREATE_RANDOM_GANG_MEMBERS
Sets whether gang members will spawn

**Class:** `Game.SetCreateRandomGangMembers`
**Flags:** static

**Input:**
- `state: bool`

---

### `08F4` SET_SCRIPT_LIMIT_TO_GANG_SIZE
Sets the maximum number of members that the player can recruit

**Class:** `Game.SetScriptLimitToGangSize`
**Flags:** static

**Input:**
- `maxSize: int`

---

### `090D` CLEAR_SPECIFIC_ZONES_TO_TRIGGER_GANG_WAR
Enables turf wars to be provoked in all zones

**Class:** `Game.ClearSpecificZonesToTriggerGangWar`
**Flags:** static

---

### `0923` SWITCH_AMBIENT_PLANES
Enables or disables planes

**Class:** `Game.SwitchAmbientPlanes`
**Flags:** static

**Input:**
- `state: bool`

---

### `0956` FIND_MAX_NUMBER_OF_GROUP_MEMBERS
Returns a number of group members the player can recruit with the current respect

**Class:** `Game.FindMaxNumberOfGroupMembers`
**Flags:** static

**Output:**
- `maxNum: int (variable)`

**Details:**

This command returns a maximum number of members in the player's group. This number depends on the total respect (stat 64):

* 0-9 : 0 members
* 10-59 : 2 members
* 60-159 : 3 members
* 160-329 : 4 members
* 330-539 : 5 members
* 540-799 : 6 members
* 800+ : 7 members

---

### `096A` SWITCH_POLICE_HELIS
Sets whether ghetto birds spawn

**Class:** `Game.SwitchPoliceHelis`
**Flags:** static

**Input:**
- `state: bool`

---

### `0970` FORCE_DEATH_RESTART
Triggers usual after player death game bahavior (respawn in front of the hospital, weapons taken away, etc.)

**Class:** `Game.ForceDeathRestart`
**Flags:** static

---

### `0974` RESET_STUFF_UPON_RESURRECTION
Emulates the shared effects of being wasted or busted

**Class:** `Game.ResetStuffUponResurrection`
**Flags:** static

---

### `0983` SET_ONLY_CREATE_GANG_MEMBERS
Sets whether gangs appear everywhere, like when "Gangs control the streets" cheat is activated

**Class:** `Game.SetOnlyCreateGangMembers`
**Flags:** static

**Input:**
- `state: bool`

---

### `098A` SET_GUNSHOT_SENSE_RANGE_FOR_RIOT2

**Class:** `Game.SetGunshotSenseRangeForRiot2`
**Flags:** static

**Input:**
- `range: float`

---

### `098E` SET_NAMED_ENTRY_EXIT_FLAG
Sets the specified enex flag

**Class:** `Game.SetNamedEntryExitFlag`
**Flags:** static

**Input:**
- `name: string`
- `flag: EntryexitsFlag`
- `state: bool`

---

### `099D` IS_NIGHT_VISION_ACTIVE
Returns true if night vision is active

**Class:** `Game.IsNightVisionActive`
**Flags:** condition, static

**Details:**

This conditional command returns true if night vision is active, which usually happens when a player wears night vision googles.

---

### `099E` SET_CREATE_RANDOM_COPS

**Class:** `Game.SetCreateRandomCops`
**Flags:** static

**Input:**
- `state: bool`

---

### `09A6` SHOW_BLIPS_ON_ALL_LEVELS
Enables entity blips showing on the radar and map while in interiors

**Class:** `Game.ShowBlipsOnAllLevels`
**Flags:** static

**Input:**
- `state: bool`

---

### `09AC` HIDE_ALL_FRONTEND_BLIPS

**Class:** `Game.HideAllFrontendBlips`
**Flags:** static

**Input:**
- `state: bool`

---

### `09BD` SET_MINIGAME_IN_PROGRESS
Disables displaying help messages in other scripts

**Class:** `Game.SetMinigameInProgress`
**Flags:** static

**Input:**
- `state: bool`

---

### `09BE` IS_MINIGAME_IN_PROGRESS
Returns true if 09BD has been used in any script to disable help messages

**Class:** `Game.IsMinigameInProgress`
**Flags:** condition, static

---

### `09BF` SET_FORCE_RANDOM_CAR_MODEL
Forces all cars spawned to be of the specified model

**Class:** `Game.SetForceRandomCarModel`
**Flags:** static

**Input:**
- `modelId: model_vehicle`

---

### `09C8` ARE_SUBTITLES_SWITCHED_ON
Returns true if subtitles are switched on in the settings menu

**Class:** `Game.AreSubtitlesSwitchedOn`
**Flags:** condition, static

**Details:**

This conditional command returns true if the subtitles menu option is switched on.

---

### `09D2` ENABLE_AMBIENT_CRIME
Sets whether cops will chase and kill criminals when their task is 'TASK_COMPLEX_KILL_CRIMINAL'

**Class:** `Game.EnableAmbientCrime`
**Flags:** static

**Input:**
- `state: bool`

---

### `09D4` CLEAR_WANTED_LEVEL_IN_GARAGE
Suspends the current players wanted level

**Class:** `Game.ClearWantedLevelInGarage`
**Flags:** static

---

### `09DD` MAKE_ROOM_IN_PLAYER_GANG_FOR_MISSION_PEDS
Ensures there is x amount of space for new members to be added to the players gang

**Class:** `Game.MakeRoomInPlayerGangForMissionPeds`
**Flags:** static

**Input:**
- `_p1: int`

---

### `09E4` SET_AIRCRAFT_CARRIER_SAM_SITE
Enables missiles to be fired from the aircraft carrier by Easter Bay Naval Station, San Fierro

**Class:** `Game.SetAircraftCarrierSamSite`
**Flags:** static

**Input:**
- `state: bool`

---

### `09E6` ENABLE_BURGLARY_HOUSES
Switches enex markers used for burglary missions on or off

**Class:** `Game.EnableBurglaryHouses`
**Flags:** static

**Input:**
- `state: bool`

---

### `09F5` SHUT_ALL_CHARS_UP
Prevents all peds from attempting to start conversations with the player

**Class:** `Game.ShutAllCharsUp`
**Flags:** static

**Input:**
- `state: bool`

---

### `09F8` DO_WEAPON_STUFF_AT_START_OF_2P_GAME
Gives all the weapons of player 1 to player 2 during a cooperative mission

**Class:** `Game.DoWeaponStuffAtStartOf2PGame`
**Flags:** static

---

### `09FA` HAS_GAME_JUST_RETURNED_FROM_FRONTEND
Returns true if the player just exited the menu on the last frame

**Class:** `Game.HasGameJustReturnedFromFrontend`
**Flags:** condition, static

**Details:**

This conditional command returns true if the main menu is closed. It is commonly used in pair with HAS_LANGUAGE_CHANGED.

---

### `09FB` GET_CURRENT_LANGUAGE
Returns the current language set in the menu language settings

**Class:** `Game.GetCurrentLanguage`
**Flags:** static

**Output:**
- `languageSlot: Language (variable)`

---

### `0A03` IS_GANG_WAR_FIGHTING_GOING_ON
Returns true if the player provoked a gang war or is defending territory

**Class:** `Game.IsGangWarFightingGoingOn`
**Flags:** condition, static

---

### `0A0F` HAS_LANGUAGE_CHANGED
Returns true if the current language set is different from the previous language set

**Class:** `Game.HasLanguageChanged`
**Flags:** condition, static

**Details:**

This conditional command returns true if a player has set new language via the main menu. Mainly it is used to refresh the texts of the currently shown panel with new language.

---

### `0A13` MANAGE_ALL_POPULATION
Deletes distant, no longer needed, objects and world dummy objects

**Class:** `Game.ManageAllPopulation`
**Flags:** static

---

### `0A14` SET_NO_RESPRAYS
Disables respray garages from opening for the player

**Class:** `Game.SetNoResprays`
**Flags:** static

**Input:**
- `state: bool`

---

### `0A2B` IS_WIDESCREEN_ON_IN_OPTIONS
Returns true if widescreen is switched on in the display settings

**Class:** `Game.IsWidescreenOnInOptions`
**Flags:** condition, static

---

### `0A37` FORCE_ALL_VEHICLE_LIGHTS_OFF
Disables all vehicle lights from being rendered if enabled

**Class:** `Game.ForceAllVehicleLightsOff`
**Flags:** static

**Input:**
- `state: bool`

---

### `0A3D` ACTIVATE_PIMP_CHEAT
Sets whether sleeping with a prostitute earns you money instead of taking it away from you

**Class:** `Game.ActivatePimpCheat`
**Flags:** static

**Input:**
- `state: bool`

---

### `0A3F` SET_SCRIPT_COOP_GAME
Sets an unused flag at address 0x96A8A8

**Class:** `Game.SetScriptCoopGame`
**Flags:** static

**Input:**
- `state: bool`

---

### `0A43` GET_RID_OF_PLAYER_PROSTITUTE
Cancels any prostitute invitations received in-game and makes any current prostitutes quit

**Class:** `Game.GetRidOfPlayerProstitute`
**Flags:** static

---

### `0A46` SWITCH_OBJECT_BRAINS
Enables or disables all object triggers with the specified grouping id (set with 0929)

**Class:** `Game.SwitchObjectBrains`
**Flags:** static

**Input:**
- `groupingId: int`
- `state: bool`

**Details:**

This command can be used to temporarily disable AI brains created with ALLOCATE_STREAMED_SCRIPT_TO_OBJECT. It was used in the original game during the mission "Breaking the Bank at Caligula's".

**Overview of Brain Types**

San Andreas has multiple types of AI brains that can be assigned to pedestrians or objects to control their behavior.

| Type                       | Trigger                              | Purpose                                    | Related Command                              |
| -------------------------- | ------------------------------------ | ------------------------------------------ | -------------------------------------------- |
| PED_STREAMED (0)           | Ped with matching model created      | Auto-run ped behavior scripts              | ALLOCATE_STREAMED_SCRIPT_TO_RANDOM_PED       |
| OBJECT_STREAMED (1)        | Object with matching model created   | Auto-run object scripts                    | ALLOCATE_STREAMED_SCRIPT_TO_OBJECT           |
| PED_GENERATOR_STREAMED (2) | —                                    | Disabled debug leftover                    | —                                            |
| CODE_PED (3)               | Game code calls brain by string name | Interior / special AI behaviors            | REGISTER_SCRIPT_BRAIN_FOR_CODE_USE           |
| CODE_OBJECT (4)            | Unused                               | —                                          | REGISTER_OBJECT_SCRIPT_BRAIN_FOR_CODE_USE    |
| CODE_ATTRACTOR_PED (5)     | Ped uses map attractor               | Attractor behaviors (chairs, gym, dancing) | REGISTER_ATTRACTOR_SCRIPT_BRAIN_FOR_CODE_USE |

---

### `0A48` ALLOW_PAUSE_IN_WIDESCREEN
Enables the player to access the pause menu while widescreen is enabled

**Class:** `Game.AllowPauseInWidescreen`
**Flags:** static

**Input:**
- `state: bool`

---

### `0A4B` IS_PC_USING_JOYPAD
Returns true if players controls are set to joystick and not mouse+keyboard

**Class:** `Game.IsPcUsingJoypad`
**Flags:** condition, static

---
