# CLEO+ Extension Opcodes

> 318 opcodes

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0B20` | READ_CLIPBOARD_DATA | Copies the specified number of bytes of text from the clipboard to the address |
| `0B21` | WRITE_CLIPBOARD_DATA |  |
| `0D01` | ROTATE_MATRIX_ON_AXIS |  |
| `0D02` | GET_MATRIX_X_ANGLE |  |
| `0D03` | GET_MATRIX_Y_ANGLE |  |
| `0D04` | GET_MATRIX_Z_ANGLE |  |
| `0D0A` | GET_OFFSET_FROM_MATRIX_IN_WORLD_COORDS |  |
| `0D0B` | GET_CHAR_BONE_MATRIX | Returns the address of the character's specified bone matrix |
| `0D0F` | SET_CAR_MODEL_ALPHA | Set's the specified car's transparency alpha |
| `0D10` | SET_CHAR_MODEL_ALPHA | Set's the specified character's transparency alpha |
| `0D11` | SET_OBJECT_MODEL_ALPHA | Set's the specified object's transparency alpha |
| `0D16` | SET_MATRIX_ROTATION_FROM_QUAT |  |
| `0D17` | SET_QUAT_FROM_MATRIX |  |
| `0D18` | ROTATE_QUAT_ON_AXIS |  |
| `0D19` | GET_NORMALISED_QUAT |  |
| `0D1A` | MULTIPLY_QUATS |  |
| `0D1E` | QUAT_SLERP |  |
| `0D24` | INITIALISE_QUAT |  |
| `0D27` | COPY_MEMORY | Copies each memory byte from src address to dest address |
| `0D29` | GET_QUAT_ELEMENTS |  |
| `0D2D` | GET_LOCAL_TIME | Returns the full local time of the player's PC |
| `0D2E` | SET_SCRIPT_VAR | Sets value for script variable in index |
| `0D2F` | GET_SCRIPT_VAR | Gets value from script variable index |
| `0D30` | GET_CHAR_BONE |  |
| `0D31` | GET_BONE_OFFSET_VECTOR |  |
| `0D32` | GET_BONE_QUAT | Returns pointer to the quaterion under bone address obtained with GET_CHAR_BONE |
| `0D33` | SET_CAR_DOOR_WINDOW_STATE | Sets the window state of the specified door of the car |
| `0D37` | WRITE_STRUCT_PARAM | Writes the dword value to the struct address by index (index*4+address) see: 0E2 |
| `0D38` | READ_STRUCT_PARAM | Reads the dword value from the struct address by index (index*4+address) see: 0D |
| `0D39` | GET_CHAR_MAX_HEALTH | Returns the character's maximum health (08AF) |
| `0D3A` | GET_COLLISION_BETWEEN_POINTS | Returns the colPoint, coordinates, and collision entity between two points |
| `0D3B` | GET_COLPOINT_NORMAL_VECTOR | Returns the vector of the specified ColPoint |
| `0D3C` | GET_COLPOINT_SURFACE | Returns the surfaceType of the specified ColPoint |
| `0D3E` | GET_COLPOINT_DEPTH | Returns the depth of the specified ColPoint |
| `0D4C` | GET_STRING_LENGTH | Returns the string length |
| `0D4D` | COPY_STRING | Copies the string to the specified address |
| `0D4E` | READ_STRUCT_OFFSET | Reads a value from the given offset from the memory address (see: 0D38) |
| `0D59` | GET_CURRENT_WEATHER | Gets weather type that is being blended from |
| `0E00` | GET_CAR_ALARM | Returns the status of the car's alarm |
| `0E01` | CREATE_OBJECT_NO_SAVE | Creates an no save game object at the specified location, with the specified mod |
| `0E02` | SET_CAR_GENERATOR_NO_SAVE |  |
| `0E03` | PERLIN_NOISE | Calculates the 1D Perlin simplex noise |
| `0E04` | GET_NEXT_WEATHER | Gets weather type that is being blended to |
| `0E05` | SET_NEXT_WEATHER | Sets weather type which will be blend to |
| `0E06` | GET_RAIN_INTENSITY | Gets rain intensity in range of 0.0 to 1.0 |
| `0E07` | SET_RAIN_INTENSITY | Sets rain intensity in range of 0.0 to 1.0 |
| `0E08` | IS_CAR_SCRIPT_CONTROLLED | Returns true if the specified vehicle is controlled by script |
| `0E09` | MARK_CAR_AS_NEEDED | Marks the vehicle as script controlled |
| `0E0A` | IS_CHAR_SCRIPT_CONTROLLED | Returns true if the specified character is controlled by script |
| `0E0B` | MARK_CHAR_AS_NEEDED | Marks the character as script controlled |
| `0E0C` | IS_OBJECT_SCRIPT_CONTROLLED | Returns true if the specified object is controlled by a script |
| `0E0D` | MARK_OBJECT_AS_NEEDED | marks object as script controlled |
| `0E0E` | GET_CURRENT_RESOLUTION | Gets the game window width and height resolution |
| `0E0F` | GET_FIXED_XY_ASPECT_RATIO | Gets x and y values based on window aspect ratio, useful for text and hud scalin |
| `0E10` | IS_MOUSE_WHEEL_UP | Returns true if the mouse wheel has been scrolled up |
| `0E11` | IS_MOUSE_WHEEL_DOWN | Returns true if the mouse wheel has been scrolled down |
| `0E12` | GET_VEHICLE_SUBCLASS | Returns vehicle subclass, useful to check if vehicle is motorbike, bicycle, trai |
| `0E13` | GET_ENTITY_TYPE | Gets the type of the entity |
| `0E14` | INIT_EXTENDED_CHAR_VARS | Inits additional variables for this char. Identifier can be "AUTO" for unique ID |
| `0E15` | SET_EXTENDED_CHAR_VAR | Sets extended var value for this char. Requires initialization (0E14), otherwise |
| `0E16` | GET_EXTENDED_CHAR_VAR | Gets extended var value for this char. Returns false if not initialized (0E14) |
| `0E17` | INIT_EXTENDED_CAR_VARS | Inits additional variables for this car. Identifier can be "AUTO" for unique ID  |
| `0E18` | SET_EXTENDED_CAR_VAR | Sets extended var value for this car. Requires initialization (0E17), otherwise  |
| `0E19` | GET_EXTENDED_CAR_VAR | Gets extended var value for this car. Returns false if not initialized (0E17) |
| `0E1A` | INIT_EXTENDED_OBJECT_VARS | Inits additional variables for this object. Identifier can be "AUTO" for unique  |
| `0E1B` | SET_EXTENDED_OBJECT_VAR | Sets extended var value for this object. Requires initialization (0E1A), otherwi |
| `0E1C` | GET_EXTENDED_OBJECT_VAR | Gets extended var value for this char. Returns false if not initialized (0E1A) |
| `0E1D` | IS_ON_MISSION | Returns true if the player is on a mission (the variable set in 0180 is not zero |
| `0E1E` | DRAW_TEXTURE_PLUS | Draws RwTexture or spriteSlot once on specific drawing event and optional mask,  |
| `0E1F` | EASE | Eases k value in range of 0.0 to 1.0, resulting in a easing value based on mode  |
| `0E20` | IS_ON_SAMP | Returns true if the current game runs on San Andreas Multiplayer (SA-MP) |
| `0E21` | GET_AUDIO_SFX_VOLUME | Gets the SFX volume set in the game options |
| `0E22` | GET_AUDIO_RADIO_VOLUME | Gets the radio volume set in the game options |
| `0E23` | GET_MOUSE_SENSIBILITY | Gets the mouse sensibility set in the game options |
| `0E24` | FIX_CHAR_GROUND_BRIGHTNESS_AND_FADE_IN |  |
| `0E25` | IS_ON_CUTSCENE | Returns true if a cutscene is active (02E7) |
| `0E26` | IS_WEAPON_FIRE_TYPE | Checks if the weapon has the specified fire type |
| `0E27` | GET_ANGLE_FROM_TWO_COORDS |  |
| `0E28` | WRITE_STRUCT_OFFSET | Writes the value at the given offset from the memory address (see: 0D37) |
| `0E29` | PERLIN_NOISE_FRACTAL | Calculates the Fractal Brownian Motion (fBm) summation of 1D Perlin Simplex nois |
| `0E2A` | ADD_CLEO_BLIP | Creates a blip that don't saves, supports any texture, alpha and don't hits the  |
| `0E2B` | REMOVE_CLEO_BLIP | Removes a cleo blip |
| `0E2C` | GET_CURRENT_SAVE_SLOT | Gets loaded save slot number. 0 if new game |
| `0E2D` | IS_GAME_FIRST_START | Is first gameplay start (game was not reloaded) |
| `0E2E` | CREATE_RENDER_OBJECT_TO_CHAR_BONE | Creates renderObject to character bone |
| `0E2F` | DELETE_RENDER_OBJECT | Deletes the renderObject |
| `0E30` | SET_RENDER_OBJECT_AUTO_HIDE | Sets the renderObject to AutoHide if the character is dead, is using a weapon, o |
| `0E31` | SET_RENDER_OBJECT_VISIBLE | Sets the visible status of the renderObject |
| `0E32` | SET_CHAR_COORDINATES_SIMPLE | Sets the character's coordinates without exception protocols |
| `0E33` | GET_PICKUP_THIS_COORD | Returns the handle of a pickup at the specified coordinates |
| `0E34` | GET_PICKUP_MODEL | Returns the model of a specified pickup |
| `0E35` | SET_RENDER_OBJECT_POSITION | Sets the position of a renderObject |
| `0E36` | SET_RENDER_OBJECT_ROTATION | Sets the rotation of the renderObject |
| `0E37` | SET_RENDER_OBJECT_SCALE | Sets the scale of the renderObject |
| `0E38` | GET_PICKUP_POINTER | Returns a pointer to the struct of a specified pickup |
| `0E39` | GET_PICKUP_TYPE | Returns the type of a specified pickup |
| `0E3A` | SET_RENDER_OBJECT_DISTORTION | Sets the renderObject's distortion |
| `0E3B` | GET_AUDIOSTREAM_INTERNAL | Returns the internal reference of a given AUDIOSTREAM to be used in bass.dll fun |
| `0E3C` | GET_TEXTURE_FROM_SPRITE | Returns the rwTexture pointer from sprite index |
| `0E3D` | IS_KEY_JUST_PRESSED | Returns true if the player has just started to press a specified key this frame |
| `0E3E` | IS_BUTTON_JUST_PRESSED | Returns true if the pad's button has just started to be pressed this frame |
| `0E3F` | CONVERT_3D_TO_SCREEN_2D | Returns 2D screen position and distance related text size for world coordinates  |
| `0E40` | GET_CURRENT_HOUR | Returns the clock's current hour |
| `0E41` | GET_CURRENT_MINUTE | Returns the clock's current minute |
| `0E42` | IS_CHAR_DOING_TASK_ID | Returns true if the character is performing the specified task |
| `0E43` | GET_CHAR_TASK_POINTER_BY_ID | Returns the address of the character's task by taskId |
| `0E44` | GET_CHAR_KILL_TARGET_CHAR | Returns the handle of the killTarget of the specified character |
| `0E45` | FRAME_MOD | Returns True every mod number of frames |
| `0E46` | IS_CHAR_USING_GUN | Returns true if the specified character is using a gun |
| `0E47` | IS_CHAR_FIGHTING | Returns true if the specified character is fighting |
| `0E48` | IS_CHAR_FALLEN_ON_GROUND | Returns true if the specified character has fallen on the ground |
| `0E49` | IS_CHAR_ENTERING_ANY_CAR | Returns true if the specified character is entering any car |
| `0E4A` | IS_CHAR_EXITING_ANY_CAR | Returns true if the specified character is exiting any car |
| `0E4B` | IS_CHAR_PLAYING_ANY_SCRIPT_ANIMATION | Returns true if the specified character is playing any script animation |
| `0E4C` | IS_CHAR_DOING_ANY_IMPORTANT_TASK | Returns true if the specified character is doing any important task |
| `0E4D` | RANDOM_PERCENT | Returns randomly True the specified percent of the time |
| `0E4E` | DISPLAY_ONSCREEN_TIMER_LOCAL | Creates a countdown or countup onscreen timer |
| `0E4F` | DISPLAY_ONSCREEN_TIMER_WITH_STRING_LOCAL | Creates a countdown or countup onscreen timer with the text |
| `0E50` | DISPLAY_ONSCREEN_COUNTER_LOCAL | Displays an onscreen counter, either shown in numbers or as a bar |
| `0E51` | DISPLAY_ONSCREEN_COUNTER_WITH_STRING_LOCAL | Displays an onscreen counter with the text, either shown in numbers or as a bar |
| `0E52` | DISPLAY_TWO_ONSCREEN_COUNTERS_LOCAL | Displays two onscreen counters separated by a slash |
| `0E53` | DISPLAY_TWO_ONSCREEN_COUNTERS_WITH_STRING_LOCAL | Displays two onscreen counters separated by a slash with the text |
| `0E54` | CLEAR_ONSCREEN_TIMER_LOCAL | Removes the local onscreen timer |
| `0E55` | CLEAR_ONSCREEN_COUNTER_LOCAL | Removes the local onscreen counter |
| `0E56` | SET_ONSCREEN_COUNTER_FLASH_WHEN_FIRST_DISPLAYED_LOCAL | Sets the local counter to flash when first displayed |
| `0E57` | SET_TIMER_BEEP_COUNTDOWN_TIME_LOCAL | Starts a sound when the countdown timer reaches the specified number of seconds |
| `0E58` | SET_ONSCREEN_COUNTER_COLOUR_LOCAL | Sets the color of the specified local counter |
| `0E59` | GET_TRAILER_FROM_CAR | Returns the handle of a trailer towed by this car |
| `0E5A` | GET_CAR_FROM_TRAILER | Returns the handle of a tractor towing this car |
| `0E5B` | GET_CAR_DUMMY_COORD | Returns the coordinates of the specified car's vehicleDummy |
| `0E5C` | GET_CHAR_HEALTH_PERCENT | Returns the character's health as a floating-point percentage |
| `0E5D` | IS_CHEAT_ACTIVE | Returns True if the specified cheat is togglable and active |
| `0E5E` | CHANGE_PLAYER_MONEY | Changes player money by set, add or remove |
| `0E5F` | CAR_HORN | Plays the car's horn (if the player is driving the car) |
| `0E60` | SET_CAMERA_CONTROL | Enables rotational control of the camera |
| `0E61` | SET_CAR_ALARM | Sets the status of the car's alarm |
| `0E62` | DRAW_STRING | Draws string once on specific drawing event |
| `0E63` | DRAW_STRING_EXT | Draws string once on specific drawing event with extended text styling |
| `0E64` | GET_CURRENT_CAMERA_MODE | Returns the current camera mode |
| `0E65` | GET_CAR_COLLISION_INTENSITY | Returns the intensity of the last collision of the specified car |
| `0E66` | GET_CAR_COLLISION_COORDINATES | Returns the coordinates of the last collision of the specified car |
| `0E67` | IS_AIM_BUTTON_PRESSED | Returns True if the pad's aim button is pressed |
| `0E68` | SET_PLAYER_CONTROL_PAD | Enables the specified control pad |
| `0E69` | SET_PLAYER_CONTROL_PAD_MOVEMENT | Enables the specified control pad's movement |
| `0E6A` | MAKE_NOP | Fills memory address with 0x90 with given size |
| `0E6B` | GET_COLPOINT_LIGHTING | Returns the lighting of the specified ColPoint |
| `0E6C` | GET_DAY_NIGHT_BALANCE | Returns the intensity of the night filter |
| `0E6D` | GET_UNDERWATERNESS | Returns the intensity of the underwater filter |
| `0E6E` | IS_SELECT_MENU_JUST_PRESSED | Returns True if menu Select was just pressed |
| `0E6F` | STREAM_CUSTOM_SCRIPT_FROM_LABEL | Loads a custom script at the specified label |
| `0E70` | GET_LAST_CREATED_CUSTOM_SCRIPT | Gets the address of the last created custom script |
| `0E71` | GET_OBJECT_CENTRE_OF_MASS_TO_BASE_OF_MODEL | Gets the distance between the object model's center of mass to its base |
| `0E72` | CREATE_LIST | Creates a list of the specified type |
| `0E73` | DELETE_LIST | Deletes the specified list |
| `0E74` | LIST_ADD | Adds a numerical value to the specified list |
| `0E75` | LIST_REMOVE_VALUE | Removes a numerical value from the specified list |
| `0E76` | LIST_REMOVE_INDEX | Removes an entry from the specified list by index |
| `0E77` | GET_LIST_SIZE | Returns the number of entries in the specified list |
| `0E78` | GET_LIST_VALUE_BY_INDEX | Returns a numerical value from the specified list by index |
| `0E79` | RESET_LIST | Resets all entries within the specified list |
| `0E7A` | GET_LIST_STRING_VALUE_BY_INDEX | Returns a string value from the specified list by index |
| `0E7B` | LIST_ADD_STRING | Adds a string value to the specified list |
| `0E7C` | LIST_REMOVE_STRING_VALUE | Removes a string value from the specified list |
| `0E7D` | LIST_REMOVE_INDEX_RANGE | Removes entries from the specified list by index range |
| `0E7E` | REVERSE_LIST | Reverses the order of entries within the specified list |
| `0E7F` | GET_MODEL_TYPE | Returns the type of the specified model |
| `0E80` | IS_STRING_EQUAL | Returns True if string1 and string2 match |
| `0E81` | IS_STRING_COMMENT | Returns True if the string starts with a hash (#), semicolon (;) or double slash |
| `0E82` | DOES_CAR_HAVE_PART_NODE | Returns True if the car has the specified carNode part |
| `0E83` | GET_CURRENT_CHAR_WEAPONINFO | Returns a pointer to the character's current weaponInfo struct |
| `0E84` | GET_WEAPONINFO | Returns a pointer to the CWeaponInfo struct of the the specified weaponType and  |
| `0E85` | GET_WEAPONINFO_MODELS | Returns the model1 and model2 of the current weaponInfo struct |
| `0E86` | GET_WEAPONINFO_FLAGS | Returns the flags of the specified WeaponInfo struct |
| `0E87` | GET_WEAPONINFO_ANIMGROUP | Returns the FireType of the current weaponInfo struct |
| `0E88` | GET_WEAPONINFO_TOTAL_CLIP | Returns the totalClip size for the current weaponInfo struct |
| `0E89` | GET_WEAPONINFO_FIRE_TYPE | Returns the FireType of the current weaponInfo struct |
| `0E8A` | GET_WEAPONINFO_SLOT | Returns the weaponSlot of the current weaponInfo struct |
| `0E8B` | GET_CHAR_WEAPON_STATE | Returns the character's current weaponState |
| `0E8C` | GET_CHAR_WEAPON_CLIP | Returns the character's current WeaponClip |
| `0E8D` | IS_ANY_FIRE_BUTTON_PRESSED | Returns True if the pad's primary or secondary fire button is pressed |
| `0E8E` | GET_CHAR_COLLISION_SURFACE | Returns the specified character's collision surfaceType |
| `0E8F` | GET_CHAR_COLLISION_LIGHTING | Returns the specified character's collision lighting |
| `0E90` | GET_CAR_COLLISION_SURFACE | Returns the specified car's collision surfaceType |
| `0E91` | GET_CAR_COLLISION_LIGHTING | Returns the specified car's collision lighting |
| `0E92` | IS_CHAR_REALLY_IN_AIR | Returns True when the character is really in air, including while using a parach |
| `0E93` | IS_CAR_REALLY_IN_AIR | Returns True if the specified car is really in the air, and False for boats floa |
| `0E94` | IS_OBJECT_REALLY_IN_AIR | Returns True if the specified object is not on a solid surface and not submerged |
| `0E95` | SIMULATE_OBJECT_DAMAGE | Simulates the specified damage amount and weaponType on the object |
| `0E96` | CLEAR_CHAR_PRIMARY_TASKS | Clears the specified character's primary tasks |
| `0E97` | CLEAR_CHAR_SECONDARY_TASKS | Clears the character's secondary tasks |
| `0E98` | REQUEST_PRIORITY_MODEL | Requests a priority modelID to be loaded |
| `0E99` | LOAD_ALL_PRIORITY_MODELS_NOW | This is a duplicate of LOAD_ALL_MODELS_NOW |
| `0E9A` | LOAD_SPECIAL_CHARACTER_FOR_ID |  |
| `0E9B` | UNLOAD_SPECIAL_CHARACTER_FROM_ID |  |
| `0E9C` | GET_MODEL_BY_NAME | Returns the modelID by name |
| `0E9D` | IS_MODEL_AVAILABLE_BY_NAME | Returns true if the specified model name is available as a valid special charact |
| `0E9E` | GET_MODEL_DOESNT_EXIST_IN_RANGE |  |
| `0E9F` | REMOVE_ALL_UNUSED_MODELS |  |
| `0EA0` | SET_CHAR_SECOND_PLAYER | Sets this char as controlled by player two |
| `0EA1` | DISABLE_SECOND_PLAYER |  |
| `0EA2` | FIX_TWO_PLAYERS_SEPARATED_CARS | Enables fixes for making two players use separated cars |
| `0EA3` | REMOVE_MODEL_IF_UNUSED | Removes the specified ModelID from memory if unused |
| `0EA4` | IS_CHAR_ON_FIRE | Returns True if the character is on fire |
| `0EA5` | GET_CLOSEST_COP_NEAR_CHAR | Returns the handle of the closestCop to the specified character |
| `0EA6` | GET_CLOSEST_COP_NEAR_POS | Returns the closestCop to the specified coordinates |
| `0EA7` | GET_ANY_CHAR_NO_SAVE_RECURSIVE | Returns the handle of anyChar in the pool, starting at the previously returned p |
| `0EA8` | GET_ANY_CAR_NO_SAVE_RECURSIVE | Returns the handle of anyCar in the pool, starting at the previously returned pr |
| `0EA9` | GET_ANY_OBJECT_NO_SAVE_RECURSIVE | Returns the handle of anyObject in the pool, starting at the previously returned |
| `0EAA` | SET_CHAR_ARRESTED | Sets the specified character's pedState to Arrested |
| `0EAB` | GET_CHAR_PEDSTATE | Returns the specified character's pedState |
| `0EAC` | GET_CHAR_PROOFS | Returns the specified character's damage proofs |
| `0EAD` | GET_CAR_PROOFS | Returns the specified car's damage proofs |
| `0EAE` | GET_OBJECT_PROOFS | Returns the specified object's damage proofs |
| `0EAF` | IS_CHAR_WEAPON_VISIBLE_SET | Returns true if the specified character has weapon visible set |
| `0EB0` | GET_FORCED_WEATHER | Returns the forced weather type |
| `0EB1` | GET_CHAR_STAT_ID | Returns the specified character's pedStat ID (data\pedstats.dat) |
| `0EB2` | GET_OFFSET_FROM_CAMERA_IN_WORLD_COORDS | Returns world coordinates for the offset from the camera |
| `0EB3` | CONVERT_DIRECTION_TO_QUAT |  |
| `0EB4` | SET_CAR_COORDINATES_SIMPLE | Sets the specified car's coordinates without exception protocols |
| `0EB5` | GET_CHAR_DAMAGE_LAST_FRAME | Returns the character's damaging entity and weaponType, bodyPart damaged, and in |
| `0EB6` | GET_CAR_WEAPON_DAMAGE_LAST_FRAME | Gets car damage by weapon last frame. Char can be invalid, and returns false if  |
| `0EB7` | IS_ON_SCRIPTED_CUTSCENE | Checks if is playing scripted mission cutscene, that is, original widescreen bor |
| `0EB8` | IS_RADAR_VISIBLE |  |
| `0EB9` | IS_HUD_VISIBLE |  |
| `0EBA` | GET_MODEL_PED_TYPE_AND_STAT | Returns the pedType and pedStat ID for the specified modelID |
| `0EBB` | PASS_TIME | Simulates the passage of time on the clock, calendar and environment |
| `0EBC` | GENERATE_RANDOM_INT_IN_RANGE_WITH_SEED | Generates a randomInteger from min to < max with seed |
| `0EBD` | GENERATE_RANDOM_FLOAT_IN_RANGE_WITH_SEED | Generates a randomFloat from min to < max with seed |
| `0EBE` | LOCATE_CAMERA_DISTANCE_TO_COORDINATES | Returns True if the camera is located within the specified radius of the coordin |
| `0EBF` | GET_FX_SYSTEM_POINTER | Returns the address of the specified FX system associated with the given particl |
| `0EC0` | ADD_FX_SYSTEM_PARTICLE | Adds an FX system particle |
| `0EC1` | IS_FX_SYSTEM_AVAILABLE_WITH_NAME | Returns True if an FX system with the specified name is available |
| `0EC2` | SET_STRING_UPPER | Sets the string at the specified address to all upper case |
| `0EC3` | SET_STRING_LOWER | Sets the string at the specified address to all lower case |
| `0EC4` | STRING_FIND | Returns the character index where strFind is found within stringOrigin |
| `0EC5` | CUT_STRING_AT | Cuts stringAddress at the specified character index |
| `0EC6` | IS_STRING_CHARACTER_AT | Returns True if the specified characters are found at the index of the string |
| `0EC7` | GET_FADE_ALPHA | Returns the current alpha of the fade being performed ( < 255.0 max ) |
| `0EC8` | GET_CHAR_RANDOM_SEED | Returns the randomSeed of the specified character |
| `0EC9` | GET_CAR_RANDOM_SEED | Returns the randomSeed of the specified car |
| `0ECA` | GET_OBJECT_RANDOM_SEED | Returns the randomSeed of the specified object |
| `0ECB` | GET_CHAR_MOVE_STATE |  |
| `0ECC` | DONT_DELETE_CHAR_UNTIL_TIME | Prevents the deletion of the specified character until MsFromNow |
| `0ECD` | DONT_DELETE_CAR_UNTIL_TIME | Prevents the deletion of the specified car until MsFromNow |
| `0ECE` | GET_TIME_CHAR_IS_DEAD | Returns the TimeIsDead in milliseconds since the specified character is dead |
| `0ECF` | GET_TIME_CAR_IS_DEAD | Returns the TimeIsDead in milliseconds since the specified car is dead |
| `0ED0` | RETURN_SCRIPT_EVENT | Returns from script event |
| `0ED1` | SET_SCRIPT_EVENT_SAVE_CONFIRMATION | Toggles script event during save, just before the game is saved |
| `0ED2` | SET_SCRIPT_EVENT_CHAR_DELETE | Toggles script event just after varChar is deleted |
| `0ED3` | SET_SCRIPT_EVENT_CHAR_CREATE | Toggles script event just after varChar is created |
| `0ED4` | SET_SCRIPT_EVENT_CAR_DELETE | Toggles script event just before some car is being deleted |
| `0ED5` | SET_SCRIPT_EVENT_CAR_CREATE | Toggles script event just after some car is created |
| `0ED6` | SET_SCRIPT_EVENT_OBJECT_DELETE | Toggles script event just before some object is being deleted |
| `0ED7` | SET_SCRIPT_EVENT_OBJECT_CREATE | Toggles script event just after some object is created |
| `0ED8` | SET_SCRIPT_EVENT_ON_MENU | Toggles script event to run during pause menu, or when just paused the game |
| `0ED9` | SET_CHAR_IGNORE_DAMAGE_ANIMS |  |
| `0EDA` | SET_SCRIPT_EVENT_CHAR_PROCESS | Toggles script event to run on each char once per frame |
| `0EDB` | SET_SCRIPT_EVENT_CAR_PROCESS | Toggles script event to run on each car once per frame |
| `0EDC` | SET_SCRIPT_EVENT_OBJECT_PROCESS | Toggles script event to run on each object once per frame. May be slow |
| `0EDD` | SET_SCRIPT_EVENT_BUILDING_PROCESS | Toggles script event to run on each building (CBuilding/Entity) once per frame.  |
| `0EDE` | SET_SCRIPT_EVENT_CHAR_DAMAGE | Toggles script event when some char receives any damage. Use 0EB5 to get damage  |
| `0EDF` | SET_SCRIPT_EVENT_CAR_WEAPON_DAMAGE | Toggles script event to run when some car is damaged by weapon. Use 0EB6 to get  |
| `0EE0` | SET_SCRIPT_EVENT_BULLET_IMPACT | Toggles script event to run when bullet impact. Char and entity can be invalid |
| `0EE1` | GET_COLPOINT_COORDINATES | Returns the coordinates of the specified ColPoint |
| `0EE2` | READ_STRUCT_OFFSET_MULTI | Reads a value from the given offset from the memory address multiple times as ar |
| `0EE3` | WRITE_STRUCT_OFFSET_MULTI | Writes the value at the given offset from the memory address multiple times as a |
| `0EE4` | LOCATE_CHAR_DISTANCE_TO_CHAR | Returns True if the character(self) is within the radius of the specified charac |
| `0EE5` | LOCATE_CHAR_DISTANCE_TO_CAR | Returns True if the character is within the radius of the specified car |
| `0EE6` | LOCATE_CHAR_DISTANCE_TO_OBJECT | Returns True if the character is within the radius of the specified object |
| `0EE7` | LOCATE_CAR_DISTANCE_TO_OBJECT | Returns True if the car is within the radius of the specified object |
| `0EE8` | LOCATE_CAR_DISTANCE_TO_CAR | Returns True if the car(self) is within the radius of the specified car |
| `0EE9` | LOCATE_OBJECT_DISTANCE_TO_OBJECT | Returns True if the object(self) is within the radius of the specified object |
| `0EEA` | LOCATE_CHAR_DISTANCE_TO_COORDINATES | Returns True if the character is within the radius of the specified coordinates |
| `0EEB` | LOCATE_CAR_DISTANCE_TO_COORDINATES | Returns True if the car is within the radius of the specified coordinates |
| `0EEC` | LOCATE_OBJECT_DISTANCE_TO_COORDINATES | Returns True if the object is within the radius of the specified coordinates |
| `0EED` | LOCATE_ENTITY_DISTANCE_TO_ENTITY | Returns True if entityB is within the radius of entityA |
| `0EEE` | GET_ENTITY_COORDINATES | Returns the coordinates of the entity at the specified address |
| `0EEF` | GET_ENTITY_HEADING | Returns the heading of the entity at the specified address |
| `0EF0` | GET_COORD_FROM_ANGLED_DISTANCE | Returns 2D coordinates for a location relative to x and y at the specified angle |
| `0EF1` | PERLIN_NOISE_FRACTAL_2D | Calculates the Fractal Brownian Motion (fBm) summation of 2D Perlin Simplex nois |
| `0EF2` | PERLIN_NOISE_FRACTAL_3D | Calculates the Fractal Brownian Motion (fBm) summation of 3D Perlin Simplex nois |
| `0EF3` | LERP |  |
| `0EF4` | CLAMP_FLOAT | Returns the clamped value of the specified float between the min and max values |
| `0EF5` | IS_CAR_OWNED_BY_PLAYER | Returns True if the specified car is owned by the player |
| `0EF6` | SET_CAR_OWNED_BY_PLAYER | Sets the specified car as OwnedByPlayer |
| `0EF7` | CLAMP_INT | Returns the clamped value of the specified integer between the min and max value |
| `0EF8` | GET_MODEL_INFO | Returns the address of the modelInfo of the specified modelId |
| `0EF9` | GET_CAR_ANIMGROUP | Returns the carAnimGroup of the specified car |
| `0EFA` | GET_CHAR_FEAR | Returns the specified character's fear level (see pedstats.dat) |
| `0EFB` | IS_CAR_CONVERTIBLE | Returns True if the specified car is a convertible |
| `0EFC` | GET_CAR_VALUE | Returns the monetary value of the car |
| `0EFD` | GET_CAR_PEDALS | Returns the value of the car's gas and brake pedals |
| `0EFE` | GET_LOADED_LIBRARY | Returns the address of a loaded dynamic-link library (DLL) |
| `0EFF` | GET_CHAR_SIMPLEST_ACTIVE_TASK | Returns the character's simplest active taskId and the address of the task |
| `0F00` | LOAD_SPECIAL_MODEL |  |
| `0F01` | REMOVE_SPECIAL_MODEL |  |
| `0F02` | CREATE_RENDER_OBJECT_TO_CHAR_BONE_FROM_SPECIAL |  |
| `0F03` | CREATE_RENDER_OBJECT_TO_OBJECT |  |
| `0F04` | CREATE_RENDER_OBJECT_TO_OBJECT_FROM_SPECIAL |  |
| `0F05` | GET_SPECIAL_MODEL_DATA |  |
| `0F06` | REPLACE_LIST_VALUE_BY_INDEX | Replaces a value on a list by index |
| `0F07` | REPLACE_LIST_STRING_VALUE_BY_INDEX | Replaces a string value on a list by index |
| `0F08` | INSERT_LIST_VALUE_BY_INDEX | Inserts a value into a list by index |
| `0F09` | INSERT_LIST_STRING_VALUE_BY_INDEX | Inserts a string value into a list by index |
| `0F0A` | RETURN_TIMES | Returns runReturns number of gosub levels |
| `0F0B` | SET_SCRIPT_EVENT_BEFORE_GAME_PROCESS |  |
| `0F0C` | SET_SCRIPT_EVENT_AFTER_GAME_PROCESS |  |
| `0F0D` | SET_MATRIX_LOOK_DIRECTION | Sets the matrix look direction |
| `0F0E` | GET_THIRD_PERSON_CAMERA_TARGET | Returns the third person camera target |
| `0F0F` | GET_DISTANCE_MULTIPLIER | Returns the games drawing and generating distance multipliers |
| `0F10` | GET_ACTIVE_CAMERA_ROTATION | Returns the active camera rotation |
| `0F11` | GET_CLOSEST_WATER_DISTANCE | Returns the closest water distance and z level |
| `0F12` | GET_CAMERA_STRUCT | Returns the address of TheCamera (CCamera) and ActiveCam (CCam) |
| `0F13` | GET_TIME_NOT_TOUCHING_PAD | Returns the time in milliseconds since the pad has been touched |
| `0F14` | GET_CAMERA_ROTATION_INPUT_VALUES | Returns the camera's rotation input values |
| `0F15` | SET_CAMERA_ROTATION_INPUT_VALUES | Sets the camera's rotation Input values |
| `0F16` | SET_ON_MISSION | Sets the game's On Mission status without referencing a global variable |
| `0F17` | GET_MODEL_NAME_POINTER | Returns the address of the name of any modelId |

## Detailed Reference

### Audio

### `0E21` GET_AUDIO_SFX_VOLUME
Gets the SFX volume set in the game options

**Class:** `Audio.GetSfxVolume`
**Flags:** static

**Output:**
- `volume: float (variable)`

---

### `0E22` GET_AUDIO_RADIO_VOLUME
Gets the radio volume set in the game options

**Class:** `Audio.GetRadioVolume`
**Flags:** static

**Output:**
- `volume: float (variable)`

---

### AudioStream

### `0E3B` GET_AUDIOSTREAM_INTERNAL
Returns the internal reference of a given AUDIOSTREAM to be used in bass.dll functions

**Class:** `AudioStream.GetInternal`

**Input:**
- `self: AudioStream`

**Output:**
- `address: int (variable)`

---

### Camera

### `0E60` SET_CAMERA_CONTROL
Enables rotational control of the camera

**Class:** `Camera.SetCameraControl`
**Flags:** static

**Input:**
- `state: bool`

---

### `0E64` GET_CURRENT_CAMERA_MODE
Returns the current camera mode

**Class:** `Camera.GetCurrentMode`
**Flags:** static

**Output:**
- `mode: CameraMode (variable)`

---

### `0EB2` GET_OFFSET_FROM_CAMERA_IN_WORLD_COORDS
Returns world coordinates for the offset from the camera

**Class:** `Camera.GetOffsetFromCameraInWorldCoords`
**Flags:** static

**Input:**
- `offsetX: float`
- `offsetY: float`
- `offsetZ: float`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0EBE` LOCATE_CAMERA_DISTANCE_TO_COORDINATES
Returns True if the camera is located within the specified radius of the coordinates

