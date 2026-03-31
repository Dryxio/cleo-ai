# Char Opcodes

> 252 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `009A` | CREATE_CHAR | Creates a character at the specified location, with the specified model and pedt |
| `009B` | DELETE_CHAR | Removes the character from the game and mission cleanup list, freeing game memor |
| `00A0` | GET_CHAR_COORDINATES | Returns the character's coordinates |
| `00A1` | SET_CHAR_COORDINATES | Puts the character at the specified location |
| `00A3` | IS_CHAR_IN_AREA_2D | Returns true if the character is within the specified 2D area |
| `00A4` | IS_CHAR_IN_AREA_3D | Returns true if the character is within the specified 3D area |
| `00D9` | STORE_CAR_CHAR_IS_IN | Returns the current vehicle of the character and adds it to the mission cleanup  |
| `00DB` | IS_CHAR_IN_CAR | Returns true if the character is in the specified vehicle |
| `00DD` | IS_CHAR_IN_MODEL | Returns true if the character is driving a vehicle with the specified model |
| `00DF` | IS_CHAR_IN_ANY_CAR | Returns true if the character has a vehicle, even if they are not actually sat i |
| `00EC` | LOCATE_CHAR_ANY_MEANS_2D | Returns true if the character is within the 2D radius of the coordinates point |
| `00ED` | LOCATE_CHAR_ON_FOOT_2D | Returns true if the character is within the 2D radius of the coordinates point o |
| `00EE` | LOCATE_CHAR_IN_CAR_2D | Returns true if the character is within the 2D radius of the coordinates point i |
| `00EF` | LOCATE_STOPPED_CHAR_ANY_MEANS_2D | Returns true if the character stopped within the 2D radius of the coordinates po |
| `00F0` | LOCATE_STOPPED_CHAR_ON_FOOT_2D | Returns true if the character stopped within the 2D radius of the coordinates po |
| `00F1` | LOCATE_STOPPED_CHAR_IN_CAR_2D | Returns true if the character stopped within the 2D radius of the coordinates po |
| `00F2` | LOCATE_CHAR_ANY_MEANS_CHAR_2D | Returns true if the character is within the 2D radius of the other character |
| `00F3` | LOCATE_CHAR_ON_FOOT_CHAR_2D | Returns true if the character is within the 2D radius of the other character on  |
| `00F4` | LOCATE_CHAR_IN_CAR_CHAR_2D | Returns true if the character is within the 2D radius of the other character in  |
| `00FE` | LOCATE_CHAR_ANY_MEANS_3D | Returns true if the character is within the 3D radius of the coordinates point |
| `00FF` | LOCATE_CHAR_ON_FOOT_3D | Returns true if the character is within the 3D radius of the coordinates point o |
| `0100` | LOCATE_CHAR_IN_CAR_3D | Returns true if the character is within the 3D radius of the coordinates point i |
| `0101` | LOCATE_STOPPED_CHAR_ANY_MEANS_3D | Returns true if the character stopped within the 3D radius of the coordinates po |
| `0102` | LOCATE_STOPPED_CHAR_ON_FOOT_3D | Returns true if the character stopped within the 3D radius of the coordinates po |
| `0103` | LOCATE_STOPPED_CHAR_IN_CAR_3D | Returns true if the character stopped within the 3D radius of the coordinates po |
| `0104` | LOCATE_CHAR_ANY_MEANS_CHAR_3D | Returns true if the character is within the 3D radius of the other character |
| `0105` | LOCATE_CHAR_ON_FOOT_CHAR_3D | Returns true if the character is within the 3D radius of the other character on  |
| `0106` | LOCATE_CHAR_IN_CAR_CHAR_3D | Returns true if the character is within the 3D radius of the other character in  |
| `0114` | ADD_AMMO_TO_CHAR | Adds the specified amount of ammo to the character's weapon, if the character ha |
| `0118` | IS_CHAR_DEAD | Returns true if the handle is an invalid character handle or the character is de |
| `0129` | CREATE_CHAR_INSIDE_CAR | Creates a character in the driver's seat of the vehicle |
| `0154` | IS_CHAR_IN_ZONE | Returns true if the character is in the specified map zone |
| `0172` | GET_CHAR_HEADING | Returns the character's heading (z-angle) |
| `0173` | SET_CHAR_HEADING | Sets the character's heading (z-angle) |
| `0179` | IS_CHAR_TOUCHING_OBJECT | Returns true if the character is colliding with the specified object |
| `017B` | SET_CHAR_AMMO | Sets the amount of ammo the character has in the specified weapon |
| `0184` | IS_CHAR_HEALTH_GREATER | Returns true if the character's health is over the specified value |
| `01A1` | IS_CHAR_IN_AREA_ON_FOOT_2D | Returns true if the character is within the specified 2D area on foot |
| `01A2` | IS_CHAR_IN_AREA_IN_CAR_2D | Returns true if the character is within the specified 2D area in a vehicle |
| `01A3` | IS_CHAR_STOPPED_IN_AREA_2D | Returns true if the character stopped within the specified 2D area |
| `01A4` | IS_CHAR_STOPPED_IN_AREA_ON_FOOT_2D | Returns true if the character stopped within the specified 2D area on foot |
| `01A5` | IS_CHAR_STOPPED_IN_AREA_IN_CAR_2D | Returns true if the character stopped within the specified 2D area in a vehicle |
| `01A6` | IS_CHAR_IN_AREA_ON_FOOT_3D | Returns true if the character is within the specified 3D area on foot |
| `01A7` | IS_CHAR_IN_AREA_IN_CAR_3D | Returns true if the character is within the specified 3D area in a vehicle |
| `01A8` | IS_CHAR_STOPPED_IN_AREA_3D | Returns true if the character stopped within the specified 3D area |
| `01A9` | IS_CHAR_STOPPED_IN_AREA_ON_FOOT_3D | Returns true if the character stopped within the specified 3D area on foot |
| `01AA` | IS_CHAR_STOPPED_IN_AREA_IN_CAR_3D | Returns true if the character stopped within the specified 3D area in a vehicle |
| `01B2` | GIVE_WEAPON_TO_CHAR | Gives the character the weapon with the specified amount of ammo |
| `01B9` | SET_CURRENT_CHAR_WEAPON | Sets the character's currently held weapon |
| `01C2` | MARK_CHAR_AS_NO_LONGER_NEEDED | Allows the character to be deleted by the game if necessary, and also removes th |
| `01C5` | DONT_REMOVE_CHAR | Removes the character from the mission cleanup list, preventing it from being de |
| `01C8` | CREATE_CHAR_AS_PASSENGER | Creates a character with the specified model in the passenger seat of the vehicl |
| `0202` | LOCATE_CHAR_ANY_MEANS_CAR_2D | Returns true if the character is within the 2D radius of the vehicle |
| `0203` | LOCATE_CHAR_ON_FOOT_CAR_2D | Returns true if the character is within the 2D radius of the vehicle on foot |
| `0204` | LOCATE_CHAR_IN_CAR_CAR_2D | Returns true if the character is within the 2D radius of the vehicle in a vehicl |
| `0205` | LOCATE_CHAR_ANY_MEANS_CAR_3D | Returns true if the character is within the 3D radius of the vehicle |
| `0206` | LOCATE_CHAR_ON_FOOT_CAR_3D | Returns true if the character is within the 3D radius of the vehicle on foot |
| `0207` | LOCATE_CHAR_IN_CAR_CAR_3D | Returns true if the character is within the 3D radius of the vehicle in a vehicl |
| `0223` | SET_CHAR_HEALTH | Sets the character's health |
| `0226` | GET_CHAR_HEALTH | Returns the character's health |
| `023B` | IS_CHAR_TOUCHING_OBJECT_ON_FOOT | Returns true if the character is colliding with the specified object on foot |
| `0245` | SET_ANIM_GROUP_FOR_CHAR | Sets the animation group for the character |
| `02A0` | IS_CHAR_STOPPED | Returns true if the character is not moving |
| `02A9` | SET_CHAR_ONLY_DAMAGED_BY_PLAYER | Makes a character immune to everything except the player |
| `02AB` | SET_CHAR_PROOFS | Sets the character's immunities |
| `02CB` | IS_CHAR_ON_SCREEN | Returns true if the character is visible |
| `02D6` | IS_CHAR_SHOOTING_IN_AREA | Returns true if the character fired a weapon within the specified 2D area |
| `02D8` | IS_CURRENT_CHAR_WEAPON | Returns true if the character is holding the given type of weapon |
| `02E0` | IS_CHAR_SHOOTING | Returns true if the character is firing a weapon |
| `02E2` | SET_CHAR_ACCURACY | Affects how often the character will hit the target when attacking with a weapon |
| `02F2` | IS_CHAR_MODEL | Returns true if the character's model ID is equivalent to the model ID passed |
| `031D` | HAS_CHAR_BEEN_DAMAGED_BY_WEAPON | Returns true if the character has been hit by the specified weapon |
| `0321` | EXPLODE_CHAR_HEAD | Dismembers the character |
| `0332` | SET_CHAR_BLEEDING | Makes a character bleed |
| `0337` | SET_CHAR_VISIBLE | Sets whether the character is visible or not |
| `034F` | REMOVE_CHAR_ELEGANTLY | Removes the character with a fade, freeing game memory |
| `0350` | SET_CHAR_STAY_IN_SAME_PLACE | Makes the character maintain their position when attacked |
| `035F` | ADD_ARMOUR_TO_CHAR | Increases the character's armor by the specified value to the maximum of 100 |
| `0362` | WARP_CHAR_FROM_CAR_TO_COORD | Pulls the character out of their car and places at the location |
| `0364` | HAS_CHAR_SPOTTED_CHAR | Returns true if the character can see the target character |
| `036A` | WARP_CHAR_INTO_CAR | Puts the character in the specified vehicle |
| `0376` | CREATE_RANDOM_CHAR | Creates a character with a randomised model and pedtype at the specified coordin |
| `0393` | SET_CHAR_ANIM_SPEED | Makes an char perform an animation at the specified speed |
| `039E` | SET_CHAR_CANT_BE_DRAGGED_OUT | Locks the character while in a car |
| `03A3` | IS_CHAR_MALE | Returns true if the character is male |
| `03C0` | STORE_CAR_CHAR_IS_IN_NO_SAVE | Returns the character's vehicle handle without marking it as used by the script, |
| `03FE` | SET_CHAR_MONEY | Sets the character's cash sum, setting how much cash they will drop when dead |
| `041A` | GET_AMMO_IN_CHAR_WEAPON | Gets the amount of ammo in the specified weapon of the character |
| `0430` | WARP_CHAR_INTO_CAR_AS_PASSENGER | Puts the character into a vehicle's passenger seat |
| `0433` | SET_CHAR_IS_CHRIS_CRIMINAL | Sets whether the character is a psychotic killer or not |
| `0446` | SET_CHAR_SUFFERS_CRITICAL_HITS | Sets whether the specified character is immune to headshots |
| `0448` | IS_CHAR_SITTING_IN_CAR | Returns true if the character is sitting in the specified vehicle |
| `0449` | IS_CHAR_SITTING_IN_ANY_CAR | Returns true if the character is sitting in any vehicle |
| `044B` | IS_CHAR_ON_FOOT | Returns true if the character is on foot, and not occupying a vehicle |
| `0464` | ATTACH_CHAR_TO_CAR | Puts character into a turret on the vehicle, allowing them to shoot |
| `0465` | DETACH_CHAR_FROM_CAR | Takes the character out of turret mode (0464) |
| `0467` | CLEAR_CHAR_LAST_WEAPON_DAMAGE | Clears the character's last weapon damage (see 031D) |
| `046D` | GET_NUMBER_OF_FOLLOWERS | Returns the number of members which are in a group of the character (01DE) |
| `0470` | GET_CURRENT_CHAR_WEAPON | Returns the type of weapon that the character is currently holding |
| `0471` | LOCATE_CHAR_ANY_MEANS_OBJECT_2D | Returns true if the character is within the 2D radius of the object |
| `0472` | LOCATE_CHAR_ON_FOOT_OBJECT_2D | Returns true if the character is within the 2D radius of the object on foot |
| `0473` | LOCATE_CHAR_IN_CAR_OBJECT_2D | Returns true if the character is within the 2D radius of the object in a vehicle |
| `0474` | LOCATE_CHAR_ANY_MEANS_OBJECT_3D | Returns true if the character is within the 3D radius of the object |
| `0475` | LOCATE_CHAR_ON_FOOT_OBJECT_3D | Returns true if the character is within the 3D radius of the object on foot |
| `0476` | LOCATE_CHAR_IN_CAR_OBJECT_3D | Returns true if the character is within the 3D radius of the object in a vehicle |
| `047A` | IS_CHAR_ON_ANY_BIKE | Returns true if the character is riding a bike |
| `0480` | CAN_CHAR_SEE_DEAD_CHAR | Returns true if the character sees a dead body of the given type |
| `0489` | SHUT_CHAR_UP | Sets the character's ability to talk |
| `048F` | REMOVE_ALL_CHAR_WEAPONS | Removes the characters weapons |
| `0491` | HAS_CHAR_GOT_WEAPON | Returns true if the character has the specified weapon |
| `04A7` | IS_CHAR_IN_ANY_BOAT | Returns true if the character is driving a boat |
| `04A9` | IS_CHAR_IN_ANY_HELI | Returns true if the character is flying a helicopter |
| `04AB` | IS_CHAR_IN_ANY_PLANE | Returns true if the character is in a plane |
| `04AD` | IS_CHAR_IN_WATER | Returns true if the character is in water |
| `04B8` | GET_CHAR_WEAPON_IN_SLOT | Returns the weapon type, ammo and model from the specified slot |
| `04C4` | GET_OFFSET_FROM_CHAR_IN_WORLD_COORDS | Returns the coordinates of the character, with an offset |
| `04C5` | HAS_CHAR_BEEN_PHOTOGRAPHED | Returns true if the character has been photographed |
| `04C8` | IS_CHAR_IN_FLYING_VEHICLE | Returns true if the character is in a flying vehicle |
| `04D7` | FREEZE_CHAR_POSITION | Sets whether the character's position remains unchanged |
| `04D8` | SET_CHAR_DROWNS_IN_WATER | Controls whether the character can drown in water |
| `04DD` | GET_CHAR_ARMOUR | Returns the character's armor amount |
| `04F0` | IS_CHAR_WAITING_FOR_WORLD_COLLISION |  |
| `04F4` | ATTACH_CHAR_TO_OBJECT | Attaches the character to the specified object, in turret mode |
| `0503` | CREATE_SWAT_ROPE | Creates a character descending from a rope |
| `051A` | HAS_CHAR_BEEN_DAMAGED_BY_CHAR | Returns true if the character has been hurt by the other character |
| `051B` | HAS_CHAR_BEEN_DAMAGED_BY_CAR | Returns true if the char has been hurt by the specified vehicle |
| `0526` | SET_CHAR_STAY_IN_CAR_WHEN_JACKED | Makes the character stay in the vehicle when it is jacked (characters let themse |
| `0547` | IS_CHAR_TOUCHING_VEHICLE | Returns true if the character is colliding with a car |
| `054A` | SET_CHAR_CAN_BE_SHOT_IN_VEHICLE | Makes the character immune to a damage while in a vehicle |
| `054E` | CLEAR_CHAR_LAST_DAMAGE_ENTITY |  |
| `0555` | REMOVE_WEAPON_FROM_CHAR | Removes the weapon from the character |
| `0560` | CREATE_RANDOM_CHAR_AS_DRIVER | Creates a driver in the vehicle |
| `0561` | CREATE_RANDOM_CHAR_AS_PASSENGER | Creates a random character in the passenger seat of the vehicle |
| `0568` | SET_CHAR_NEVER_TARGETTED | Sets whether the character won't be targeted by the autoaim system |
| `056C` | IS_CHAR_IN_ANY_POLICE_VEHICLE | Returns true if the character is driving a police vehicle |
| `056D` | DOES_CHAR_EXIST | Returns true if the handle is a valid character handle |
| `0575` | FREEZE_CHAR_POSITION_AND_DONT_LOAD_COLLISION |  |
| `0588` | SET_LOAD_COLLISION_FOR_CHAR_FLAG |  |
| `0597` | IS_CHAR_DUCKING | Returns true if the specified character is crouching |
| `05F6` | IS_CHAR_IN_ANGLED_AREA_2D | Checks if the character is within the angled 2D area |
| `05F7` | IS_CHAR_IN_ANGLED_AREA_ON_FOOT_2D | Checks if the character is within the angled 2D area |
| `05F8` | IS_CHAR_IN_ANGLED_AREA_IN_CAR_2D | Checks if the character is in a car which is within the angled 2D area |
| `05F9` | IS_CHAR_STOPPED_IN_ANGLED_AREA_2D | Checks if the character is within the angled 2D area and is motionless |
| `05FA` | IS_CHAR_STOPPED_IN_ANGLED_AREA_ON_FOOT_2D | Checks if the character is within the angled 2D area |
| `05FB` | IS_CHAR_STOPPED_IN_ANGLED_AREA_IN_CAR_2D | Checks if the character is in a motionless car within the angled 2D area |
| `05FC` | IS_CHAR_IN_ANGLED_AREA_3D | Checks if the character is within the angled 3D area |
| `05FD` | IS_CHAR_IN_ANGLED_AREA_ON_FOOT_3D | Checks if the character is within the angled 3D area |
| `05FE` | IS_CHAR_IN_ANGLED_AREA_IN_CAR_3D | Checks if the character is in a car which is within the angled 3D area |
| `05FF` | IS_CHAR_STOPPED_IN_ANGLED_AREA_3D | Checks if the character is within the angled 3D area and is motionless |
| `0600` | IS_CHAR_STOPPED_IN_ANGLED_AREA_ON_FOOT_3D | Checks if the character is on foot within the angled 3D area and is motionless |
| `0601` | IS_CHAR_STOPPED_IN_ANGLED_AREA_IN_CAR_3D | Checks if the character is in a motionless car within the angled 3D area |
| `0602` | IS_CHAR_IN_TAXI | Returns true if the character is driving a taxi |
| `060B` | SET_CHAR_DECISION_MAKER | Sets the decision maker for the character |
| `060F` | SET_SENSE_RANGE | Sets the seeing and hearing range for the specified character or for all mission |
| `0611` | IS_CHAR_PLAYING_ANIM | Returns true if character is performing the specified animation |
| `0612` | SET_CHAR_ANIM_PLAYING_FLAG | Sets whether the animation is playing |
| `0613` | GET_CHAR_ANIM_CURRENT_TIME | Returns the progress of the animation on the char, ranging from 0.0 to 1.0 |
| `0614` | SET_CHAR_ANIM_CURRENT_TIME | Sets how far through the animation the character is, with 1 |
| `0618` | PERFORM_SEQUENCE_TASK | Assigns the character to the specified action sequence |
| `0619` | SET_CHAR_COLLISION | Sets whether collision detection is enabled for the character |
| `061A` | GET_CHAR_ANIM_TOTAL_TIME | Returns a float of the length of the animation in milliseconds |
| `0621` | CREATE_CHAR_AT_ATTRACTOR |  |
| `062E` | GET_SCRIPT_TASK_STATUS | Returns the status of the specified script task of the character |
| `0642` | IS_CHAR_AT_SCRIPTED_ATTRACTOR |  |
| `0646` | GET_SEQUENCE_PROGRESS | Gets the characters task sequence progress, as started by 0618 |
| `0647` | CLEAR_LOOK_AT | Clears the char's look task, making them stop looking at whatever they were assi |
| `0648` | SET_FOLLOW_NODE_THRESHOLD_DISTANCE | Sets the range within which the char responds to events |
| `0665` | GET_CHAR_MODEL | Returns the characters model |
| `0687` | CLEAR_CHAR_TASKS | Clears the char's task, making them quit whatever they were doing |
| `06A7` | ATTACH_CHAR_TO_BIKE |  |
| `06AB` | HIDE_CHAR_WEAPON_FOR_SCRIPTED_CUTSCENE | Hides all of the specified char's weapons |
| `06AC` | GET_CHAR_SPEED | Returns the char's movement speed |
| `06C9` | REMOVE_CHAR_FROM_GROUP | Removes the character from their current group |
| `06EE` | IS_GROUP_MEMBER | Returns true if the character is a member of the specified group |
| `06EF` | IS_GROUP_LEADER | Returns true if the character is the leader of the specified group |
| `06FF` | ARE_ANY_CHARS_NEAR_CHAR | Returns true if any characters are within range of the character |
| `070B` | DROP_OBJECT |  |
| `0737` | IS_CHAR_HOLDING_OBJECT | Returns true if the char is lifting the specified object |
| `0741` | HAS_CHAR_BEEN_ARRESTED | Returns true if the character has been arrested |
| `074E` | SET_INFORM_RESPECTED_FRIENDS |  |
| `074F` | IS_CHAR_RESPONDING_TO_EVENT | Returns true if the character is responding to the specified ped event |
| `0770` | SET_CHAR_IS_TARGET_PRIORITY | Causes the auto aim to be more likely to target the specified char than actors w |
| `077A` | SET_CHAR_RELATIONSHIP |  |
| `077B` | CLEAR_CHAR_RELATIONSHIP |  |
| `077C` | CLEAR_ALL_CHAR_RELATIONSHIPS |  |
| `0792` | CLEAR_CHAR_TASKS_IMMEDIATELY | Clears all the characters tasks immediately, resetting the character to an idle  |
| `07A0` | PERFORM_SEQUENCE_TASK_FROM_PROGRESS |  |
| `07A1` | SET_NEXT_DESIRED_MOVE_STATE | Sets how the character chooses to go to their destination in the next task witho |
| `07A4` | GET_SEQUENCE_PROGRESS_RECURSIVE |  |
| `07A9` | IS_CHAR_IN_ANY_SEARCHLIGHT | Returns the handle for the searchlight that's targeting the character |
| `07CB` | LISTEN_TO_PLAYER_GROUP_COMMANDS |  |
| `07DD` | SET_CHAR_SHOOT_RATE | Sets the attack rate of the char |
| `07FE` | GIVE_MELEE_ATTACK_TO_CHAR | Sets the specified characters fighting style and moves |
| `080E` | GET_CHAR_HIGHEST_PRIORITY_EVENT | Gets the characters active ped event |
| `0811` | GET_CAR_CHAR_IS_USING | Stores a handle for the vehicle the character is in or entering (alts: 00D9,03C0 |
| `0816` | SET_CHAR_KINDA_STAY_IN_SAME_PLACE | Sets whether the character shouldn't chase their victim far (to attempt a melee  |
| `0818` | IS_CHAR_IN_AIR | Returns true if the character is in the air |
| `0819` | GET_CHAR_HEIGHT_ABOVE_GROUND | Returns the char's distance from ground |
| `081A` | SET_CHAR_WEAPON_SKILL | Sets the character's fire arms wielding style |
| `083C` | SET_CHAR_VELOCITY | Sets the characters velocity |
| `083D` | GET_CHAR_VELOCITY | Gets the characters velocity |
| `083E` | SET_CHAR_ROTATION | Sets the characters rotation |
| `0851` | DAMAGE_CHAR | Decreases the characters health |
| `0856` | SET_CHAR_ALLOWED_TO_DUCK | Sets whether the character can crouch |
| `0860` | SET_CHAR_AREA_VISIBLE | Sets the interior that the char is in |
| `087E` | SET_CHAR_DROPS_WEAPONS_WHEN_DEAD | Sets whether the character will drop any of their weapons when they die |
| `087F` | SET_CHAR_NEVER_LEAVES_GROUP | Prevents the character from leaving their group |
| `0887` | SET_HEADING_LIMIT_FOR_ATTACHED_CHAR | Sets the heading limit for a character attached to an object or vehicle |
| `0889` | GET_DEAD_CHAR_COORDINATES |  |
| `089F` | GET_PED_TYPE | Gets the ped type of the character |
| `08AD` | SET_CHAR_HAS_USED_ENTRY_EXIT | Locates the entry/exit marker in the specified radius of the specified coordinat |
| `08AF` | SET_CHAR_MAX_HEALTH | Sets the characters max health |
| `08C6` | SET_CHAR_CAN_BE_KNOCKED_OFF_BIKE | Sets whether the character always stays on bike in collisions |
| `08C7` | SET_CHAR_COORDINATES_DONT_WARP_GANG | Sets the character's coordinates without warping the rest of their group |
| `093B` | SET_CHAR_BULLETPROOF_VEST | Specifies that the character should only use upper-body damage animations, meani |
| `0946` | SET_CHAR_USES_UPPERBODY_DAMAGE_ANIMS_ONLY |  |
| `0947` | SET_CHAR_SAY_CONTEXT | Works similar to 05C1, but returns which phrase was spoken and is not run as a t |
| `094B` | GET_NAME_OF_ENTRY_EXIT_CHAR_USED | Gets the name of the characters interior |
| `094C` | GET_POSITION_OF_ENTRY_EXIT_CHAR_USED | Returns the coordinates and heading of the entry (enex) marker the character use |
| `094D` | IS_CHAR_TALKING | Returns true if the character is playing any speech |
| `094E` | DISABLE_CHAR_SPEECH | Prevents any character speech from playing |
| `094F` | ENABLE_CHAR_SPEECH | Enables pain audio if it was disabled using 094E |
| `095D` | IS_CHAR_STUCK_UNDER_CAR | Returns true if the char is stuck under a car |
| `0961` | SET_CHAR_KEEP_TASK | Sets whether the character should keep their tasks after mission cleanup (basica |
| `0965` | IS_CHAR_SWIMMING |  |
| `0966` | GET_CHAR_SWIM_STATE |  |
| `0967` | START_CHAR_FACIAL_TALK | Makes a character move their mouth as if they were talking |
| `0968` | STOP_CHAR_FACIAL_TALK | Stops the character moving their mouth as if they were talking |
| `0972` | SET_CHAR_COORDINATES_NO_OFFSET | Puts the characters at the coordinates by the center of body instead of the feet |
| `0982` | SET_CHAR_FORCE_DIE_IN_CAR | Makes a character remain in the car upon death |
| `09A1` | DROP_SECOND_OBJECT |  |
| `09A7` | SET_CHAR_DRUGGED_UP |  |
| `09A8` | IS_CHAR_HEAD_MISSING | Returns true if the character has had its head shot off |
| `09AE` | IS_CHAR_IN_ANY_TRAIN | Returns true if the specified character is in a train |
| `09B5` | SET_CHAR_SIGNAL_AFTER_KILL | Sets whether the character signals after killing |
| `09B6` | SET_CHAR_WANTED_BY_POLICE | Sets whether police should chase the character |
| `09BC` | SET_CHAR_COORDINATES_DONT_WARP_GANG_NO_OFFSET | This command is a combination of 0972 and 08C7 |
| `09C5` | IS_CHAR_USING_MAP_ATTRACTOR | Returns true if the character is using a map attractor |
| `09C9` | REMOVE_CHAR_FROM_CAR_MAINTAIN_POSITION | Removes the character from the vehicle |
| `09D5` | SET_CHAR_SAY_CONTEXT_IMPORTANT |  |
| `09D6` | SET_CHAR_SAY_SCRIPT |  |
| `09DE` | IS_CHAR_GETTING_IN_TO_A_CAR | Returns true if the character is entering a car, but is not in the car |
| `09E8` | GET_CHAR_AREA_VISIBLE | Returns the interior ID that the character is in |
| `09ED` | HAS_CHAR_SPOTTED_CHAR_IN_FRONT | Returns true if the character can see the other character in front of them |
| `09F4` | IGNORE_HEIGHT_DIFFERENCE_FOLLOWING_NODES |  |
| `09F6` | SET_CHAR_GET_OUT_UPSIDE_DOWN_CAR | Controls whether the character will try to exit an upside-down car until it is o |
| `0A09` | SHUT_CHAR_UP_FOR_SCRIPTED_SPEECH | Works similar to 0489, but mutes more things, including ambient speeches (needs  |
| `0A1B` | IS_CHAR_TOUCHING_CHAR | Returns true if the character is touching the other character |
| `0A27` | SET_DEATH_WEAPONS_PERSIST | Prevents pickups, which are created when this character dies, from disappearing  |
| `0A28` | SET_SWIM_SPEED | Sets the speed that the character swims at, changing their swimming animation sp |
| `0A32` | IS_CHAR_ATTACHED_TO_ANY_CAR | Returns true if the char is turreted on any vehicle |
| `0A33` | STORE_CAR_CHAR_IS_ATTACHED_TO_NO_SAVE | Returns the vehicle the character is attached to |

## Detailed Reference

### `009A` CREATE_CHAR
Creates a character at the specified location, with the specified model and pedtype

**Class:** `Char.Create`
**Flags:** constructor

**Input:**
- `pedType: PedType`
- `modelId: model_char`
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `handle: Char (variable)`

---

### `009B` DELETE_CHAR
Removes the character from the game and mission cleanup list, freeing game memory

**Class:** `Char.Delete`
**Flags:** destructor

**Input:**
- `self: Char`

---

### `00A0` GET_CHAR_COORDINATES
Returns the character's coordinates

**Class:** `Char.GetCoordinates`

**Input:**
- `self: Char`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `00A1` SET_CHAR_COORDINATES
Puts the character at the specified location

**Class:** `Char.SetCoordinates`

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `z: float`

**Details:**

This command teleports the character at the given location. Before doing that it checks whether the char is driving a vehicle and, if yes, it teleports the vehicle.

If the char is a leader of a group on foot, it also teleports the group (not tested). 

Additionally it: 
- automatically calculates the ground position if the Z-coord was set to `-100.0` 
- interrupts any active task
- respawns the character or the vehicle (removes and creates a new entity in the game)
- resets any speed

---

### `00A3` IS_CHAR_IN_AREA_2D
Returns true if the character is within the specified 2D area

**Class:** `Char.IsInArea2D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `drawSphere: bool`

---

### `00A4` IS_CHAR_IN_AREA_3D
Returns true if the character is within the specified 3D area

**Class:** `Char.IsInArea3D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `drawSphere: bool`

---

### `00D9` STORE_CAR_CHAR_IS_IN
Returns the current vehicle of the character and adds it to the mission cleanup list (alts:03C0,0811,0484)

**Class:** `Char.StoreCarIsIn`

**Input:**
- `self: Char`

**Output:**
- `handle: Car (variable)`

---

### `00DB` IS_CHAR_IN_CAR
Returns true if the character is in the specified vehicle

**Class:** `Char.IsInCar`
**Flags:** condition

**Input:**
- `self: Char`
- `vehicle: Car`

---

### `00DD` IS_CHAR_IN_MODEL
Returns true if the character is driving a vehicle with the specified model

**Class:** `Char.IsInModel`
**Flags:** condition

**Input:**
- `self: Char`
- `modelId: model_vehicle`

---

### `00DF` IS_CHAR_IN_ANY_CAR
Returns true if the character has a vehicle, even if they are not actually sat inside it (opening and closing the door)

**Class:** `Char.IsInAnyCar`
**Flags:** condition

**Input:**
- `self: Char`

---

### `00EC` LOCATE_CHAR_ANY_MEANS_2D
Returns true if the character is within the 2D radius of the coordinates point

**Class:** `Char.LocateAnyMeans2D`
**Flags:** condition

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `xRadius: float`
- `yRadius: float`
- `drawSphere: bool`

---

### `00ED` LOCATE_CHAR_ON_FOOT_2D
Returns true if the character is within the 2D radius of the coordinates point on foot

**Class:** `Char.LocateOnFoot2D`
**Flags:** condition

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `xRadius: float`
- `yRadius: float`
- `drawSphere: bool`

---

### `00EE` LOCATE_CHAR_IN_CAR_2D
Returns true if the character is within the 2D radius of the coordinates point in a vehicle

**Class:** `Char.LocateInCar2D`
**Flags:** condition

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `xRadius: float`
- `yRadius: float`
- `drawSphere: bool`

---

### `00EF` LOCATE_STOPPED_CHAR_ANY_MEANS_2D
Returns true if the character stopped within the 2D radius of the coordinates point

**Class:** `Char.LocateStoppedAnyMeans2D`
**Flags:** condition

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `xRadius: float`
- `yRadius: float`
- `drawSphere: bool`

---

### `00F0` LOCATE_STOPPED_CHAR_ON_FOOT_2D
Returns true if the character stopped within the 2D radius of the coordinates point on foot

**Class:** `Char.LocateStoppedOnFoot2D`
**Flags:** condition

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `xRadius: float`
- `yRadius: float`
- `drawSphere: bool`

---

### `00F1` LOCATE_STOPPED_CHAR_IN_CAR_2D
Returns true if the character stopped within the 2D radius of the coordinates point in a vehicle

**Class:** `Char.LocateStoppedInCar2D`
**Flags:** condition

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `xRadius: float`
- `yRadius: float`
- `drawSphere: bool`

---

### `00F2` LOCATE_CHAR_ANY_MEANS_CHAR_2D
Returns true if the character is within the 2D radius of the other character

**Class:** `Char.LocateAnyMeansChar2D`
**Flags:** condition

**Input:**
- `self: Char`
- `target: Char`
- `xRadius: float`
- `yRadius: float`
- `drawSphere: bool`

---

### `00F3` LOCATE_CHAR_ON_FOOT_CHAR_2D
Returns true if the character is within the 2D radius of the other character on foot

**Class:** `Char.LocateOnFootChar2D`
**Flags:** condition

**Input:**
- `self: Char`
- `target: Char`
- `xRadius: float`
- `yRadius: float`
- `drawSphere: bool`

---

### `00F4` LOCATE_CHAR_IN_CAR_CHAR_2D
Returns true if the character is within the 2D radius of the other character in a vehicle

**Class:** `Char.LocateInCarChar2D`
**Flags:** condition

**Input:**
- `self: Char`
- `otherChar: Char`
- `xRadius: float`
- `yRadius: float`
- `drawSphere: bool`

---

### `00FE` LOCATE_CHAR_ANY_MEANS_3D
Returns true if the character is within the 3D radius of the coordinates point

**Class:** `Char.LocateAnyMeans3D`
**Flags:** condition

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `z: float`
- `xRadius: float`
- `yRadius: float`
- `zRadius: float`
- `drawSphere: bool`

---

### `00FF` LOCATE_CHAR_ON_FOOT_3D
Returns true if the character is within the 3D radius of the coordinates point on foot

**Class:** `Char.LocateOnFoot3D`
**Flags:** condition

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `z: float`
- `xRadius: float`
- `yRadius: float`
- `zRadius: float`
- `drawSphere: bool`

---

### `0100` LOCATE_CHAR_IN_CAR_3D
Returns true if the character is within the 3D radius of the coordinates point in a vehicle

**Class:** `Char.LocateInCar3D`
**Flags:** condition

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `z: float`
- `xRadius: float`
- `yRadius: float`
- `zRadius: float`
- `drawSphere: bool`

---

### `0101` LOCATE_STOPPED_CHAR_ANY_MEANS_3D
Returns true if the character stopped within the 3D radius of the coordinates point

**Class:** `Char.LocateStoppedAnyMeans3D`
**Flags:** condition

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `z: float`
- `xRadius: float`
- `yRadius: float`
- `zRadius: float`
- `drawSphere: bool`

---

### `0102` LOCATE_STOPPED_CHAR_ON_FOOT_3D
Returns true if the character stopped within the 3D radius of the coordinates point on foot

**Class:** `Char.LocateStoppedOnFoot3D`
**Flags:** condition

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `z: float`
- `xRadius: float`
- `yRadius: float`
- `zRadius: float`
- `drawSphere: bool`

---

### `0103` LOCATE_STOPPED_CHAR_IN_CAR_3D
Returns true if the character stopped within the 3D radius of the coordinates point in a vehicle

**Class:** `Char.LocateStoppedInCar3D`
**Flags:** condition

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `z: float`
- `xRadius: float`
- `yRadius: float`
- `zRadius: float`
- `drawSphere: bool`

---

### `0104` LOCATE_CHAR_ANY_MEANS_CHAR_3D
Returns true if the character is within the 3D radius of the other character

**Class:** `Char.LocateAnyMeansChar3D`
**Flags:** condition

**Input:**
- `self: Char`
- `target: Char`
- `xRadius: float`
- `yRadius: float`
- `zRadius: float`
- `drawSphere: bool`

---

### `0105` LOCATE_CHAR_ON_FOOT_CHAR_3D
Returns true if the character is within the 3D radius of the other character on foot

**Class:** `Char.LocateOnFootChar3D`
**Flags:** condition

**Input:**
- `self: Char`
- `target: Char`
- `xRadius: float`
- `yRadius: float`
- `zRadius: float`
- `drawSphere: bool`

---

### `0106` LOCATE_CHAR_IN_CAR_CHAR_3D
Returns true if the character is within the 3D radius of the other character in a vehicle

**Class:** `Char.LocateInCarChar3D`
**Flags:** condition

**Input:**
- `self: Char`
- `target: Char`
- `xRadius: float`
- `yRadius: float`
- `zRadius: float`
- `drawSphere: bool`

---

### `0114` ADD_AMMO_TO_CHAR
Adds the specified amount of ammo to the character's weapon, if the character has the weapon

**Class:** `Char.AddAmmo`

**Input:**
- `self: Char`
- `weaponType: WeaponType`
- `ammo: int`

---

### `0118` IS_CHAR_DEAD
Returns true if the handle is an invalid character handle or the character is dead (wasted)

**Class:** `Char.IsDead`
**Flags:** condition, static

**Input:**
- `handle: any`

---

### `0129` CREATE_CHAR_INSIDE_CAR
Creates a character in the driver's seat of the vehicle

**Class:** `Char.CreateInsideCar`
**Flags:** constructor

**Input:**
- `vehicle: Car`
- `pedType: PedType`
- `modelId: model_char`

**Output:**
- `handle: Char (variable)`

---

### `0154` IS_CHAR_IN_ZONE
Returns true if the character is in the specified map zone

**Class:** `Char.IsInZone`
**Flags:** condition

**Input:**
- `self: Char`
- `zone: zone_key`

---

### `0172` GET_CHAR_HEADING
Returns the character's heading (z-angle)

**Class:** `Char.GetHeading`

**Input:**
- `self: Char`

**Output:**
- `heading: float (variable)`

---

### `0173` SET_CHAR_HEADING
Sets the character's heading (z-angle)

**Class:** `Char.SetHeading`

**Input:**
- `self: Char`
- `heading: float`

---

### `0179` IS_CHAR_TOUCHING_OBJECT
Returns true if the character is colliding with the specified object

**Class:** `Char.IsTouchingObject`
**Flags:** condition

**Input:**
- `self: Char`
- `object: Object`

---

### `017B` SET_CHAR_AMMO
Sets the amount of ammo the character has in the specified weapon

**Class:** `Char.SetAmmo`

**Input:**
- `self: Char`
- `weaponType: WeaponType`
- `ammo: int`

---

### `0184` IS_CHAR_HEALTH_GREATER
Returns true if the character's health is over the specified value

**Class:** `Char.IsHealthGreater`
**Flags:** condition

**Input:**
- `self: Char`
- `health: int`

---

### `01A1` IS_CHAR_IN_AREA_ON_FOOT_2D
Returns true if the character is within the specified 2D area on foot

**Class:** `Char.IsInAreaOnFoot2D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `drawSphere: bool`

---

### `01A2` IS_CHAR_IN_AREA_IN_CAR_2D
Returns true if the character is within the specified 2D area in a vehicle

**Class:** `Char.IsInAreaInCar2D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `drawSphere: bool`

---

### `01A3` IS_CHAR_STOPPED_IN_AREA_2D
Returns true if the character stopped within the specified 2D area

**Class:** `Char.IsStoppedInArea2D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `drawSphere: bool`

---

### `01A4` IS_CHAR_STOPPED_IN_AREA_ON_FOOT_2D
Returns true if the character stopped within the specified 2D area on foot

**Class:** `Char.IsStoppedInAreaOnFoot2D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `drawSphere: bool`

---

### `01A5` IS_CHAR_STOPPED_IN_AREA_IN_CAR_2D
Returns true if the character stopped within the specified 2D area in a vehicle

**Class:** `Char.IsStoppedInAreaInCar2D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `drawSphere: bool`

---

### `01A6` IS_CHAR_IN_AREA_ON_FOOT_3D
Returns true if the character is within the specified 3D area on foot

**Class:** `Char.IsInAreaOnFoot3D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `drawSphere: bool`

---

### `01A7` IS_CHAR_IN_AREA_IN_CAR_3D
Returns true if the character is within the specified 3D area in a vehicle

**Class:** `Char.IsInAreaInCar3D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `drawSphere: bool`

---

### `01A8` IS_CHAR_STOPPED_IN_AREA_3D
Returns true if the character stopped within the specified 3D area

**Class:** `Char.IsStoppedInArea3D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `drawSphere: bool`

---

### `01A9` IS_CHAR_STOPPED_IN_AREA_ON_FOOT_3D
Returns true if the character stopped within the specified 3D area on foot

**Class:** `Char.IsStoppedInAreaOnFoot3D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `drawSphere: bool`

---

### `01AA` IS_CHAR_STOPPED_IN_AREA_IN_CAR_3D
Returns true if the character stopped within the specified 3D area in a vehicle

**Class:** `Char.IsStoppedInAreaInCar3D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `drawSphere: bool`

---

### `01B2` GIVE_WEAPON_TO_CHAR
Gives the character the weapon with the specified amount of ammo

**Class:** `Char.GiveWeapon`

**Input:**
- `self: Char`
- `weaponType: WeaponType`
- `ammo: int`

---

### `01B9` SET_CURRENT_CHAR_WEAPON
Sets the character's currently held weapon

**Class:** `Char.SetCurrentWeapon`

**Input:**
- `self: Char`
- `weaponType: WeaponType`

---

### `01C2` MARK_CHAR_AS_NO_LONGER_NEEDED
Allows the character to be deleted by the game if necessary, and also removes them from the mission cleanup list, if applicable

**Class:** `Char.MarkAsNoLongerNeeded`

**Input:**
- `self: Char`

---

### `01C5` DONT_REMOVE_CHAR
Removes the character from the mission cleanup list, preventing it from being deleted when the mission ends

**Class:** `Char.DontRemove`

**Input:**
- `self: Char`

---

### `01C8` CREATE_CHAR_AS_PASSENGER
Creates a character with the specified model in the passenger seat of the vehicle

**Class:** `Char.CreateAsPassenger`
**Flags:** constructor

**Input:**
- `vehicle: Car`
- `pedType: PedType`
- `modelId: model_char`
- `seat: SeatId`

**Output:**
- `handle: Char (variable)`

---

### `0202` LOCATE_CHAR_ANY_MEANS_CAR_2D
Returns true if the character is within the 2D radius of the vehicle

**Class:** `Char.LocateAnyMeansCar2D`
**Flags:** condition

**Input:**
- `self: Char`
- `vehicle: Car`
- `xRadius: float`
- `yRadius: float`
- `drawSphere: bool`

---

### `0203` LOCATE_CHAR_ON_FOOT_CAR_2D
Returns true if the character is within the 2D radius of the vehicle on foot

**Class:** `Char.LocateOnFootCar2D`
**Flags:** condition

**Input:**
- `self: Char`
- `vehicle: Car`
- `xRadius: float`
- `yRadius: float`
- `drawSphere: bool`

---

### `0204` LOCATE_CHAR_IN_CAR_CAR_2D
Returns true if the character is within the 2D radius of the vehicle in a vehicle

**Class:** `Char.LocateInCarCar2D`
**Flags:** condition

**Input:**
- `self: Char`
- `handle: Car`
- `xRadius: float`
- `yRadius: float`
- `drawSphere: bool`

---

### `0205` LOCATE_CHAR_ANY_MEANS_CAR_3D
Returns true if the character is within the 3D radius of the vehicle

**Class:** `Char.LocateAnyMeansCar3D`
**Flags:** condition

**Input:**
- `self: Char`
- `vehicle: Car`
- `xRadius: float`
- `yRadius: float`
- `zRadius: float`
- `drawSphere: bool`

---

### `0206` LOCATE_CHAR_ON_FOOT_CAR_3D
Returns true if the character is within the 3D radius of the vehicle on foot

**Class:** `Char.LocateOnFootCar3D`
**Flags:** condition

**Input:**
- `self: Char`
- `vehicle: Car`
- `xRadius: float`
- `yRadius: float`
- `zRadius: float`
- `drawSphere: bool`

---

### `0207` LOCATE_CHAR_IN_CAR_CAR_3D
Returns true if the character is within the 3D radius of the vehicle in a vehicle

**Class:** `Char.LocateInCarCar3D`
**Flags:** condition

**Input:**
- `self: Char`
- `vehicle: Car`
- `xRadius: float`
- `yRadius: float`
- `zRadius: float`
- `drawSphere: bool`

---

### `0223` SET_CHAR_HEALTH
Sets the character's health

**Class:** `Char.SetHealth`

**Input:**
- `self: Char`
- `health: int`

---

### `0226` GET_CHAR_HEALTH
Returns the character's health

**Class:** `Char.GetHealth`

**Input:**
- `self: Char`

**Output:**
- `health: int (variable)`

---

### `023B` IS_CHAR_TOUCHING_OBJECT_ON_FOOT
Returns true if the character is colliding with the specified object on foot

**Class:** `Char.IsTouchingObjectOnFoot`
**Flags:** condition

**Input:**
- `self: Char`
- `object: Object`

---

### `0245` SET_ANIM_GROUP_FOR_CHAR
Sets the animation group for the character

**Class:** `Char.SetAnimGroup`

**Input:**
- `self: Char`
- `animGroup: AnimGroup`

---

### `02A0` IS_CHAR_STOPPED
Returns true if the character is not moving

**Class:** `Char.IsStopped`
**Flags:** condition

**Input:**
- `self: Char`

---

### `02A9` SET_CHAR_ONLY_DAMAGED_BY_PLAYER
Makes a character immune to everything except the player

**Class:** `Char.SetOnlyDamagedByPlayer`

**Input:**
- `self: Char`
- `state: bool`

---

### `02AB` SET_CHAR_PROOFS
Sets the character's immunities

**Class:** `Char.SetProofs`

**Input:**
- `self: Char`
- `bulletProof: bool`
- `fireProof: bool`
- `explosionProof: bool`
- `collisionProof: bool`
- `meleeProof: bool`

---

### `02CB` IS_CHAR_ON_SCREEN
Returns true if the character is visible

**Class:** `Char.IsOnScreen`
**Flags:** condition

**Input:**
- `self: Char`

---

### `02D6` IS_CHAR_SHOOTING_IN_AREA
Returns true if the character fired a weapon within the specified 2D area

**Class:** `Char.IsShootingInArea`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `topRightX: float`
- `topRightY: float`
- `drawSphere: bool`

---

### `02D8` IS_CURRENT_CHAR_WEAPON
Returns true if the character is holding the given type of weapon

**Class:** `Char.IsCurrentWeapon`
**Flags:** condition

**Input:**
- `self: Char`
- `weaponType: WeaponType`

---

### `02E0` IS_CHAR_SHOOTING
Returns true if the character is firing a weapon

**Class:** `Char.IsShooting`
**Flags:** condition

**Input:**
- `self: Char`

---

### `02E2` SET_CHAR_ACCURACY
Affects how often the character will hit the target when attacking with a weapon

**Class:** `Char.SetAccuracy`

**Input:**
- `self: Char`
- `accuracy: int`

---

### `02F2` IS_CHAR_MODEL
Returns true if the character's model ID is equivalent to the model ID passed

**Class:** `Char.IsModel`
**Flags:** condition

**Input:**
- `self: Char`
- `modelId: model_char`

---

### `031D` HAS_CHAR_BEEN_DAMAGED_BY_WEAPON
Returns true if the character has been hit by the specified weapon

**Class:** `Char.HasBeenDamagedByWeapon`
**Flags:** condition

**Input:**
- `self: Char`
- `weaponType: WeaponType`

---

### `0321` EXPLODE_CHAR_HEAD
Dismembers the character

**Class:** `Char.ExplodeHead`

**Input:**
- `self: Char`

---

### `0332` SET_CHAR_BLEEDING
Makes a character bleed

**Class:** `Char.SetBleeding`

**Input:**
- `self: Char`
- `state: bool`

---

### `0337` SET_CHAR_VISIBLE
Sets whether the character is visible or not

**Class:** `Char.SetVisible`

**Input:**
- `self: Char`
- `state: bool`

---

### `034F` REMOVE_CHAR_ELEGANTLY
Removes the character with a fade, freeing game memory

**Class:** `Char.RemoveElegantly`

**Input:**
- `self: Char`

---

### `0350` SET_CHAR_STAY_IN_SAME_PLACE
Makes the character maintain their position when attacked

**Class:** `Char.SetStayInSamePlace`

**Input:**
- `self: Char`
- `state: bool`

---

### `035F` ADD_ARMOUR_TO_CHAR
Increases the character's armor by the specified value to the maximum of 100

**Class:** `Char.AddArmor`

**Input:**
- `self: Char`
- `amount: int`

---

### `0362` WARP_CHAR_FROM_CAR_TO_COORD
Pulls the character out of their car and places at the location

**Class:** `Char.WarpFromCarToCoord`

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `z: float`

---

### `0364` HAS_CHAR_SPOTTED_CHAR
Returns true if the character can see the target character

**Class:** `Char.HasSpottedChar`
**Flags:** condition

**Input:**
- `self: Char`
- `target: Char`

---

### `036A` WARP_CHAR_INTO_CAR
Puts the character in the specified vehicle

**Class:** `Char.WarpIntoCar`

**Input:**
- `self: Char`
- `vehicle: Car`

---

### `0376` CREATE_RANDOM_CHAR
Creates a character with a randomised model and pedtype at the specified coordinates

**Class:** `Char.CreateRandom`
**Flags:** constructor

**Input:**
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `handle: Char (variable)`

---

### `0393` SET_CHAR_ANIM_SPEED
Makes an char perform an animation at the specified speed

**Class:** `Char.SetAnimSpeed`

**Input:**
- `self: Char`
- `animName: string`
- `animSpeed: float`

---

### `039E` SET_CHAR_CANT_BE_DRAGGED_OUT
Locks the character while in a car

**Class:** `Char.SetCantBeDraggedOut`

**Input:**
- `self: Char`
- `state: bool`

---

### `03A3` IS_CHAR_MALE
Returns true if the character is male

**Class:** `Char.IsMale`
**Flags:** condition

**Input:**
- `self: Char`

---

### `03C0` STORE_CAR_CHAR_IS_IN_NO_SAVE
Returns the character's vehicle handle without marking it as used by the script, therefore allowing it to be deleted by the game at any time (alts:00D9,0811,0484)

**Class:** `Char.StoreCarIsInNoSave`

**Input:**
- `self: Char`

**Output:**
- `handle: Car (variable)`

---

### `03FE` SET_CHAR_MONEY
Sets the character's cash sum, setting how much cash they will drop when dead

**Class:** `Char.SetMoney`

**Input:**
- `self: Char`
- `amount: int`

---

### `041A` GET_AMMO_IN_CHAR_WEAPON
Gets the amount of ammo in the specified weapon of the character

**Class:** `Char.GetAmmoInWeapon`

**Input:**
- `self: Char`
- `weaponType: WeaponType`

**Output:**
- `ammo: int (variable)`

---

### `0430` WARP_CHAR_INTO_CAR_AS_PASSENGER
Puts the character into a vehicle's passenger seat

**Class:** `Char.WarpIntoCarAsPassenger`

**Input:**
- `self: Char`
- `handle: Car`
- `seat: SeatId`

---

### `0433` SET_CHAR_IS_CHRIS_CRIMINAL
Sets whether the character is a psychotic killer or not

**Class:** `Char.SetIsChrisCriminal`

**Input:**
- `self: Char`
- `state: bool`

---

### `0446` SET_CHAR_SUFFERS_CRITICAL_HITS
Sets whether the specified character is immune to headshots

**Class:** `Char.SetSuffersCriticalHits`

**Input:**
- `self: Char`
- `state: bool`

---

### `0448` IS_CHAR_SITTING_IN_CAR
Returns true if the character is sitting in the specified vehicle

**Class:** `Char.IsSittingInCar`
**Flags:** condition

**Input:**
- `self: Char`
- `vehicle: Car`

---

### `0449` IS_CHAR_SITTING_IN_ANY_CAR
Returns true if the character is sitting in any vehicle

**Class:** `Char.IsSittingInAnyCar`
**Flags:** condition

**Input:**
- `self: Char`

---

### `044B` IS_CHAR_ON_FOOT
Returns true if the character is on foot, and not occupying a vehicle

**Class:** `Char.IsOnFoot`
**Flags:** condition

**Input:**
- `self: Char`

---

### `0464` ATTACH_CHAR_TO_CAR
Puts character into a turret on the vehicle, allowing them to shoot

**Class:** `Char.AttachToCar`

**Input:**
- `self: Char`
- `vehicle: Car`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `heading: Facing`
- `headingRange: float`
- `weaponType: WeaponType`

---

### `0465` DETACH_CHAR_FROM_CAR
Takes the character out of turret mode (0464)

**Class:** `Char.DetachFromCar`

**Input:**
- `self: Char`

---

### `0467` CLEAR_CHAR_LAST_WEAPON_DAMAGE
Clears the character's last weapon damage (see 031D)

**Class:** `Char.ClearLastWeaponDamage`

**Input:**
- `self: Char`

---

### `046D` GET_NUMBER_OF_FOLLOWERS
Returns the number of members which are in a group of the character (01DE)

**Class:** `Char.GetNumberOfFollowers`

**Input:**
- `self: Char`

**Output:**
- `number: int (variable)`

---

### `0470` GET_CURRENT_CHAR_WEAPON
Returns the type of weapon that the character is currently holding

**Class:** `Char.GetCurrentWeapon`

**Input:**
- `self: Char`

**Output:**
- `weaponType: WeaponType (variable)`

---

### `0471` LOCATE_CHAR_ANY_MEANS_OBJECT_2D
Returns true if the character is within the 2D radius of the object

**Class:** `Char.LocateAnyMeansObject2D`
**Flags:** condition

**Input:**
- `self: Char`
- `object: Object`
- `xRadius: float`
- `yRadius: float`
- `drawSphere: bool`

---

### `0472` LOCATE_CHAR_ON_FOOT_OBJECT_2D
Returns true if the character is within the 2D radius of the object on foot

**Class:** `Char.LocateOnFootObject2D`
**Flags:** condition

**Input:**
- `self: Char`
- `object: Object`
- `xRadius: float`
- `yRadius: float`
- `drawSphere: bool`

---

### `0473` LOCATE_CHAR_IN_CAR_OBJECT_2D
Returns true if the character is within the 2D radius of the object in a vehicle

**Class:** `Char.LocateInCarObject2D`
**Flags:** condition

**Input:**
- `self: Char`
- `object: Object`
- `xRadius: float`
- `yRadius: float`
- `drawSphere: bool`

---

### `0474` LOCATE_CHAR_ANY_MEANS_OBJECT_3D
Returns true if the character is within the 3D radius of the object

**Class:** `Char.LocateAnyMeansObject3D`
**Flags:** condition

**Input:**
- `self: Char`
- `object: Object`
- `xRadius: float`
- `yRadius: float`
- `zRadius: float`
- `drawSphere: bool`

---

### `0475` LOCATE_CHAR_ON_FOOT_OBJECT_3D
Returns true if the character is within the 3D radius of the object on foot

**Class:** `Char.LocateOnFootObject3D`
**Flags:** condition

**Input:**
- `self: Char`
- `object: Object`
- `xRadius: float`
- `yRadius: float`
- `zRadius: float`
- `drawSphere: bool`

---

### `0476` LOCATE_CHAR_IN_CAR_OBJECT_3D
Returns true if the character is within the 3D radius of the object in a vehicle

**Class:** `Char.LocateInCarObject3D`
**Flags:** condition

**Input:**
- `self: Char`
- `object: Object`
- `xRadius: float`
- `yRadius: float`
- `zRadius: float`
- `drawSphere: bool`

---

### `047A` IS_CHAR_ON_ANY_BIKE
Returns true if the character is riding a bike

**Class:** `Char.IsOnAnyBike`
**Flags:** condition

**Input:**
- `self: Char`

---

### `0480` CAN_CHAR_SEE_DEAD_CHAR
Returns true if the character sees a dead body of the given type

**Class:** `Char.CanSeeDeadChar`
**Flags:** condition

**Input:**
- `self: Char`
- `pedType: PedType`

---

### `0489` SHUT_CHAR_UP
Sets the character's ability to talk

**Class:** `Char.ShutUp`

**Input:**
- `self: Char`
- `state: bool`

---

### `048F` REMOVE_ALL_CHAR_WEAPONS
Removes the characters weapons

**Class:** `Char.RemoveAllWeapons`

**Input:**
- `self: Char`

---

### `0491` HAS_CHAR_GOT_WEAPON
Returns true if the character has the specified weapon

**Class:** `Char.HasGotWeapon`
**Flags:** condition

**Input:**
- `self: Char`
- `weaponType: WeaponType`

---

### `04A7` IS_CHAR_IN_ANY_BOAT
Returns true if the character is driving a boat

**Class:** `Char.IsInAnyBoat`
**Flags:** condition

**Input:**
- `self: Char`

**Details:**

This conditional command returns true if the character is in a boat, either as a driver or a passenger. By default the game will recognize the following list of vehicles as boats (for which the `IS_BOAT` model flag is set in the `handling.cfg` file):

- Coastguard
- Dinghy
- Jetmax
- Launch
- Marquis
- Predator
- Speeder
- Squalo
- Reefer
- Tropic

---

### `04A9` IS_CHAR_IN_ANY_HELI
Returns true if the character is flying a helicopter

**Class:** `Char.IsInAnyHeli`
**Flags:** condition

**Input:**
- `self: Char`

**Details:**

This conditional command returns true if the character is in a helicopter. By default the game will recognize the following list of vehicles as helicopters (for which the `IS_HELI` flag is set in the `handling.cfg` file):

- Cargobob
- Hunter
- Leviathan
- Maverick
- News Chopper
- Police Maverick
- Raindancer
- RC Goblin
- RC Raider
- Sea Sparrow
- Sparrow

---

### `04AB` IS_CHAR_IN_ANY_PLANE
Returns true if the character is in a plane

**Class:** `Char.IsInAnyPlane`
**Flags:** condition

**Input:**
- `self: Char`

**Details:**

This conditional command returns true if the character is in a plane, either as a driver or a passenger. By default the game will recognize the following list of vehicles as planes (for which the `IS_PLANE` flag is set in the `handling.cfg` file):

- Andromada
- AT-400
- Beagle
- Cropduster
- Dodo
- Hydra
- Nevada
- RC Baron
- Shamal
- Skimmer
- Stuntplane

---

### `04AD` IS_CHAR_IN_WATER
Returns true if the character is in water

**Class:** `Char.IsInWater`
**Flags:** condition

**Input:**
- `self: Char`

---

### `04B8` GET_CHAR_WEAPON_IN_SLOT
Returns the weapon type, ammo and model from the specified slot

**Class:** `Char.GetWeaponInSlot`

**Input:**
- `self: Char`
- `slot: int`

**Output:**
- `weaponType: WeaponType (variable)`
- `weaponAmmo: int (variable)`
- `weaponModel: model_object (variable)`

---

### `04C4` GET_OFFSET_FROM_CHAR_IN_WORLD_COORDS
Returns the coordinates of the character, with an offset

**Class:** `Char.GetOffsetInWorldCoords`

**Input:**
- `self: Char`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `04C5` HAS_CHAR_BEEN_PHOTOGRAPHED
Returns true if the character has been photographed

**Class:** `Char.HasBeenPhotographed`
**Flags:** condition

**Input:**
- `self: Char`

---

### `04C8` IS_CHAR_IN_FLYING_VEHICLE
Returns true if the character is in a flying vehicle

**Class:** `Char.IsInFlyingVehicle`
**Flags:** condition

**Input:**
- `self: Char`

**Details:**

This conditional command returns true if the character is in a flying vehicle. Flying vehicles include all planes and helicopters.

---

### `04D7` FREEZE_CHAR_POSITION
Sets whether the character's position remains unchanged

**Class:** `Char.FreezePosition`

**Input:**
- `self: Char`
- `state: bool`

---

### `04D8` SET_CHAR_DROWNS_IN_WATER
Controls whether the character can drown in water

**Class:** `Char.SetDrownsInWater`

**Input:**
- `self: Char`
- `state: bool`

---

### `04DD` GET_CHAR_ARMOUR
Returns the character's armor amount

**Class:** `Char.GetArmor`

**Input:**
- `self: Char`

**Output:**
- `armor: int (variable)`

---

### `04F0` IS_CHAR_WAITING_FOR_WORLD_COLLISION

**Class:** `Char.IsWaitingForWorldCollision`
**Flags:** condition

**Input:**
- `self: Char`

---

### `04F4` ATTACH_CHAR_TO_OBJECT
Attaches the character to the specified object, in turret mode

**Class:** `Char.AttachToObject`

**Input:**
- `self: Char`
- `handle: Object`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `heading: Facing`
- `headingRange: float`
- `weaponType: WeaponType`

---

### `0503` CREATE_SWAT_ROPE
Creates a character descending from a rope

**Class:** `Char.CreateSwatRope`
**Flags:** constructor

**Input:**
- `pedType: PedType`
- `modelId: model_char`
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `handle: Char (variable)`

---

### `051A` HAS_CHAR_BEEN_DAMAGED_BY_CHAR
Returns true if the character has been hurt by the other character

**Class:** `Char.HasBeenDamagedByChar`
**Flags:** condition

**Input:**
- `self: Char`
- `handle: Char`

---

### `051B` HAS_CHAR_BEEN_DAMAGED_BY_CAR
Returns true if the char has been hurt by the specified vehicle

**Class:** `Char.HasBeenDamagedByCar`
**Flags:** condition

**Input:**
- `self: Char`
- `handle: Car`

---

### `0526` SET_CHAR_STAY_IN_CAR_WHEN_JACKED
Makes the character stay in the vehicle when it is jacked (characters let themselves get "kidnapped")

**Class:** `Char.SetStayInCarWhenJacked`

**Input:**
- `self: Char`
- `state: bool`

---

### `0547` IS_CHAR_TOUCHING_VEHICLE
Returns true if the character is colliding with a car

**Class:** `Char.IsTouchingVehicle`
**Flags:** condition

**Input:**
- `self: Char`
- `handle: Car`

---

### `054A` SET_CHAR_CAN_BE_SHOT_IN_VEHICLE
Makes the character immune to a damage while in a vehicle

**Class:** `Char.SetCanBeShotInVehicle`

**Input:**
- `self: Char`
- `state: bool`

---

### `054E` CLEAR_CHAR_LAST_DAMAGE_ENTITY

**Class:** `Char.ClearLastDamageEntity`

**Input:**
- `self: Char`

---

### `0555` REMOVE_WEAPON_FROM_CHAR
Removes the weapon from the character

**Class:** `Char.RemoveWeapon`

**Input:**
- `self: Char`
- `weaponType: WeaponType`

---

### `0560` CREATE_RANDOM_CHAR_AS_DRIVER
Creates a driver in the vehicle

**Class:** `Char.CreateRandomAsDriver`
**Flags:** constructor

**Input:**
- `vehicle: Car`

**Output:**
- `handle: Char (variable)`

---

### `0561` CREATE_RANDOM_CHAR_AS_PASSENGER
Creates a random character in the passenger seat of the vehicle

**Class:** `Char.CreateRandomAsPassenger`
**Flags:** constructor

**Input:**
- `vehicle: Car`
- `seat: SeatId`

**Output:**
- `handle: Char (variable)`

---

### `0568` SET_CHAR_NEVER_TARGETTED
Sets whether the character won't be targeted by the autoaim system

**Class:** `Char.SetNeverTargeted`

**Input:**
- `self: Char`
- `state: bool`

---

### `056C` IS_CHAR_IN_ANY_POLICE_VEHICLE
Returns true if the character is driving a police vehicle

**Class:** `Char.IsInAnyPoliceVehicle`
**Flags:** condition

**Input:**
- `self: Char`

**Details:**

This conditional command returns true if the character is in a police vehicle. It recognizes the following as police vehicles:

| Id  | Name                  |
| --- | --------------------- |
| 427 | Enforcer              |
| 430 | Predator              |
| 432 | Rhino                 |
| 433 | Barracks              |
| 497 | Police Maverick       |
| 523 | HPV1000               |
| 528 | FBI Truck             |
| 596 | Police (Los Santos)   |
| 597 | Police (San Fierro)   |
| 598 | Police (Las Venturas) |
| 599 | Ranger                |
| 601 | S.W.A.T.              |

---

### `056D` DOES_CHAR_EXIST
Returns true if the handle is a valid character handle

**Class:** `Char.DoesExist`
**Flags:** condition, static

**Input:**
- `handle: any`

---

### `0575` FREEZE_CHAR_POSITION_AND_DONT_LOAD_COLLISION

**Class:** `Char.FreezePositionAndDontLoadCollision`

**Input:**
- `self: Char`
- `state: bool`

---

### `0588` SET_LOAD_COLLISION_FOR_CHAR_FLAG

**Class:** `Char.SetLoadCollisionFlag`

**Input:**
- `self: Char`
- `state: bool`

---

### `0597` IS_CHAR_DUCKING
Returns true if the specified character is crouching

**Class:** `Char.IsDucking`
**Flags:** condition

**Input:**
- `self: Char`

---

### `05F6` IS_CHAR_IN_ANGLED_AREA_2D
Checks if the character is within the angled 2D area

**Class:** `Char.IsInAngledArea2D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `angle: float`
- `drawSphere: bool`

---

### `05F7` IS_CHAR_IN_ANGLED_AREA_ON_FOOT_2D
Checks if the character is within the angled 2D area

**Class:** `Char.IsInAngledAreaOnFoot2D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `angle: float`
- `drawSphere: bool`

---

### `05F8` IS_CHAR_IN_ANGLED_AREA_IN_CAR_2D
Checks if the character is in a car which is within the angled 2D area

**Class:** `Char.IsInAngledAreaInCar2D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `angle: float`
- `drawSphere: bool`

---

### `05F9` IS_CHAR_STOPPED_IN_ANGLED_AREA_2D
Checks if the character is within the angled 2D area and is motionless

**Class:** `Char.IsStoppedInAngledArea2D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `angle: float`
- `drawSphere: bool`

---

### `05FA` IS_CHAR_STOPPED_IN_ANGLED_AREA_ON_FOOT_2D
Checks if the character is within the angled 2D area

**Class:** `Char.IsStoppedInAngledAreaOnFoot2D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `angle: float`
- `drawSphere: bool`

---

### `05FB` IS_CHAR_STOPPED_IN_ANGLED_AREA_IN_CAR_2D
Checks if the character is in a motionless car within the angled 2D area

**Class:** `Char.IsStoppedInAngledAreaInCar2D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`
- `angle: float`
- `drawSphere: bool`

---

### `05FC` IS_CHAR_IN_ANGLED_AREA_3D
Checks if the character is within the angled 3D area

**Class:** `Char.IsInAngledArea3D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `angle: float`
- `drawSphere: bool`

---

### `05FD` IS_CHAR_IN_ANGLED_AREA_ON_FOOT_3D
Checks if the character is within the angled 3D area

**Class:** `Char.IsInAngledAreaOnFoot3D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `angle: float`
- `drawSphere: bool`

---

### `05FE` IS_CHAR_IN_ANGLED_AREA_IN_CAR_3D
Checks if the character is in a car which is within the angled 3D area

**Class:** `Char.IsInAngledAreaInCar3D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `angle: float`
- `drawSphere: bool`

---

### `05FF` IS_CHAR_STOPPED_IN_ANGLED_AREA_3D
Checks if the character is within the angled 3D area and is motionless

**Class:** `Char.IsStoppedInAngledArea3D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `angle: float`
- `drawSphere: bool`

---

### `0600` IS_CHAR_STOPPED_IN_ANGLED_AREA_ON_FOOT_3D
Checks if the character is on foot within the angled 3D area and is motionless

**Class:** `Char.IsStoppedInAngledAreaOnFoot3D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `angle: float`
- `drawSphere: bool`

---

### `0601` IS_CHAR_STOPPED_IN_ANGLED_AREA_IN_CAR_3D
Checks if the character is in a motionless car within the angled 3D area

**Class:** `Char.IsStoppedInAngledAreaInCar3D`
**Flags:** condition

**Input:**
- `self: Char`
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`
- `angle: float`
- `drawSphere: bool`

---

### `0602` IS_CHAR_IN_TAXI
Returns true if the character is driving a taxi

**Class:** `Char.IsInTaxi`
**Flags:** condition

**Input:**
- `self: Char`

---

### `060B` SET_CHAR_DECISION_MAKER
Sets the decision maker for the character

**Class:** `Char.SetDecisionMaker`

**Input:**
- `self: Char`
- `handleOrTemplate: DecisionMakerCharTemplate`

---

### `060F` SET_SENSE_RANGE
Sets the seeing and hearing range for the specified character or for all mission characters when handle is -1

**Class:** `Char.SetSenseRange`
**Flags:** static

**Input:**
- `handle: Char`
- `range: float`

---

### `0611` IS_CHAR_PLAYING_ANIM
Returns true if character is performing the specified animation

**Class:** `Char.IsPlayingAnim`
**Flags:** condition

**Input:**
- `self: Char`
- `animationName: string`

---

### `0612` SET_CHAR_ANIM_PLAYING_FLAG
Sets whether the animation is playing

**Class:** `Char.SetAnimPlayingFlag`

**Input:**
- `self: Char`
- `animationName: string`
- `flag: bool`

---

### `0613` GET_CHAR_ANIM_CURRENT_TIME
Returns the progress of the animation on the char, ranging from 0.0 to 1.0

**Class:** `Char.GetAnimCurrentTime`

**Input:**
- `self: Char`
- `animationName: string`

**Output:**
- `time: float (variable)`

---

### `0614` SET_CHAR_ANIM_CURRENT_TIME
Sets how far through the animation the character is, with 1

**Class:** `Char.SetAnimCurrentTime`

**Input:**
- `self: Char`
- `animationName: string`
- `time: float`

---

### `0618` PERFORM_SEQUENCE_TASK
Assigns the character to the specified action sequence

**Class:** `Char.PerformSequence`

**Input:**
- `self: Char`
- `sequence: Sequence`

---

### `0619` SET_CHAR_COLLISION
Sets whether collision detection is enabled for the character

**Class:** `Char.SetCollision`

**Input:**
- `self: Char`
- `state: bool`

---

### `061A` GET_CHAR_ANIM_TOTAL_TIME
Returns a float of the length of the animation in milliseconds

**Class:** `Char.GetAnimTotalTime`

**Input:**
- `self: Char`
- `animationName: string`

**Output:**
- `totalTime: float (variable)`

---

### `0621` CREATE_CHAR_AT_ATTRACTOR

**Class:** `Char.CreateAtAttractor`
**Flags:** constructor

**Input:**
- `pedType: PedType`
- `modelId: model_char`
- `attractor: Attractor`
- `task: TaskCommand`

**Output:**
- `handle: Char (variable)`

---

### `062E` GET_SCRIPT_TASK_STATUS
Returns the status of the specified script task of the character

**Class:** `Char.GetScriptTaskStatus`

**Input:**
- `self: Char`
- `task: TaskCommand`

**Output:**
- `status: TaskStatus (variable)`

**Details:**

The second argument is the task id. This id matches an opcode id for Task commands. 
For example, TASK_STAND_STILL has an id `0x05BA`, TASK_LOOK_ABOUT has an id `0x05C9`, etc.

---

### `0642` IS_CHAR_AT_SCRIPTED_ATTRACTOR

**Class:** `Char.IsAtScriptedAttractor`
**Flags:** condition

**Input:**
- `self: Char`
- `handle: Attractor`

---

### `0646` GET_SEQUENCE_PROGRESS
Gets the characters task sequence progress, as started by 0618

**Class:** `Char.GetSequenceProgress`

**Input:**
- `self: Char`

**Output:**
- `progress: int (variable)`

---

### `0647` CLEAR_LOOK_AT
Clears the char's look task, making them stop looking at whatever they were assigned to look at

**Class:** `Char.ClearLookAt`

**Input:**
- `self: Char`

---

### `0648` SET_FOLLOW_NODE_THRESHOLD_DISTANCE
Sets the range within which the char responds to events

**Class:** `Char.SetFollowNodeThresholdDistance`

**Input:**
- `self: Char`
- `range: float`

---

### `0665` GET_CHAR_MODEL
Returns the characters model

**Class:** `Char.GetModel`

**Input:**
- `self: Char`

**Output:**
- `modelId: int (variable)`

---

### `0687` CLEAR_CHAR_TASKS
Clears the char's task, making them quit whatever they were doing

**Class:** `Char.ClearTasks`

**Input:**
- `self: Char`

---

### `06A7` ATTACH_CHAR_TO_BIKE

**Class:** `Char.AttachToBike`

**Input:**
- `self: Char`
- `vehicle: Car`
- `xOffset: float`
- `yOffset: float`
- `zOffset: float`
- `heading: Facing`
- `headingRange: float`
- `pitchRange: float`
- `weaponType: WeaponType`

---

### `06AB` HIDE_CHAR_WEAPON_FOR_SCRIPTED_CUTSCENE
Hides all of the specified char's weapons

**Class:** `Char.HideWeaponForScriptedCutscene`

**Input:**
- `self: Char`
- `state: bool`

---

### `06AC` GET_CHAR_SPEED
Returns the char's movement speed

**Class:** `Char.GetSpeed`

**Input:**
- `self: Char`

**Output:**
- `speed: float (variable)`

---

### `06C9` REMOVE_CHAR_FROM_GROUP
Removes the character from their current group

**Class:** `Char.RemoveFromGroup`

**Input:**
- `self: Char`

**Details:**

This command removes the character from any group it belongs to. This command is similar to LEAVE_GROUP used in GTA3 and Vice City.

---

### `06EE` IS_GROUP_MEMBER
Returns true if the character is a member of the specified group

**Class:** `Char.IsGroupMember`
**Flags:** condition

**Input:**
- `self: Char`
- `handle: Group`

---

### `06EF` IS_GROUP_LEADER
Returns true if the character is the leader of the specified group

**Class:** `Char.IsGroupLeader`
**Flags:** condition

**Input:**
- `self: Char`
- `handle: Group`

---

### `06FF` ARE_ANY_CHARS_NEAR_CHAR
Returns true if any characters are within range of the character

**Class:** `Char.IsNearAnyChars`
**Flags:** condition

**Input:**
- `self: Char`
- `radius: float`

---

### `070B` DROP_OBJECT

**Class:** `Char.DropObject`

**Input:**
- `self: Char`
- `state: bool`

---

### `0737` IS_CHAR_HOLDING_OBJECT
Returns true if the char is lifting the specified object

**Class:** `Char.IsHoldingObject`
**Flags:** condition

**Input:**
- `self: Char`
- `handle: Object`

---

### `0741` HAS_CHAR_BEEN_ARRESTED
Returns true if the character has been arrested

**Class:** `Char.HasBeenArrested`
**Flags:** condition

**Input:**
- `self: Char`

---

### `074E` SET_INFORM_RESPECTED_FRIENDS

**Class:** `Char.SetInformRespectedFriends`

**Input:**
- `self: Char`
- `radius: float`
- `_p3: int`

---

### `074F` IS_CHAR_RESPONDING_TO_EVENT
Returns true if the character is responding to the specified ped event

**Class:** `Char.IsRespondingToEvent`
**Flags:** condition

**Input:**
- `self: Char`
- `event: Event`

---

### `0770` SET_CHAR_IS_TARGET_PRIORITY
Causes the auto aim to be more likely to target the specified char than actors without this flag

**Class:** `Char.SetIsTargetPriority`

**Input:**
- `self: Char`
- `state: bool`

---

### `077A` SET_CHAR_RELATIONSHIP

**Class:** `Char.SetRelationship`

**Input:**
- `self: Char`
- `relationshipType: RelationshipType`
- `pedType: PedType`

---

### `077B` CLEAR_CHAR_RELATIONSHIP

**Class:** `Char.ClearRelationship`

**Input:**
- `self: Char`
- `relationshipType: RelationshipType`
- `toPedType: PedType`

---

### `077C` CLEAR_ALL_CHAR_RELATIONSHIPS

**Class:** `Char.ClearAllRelationships`

**Input:**
- `self: Char`
- `relationshipType: RelationshipType`

---

### `0792` CLEAR_CHAR_TASKS_IMMEDIATELY
Clears all the characters tasks immediately, resetting the character to an idle state

**Class:** `Char.ClearTasksImmediately`

**Input:**
- `self: Char`

---

### `07A0` PERFORM_SEQUENCE_TASK_FROM_PROGRESS

**Class:** `Char.PerformSequenceFromProgress`

**Input:**
- `self: Char`
- `sequence: Sequence`
- `startTaskIndex: int`
- `endTaskIndex: int`

---

### `07A1` SET_NEXT_DESIRED_MOVE_STATE
Sets how the character chooses to go to their destination in the next task without a parameter specifying this

**Class:** `Char.SetNextDesiredMoveState`
**Flags:** static

**Input:**
- `moveState: MoveState`

---

### `07A4` GET_SEQUENCE_PROGRESS_RECURSIVE

**Class:** `Char.GetSequenceProgressRecursive`

**Input:**
- `self: Char`

**Output:**
- `_p2: int (variable)`
- `_p3: int (variable)`

---

### `07A9` IS_CHAR_IN_ANY_SEARCHLIGHT
Returns the handle for the searchlight that's targeting the character

**Class:** `Char.IsInAnySearchlight`
**Flags:** condition

**Input:**
- `self: Char`

**Output:**
- `handle: Searchlight (variable)`

---

### `07CB` LISTEN_TO_PLAYER_GROUP_COMMANDS

**Class:** `Char.ListenToPlayerGroupCommands`

**Input:**
- `self: Char`
- `state: bool`

---

### `07DD` SET_CHAR_SHOOT_RATE
Sets the attack rate of the char

**Class:** `Char.SetShootRate`

**Input:**
- `self: Char`
- `rate: int`

---

### `07FE` GIVE_MELEE_ATTACK_TO_CHAR
Sets the specified characters fighting style and moves

**Class:** `Char.GiveMeleeAttack`

**Input:**
- `self: Char`
- `style: FightStyle`
- `move: FightMoves`

---

### `080E` GET_CHAR_HIGHEST_PRIORITY_EVENT
Gets the characters active ped event

**Class:** `Char.GetHighestPriorityEvent`

**Input:**
- `self: Char`

**Output:**
- `event: Event (variable)`

**Details:**

The event is only available for one frame. To capture it, use `wait 0`.

This command always returns `0` in CLEO Redux (a known issue).

---

### `0811` GET_CAR_CHAR_IS_USING
Stores a handle for the vehicle the character is in or entering (alts: 00D9,03C0,0484)

**Class:** `Char.GetCarIsUsing`

**Input:**
- `self: Char`

**Output:**
- `handle: Car (variable)`

---

### `0816` SET_CHAR_KINDA_STAY_IN_SAME_PLACE
Sets whether the character shouldn't chase their victim far (to attempt a melee attack or get in weapon range)

**Class:** `Char.SetKindaStayInSamePlace`

**Input:**
- `self: Char`
- `state: bool`

---

### `0818` IS_CHAR_IN_AIR
Returns true if the character is in the air

**Class:** `Char.IsInAir`
**Flags:** condition

**Input:**
- `self: Char`

---

### `0819` GET_CHAR_HEIGHT_ABOVE_GROUND
Returns the char's distance from ground

**Class:** `Char.GetHeightAboveGround`

**Input:**
- `self: Char`

**Output:**
- `height: float (variable)`

---

### `081A` SET_CHAR_WEAPON_SKILL
Sets the character's fire arms wielding style

**Class:** `Char.SetWeaponSkill`

**Input:**
- `self: Char`
- `skill: WeaponSkill`

---

### `083C` SET_CHAR_VELOCITY
Sets the characters velocity

**Class:** `Char.SetVelocity`

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `z: float`

---

### `083D` GET_CHAR_VELOCITY
Gets the characters velocity

**Class:** `Char.GetVelocity`

**Input:**
- `self: Char`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `083E` SET_CHAR_ROTATION
Sets the characters rotation

**Class:** `Char.SetRotation`

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `z: float`

---

### `0851` DAMAGE_CHAR
Decreases the characters health

**Class:** `Char.Damage`

**Input:**
- `self: Char`
- `amount: int`
- `damageArmour: bool`

---

### `0856` SET_CHAR_ALLOWED_TO_DUCK
Sets whether the character can crouch

**Class:** `Char.SetAllowedToDuck`

**Input:**
- `self: Char`
- `state: bool`

---

### `0860` SET_CHAR_AREA_VISIBLE
Sets the interior that the char is in

**Class:** `Char.SetAreaVisible`

**Input:**
- `self: Char`
- `areaId: int`

**Details:**

This command sets the interior of the character. This is required when creating the character inside an interior or moving the character to another interior with a different number or else the character will become non-solid.

---

### `087E` SET_CHAR_DROPS_WEAPONS_WHEN_DEAD
Sets whether the character will drop any of their weapons when they die

**Class:** `Char.SetDropsWeaponsWhenDead`

**Input:**
- `self: Char`
- `state: bool`

---

### `087F` SET_CHAR_NEVER_LEAVES_GROUP
Prevents the character from leaving their group

**Class:** `Char.SetNeverLeavesGroup`

**Input:**
- `self: Char`
- `state: bool`

---

### `0887` SET_HEADING_LIMIT_FOR_ATTACHED_CHAR
Sets the heading limit for a character attached to an object or vehicle

**Class:** `Char.SetHeadingLimitForAttached`

**Input:**
- `self: Char`
- `heading: Facing`
- `headingRange: float`

---

### `0889` GET_DEAD_CHAR_COORDINATES

**Class:** `Char.GetCoordinatesOfDied`

**Input:**
- `self: Char`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `089F` GET_PED_TYPE
Gets the ped type of the character

**Class:** `Char.GetPedType`

**Input:**
- `self: Char`

**Output:**
- `pedType: PedType (variable)`

---

### `08AD` SET_CHAR_HAS_USED_ENTRY_EXIT
Locates the entry/exit marker in the specified radius of the specified coordinates and links it to the character, also setting the appropriate interior ID for the character and setting the appropriate sky color if the character is player-controlled

**Class:** `Char.SetHasUsedEntryExit`

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `radius: float`

---

### `08AF` SET_CHAR_MAX_HEALTH
Sets the characters max health

**Class:** `Char.SetMaxHealth`

**Input:**
- `self: Char`
- `maxHealth: int`

---

### `08C6` SET_CHAR_CAN_BE_KNOCKED_OFF_BIKE
Sets whether the character always stays on bike in collisions

**Class:** `Char.SetCanBeKnockedOffBike`

**Input:**
- `self: Char`
- `stayOnBike: bool`

---

### `08C7` SET_CHAR_COORDINATES_DONT_WARP_GANG
Sets the character's coordinates without warping the rest of their group

**Class:** `Char.SetCoordinatesDontWarpGang`

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `z: float`

---

### `093B` SET_CHAR_BULLETPROOF_VEST
Specifies that the character should only use upper-body damage animations, meaning they can still run if shot in the legs etc

**Class:** `Char.SetBulletproofVest`

**Input:**
- `self: Char`
- `state: bool`

---

### `0946` SET_CHAR_USES_UPPERBODY_DAMAGE_ANIMS_ONLY

**Class:** `Char.SetUsesUpperbodyDamageAnimsOnly`

**Input:**
- `self: Char`
- `state: bool`

---

### `0947` SET_CHAR_SAY_CONTEXT
Works similar to 05C1, but returns which phrase was spoken and is not run as a task

**Class:** `Char.SetSayContext`

**Input:**
- `self: Char`
- `phrase: SpeechId`

**Output:**
- `_p3: int (variable)`

---

### `094B` GET_NAME_OF_ENTRY_EXIT_CHAR_USED
Gets the name of the characters interior

**Class:** `Char.GetNameOfEntryExitUsed`

**Input:**
- `self: Char`

**Output:**
- `interiorName: string (variable)`

---

### `094C` GET_POSITION_OF_ENTRY_EXIT_CHAR_USED
Returns the coordinates and heading of the entry (enex) marker the character used to get to the current interior

**Class:** `Char.GetPositionOfEntryExitCharUsed`

**Input:**
- `self: Char`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`
- `heading: float (variable)`

---

### `094D` IS_CHAR_TALKING
Returns true if the character is playing any speech

**Class:** `Char.IsTalking`
**Flags:** condition

**Input:**
- `self: Char`

---

### `094E` DISABLE_CHAR_SPEECH
Prevents any character speech from playing

**Class:** `Char.DisableSpeech`

**Input:**
- `self: Char`
- `stopNow: bool`

---

### `094F` ENABLE_CHAR_SPEECH
Enables pain audio if it was disabled using 094E

**Class:** `Char.EnableSpeech`

**Input:**
- `self: Char`

---

### `095D` IS_CHAR_STUCK_UNDER_CAR
Returns true if the char is stuck under a car

**Class:** `Char.IsStuckUnderCar`
**Flags:** condition

**Input:**
- `self: Char`

---

### `0961` SET_CHAR_KEEP_TASK
Sets whether the character should keep their tasks after mission cleanup (basically cleanup will be skipped for this character)

**Class:** `Char.SetKeepTask`

**Input:**
- `self: Char`
- `state: bool`

---

### `0965` IS_CHAR_SWIMMING

**Class:** `Char.IsSwimming`
**Flags:** condition

**Input:**
- `self: Char`

---

### `0966` GET_CHAR_SWIM_STATE

**Class:** `Char.GetSwimState`

**Input:**
- `self: Char`

**Output:**
- `state: SwimState (variable)`

---

### `0967` START_CHAR_FACIAL_TALK
Makes a character move their mouth as if they were talking

**Class:** `Char.StartFacialTalk`

**Input:**
- `self: Char`
- `duration: int`

---

### `0968` STOP_CHAR_FACIAL_TALK
Stops the character moving their mouth as if they were talking

**Class:** `Char.StopFacialTalk`

**Input:**
- `self: Char`

---

### `0972` SET_CHAR_COORDINATES_NO_OFFSET
Puts the characters at the coordinates by the center of body instead of the feet

**Class:** `Char.SetCoordinatesNoOffset`

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `z: float`

---

### `0982` SET_CHAR_FORCE_DIE_IN_CAR
Makes a character remain in the car upon death

**Class:** `Char.SetForceDieInCar`

**Input:**
- `self: Char`
- `state: bool`

---

### `09A1` DROP_SECOND_OBJECT

**Class:** `Char.DropSecondObject`

**Input:**
- `self: Char`
- `state: bool`

---

### `09A7` SET_CHAR_DRUGGED_UP

**Class:** `Char.SetDruggedUp`

**Input:**
- `self: Char`
- `state: bool`

---

### `09A8` IS_CHAR_HEAD_MISSING
Returns true if the character has had its head shot off

**Class:** `Char.IsHeadMissing`
**Flags:** condition

**Input:**
- `self: Char`

---

### `09AE` IS_CHAR_IN_ANY_TRAIN
Returns true if the specified character is in a train

**Class:** `Char.IsInAnyTrain`
**Flags:** condition

**Input:**
- `self: Char`

---

### `09B5` SET_CHAR_SIGNAL_AFTER_KILL
Sets whether the character signals after killing

**Class:** `Char.SetSignalAfterKill`

**Input:**
- `self: Char`
- `state: bool`

---

### `09B6` SET_CHAR_WANTED_BY_POLICE
Sets whether police should chase the character

**Class:** `Char.SetWantedByPolice`

**Input:**
- `self: Char`
- `state: bool`

---

### `09BC` SET_CHAR_COORDINATES_DONT_WARP_GANG_NO_OFFSET
This command is a combination of 0972 and 08C7

**Class:** `Char.SetCoordinatesDontWarpGangNoOffset`

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `z: float`

---

### `09C5` IS_CHAR_USING_MAP_ATTRACTOR
Returns true if the character is using a map attractor

**Class:** `Char.IsUsingMapAttractor`
**Flags:** condition

**Input:**
- `self: Char`

---

### `09C9` REMOVE_CHAR_FROM_CAR_MAINTAIN_POSITION
Removes the character from the vehicle

**Class:** `Char.RemoveFromCarMaintainPosition`

**Input:**
- `self: Char`
- `vehicle: Car`

---

### `09D5` SET_CHAR_SAY_CONTEXT_IMPORTANT

**Class:** `Char.SetSayContextImportant`

**Input:**
- `self: Char`
- `phrase: SpeechId`
- `overrideSilence: bool`
- `ignoreMute: bool`
- `frontEnd: bool`

**Output:**
- `saidVariant: int (variable)`

---

### `09D6` SET_CHAR_SAY_SCRIPT

**Class:** `Char.SetSayScript`

**Input:**
- `self: Char`
- `_p2: int`
- `_p3: bool`
- `_p4: bool`
- `_p5: bool`

---

### `09DE` IS_CHAR_GETTING_IN_TO_A_CAR
Returns true if the character is entering a car, but is not in the car

**Class:** `Char.IsGettingInToACar`
**Flags:** condition

**Input:**
- `self: Char`

---

### `09E8` GET_CHAR_AREA_VISIBLE
Returns the interior ID that the character is in

**Class:** `Char.GetAreaVisible`

**Input:**
- `self: Char`

**Output:**
- `areaId: int (variable)`

---

### `09ED` HAS_CHAR_SPOTTED_CHAR_IN_FRONT
Returns true if the character can see the other character in front of them

**Class:** `Char.HasSpottedCharInFront`
**Flags:** condition

**Input:**
- `self: Char`
- `handle: Char`

---

### `09F4` IGNORE_HEIGHT_DIFFERENCE_FOLLOWING_NODES

**Class:** `Char.IgnoreHeightDifferenceFollowingNodes`

**Input:**
- `self: Char`
- `state: bool`

---

### `09F6` SET_CHAR_GET_OUT_UPSIDE_DOWN_CAR
Controls whether the character will try to exit an upside-down car until it is on fire

**Class:** `Char.SetGetOutUpsideDownCar`

**Input:**
- `self: Char`
- `state: bool`

---

### `0A09` SHUT_CHAR_UP_FOR_SCRIPTED_SPEECH
Works similar to 0489, but mutes more things, including ambient speeches (needs confirming)

**Class:** `Char.ShutUpForScriptedSpeech`

**Input:**
- `self: Char`
- `state: bool`

---

### `0A1B` IS_CHAR_TOUCHING_CHAR
Returns true if the character is touching the other character

**Class:** `Char.IsTouchingChar`
**Flags:** condition

**Input:**
- `self: Char`
- `other: Char`

---

### `0A27` SET_DEATH_WEAPONS_PERSIST
Prevents pickups, which are created when this character dies, from disappearing until picked up by the player

**Class:** `Char.SetDeathWeaponsPersist`

**Input:**
- `self: Char`
- `state: bool`

---

### `0A28` SET_SWIM_SPEED
Sets the speed that the character swims at, changing their swimming animation speed

**Class:** `Char.SetSwimSpeed`

**Input:**
- `self: Char`
- `speed: float`

---

### `0A32` IS_CHAR_ATTACHED_TO_ANY_CAR
Returns true if the char is turreted on any vehicle

**Class:** `Char.IsAttachedToAnyCar`
**Flags:** condition

**Input:**
- `self: Char`

---

### `0A33` STORE_CAR_CHAR_IS_ATTACHED_TO_NO_SAVE
Returns the vehicle the character is attached to

**Class:** `Char.StoreCarIsAttachedToNoSave`

**Input:**
- `self: Char`

**Output:**
- `handle: Car (variable)`

---