**Class:** `Camera.LocateDistanceToCoordinates`
**Flags:** static, condition

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`

---

### `0EC7` GET_FADE_ALPHA
Returns the current alpha of the fade being performed ( < 255.0 max )

**Class:** `Camera.GetFadeAlpha`
**Flags:** static

**Output:**
- `alpha: float (variable)`

---

### `0F0E` GET_THIRD_PERSON_CAMERA_TARGET
Returns the third person camera target

**Class:** `Camera.GetThirdPersonTarget`
**Flags:** static

**Input:**
- `range: float`
- `sourceX: float`
- `sourceY: float`
- `sourceZ: float`

**Output:**
- `startX: float (variable)`
- `startY: float (variable)`
- `startZ: float (variable)`
- `endX: float (variable)`
- `endY: float (variable)`
- `endZ: float (variable)`

---

### `0F10` GET_ACTIVE_CAMERA_ROTATION
Returns the active camera rotation

**Class:** `Camera.GetActiveRotation`
**Flags:** static

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0F12` GET_CAMERA_STRUCT
Returns the address of TheCamera (CCamera) and ActiveCam (CCam)

**Class:** `Camera.GetStruct`
**Flags:** static

**Output:**
- `cCamera: int (variable)`
- `activeCCam: int (variable)`

---

### `0F14` GET_CAMERA_ROTATION_INPUT_VALUES
Returns the camera's rotation input values

**Class:** `Camera.GetRotationInputValues`
**Flags:** static

**Output:**
- `x: float (variable)`
- `y: float (variable)`

---

### `0F15` SET_CAMERA_ROTATION_INPUT_VALUES
Sets the camera's rotation Input values

**Class:** `Camera.SetRotationInputValues`
**Flags:** static

**Input:**
- `x: float`
- `y: float`

---

### Car

### `0D0F` SET_CAR_MODEL_ALPHA
Set's the specified car's transparency alpha

**Class:** `Car.SetModelAlpha`

**Input:**
- `self: Car`
- `alpha: int`

---

### `0D33` SET_CAR_DOOR_WINDOW_STATE
Sets the window state of the specified door of the car

**Class:** `Car.SetDoorWindowState`

**Input:**
- `self: Car`
- `door: CarNodeDoor`
- `state: bool`

---

### `0E00` GET_CAR_ALARM
Returns the status of the car's alarm

**Class:** `Car.GetAlarm`

**Input:**
- `self: Car`

**Output:**
- `status: CarAlarm (variable)`

---

### `0E08` IS_CAR_SCRIPT_CONTROLLED
Returns true if the specified vehicle is controlled by script

**Class:** `Car.IsScriptControlled`
**Flags:** condition

**Input:**
- `self: Car`

---

### `0E09` MARK_CAR_AS_NEEDED
Marks the vehicle as script controlled

**Class:** `Car.MarkAsNeeded`

**Input:**
- `self: Car`

---

### `0E12` GET_VEHICLE_SUBCLASS
Returns vehicle subclass, useful to check if vehicle is motorbike, bicycle, trailer etc

**Class:** `Car.GetSubclass`

**Input:**
- `self: Car`

**Output:**
- `subclass: VehicleSubclass (variable)`

---

### `0E17` INIT_EXTENDED_CAR_VARS
Inits additional variables for this car. Identifier can be "AUTO" for unique ID based on script pointer

**Class:** `Car.InitExtendedVars`
**Flags:** condition

**Input:**
- `self: Car`
- `identifier: string`
- `totalVars: int`

---

### `0E18` SET_EXTENDED_CAR_VAR
Sets extended var value for this car. Requires initialization (0E17), otherwise returns false

**Class:** `Car.SetExtendedVar`
**Flags:** condition

**Input:**
- `self: Car`
- `identifier: string`
- `varNumber: int`
- `value: any`

---

### `0E19` GET_EXTENDED_CAR_VAR
Gets extended var value for this car. Returns false if not initialized (0E17)

**Class:** `Car.GetExtendedCarVar`
**Flags:** condition

**Input:**
- `self: Car`
- `identifier: string`
- `varNumber: int`

**Output:**
- `value: any (variable)`

---

### `0E59` GET_TRAILER_FROM_CAR
Returns the handle of a trailer towed by this car

**Class:** `Car.GetTrailer`
**Flags:** condition

**Input:**
- `self: Car`

**Output:**
- `trailer: Car (variable)`

---

### `0E5A` GET_CAR_FROM_TRAILER
Returns the handle of a tractor towing this car

**Class:** `Car.GetTractor`
**Flags:** condition

**Input:**
- `self: Car`

**Output:**
- `tractor: Car (variable)`

---

### `0E5B` GET_CAR_DUMMY_COORD
Returns the coordinates of the specified car's vehicleDummy

**Class:** `Car.GetDummyCoord`
**Flags:** condition

**Input:**
- `self: Car`
- `vehicleDummy: VehicleDummy`
- `worldCoords: bool`
- `invertX: bool`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0E5F` CAR_HORN
Plays the car's horn (if the player is driving the car)

**Class:** `Car.PlayHorn`

**Input:**
- `self: Car`

---

### `0E61` SET_CAR_ALARM
Sets the status of the car's alarm

**Class:** `Car.SetAlarm`

**Input:**
- `self: Car`
- `status: CarAlarm`

---

### `0E65` GET_CAR_COLLISION_INTENSITY
Returns the intensity of the last collision of the specified car

**Class:** `Car.GetCollisionIntensity`
**Flags:** condition

**Input:**
- `self: Car`

**Output:**
- `intensity: float (variable)`

---

### `0E66` GET_CAR_COLLISION_COORDINATES
Returns the coordinates of the last collision of the specified car

**Class:** `Car.GetCollisionCoordinates`

**Input:**
- `self: Car`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0E82` DOES_CAR_HAVE_PART_NODE
Returns True if the car has the specified carNode part

**Class:** `Car.DoesHavePartNode`
**Flags:** condition

**Input:**
- `self: Car`
- `carNode: CarNode`

---

### `0E90` GET_CAR_COLLISION_SURFACE
Returns the specified car's collision surfaceType

**Class:** `Car.GetCollisionSurface`

**Input:**
- `self: Car`

**Output:**
- `surfaceType: SurfaceType (variable)`

---

### `0E91` GET_CAR_COLLISION_LIGHTING
Returns the specified car's collision lighting

**Class:** `Car.GetCollisionLighting`

**Input:**
- `self: Car`

**Output:**
- `lighting: float (variable)`

---

### `0E93` IS_CAR_REALLY_IN_AIR
Returns True if the specified car is really in the air, and False for boats floating on water

**Class:** `Car.IsReallyInAir`
**Flags:** condition

**Input:**
- `self: Car`

---

### `0EAD` GET_CAR_PROOFS
Returns the specified car's damage proofs

**Class:** `Car.GetProofs`

**Input:**
- `self: Car`

**Output:**
- `bullet: bool (variable)`
- `fire: bool (variable)`
- `explosion: bool (variable)`
- `collision: bool (variable)`
- `melee: bool (variable)`

---

### `0EB4` SET_CAR_COORDINATES_SIMPLE
Sets the specified car's coordinates without exception protocols

**Class:** `Car.SetCoordinatesSimple`

**Input:**
- `self: Car`
- `x: float`
- `y: float`
- `z: float`

---

### `0EB6` GET_CAR_WEAPON_DAMAGE_LAST_FRAME
Gets car damage by weapon last frame. Char can be invalid, and returns false if no damage last frame

**Class:** `Car.GetWeaponDamageLastFrame`
**Flags:** condition

**Input:**
- `self: Car`

**Output:**
- `char: Char (variable)`
- `weaponType: WeaponType (variable)`
- `intensity: float (variable)`

---

### `0EC9` GET_CAR_RANDOM_SEED
Returns the randomSeed of the specified car

**Class:** `Car.GetRandomSeed`

**Input:**
- `self: Car`

**Output:**
- `randomSeed: int (variable)`

---

### `0ECD` DONT_DELETE_CAR_UNTIL_TIME
Prevents the deletion of the specified car until MsFromNow

**Class:** `Car.DontDeleteUntilTime`

**Input:**
- `self: Car`
- `msFromNow: int`

---

### `0ECF` GET_TIME_CAR_IS_DEAD
Returns the TimeIsDead in milliseconds since the specified car is dead

**Class:** `Car.GetTimeIsDead`

**Input:**
- `self: Car`

**Output:**
- `timeIsDead: int (variable)`

---

### `0EE7` LOCATE_CAR_DISTANCE_TO_OBJECT
Returns True if the car is within the radius of the specified object

**Class:** `Car.LocateDistanceToObject`
**Flags:** condition

**Input:**
- `self: Car`
- `object: Object`
- `radius: float`

---

### `0EE8` LOCATE_CAR_DISTANCE_TO_CAR
Returns True if the car(self) is within the radius of the specified car

**Class:** `Car.LocateDistanceToCar`
**Flags:** condition

**Input:**
- `self: Car`
- `car: Car`
- `radius: float`

---

### `0EEB` LOCATE_CAR_DISTANCE_TO_COORDINATES
Returns True if the car is within the radius of the specified coordinates

**Class:** `Car.LocateDistanceToCoordinates`
**Flags:** condition

**Input:**
- `self: Car`
- `x: float`
- `y: float`
- `z: float`
- `radius: float`

---

### `0EF5` IS_CAR_OWNED_BY_PLAYER
Returns True if the specified car is owned by the player

**Class:** `Car.IsOwnedByPlayer`
**Flags:** condition

**Input:**
- `self: Car`

---

### `0EF6` SET_CAR_OWNED_BY_PLAYER
Sets the specified car as OwnedByPlayer

**Class:** `Car.SetOwnedByPlayer`

**Input:**
- `self: Car`
- `ownedByPlayer: bool`

---

### `0EF9` GET_CAR_ANIMGROUP
Returns the carAnimGroup of the specified car

**Class:** `Car.GetAnimGroup`

**Input:**
- `self: Car`

**Output:**
- `carAnimGroup: CarAnimGroup (variable)`

---

### `0EFB` IS_CAR_CONVERTIBLE
Returns True if the specified car is a convertible

**Class:** `Car.IsConvertible`
**Flags:** condition

**Input:**
- `self: Car`

---

### `0EFC` GET_CAR_VALUE
Returns the monetary value of the car

**Class:** `Car.GetValue`

**Input:**
- `self: Car`

**Output:**
- `value: int (variable)`

---

### `0EFD` GET_CAR_PEDALS
Returns the value of the car's gas and brake pedals

**Class:** `Car.GetPedals`

**Input:**
- `self: Car`

**Output:**
- `gas: float (variable)`
- `brake: float (variable)`

---

### CarGenerator

### `0E02` SET_CAR_GENERATOR_NO_SAVE

**Class:** `CarGenerator.SetNoSave`

**Input:**
- `self: CarGenerator`

---

### Char

### `0D0B` GET_CHAR_BONE_MATRIX
Returns the address of the character's specified bone matrix

**Class:** `Char.GetBoneMatrix`
**Flags:** condition

**Input:**
- `self: Char`
- `pedBone: PedBone`

**Output:**
- `matrix: int (variable)`

---

### `0D10` SET_CHAR_MODEL_ALPHA
Set's the specified character's transparency alpha

**Class:** `Char.SetModelAlpha`

**Input:**
- `self: Char`
- `alpha: int`

---

### `0D30` GET_CHAR_BONE

**Class:** `Char.GetBone`
**Flags:** condition

**Input:**
- `self: Char`
- `pedBone: PedBone`

**Output:**
- `address: int (variable)`

---

### `0D31` GET_BONE_OFFSET_VECTOR

**Class:** `Char.GetBoneOffsetVector`
**Flags:** static

**Input:**
- `pedBone: PedBone`

**Output:**
- `offsetVector: int (variable)`

---

### `0D32` GET_BONE_QUAT
Returns pointer to the quaterion under bone address obtained with GET_CHAR_BONE

**Class:** `Char.GetBoneQuat`
**Flags:** static

**Input:**
- `bone: int`

**Output:**
- `quat: int (variable)`

---

### `0D39` GET_CHAR_MAX_HEALTH
Returns the character's maximum health (08AF)

**Class:** `Char.GetMaxHealth`

**Input:**
- `self: Char`

**Output:**
- `maxHealth: float (variable)`

---

### `0E0A` IS_CHAR_SCRIPT_CONTROLLED
Returns true if the specified character is controlled by script

**Class:** `Char.IsScriptControlled`
**Flags:** condition

**Input:**
- `self: Char`

---

### `0E0B` MARK_CHAR_AS_NEEDED
Marks the character as script controlled

**Class:** `Char.MarkAsNeeded`

**Input:**
- `self: Char`

---

### `0E14` INIT_EXTENDED_CHAR_VARS
Inits additional variables for this char. Identifier can be "AUTO" for unique ID based on script pointer

**Class:** `Char.InitExtendedVars`
**Flags:** condition

**Input:**
- `self: Char`
- `identifier: string`
- `totalVars: int`

---

### `0E15` SET_EXTENDED_CHAR_VAR
Sets extended var value for this char. Requires initialization (0E14), otherwise returns false

**Class:** `Char.SetExtendedVar`
**Flags:** condition

**Input:**
- `self: Char`
- `identifier: string`
- `varNumber: int`
- `value: any`

---

### `0E16` GET_EXTENDED_CHAR_VAR
Gets extended var value for this char. Returns false if not initialized (0E14)

**Class:** `Char.GetExtendedVar`
**Flags:** condition

**Input:**
- `self: Char`
- `identifier: string`
- `varNumber: int`

**Output:**
- `value: any (variable)`

---

### `0E24` FIX_CHAR_GROUND_BRIGHTNESS_AND_FADE_IN

**Class:** `Char.FixGroundBrightnessAndFadeIn`

**Input:**
- `self: Char`
- `fixGround: bool`
- `fixBrightness: bool`
- `fadeIn: bool`

---

### `0E30` SET_RENDER_OBJECT_AUTO_HIDE
Sets the renderObject to AutoHide if the character is dead, is using a weapon, or enters a car

**Class:** `Char.SetRenderObjectAutoHide`

**Input:**
- `self: Char`
- `dead: bool`
- `weapon: bool`
- `car: bool`

---

### `0E32` SET_CHAR_COORDINATES_SIMPLE
Sets the character's coordinates without exception protocols

**Class:** `Char.SetCoordinatesSimple`

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `z: float`

---

### `0E42` IS_CHAR_DOING_TASK_ID
Returns true if the character is performing the specified task

**Class:** `Char.IsDoingTaskId`
**Flags:** condition

**Input:**
- `self: Char`
- `taskId: TaskId`

---

### `0E43` GET_CHAR_TASK_POINTER_BY_ID
Returns the address of the character's task by taskId

**Class:** `Char.GetTaskPointerById`
**Flags:** condition

**Input:**
- `self: Char`
- `taskId: TaskId`

**Output:**
- `address: int (variable)`

---

### `0E44` GET_CHAR_KILL_TARGET_CHAR
Returns the handle of the killTarget of the specified character

**Class:** `Char.GetKillTargetChar`
**Flags:** condition

**Input:**
- `self: Char`

**Output:**
- `killTarget: Char (variable)`

---

### `0E46` IS_CHAR_USING_GUN
Returns true if the specified character is using a gun

**Class:** `Char.IsUsingGun`
**Flags:** condition

**Input:**
- `self: Char`

---

### `0E47` IS_CHAR_FIGHTING
Returns true if the specified character is fighting

**Class:** `Char.IsFighting`
**Flags:** condition

**Input:**
- `self: Char`

---

### `0E48` IS_CHAR_FALLEN_ON_GROUND
Returns true if the specified character has fallen on the ground

**Class:** `Char.IsFallenOnGround`
**Flags:** condition

**Input:**
- `self: Char`

---

### `0E49` IS_CHAR_ENTERING_ANY_CAR
Returns true if the specified character is entering any car

**Class:** `Char.IsEnteringAnyCar`
**Flags:** condition

**Input:**
- `self: Char`

---

### `0E4A` IS_CHAR_EXITING_ANY_CAR
Returns true if the specified character is exiting any car

**Class:** `Char.IsExitingAnyCar`
**Flags:** condition

**Input:**
- `self: Char`

---

### `0E4B` IS_CHAR_PLAYING_ANY_SCRIPT_ANIMATION
Returns true if the specified character is playing any script animation

**Class:** `Char.IsPlayingAnyScriptAnimation`
**Flags:** condition

**Input:**
- `self: Char`
- `includeAnims: bool`

---

### `0E4C` IS_CHAR_DOING_ANY_IMPORTANT_TASK
Returns true if the specified character is doing any important task

**Class:** `Char.IsDoingAnyImportantTask`
**Flags:** condition

**Input:**
- `self: Char`
- `includeAnims: bool`

---

### `0E5C` GET_CHAR_HEALTH_PERCENT
Returns the character's health as a floating-point percentage

**Class:** `Char.GetHealthPercent`

**Input:**
- `self: Char`

**Output:**
- `healthPercent: float (variable)`

---

### `0E83` GET_CURRENT_CHAR_WEAPONINFO
Returns a pointer to the character's current weaponInfo struct

**Class:** `Char.GetCurrentWeaponinfo`
**Flags:** condition

**Input:**
- `self: Char`

**Output:**
- `handle: WeaponInfo (variable)`

---

### `0E8B` GET_CHAR_WEAPON_STATE
Returns the character's current weaponState

**Class:** `Char.GetWeaponState`

**Input:**
- `self: Char`

**Output:**
- `weaponState: WeaponState (variable)`

---

### `0E8C` GET_CHAR_WEAPON_CLIP
Returns the character's current WeaponClip

**Class:** `Char.GetCharWeaponClip`

**Input:**
- `self: Char`

**Output:**
- `weaponClip: int (variable)`

---

### `0E8E` GET_CHAR_COLLISION_SURFACE
Returns the specified character's collision surfaceType

**Class:** `Char.GetCollisionSurface`

**Input:**
- `self: Char`

**Output:**
- `surfaceType: SurfaceType (variable)`

---

### `0E8F` GET_CHAR_COLLISION_LIGHTING
Returns the specified character's collision lighting

**Class:** `Char.GetCollisionLighting`

**Input:**
- `self: Char`

**Output:**
- `lighting: float (variable)`

---

### `0E92` IS_CHAR_REALLY_IN_AIR
Returns True when the character is really in air, including while using a parachute or jetpack

**Class:** `Char.IsReallyInAir`
**Flags:** condition

**Input:**
- `self: Char`

---

### `0E96` CLEAR_CHAR_PRIMARY_TASKS
Clears the specified character's primary tasks

**Class:** `Char.ClearPrimaryTasks`

**Input:**
- `self: Char`

---

### `0E97` CLEAR_CHAR_SECONDARY_TASKS
Clears the character's secondary tasks

**Class:** `Char.ClearSecondaryTasks`

**Input:**
- `self: Char`

---

### `0EA0` SET_CHAR_SECOND_PLAYER
Sets this char as controlled by player two

**Class:** `Char.SetSecondPlayer`

**Input:**
- `self: Char`
- `enableCamera: bool`
- `separateCars: bool`

---

### `0EA4` IS_CHAR_ON_FIRE
Returns True if the character is on fire

**Class:** `Char.IsOnFire`
**Flags:** condition

**Input:**
- `self: Char`

---

### `0EA5` GET_CLOSEST_COP_NEAR_CHAR
Returns the handle of the closestCop to the specified character

**Class:** `Char.GetClosestCop`
**Flags:** condition

**Input:**
- `self: Char`
- `radius: float`
- `alive: bool`
- `inCar: bool`
- `onFoot: bool`
- `seenInFront: bool`

**Output:**
- `closestCop: Char (variable)`

---

### `0EAA` SET_CHAR_ARRESTED
Sets the specified character's pedState to Arrested

**Class:** `Char.SetArrested`

**Input:**
- `self: Char`

---

### `0EAB` GET_CHAR_PEDSTATE
Returns the specified character's pedState

**Class:** `Char.GetPedState`

**Input:**
- `self: Char`

**Output:**
- `pedState: PedState (variable)`

---

### `0EAC` GET_CHAR_PROOFS
Returns the specified character's damage proofs

**Class:** `Char.GetProofs`

**Input:**
- `self: Char`

**Output:**
- `bullet: bool (variable)`
- `fire: bool (variable)`
- `explosion: bool (variable)`
- `collision: bool (variable)`
- `melee: bool (variable)`

---

### `0EAF` IS_CHAR_WEAPON_VISIBLE_SET
Returns true if the specified character has weapon visible set

**Class:** `Char.IsWeaponVisibleSet`
**Flags:** condition

**Input:**
- `self: Char`

---

### `0EB1` GET_CHAR_STAT_ID
Returns the specified character's pedStat ID (data\pedstats.dat)

**Class:** `Char.GetStatId`

**Input:**
- `self: Char`

**Output:**
- `pedStat: PedStat (variable)`

---

### `0EB5` GET_CHAR_DAMAGE_LAST_FRAME
Returns the character's damaging entity and weaponType, bodyPart damaged, and intensity of damage last frame

**Class:** `Char.GetDamageLastFrame`
**Flags:** condition

**Input:**
- `self: Char`

**Output:**
- `entity: Char (variable)`
- `weaponType: WeaponType (variable)`
- `bodyPart: BodyPart (variable)`
- `intensity: float (variable)`

---

### `0EC8` GET_CHAR_RANDOM_SEED
Returns the randomSeed of the specified character

**Class:** `Char.GetRandomSeed`

**Input:**
- `self: Char`

**Output:**
- `randomSeed: int (variable)`

---

### `0ECB` GET_CHAR_MOVE_STATE

**Class:** `Char.GetMoveState`

**Input:**
- `self: Char`

**Output:**
- `moveState: MoveState (variable)`

---

### `0ECC` DONT_DELETE_CHAR_UNTIL_TIME
Prevents the deletion of the specified character until MsFromNow

**Class:** `Char.DontDeleteUntilTime`

**Input:**
- `self: Char`
- `msFromNow: int`

---

### `0ECE` GET_TIME_CHAR_IS_DEAD
Returns the TimeIsDead in milliseconds since the specified character is dead

**Class:** `Char.GetTimeIsDead`

**Input:**
- `self: Char`

**Output:**
- `timeIsDead: int (variable)`

---

### `0ED9` SET_CHAR_IGNORE_DAMAGE_ANIMS

**Class:** `Char.SetIgnoreDamageAnims`

**Input:**
- `self: Char`
- `state: bool`

---

### `0EE4` LOCATE_CHAR_DISTANCE_TO_CHAR
Returns True if the character(self) is within the radius of the specified character

**Class:** `Char.LocateDistanceToChar`
**Flags:** condition

**Input:**
- `self: Char`
- `character: Char`
- `radius: float`

---

### `0EE5` LOCATE_CHAR_DISTANCE_TO_CAR
Returns True if the character is within the radius of the specified car

**Class:** `Char.LocateDistanceToCar`
**Flags:** condition

**Input:**
- `self: Char`
- `car: Car`
- `radius: float`

---

### `0EE6` LOCATE_CHAR_DISTANCE_TO_OBJECT
Returns True if the character is within the radius of the specified object

**Class:** `Char.LocateDistanceToObject`
**Flags:** condition

**Input:**
- `self: Char`
- `object: Object`
- `radius: float`

---

### `0EEA` LOCATE_CHAR_DISTANCE_TO_COORDINATES
Returns True if the character is within the radius of the specified coordinates

**Class:** `Char.LocateDistanceToCoordinates`
**Flags:** condition

**Input:**
- `self: Char`
- `x: float`
- `y: float`
- `z: float`
- `radius: float`

---

### `0EFA` GET_CHAR_FEAR
Returns the specified character's fear level (see pedstats.dat)

**Class:** `Char.GetFear`

**Input:**
- `self: Char`

**Output:**
- `fear: int (variable)`

---

### `0EFF` GET_CHAR_SIMPLEST_ACTIVE_TASK
Returns the character's simplest active taskId and the address of the task

**Class:** `Char.GetSimplestActiveTask`
**Flags:** condition

**Input:**
- `self: Char`

**Output:**
- `taskId: TaskId (variable)`
- `address: int (variable)`

---

### `0F02` CREATE_RENDER_OBJECT_TO_CHAR_BONE_FROM_SPECIAL

**Class:** `Char.CreateRenderObjectToCharBoneFromSpecial`

**Input:**
- `self: Char`
- `specialModel: int`
- `pedBone: PedBone`
- `x: float`
- `y: float`
- `z: float`
- `rx: float`
- `ry: float`
- `rz: float`

**Output:**
- `renderobject: int (variable)`

---

### CleoBlip

### `0E2A` ADD_CLEO_BLIP
Creates a blip that don't saves, supports any texture, alpha and don't hits the blip limit

**Class:** `CleoBlip.Add`
**Flags:** constructor

**Input:**
- `rwTextureOrRadarSprite: any`
- `x: float`
- `y: float`
- `short: bool`
- `red: int`
- `green: int`
- `blue: int`
- `alpha: int`

**Output:**
- `handle: CleoBlip (variable)`

---

### `0E2B` REMOVE_CLEO_BLIP
Removes a cleo blip

**Class:** `CleoBlip.Remove`
**Flags:** destructor

**Input:**
- `self: CleoBlip`

---

### Clipboard

### `0B20` READ_CLIPBOARD_DATA
Copies the specified number of bytes of text from the clipboard to the address

**Class:** `Clipboard.ReadData`
**Flags:** static

**Input:**
- `address: int`
- `number: int`

---

### `0B21` WRITE_CLIPBOARD_DATA

**Class:** `Clipboard.WriteData`
**Flags:** static

**Input:**
- `address: int`
- `number: int`

---

### Clock

### `0D2D` GET_LOCAL_TIME
Returns the full local time of the player's PC

**Class:** `Clock.GetLocalTime`
**Flags:** static

**Output:**
- `year: int (variable)`
- `month: int (variable)`
- `weekDay: int (variable)`
- `day: int (variable)`
- `hour: int (variable)`
- `minute: int (variable)`
- `second: int (variable)`
- `millisecond: int (variable)`

---

### `0E40` GET_CURRENT_HOUR
Returns the clock's current hour

**Class:** `Clock.GetCurrentHour`
**Flags:** static

**Output:**
- `hour: int (variable)`

---

### `0E41` GET_CURRENT_MINUTE
Returns the clock's current minute

**Class:** `Clock.GetCurrentMinute`
**Flags:** static

**Output:**
- `minute: int (variable)`

---

### `0EBB` PASS_TIME
Simulates the passage of time on the clock, calendar and environment

**Class:** `Clock.PassTime`
**Flags:** static

**Input:**
- `minutes: int`

---

### ColPoint

### `0D3A` GET_COLLISION_BETWEEN_POINTS
Returns the colPoint, coordinates, and collision entity between two points

**Class:** `ColPoint.GetCollisionBetweenPoints`
**Flags:** condition, static, constructor

**Input:**
- `fromX: float`
- `fromY: float`
- `fromZ: float`
- `toX: float`
- `toY: float`
- `toZ: float`
- `buildings: bool`
- `vehicles: bool`
- `peds: bool`
- `objects: bool`
- `dummies: bool`
- `seeThroughCheck: bool`
- `cameraIgnoreCheck: bool`
- `shotThroughCheck: bool`
- `entityToIgnore: int`

**Output:**
- `handle: ColPoint (variable)`
- `outX: float (variable)`
- `outY: float (variable)`
- `outZ: float (variable)`
- `entity: int (variable)`

---

### `0D3B` GET_COLPOINT_NORMAL_VECTOR
Returns the vector of the specified ColPoint

**Class:** `ColPoint.GetNormalVector`

**Input:**
- `self: ColPoint`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0D3C` GET_COLPOINT_SURFACE
Returns the surfaceType of the specified ColPoint

**Class:** `ColPoint.GetSurface`

**Input:**
- `self: ColPoint`

**Output:**
- `surfaceType: SurfaceType (variable)`

---

### `0D3E` GET_COLPOINT_DEPTH
Returns the depth of the specified ColPoint

**Class:** `ColPoint.GetDepth`

**Input:**
- `self: ColPoint`

**Output:**
- `depth: float (variable)`

---

### `0E6B` GET_COLPOINT_LIGHTING
Returns the lighting of the specified ColPoint

**Class:** `ColPoint.GetLighting`

**Input:**
- `self: ColPoint`
- `fromNight: bool`

**Output:**
- `lighting: int (variable)`

---

### `0EE1` GET_COLPOINT_COORDINATES
Returns the coordinates of the specified ColPoint

**Class:** `ColPoint.GetCoordinates`

**Input:**
- `self: ColPoint`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### Cutscene

### `0E25` IS_ON_CUTSCENE
Returns true if a cutscene is active (02E7)

**Class:** `Cutscene.IsOn`
**Flags:** static, condition

---

### DynamicLibrary

### `0EFE` GET_LOADED_LIBRARY
Returns the address of a loaded dynamic-link library (DLL)

**Class:** `DynamicLibrary.GetLoadedLibrary`
**Flags:** condition, static, constructor

**Input:**
- `fileName: string`

**Output:**
- `handle: DynamicLibrary (variable)`

---

### Entity

### `0E13` GET_ENTITY_TYPE
Gets the type of the entity

**Class:** `Entity.GetType`
**Flags:** static

**Input:**
- `entity: any`

**Output:**
- `type: EntityType (variable)`

---

### `0EED` LOCATE_ENTITY_DISTANCE_TO_ENTITY
Returns True if entityB is within the radius of entityA

**Class:** `Entity.LocateDistanceToEntity`
**Flags:** static, condition

**Input:**
- `entityA: int`
- `entityB: int`
- `radius: float`

---

### `0EEE` GET_ENTITY_COORDINATES
Returns the coordinates of the entity at the specified address

**Class:** `Entity.GetCoordinates`
**Flags:** static

**Input:**
- `address: int`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0EEF` GET_ENTITY_HEADING
Returns the heading of the entity at the specified address

**Class:** `Entity.GetHeading`
**Flags:** static

**Input:**
- `address: int`

**Output:**
- `heading: float (variable)`

---

### Fx

### `0EBF` GET_FX_SYSTEM_POINTER
Returns the address of the specified FX system associated with the given particle, or 0 if handle is invalid

**Class:** `Fx.GetAddress`
**Flags:** condition, static

**Input:**
- `particle: Particle`

**Output:**
- `address: int (variable)`

---

### `0EC0` ADD_FX_SYSTEM_PARTICLE
Adds an FX system particle

**Class:** `Fx.AddParticle`
**Flags:** static

**Input:**
- `particle: Particle`
- `posX: float`
- `posY: float`
- `posZ: float`
- `velX: float`
- `velY: float`
- `velZ: float`
- `size: float`
- `brightness: float`
- `r: float`
- `g: float`
- `b: float`
- `a: float`
- `lastFactor: float`

---

### `0EC1` IS_FX_SYSTEM_AVAILABLE_WITH_NAME
Returns True if an FX system with the specified name is available

**Class:** `Fx.IsAvailableWithName`
**Flags:** static, condition

**Input:**
- `name: string`

---

### Game

### `0E0E` GET_CURRENT_RESOLUTION
Gets the game window width and height resolution

**Class:** `Game.GetCurrentResolution`
**Flags:** static

**Output:**
- `width: int (variable)`
- `height: int (variable)`

---

### `0E20` IS_ON_SAMP
Returns true if the current game runs on San Andreas Multiplayer (SA-MP)

**Class:** `Game.IsSamp`
**Flags:** condition, static

---

### `0E2C` GET_CURRENT_SAVE_SLOT
Gets loaded save slot number. 0 if new game

**Class:** `Game.GetCurrentSaveSlot`
**Flags:** static

**Output:**
- `slot: int (variable)`

---

### `0E2D` IS_GAME_FIRST_START
Is first gameplay start (game was not reloaded)

**Class:** `Game.IsFirstStart`
**Flags:** static, condition

---

### `0E45` FRAME_MOD
Returns True every mod number of frames

**Class:** `Game.FrameMod`
**Flags:** static, condition

**Input:**
- `mod: int`

---

### `0E5D` IS_CHEAT_ACTIVE
Returns True if the specified cheat is togglable and active

**Class:** `Game.IsCheatActive`
**Flags:** condition, static

**Input:**
- `cheat: Cheats`

---

### `0E6E` IS_SELECT_MENU_JUST_PRESSED
Returns True if menu Select was just pressed

**Class:** `Game.IsSelectMenuJustPressed`
**Flags:** condition, static

---

### `0EA1` DISABLE_SECOND_PLAYER

**Class:** `Game.DisableSecondPlayer`
**Flags:** static

**Input:**
- `restoreCamera: bool`

---

### `0EA2` FIX_TWO_PLAYERS_SEPARATED_CARS
Enables fixes for making two players use separated cars

**Class:** `Game.FixTwoPlayersSeparatedCars`
**Flags:** static

---

### `0F16` SET_ON_MISSION
Sets the game's On Mission status without referencing a global variable

**Class:** `Game.SetOnMission`
**Flags:** static

**Input:**
- `status: bool`

---

### Hud

### `0E0F` GET_FIXED_XY_ASPECT_RATIO
Gets x and y values based on window aspect ratio, useful for text and hud scaling

**Class:** `Hud.GetFixedXyAspectRatio`
**Flags:** static

**Input:**
- `x: float`
- `y: float`

**Output:**
- `x: float (variable)`
- `y: float (variable)`

---

### `0E4E` DISPLAY_ONSCREEN_TIMER_LOCAL
Creates a countdown or countup onscreen timer

**Class:** `Hud.DisplayTimerLocal`
**Flags:** static

**Input:**
- `timer: int (variable)`
- `direction: TimerDirection`

---

### `0E4F` DISPLAY_ONSCREEN_TIMER_WITH_STRING_LOCAL
Creates a countdown or countup onscreen timer with the text

**Class:** `Hud.DisplayTimerWithStringLocal`
**Flags:** static

**Input:**
- `timer: int (variable)`
- `direction: TimerDirection`
- `text: gxt_key`

---

### `0E50` DISPLAY_ONSCREEN_COUNTER_LOCAL
Displays an onscreen counter, either shown in numbers or as a bar

**Class:** `Hud.DisplayCounterLocal`
**Flags:** static

**Input:**
- `timer: int (variable)`
- `display: CounterDisplay`

---

### `0E51` DISPLAY_ONSCREEN_COUNTER_WITH_STRING_LOCAL
Displays an onscreen counter with the text, either shown in numbers or as a bar

**Class:** `Hud.DisplayCounterWithStringLocal`
**Flags:** static

**Input:**
- `counter: int (variable)`
- `display: CounterDisplay`
- `text: gxt_key`

---

### `0E52` DISPLAY_TWO_ONSCREEN_COUNTERS_LOCAL
Displays two onscreen counters separated by a slash

**Class:** `Hud.DisplayTwoCountersLocal`
**Flags:** static

**Input:**
- `leftCounter: int (variable)`
- `rightCounter: int (variable)`

---

### `0E53` DISPLAY_TWO_ONSCREEN_COUNTERS_WITH_STRING_LOCAL
Displays two onscreen counters separated by a slash with the text

**Class:** `Hud.DisplayTwoCountersWithStringLocal`
**Flags:** static

**Input:**
- `leftCounter: int (variable)`
- `rightCounter: int (variable)`
- `text: gxt_key`

---

### `0E54` CLEAR_ONSCREEN_TIMER_LOCAL
Removes the local onscreen timer

**Class:** `Hud.ClearTimerLocal`
**Flags:** static

**Input:**
- `timer: int (variable)`

---

### `0E55` CLEAR_ONSCREEN_COUNTER_LOCAL
Removes the local onscreen counter

**Class:** `Hud.ClearCounterLocal`
**Flags:** static

**Input:**
- `counter: int (variable)`

---

### `0E56` SET_ONSCREEN_COUNTER_FLASH_WHEN_FIRST_DISPLAYED_LOCAL
Sets the local counter to flash when first displayed

**Class:** `Hud.SetCounterFlashWhenFirstDisplayedLocal`
**Flags:** static

**Input:**
- `counter: int (variable)`
- `state: bool`

---

### `0E57` SET_TIMER_BEEP_COUNTDOWN_TIME_LOCAL
Starts a sound when the countdown timer reaches the specified number of seconds

**Class:** `Hud.SetTimerBeepCountdownTimeLocal`
**Flags:** static

**Input:**
- `timer: int (variable)`
- `timeInSec: int`

---

### `0E58` SET_ONSCREEN_COUNTER_COLOUR_LOCAL
Sets the color of the specified local counter

**Class:** `Hud.SetCounterColorLocal`
**Flags:** static

**Input:**
- `counter: int (variable)`
- `color: HudColors`

---

### `0EB8` IS_RADAR_VISIBLE

**Class:** `Hud.IsRadarVisible`
**Flags:** static, condition

---

### `0EB9` IS_HUD_VISIBLE

**Class:** `Hud.IsVisible`
**Flags:** static, condition

---

### List

### `0E72` CREATE_LIST
Creates a list of the specified type

**Class:** `List.Create`
**Flags:** constructor

**Input:**
- `type: ListType`

**Output:**
- `handle: List (variable)`

---

### `0E73` DELETE_LIST
Deletes the specified list

**Class:** `List.Delete`
**Flags:** destructor

**Input:**
- `self: List`

---

### `0E74` LIST_ADD
Adds a numerical value to the specified list

**Class:** `List.Add`

**Input:**
- `self: List`
- `value: any`

---

### `0E75` LIST_REMOVE_VALUE
Removes a numerical value from the specified list

**Class:** `List.RemoveValue`

**Input:**
- `self: List`
- `value: any`

---

### `0E76` LIST_REMOVE_INDEX
Removes an entry from the specified list by index

**Class:** `List.RemoveIndex`

**Input:**
- `self: List`
- `index: int`

---

### `0E77` GET_LIST_SIZE
Returns the number of entries in the specified list

**Class:** `List.GetSize`

**Input:**
- `self: List`

**Output:**
- `entries: int (variable)`

---

### `0E78` GET_LIST_VALUE_BY_INDEX
Returns a numerical value from the specified list by index

**Class:** `List.GetValueByIndex`

**Input:**
- `self: List`
- `index: int`

**Output:**
- `value: any (variable)`

---

### `0E79` RESET_LIST
Resets all entries within the specified list

**Class:** `List.Reset`

**Input:**
- `self: List`

---

### `0E7A` GET_LIST_STRING_VALUE_BY_INDEX
Returns a string value from the specified list by index

**Class:** `List.GetStringValueByIndex`

**Input:**
- `self: List`
- `index: int`

**Output:**
- `string: string (variable)`

---

### `0E7B` LIST_ADD_STRING
Adds a string value to the specified list

**Class:** `List.AddString`

**Input:**
- `self: List`
- `string: string`

---

### `0E7C` LIST_REMOVE_STRING_VALUE
Removes a string value from the specified list

**Class:** `List.RemoveStringValue`

**Input:**
- `self: List`
- `string: string`

---

### `0E7D` LIST_REMOVE_INDEX_RANGE
Removes entries from the specified list by index range

**Class:** `List.RemoveIndexRange`

**Input:**
- `self: List`
- `start: int`
- `stop: int`

---

### `0E7E` REVERSE_LIST
Reverses the order of entries within the specified list

**Class:** `List.Reverse`

**Input:**
- `self: List`

---

### `0F06` REPLACE_LIST_VALUE_BY_INDEX
Replaces a value on a list by index

**Class:** `List.ReplaceValueByIndex`

**Input:**
- `self: List`
- `index: int`
- `value: any`

---

### `0F07` REPLACE_LIST_STRING_VALUE_BY_INDEX
Replaces a string value on a list by index

**Class:** `List.ReplaceStringValueByIndex`

**Input:**
- `self: List`
- `index: int`
- `string: string`

---

### `0F08` INSERT_LIST_VALUE_BY_INDEX
Inserts a value into a list by index

**Class:** `List.InsertValueByIndex`

**Input:**
- `self: List`
- `index: int`
- `value: any`

---

### `0F09` INSERT_LIST_STRING_VALUE_BY_INDEX
Inserts a string value into a list by index

**Class:** `List.InsertStringValueByIndex`

**Input:**
- `self: List`
- `index: int`
- `string: string`

---

### Math

### `0E03` PERLIN_NOISE
Calculates the 1D Perlin simplex noise

**Class:** `Math.PerlinNoise`
**Flags:** static

**Input:**
- `x: float`

**Output:**
- `result: float (variable)`

---

### `0E1F` EASE
Eases k value in range of 0.0 to 1.0, resulting in a easing value based on mode and way, useful for smooth animations

**Class:** `Math.Ease`
**Flags:** static

**Input:**
- `k: float`
- `mode: EaseMode`
- `way: EaseWay`

**Output:**
- `result: float (variable)`

---

### `0E27` GET_ANGLE_FROM_TWO_COORDS

**Class:** `Math.GetAngleFromTwoCoords`
**Flags:** static

**Input:**
- `x1: float`
- `y1: float`
- `x2: float`
- `y2: float`

**Output:**
- `angle: float (variable)`

---

### `0E29` PERLIN_NOISE_FRACTAL
Calculates the Fractal Brownian Motion (fBm) summation of 1D Perlin Simplex noise

**Class:** `Math.PerlinNoiseFractal`
**Flags:** static

**Input:**
- `x: float`
- `octaves: int`
- `frequency: float`
- `amplitude: float`
- `lacunarity: float`
- `persistence: float`

**Output:**
- `result: float (variable)`

---

### `0E4D` RANDOM_PERCENT
Returns randomly True the specified percent of the time

**Class:** `Math.RandomPercent`
**Flags:** static, condition

**Input:**
- `percent: int`

---

### `0EBC` GENERATE_RANDOM_INT_IN_RANGE_WITH_SEED
Generates a randomInteger from min to < max with seed

**Class:** `Math.GenerateRandomIntInRangeWithSeed`
**Flags:** static

**Input:**
- `seed: int`
- `min: int`
- `max: int`

**Output:**
- `randomInteger: int (variable)`

---

### `0EBD` GENERATE_RANDOM_FLOAT_IN_RANGE_WITH_SEED
Generates a randomFloat from min to < max with seed

**Class:** `Math.GenerateRandomFloatInRangeWithSeed`
**Flags:** static

**Input:**
- `seed: int`
- `min: float`
- `max: float`

**Output:**
- `randomFloat: float (variable)`

---

### `0EF1` PERLIN_NOISE_FRACTAL_2D
Calculates the Fractal Brownian Motion (fBm) summation of 2D Perlin Simplex noise

**Class:** `Math.PerlinNoiseFractal2D`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `octaves: int`
- `frequency: float`
- `amplitude: float`
- `lacunarity: float`
- `persistence: float`

**Output:**
- `result: float (variable)`

---

### `0EF2` PERLIN_NOISE_FRACTAL_3D
Calculates the Fractal Brownian Motion (fBm) summation of 3D Perlin Simplex noise

**Class:** `Math.PerlinNoiseFractal3D`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `octaves: int`
- `frequency: float`
- `amplitude: float`
- `lacunarity: float`
- `persistence: float`

**Output:**
- `result: float (variable)`

---

### `0EF4` CLAMP_FLOAT
Returns the clamped value of the specified float between the min and max values

**Class:** `Math.ClampFloat`
**Flags:** static

**Input:**
- `float: float`
- `min: float`
- `max: float`

**Output:**
- `clamped: float (variable)`

---

### `0EF7` CLAMP_INT
Returns the clamped value of the specified integer between the min and max values

**Class:** `Math.ClampInt`
**Flags:** static

**Input:**
- `integer: int`
- `min: int`
- `max: int`

**Output:**
- `clamped: int (variable)`

---

### Memory

### `0D27` COPY_MEMORY
Copies each memory byte from src address to dest address

**Class:** `Memory.Copy`
**Flags:** static

**Input:**
- `src: int`
- `dest: int`
- `size: int`

---

### `0D37` WRITE_STRUCT_PARAM
Writes the dword value to the struct address by index (index*4+address) see: 0E28

**Class:** `Memory.WriteStructParam`
**Flags:** static

**Input:**
- `address: int`
- `index: int`
- `value: int`

---

### `0D38` READ_STRUCT_PARAM
Reads the dword value from the struct address by index (index*4+address) see: 0D4E

**Class:** `Memory.ReadStructParam`
**Flags:** static

**Input:**
- `address: int`
- `index: int`

**Output:**
- `value: int (variable)`

---

### `0D4E` READ_STRUCT_OFFSET
Reads a value from the given offset from the memory address (see: 0D38)

**Class:** `Memory.ReadStructOffset`
**Flags:** static

**Input:**
- `address: int`
- `offset: int`
- `size: int`

**Output:**
- `result: any (variable)`

---

### `0E28` WRITE_STRUCT_OFFSET
Writes the value at the given offset from the memory address (see: 0D37)

**Class:** `Memory.WriteStructOffset`
**Flags:** static

**Input:**
- `address: int`
- `offset: int`
- `size: int`
- `value: int`

---

### `0E6A` MAKE_NOP
Fills memory address with 0x90 with given size

**Class:** `Memory.MakeNop`
**Flags:** static

**Input:**
- `address: int`
- `size: int`

---

### `0E70` GET_LAST_CREATED_CUSTOM_SCRIPT
Gets the address of the last created custom script

**Class:** `Memory.GetLastCreatedCustomScript`
**Flags:** static, condition

**Output:**
- `address: int (variable)`

---

### `0EE2` READ_STRUCT_OFFSET_MULTI
Reads a value from the given offset from the memory address multiple times as array/vector

**Class:** `Memory.ReadStructOffsetMulti`
**Flags:** static

**Input:**
- `address: int`
- `offset: int`
- `count: int`
- `size: int`

**Output:**
- `results: arguments (variable)`

---

### `0EE3` WRITE_STRUCT_OFFSET_MULTI
Writes the value at the given offset from the memory address multiple times as array/vector

**Class:** `Memory.WriteStructOffsetMulti`
**Flags:** static

**Input:**
- `address: int`
- `offset: int`
- `count: int`
- `size: int`
- `params: arguments`

---

### Mission

### `0E1D` IS_ON_MISSION
Returns true if the player is on a mission (the variable set in 0180 is not zero)

**Class:** `Mission.IsOn`
**Flags:** condition, static

---

### `0EB7` IS_ON_SCRIPTED_CUTSCENE
Checks if is playing scripted mission cutscene, that is, original widescreen borders are toggled on

**Class:** `Mission.IsOnScriptedCutscene`
**Flags:** condition, static

---

### Mouse

### `0E10` IS_MOUSE_WHEEL_UP
Returns true if the mouse wheel has been scrolled up

**Class:** `Mouse.IsWheelUp`
**Flags:** static, condition

---

### `0E11` IS_MOUSE_WHEEL_DOWN
Returns true if the mouse wheel has been scrolled down

**Class:** `Mouse.IsWheelDown`
**Flags:** condition, static

---

### `0E23` GET_MOUSE_SENSIBILITY
Gets the mouse sensibility set in the game options

**Class:** `Mouse.GetSensibility`
**Flags:** static

**Output:**
- `sensibility: float (variable)`

---

### Object

### `0D11` SET_OBJECT_MODEL_ALPHA
Set's the specified object's transparency alpha

**Class:** `Object.SetModelAlpha`

**Input:**
- `self: Object`
- `alpha: int`

---

### `0E01` CREATE_OBJECT_NO_SAVE
Creates an no save game object at the specified location, with the specified model

**Class:** `Object.CreateNoSave`
**Flags:** constructor

**Input:**
- `modelId: model_object`
- `x: float`
- `y: float`
- `z: float`
- `useOffset: bool`
- `useGround: bool`

**Output:**
- `handle: Object (variable)`

---

### `0E0C` IS_OBJECT_SCRIPT_CONTROLLED
Returns true if the specified object is controlled by a script

**Class:** `Object.IsScriptControlled`
**Flags:** condition

**Input:**
- `self: Object`

---

### `0E0D` MARK_OBJECT_AS_NEEDED
marks object as script controlled

**Class:** `Object.MarkAsNeeded`

**Input:**
- `self: Object`

---

### `0E1A` INIT_EXTENDED_OBJECT_VARS
Inits additional variables for this object. Identifier can be "AUTO" for unique ID based on script pointer

**Class:** `Object.InitExtendedVars`
**Flags:** condition

**Input:**
- `self: Object`
- `identifier: string`
- `totalVars: int`

---

### `0E1B` SET_EXTENDED_OBJECT_VAR
Sets extended var value for this object. Requires initialization (0E1A), otherwise returns false

**Class:** `Object.SetExtendedVar`
**Flags:** condition

**Input:**
- `self: Object`
- `identifier: string`
- `varNumber: int`
- `value: any`

---

### `0E1C` GET_EXTENDED_OBJECT_VAR
Gets extended var value for this char. Returns false if not initialized (0E1A)

**Class:** `Object.GetExtendedVar`
**Flags:** condition

**Input:**
- `self: Object`
- `identifier: string`
- `varNumber: int`

**Output:**
- `value: any (variable)`

---

### `0E71` GET_OBJECT_CENTRE_OF_MASS_TO_BASE_OF_MODEL
Gets the distance between the object model's center of mass to its base

**Class:** `Object.GetDistanceFromCenterOfMassToBaseOfModel`

**Input:**
- `self: Object`

**Output:**
- `distance: float (variable)`

---

### `0E94` IS_OBJECT_REALLY_IN_AIR
Returns True if the specified object is not on a solid surface and not submerged

**Class:** `Object.IsReallyInAir`
**Flags:** condition

**Input:**
- `self: Object`

---

### `0E95` SIMULATE_OBJECT_DAMAGE
Simulates the specified damage amount and weaponType on the object

**Class:** `Object.SimulateDamage`

**Input:**
- `self: Object`
- `damage: float`
- `weaponType: WeaponType`

---

### `0EAE` GET_OBJECT_PROOFS
Returns the specified object's damage proofs

**Class:** `Object.GetProofs`

**Input:**
- `self: Object`

**Output:**
- `bullet: bool (variable)`
- `fire: bool (variable)`
- `explosion: bool (variable)`
- `collision: bool (variable)`
- `melee: bool (variable)`

---

### `0ECA` GET_OBJECT_RANDOM_SEED
Returns the randomSeed of the specified object

**Class:** `Object.GetRandomSeed`

**Input:**
- `self: Object`

**Output:**
- `randomSeed: int (variable)`

---

### `0EE9` LOCATE_OBJECT_DISTANCE_TO_OBJECT
Returns True if the object(self) is within the radius of the specified object

**Class:** `Object.LocateDistanceToObject`
**Flags:** condition

**Input:**
- `self: Object`
- `object: Object`
- `radius: float`

---

### `0EEC` LOCATE_OBJECT_DISTANCE_TO_COORDINATES
Returns True if the object is within the radius of the specified coordinates

**Class:** `Object.LocateDistanceToCoordinates`
**Flags:** condition

**Input:**
- `self: Object`
- `x: float`
- `y: float`
- `z: float`
- `radius: float`

---

### `0F03` CREATE_RENDER_OBJECT_TO_OBJECT

**Class:** `Object.CreateRenderObjectToObject`

**Input:**
- `self: Object`
- `modelId: model_any`
- `x: float`
- `y: float`
- `z: float`
- `rx: float`
- `ry: float`
- `rz: float`

**Output:**
- `renderobject: int (variable)`

---

### `0F04` CREATE_RENDER_OBJECT_TO_OBJECT_FROM_SPECIAL

**Class:** `Object.CreateRenderObjectToObjectFromSpecial`

**Input:**
- `self: Object`
- `specialModel: int`
- `x: float`
- `y: float`
- `z: float`
- `rx: float`
- `ry: float`
- `rz: float`

**Output:**
- `renderobject: int (variable)`

---

### Pad

### `0E3D` IS_KEY_JUST_PRESSED
Returns true if the player has just started to press a specified key this frame

**Class:** `Pad.IsKeyJustPressed`
**Flags:** condition, static

**Input:**
- `keyCode: KeyCode`

---

### `0E3E` IS_BUTTON_JUST_PRESSED
Returns true if the pad's button has just started to be pressed this frame

**Class:** `Pad.IsButtonJustPressed`
**Flags:** condition, static

**Input:**
- `pad: PadId`
- `buttonId: Button`

---

### `0E67` IS_AIM_BUTTON_PRESSED
Returns True if the pad's aim button is pressed

**Class:** `Pad.IsAimButtonPressed`
**Flags:** condition, static

**Input:**
- `pad: PadId`

---

### `0E68` SET_PLAYER_CONTROL_PAD
Enables the specified control pad

**Class:** `Pad.SetControl`
**Flags:** static

**Input:**
- `pad: PadId`
- `enabled: bool`

---

### `0E69` SET_PLAYER_CONTROL_PAD_MOVEMENT
Enables the specified control pad's movement

**Class:** `Pad.SetMovement`
**Flags:** static

**Input:**
- `pad: PadId`
- `movement: bool`

---

### `0E8D` IS_ANY_FIRE_BUTTON_PRESSED
Returns True if the pad's primary or secondary fire button is pressed

**Class:** `Pad.IsAnyFireButtonPressed`
**Flags:** condition, static

**Input:**
- `pad: PadId`

---

### `0F13` GET_TIME_NOT_TOUCHING_PAD
Returns the time in milliseconds since the pad has been touched

**Class:** `Pad.GetTimeNotTouching`
**Flags:** static

**Input:**
- `pad: PadId`

**Output:**
- `timeInMs: int (variable)`

---

### Pickup

### `0E34` GET_PICKUP_MODEL
Returns the model of a specified pickup

**Class:** `Pickup.GetModel`
**Flags:** condition

**Input:**
- `self: Pickup`

**Output:**
- `modelId: model_any (variable)`

---

### `0E38` GET_PICKUP_POINTER
Returns a pointer to the struct of a specified pickup

**Class:** `Pickup.GetPointer`
**Flags:** condition

**Input:**
- `self: Pickup`

**Output:**
- `pointer: int (variable)`

---

### `0E39` GET_PICKUP_TYPE
Returns the type of a specified pickup

**Class:** `Pickup.GetType`

**Input:**
- `self: Pickup`

**Output:**
- `type: PickupType (variable)`

---

### Player

### `0E5E` CHANGE_PLAYER_MONEY
Changes player money by set, add or remove

**Class:** `Player.ChangeMoney`

**Input:**
- `self: Player`
- `mode: ChangeMoney`
- `value: int`

---

### RenderObject

### `0E2E` CREATE_RENDER_OBJECT_TO_CHAR_BONE
Creates renderObject to character bone

**Class:** `RenderObject.CreateToCharBone`
**Flags:** constructor

**Input:**
- `char: Char`
- `modelId: model_object`
- `pedBone: PedBone`
- `x: float`
- `y: float`
- `z: float`
- `rx: float`
- `ry: float`
- `rz: float`

**Output:**
- `handle: RenderObject (variable)`

---

### `0E2F` DELETE_RENDER_OBJECT
Deletes the renderObject

**Class:** `RenderObject.Delete`
**Flags:** destructor

**Input:**
- `self: RenderObject`

---

### `0E31` SET_RENDER_OBJECT_VISIBLE
Sets the visible status of the renderObject

**Class:** `RenderObject.SetVisible`

**Input:**
- `self: RenderObject`
- `visible: bool`

---

### `0E35` SET_RENDER_OBJECT_POSITION
Sets the position of a renderObject

**Class:** `RenderObject.SetPosition`

**Input:**
- `self: RenderObject`
- `x: float`
- `y: float`
- `z: float`

---

### `0E36` SET_RENDER_OBJECT_ROTATION
Sets the rotation of the renderObject

**Class:** `RenderObject.SetRotation`

**Input:**
- `self: RenderObject`
- `x: float`
- `y: float`
- `z: float`

---

### `0E37` SET_RENDER_OBJECT_SCALE
Sets the scale of the renderObject

**Class:** `RenderObject.SetScale`

**Input:**
- `self: RenderObject`
- `x: float`
- `y: float`
- `z: float`

---

### `0E3A` SET_RENDER_OBJECT_DISTORTION
Sets the renderObject's distortion

**Class:** `RenderObject.SetDistortion`

**Input:**
- `self: RenderObject`
- `x: float`
- `y: float`
- `z: float`
- `w: float`

---

### Streaming

### `0E7F` GET_MODEL_TYPE
Returns the type of the specified model

**Class:** `Streaming.GetModelType`
**Flags:** static

**Input:**
- `model: model_any`

**Output:**
- `type: ModelInfoType (variable)`

---

### `0E98` REQUEST_PRIORITY_MODEL
Requests a priority modelID to be loaded

**Class:** `Streaming.RequestPriorityModel`
**Flags:** static

**Input:**
- `modelId: model_any`

---

### `0E99` LOAD_ALL_PRIORITY_MODELS_NOW
This is a duplicate of LOAD_ALL_MODELS_NOW

**Class:** `Streaming.LoadAllPriorityModelsNow`
**Flags:** static

---

### `0E9A` LOAD_SPECIAL_CHARACTER_FOR_ID

**Class:** `Streaming.LoadSpecialCharacterForId`
**Flags:** static

**Input:**
- `id: int`
- `name: string`

---

### `0E9B` UNLOAD_SPECIAL_CHARACTER_FROM_ID

**Class:** `Streaming.UnloadSpecialCharacterFromId`
**Flags:** static

**Input:**
- `id: int`

---

### `0E9C` GET_MODEL_BY_NAME
Returns the modelID by name

**Class:** `Streaming.GetModelByName`
**Flags:** static, condition

**Input:**
- `name: string`

**Output:**
- `modelId: model_any (variable)`

---

### `0E9D` IS_MODEL_AVAILABLE_BY_NAME
Returns true if the specified model name is available as a valid special character

**Class:** `Streaming.IsModelAvailableByName`
**Flags:** condition, static

**Input:**
- `name: string`

---

### `0E9F` REMOVE_ALL_UNUSED_MODELS

**Class:** `Streaming.RemoveAllUnusedModels`
**Flags:** static

---

### `0EA3` REMOVE_MODEL_IF_UNUSED
Removes the specified ModelID from memory if unused

**Class:** `Streaming.RemoveModelIfUnused`
**Flags:** static

**Input:**
- `modelId: model_any`

---

### `0EF8` GET_MODEL_INFO
Returns the address of the modelInfo of the specified modelId

**Class:** `Streaming.GetModelInfo`
**Flags:** static, condition

**Input:**
- `modelId: model_any`

**Output:**
- `modelInfo: int (variable)`

---

### `0F00` LOAD_SPECIAL_MODEL

**Class:** `Streaming.LoadSpecialModel`
**Flags:** static, condition

**Input:**
- `dff: string`
- `txd: string`

**Output:**
- `specialModel: int (variable)`

---

### `0F01` REMOVE_SPECIAL_MODEL

**Class:** `Streaming.RemoveSpecialModel`
**Flags:** static

**Input:**
- `specialModel: int`

---

### `0F05` GET_SPECIAL_MODEL_DATA

**Class:** `Streaming.GetSpecialModelData`
**Flags:** static

**Input:**
- `specialModel: int`

**Output:**
- `clump: int (variable)`
- `atomic: int (variable)`
- `txdIndex: int (variable)`

---

### Text

### `0D4C` GET_STRING_LENGTH
Returns the string length

**Class:** `Text.GetStringLength`
**Flags:** static

**Input:**
- `text: string`

**Output:**
- `length: int (variable)`

---

### `0D4D` COPY_STRING
Copies the string to the specified address

**Class:** `Text.CopyString`
**Flags:** static

**Input:**
- `string: string`
- `address: int`

---

### `0E62` DRAW_STRING
Draws string once on specific drawing event

**Class:** `Text.DrawString`
**Flags:** static

**Input:**
- `string: string`
- `drawEvent: DrawEvent`
- `posX: float`
- `posY: float`
- `sizeX: float`
- `sizeY: float`
- `fixAr: bool`
- `font: Font`

---

### `0E63` DRAW_STRING_EXT
Draws string once on specific drawing event with extended text styling

**Class:** `Text.DrawStringExt`
**Flags:** static

**Input:**
- `string: string`
- `drawEvent: DrawEvent`
- `posX: float`
- `posY: float`
- `sizeX: float`
- `sizeY: float`
- `fixAr: bool`
- `font: Font`
- `prop: bool`
- `align: Align`
- `wrap: float`
- `justify: bool`
- `red: int`
- `green: int`
- `blue: int`
- `alpha: int`
- `edge: int`
- `shadow: int`
- `dropRed: int`
- `dropGreen: int`
- `dropBlue: int`
- `dropAlpha: int`
- `background: bool`
- `backRed: int`
- `backGreen: int`
- `backBlue: int`
- `backAlpha: int`

---

### `0E80` IS_STRING_EQUAL
Returns True if string1 and string2 match

**Class:** `Text.IsStringEqual`
**Flags:** static, condition

**Input:**
- `string1: string`
- `string2: string`
- `maxSize: int`
- `caseSensitive: bool`
- `ignoreCharacter: string`

---

### `0E81` IS_STRING_COMMENT
Returns True if the string starts with a hash (#), semicolon (;) or double slash (//)

**Class:** `Text.IsStringComment`
**Flags:** static, condition

**Input:**
- `string: string`

---

### `0EC2` SET_STRING_UPPER
Sets the string at the specified address to all upper case

**Class:** `Text.SetStringUpper`
**Flags:** static

**Input:**
- `stringAddress: int`

---

### `0EC3` SET_STRING_LOWER
Sets the string at the specified address to all lower case

**Class:** `Text.SetStringLower`
**Flags:** static

**Input:**
- `stringAddress: int`

---

### `0EC4` STRING_FIND
Returns the character index where strFind is found within stringOrigin

**Class:** `Text.StringFind`
**Flags:** static, condition

**Input:**
- `stringFind: StringFind`
- `stringOrigin: string`
- `strFind: string`

**Output:**
- `index: int (variable)`

---

### `0EC5` CUT_STRING_AT
Cuts stringAddress at the specified character index

**Class:** `Text.CutStringAt`
**Flags:** static

**Input:**
- `stringAddress: int`
- `index: int`

---

### `0EC6` IS_STRING_CHARACTER_AT
Returns True if the specified characters are found at the index of the string

**Class:** `Text.IsStringCharacterAt`
**Flags:** static, condition

**Input:**
- `string: string`
- `characters: string`
- `index: int`

---

### Txd

### `0E1E` DRAW_TEXTURE_PLUS
Draws RwTexture or spriteSlot once on specific drawing event and optional mask, no limits

**Class:** `Txd.DrawTexturePlus`
**Flags:** static

**Input:**
- `rwTextureOrSprite: int`
- `drawEvent: DrawEvent`
- `posX: float`
- `posY: float`
- `sizeX: float`
- `sizeY: float`
- `angle: float`
- `depth: float`
- `fixAr: bool`
- `maskVertCount: int`
- `maskVertArray: int`
- `red: int`
- `green: int`
- `blue: int`
- `alpha: int`

---

### `0E3C` GET_TEXTURE_FROM_SPRITE
Returns the rwTexture pointer from sprite index

**Class:** `Txd.GetTextureFromSprite`
**Flags:** static

**Input:**
- `spriteSlot: int`

**Output:**
- `rwTexture: int (variable)`

---

### Weapon

### `0E26` IS_WEAPON_FIRE_TYPE
Checks if the weapon has the specified fire type

**Class:** `Weapon.IsFireType`
**Flags:** condition, static

**Input:**
- `weaponType: WeaponType`
- `weaponFire: WeaponFire`

---

### `0E84` GET_WEAPONINFO
Returns a pointer to the CWeaponInfo struct of the the specified weaponType and weaponSkill

**Class:** `Weapon.GetWeaponInfo`
**Flags:** condition, constructor, static

**Input:**
- `weaponType: WeaponType`
- `weaponSkill: WeaponSkill`

**Output:**
- `handle: WeaponInfo (variable)`

**Details:**

This command returns a pointer to a static `CWeaponInfo` struct that holds data from [`weapon.dat`](https://gtamods.com/wiki/Weapon.dat#San_Andreas) for the given weapontype and skill.

The `CWeaponInfo` struct has the following layout:

```
00000000 CWeaponInfo     struc
00000000 m_eFireType     dd ?
00000004 targetRange     dd ?
00000008 m_fWeaponRange  dd ?
0000000C dwModelId1      dd ?
00000010 dwModelId2      dd ?
00000014 nSlot           dd ?
00000018 m_nFlags        dd ?
0000001C AssocGroupId    dd ?
00000020 ammoClip        dw ?
00000022 damage          dw ?
00000024 fireOffset      RwV3d ?
00000030 skillLevel      dd ?
00000034 reqStatLevelToGetThisWeaponSkilLevel dd ?
00000038 m_fAccuracy     dd ?
0000003C moveSpeed       dd ?
00000040 animLoopStart   dd ?
00000044 animLoopEnd     dd ?
00000048 animLoopFire    dd ?
0000004C animLoop2Start  dd ?
00000050 animLoop2End    dd ?
00000054 animLoop2Fire   dd ?
00000058 breakoutTime    dd ?
0000005C speed           dd ?
00000060 radius          dd ?
00000064 lifespan        dd ?
00000068 spread          dd ?
0000006C AssocGroupId2   db ?
0000006D field_6D        db ?
0000006E baseCombo       db ?
0000006F m_nNumCombos    db ?
00000070 CWeaponInfo     ends
```

Individual fields can be read with READ_MEMORY or specialized commands, like GET_WEAPONINFO_ANIMGROUP or GET_WEAPONINFO_FLAGS.

---

### WeaponInfo

### `0E85` GET_WEAPONINFO_MODELS
Returns the model1 and model2 of the current weaponInfo struct

**Class:** `WeaponInfo.GetModels`

**Input:**
- `self: WeaponInfo`

**Output:**
- `model1: model_any (variable)`
- `model2: model_any (variable)`

---

### `0E86` GET_WEAPONINFO_FLAGS
Returns the flags of the specified WeaponInfo struct

**Class:** `WeaponInfo.GetFlags`

**Input:**
- `self: WeaponInfo`

**Output:**
- `flags: int (variable)`

---

### `0E87` GET_WEAPONINFO_ANIMGROUP
Returns the FireType of the current weaponInfo struct

**Class:** `WeaponInfo.GetAnimgroup`

**Input:**
- `self: WeaponInfo`

**Output:**
- `animGroup: AnimGrp (variable)`

---

### `0E88` GET_WEAPONINFO_TOTAL_CLIP
Returns the totalClip size for the current weaponInfo struct

**Class:** `WeaponInfo.GetTotalClip`

**Input:**
- `self: WeaponInfo`

**Output:**
- `totalClip: int (variable)`

---

### `0E89` GET_WEAPONINFO_FIRE_TYPE
Returns the FireType of the current weaponInfo struct

**Class:** `WeaponInfo.GetFireType`

**Input:**
- `self: WeaponInfo`

**Output:**
- `fireType: WeaponFire (variable)`

---

### `0E8A` GET_WEAPONINFO_SLOT
Returns the weaponSlot of the current weaponInfo struct

**Class:** `WeaponInfo.GetSlot`

**Input:**
- `self: WeaponInfo`

**Output:**
- `weaponSlot: WeaponSlot (variable)`

---

### Weather

### `0D59` GET_CURRENT_WEATHER
Gets weather type that is being blended from

**Class:** `Weather.GetCurrent`
**Flags:** static

**Output:**
- `type: WeatherType (variable)`

---

### `0E04` GET_NEXT_WEATHER
Gets weather type that is being blended to

**Class:** `Weather.GetNext`
**Flags:** static

**Output:**
- `type: WeatherType (variable)`

---

### `0E05` SET_NEXT_WEATHER
Sets weather type which will be blend to

**Class:** `Weather.SetNext`
**Flags:** static

**Input:**
- `type: WeatherType`

---

### `0E06` GET_RAIN_INTENSITY
Gets rain intensity in range of 0.0 to 1.0

**Class:** `Weather.GetRainIntensity`
**Flags:** static

**Output:**
- `intensity: float (variable)`

---

### `0E07` SET_RAIN_INTENSITY
Sets rain intensity in range of 0.0 to 1.0

**Class:** `Weather.SetRainIntensity`
**Flags:** static

**Input:**
- `intensity: float`

---

### `0E6C` GET_DAY_NIGHT_BALANCE
Returns the intensity of the night filter

**Class:** `Weather.GetDayNightBalance`
**Flags:** static

**Output:**
- `intensity: float (variable)`

---

### `0E6D` GET_UNDERWATERNESS
Returns the intensity of the underwater filter

**Class:** `Weather.GetUnderwaterness`
**Flags:** static

**Output:**
- `intensity: float (variable)`

---

### `0EB0` GET_FORCED_WEATHER
Returns the forced weather type

**Class:** `Weather.GetForced`
**Flags:** static

**Output:**
- `weather: WeatherType (variable)`

---

### World

### `0E33` GET_PICKUP_THIS_COORD
Returns the handle of a pickup at the specified coordinates

**Class:** `World.GetPickupThisCoord`
**Flags:** static, condition

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `onlyValid: bool`

**Output:**
- `handle: Pickup (variable)`

---

### `0E3F` CONVERT_3D_TO_SCREEN_2D
Returns 2D screen position and distance related text size for world coordinates between nearClip and farClip

**Class:** `World.Convert3DToScreen2D`
**Flags:** condition, static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `nearClip: bool`
- `farClip: bool`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `sizeX: float (variable)`
- `sizeY: float (variable)`

---

### `0EA6` GET_CLOSEST_COP_NEAR_POS
Returns the closestCop to the specified coordinates

**Class:** `World.GetClosestCopNearPos`
**Flags:** condition, static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `radius: float`
- `alive: bool`
- `inCar: bool`
- `onFoot: bool`

**Output:**
- `closestCop: Char (variable)`

---

### `0EA7` GET_ANY_CHAR_NO_SAVE_RECURSIVE
Returns the handle of anyChar in the pool, starting at the previously returned progress index

**Class:** `World.GetAnyCharNoSaveRecursive`
**Flags:** condition, static

**Input:**
- `progress: int`

**Output:**
- `progress: int (variable)`
- `anyChar: Char (variable)`

---

### `0EA8` GET_ANY_CAR_NO_SAVE_RECURSIVE
Returns the handle of anyCar in the pool, starting at the previously returned progress index

**Class:** `World.GetAnyCarNoSaveRecursive`
**Flags:** condition, static

**Input:**
- `progress: int`

**Output:**
- `progress: int (variable)`
- `anyCar: Car (variable)`

---

### `0EA9` GET_ANY_OBJECT_NO_SAVE_RECURSIVE
Returns the handle of anyObject in the pool, starting at the previously returned progress index

**Class:** `World.GetAnyObjectNoSaveRecursive`
**Flags:** condition, static

**Input:**
- `progress: int`

**Output:**
- `progress: int (variable)`
- `anyObject: Object (variable)`

---

### `0EF0` GET_COORD_FROM_ANGLED_DISTANCE
Returns 2D coordinates for a location relative to x and y at the specified angle and distance

**Class:** `World.GetCoordFromAngledDistance`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `angle: float`
- `distance: float`

**Output:**
- `x: float (variable)`
- `y: float (variable)`

---

### `0D01` ROTATE_MATRIX_ON_AXIS


**Input:**
- `matrix: int`
- `x: float`
- `y: float`
- `z: float`
- `angle: float`
- `rwCombine: RwCombine`

---

### `0D02` GET_MATRIX_X_ANGLE


**Input:**
- `matrix: int`

**Output:**
- `angle: float (variable)`

---

### `0D03` GET_MATRIX_Y_ANGLE


**Input:**
- `matrix: int`

**Output:**
- `angle: float (variable)`

---

### `0D04` GET_MATRIX_Z_ANGLE


**Input:**
- `matrix: int`

**Output:**
- `angle: float (variable)`

---

### `0D0A` GET_OFFSET_FROM_MATRIX_IN_WORLD_COORDS


**Input:**
- `matrix: int`
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0D16` SET_MATRIX_ROTATION_FROM_QUAT


**Input:**
- `matrix: int`
- `quat: int`

---

### `0D17` SET_QUAT_FROM_MATRIX


**Input:**
- `quat: int`
- `matrix: int`

---

### `0D18` ROTATE_QUAT_ON_AXIS


**Input:**
- `quat: int`
- `x: float`
- `y: float`
- `z: float`
- `angle: float`
- `rwCombine: RwCombine`

---

### `0D19` GET_NORMALISED_QUAT


**Input:**
- `quat: int`

**Output:**
- `quat: int (variable)`

---

### `0D1A` MULTIPLY_QUATS


**Input:**
- `quat1: int`
- `quat2: int`

**Output:**
- `quatResult: int (variable)`

---

### `0D1E` QUAT_SLERP


**Input:**
- `from: int`
- `to: int`
- `lambda: float`

**Output:**
- `result: int (variable)`

---

### `0D24` INITIALISE_QUAT


**Input:**
- `quat: int`
- `x: float`
- `y: float`
- `z: float`
- `real: float`

---

### `0D29` GET_QUAT_ELEMENTS


**Input:**
- `quat: int`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`
- `real: float (variable)`

---

### `0D2E` SET_SCRIPT_VAR
Sets value for script variable in index


**Input:**
- `scriptPointer: int`
- `varIndex: int`
- `value: any`

---

### `0D2F` GET_SCRIPT_VAR
Gets value from script variable index


**Input:**
- `scriptPointer: int`
- `varIndex: int`

**Output:**
- `result: any (variable)`

---

### `0E6F` STREAM_CUSTOM_SCRIPT_FROM_LABEL
Loads a custom script at the specified label


**Input:**
- `label: label`
- `params: arguments`

---

### `0E9E` GET_MODEL_DOESNT_EXIST_IN_RANGE


**Input:**
- `start: int`
- `end: int`

**Output:**
- `modelId: model_any (variable)`

---

### `0EB3` CONVERT_DIRECTION_TO_QUAT


**Input:**
- `quat: int`
- `x: float`
- `y: float`
- `z: float`

---

### `0EBA` GET_MODEL_PED_TYPE_AND_STAT
Returns the pedType and pedStat ID for the specified modelID

**Flags:** condition, static

**Input:**
- `modelId: model_char`

**Output:**
- `pedType: PedType (variable)`
- `pedStat: PedStat (variable)`

---

### `0ED0` RETURN_SCRIPT_EVENT
Returns from script event


---

### `0ED1` SET_SCRIPT_EVENT_SAVE_CONFIRMATION
Toggles script event during save, just before the game is saved


**Input:**
- `add: bool`
- `label: label`
- `saveSlot: int (variable)`

---

### `0ED2` SET_SCRIPT_EVENT_CHAR_DELETE
Toggles script event just after varChar is deleted


**Input:**
- `add: bool`
- `label: label`
- `char: Char (variable)`

---

### `0ED3` SET_SCRIPT_EVENT_CHAR_CREATE
Toggles script event just after varChar is created


**Input:**
- `add: bool`
- `label: label`
- `char: Char (variable)`

---

### `0ED4` SET_SCRIPT_EVENT_CAR_DELETE
Toggles script event just before some car is being deleted


**Input:**
- `add: bool`
- `label: label`
- `car: Car (variable)`

---

### `0ED5` SET_SCRIPT_EVENT_CAR_CREATE
Toggles script event just after some car is created


**Input:**
- `add: bool`
- `label: label`
- `car: Car (variable)`

---

### `0ED6` SET_SCRIPT_EVENT_OBJECT_DELETE
Toggles script event just before some object is being deleted


**Input:**
- `add: bool`
- `label: label`
- `object: Object (variable)`

---

### `0ED7` SET_SCRIPT_EVENT_OBJECT_CREATE
Toggles script event just after some object is created


**Input:**
- `add: bool`
- `label: label`
- `object: Object (variable)`

---

### `0ED8` SET_SCRIPT_EVENT_ON_MENU
Toggles script event to run during pause menu, or when just paused the game


**Input:**
- `add: bool`
- `label: label`
- `justPaused: bool (variable)`

---

### `0EDA` SET_SCRIPT_EVENT_CHAR_PROCESS
Toggles script event to run on each char once per frame


**Input:**
- `add: bool`
- `label: label`
- `char: Char (variable)`

---

### `0EDB` SET_SCRIPT_EVENT_CAR_PROCESS
Toggles script event to run on each car once per frame


**Input:**
- `add: bool`
- `label: label`
- `car: Car (variable)`

---

### `0EDC` SET_SCRIPT_EVENT_OBJECT_PROCESS
Toggles script event to run on each object once per frame. May be slow


**Input:**
- `add: bool`
- `label: label`
- `object: Object (variable)`

---

### `0EDD` SET_SCRIPT_EVENT_BUILDING_PROCESS
Toggles script event to run on each building (CBuilding/Entity) once per frame. CAUTION! Very slow


**Input:**
- `add: bool`
- `label: label`
- `entityPtr: int (variable)`

---

### `0EDE` SET_SCRIPT_EVENT_CHAR_DAMAGE
Toggles script event when some char receives any damage. Use 0EB5 to get damage data


**Input:**
- `add: bool`
- `label: label`
- `char: Char (variable)`

---

### `0EDF` SET_SCRIPT_EVENT_CAR_WEAPON_DAMAGE
Toggles script event to run when some car is damaged by weapon. Use 0EB6 to get damage data


**Input:**
- `add: bool`
- `label: label`
- `car: Car (variable)`

---

### `0EE0` SET_SCRIPT_EVENT_BULLET_IMPACT
Toggles script event to run when bullet impact. Char and entity can be invalid


**Input:**
- `add: bool`
- `label: label`
- `ownerPtr: int (variable)`
- `victimPtr: int (variable)`
- `weaponType: WeaponType (variable)`
- `colPoint: int (variable)`

---

### `0EF3` LERP


**Input:**
- `a: float`
- `b: float`
- `t: float`

**Output:**
- `result: float (variable)`

---

### `0F0A` RETURN_TIMES
Returns runReturns number of gosub levels


**Input:**
- `numReturns: int`

---

### `0F0B` SET_SCRIPT_EVENT_BEFORE_GAME_PROCESS


**Input:**
- `add: int`
- `label: label`

---

### `0F0C` SET_SCRIPT_EVENT_AFTER_GAME_PROCESS


**Input:**
- `add: int`
- `label: label`

---

### `0F0D` SET_MATRIX_LOOK_DIRECTION
Sets the matrix look direction


**Input:**
- `matrix: int`
- `originX: float`
- `originY: float`
- `originZ: float`
- `dirX: float`
- `dirY: float`
- `dirZ: float`

---

### `0F0F` GET_DISTANCE_MULTIPLIER
Returns the games drawing and generating distance multipliers


**Output:**
- `drawing: float (variable)`
- `generating: float (variable)`

---

### `0F11` GET_CLOSEST_WATER_DISTANCE
Returns the closest water distance and z level


**Output:**
- `distance: float (variable)`
- `closestZ: float (variable)`

---

### `0F17` GET_MODEL_NAME_POINTER
Returns the address of the name of any modelId


**Input:**
- `modelId: model_any`

**Output:**
- `address: int (variable)`

---
