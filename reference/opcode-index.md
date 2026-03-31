# Opcode Index

Searchable index of all opcodes. Use Ctrl+F / grep to find opcodes by ID or name.

| Opcode | Name | Class | Extension | Params | Description |
|--------|------|-------|-----------|--------|-------------|
| `0000` | NOP |  | default | 0 | Has no effect and is commonly used to pad CLEO scripts with extra space to avoid the jump-at-zero-offset bug |
| `0001` | WAIT |  | default | 1 | Pauses the script execution for specified amount of time in milliseconds |
| `0002` | GOTO |  | default | 1 | Transfers the script execution to the label unconditionally |
| `0003` | SHAKE_CAM | Camera | default | 1 | Shakes the camera with the given intensity |
| `0004` | SET_VAR_INT |  | default | 2 | Sets the integer value of the VAR |
| `0005` | SET_VAR_FLOAT |  | default | 2 | Sets the float value of the VAR |
| `0006` | SET_LVAR_INT |  | default | 2 | Sets the integer value of the LVAR |
| `0007` | SET_LVAR_FLOAT |  | default | 2 | Sets the float value of the LVAR |
| `0008` | ADD_VAL_TO_INT_VAR |  | default | 2 | Adds the value to the value of the int VAR |
| `0009` | ADD_VAL_TO_FLOAT_VAR |  | default | 2 | Adds the value to the value of the float VAR |
| `000A` | ADD_VAL_TO_INT_LVAR |  | default | 2 | Adds the value to the value of the integer LVAR |
| `000B` | ADD_VAL_TO_FLOAT_LVAR |  | default | 2 | Adds the value to the value of the float LVAR |
| `000C` | SUB_VAL_FROM_INT_VAR |  | default | 2 | Subtracts the value from the value of the integer VAR |
| `000D` | SUB_VAL_FROM_FLOAT_VAR |  | default | 2 | Subtracts the value from the value of the float VAR |
| `000E` | SUB_VAL_FROM_INT_LVAR |  | default | 2 | Subtracts the value from the value of the int LVAR |
| `000F` | SUB_VAL_FROM_FLOAT_LVAR |  | default | 2 | Subtracts the value from the value of the float LVAR |
| `0010` | MULT_INT_VAR_BY_VAL |  | default | 2 | Multiplies the int VAR by the value |
| `0011` | MULT_FLOAT_VAR_BY_VAL |  | default | 2 | Multiplies the float VAR by the value |
| `0012` | MULT_INT_LVAR_BY_VAL |  | default | 2 | Multiplies the int LVAR by the value |
| `0013` | MULT_FLOAT_LVAR_BY_VAL |  | default | 2 | Multiplies the float LVAR by the value |
| `0014` | DIV_INT_VAR_BY_VAL |  | default | 2 | Divides the int VAR by the value |
| `0015` | DIV_FLOAT_VAR_BY_VAL |  | default | 2 | Divides the float VAR by the value |
| `0016` | DIV_INT_LVAR_BY_VAL |  | default | 2 | Divides the int LVAR by the value |
| `0017` | DIV_FLOAT_LVAR_BY_VAL |  | default | 2 | Divides the float LVAR by the value |
| `0018` | IS_INT_VAR_GREATER_THAN_NUMBER |  | default | 2 | Returns true if the int VAR value is greater than the value |
| `0019` | IS_INT_LVAR_GREATER_THAN_NUMBER |  | default | 2 | Returns true if the int LVAR value is greater than the value |
| `001A` | IS_NUMBER_GREATER_THAN_INT_VAR |  | default | 2 | Returns true if the value is greater than the int VAR value |
| `001B` | IS_NUMBER_GREATER_THAN_INT_LVAR |  | default | 2 | Returns true if the value is greater than the int LVAR value |
| `001C` | IS_INT_VAR_GREATER_THAN_INT_VAR |  | default | 2 | Returns true if the int VAR value is greater than the other int VAR value |
| `001D` | IS_INT_LVAR_GREATER_THAN_INT_LVAR |  | default | 2 | Returns true if the int LVAR value is greater than the other int LVAR value |
| `001E` | IS_INT_VAR_GREATER_THAN_INT_LVAR |  | default | 2 | Returns true if the int VAR value is greater than the int LVAR value |
| `001F` | IS_INT_LVAR_GREATER_THAN_INT_VAR |  | default | 2 | Returns true if the int LVAR value is greater than the int VAR value |
| `0020` | IS_FLOAT_VAR_GREATER_THAN_NUMBER |  | default | 2 | Returns true if the float VAR value is greater than the float value |
| `0021` | IS_FLOAT_LVAR_GREATER_THAN_NUMBER |  | default | 2 | Returns true if the float LVAR value is greater than the float value |
| `0022` | IS_NUMBER_GREATER_THAN_FLOAT_VAR |  | default | 2 | Returns true if the float value is greater than the float VAR value |
| `0023` | IS_NUMBER_GREATER_THAN_FLOAT_LVAR |  | default | 2 | Returns true if the float value is greater than the float LVAR value |
| `0024` | IS_FLOAT_VAR_GREATER_THAN_FLOAT_VAR |  | default | 2 | Returns true if the float VAR value is greater than the other float VAR value |
| `0025` | IS_FLOAT_LVAR_GREATER_THAN_FLOAT_LVAR |  | default | 2 | Returns true if the float LVAR value is greater than the other float LVAR value |
| `0026` | IS_FLOAT_VAR_GREATER_THAN_FLOAT_LVAR |  | default | 2 | Returns true if the float VAR value is greater than the float LVAR value |
| `0027` | IS_FLOAT_LVAR_GREATER_THAN_FLOAT_VAR |  | default | 2 | Returns true if the float LVAR value is greater than the float VAR value |
| `0028` | IS_INT_VAR_GREATER_OR_EQUAL_TO_NUMBER |  | default | 2 | Returns true if the int VAR value is greater or equal to the value |
| `0029` | IS_INT_LVAR_GREATER_OR_EQUAL_TO_NUMBER |  | default | 2 | Returns true if the int LVAR value is greater or equal to the value |
| `002A` | IS_NUMBER_GREATER_OR_EQUAL_TO_INT_VAR |  | default | 2 | Returns true if the value is greater or equal to the int VAR value |
| `002B` | IS_NUMBER_GREATER_OR_EQUAL_TO_INT_LVAR |  | default | 2 | Returns true if the value is greater or equal to the int LVAR value |
| `002C` | IS_INT_VAR_GREATER_OR_EQUAL_TO_INT_VAR |  | default | 2 | Returns true if the int VAR value is greater or equal to the other int VAR value |
| `002D` | IS_INT_LVAR_GREATER_OR_EQUAL_TO_INT_LVAR |  | default | 2 | Returns true if the int LVAR value is greater or equal to the other int LVAR value |
| `002E` | IS_INT_VAR_GREATER_OR_EQUAL_TO_INT_LVAR |  | default | 2 | Returns true if the int VAR value is greater or equal to the int LVAR value |
| `002F` | IS_INT_LVAR_GREATER_OR_EQUAL_TO_INT_VAR |  | default | 2 | Returns true if the int LVAR value is greater or equal to the int VAR value |
| `0030` | IS_FLOAT_VAR_GREATER_OR_EQUAL_TO_NUMBER |  | default | 2 | Returns true if the float VAR value is greater or equal to the value |
| `0031` | IS_FLOAT_LVAR_GREATER_OR_EQUAL_TO_NUMBER |  | default | 2 | Returns true if the float LVAR value is greater or equal to the value |
| `0032` | IS_NUMBER_GREATER_OR_EQUAL_TO_FLOAT_VAR |  | default | 2 | Returns true if the value is greater or equal to the float VAR value |
| `0033` | IS_NUMBER_GREATER_OR_EQUAL_TO_FLOAT_LVAR |  | default | 2 | Returns true if the value is greater or equal to the float LVAR value |
| `0034` | IS_FLOAT_VAR_GREATER_OR_EQUAL_TO_FLOAT_VAR |  | default | 2 | Returns true if the float VAR value is greater or equal to the other float VAR value |
| `0035` | IS_FLOAT_LVAR_GREATER_OR_EQUAL_TO_FLOAT_LVAR |  | default | 2 | Returns true if the float LVAR value is greater or equal to the other float LVAR value |
| `0036` | IS_FLOAT_VAR_GREATER_OR_EQUAL_TO_FLOAT_LVAR |  | default | 2 | Returns true if the float VAR value is greater or equal to the LVAR value |
| `0037` | IS_FLOAT_LVAR_GREATER_OR_EQUAL_TO_FLOAT_VAR |  | default | 2 | Returns true if the float LVAR value is greater or equal to the float VAR value |
| `0038` | IS_INT_VAR_EQUAL_TO_NUMBER |  | default | 2 | Returns true if the int VAR value is equal to the value |
| `0039` | IS_INT_LVAR_EQUAL_TO_NUMBER |  | default | 2 | Returns true if the int LVAR value is equal to the value |
| `003A` | IS_INT_VAR_EQUAL_TO_INT_VAR |  | default | 2 | Returns true if the int VAR value is equal to the other int VAR value |
| `003B` | IS_INT_LVAR_EQUAL_TO_INT_LVAR |  | default | 2 | Returns true if the int LVAR value is equal to the other int LVAR value |
| `003C` | IS_INT_VAR_EQUAL_TO_INT_LVAR |  | default | 2 | Returns true if the int VAR value is equal to the int LVAR value |
| `003D` | IS_INT_VAR_NOT_EQUAL_TO_NUMBER |  | default | 0 |  |
| `003E` | IS_INT_LVAR_NOT_EQUAL_TO_NUMBER |  | default | 0 |  |
| `003F` | IS_INT_VAR_NOT_EQUAL_TO_INT_VAR |  | default | 0 |  |
| `0040` | IS_INT_LVAR_NOT_EQUAL_TO_INT_LVAR |  | default | 0 |  |
| `0041` | IS_INT_VAR_NOT_EQUAL_TO_INT_LVAR |  | default | 0 |  |
| `0042` | IS_FLOAT_VAR_EQUAL_TO_NUMBER |  | default | 2 | Returns true if the float VAR value is equal to the value |
| `0043` | IS_FLOAT_LVAR_EQUAL_TO_NUMBER |  | default | 2 | Returns true if the float LVAR value is equal to the value |
| `0044` | IS_FLOAT_VAR_EQUAL_TO_FLOAT_VAR |  | default | 2 | Returns true if the float VAR value is equal to the other float VAR value |
| `0045` | IS_FLOAT_LVAR_EQUAL_TO_FLOAT_LVAR |  | default | 2 | Returns true if the float LVAR value is equal to the other float LVAR value |
| `0046` | IS_FLOAT_VAR_EQUAL_TO_FLOAT_LVAR |  | default | 2 | Returns true if the float VAR value is equal to the float LVAR value |
| `0047` | IS_FLOAT_VAR_NOT_EQUAL_TO_NUMBER |  | default | 0 |  |
| `0048` | IS_FLOAT_LVAR_NOT_EQUAL_TO_NUMBER |  | default | 0 |  |
| `0049` | IS_FLOAT_VAR_NOT_EQUAL_TO_FLOAT_VAR |  | default | 0 |  |
| `004A` | IS_FLOAT_LVAR_NOT_EQUAL_TO_FLOAT_LVAR |  | default | 0 |  |
| `004B` | IS_FLOAT_VAR_NOT_EQUAL_TO_FLOAT_LVAR |  | default | 0 |  |
| `004C` | GOTO_IF_TRUE |  | default | 0 |  |
| `004D` | GOTO_IF_FALSE |  | default | 1 | Transfers the script execution to the label if the condition result is false |
| `004E` | TERMINATE_THIS_SCRIPT |  | default | 0 | Ends the current script, preventing further execution |
| `004F` | START_NEW_SCRIPT |  | default | 2 | Starts a new script at the specified label |
| `0050` | GOSUB |  | default | 1 | Transfers the script execution to the label as a subroutine |
| `0051` | RETURN |  | default | 0 | Returns from the current subroutine (0050) |
| `0052` | LINE | Debugger | default | 6 | Displays 6 floating-point values on the screen |
| `0053` | CREATE_PLAYER | Player | default | 5 | Creates a player at the specified location |
| `0054` | GET_PLAYER_COORDINATES |  | default | 0 |  |
| `0055` | SET_PLAYER_COORDINATES |  | default | 0 |  |
| `0056` | IS_PLAYER_IN_AREA_2D |  | default | 0 |  |
| `0057` | IS_PLAYER_IN_AREA_3D |  | default | 0 |  |
| `0058` | ADD_INT_VAR_TO_INT_VAR |  | default | 2 | Adds the int VAR value to the other int VAR |
| `0059` | ADD_FLOAT_VAR_TO_FLOAT_VAR |  | default | 2 | Adds the float VAR value to the other float VAR |
| `005A` | ADD_INT_LVAR_TO_INT_LVAR |  | default | 2 | Adds the int LVAR value to the other int LVAR |
| `005B` | ADD_FLOAT_LVAR_TO_FLOAT_LVAR |  | default | 2 | Adds the float LVAR value to the other float LVAR |
| `005C` | ADD_INT_VAR_TO_INT_LVAR |  | default | 2 | Adds the int VAR value to the int LVAR |
| `005D` | ADD_FLOAT_VAR_TO_FLOAT_LVAR |  | default | 2 | Adds the float VAR value to the float LVAR |
| `005E` | ADD_INT_LVAR_TO_INT_VAR |  | default | 2 | Adds the float LVAR value to the float VAR |
| `005F` | ADD_FLOAT_LVAR_TO_FLOAT_VAR |  | default | 2 | Adds the float LVAR value to the float VAR |
| `0060` | SUB_INT_VAR_FROM_INT_VAR |  | default | 2 | Subtracts the int VAR value from the int VAR |
| `0061` | SUB_FLOAT_VAR_FROM_FLOAT_VAR |  | default | 2 | Subtracts the float VAR value from the float VAR |
| `0062` | SUB_INT_LVAR_FROM_INT_LVAR |  | default | 2 | Subtracts the int LVAR value from the int LVAR |
| `0063` | SUB_FLOAT_LVAR_FROM_FLOAT_LVAR |  | default | 2 | Subtracts the float LVAR value from the float LVAR |
| `0064` | SUB_INT_VAR_FROM_INT_LVAR |  | default | 2 | Subtracts the int VAR value from the int LVAR |
| `0065` | SUB_FLOAT_VAR_FROM_FLOAT_LVAR |  | default | 2 | Subtracts the float VAR value from the float LVAR |
| `0066` | SUB_INT_LVAR_FROM_INT_VAR |  | default | 2 | Subtracts the float LVAR value from the float VAR |
| `0067` | SUB_FLOAT_LVAR_FROM_FLOAT_VAR |  | default | 2 | Subtracts the float LVAR value from the float VAR |
| `0068` | MULT_INT_VAR_BY_INT_VAR |  | default | 2 | Multiplies the int VAR value by the int VAR |
| `0069` | MULT_FLOAT_VAR_BY_FLOAT_VAR |  | default | 2 | Multiplies the float VAR value by the float VAR |
| `006A` | MULT_INT_LVAR_BY_INT_LVAR |  | default | 2 | Multiplies the int LVAR value by the int LVAR |
| `006B` | MULT_FLOAT_LVAR_BY_FLOAT_LVAR |  | default | 2 | Multiplies the int LVAR value by the int LVAR |
| `006C` | MULT_INT_VAR_BY_INT_LVAR |  | default | 2 | Multiplies the int VAR value by the int LVAR |
| `006D` | MULT_FLOAT_VAR_BY_FLOAT_LVAR |  | default | 2 | Multiplies the float VAR value by the float LVAR |
| `006E` | MULT_INT_LVAR_BY_INT_VAR |  | default | 2 | Multiplies the int LVAR value by the int VAR |
| `006F` | MULT_FLOAT_LVAR_BY_FLOAT_VAR |  | default | 2 | Multiplies the float LVAR value by the float VAR |
| `0070` | DIV_INT_VAR_BY_INT_VAR |  | default | 2 | Divides the int VAR value by the int VAR |
| `0071` | DIV_FLOAT_VAR_BY_FLOAT_VAR |  | default | 2 | Divides the float VAR value by the float VAR |
| `0072` | DIV_INT_LVAR_BY_INT_LVAR |  | default | 2 | Divides the int LVAR by the int LVAR |
| `0073` | DIV_FLOAT_LVAR_BY_FLOAT_LVAR |  | default | 2 | Divides the float LVAR by the float LVAR |
| `0074` | DIV_INT_VAR_BY_INT_LVAR |  | default | 2 | Divides the int VAR by the int LVAR |
| `0075` | DIV_FLOAT_VAR_BY_FLOAT_LVAR |  | default | 2 | Divides the float VAR by the float LVAR |
| `0076` | DIV_INT_LVAR_BY_INT_VAR |  | default | 2 | Divides the int LVAR by the int VAR |
| `0077` | DIV_FLOAT_LVAR_BY_FLOAT_VAR |  | default | 2 | Divides the float LVAR by the float VAR |
| `0078` | ADD_TIMED_VAL_TO_FLOAT_VAR |  | default | 2 | Multiplies the delta time since the last frame by the specified value and adds the result to the specified variable |
| `0079` | ADD_TIMED_VAL_TO_FLOAT_LVAR |  | default | 2 | Multiplies the delta time since the last frame by the specified value and adds the result to the specified variable |
| `007A` | ADD_TIMED_FLOAT_VAR_TO_FLOAT_VAR |  | default | 2 | Multiplies the delta time since the last frame by the float value of the specified global variable and adds the result to the specified global variable |
| `007B` | ADD_TIMED_FLOAT_LVAR_TO_FLOAT_LVAR |  | default | 2 | Multiplies the delta time since the last frame by the float value of the specified local variable and adds the result to the specified local variable |
| `007C` | ADD_TIMED_FLOAT_VAR_TO_FLOAT_LVAR |  | default | 2 | Multiplies the delta time since the last frame by the float value of the specified global variable and adds the result to the specified local variable |
| `007D` | ADD_TIMED_FLOAT_LVAR_TO_FLOAT_VAR |  | default | 2 | Multiplies the delta time since the last frame by the float value of the specified local variable and adds the result to the specified global variable |
| `007E` | SUB_TIMED_VAL_FROM_FLOAT_VAR |  | default | 2 | Multiplies the delta time since the last frame by the specified float value and subtracts the result from the specified global variable |
| `007F` | SUB_TIMED_VAL_FROM_FLOAT_LVAR |  | default | 2 | Multiplies the delta time since the last frame by the specified value and subtracts the result from the specified local variable |
| `0080` | SUB_TIMED_FLOAT_VAR_FROM_FLOAT_VAR |  | default | 2 | Multiplies the delta time since the last frame by the value of the specified global variable and subtracts the result from the specified global variable |
| `0081` | SUB_TIMED_FLOAT_LVAR_FROM_FLOAT_LVAR |  | default | 2 | Multiplies the delta time since the last frame by the value of the specified local variable and adds the result to the specified local variable |
| `0082` | SUB_TIMED_FLOAT_VAR_FROM_FLOAT_LVAR |  | default | 2 | Multiplies the delta time since the last frame by the value of the specified global variable and subtracts the result from the specified local variable |
| `0083` | SUB_TIMED_FLOAT_LVAR_FROM_FLOAT_VAR |  | default | 2 | Multiplies the frame delta time (the time in milliseconds that has passed since the last frame) by float stored in the specified local variable |
| `0084` | SET_VAR_INT_TO_VAR_INT |  | default | 2 | Sets the int VAR to the VAR value |
| `0085` | SET_LVAR_INT_TO_LVAR_INT |  | default | 2 | Sets the int LVAR to the LVAR value |
| `0086` | SET_VAR_FLOAT_TO_VAR_FLOAT |  | default | 2 | Sets the float VAR to the VAR value |
| `0087` | SET_LVAR_FLOAT_TO_LVAR_FLOAT |  | default | 2 | Sets the float LVAR to the LVAR value |
| `0088` | SET_VAR_FLOAT_TO_LVAR_FLOAT |  | default | 2 | Sets the float VAR to the LVAR value |
| `0089` | SET_LVAR_FLOAT_TO_VAR_FLOAT |  | default | 2 | Sets the float LVAR to the VAR value |
| `008A` | SET_VAR_INT_TO_LVAR_INT |  | default | 2 | Sets the int VAR to the LVAR value |
| `008B` | SET_LVAR_INT_TO_VAR_INT |  | default | 2 | Sets the int LVAR to the VAR value |
| `008C` | CSET_VAR_INT_TO_VAR_FLOAT |  | default | 2 | Converts the float in the second global variable to an integer (via flooring) and stores the integer into the first global variable |
| `008D` | CSET_VAR_FLOAT_TO_VAR_INT |  | default | 2 | Converts the integer value of the second global variable to a float and stores the result in the first global variable |
| `008E` | CSET_LVAR_INT_TO_VAR_FLOAT |  | default | 2 | Converts the float value of the global variable to an integer (via flooring) and stores the result into a local variable |
| `008F` | CSET_LVAR_FLOAT_TO_VAR_INT |  | default | 2 | Converts the integer value of the global variable to a float and then stores the result in the local variable |
| `0090` | CSET_VAR_INT_TO_LVAR_FLOAT |  | default | 2 | Converts the float value of the local variable to an integer (via flooring) and stores the result to the global variable |
| `0091` | CSET_VAR_FLOAT_TO_LVAR_INT |  | default | 2 | Converts the integer value of the local variable to a float and stores the result in the global variable |
| `0092` | CSET_LVAR_INT_TO_LVAR_FLOAT |  | default | 2 | Converts a float value to an integer (via truncating) |
| `0093` | CSET_LVAR_FLOAT_TO_LVAR_INT |  | default | 2 | Converts the integer value of the second local variable to a float and stores the result to the first local variable |
| `0094` | ABS_VAR_INT | Math | default | 1 | Returns the absolute value of the global integer variable |
| `0095` | ABS_LVAR_INT | Math | default | 1 | Returns the absolute value of the local integer variable |
| `0096` | ABS_VAR_FLOAT | Math | default | 1 | Returns the absolute value of the global float variable |
| `0097` | ABS_LVAR_FLOAT | Math | default | 1 | Returns the absolute value of the local float variable |
| `0098` | GENERATE_RANDOM_FLOAT | Math | default | 1 | Returns a random float between 0.0 to 1.0; excluding 1.0 |
| `0099` | GENERATE_RANDOM_INT | Math | default | 1 | Returns a random integer between 0 and 32767 |
| `009A` | CREATE_CHAR | Char | default | 6 | Creates a character at the specified location, with the specified model and pedtype |
| `009B` | DELETE_CHAR | Char | default | 1 | Removes the character from the game and mission cleanup list, freeing game memory |
| `009C` | CHAR_WANDER_DIR |  | default | 0 |  |
| `009D` | CHAR_WANDER_RANGE |  | default | 0 |  |
| `009E` | CHAR_FOLLOW_PATH |  | default | 0 |  |
| `009F` | CHAR_SET_IDLE |  | default | 0 |  |
| `00A0` | GET_CHAR_COORDINATES | Char | default | 4 | Returns the character's coordinates |
| `00A1` | SET_CHAR_COORDINATES | Char | default | 4 | Puts the character at the specified location |
| `00A2` | IS_CHAR_STILL_ALIVE |  | default | 0 |  |
| `00A3` | IS_CHAR_IN_AREA_2D | Char | default | 6 | Returns true if the character is within the specified 2D area |
| `00A4` | IS_CHAR_IN_AREA_3D | Char | default | 8 | Returns true if the character is within the specified 3D area |
| `00A5` | CREATE_CAR | Car | default | 5 | Creates a vehicle at the specified location, with the specified model |
| `00A6` | DELETE_CAR | Car | default | 1 | Removes the vehicle from the game |
| `00A7` | CAR_GOTO_COORDINATES | Car | default | 4 | Makes the AI drive to the specified location by any means |
| `00A8` | CAR_WANDER_RANDOMLY | Car | default | 1 | Clears any current tasks the vehicle has and makes it drive around aimlessly |
| `00A9` | CAR_SET_IDLE | Car | default | 1 | Sets the car's mission to idle (MISSION_NONE), stopping any driving activity |
| `00AA` | GET_CAR_COORDINATES | Car | default | 4 | Returns the vehicle's coordinates |
| `00AB` | SET_CAR_COORDINATES | Car | default | 4 | Puts the vehicle at the specified location |
| `00AC` | IS_CAR_STILL_ALIVE |  | default | 0 |  |
| `00AD` | SET_CAR_CRUISE_SPEED | Car | default | 2 | Sets the vehicle's max speed |
| `00AE` | SET_CAR_DRIVING_STYLE | Car | default | 2 | Sets the behavior of the vehicle's AI driver |
| `00AF` | SET_CAR_MISSION | Car | default | 2 | Sets the mission of the vehicle's AI driver |
| `00B0` | IS_CAR_IN_AREA_2D | Car | default | 6 | Returns true if the vehicle is located within the specified 2D area |
| `00B1` | IS_CAR_IN_AREA_3D | Car | default | 8 | Returns true if the vehicle is located within the specified 3D area |
| `00B2` | SPECIAL_0 |  | default | 0 |  |
| `00B3` | SPECIAL_1 |  | default | 0 |  |
| `00B4` | SPECIAL_2 |  | default | 0 |  |
| `00B5` | SPECIAL_3 |  | default | 0 |  |
| `00B6` | SPECIAL_4 |  | default | 0 |  |
| `00B7` | SPECIAL_5 |  | default | 0 |  |
| `00B8` | SPECIAL_6 |  | default | 0 |  |
| `00B9` | SPECIAL_7 |  | default | 0 |  |
| `00BA` | PRINT_BIG | Text | default | 3 | Displays a styled message for the specified time |
| `00BB` | PRINT | Text | default | 3 | Displays a message positioned on the bottom of the screen for the specified time |
| `00BC` | PRINT_NOW | Text | default | 3 | Displays a message positioned on the bottom of the screen for the specified time |
| `00BD` | PRINT_SOON |  | default | 0 |  |
| `00BE` | CLEAR_PRINTS | Text | default | 0 | Clears all priority text and some styles of big texts |
| `00BF` | GET_TIME_OF_DAY | Clock | default | 2 | Returns the number of hours and minutes passed since midnight |
| `00C0` | SET_TIME_OF_DAY | Clock | default | 2 | Sets the current in-game time |
| `00C1` | GET_MINUTES_TO_TIME_OF_DAY | Clock | default | 3 | Returns the number of minutes left until the clock matches the time specified |
| `00C2` | IS_POINT_ON_SCREEN | Camera | default | 4 | Returns true if any part of the radius of the specified point is visible on screen |
| `00C3` | DEBUG_ON | Debugger | default | 0 | Activates debug features in this script |
| `00C4` | DEBUG_OFF | Debugger | default | 0 | Deactivates debug features in this script |
| `00C5` | RETURN_TRUE |  | default | 0 |  |
| `00C6` | RETURN_FALSE |  | default | 0 |  |
| `00C7` | VAR_INT |  | default | 0 |  |
| `00C8` | VAR_FLOAT |  | default | 0 |  |
| `00C9` | LVAR_INT |  | default | 0 |  |
| `00CA` | LVAR_FLOAT |  | default | 0 |  |
| `00CB` | { |  | default | 0 |  |
| `00CC` | } |  | default | 0 |  |
| `00CF` | IF_INTERNAL |  | default | 0 |  |
| `00D0` | IFNOT |  | default | 0 |  |
| `00D1` | ELSE |  | default | 0 |  |
| `00D2` | ENDIF |  | default | 0 |  |
| `00D3` | WHILE |  | default | 0 |  |
| `00D4` | WHILENOT |  | default | 0 |  |
| `00D5` | ENDWHILE |  | default | 0 |  |
| `00D6` | IF |  | default | 1 | Begins a conditional statement with the specified number of conditions |
| `00D7` | LAUNCH_MISSION |  | default | 1 | Launches a submission script |
| `00D8` | MISSION_HAS_FINISHED | Mission | default | 0 | Resets multiple settings that are usually set during missions and in some scripts |
| `00D9` | STORE_CAR_CHAR_IS_IN | Char | default | 2 | Returns the current vehicle of the character and adds it to the mission cleanup list (alts:03C0,0811,0484) |
| `00DA` | STORE_CAR_PLAYER_IS_IN |  | default | 0 |  |
| `00DB` | IS_CHAR_IN_CAR | Char | default | 2 | Returns true if the character is in the specified vehicle |
| `00DC` | IS_PLAYER_IN_CAR |  | default | 0 |  |
| `00DD` | IS_CHAR_IN_MODEL | Char | default | 2 | Returns true if the character is driving a vehicle with the specified model |
| `00DE` | IS_PLAYER_IN_MODEL |  | default | 0 |  |
| `00DF` | IS_CHAR_IN_ANY_CAR | Char | default | 1 | Returns true if the character has a vehicle, even if they are not actually sat inside it (opening and closing the door) |
| `00E0` | IS_PLAYER_IN_ANY_CAR |  | default | 0 |  |
| `00E1` | IS_BUTTON_PRESSED | Pad | default | 2 | Returns true if the pad's button has been pressed |
| `00E2` | GET_PAD_STATE | Pad | default | 3 | Stores the status of the specified key into a variable |
| `00E3` | LOCATE_PLAYER_ANY_MEANS_2D |  | default | 0 |  |
| `00E4` | LOCATE_PLAYER_ON_FOOT_2D |  | default | 0 |  |
| `00E5` | LOCATE_PLAYER_IN_CAR_2D |  | default | 0 |  |
| `00E6` | LOCATE_STOPPED_PLAYER_ANY_MEANS_2D |  | default | 0 |  |
| `00E7` | LOCATE_STOPPED_PLAYER_ON_FOOT_2D |  | default | 0 |  |
| `00E8` | LOCATE_STOPPED_PLAYER_IN_CAR_2D |  | default | 0 |  |
| `00E9` | LOCATE_PLAYER_ANY_MEANS_CHAR_2D |  | default | 0 |  |
| `00EA` | LOCATE_PLAYER_ON_FOOT_CHAR_2D |  | default | 0 |  |
| `00EB` | LOCATE_PLAYER_IN_CAR_CHAR_2D |  | default | 0 |  |
| `00EC` | LOCATE_CHAR_ANY_MEANS_2D | Char | default | 6 | Returns true if the character is within the 2D radius of the coordinates point |
| `00ED` | LOCATE_CHAR_ON_FOOT_2D | Char | default | 6 | Returns true if the character is within the 2D radius of the coordinates point on foot |
| `00EE` | LOCATE_CHAR_IN_CAR_2D | Char | default | 6 | Returns true if the character is within the 2D radius of the coordinates point in a vehicle |
| `00EF` | LOCATE_STOPPED_CHAR_ANY_MEANS_2D | Char | default | 6 | Returns true if the character stopped within the 2D radius of the coordinates point |
| `00F0` | LOCATE_STOPPED_CHAR_ON_FOOT_2D | Char | default | 6 | Returns true if the character stopped within the 2D radius of the coordinates point on foot |
| `00F1` | LOCATE_STOPPED_CHAR_IN_CAR_2D | Char | default | 6 | Returns true if the character stopped within the 2D radius of the coordinates point in a vehicle |
| `00F2` | LOCATE_CHAR_ANY_MEANS_CHAR_2D | Char | default | 5 | Returns true if the character is within the 2D radius of the other character |
| `00F3` | LOCATE_CHAR_ON_FOOT_CHAR_2D | Char | default | 5 | Returns true if the character is within the 2D radius of the other character on foot |
| `00F4` | LOCATE_CHAR_IN_CAR_CHAR_2D | Char | default | 5 | Returns true if the character is within the 2D radius of the other character in a vehicle |
| `00F5` | LOCATE_PLAYER_ANY_MEANS_3D |  | default | 0 |  |
| `00F6` | LOCATE_PLAYER_ON_FOOT_3D |  | default | 0 |  |
| `00F7` | LOCATE_PLAYER_IN_CAR_3D |  | default | 0 |  |
| `00F8` | LOCATE_STOPPED_PLAYER_ANY_MEANS_3D |  | default | 0 |  |
| `00F9` | LOCATE_STOPPED_PLAYER_ON_FOOT_3D |  | default | 0 |  |
| `00FA` | LOCATE_STOPPED_PLAYER_IN_CAR_3D |  | default | 0 |  |
| `00FB` | LOCATE_PLAYER_ANY_MEANS_CHAR_3D |  | default | 0 |  |
| `00FC` | LOCATE_PLAYER_ON_FOOT_CHAR_3D |  | default | 0 |  |
| `00FD` | LOCATE_PLAYER_IN_CAR_CHAR_3D |  | default | 0 |  |
| `00FE` | LOCATE_CHAR_ANY_MEANS_3D | Char | default | 8 | Returns true if the character is within the 3D radius of the coordinates point |
| `00FF` | LOCATE_CHAR_ON_FOOT_3D | Char | default | 8 | Returns true if the character is within the 3D radius of the coordinates point on foot |
| `0100` | LOCATE_CHAR_IN_CAR_3D | Char | default | 8 | Returns true if the character is within the 3D radius of the coordinates point in a vehicle |
| `0101` | LOCATE_STOPPED_CHAR_ANY_MEANS_3D | Char | default | 8 | Returns true if the character stopped within the 3D radius of the coordinates point |
| `0102` | LOCATE_STOPPED_CHAR_ON_FOOT_3D | Char | default | 8 | Returns true if the character stopped within the 3D radius of the coordinates point on foot |
| `0103` | LOCATE_STOPPED_CHAR_IN_CAR_3D | Char | default | 8 | Returns true if the character stopped within the 3D radius of the coordinates point in a vehicle |
| `0104` | LOCATE_CHAR_ANY_MEANS_CHAR_3D | Char | default | 6 | Returns true if the character is within the 3D radius of the other character |
| `0105` | LOCATE_CHAR_ON_FOOT_CHAR_3D | Char | default | 6 | Returns true if the character is within the 3D radius of the other character on foot |
| `0106` | LOCATE_CHAR_IN_CAR_CHAR_3D | Char | default | 6 | Returns true if the character is within the 3D radius of the other character in a vehicle |
| `0107` | CREATE_OBJECT | Object | default | 5 | Creates an object at the specified location, with the specified model |
| `0108` | DELETE_OBJECT | Object | default | 1 | Destroys the object, freeing game memory |
| `0109` | ADD_SCORE | Player | default | 2 | Adds to the player's money |
| `010A` | IS_SCORE_GREATER | Player | default | 2 | Returns true if the player's money is over the specified value |
| `010B` | STORE_SCORE | Player | default | 2 | Returns the player's money |
| `010C` | GIVE_REMOTE_CONTROLLED_CAR_TO_PLAYER |  | default | 0 | Gives control of the remote-control vehicle to the player |
| `010D` | ALTER_WANTED_LEVEL | Player | default | 2 | Sets the player's wanted level |
| `010E` | ALTER_WANTED_LEVEL_NO_DROP | Player | default | 2 | Sets the player's wanted level if the specified level is higher than the current one |
| `010F` | IS_WANTED_LEVEL_GREATER | Player | default | 2 | Returns true if the player's wanted level is over the specified value |
| `0110` | CLEAR_WANTED_LEVEL | Player | default | 1 | Clears the player's wanted level |
| `0111` | SET_DEATHARREST_STATE |  | default | 1 | Sets the detection of death and arrest during a mission (0112) |
| `0112` | HAS_DEATHARREST_BEEN_EXECUTED |  | default | 0 | Returns true if the player is dead (wasted) or arrested (busted) |
| `0113` | ADD_AMMO_TO_PLAYER |  | default | 0 |  |
| `0114` | ADD_AMMO_TO_CHAR | Char | default | 3 | Adds the specified amount of ammo to the character's weapon, if the character has the weapon |
| `0115` | ADD_AMMO_TO_CAR |  | default | 0 |  |
| `0116` | IS_PLAYER_STILL_ALIVE |  | default | 0 |  |
| `0117` | IS_PLAYER_DEAD | Player | default | 1 | Returns true when player is dead (wasted) |
| `0118` | IS_CHAR_DEAD | Char | default | 1 | Returns true if the handle is an invalid character handle or the character is dead (wasted) |
| `0119` | IS_CAR_DEAD | Car | default | 1 | Returns true if the handle is an invalid vehicle handle or the vehicle has been destroyed (wrecked) |
| `011A` | SET_CHAR_THREAT_SEARCH |  | default | 0 |  |
| `011B` | SET_CHAR_THREAT_REACTION |  | default | 0 |  |
| `011C` | SET_CHAR_OBJ_NO_OBJ |  | default | 0 |  |
| `011D` | ORDER_DRIVER_OUT_OF_CAR |  | default | 0 |  |
| `011E` | ORDER_CHAR_TO_DRIVE_CAR |  | default | 0 |  |
| `011F` | ADD_PATROL_POINT |  | default | 0 |  |
| `0120` | IS_PLAYER_IN_GANGZONE |  | default | 0 |  |
| `0121` | IS_PLAYER_IN_ZONE |  | default | 0 |  |
| `0122` | IS_PLAYER_PRESSING_HORN | Player | default | 1 | Returns true if the player is honking the horn in a car |
| `0123` | HAS_CHAR_SPOTTED_PLAYER |  | default | 0 |  |
| `0124` | ORDER_CHAR_TO_BACKDOOR |  | default | 0 |  |
| `0125` | ADD_CHAR_TO_GANG |  | default | 0 |  |
| `0126` | IS_CHAR_OBJECTIVE_PASSED |  | default | 0 |  |
| `0127` | SET_CHAR_DRIVE_AGGRESSION |  | default | 0 |  |
| `0128` | SET_CHAR_MAX_DRIVESPEED |  | default | 0 |  |
| `0129` | CREATE_CHAR_INSIDE_CAR | Char | default | 4 | Creates a character in the driver's seat of the vehicle |
| `012A` | WARP_PLAYER_FROM_CAR_TO_COORD |  | default | 0 |  |
| `012B` | MAKE_CHAR_DO_NOTHING |  | default | 0 |  |
| `012C` | SET_CHAR_INVINCIBLE |  | default | 0 |  |
| `012D` | SET_PLAYER_INVINCIBLE |  | default | 0 |  |
| `012E` | SET_CHAR_GRAPHIC_TYPE |  | default | 0 |  |
| `012F` | SET_PLAYER_GRAPHIC_TYPE |  | default | 0 |  |
| `0130` | HAS_PLAYER_BEEN_ARRESTED |  | default | 0 |  |
| `0131` | STOP_CHAR_DRIVING |  | default | 0 |  |
| `0132` | KILL_CHAR |  | default | 0 |  |
| `0133` | SET_FAVOURITE_CAR_MODEL_FOR_CHAR |  | default | 0 |  |
| `0134` | SET_CHAR_OCCUPATION |  | default | 0 |  |
| `0135` | CHANGE_CAR_LOCK |  | default | 0 |  |
| `0136` | SHAKE_CAM_WITH_POINT |  | default | 0 |  |
| `0137` | IS_CAR_MODEL | Car | default | 2 | Returns true if the vehicle has the specified model |
| `0138` | IS_CAR_REMAP |  | default | 0 |  |
| `0139` | HAS_CAR_JUST_SUNK |  | default | 0 |  |
| `013A` | SET_CAR_NO_COLLIDE |  | default | 0 |  |
| `013B` | IS_CAR_DEAD_IN_AREA_2D |  | default | 0 |  |
| `013C` | IS_CAR_DEAD_IN_AREA_3D |  | default | 0 |  |
| `013D` | IS_TRAILER_ATTACHED |  | default | 0 |  |
| `013E` | IS_CAR_ON_TRAILER |  | default | 0 |  |
| `013F` | HAS_CAR_GOT_WEAPON |  | default | 0 |  |
| `0140` | PARK |  | default | 0 |  |
| `0141` | HAS_PARK_FINISHED |  | default | 0 |  |
| `0142` | KILL_ALL_PASSENGERS |  | default | 0 |  |
| `0143` | SET_CAR_BULLETPROOF |  | default | 0 |  |
| `0144` | SET_CAR_FLAMEPROOF |  | default | 0 |  |
| `0145` | SET_CAR_ROCKETPROOF |  | default | 0 |  |
| `0146` | IS_CARBOMB_ACTIVE |  | default | 0 |  |
| `0147` | GIVE_CAR_ALARM |  | default | 0 |  |
| `0148` | PUT_CAR_ON_TRAILER |  | default | 0 |  |
| `0149` | IS_CAR_CRUSHED |  | default | 0 |  |
| `014A` | CREATE_GANG_CAR |  | default | 0 |  |
| `014B` | CREATE_CAR_GENERATOR | CarGenerator | default | 13 | Initializes a parked car generator (modelId -1 selects a random vehicle from the local popcycle) |
| `014C` | SWITCH_CAR_GENERATOR | CarGenerator | default | 2 | Specifies the number of times the car generator spawns a car (101 - infinite) |
| `014D` | ADD_PAGER_MESSAGE |  | default | 0 |  |
| `014E` | DISPLAY_ONSCREEN_TIMER | Hud | default | 2 | Creates a countdown or countup onscreen timer |
| `014F` | CLEAR_ONSCREEN_TIMER | Hud | default | 1 | Removes the onscreen timer |
| `0150` | DISPLAY_ONSCREEN_COUNTER |  | default | 0 |  |
| `0151` | CLEAR_ONSCREEN_COUNTER | Hud | default | 1 | Removes the onscreen counter (0150 or 03C4) |
| `0152` | SET_ZONE_CAR_INFO |  | default | 0 |  |
| `0153` | IS_CHAR_IN_GANG_ZONE |  | default | 0 |  |
| `0154` | IS_CHAR_IN_ZONE | Char | default | 2 | Returns true if the character is in the specified map zone |
| `0155` | SET_CAR_DENSITY |  | default | 0 |  |
| `0156` | SET_PED_DENSITY |  | default | 0 |  |
| `0157` | POINT_CAMERA_AT_PLAYER |  | default | 0 |  |
| `0158` | POINT_CAMERA_AT_CAR | Camera | default | 3 | Attaches the camera to the specified vehicle |
| `0159` | POINT_CAMERA_AT_CHAR | Camera | default | 3 | Attaches the camera to the specified character |
| `015A` | RESTORE_CAMERA | Camera | default | 0 | Restores the camera to its usual position |
| `015B` | SHAKE_PAD | Pad | default | 3 | Shakes the player's joypad at the specified intensity for the specified time |
| `015C` | SET_ZONE_PED_INFO |  | default | 0 |  |
| `015D` | SET_TIME_SCALE | Clock | default | 1 | Sets the game to run at the specified speed |
| `015E` | IS_CAR_IN_AIR |  | default | 0 |  |
| `015F` | SET_FIXED_CAMERA_POSITION | Camera | default | 6 | Sets the fixed camera's position and up vector offset |
| `0160` | POINT_CAMERA_AT_POINT | Camera | default | 4 | Points the camera at the specified location and applies the position set by 0159 |
| `0161` | ADD_BLIP_FOR_CAR_OLD | Blip | default | 4 | Adds a blip with properties to the vehicle |
| `0162` | ADD_BLIP_FOR_CHAR_OLD |  | default | 0 |  |
| `0163` | ADD_BLIP_FOR_OBJECT_OLD |  | default | 0 |  |
| `0164` | REMOVE_BLIP | Blip | default | 1 | Removes the blip |
| `0165` | CHANGE_BLIP_COLOUR | Blip | default | 2 | Sets the blip's color |
| `0166` | DIM_BLIP |  | default | 0 |  |
| `0167` | ADD_BLIP_FOR_COORD_OLD | Blip | default | 6 | Adds a blip with properties at the location |
| `0168` | CHANGE_BLIP_SCALE | Blip | default | 2 | Sets the blip's size |
| `0169` | SET_FADING_COLOUR | Camera | default | 3 | Sets the RGB color of the fade command (016A) |
| `016A` | DO_FADE | Camera | default | 2 | Fades the screen for the specified time |
| `016B` | GET_FADING_STATUS | Camera | default | 0 | Returns true if the screen is fading (016A) |
| `016C` | ADD_HOSPITAL_RESTART | Restart | default | 5 | Adds a hospital restart, which is where the player will spawn after death (wasted) if the point is closer than any other hospital restart |
| `016D` | ADD_POLICE_RESTART | Restart | default | 5 | Adds a police restart, which is where the player will spawn after being arrested (busted) if the point is closer than any other police restart |
| `016E` | OVERRIDE_NEXT_RESTART | Restart | default | 4 | Forces this location to be the next respawn location |
| `016F` | DRAW_SHADOW | Fx | default | 10 | Draws a shadow in the current frame |
| `0170` | GET_PLAYER_HEADING |  | default | 0 |  |
| `0171` | SET_PLAYER_HEADING |  | default | 0 |  |
| `0172` | GET_CHAR_HEADING | Char | default | 2 | Returns the character's heading (z-angle) |
| `0173` | SET_CHAR_HEADING | Char | default | 2 | Sets the character's heading (z-angle) |
| `0174` | GET_CAR_HEADING | Car | default | 2 | Returns the vehicle's heading (z-angle) |
| `0175` | SET_CAR_HEADING | Car | default | 2 | Sets the vehicle's heading (z-angle) |
| `0176` | GET_OBJECT_HEADING | Object | default | 2 | Returns the object's heading (z-angle) |
| `0177` | SET_OBJECT_HEADING | Object | default | 2 | Sets the object's heading (z-angle) |
| `0178` | IS_PLAYER_TOUCHING_OBJECT |  | default | 0 |  |
| `0179` | IS_CHAR_TOUCHING_OBJECT | Char | default | 2 | Returns true if the character is colliding with the specified object |
| `017A` | SET_PLAYER_AMMO |  | default | 0 |  |
| `017B` | SET_CHAR_AMMO | Char | default | 3 | Sets the amount of ammo the character has in the specified weapon |
| `017C` | SET_CAR_AMMO |  | default | 0 |  |
| `017D` | LOAD_CAMERA_SPLINE |  | default | 0 |  |
| `017E` | MOVE_CAMERA_ALONG_SPLINE |  | default | 0 |  |
| `017F` | GET_CAMERA_POSITION_ALONG_SPLINE |  | default | 0 |  |
| `0180` | DECLARE_MISSION_FLAG |  | default | 1 | Links the global variable to the specific hardcoded flag that defines is there an active mission or not |
| `0181` | DECLARE_MISSION_FLAG_FOR_CONTACT |  | default | 0 |  |
| `0182` | DECLARE_BASE_BRIEF_ID_FOR_CONTACT |  | default | 0 |  |
| `0183` | IS_PLAYER_HEALTH_GREATER |  | default | 0 |  |
| `0184` | IS_CHAR_HEALTH_GREATER | Char | default | 2 | Returns true if the character's health is over the specified value |
| `0185` | IS_CAR_HEALTH_GREATER | Car | default | 2 | Returns true if the car's health is over the specified value |
| `0186` | ADD_BLIP_FOR_CAR | Blip | default | 2 | Adds a blip and a marker to the vehicle |
| `0187` | ADD_BLIP_FOR_CHAR | Blip | default | 2 | Adds a blip and a marker to the character |
| `0188` | ADD_BLIP_FOR_OBJECT | Blip | default | 2 | Adds a blip and a marker to the object |
| `0189` | ADD_BLIP_FOR_CONTACT_POINT |  | default | 0 |  |
| `018A` | ADD_BLIP_FOR_COORD | Blip | default | 4 | Adds a blip to the location |
| `018B` | CHANGE_BLIP_DISPLAY | Blip | default | 2 | Changes the display of the specified blip |
| `018C` | ADD_ONE_OFF_SOUND | Sound | default | 4 | Plays a sound with the specified ID at the location |
| `018D` | ADD_CONTINUOUS_SOUND |  | default | 5 | Creates a continuous sound at the specified coordinates and stores the handle to a variable |
| `018E` | REMOVE_SOUND | Sound | default | 1 | Stops the sound |
| `018F` | IS_CAR_STUCK_ON_ROOF | Car | default | 1 | Returns true if the car has been upside down for more than 2 seconds (requires 0190) |
| `0190` | ADD_UPSIDEDOWN_CAR_CHECK | Car | default | 1 | Activates upside-down car check for the car |
| `0191` | REMOVE_UPSIDEDOWN_CAR_CHECK | Car | default | 1 | Deactivates upside-down car check (0190) for the car |
| `0192` | SET_CHAR_OBJ_WAIT_ON_FOOT |  | default | 0 |  |
| `0193` | SET_CHAR_OBJ_FLEE_ON_FOOT_TILL_SAFE |  | default | 0 |  |
| `0194` | SET_CHAR_OBJ_GUARD_SPOT |  | default | 0 |  |
| `0195` | SET_CHAR_OBJ_GUARD_AREA |  | default | 0 |  |
| `0196` | SET_CHAR_OBJ_WAIT_IN_CAR |  | default | 0 |  |
| `0197` | IS_PLAYER_IN_AREA_ON_FOOT_2D |  | default | 0 |  |
| `0198` | IS_PLAYER_IN_AREA_IN_CAR_2D |  | default | 0 |  |
| `0199` | IS_PLAYER_STOPPED_IN_AREA_2D |  | default | 0 |  |
| `019A` | IS_PLAYER_STOPPED_IN_AREA_ON_FOOT_2D |  | default | 0 |  |
| `019B` | IS_PLAYER_STOPPED_IN_AREA_IN_CAR_2D |  | default | 0 |  |
| `019C` | IS_PLAYER_IN_AREA_ON_FOOT_3D |  | default | 0 |  |
| `019D` | IS_PLAYER_IN_AREA_IN_CAR_3D |  | default | 0 |  |
| `019E` | IS_PLAYER_STOPPED_IN_AREA_3D |  | default | 0 |  |
| `019F` | IS_PLAYER_STOPPED_IN_AREA_ON_FOOT_3D |  | default | 0 |  |
| `01A0` | IS_PLAYER_STOPPED_IN_AREA_IN_CAR_3D |  | default | 0 |  |
| `01A1` | IS_CHAR_IN_AREA_ON_FOOT_2D | Char | default | 6 | Returns true if the character is within the specified 2D area on foot |
| `01A2` | IS_CHAR_IN_AREA_IN_CAR_2D | Char | default | 6 | Returns true if the character is within the specified 2D area in a vehicle |
| `01A3` | IS_CHAR_STOPPED_IN_AREA_2D | Char | default | 6 | Returns true if the character stopped within the specified 2D area |
| `01A4` | IS_CHAR_STOPPED_IN_AREA_ON_FOOT_2D | Char | default | 6 | Returns true if the character stopped within the specified 2D area on foot |
| `01A5` | IS_CHAR_STOPPED_IN_AREA_IN_CAR_2D | Char | default | 6 | Returns true if the character stopped within the specified 2D area in a vehicle |
| `01A6` | IS_CHAR_IN_AREA_ON_FOOT_3D | Char | default | 8 | Returns true if the character is within the specified 3D area on foot |
| `01A7` | IS_CHAR_IN_AREA_IN_CAR_3D | Char | default | 8 | Returns true if the character is within the specified 3D area in a vehicle |
| `01A8` | IS_CHAR_STOPPED_IN_AREA_3D | Char | default | 8 | Returns true if the character stopped within the specified 3D area |
| `01A9` | IS_CHAR_STOPPED_IN_AREA_ON_FOOT_3D | Char | default | 8 | Returns true if the character stopped within the specified 3D area on foot |
| `01AA` | IS_CHAR_STOPPED_IN_AREA_IN_CAR_3D | Char | default | 8 | Returns true if the character stopped within the specified 3D area in a vehicle |
| `01AB` | IS_CAR_STOPPED_IN_AREA_2D | Car | default | 6 | Returns true if the car stopped within the specified 2D area |
| `01AC` | IS_CAR_STOPPED_IN_AREA_3D | Car | default | 8 | Returns true if the car stopped within the specified 3D area |
| `01AD` | LOCATE_CAR_2D | Car | default | 6 | Returns true if the car is within the 2D radius of the point |
| `01AE` | LOCATE_STOPPED_CAR_2D | Car | default | 6 | Returns true if the car is stopped within the 2D radius of the point |
| `01AF` | LOCATE_CAR_3D | Car | default | 8 | Returns true if the car is within the 3D radius of the point |
| `01B0` | LOCATE_STOPPED_CAR_3D | Car | default | 8 | Returns true if the car is stopped in the radius of the specified point |
| `01B1` | GIVE_WEAPON_TO_PLAYER |  | default | 0 |  |
| `01B2` | GIVE_WEAPON_TO_CHAR | Char | default | 3 | Gives the character the weapon with the specified amount of ammo |
| `01B3` | GIVE_WEAPON_TO_CAR |  | default | 0 |  |
| `01B4` | SET_PLAYER_CONTROL | Player | default | 2 | Sets whether player's control is enabled |
| `01B5` | FORCE_WEATHER | Weather | default | 1 | Forces the game weather to the specified type |
| `01B6` | FORCE_WEATHER_NOW | Weather | default | 1 | Forces the upcoming weather to the specified type |
| `01B7` | RELEASE_WEATHER | Weather | default | 0 | Allows the game to continue its usual weather pattern after using 01B5 |
| `01B8` | SET_CURRENT_PLAYER_WEAPON |  | default | 0 |  |
| `01B9` | SET_CURRENT_CHAR_WEAPON | Char | default | 2 | Sets the character's currently held weapon |
| `01BA` | SET_CURRENT_CAR_WEAPON |  | default | 0 |  |
| `01BB` | GET_OBJECT_COORDINATES | Object | default | 4 | Returns the object's coordinates |
| `01BC` | SET_OBJECT_COORDINATES | Object | default | 4 | Puts the object at the specified location |
| `01BD` | GET_GAME_TIMER | Clock | default | 1 | Returns the time passed in milliseconds since the game started |
| `01BE` | TURN_CHAR_TO_FACE_COORD |  | default | 0 |  |
| `01BF` | TURN_PLAYER_TO_FACE_COORD |  | default | 0 |  |
| `01C0` | STORE_WANTED_LEVEL | Player | default | 2 | Returns the player's current wanted level |
| `01C1` | IS_CAR_STOPPED | Car | default | 1 | Returns true if the vehicle is not moving |
| `01C2` | MARK_CHAR_AS_NO_LONGER_NEEDED | Char | default | 1 | Allows the character to be deleted by the game if necessary, and also removes them from the mission cleanup list, if applicable |
| `01C3` | MARK_CAR_AS_NO_LONGER_NEEDED | Car | default | 1 | Allows the vehicle to be deleted by the game if necessary, and also removes it from the mission cleanup list, if applicable |
| `01C4` | MARK_OBJECT_AS_NO_LONGER_NEEDED | Object | default | 1 | Allows the object to be deleted by the game if necessary, and also removes it from the mission cleanup list, if applicable |
| `01C5` | DONT_REMOVE_CHAR | Char | default | 1 | Removes the character from the mission cleanup list, preventing it from being deleted when the mission ends |
| `01C6` | DONT_REMOVE_CAR |  | default | 0 |  |
| `01C7` | DONT_REMOVE_OBJECT | Object | default | 1 | Removes the object from the mission cleanup list, preventing it from being deleted when the mission ends |
| `01C8` | CREATE_CHAR_AS_PASSENGER | Char | default | 5 | Creates a character with the specified model in the passenger seat of the vehicle |
| `01C9` | SET_CHAR_OBJ_KILL_CHAR_ON_FOOT |  | default | 0 |  |
| `01CA` | SET_CHAR_OBJ_KILL_PLAYER_ON_FOOT |  | default | 0 |  |
| `01CB` | SET_CHAR_OBJ_KILL_CHAR_ANY_MEANS |  | default | 0 |  |
| `01CC` | SET_CHAR_OBJ_KILL_PLAYER_ANY_MEANS |  | default | 0 |  |
| `01CD` | SET_CHAR_OBJ_FLEE_CHAR_ON_FOOT_TILL_SAFE |  | default | 0 |  |
| `01CE` | SET_CHAR_OBJ_FLEE_PLAYER_ON_FOOT_TILL_SAFE |  | default | 0 |  |
| `01CF` | SET_CHAR_OBJ_FLEE_CHAR_ON_FOOT_ALWAYS |  | default | 0 |  |
| `01D0` | SET_CHAR_OBJ_FLEE_PLAYER_ON_FOOT_ALWAYS |  | default | 0 |  |
| `01D1` | SET_CHAR_OBJ_GOTO_CHAR_ON_FOOT |  | default | 0 |  |
| `01D2` | SET_CHAR_OBJ_GOTO_PLAYER_ON_FOOT |  | default | 0 |  |
| `01D3` | SET_CHAR_OBJ_LEAVE_CAR |  | default | 0 |  |
| `01D4` | SET_CHAR_OBJ_ENTER_CAR_AS_PASSENGER |  | default | 0 |  |
| `01D5` | SET_CHAR_OBJ_ENTER_CAR_AS_DRIVER |  | default | 0 |  |
| `01D6` | SET_CHAR_OBJ_FOLLOW_CAR_IN_CAR |  | default | 0 |  |
| `01D7` | SET_CHAR_OBJ_FIRE_AT_OBJECT_FROM_VEHICLE |  | default | 0 |  |
| `01D8` | SET_CHAR_OBJ_DESTROY_OBJECT |  | default | 0 |  |
| `01D9` | SET_CHAR_OBJ_DESTROY_CAR |  | default | 0 |  |
| `01DA` | SET_CHAR_OBJ_GOTO_AREA_ON_FOOT |  | default | 0 |  |
| `01DB` | SET_CHAR_OBJ_GOTO_AREA_IN_CAR |  | default | 0 |  |
| `01DC` | SET_CHAR_OBJ_FOLLOW_CAR_ON_FOOT_WITH_OFFSET |  | default | 0 |  |
| `01DD` | SET_CHAR_OBJ_GUARD_ATTACK |  | default | 0 |  |
| `01DE` | SET_CHAR_AS_LEADER |  | default | 0 |  |
| `01DF` | SET_PLAYER_AS_LEADER |  | default | 0 |  |
| `01E0` | LEAVE_GROUP |  | default | 0 |  |
| `01E1` | SET_CHAR_OBJ_FOLLOW_ROUTE |  | default | 0 |  |
| `01E2` | ADD_ROUTE_POINT |  | default | 0 |  |
| `01E3` | PRINT_WITH_NUMBER_BIG | Text | default | 4 | Displays a styled message in which the first string token~1~ is substituted with the specified number |
| `01E4` | PRINT_WITH_NUMBER | Text | default | 4 | Displays a styled message in which the first string token ~1~ is substituted with the specified number |
| `01E5` | PRINT_WITH_NUMBER_NOW | Text | default | 4 | Displays a styled message in which the first string token ~1~ is substituted with the specified number |
| `01E6` | PRINT_WITH_NUMBER_SOON |  | default | 0 |  |
| `01E7` | SWITCH_ROADS_ON | Path | default | 6 | Enables all car paths in the given area |
| `01E8` | SWITCH_ROADS_OFF | Path | default | 6 | Disables all car paths in the given area |
| `01E9` | GET_NUMBER_OF_PASSENGERS | Car | default | 2 | Returns the number of passengers sitting in the car |
| `01EA` | GET_MAXIMUM_NUMBER_OF_PASSENGERS | Car | default | 2 | Returns the maximum number of passengers that could sit in the car |
| `01EB` | SET_CAR_DENSITY_MULTIPLIER | World | default | 1 | Sets the quantity of traffic that will spawn in the game |
| `01EC` | SET_CAR_HEAVY | Car | default | 2 | Sets whether the car is heavy |
| `01ED` | CLEAR_CHAR_THREAT_SEARCH |  | default | 0 |  |
| `01EE` | ACTIVATE_CRANE |  | default | 0 |  |
| `01EF` | DEACTIVATE_CRANE |  | default | 0 |  |
| `01F0` | SET_MAX_WANTED_LEVEL | Game | default | 1 | Sets the maximum wanted level the player can receive |
| `01F1` | SAVE_VAR_INT |  | default | 0 |  |
| `01F2` | SAVE_VAR_FLOAT |  | default | 0 |  |
| `01F3` | IS_CAR_IN_AIR_PROPER | Car | default | 1 | Returns true if the vehicle is in the air |
| `01F4` | IS_CAR_UPSIDEDOWN | Car | default | 1 | Returns true if the car is upside down |
| `01F5` | GET_PLAYER_CHAR | Player | default | 2 | Gets the character handle for the specified player |
| `01F6` | CANCEL_OVERRIDE_RESTART | Restart | default | 0 | Stops the player from spawning at the override location (016E) |
| `01F7` | SET_POLICE_IGNORE_PLAYER | Game | default | 2 | Sets whether cops should ignore the player regardless of wanted level |
| `01F8` | ADD_PAGER_MESSAGE_WITH_NUMBER |  | default | 0 |  |
| `01F9` | START_KILL_FRENZY | KillFrenzy | default | 9 | Starts a rampage |
| `01FA` | READ_KILL_FRENZY_STATUS | KillFrenzy | default | 1 | Returns the status of the current rampage |
| `01FB` | SQRT | Math | default | 2 | Returns the square root of a number |
| `01FC` | LOCATE_PLAYER_ANY_MEANS_CAR_2D |  | default | 0 |  |
| `01FD` | LOCATE_PLAYER_ON_FOOT_CAR_2D |  | default | 0 |  |
| `01FE` | LOCATE_PLAYER_IN_CAR_CAR_2D |  | default | 0 |  |
| `01FF` | LOCATE_PLAYER_ANY_MEANS_CAR_3D |  | default | 0 |  |
| `0200` | LOCATE_PLAYER_ON_FOOT_CAR_3D |  | default | 0 |  |
| `0201` | LOCATE_PLAYER_IN_CAR_CAR_3D |  | default | 0 |  |
| `0202` | LOCATE_CHAR_ANY_MEANS_CAR_2D | Char | default | 5 | Returns true if the character is within the 2D radius of the vehicle |
| `0203` | LOCATE_CHAR_ON_FOOT_CAR_2D | Char | default | 5 | Returns true if the character is within the 2D radius of the vehicle on foot |
| `0204` | LOCATE_CHAR_IN_CAR_CAR_2D | Char | default | 5 | Returns true if the character is within the 2D radius of the vehicle in a vehicle |
| `0205` | LOCATE_CHAR_ANY_MEANS_CAR_3D | Char | default | 6 | Returns true if the character is within the 3D radius of the vehicle |
| `0206` | LOCATE_CHAR_ON_FOOT_CAR_3D | Char | default | 6 | Returns true if the character is within the 3D radius of the vehicle on foot |
| `0207` | LOCATE_CHAR_IN_CAR_CAR_3D | Char | default | 6 | Returns true if the character is within the 3D radius of the vehicle in a vehicle |
| `0208` | GENERATE_RANDOM_FLOAT_IN_RANGE | Math | default | 3 | Returns a random float within the specified range; including min and max values |
| `0209` | GENERATE_RANDOM_INT_IN_RANGE | Math | default | 3 | Returns a random integer within the specified range; including min and excluding max values |
| `020A` | LOCK_CAR_DOORS | Car | default | 2 | Sets the locked status of the car's doors |
| `020B` | EXPLODE_CAR | Car | default | 1 | Makes the vehicle explode |
| `020C` | ADD_EXPLOSION | Fx | default | 4 | Creates an explosion at the point |
| `020D` | IS_CAR_UPRIGHT | Car | default | 1 | Returns true if the vehicle is in the normal position (upright) |
| `020E` | TURN_CHAR_TO_FACE_CHAR |  | default | 0 |  |
| `020F` | TURN_CHAR_TO_FACE_PLAYER |  | default | 0 |  |
| `0210` | TURN_PLAYER_TO_FACE_CHAR |  | default | 0 |  |
| `0211` | SET_CHAR_OBJ_GOTO_COORD_ON_FOOT |  | default | 0 |  |
| `0212` | SET_CHAR_OBJ_GOTO_COORD_IN_CAR |  | default | 0 |  |
| `0213` | CREATE_PICKUP | Pickup | default | 6 | Creates a pickup with the given model and type |
| `0214` | HAS_PICKUP_BEEN_COLLECTED | Pickup | default | 1 | Returns true if specified pickup has been collected |
| `0215` | REMOVE_PICKUP | Pickup | default | 1 | Destroys the specified pickup, freeing game memory |
| `0216` | SET_TAXI_LIGHTS | Car | default | 2 | Sets whether the taxi's roof light is on |
| `0217` | PRINT_BIG_Q | Text | default | 3 | Displays a low-priority styled message for the specified time |
| `0218` | PRINT_WITH_NUMBER_BIG_Q |  | default | 0 |  |
| `0219` | SET_GARAGE |  | default | 0 |  |
| `021A` | SET_GARAGE_WITH_CAR_MODEL |  | default | 0 |  |
| `021B` | SET_TARGET_CAR_FOR_MISSION_GARAGE | Garage | default | 2 | Sets the specified garage to only accept the specified vehicle |
| `021C` | IS_CAR_IN_MISSION_GARAGE |  | default | 0 |  |
| `021D` | SET_FREE_BOMBS |  | default | 0 |  |
| `021E` | SET_POWERPOINT |  | default | 0 |  |
| `021F` | SET_ALL_TAXI_LIGHTS |  | default | 0 |  |
| `0220` | IS_CAR_ARMED_WITH_ANY_BOMB |  | default | 0 |  |
| `0221` | APPLY_BRAKES_TO_PLAYERS_CAR | Player | default | 2 | Applies brakes to the player's car |
| `0222` | SET_PLAYER_HEALTH |  | default | 0 |  |
| `0223` | SET_CHAR_HEALTH | Char | default | 2 | Sets the character's health |
| `0224` | SET_CAR_HEALTH | Car | default | 2 | Sets the vehicle's health |
| `0225` | GET_PLAYER_HEALTH |  | default | 0 |  |
| `0226` | GET_CHAR_HEALTH | Char | default | 2 | Returns the character's health |
| `0227` | GET_CAR_HEALTH | Car | default | 2 | Returns the vehicle's health |
| `0228` | IS_CAR_ARMED_WITH_BOMB |  | default | 0 |  |
| `0229` | CHANGE_CAR_COLOUR | Car | default | 3 | Sets the car's primary and secondary colors |
| `022A` | SWITCH_PED_ROADS_ON | Path | default | 6 | Enables all ped paths in the given area |
| `022B` | SWITCH_PED_ROADS_OFF | Path | default | 6 | Disables all ped paths in the given area |
| `022C` | CHAR_LOOK_AT_CHAR_ALWAYS |  | default | 0 |  |
| `022D` | CHAR_LOOK_AT_PLAYER_ALWAYS |  | default | 0 |  |
| `022E` | PLAYER_LOOK_AT_CHAR_ALWAYS |  | default | 0 |  |
| `022F` | STOP_CHAR_LOOKING |  | default | 0 |  |
| `0230` | STOP_PLAYER_LOOKING |  | default | 0 |  |
| `0231` | SET_SCRIPT_POLICE_HELI_TO_CHASE_CHAR |  | default | 0 |  |
| `0232` | SET_GANG_ATTITUDE |  | default | 0 |  |
| `0233` | SET_GANG_GANG_ATTITUDE |  | default | 0 |  |
| `0234` | SET_GANG_PLAYER_ATTITUDE |  | default | 0 |  |
| `0235` | SET_GANG_PED_MODELS |  | default | 3 | Sets the models used by members of the specified gang |
| `0236` | SET_GANG_CAR_MODEL |  | default | 2 | Sets the car used by members of the specified gang |
| `0237` | SET_GANG_WEAPONS | Gang | default | 4 | Sets the weapons that the specified gang can use |
| `0238` | SET_CHAR_OBJ_RUN_TO_AREA |  | default | 0 |  |
| `0239` | SET_CHAR_OBJ_RUN_TO_COORD |  | default | 0 |  |
| `023A` | IS_PLAYER_TOUCHING_OBJECT_ON_FOOT |  | default | 0 |  |
| `023B` | IS_CHAR_TOUCHING_OBJECT_ON_FOOT | Char | default | 2 | Returns true if the character is colliding with the specified object on foot |
| `023C` | LOAD_SPECIAL_CHARACTER | Streaming | default | 2 | Requests a special character's model to be loaded into the specified slot |
| `023D` | HAS_SPECIAL_CHARACTER_LOADED | Streaming | default | 1 | Returns true if the special character's model (023C) is available for creation |
| `023E` | FLASH_CAR |  | default | 0 |  |
| `023F` | FLASH_CHAR |  | default | 0 |  |
| `0240` | FLASH_OBJECT |  | default | 0 |  |
| `0241` | IS_PLAYER_IN_REMOTE_MODE | Player | default | 1 | Returns true if the player is controlling a remote-control vehicle |
| `0242` | ARM_CAR_WITH_BOMB |  | default | 0 |  |
| `0243` | SET_CHAR_PERSONALITY |  | default | 0 |  |
| `0244` | SET_CUTSCENE_OFFSET | Cutscene | default | 3 | Sets the position for a cutscene |
| `0245` | SET_ANIM_GROUP_FOR_CHAR | Char | default | 2 | Sets the animation group for the character |
| `0246` | SET_ANIM_GROUP_FOR_PLAYER |  | default | 0 |  |
| `0247` | REQUEST_MODEL | Streaming | default | 1 | Requests a new model to load |
| `0248` | HAS_MODEL_LOADED | Streaming | default | 1 | Returns true if the model is available for creation |
| `0249` | MARK_MODEL_AS_NO_LONGER_NEEDED | Streaming | default | 1 | Releases the specified model, freeing game memory |
| `024A` | GRAB_PHONE |  | default | 0 |  |
| `024B` | SET_REPEATED_PHONE_MESSAGE |  | default | 0 |  |
| `024C` | SET_PHONE_MESSAGE |  | default | 0 |  |
| `024D` | HAS_PHONE_DISPLAYED_MESSAGE |  | default | 0 |  |
| `024E` | TURN_PHONE_OFF |  | default | 0 |  |
| `024F` | DRAW_CORONA | Fx | default | 9 | Displays a corona with fade in-out effect at the specified location |
| `0250` | DRAW_LIGHT |  | default | 0 |  |
| `0251` | STORE_WEATHER |  | default | 0 |  |
| `0252` | RESTORE_WEATHER |  | default | 0 |  |
| `0253` | STORE_CLOCK | Clock | default | 0 | Saves the current time in game |
| `0254` | RESTORE_CLOCK | Clock | default | 0 | Restores the game time to the time when it was saved with 0253 |
| `0255` | RESTART_CRITICAL_MISSION |  | default | 0 |  |
| `0256` | IS_PLAYER_PLAYING | Player | default | 1 | Returns true if the player hasn't been wasted or busted (the player is still playing) |
| `0257` | SET_COLL_OBJ_NO_OBJ |  | default | 0 |  |
| `0258` | SET_COLL_OBJ_WAIT_ON_FOOT |  | default | 0 |  |
| `0259` | SET_COLL_OBJ_FLEE_ON_FOOT_TILL_SAFE |  | default | 0 |  |
| `025A` | SET_COLL_OBJ_GUARD_SPOT |  | default | 0 |  |
| `025B` | SET_COLL_OBJ_GUARD_AREA |  | default | 0 |  |
| `025C` | SET_COLL_OBJ_WAIT_IN_CAR |  | default | 0 |  |
| `025D` | SET_COLL_OBJ_KILL_CHAR_ON_FOOT |  | default | 0 |  |
| `025E` | SET_COLL_OBJ_KILL_PLAYER_ON_FOOT |  | default | 0 |  |
| `025F` | SET_COLL_OBJ_KILL_CHAR_ANY_MEANS |  | default | 0 |  |
| `0260` | SET_COLL_OBJ_KILL_PLAYER_ANY_MEANS |  | default | 0 |  |
| `0261` | SET_COLL_OBJ_FLEE_CHAR_ON_FOOT_TILL_SAFE |  | default | 0 |  |
| `0262` | SET_COLL_OBJ_FLEE_PLAYER_ON_FOOT_TILL_SAFE |  | default | 0 |  |
| `0263` | SET_COLL_OBJ_FLEE_CHAR_ON_FOOT_ALWAYS |  | default | 0 |  |
| `0264` | SET_COLL_OBJ_FLEE_PLAYER_ON_FOOT_ALWAYS |  | default | 0 |  |
| `0265` | SET_COLL_OBJ_GOTO_CHAR_ON_FOOT |  | default | 0 |  |
| `0266` | SET_COLL_OBJ_GOTO_PLAYER_ON_FOOT |  | default | 0 |  |
| `0267` | SET_COLL_OBJ_LEAVE_CAR |  | default | 0 |  |
| `0268` | SET_COLL_OBJ_ENTER_CAR_AS_PASSENGER |  | default | 0 |  |
| `0269` | SET_COLL_OBJ_ENTER_CAR_AS_DRIVER |  | default | 0 |  |
| `026A` | SET_COLL_OBJ_FOLLOW_CAR_IN_CAR |  | default | 0 |  |
| `026B` | SET_COLL_OBJ_FIRE_AT_OBJECT_FROM_VEHICLE |  | default | 0 |  |
| `026C` | SET_COLL_OBJ_DESTROY_OBJECT |  | default | 0 |  |
| `026D` | SET_COLL_OBJ_DESTROY_CAR |  | default | 0 |  |
| `026E` | SET_COLL_OBJ_GOTO_AREA_ON_FOOT |  | default | 0 |  |
| `026F` | SET_COLL_OBJ_GOTO_AREA_IN_CAR |  | default | 0 |  |
| `0270` | SET_COLL_OBJ_FOLLOW_CAR_ON_FOOT_WITH_OFFSET |  | default | 0 |  |
| `0271` | SET_COLL_OBJ_GUARD_ATTACK |  | default | 0 |  |
| `0272` | SET_COLL_OBJ_FOLLOW_ROUTE |  | default | 0 |  |
| `0273` | SET_COLL_OBJ_GOTO_COORD_ON_FOOT |  | default | 0 |  |
| `0274` | SET_COLL_OBJ_GOTO_COORD_IN_CAR |  | default | 0 |  |
| `0275` | SET_COLL_OBJ_RUN_TO_AREA |  | default | 0 |  |
| `0276` | SET_COLL_OBJ_RUN_TO_COORD |  | default | 0 |  |
| `0277` | ADD_PEDS_IN_AREA_TO_COLL |  | default | 0 |  |
| `0278` | ADD_PEDS_IN_VEHICLE_TO_COLL |  | default | 0 |  |
| `0279` | CLEAR_COLL |  | default | 0 |  |
| `027A` | IS_COLL_IN_CARS |  | default | 0 |  |
| `027B` | LOCATE_COLL_ANY_MEANS_2D |  | default | 0 |  |
| `027C` | LOCATE_COLL_ON_FOOT_2D |  | default | 0 |  |
| `027D` | LOCATE_COLL_IN_CAR_2D |  | default | 0 |  |
| `027E` | LOCATE_STOPPED_COLL_ANY_MEANS_2D |  | default | 0 |  |
| `027F` | LOCATE_STOPPED_COLL_ON_FOOT_2D |  | default | 0 |  |
| `0280` | LOCATE_STOPPED_COLL_IN_CAR_2D |  | default | 0 |  |
| `0281` | LOCATE_COLL_ANY_MEANS_CHAR_2D |  | default | 0 |  |
| `0282` | LOCATE_COLL_ON_FOOT_CHAR_2D |  | default | 0 |  |
| `0283` | LOCATE_COLL_IN_CAR_CHAR_2D |  | default | 0 |  |
| `0284` | LOCATE_COLL_ANY_MEANS_CAR_2D |  | default | 0 |  |
| `0285` | LOCATE_COLL_ON_FOOT_CAR_2D |  | default | 0 |  |
| `0286` | LOCATE_COLL_IN_CAR_CAR_2D |  | default | 0 |  |
| `0287` | LOCATE_COLL_ANY_MEANS_PLAYER_2D |  | default | 0 |  |
| `0288` | LOCATE_COLL_ON_FOOT_PLAYER_2D |  | default | 0 |  |
| `0289` | LOCATE_COLL_IN_CAR_PLAYER_2D |  | default | 0 |  |
| `028A` | IS_COLL_IN_AREA_2D |  | default | 0 |  |
| `028B` | IS_COLL_IN_AREA_ON_FOOT_2D |  | default | 0 |  |
| `028C` | IS_COLL_IN_AREA_IN_CAR_2D |  | default | 0 |  |
| `028D` | IS_COLL_STOPPED_IN_AREA_2D |  | default | 0 |  |
| `028E` | IS_COLL_STOPPED_IN_AREA_ON_FOOT_2D |  | default | 0 |  |
| `028F` | IS_COLL_STOPPED_IN_AREA_IN_CAR_2D |  | default | 0 |  |
| `0290` | GET_NUMBER_OF_PEDS_IN_COLL |  | default | 0 |  |
| `0291` | SET_CHAR_HEED_THREATS |  | default | 0 |  |
| `0292` | SET_PLAYER_HEED_THREATS |  | default | 0 |  |
| `0293` | GET_CONTROLLER_MODE | Pad | default | 1 | Returns the controller mode |
| `0294` | SET_CAN_RESPRAY_CAR | Car | default | 2 | Makes car keep current colors when Pay'n'Spray is used |
| `0295` | IS_TAXI |  | default | 0 |  |
| `0296` | UNLOAD_SPECIAL_CHARACTER | Streaming | default | 1 | Releases the special character (023C), freeing game memory |
| `0297` | RESET_NUM_OF_MODELS_KILLED_BY_PLAYER | Player | default | 1 | Resets the count of how many times the player has destroyed a certain model |
| `0298` | GET_NUM_OF_MODELS_KILLED_BY_PLAYER | Player | default | 3 | Returns the number of times the player has destroyed a specific model |
| `0299` | ACTIVATE_GARAGE | Garage | default | 1 | Activates the garage |
| `029A` | SWITCH_TAXI_TIMER |  | default | 0 |  |
| `029B` | CREATE_OBJECT_NO_OFFSET | Object | default | 5 | Creates an object without offset at the location |
| `029C` | IS_BOAT |  | default | 0 |  |
| `029D` | SET_CHAR_OBJ_GOTO_AREA_ANY_MEANS |  | default | 0 |  |
| `029E` | SET_COLL_OBJ_GOTO_AREA_ANY_MEANS |  | default | 0 |  |
| `029F` | IS_PLAYER_STOPPED |  | default | 0 |  |
| `02A0` | IS_CHAR_STOPPED | Char | default | 1 | Returns true if the character is not moving |
| `02A1` | MESSAGE_WAIT |  | default | 0 |  |
| `02A2` | ADD_PARTICLE_EFFECT |  | default | 0 |  |
| `02A3` | SWITCH_WIDESCREEN | Hud | default | 1 | Enables widescreen |
| `02A4` | ADD_SPRITE_BLIP_FOR_CAR |  | default | 0 | Does nothing |
| `02A5` | ADD_SPRITE_BLIP_FOR_CHAR |  | default | 0 | Does nothing |
| `02A6` | ADD_SPRITE_BLIP_FOR_OBJECT |  | default | 0 |  |
| `02A7` | ADD_SPRITE_BLIP_FOR_CONTACT_POINT | Blip | default | 5 | Adds a long range sprite blip and sphere to the contact point that is not displayed while on mission |
| `02A8` | ADD_SPRITE_BLIP_FOR_COORD | Blip | default | 5 | Adds a sprite blip to the location |
| `02A9` | SET_CHAR_ONLY_DAMAGED_BY_PLAYER | Char | default | 2 | Makes a character immune to everything except the player |
| `02AA` | SET_CAR_ONLY_DAMAGED_BY_PLAYER | Car | default | 2 | Makes a vehicle immune to everything except the player |
| `02AB` | SET_CHAR_PROOFS | Char | default | 6 | Sets the character's immunities |
| `02AC` | SET_CAR_PROOFS | Car | default | 6 | Sets the vehicle's immunities |
| `02AD` | IS_PLAYER_IN_ANGLED_AREA_2D |  | default | 0 |  |
| `02AE` | IS_PLAYER_IN_ANGLED_AREA_ON_FOOT_2D |  | default | 0 |  |
| `02AF` | IS_PLAYER_IN_ANGLED_AREA_IN_CAR_2D |  | default | 0 |  |
| `02B0` | IS_PLAYER_STOPPED_IN_ANGLED_AREA_2D |  | default | 0 |  |
| `02B1` | IS_PLAYER_STOPPED_IN_ANGLED_AREA_ON_FOOT_2D |  | default | 0 |  |
| `02B2` | IS_PLAYER_STOPPED_IN_ANGLED_AREA_IN_CAR_2D |  | default | 0 |  |
| `02B3` | IS_PLAYER_IN_ANGLED_AREA_3D |  | default | 0 |  |
| `02B4` | IS_PLAYER_IN_ANGLED_AREA_ON_FOOT_3D |  | default | 0 |  |
| `02B5` | IS_PLAYER_IN_ANGLED_AREA_IN_CAR_3D |  | default | 0 |  |
| `02B6` | IS_PLAYER_STOPPED_IN_ANGLED_AREA_3D |  | default | 0 |  |
| `02B7` | IS_PLAYER_STOPPED_IN_ANGLED_AREA_ON_FOOT_3D |  | default | 0 |  |
| `02B8` | IS_PLAYER_STOPPED_IN_ANGLED_AREA_IN_CAR_3D |  | default | 0 |  |
| `02B9` | DEACTIVATE_GARAGE | Garage | default | 1 | Deactivates the garage |
| `02BA` | GET_NUMBER_OF_CARS_COLLECTED_BY_GARAGE |  | default | 0 |  |
| `02BB` | HAS_CAR_BEEN_TAKEN_TO_GARAGE |  | default | 0 |  |
| `02BC` | SET_SWAT_REQUIRED |  | default | 0 |  |
| `02BD` | SET_FBI_REQUIRED |  | default | 0 |  |
| `02BE` | SET_ARMY_REQUIRED |  | default | 0 |  |
| `02BF` | IS_CAR_IN_WATER | Car | default | 1 | Returns true if the vehicle is submerged in water |
| `02C0` | GET_CLOSEST_CHAR_NODE | Path | default | 6 | Returns the nearest path node from the specified coordinates that a pedestrian can walk on |
| `02C1` | GET_CLOSEST_CAR_NODE | Path | default | 6 | Returns the nearest path note from the specified coordinates that a vehicle can drive on |
| `02C2` | CAR_GOTO_COORDINATES_ACCURATE | Car | default | 4 | Makes the AI drive to the specified location obeying the traffic rules |
| `02C3` | START_PACMAN_RACE |  | default | 0 |  |
| `02C4` | START_PACMAN_RECORD |  | default | 0 |  |
| `02C5` | GET_NUMBER_OF_POWER_PILLS_EATEN |  | default | 0 |  |
| `02C6` | CLEAR_PACMAN |  | default | 0 |  |
| `02C7` | START_PACMAN_SCRAMBLE |  | default | 0 |  |
| `02C8` | GET_NUMBER_OF_POWER_PILLS_CARRIED |  | default | 0 |  |
| `02C9` | CLEAR_NUMBER_OF_POWER_PILLS_CARRIED |  | default | 0 |  |
| `02CA` | IS_CAR_ON_SCREEN | Car | default | 1 | Returns true if the car is visible |
| `02CB` | IS_CHAR_ON_SCREEN | Char | default | 1 | Returns true if the character is visible |
| `02CC` | IS_OBJECT_ON_SCREEN | Object | default | 1 | Returns true if the object is visible |
| `02CD` | GOSUB_FILE |  | default | 0 |  |
| `02CE` | GET_GROUND_Z_FOR_3D_COORD | World | default | 4 | Stores the ground position at the location |
| `02CF` | START_SCRIPT_FIRE | ScriptFire | default | 6 | Creates a fire at the specified coordinates |
| `02D0` | IS_SCRIPT_FIRE_EXTINGUISHED | ScriptFire | default | 1 | Returns true if the script fire has been put out |
| `02D1` | REMOVE_SCRIPT_FIRE | ScriptFire | default | 1 | Removes the script fire |
| `02D2` | SET_COMEDY_CONTROLS |  | default | 0 |  |
| `02D3` | BOAT_GOTO_COORDS | Boat | default | 4 | Makes the boat sail to the location |
| `02D4` | BOAT_STOP | Boat | default | 1 | Turns off the car's engine |
| `02D5` | IS_PLAYER_SHOOTING_IN_AREA |  | default | 0 |  |
| `02D6` | IS_CHAR_SHOOTING_IN_AREA | Char | default | 6 | Returns true if the character fired a weapon within the specified 2D area |
| `02D7` | IS_CURRENT_PLAYER_WEAPON |  | default | 0 |  |
| `02D8` | IS_CURRENT_CHAR_WEAPON | Char | default | 2 | Returns true if the character is holding the given type of weapon |
| `02D9` | CLEAR_NUMBER_OF_POWER_PILLS_EATEN |  | default | 0 |  |
| `02DA` | ADD_POWER_PILL |  | default | 0 |  |
| `02DB` | SET_BOAT_CRUISE_SPEED | Boat | default | 2 | Sets the boat's max speed |
| `02DC` | GET_RANDOM_CHAR_IN_AREA |  | default | 0 |  |
| `02DD` | GET_RANDOM_CHAR_IN_ZONE | Zone | default | 5 | Gets a random character in the specified zone whose pedtype matches the specified values |
| `02DE` | IS_PLAYER_IN_TAXI |  | default | 0 |  |
| `02DF` | IS_PLAYER_SHOOTING |  | default | 0 |  |
| `02E0` | IS_CHAR_SHOOTING | Char | default | 1 | Returns true if the character is firing a weapon |
| `02E1` | CREATE_MONEY_PICKUP | Pickup | default | 6 | Creates a money pickup with the specified cash value |
| `02E2` | SET_CHAR_ACCURACY | Char | default | 2 | Affects how often the character will hit the target when attacking with a weapon |
| `02E3` | GET_CAR_SPEED | Car | default | 2 | Gets the car's speed |
| `02E4` | LOAD_CUTSCENE | Cutscene | default | 1 | Loads the data for the specified cutscene |
| `02E5` | CREATE_CUTSCENE_OBJECT |  | default | 0 |  |
| `02E6` | SET_CUTSCENE_ANIM |  | default | 0 |  |
| `02E7` | START_CUTSCENE | Cutscene | default | 0 | Starts the loaded cutscene (02E4) |
| `02E8` | GET_CUTSCENE_TIME | Cutscene | default | 1 | Returns the time in milliseconds passed since the cutscene has started (02E7) |
| `02E9` | HAS_CUTSCENE_FINISHED | Cutscene | default | 0 | Returns true if the cutscene has finished |
| `02EA` | CLEAR_CUTSCENE | Cutscene | default | 0 | Ends the current cutscene, freeing game memory |
| `02EB` | RESTORE_CAMERA_JUMPCUT | Camera | default | 0 | Restores the camera, putting it back behind the player |
| `02EC` | CREATE_COLLECTABLE1 |  | default | 3 | Does nothing |
| `02ED` | SET_COLLECTABLE1_TOTAL | Game | default | 1 | Sets the total number of hidden packages to collect |
| `02EE` | IS_PROJECTILE_IN_AREA | World | default | 6 | Returns true if a projectile is in the specified 3D area |
| `02EF` | DESTROY_PROJECTILES_IN_AREA |  | default | 0 |  |
| `02F0` | DROP_MINE |  | default | 0 |  |
| `02F1` | DROP_NAUTICAL_MINE |  | default | 0 |  |
| `02F2` | IS_CHAR_MODEL | Char | default | 2 | Returns true if the character's model ID is equivalent to the model ID passed |
| `02F3` | LOAD_SPECIAL_MODEL |  | default | 0 |  |
| `02F4` | CREATE_CUTSCENE_HEAD |  | default | 0 |  |
| `02F5` | SET_CUTSCENE_HEAD_ANIM |  | default | 0 |  |
| `02F6` | SIN | Math | default | 2 | Returns the sine of the angle |
| `02F7` | COS | Math | default | 2 | Returns the cosine of the angle |
| `02F8` | GET_CAR_FORWARD_X | Car | default | 2 | Returns the X coord of the vehicle's angle |
| `02F9` | GET_CAR_FORWARD_Y | Car | default | 2 | Returns the Y coord of the vehicle's angle |
| `02FA` | CHANGE_GARAGE_TYPE | Garage | default | 2 | Sets the garage's type |
| `02FB` | ACTIVATE_CRUSHER_CRANE |  | default | 0 |  |
| `02FC` | PRINT_WITH_2_NUMBERS |  | default | 0 |  |
| `02FD` | PRINT_WITH_2_NUMBERS_NOW | Text | default | 5 | Displays a styled message in which the first two ~1~ tokens are substituted with the specified numbers |
| `02FE` | PRINT_WITH_2_NUMBERS_SOON |  | default | 0 |  |
| `02FF` | PRINT_WITH_3_NUMBERS | Text | default | 6 | Displays a styled message in which the first three ~1~ tokens are substituted with the specified numbers |
| `0300` | PRINT_WITH_3_NUMBERS_NOW |  | default | 0 |  |
| `0301` | PRINT_WITH_3_NUMBERS_SOON |  | default | 0 |  |
| `0302` | PRINT_WITH_4_NUMBERS | Text | default | 7 | Displays a styled message in which the first four ~1~ tokens are substituted with the specified numbers |
| `0303` | PRINT_WITH_4_NUMBERS_NOW | Text | default | 7 | Displays a styled message in which the first four ~1~ tokens are substituted with the specified numbers |
| `0304` | PRINT_WITH_4_NUMBERS_SOON |  | default | 0 |  |
| `0305` | PRINT_WITH_5_NUMBERS |  | default | 0 |  |
| `0306` | PRINT_WITH_5_NUMBERS_NOW |  | default | 0 |  |
| `0307` | PRINT_WITH_5_NUMBERS_SOON |  | default | 0 |  |
| `0308` | PRINT_WITH_6_NUMBERS | Text | default | 9 | Displays a styled message in which the first six ~1~ tokens are substituted with the specified numbers |
| `0309` | PRINT_WITH_6_NUMBERS_NOW |  | default | 0 |  |
| `030A` | PRINT_WITH_6_NUMBERS_SOON |  | default | 0 |  |
| `030B` | SET_CHAR_OBJ_FOLLOW_CHAR_IN_FORMATION |  | default | 0 |  |
| `030C` | PLAYER_MADE_PROGRESS | Stat | default | 1 | Increases the progress made stat by the specified amount |
| `030D` | SET_PROGRESS_TOTAL | Stat | default | 1 | Sets the maximum progress the player can reach |
| `030E` | REGISTER_JUMP_DISTANCE |  | default | 0 |  |
| `030F` | REGISTER_JUMP_HEIGHT |  | default | 0 |  |
| `0310` | REGISTER_JUMP_FLIPS |  | default | 0 |  |
| `0311` | REGISTER_JUMP_SPINS |  | default | 0 |  |
| `0312` | REGISTER_JUMP_STUNT |  | default | 0 |  |
| `0313` | REGISTER_UNIQUE_JUMP_FOUND |  | default | 0 |  |
| `0314` | SET_UNIQUE_JUMPS_TOTAL |  | default | 0 |  |
| `0315` | REGISTER_PASSENGER_DROPPED_OFF_TAXI |  | default | 0 |  |
| `0316` | REGISTER_MONEY_MADE_TAXI |  | default | 0 |  |
| `0317` | REGISTER_MISSION_GIVEN | Stat | default | 0 | Increments the number of mission attempts stat by one |
| `0318` | REGISTER_MISSION_PASSED | Stat | default | 1 | Sets the GXT of the last mission passed |
| `0319` | SET_CHAR_RUNNING |  | default | 0 |  |
| `031A` | REMOVE_ALL_SCRIPT_FIRES | World | default | 0 | Removes all script fires (02CF) |
| `031B` | IS_FIRST_CAR_COLOUR |  | default | 0 |  |
| `031C` | IS_SECOND_CAR_COLOUR |  | default | 0 |  |
| `031D` | HAS_CHAR_BEEN_DAMAGED_BY_WEAPON | Char | default | 2 | Returns true if the character has been hit by the specified weapon |
| `031E` | HAS_CAR_BEEN_DAMAGED_BY_WEAPON | Car | default | 2 | Returns true if the vehicle has been hit by the specified weapon |
| `031F` | IS_CHAR_IN_CHARS_GROUP |  | default | 0 |  |
| `0320` | IS_CHAR_IN_PLAYERS_GROUP |  | default | 0 |  |
| `0321` | EXPLODE_CHAR_HEAD | Char | default | 1 | Dismembers the character |
| `0322` | EXPLODE_PLAYER_HEAD |  | default | 0 |  |
| `0323` | ANCHOR_BOAT | Boat | default | 2 | Makes the boat stay motionless in the water |
| `0324` | SET_ZONE_GROUP |  | default | 0 |  |
| `0325` | START_CAR_FIRE | ScriptFire | default | 2 | Creates a script fire on the vehicle |
| `0326` | START_CHAR_FIRE | ScriptFire | default | 2 | Creates a script fire on the character |
| `0327` | GET_RANDOM_CAR_OF_TYPE_IN_AREA | World | default | 6 | Returns the handle of a random car with the specified model in the specified 2D area, or -1 otherwise |
| `0328` | GET_RANDOM_CAR_OF_TYPE_IN_ZONE |  | default | 0 |  |
| `0329` | HAS_RESPRAY_HAPPENED |  | default | 0 | Returns true if the players car has been resprayed by the garage |
| `032A` | SET_CAMERA_ZOOM | Camera | default | 1 | Sets how far behind the camera is from the player |
| `032B` | CREATE_PICKUP_WITH_AMMO | Pickup | default | 7 | Creates a weapon pickup, giving the player the specified amount of ammo when they pick it up |
| `032C` | SET_CAR_RAM_CAR |  | default | 0 | Sets the cars goal to ram another car |
| `032D` | SET_CAR_BLOCK_CAR |  | default | 0 |  |
| `032E` | SET_CHAR_OBJ_CATCH_TRAIN |  | default | 0 |  |
| `032F` | SET_COLL_OBJ_CATCH_TRAIN |  | default | 0 |  |
| `0330` | SET_PLAYER_NEVER_GETS_TIRED | Player | default | 2 | Defines whether the player can run fast forever |
| `0331` | SET_PLAYER_FAST_RELOAD | Player | default | 2 | Defines whether the player can reload their gun 4x times faster |
| `0332` | SET_CHAR_BLEEDING | Char | default | 2 | Makes a character bleed |
| `0333` | SET_CAR_FUNNY_SUSPENSION |  | default | 0 |  |
| `0334` | SET_CAR_BIG_WHEELS |  | default | 0 |  |
| `0335` | SET_FREE_RESPRAYS | Game | default | 1 | Defines whether the player can respray their car for free |
| `0336` | SET_PLAYER_VISIBLE |  | default | 0 |  |
| `0337` | SET_CHAR_VISIBLE | Char | default | 2 | Sets whether the character is visible or not |
| `0338` | SET_CAR_VISIBLE | Car | default | 2 | Sets whether the vehicle is visible or not |
| `0339` | IS_AREA_OCCUPIED | World | default | 11 | Returns true if there is anything with the specified properties within the 3D area |
| `033A` | START_DRUG_RUN |  | default | 0 |  |
| `033B` | HAS_DRUG_RUN_BEEN_COMPLETED |  | default | 0 |  |
| `033C` | HAS_DRUG_PLANE_BEEN_SHOT_DOWN |  | default | 0 |  |
| `033D` | SAVE_PLAYER_FROM_FIRES |  | default | 0 |  |
| `033E` | DISPLAY_TEXT | Text | default | 3 | Draws text at the specified on-screen position |
| `033F` | SET_TEXT_SCALE | Text | default | 2 | Scales the width and height of the text letters |
| `0340` | SET_TEXT_COLOUR | Text | default | 4 | Sets the color of the text letters |
| `0341` | SET_TEXT_JUSTIFY | Text | default | 1 | Sets the text to be drawn justified, which means the text will wrap in order to fill an even rectangle of space |
| `0342` | SET_TEXT_CENTRE | Text | default | 1 | Centers the text |
| `0343` | SET_TEXT_WRAPX | Text | default | 1 | Sets the line width of the text |
| `0344` | SET_TEXT_CENTRE_SIZE | Text | default | 1 | Sets the line width of the centered text |
| `0345` | SET_TEXT_BACKGROUND | Text | default | 1 | Gives the text a background (0346) |
| `0346` | SET_TEXT_BACKGROUND_COLOUR |  | default | 0 |  |
| `0347` | SET_TEXT_BACKGROUND_ONLY_TEXT |  | default | 0 |  |
| `0348` | SET_TEXT_PROPORTIONAL | Text | default | 1 | Makes the text size proportionate |
| `0349` | SET_TEXT_FONT | Text | default | 1 | Sets the text draw font |
| `034A` | INDUSTRIAL_PASSED |  | default | 0 |  |
| `034B` | COMMERCIAL_PASSED |  | default | 0 |  |
| `034C` | SUBURBAN_PASSED |  | default | 0 |  |
| `034D` | ROTATE_OBJECT | Object | default | 4 | Rotates the object from one angle to another, optionally accounting for a collision during the rotation |
| `034E` | SLIDE_OBJECT | Object | default | 8 | Animates object movement toward specified coordinates. Returns true if the object has finished moving |
| `034F` | REMOVE_CHAR_ELEGANTLY | Char | default | 1 | Removes the character with a fade, freeing game memory |
| `0350` | SET_CHAR_STAY_IN_SAME_PLACE | Char | default | 2 | Makes the character maintain their position when attacked |
| `0351` | IS_NASTY_GAME |  | default | 0 |  |
| `0352` | UNDRESS_CHAR |  | default | 0 |  |
| `0353` | DRESS_CHAR |  | default | 0 |  |
| `0354` | START_CHASE_SCENE |  | default | 0 |  |
| `0355` | STOP_CHASE_SCENE |  | default | 0 |  |
| `0356` | IS_EXPLOSION_IN_AREA | World | default | 7 | Returns true if there is an explosion of the specified type in the 3D area |
| `0357` | IS_EXPLOSION_IN_ZONE |  | default | 0 |  |
| `0358` | START_DRUG_DROP_OFF |  | default | 0 |  |
| `0359` | HAS_DROP_OFF_PLANE_BEEN_SHOT_DOWN |  | default | 0 |  |
| `035A` | FIND_DROP_OFF_PLANE_COORDINATES |  | default | 0 |  |
| `035B` | CREATE_FLOATING_PACKAGE |  | default | 0 |  |
| `035C` | PLACE_OBJECT_RELATIVE_TO_CAR | Object | default | 5 | Places the object at an offset from the car |
| `035D` | MAKE_OBJECT_TARGETTABLE | Object | default | 2 | Sets whether the object can be targeted (auto-aimed) or not |
| `035E` | ADD_ARMOUR_TO_PLAYER |  | default | 0 |  |
| `035F` | ADD_ARMOUR_TO_CHAR | Char | default | 2 | Increases the character's armor by the specified value to the maximum of 100 |
| `0360` | OPEN_GARAGE | Garage | default | 1 | Opens the garage |
| `0361` | CLOSE_GARAGE | Garage | default | 1 | Closes the garage |
| `0362` | WARP_CHAR_FROM_CAR_TO_COORD | Char | default | 4 | Pulls the character out of their car and places at the location |
| `0363` | SET_VISIBILITY_OF_CLOSEST_OBJECT_OF_TYPE | World | default | 6 | Sets the visibility of the object closest to the specified coordinates, matching the specified model |
| `0364` | HAS_CHAR_SPOTTED_CHAR | Char | default | 2 | Returns true if the character can see the target character |
| `0365` | SET_CHAR_OBJ_HAIL_TAXI |  | default | 0 |  |
| `0366` | HAS_OBJECT_BEEN_DAMAGED | Object | default | 1 | Returns true if the object is damaged |
| `0367` | START_KILL_FRENZY_HEADSHOT |  | default | 0 |  |
| `0368` | ACTIVATE_MILITARY_CRANE |  | default | 0 |  |
| `0369` | WARP_PLAYER_INTO_CAR |  | default | 0 |  |
| `036A` | WARP_CHAR_INTO_CAR | Char | default | 2 | Puts the character in the specified vehicle |
| `036B` | SWITCH_CAR_RADIO |  | default | 0 |  |
| `036C` | SET_AUDIO_STREAM |  | default | 0 |  |
| `036D` | PRINT_WITH_2_NUMBERS_BIG | Text | default | 5 | Displays a styled message in which the first two ~1~ tokens are substituted with the specified numbers |
| `036E` | PRINT_WITH_3_NUMBERS_BIG |  | default | 0 |  |
| `036F` | PRINT_WITH_4_NUMBERS_BIG |  | default | 0 |  |
| `0370` | PRINT_WITH_5_NUMBERS_BIG |  | default | 0 |  |
| `0371` | PRINT_WITH_6_NUMBERS_BIG |  | default | 0 |  |
| `0372` | SET_CHAR_WAIT_STATE |  | default | 0 |  |
| `0373` | SET_CAMERA_BEHIND_PLAYER | Camera | default | 0 | Puts the camera behind the player |
| `0374` | SET_MOTION_BLUR |  | default | 0 |  |
| `0375` | PRINT_STRING_IN_STRING |  | default | 0 |  |
| `0376` | CREATE_RANDOM_CHAR | Char | default | 4 | Creates a character with a randomised model and pedtype at the specified coordinates |
| `0377` | SET_CHAR_OBJ_STEAL_ANY_CAR |  | default | 0 |  |
| `0378` | SET_2_REPEATED_PHONE_MESSAGES |  | default | 0 |  |
| `0379` | SET_2_PHONE_MESSAGES |  | default | 0 |  |
| `037A` | SET_3_REPEATED_PHONE_MESSAGES |  | default | 0 |  |
| `037B` | SET_3_PHONE_MESSAGES |  | default | 0 |  |
| `037C` | SET_4_REPEATED_PHONE_MESSAGES |  | default | 0 |  |
| `037D` | SET_4_PHONE_MESSAGES |  | default | 0 |  |
| `037E` | IS_SNIPER_BULLET_IN_AREA |  | default | 0 | Returns true if a sniper bullet is in the specified area |
| `037F` | GIVE_PLAYER_DETONATOR |  | default | 0 |  |
| `0380` | SET_COLL_OBJ_STEAL_ANY_CAR |  | default | 0 |  |
| `0381` | SET_OBJECT_VELOCITY | Object | default | 4 | Sets the object's velocity |
| `0382` | SET_OBJECT_COLLISION | Object | default | 2 | Sets the object's collision detection |
| `0383` | IS_ICECREAM_JINGLE_ON |  | default | 0 | Returns true if the vehicles siren is on |
| `0384` | PRINT_STRING_IN_STRING_NOW | Text | default | 4 | Displays a styled message in which the first string token ~a~ is substituted with the specified text |
| `0385` | PRINT_STRING_IN_STRING_SOON |  | default | 0 |  |
| `0386` | SET_5_REPEATED_PHONE_MESSAGES |  | default | 0 |  |
| `0387` | SET_5_PHONE_MESSAGES |  | default | 0 |  |
| `0388` | SET_6_REPEATED_PHONE_MESSAGES |  | default | 0 |  |
| `0389` | SET_6_PHONE_MESSAGES |  | default | 0 |  |
| `038A` | IS_POINT_OBSCURED_BY_A_MISSION_ENTITY | World | default | 6 | Returns true if there is a vehicle in the specified area |
| `038B` | LOAD_ALL_MODELS_NOW | Streaming | default | 0 | Loads any requested models (0247 or 0353) synchronously |
| `038C` | ADD_TO_OBJECT_VELOCITY | Object | default | 4 | Adds the given vector to the object's velocity (0381) |
| `038D` | DRAW_SPRITE | Hud | default | 9 | Draws a loaded texture (038F) at the specified on-screen X and Y coordinates, with the specified size and RGBA color |
| `038E` | DRAW_RECT | Hud | default | 8 | Draws a box at the specified screen X and Y position, with the specified size and RGBA colors |
| `038F` | LOAD_SPRITE | Txd | default | 2 | Loads a sprite from the most recently loaded texture dictionary (0390) |
| `0390` | LOAD_TEXTURE_DICTIONARY | Txd | default | 1 | Loads the texture dictionary for use in drawing sprites (038D) on the screen |
| `0391` | REMOVE_TEXTURE_DICTIONARY | Txd | default | 0 | Unloads all currently loaded textures (038F), as well as texture dictionaries (0390), freeing game memory |
| `0392` | SET_OBJECT_DYNAMIC | Object | default | 2 | Defines whether or not the object is moveable |
| `0393` | SET_CHAR_ANIM_SPEED | Char | default | 3 | Makes an char perform an animation at the specified speed |
| `0394` | PLAY_MISSION_PASSED_TUNE | Audio | default | 1 | Plays an audio file with the specified ID from the Audio directory |
| `0395` | CLEAR_AREA | World | default | 5 | Clears the area, removing all vehicles and pedestrians that are not marked as needed by a mission |
| `0396` | FREEZE_ONSCREEN_TIMER | Hud | default | 1 | Makes the on-screen timer stop updating |
| `0397` | SWITCH_CAR_SIREN | Car | default | 2 | Sets whether the car's alarm can be activated |
| `0398` | SWITCH_PED_ROADS_ON_ANGLED |  | default | 0 |  |
| `0399` | SWITCH_PED_ROADS_OFF_ANGLED |  | default | 0 |  |
| `039A` | SWITCH_ROADS_ON_ANGLED |  | default | 0 |  |
| `039B` | SWITCH_ROADS_OFF_ANGLED |  | default | 0 |  |
| `039C` | SET_CAR_WATERTIGHT | Car | default | 2 | Makes the vehicle watertight, meaning characters inside will not be harmed if the vehicle is submerged in water |
| `039D` | ADD_MOVING_PARTICLE_EFFECT |  | default | 0 |  |
| `039E` | SET_CHAR_CANT_BE_DRAGGED_OUT | Char | default | 2 | Locks the character while in a car |
| `039F` | TURN_CAR_TO_FACE_COORD | Car | default | 3 | Sets the car's heading so that it is facing the 2D coordinate |
| `03A0` | IS_CRANE_LIFTING_CAR |  | default | 0 |  |
| `03A1` | DRAW_SPHERE | Sphere | default | 4 | Displays a red cylinder sphere |
| `03A2` | SET_CAR_STATUS | Car | default | 2 | Sets the car's status |
| `03A3` | IS_CHAR_MALE | Char | default | 1 | Returns true if the character is male |
| `03A4` | SCRIPT_NAME |  | default | 1 | Assigns a new name to the current script |
| `03A5` | CHANGE_GARAGE_TYPE_WITH_CAR_MODEL |  | default | 0 |  |
| `03A6` | FIND_DRUG_PLANE_COORDINATES |  | default | 0 |  |
| `03A7` | SAVE_INT_TO_DEBUG_FILE |  | default | 1 | Saves an integer to a debug file |
| `03A8` | SAVE_FLOAT_TO_DEBUG_FILE |  | default | 1 | Saves a float to the debug file |
| `03A9` | SAVE_NEWLINE_TO_DEBUG_FILE |  | default | 0 | Writes a newline to the debug file |
| `03AA` | POLICE_RADIO_MESSAGE |  | default | 3 | Plays police radio message audio reporting the suspect has last been seen in the area specified by the coordinates |
| `03AB` | SET_CAR_STRONG | Car | default | 2 | Defines whether the car is more resistant to collisions than normal |
| `03AC` | REMOVE_ROUTE |  | default | 0 |  |
| `03AD` | SWITCH_RUBBISH |  | default | 1 | Toggles garbage |
| `03AE` | REMOVE_PARTICLE_EFFECTS_IN_AREA |  | default | 0 |  |
| `03AF` | SWITCH_STREAMING | Streaming | default | 1 | Sets the streaming of additional models like peds, cars, and maps |
| `03B0` | IS_GARAGE_OPEN | Garage | default | 1 | Returns true if the garage's door is open |
| `03B1` | IS_GARAGE_CLOSED | Garage | default | 1 | Returns true if the garage's door is closed |
| `03B2` | START_CATALINA_HELI |  | default | 0 |  |
| `03B3` | CATALINA_HELI_TAKE_OFF |  | default | 0 |  |
| `03B4` | REMOVE_CATALINA_HELI |  | default | 0 |  |
| `03B5` | HAS_CATALINA_HELI_BEEN_SHOT_DOWN |  | default | 0 |  |
| `03B6` | SWAP_NEAREST_BUILDING_MODEL | World | default | 6 | Swaps a map model with another map model nearest to the center of the search area |
| `03B7` | SWITCH_WORLD_PROCESSING | World | default | 1 | Sets whether the game should render the world or only the cutscene objects |
| `03B8` | REMOVE_ALL_PLAYER_WEAPONS |  | default | 0 |  |
| `03B9` | GRAB_CATALINA_HELI |  | default | 0 |  |
| `03BA` | CLEAR_AREA_OF_CARS | World | default | 6 | Clears all cars in the specified 3D area |
| `03BB` | SET_ROTATING_GARAGE_DOOR |  | default | 0 |  |
| `03BC` | ADD_SPHERE | Sphere | default | 5 | Creates a static sphere at the location, with the specified radius |
| `03BD` | REMOVE_SPHERE | Sphere | default | 1 | Destroys a static sphere |
| `03BE` | CATALINA_HELI_FLY_AWAY |  | default | 0 |  |
| `03BF` | SET_EVERYONE_IGNORE_PLAYER | Game | default | 2 | Makes pedestrians pay no attention to the player |
| `03C0` | STORE_CAR_CHAR_IS_IN_NO_SAVE | Char | default | 2 | Returns the character's vehicle handle without marking it as used by the script, therefore allowing it to be deleted by the game at any time (alts:00D9,0811,0484) |
| `03C1` | STORE_CAR_PLAYER_IS_IN_NO_SAVE |  | default | 0 |  |
| `03C2` | IS_PHONE_DISPLAYING_MESSAGE |  | default | 0 |  |
| `03C3` | DISPLAY_ONSCREEN_TIMER_WITH_STRING | Hud | default | 3 | Creates a countdown or countup onscreen timer with the text |
| `03C4` | DISPLAY_ONSCREEN_COUNTER_WITH_STRING | Hud | default | 3 | Displays an onscreen counter with the text, either shown in numbers or as a bar |
| `03C5` | CREATE_RANDOM_CAR_FOR_CAR_PARK | World | default | 4 | Starts spawning random cars at the specified location |
| `03C6` | IS_COLLISION_IN_MEMORY |  | default | 0 |  |
| `03C7` | SET_WANTED_MULTIPLIER | Game | default | 1 | Sets sensitivity to crime, changing how many crimes a player can commit before police begin to pursue |
| `03C8` | SET_CAMERA_IN_FRONT_OF_PLAYER | Camera | default | 0 | Puts the camera in front of the player, pointing towards the player |
| `03C9` | IS_CAR_VISIBLY_DAMAGED | Car | default | 1 | Returns true if any of the car components is visibly damaged or lost |
| `03CA` | DOES_OBJECT_EXIST | Object | default | 1 | Returns true if the handle is a valid object handle |
| `03CB` | LOAD_SCENE | Streaming | default | 3 | Starts loading a specific location, just like if the player was there, removing LOD textures |
| `03CC` | ADD_STUCK_CAR_CHECK | StuckCarCheck | default | 3 | Adds the vehicle to the stuck cars array |
| `03CD` | REMOVE_STUCK_CAR_CHECK | StuckCarCheck | default | 1 | Removes the vehicle from the stuck cars array |
| `03CE` | IS_CAR_STUCK | StuckCarCheck | default | 1 | Returns true if the car is stuck |
| `03CF` | LOAD_MISSION_AUDIO | Audio | default | 2 | Loads the file from the audio directory |
| `03D0` | HAS_MISSION_AUDIO_LOADED | Audio | default | 1 | Returns true if the mission audio requested with LOAD_MISSION_AUDIO has loaded |
| `03D1` | PLAY_MISSION_AUDIO | Audio | default | 1 | Plays the loaded sound (03CF) |
| `03D2` | HAS_MISSION_AUDIO_FINISHED | Audio | default | 1 | Returns true if the audio (03CF) is no longer playing |
| `03D3` | GET_CLOSEST_CAR_NODE_WITH_HEADING | Path | default | 7 | Returns the position and heading of the closest vehicle path node to the specified position |
| `03D4` | HAS_IMPORT_GARAGE_SLOT_BEEN_FILLED |  | default | 0 | Returns true if the import slot has been filled |
| `03D5` | CLEAR_THIS_PRINT | Text | default | 1 | Removes the priority text from the screen |
| `03D6` | CLEAR_THIS_BIG_PRINT | Text | default | 1 | Removes the styled text from the screen |
| `03D7` | SET_MISSION_AUDIO_POSITION | Audio | default | 4 | Sets the location of the mission audio (03CF) where it can be heard |
| `03D8` | ACTIVATE_SAVE_MENU | Game | default | 0 | Displays a screen prompting the player to save |
| `03D9` | HAS_SAVE_GAME_FINISHED | Game | default | 0 | Returns true if the player has saved their game |
| `03DA` | NO_SPECIAL_CAMERA_FOR_THIS_GARAGE |  | default | 0 |  |
| `03DB` | ADD_BLIP_FOR_PICKUP_OLD |  | default | 0 |  |
| `03DC` | ADD_BLIP_FOR_PICKUP | Blip | default | 2 | Adds a blip and a marker to the pickup |
| `03DD` | ADD_SPRITE_BLIP_FOR_PICKUP |  | default | 0 |  |
| `03DE` | SET_PED_DENSITY_MULTIPLIER | World | default | 1 | Sets the quantity of pedestrians to spawn in the game |
| `03DF` | FORCE_RANDOM_PED_TYPE |  | default | 0 | Forces a model on all randomly spawning peds |
| `03E0` | SET_TEXT_DRAW_BEFORE_FADE | Text | default | 1 | Causes the next text to be drawn before the fade is drawn |
| `03E1` | GET_COLLECTABLE1S_COLLECTED |  | default | 0 | Gets the number of collectable1s collected |
| `03E2` | SET_CHAR_OBJ_LEAVE_ANY_CAR |  | default | 0 |  |
| `03E3` | SET_SPRITES_DRAW_BEFORE_FADE | Hud | default | 1 | Causes the next texture to be drawn (038D) before the fade is drawn |
| `03E4` | SET_TEXT_RIGHT_JUSTIFY | Text | default | 1 | Sets the text draw to be aligned to the right |
| `03E5` | PRINT_HELP | Text | default | 1 | Displays a black text box for a few seconds |
| `03E6` | CLEAR_HELP | Text | default | 0 | Removes the text box from the screen |
| `03E7` | FLASH_HUD_OBJECT | Hud | default | 1 | Makes a specific part of the HUD disappear and reappear several times |
| `03E8` | FLASH_RADAR_BLIP |  | default | 0 | Does nothing |
| `03E9` | IS_CHAR_IN_CONTROL |  | default | 0 |  |
| `03EA` | SET_GENERATE_CARS_AROUND_CAMERA |  | default | 0 |  |
| `03EB` | CLEAR_SMALL_PRINTS | Text | default | 0 | Clears small messages from the screen |
| `03EC` | HAS_MILITARY_CRANE_COLLECTED_ALL_CARS |  | default | 0 |  |
| `03ED` | SET_UPSIDEDOWN_CAR_NOT_DAMAGED | Car | default | 2 | Disables the car from exploding when it is upside down, as long as the player is not in the vehicle |
| `03EE` | CAN_PLAYER_START_MISSION | Player | default | 1 | Returns true if the player can move |
| `03EF` | MAKE_PLAYER_SAFE_FOR_CUTSCENE | Player | default | 1 | Makes the player safe, putting the character in a safe location |
| `03F0` | USE_TEXT_COMMANDS | Text | default | 1 | Enables text and texture drawing |
| `03F1` | SET_THREAT_FOR_PED_TYPE |  | default | 0 |  |
| `03F2` | CLEAR_THREAT_FOR_PED_TYPE |  | default | 0 |  |
| `03F3` | GET_CAR_COLOURS | Car | default | 3 | Gets the car's primary and secondary colors |
| `03F4` | SET_ALL_CARS_CAN_BE_DAMAGED | Game | default | 1 | Sets whether all cars receive damage |
| `03F5` | SET_CAR_CAN_BE_DAMAGED | Car | default | 2 | Sets whether the car receives damage |
| `03F6` | MAKE_PLAYER_UNSAFE |  | default | 0 |  |
| `03F7` | LOAD_COLLISION |  | default | 0 |  |
| `03F8` | GET_BODY_CAST_HEALTH |  | default | 0 |  |
| `03F9` | SET_CHARS_CHATTING |  | default | 0 |  |
| `03FA` | MAKE_PLAYER_SAFE |  | default | 0 |  |
| `03FB` | SET_CAR_STAYS_IN_CURRENT_LEVEL |  | default | 0 |  |
| `03FC` | SET_CHAR_STAYS_IN_CURRENT_LEVEL |  | default | 0 |  |
| `03FD` | SET_DRUNK_INPUT_DELAY | Pad | default | 2 | Affects the delay to the left and right steering while driving |
| `03FE` | SET_CHAR_MONEY | Char | default | 2 | Sets the character's cash sum, setting how much cash they will drop when dead |
| `03FF` | INCREASE_CHAR_MONEY |  | default | 0 |  |
| `0400` | GET_OFFSET_FROM_OBJECT_IN_WORLD_COORDS | Object | default | 7 | Returns the object's coordinates with an offset |
| `0401` | REGISTER_LIFE_SAVED |  | default | 0 |  |
| `0402` | REGISTER_CRIMINAL_CAUGHT |  | default | 0 |  |
| `0403` | REGISTER_AMBULANCE_LEVEL |  | default | 0 |  |
| `0404` | REGISTER_FIRE_EXTINGUISHED |  | default | 0 |  |
| `0405` | TURN_PHONE_ON |  | default | 0 |  |
| `0406` | REGISTER_LONGEST_DODO_FLIGHT |  | default | 0 |  |
| `0407` | GET_OFFSET_FROM_CAR_IN_WORLD_COORDS | Car | default | 7 | Returns the coordinates of an offset of the vehicle's position, depending on the vehicle's rotation |
| `0408` | SET_TOTAL_NUMBER_OF_KILL_FRENZIES |  | default | 0 |  |
| `0409` | BLOW_UP_RC_BUGGY |  | default | 0 |  |
| `040A` | REMOVE_CAR_FROM_CHASE |  | default | 0 |  |
| `040B` | IS_FRENCH_GAME |  | default | 0 | Returns true if the game is in French |
| `040C` | IS_GERMAN_GAME | Game | default | 0 | Returns true if the game language is set to German |
| `040D` | CLEAR_MISSION_AUDIO | Audio | default | 1 | Unloads the mission audio (03CF), freeing game memory |
| `040E` | SET_FADE_IN_AFTER_NEXT_ARREST |  | default | 0 |  |
| `040F` | SET_FADE_IN_AFTER_NEXT_DEATH |  | default | 0 |  |
| `0410` | SET_GANG_PED_MODEL_PREFERENCE |  | default | 0 |  |
| `0411` | SET_CHAR_USE_PEDNODE_SEEK |  | default | 0 |  |
| `0412` | SWITCH_VEHICLE_WEAPONS |  | default | 0 |  |
| `0413` | SET_GET_OUT_OF_JAIL_FREE |  | default | 0 |  |
| `0414` | SET_FREE_HEALTH_CARE | Player | default | 2 | Sets whether the player loses the cash when gets wasted (works once) |
| `0415` | IS_CAR_DOOR_CLOSED |  | default | 0 |  |
| `0416` | LOAD_AND_LAUNCH_MISSION |  | default | 0 | Does nothing |
| `0417` | LOAD_AND_LAUNCH_MISSION_INTERNAL | Mission | default | 1 | Loads a mission from the list defined in the main.scm header |
| `0418` | SET_OBJECT_DRAW_LAST | Object | default | 2 | Sets the specified object to always draw on top of other objects |
| `0419` | GET_AMMO_IN_PLAYER_WEAPON |  | default | 0 |  |
| `041A` | GET_AMMO_IN_CHAR_WEAPON | Char | default | 3 | Gets the amount of ammo in the specified weapon of the character |
| `041B` | REGISTER_KILL_FRENZY_PASSED |  | default | 0 |  |
| `041C` | SET_CHAR_SAY |  | default | 0 |  |
| `041D` | SET_NEAR_CLIP | Camera | default | 1 | Sets camera minimum drawing distance |
| `041E` | SET_RADIO_CHANNEL | Audio | default | 1 | Sets the current radio station that is playing, if the player is in a vehicle |
| `041F` | OVERRIDE_HOSPITAL_LEVEL |  | default | 0 |  |
| `0420` | OVERRIDE_POLICE_STATION_LEVEL |  | default | 0 |  |
| `0421` | FORCE_RAIN |  | default | 0 |  |
| `0422` | DOES_GARAGE_CONTAIN_CAR |  | default | 0 |  |
| `0423` | SET_CAR_TRACTION | Car | default | 2 | Overrides the default AI controlled vehicle traction value of 1.0 |
| `0424` | ARE_MEASUREMENTS_IN_METRES | Game | default | 0 | Returns true if the game uses metric measurements (meters instead of feet) |
| `0425` | CONVERT_METRES_TO_FEET | Math | default | 2 | Returns the result of converting meters to feet |
| `0426` | MARK_ROADS_BETWEEN_LEVELS |  | default | 0 |  |
| `0427` | MARK_PED_ROADS_BETWEEN_LEVELS |  | default | 0 |  |
| `0428` | SET_CAR_AVOID_LEVEL_TRANSITIONS | Car | default | 2 | Sets whether the vehicle will avoid paths between levels (0426) |
| `0429` | SET_CHAR_AVOID_LEVEL_TRANSITIONS |  | default | 0 |  |
| `042A` | IS_THREAT_FOR_PED_TYPE |  | default | 0 |  |
| `042B` | CLEAR_AREA_OF_CHARS | World | default | 6 | Clears all pedestrians from the given area |
| `042C` | SET_TOTAL_NUMBER_OF_MISSIONS | Stat | default | 1 | Sets the total number of missions that can be completed |
| `042D` | CONVERT_METRES_TO_FEET_INT | Math | default | 2 | Returns the result of converting meters to feet |
| `042E` | REGISTER_FASTEST_TIME | Stat | default | 2 | Updates the stat if the value is lower than the current stat value |
| `042F` | REGISTER_HIGHEST_SCORE |  | default | 0 |  |
| `0430` | WARP_CHAR_INTO_CAR_AS_PASSENGER | Char | default | 3 | Puts the character into a vehicle's passenger seat |
| `0431` | IS_CAR_PASSENGER_SEAT_FREE | Car | default | 2 | Returns true if the specified car seat is empty |
| `0432` | GET_CHAR_IN_CAR_PASSENGER_SEAT | Car | default | 3 | Returns the handle of a character sitting in the specified car seat |
| `0433` | SET_CHAR_IS_CHRIS_CRIMINAL | Char | default | 2 | Sets whether the character is a psychotic killer or not |
| `0434` | START_CREDITS | Credits | default | 0 | Makes the credits scroll up the screen |
| `0435` | STOP_CREDITS | Credits | default | 0 | Stops the credits text from showing |
| `0436` | ARE_CREDITS_FINISHED | Credits | default | 0 | Returns true if the credits have finished |
| `0437` | CREATE_SINGLE_PARTICLE |  | default | 0 |  |
| `0438` | SET_CHAR_IGNORE_LEVEL_TRANSITIONS |  | default | 0 |  |
| `0439` | GET_CHASE_CAR |  | default | 0 |  |
| `043A` | START_BOAT_FOAM_ANIMATION |  | default | 0 |  |
| `043B` | UPDATE_BOAT_FOAM_ANIMATION |  | default | 0 |  |
| `043C` | SET_MUSIC_DOES_FADE | Audio | default | 1 | Sets whether sounds should fade along with the screen |
| `043D` | SET_INTRO_IS_PLAYING |  | default | 0 |  |
| `043E` | SET_PLAYER_HOOKER |  | default | 0 | Does nothing |
| `043F` | PLAY_END_OF_GAME_TUNE |  | default | 0 | Plays the theme tune |
| `0440` | STOP_END_OF_GAME_TUNE |  | default | 0 | Stops the theme tune |
| `0441` | GET_CAR_MODEL | Car | default | 2 | Returns the car's model id |
| `0442` | IS_PLAYER_SITTING_IN_CAR |  | default | 0 |  |
| `0443` | IS_PLAYER_SITTING_IN_ANY_CAR |  | default | 0 |  |
| `0444` | SET_SCRIPT_FIRE_AUDIO |  | default | 0 |  |
| `0445` | ARE_ANY_CAR_CHEATS_ACTIVATED | Game | default | 0 | Returns true if the player has used any of the cheats |
| `0446` | SET_CHAR_SUFFERS_CRITICAL_HITS | Char | default | 2 | Sets whether the specified character is immune to headshots |
| `0447` | IS_PLAYER_LIFTING_A_PHONE |  | default | 0 |  |
| `0448` | IS_CHAR_SITTING_IN_CAR | Char | default | 2 | Returns true if the character is sitting in the specified vehicle |
| `0449` | IS_CHAR_SITTING_IN_ANY_CAR | Char | default | 1 | Returns true if the character is sitting in any vehicle |
| `044A` | IS_PLAYER_ON_FOOT |  | default | 0 |  |
| `044B` | IS_CHAR_ON_FOOT | Char | default | 1 | Returns true if the character is on foot, and not occupying a vehicle |
| `044C` | LOAD_COLLISION_WITH_SCREEN |  | default | 0 |  |
| `044D` | LOAD_SPLASH_SCREEN |  | default | 0 | Loads the specified splash screen |
| `044E` | SET_CAR_IGNORE_LEVEL_TRANSITIONS |  | default | 0 |  |
| `044F` | MAKE_CRAIGS_CAR_A_BIT_STRONGER |  | default | 0 |  |
| `0450` | SET_JAMES_CAR_ON_PATH_TO_PLAYER |  | default | 0 |  |
| `0451` | LOAD_END_OF_GAME_TUNE |  | default | 0 | Loads the end of game music |
| `0452` | ENABLE_PLAYER_CONTROL_CAMERA |  | default | 0 |  |
| `0453` | SET_OBJECT_ROTATION | Object | default | 4 | Sets the object rotation along X, Y and Z axis |
| `0454` | GET_DEBUG_CAMERA_COORDINATES | Camera | default | 3 | Returns the debug camera position |
| `0455` | GET_DEBUG_CAMERA_FRONT_VECTOR |  | default | 0 |  |
| `0456` | IS_PLAYER_TARGETTING_ANY_CHAR |  | default | 0 |  |
| `0457` | IS_PLAYER_TARGETTING_CHAR | Player | default | 2 | Returns true if the player is aiming at the specified character |
| `0458` | IS_PLAYER_TARGETTING_OBJECT | Player | default | 2 | Returns true if the player is aiming at the specified object |
| `0459` | TERMINATE_ALL_SCRIPTS_WITH_THIS_NAME |  | default | 1 | Ends any script whose name (03A4) matches the given string |
| `045A` | DISPLAY_TEXT_WITH_NUMBER | Text | default | 4 | Draws text with one number |
| `045B` | DISPLAY_TEXT_WITH_2_NUMBERS | Text | default | 5 | Draws text with two numbers |
| `045C` | FAIL_CURRENT_MISSION | Mission | default | 0 | Terminates the active mission by executing its mission cleanup routine |
| `045D` | GET_CLOSEST_OBJECT_OF_TYPE |  | default | 0 | Does nothing |
| `045E` | PLACE_OBJECT_RELATIVE_TO_OBJECT |  | default | 0 |  |
| `045F` | SET_ALL_OCCUPANTS_OF_CAR_LEAVE_CAR |  | default | 0 |  |
| `0460` | SET_INTERPOLATION_PARAMETERS | Camera | default | 2 | Sets how long the camera transition will last |
| `0461` | GET_CLOSEST_CAR_NODE_WITH_HEADING_TOWARDS_POINT |  | default | 0 |  |
| `0462` | GET_CLOSEST_CAR_NODE_WITH_HEADING_AWAY_POINT |  | default | 0 |  |
| `0463` | GET_DEBUG_CAMERA_POINT_AT | Camera | default | 3 | Stores the location the debug camera is pointing to |
| `0464` | ATTACH_CHAR_TO_CAR | Char | default | 8 | Puts character into a turret on the vehicle, allowing them to shoot |
| `0465` | DETACH_CHAR_FROM_CAR | Char | default | 1 | Takes the character out of turret mode (0464) |
| `0466` | SET_CAR_STAY_IN_FAST_LANE | Car | default | 2 |  |
| `0467` | CLEAR_CHAR_LAST_WEAPON_DAMAGE | Char | default | 1 | Clears the character's last weapon damage (see 031D) |
| `0468` | CLEAR_CAR_LAST_WEAPON_DAMAGE | Car | default | 1 | Clears the vehicle's last weapon damage (see 031E) |
| `0469` | GET_RANDOM_COP_IN_AREA |  | default | 0 | Gets a random law enforcement ped of any of the specified types in the 2D area |
| `046A` | GET_RANDOM_COP_IN_ZONE |  | default | 0 |  |
| `046B` | SET_CHAR_OBJ_FLEE_CAR |  | default | 0 |  |
| `046C` | GET_DRIVER_OF_CAR | Car | default | 2 | Returns the car's driver handle |
| `046D` | GET_NUMBER_OF_FOLLOWERS | Char | default | 2 | Returns the number of members which are in a group of the character (01DE) |
| `046E` | GIVE_REMOTE_CONTROLLED_MODEL_TO_PLAYER | Rc | default | 6 | Puts the player in control of a remote-control vehicle |
| `046F` | GET_CURRENT_PLAYER_WEAPON |  | default | 0 |  |
| `0470` | GET_CURRENT_CHAR_WEAPON | Char | default | 2 | Returns the type of weapon that the character is currently holding |
| `0471` | LOCATE_CHAR_ANY_MEANS_OBJECT_2D | Char | default | 5 | Returns true if the character is within the 2D radius of the object |
| `0472` | LOCATE_CHAR_ON_FOOT_OBJECT_2D | Char | default | 5 | Returns true if the character is within the 2D radius of the object on foot |
| `0473` | LOCATE_CHAR_IN_CAR_OBJECT_2D | Char | default | 5 | Returns true if the character is within the 2D radius of the object in a vehicle |
| `0474` | LOCATE_CHAR_ANY_MEANS_OBJECT_3D | Char | default | 6 | Returns true if the character is within the 3D radius of the object |
| `0475` | LOCATE_CHAR_ON_FOOT_OBJECT_3D | Char | default | 6 | Returns true if the character is within the 3D radius of the object on foot |
| `0476` | LOCATE_CHAR_IN_CAR_OBJECT_3D | Char | default | 6 | Returns true if the character is within the 3D radius of the object in a vehicle |
| `0477` | SET_CAR_TEMP_ACTION | Car | default | 3 | Makes the AI driver perform the action in the vehicle for the specified period of time |
| `0478` | SET_CAR_HANDBRAKE_TURN_RIGHT |  | default | 0 |  |
| `0479` | SET_CAR_HANDBRAKE_STOP |  | default | 0 |  |
| `047A` | IS_CHAR_ON_ANY_BIKE | Char | default | 1 | Returns true if the character is riding a bike |
| `047B` | LOCATE_SNIPER_BULLET_2D |  | default | 0 |  |
| `047C` | LOCATE_SNIPER_BULLET_3D |  | default | 0 |  |
| `047D` | GET_NUMBER_OF_SEATS_IN_MODEL |  | default | 0 |  |
| `047E` | IS_PLAYER_ON_ANY_BIKE |  | default | 0 |  |
| `047F` | IS_CHAR_LYING_DOWN |  | default | 0 |  |
| `0480` | CAN_CHAR_SEE_DEAD_CHAR | Char | default | 2 | Returns true if the character sees a dead body of the given type |
| `0481` | SET_ENTER_CAR_RANGE_MULTIPLIER |  | default | 0 |  |
| `0482` | SET_THREAT_REACTION_RANGE_MULTIPLIER |  | default | 0 | Does nothing |
| `0483` | SET_CHAR_CEASE_ATTACK_TIMER |  | default | 0 |  |
| `0484` | GET_REMOTE_CONTROLLED_CAR | Rc | default | 2 | Returns the player's radio-controlled vehicle (alts:00D9,03C0,0811) |
| `0485` | IS_PC_VERSION | Game | default | 0 | Returns true on PC versions of the game |
| `0486` | REPLAY |  | default | 0 |  |
| `0487` | IS_REPLAY_PLAYING |  | default | 0 |  |
| `0488` | IS_MODEL_AVAILABLE | Streaming | default | 1 | Returns true if the specified model exists in the loaded  |
| `0489` | SHUT_CHAR_UP | Char | default | 2 | Sets the character's ability to talk |
| `048A` | SET_ENABLE_RC_DETONATE | Rc | default | 1 | Enables a remote-control vehicle detonation |
| `048B` | SET_CAR_RANDOM_ROUTE_SEED | Car | default | 2 | Sets the car on a specific route |
| `048C` | IS_ANY_PICKUP_AT_COORDS | World | default | 3 | Returns true if the pickup at the specified coordinates is available to be picked up |
| `048D` | GET_FIRST_PICKUP_COORDS |  | default | 0 |  |
| `048E` | GET_NEXT_PICKUP_COORDS |  | default | 0 |  |
| `048F` | REMOVE_ALL_CHAR_WEAPONS | Char | default | 1 | Removes the characters weapons |
| `0490` | HAS_PLAYER_GOT_WEAPON |  | default | 0 |  |
| `0491` | HAS_CHAR_GOT_WEAPON | Char | default | 2 | Returns true if the character has the specified weapon |
| `0492` | IS_PLAYER_FACING_CHAR |  | default | 0 |  |
| `0493` | SET_TANK_DETONATE_CARS |  | default | 0 |  |
| `0494` | GET_POSITION_OF_ANALOGUE_STICKS | Pad | default | 5 | Returns the offset of the specified Left/Right, Up/Down, Look Left/Look Right and Look Up/Look Down keys |
| `0495` | IS_CAR_ON_FIRE | Car | default | 1 | Returns true if the car is burning |
| `0496` | IS_CAR_TYRE_BURST | Car | default | 2 | Returns true if a given tire on the car is deflated |
| `0497` | SET_CAR_DRIVE_STRAIGHT_AHEAD |  | default | 0 |  |
| `0498` | SET_CAR_WAIT |  | default | 0 |  |
| `0499` | IS_PLAYER_STANDING_ON_A_VEHICLE |  | default | 0 |  |
| `049A` | IS_PLAYER_FOOT_DOWN |  | default | 0 |  |
| `049B` | IS_CHAR_FOOT_DOWN |  | default | 0 |  |
| `049C` | INITIALISE_OBJECT_PATH |  | default | 0 |  |
| `049D` | START_OBJECT_ON_PATH |  | default | 0 |  |
| `049E` | SET_OBJECT_PATH_SPEED |  | default | 0 | Does nothing |
| `049F` | SET_OBJECT_PATH_POSITION |  | default | 0 | Does nothing |
| `04A0` | GET_OBJECT_DISTANCE_ALONG_PATH |  | default | 0 |  |
| `04A1` | CLEAR_OBJECT_PATH |  | default | 0 |  |
| `04A2` | HELI_GOTO_COORDS | Heli | default | 6 | Makes the helicopter fly to the specified location, keeping a specific Z height/altitude |
| `04A3` | IS_INT_VAR_EQUAL_TO_CONSTANT |  | default | 2 | Returns true if the value of the global variable is equal to the integer constant |
| `04A4` | IS_INT_LVAR_EQUAL_TO_CONSTANT |  | default | 2 | Returns true if the value of the local variable is equal to the integer constant |
| `04A5` | GET_DEAD_CHAR_PICKUP_COORDS | World | default | 4 | Returns appropriate coordinates for creating a pickup by a dead character |
| `04A6` | CREATE_PROTECTION_PICKUP | Pickup | default | 6 | Creates an asset revenue pickup |
| `04A7` | IS_CHAR_IN_ANY_BOAT | Char | default | 1 | Returns true if the character is driving a boat |
| `04A8` | IS_PLAYER_IN_ANY_BOAT |  | default | 0 |  |
| `04A9` | IS_CHAR_IN_ANY_HELI | Char | default | 1 | Returns true if the character is flying a helicopter |
| `04AA` | IS_PLAYER_IN_ANY_HELI |  | default | 0 |  |
| `04AB` | IS_CHAR_IN_ANY_PLANE | Char | default | 1 | Returns true if the character is in a plane |
| `04AC` | IS_PLAYER_IN_ANY_PLANE |  | default | 0 |  |
| `04AD` | IS_CHAR_IN_WATER | Char | default | 1 | Returns true if the character is in water |
| `04AE` | SET_VAR_INT_TO_CONSTANT |  | default | 2 | Assigns the global variable to the integer constant |
| `04AF` | SET_LVAR_INT_TO_CONSTANT |  | default | 2 | Assigns the local variable to the integer constant |
| `04B0` | IS_INT_VAR_GREATER_THAN_CONSTANT |  | default | 2 | Returns true if the value of the global variable is greater than the integer constant |
| `04B1` | IS_INT_LVAR_GREATER_THAN_CONSTANT |  | default | 2 | Returns true if the value of the local variable is greater than the integer constant |
| `04B2` | IS_CONSTANT_GREATER_THAN_INT_VAR |  | default | 2 | Returns true if the integer constant is greater than the value of the global variable |
| `04B3` | IS_CONSTANT_GREATER_THAN_INT_LVAR |  | default | 2 | Returns true if the integer constant is greater than the value of the local variable |
| `04B4` | IS_INT_VAR_GREATER_OR_EQUAL_TO_CONSTANT |  | default | 2 | Returns true if the value of the global variable is equal to or greater than the integer constant  |
| `04B5` | IS_INT_LVAR_GREATER_OR_EQUAL_TO_CONSTANT |  | default | 2 | Returns true if the value of the local variable is greater than or equal to the integer constant  |
| `04B6` | IS_CONSTANT_GREATER_OR_EQUAL_TO_INT_VAR |  | default | 2 | Returns true if the integer constant is equal to or greater than the value of the global variable |
| `04B7` | IS_CONSTANT_GREATER_OR_EQUAL_TO_INT_LVAR |  | default | 2 | Returns true if the integer constant is equal to or greater than the value of the local variable |
| `04B8` | GET_CHAR_WEAPON_IN_SLOT | Char | default | 5 | Returns the weapon type, ammo and model from the specified slot |
| `04B9` | GET_CLOSEST_STRAIGHT_ROAD | Path | default | 12 | Gets two closest path nodes within the specified distance range |
| `04BA` | SET_CAR_FORWARD_SPEED | Car | default | 2 | Sets the speed of the car |
| `04BB` | SET_AREA_VISIBLE | Streaming | default | 1 | Sets the visibility of an interior area |
| `04BC` | SET_CUTSCENE_ANIM_TO_LOOP |  | default | 0 | Does nothing |
| `04BD` | MARK_CAR_AS_CONVOY_CAR | Car | default | 2 | Marks the car as being part of a convoy, which seems to follow a path set by 0994 |
| `04BE` | RESET_HAVOC_CAUSED_BY_PLAYER |  | default | 0 |  |
| `04BF` | GET_HAVOC_CAUSED_BY_PLAYER |  | default | 0 | Does nothing |
| `04C0` | CREATE_SCRIPT_ROADBLOCK | World | default | 7 | Creates a roadblock in the specified area with the specified type |
| `04C1` | CLEAR_ALL_SCRIPT_ROADBLOCKS | World | default | 0 | Removes references to all created roadblocks (04C0), freeing game memory |
| `04C2` | SET_CHAR_OBJ_WALK_TO_CHAR |  | default | 0 |  |
| `04C3` | IS_PICKUP_IN_ZONE |  | default | 0 |  |
| `04C4` | GET_OFFSET_FROM_CHAR_IN_WORLD_COORDS | Char | default | 7 | Returns the coordinates of the character, with an offset |
| `04C5` | HAS_CHAR_BEEN_PHOTOGRAPHED | Char | default | 1 | Returns true if the character has been photographed |
| `04C6` | SET_CHAR_OBJ_AIM_GUN_AT_CHAR |  | default | 0 |  |
| `04C7` | SWITCH_SECURITY_CAMERA |  | default | 0 |  |
| `04C8` | IS_CHAR_IN_FLYING_VEHICLE | Char | default | 1 | Returns true if the character is in a flying vehicle |
| `04C9` | IS_PLAYER_IN_FLYING_VEHICLE |  | default | 0 |  |
| `04CA` | HAS_SONY_CD_BEEN_READ |  | default | 0 |  |
| `04CB` | GET_NUMBER_OF_SONY_CDS_READ |  | default | 0 |  |
| `04CC` | ADD_SHORT_RANGE_BLIP_FOR_COORD_OLD |  | default | 0 |  |
| `04CD` | ADD_SHORT_RANGE_BLIP_FOR_COORD |  | default | 0 |  |
| `04CE` | ADD_SHORT_RANGE_SPRITE_BLIP_FOR_COORD | Blip | default | 5 | Adds a sprite blip for the specified coordinates |
| `04CF` | ADD_MONEY_SPENT_ON_CLOTHES |  | default | 0 |  |
| `04D0` | SET_HELI_ORIENTATION | Heli | default | 2 | Forces the heli rotation relative to the north |
| `04D1` | CLEAR_HELI_ORIENTATION | Heli | default | 1 | Resets the heli rotation set with 04D0 |
| `04D2` | PLANE_GOTO_COORDS | Plane | default | 6 |  |
| `04D3` | GET_NTH_CLOSEST_CAR_NODE | Path | default | 7 | Gets the coordinates of the nth car path node closest to the given coordinates |
| `04D4` | GET_NTH_CLOSEST_CHAR_NODE |  | default | 0 |  |
| `04D5` | DRAW_WEAPONSHOP_CORONA | Fx | default | 9 | Displays a corona with the lowered draw distance at the specified coordinates |
| `04D6` | SET_ENABLE_RC_DETONATE_ON_CONTACT | Rc | default | 1 | Sets whether RC Bandits detonate on contact with the wheels of any four-wheeled vehicles |
| `04D7` | FREEZE_CHAR_POSITION | Char | default | 2 | Sets whether the character's position remains unchanged |
| `04D8` | SET_CHAR_DROWNS_IN_WATER | Char | default | 2 | Controls whether the character can drown in water |
| `04D9` | SET_OBJECT_RECORDS_COLLISIONS | Object | default | 2 | Enables the use of collision checking for the object |
| `04DA` | HAS_OBJECT_COLLIDED_WITH_ANYTHING | Object | default | 1 | Returns true if the object has collided |
| `04DB` | REMOVE_RC_BUGGY | Rc | default | 0 | Exits remote-control mode |
| `04DC` | HAS_PHOTOGRAPH_BEEN_TAKEN |  | default | 0 |  |
| `04DD` | GET_CHAR_ARMOUR | Char | default | 2 | Returns the character's armor amount |
| `04DE` | SET_CHAR_ARMOUR |  | default | 0 |  |
| `04DF` | SET_HELI_STABILISER | Heli | default | 2 | Limits the amount a helicopter can tilt |
| `04E0` | SET_CAR_STRAIGHT_LINE_DISTANCE | Car | default | 2 | Sets the minimum distance for the AI driver to start ignoring car paths and go straight to the target |
| `04E1` | POP_CAR_BOOT | Car | default | 1 | Opens the car's trunk and keeps it open |
| `04E2` | SHUT_PLAYER_UP |  | default | 2 | Shuts the player up |
| `04E3` | SET_PLAYER_MOOD | Player | default | 3 | Sets the players mood, affecting the dialogue spoken by the player |
| `04E4` | REQUEST_COLLISION | Streaming | default | 2 | Reloads the area at the specified coordinates |
| `04E5` | LOCATE_OBJECT_2D | Object | default | 6 | Returns true if the object is near the specified coordinates |
| `04E6` | LOCATE_OBJECT_3D | Object | default | 8 | Returns true if the object is near the specified point |
| `04E7` | IS_OBJECT_IN_WATER | Object | default | 1 | Returns true if the object is in water |
| `04E8` | SET_CHAR_OBJ_STEAL_ANY_CAR_EVEN_MISSION_CAR |  | default | 0 |  |
| `04E9` | IS_OBJECT_IN_AREA_2D | Object | default | 6 | Returns true if object is in the specified area |
| `04EA` | IS_OBJECT_IN_AREA_3D | Object | default | 8 | Returns true if the object is in the specified area |
| `04EB` | TASK_TOGGLE_DUCK | Task | default | 2 | Makes the character crouch |
| `04EC` | SET_ZONE_CIVILIAN_CAR_INFO |  | default | 0 |  |
| `04ED` | REQUEST_ANIMATION | Streaming | default | 1 | Loads the specified IFP File |
| `04EE` | HAS_ANIMATION_LOADED | Streaming | default | 1 | Returns true if the specified IFP file is loaded |
| `04EF` | REMOVE_ANIMATION | Streaming | default | 1 | Releases the specified IFP file, freeing game memory |
| `04F0` | IS_CHAR_WAITING_FOR_WORLD_COLLISION | Char | default | 1 |  |
| `04F1` | IS_CAR_WAITING_FOR_WORLD_COLLISION | Car | default | 1 |  |
| `04F2` | IS_OBJECT_WAITING_FOR_WORLD_COLLISION |  | default | 0 |  |
| `04F3` | SET_CHAR_SHUFFLE_INTO_DRIVERS_SEAT |  | default | 0 |  |
| `04F4` | ATTACH_CHAR_TO_OBJECT | Char | default | 8 | Attaches the character to the specified object, in turret mode |
| `04F5` | SET_CHAR_AS_PLAYER_FRIEND |  | default | 0 |  |
| `04F6` | DISPLAY_NTH_ONSCREEN_COUNTER |  | default | 0 |  |
| `04F7` | DISPLAY_NTH_ONSCREEN_COUNTER_WITH_STRING | Hud | default | 4 | Displays an onscreen counter with the text in the specified slot, either shown in numbers or as a bar |
| `04F8` | ADD_SET_PIECE | World | default | 13 | Creates a trigger zone for police to appear during chases |
| `04F9` | SET_EXTRA_COLOURS | World | default | 2 | Sets the extra color of the sky |
| `04FA` | CLEAR_EXTRA_COLOURS | World | default | 1 | Clears the extra color of the sky |
| `04FB` | CLOSE_CAR_BOOT |  | default | 0 |  |
| `04FC` | GET_WHEELIE_STATS | Player | default | 7 | Returns the stats of the most recent wheelie or stoppie attempt |
| `04FD` | DISARM_CHAR |  | default | 0 |  |
| `04FE` | BURST_CAR_TYRE | Car | default | 2 | Deflates the car's tire |
| `04FF` | IS_CHAR_OBJ_NO_OBJ |  | default | 0 |  |
| `0500` | IS_PLAYER_WEARING | Player | default | 3 | Returns true if the player's bodypart has the specified model (0784 or 087B)  |
| `0501` | SET_PLAYER_CAN_DO_DRIVE_BY | Player | default | 2 | Sets the players driveby mode |
| `0502` | SET_CHAR_OBJ_SPRINT_TO_COORD |  | default | 0 |  |
| `0503` | CREATE_SWAT_ROPE | Char | default | 6 | Creates a character descending from a rope |
| `0504` | SET_FIRST_PERSON_CONTROL_CAMERA |  | default | 0 |  |
| `0505` | GET_NEAREST_TYRE_TO_POINT |  | default | 0 |  |
| `0506` | SET_CAR_MODEL_COMPONENTS | Car | default | 3 | Sets the variation of the next car to be created |
| `0507` | SWITCH_LIFT_CAMERA |  | default | 0 | Applies a camera overlay |
| `0508` | CLOSE_ALL_CAR_DOORS | Car | default | 1 | Closes all car doors, hoods and boots |
| `0509` | GET_DISTANCE_BETWEEN_COORDS_2D | Math | default | 5 | Gets the distance between two points |
| `050A` | GET_DISTANCE_BETWEEN_COORDS_3D | Math | default | 7 | Gets the distance between two points |
| `050B` | POP_CAR_BOOT_USING_PHYSICS |  | default | 0 | Opens the trunk/boot door component of the vehicle |
| `050C` | SET_FIRST_PERSON_WEAPON_CAMERA |  | default | 0 |  |
| `050D` | IS_CHAR_LEAVING_VEHICLE_TO_DIE |  | default | 0 |  |
| `050E` | SORT_OUT_OBJECT_COLLISION_WITH_CAR | Object | default | 2 | Makes the specified car have no collision with the specified object |
| `050F` | GET_MAX_WANTED_LEVEL | Game | default | 1 | Gets the maximum wanted level the player can receive |
| `0510` | IS_CHAR_WANDER_PATH_CLEAR |  | default | 0 |  |
| `0511` | PRINT_HELP_WITH_NUMBER |  | default | 0 |  |
| `0512` | PRINT_HELP_FOREVER | Text | default | 1 | Shows a text box which stays on screen until it is removed by another command |
| `0513` | PRINT_HELP_FOREVER_WITH_NUMBER | Text | default | 2 | Shows a text box with one number |
| `0514` | SET_CHAR_CAN_BE_DAMAGED_BY_MEMBERS_OF_GANG |  | default | 0 |  |
| `0515` | LOAD_AND_LAUNCH_MISSION_EXCLUSIVE |  | default | 0 | Does nothing |
| `0516` | IS_MISSION_AUDIO_PLAYING |  | default | 0 |  |
| `0517` | CREATE_LOCKED_PROPERTY_PICKUP | Pickup | default | 5 | Creates an asset icon for an asset that is not for sale |
| `0518` | CREATE_FORSALE_PROPERTY_PICKUP | Pickup | default | 6 | Creates an asset pickup for an asset which can be bought |
| `0519` | FREEZE_CAR_POSITION | Car | default | 2 | Locks the vehicle's position |
| `051A` | HAS_CHAR_BEEN_DAMAGED_BY_CHAR | Char | default | 2 | Returns true if the character has been hurt by the other character |
| `051B` | HAS_CHAR_BEEN_DAMAGED_BY_CAR | Char | default | 2 | Returns true if the char has been hurt by the specified vehicle |
| `051C` | HAS_CAR_BEEN_DAMAGED_BY_CHAR | Car | default | 2 | Returns true if the car has been damaged by the specified char |
| `051D` | HAS_CAR_BEEN_DAMAGED_BY_CAR | Car | default | 2 | Returns true if the vehicle has been damaged by another specified vehicle |
| `051E` | GET_RADIO_CHANNEL | Audio | default | 1 | Returns the current radio station that is being played |
| `051F` | DISPLAY_TEXT_WITH_3_NUMBERS |  | default | 0 |  |
| `0520` | IS_CAR_DROWNING_IN_WATER |  | default | 0 |  |
| `0521` | IS_CHAR_DROWNING_IN_WATER |  | default | 0 |  |
| `0522` | DISABLE_CUTSCENE_SHADOWS |  | default | 0 | Does nothing |
| `0523` | HAS_GLASS_BEEN_SHATTERED_NEARBY |  | default | 0 |  |
| `0524` | ATTACH_CUTSCENE_OBJECT_TO_BONE |  | default | 0 | Does nothing |
| `0525` | ATTACH_CUTSCENE_OBJECT_TO_COMPONENT |  | default | 0 |  |
| `0526` | SET_CHAR_STAY_IN_CAR_WHEN_JACKED | Char | default | 2 | Makes the character stay in the vehicle when it is jacked (characters let themselves get "kidnapped") |
| `0527` | IS_MISSION_AUDIO_LOADING |  | default | 0 |  |
| `0528` | ADD_MONEY_SPENT_ON_WEAPONS |  | default | 0 |  |
| `0529` | ADD_MONEY_SPENT_ON_PROPERTY |  | default | 0 |  |
| `052A` | ADD_MONEY_SPENT_ON_AUTO_PAINTING |  | default | 0 |  |
| `052B` | SET_CHAR_ANSWERING_MOBILE |  | default | 0 |  |
| `052C` | SET_PLAYER_DRUNKENNESS | Player | default | 2 | Makes the camera start moving around in a swirling motion with the specified intensity as if drunk |
| `052D` | GET_PLAYER_DRUNKENNESS |  | default | 0 |  |
| `052E` | SET_PLAYER_DRUG_LEVEL |  | default | 0 |  |
| `052F` | GET_PLAYER_DRUG_LEVEL |  | default | 0 |  |
| `0530` | ADD_LOAN_SHARK_VISITS |  | default | 0 |  |
| `0531` | ADD_STORES_KNOCKED_OFF |  | default | 0 |  |
| `0532` | ADD_MOVIE_STUNTS |  | default | 0 |  |
| `0533` | ADD_NUMBER_OF_ASSASSINATIONS |  | default | 0 |  |
| `0534` | ADD_PIZZAS_DELIVERED |  | default | 0 |  |
| `0535` | ADD_GARBAGE_PICKUPS |  | default | 0 |  |
| `0536` | ADD_ICE_CREAMS_SOLD |  | default | 0 |  |
| `0537` | SET_TOP_SHOOTING_RANGE_SCORE |  | default | 0 |  |
| `0538` | ADD_SHOOTING_RANGE_RANK |  | default | 0 |  |
| `0539` | ADD_MONEY_SPENT_ON_GAMBLING |  | default | 0 |  |
| `053A` | ADD_MONEY_WON_ON_GAMBLING |  | default | 0 |  |
| `053B` | SET_LARGEST_GAMBLING_WIN |  | default | 0 |  |
| `053C` | SET_CHAR_IN_PLAYERS_GROUP_CAN_FIGHT |  | default | 0 |  |
| `053D` | CLEAR_CHAR_WAIT_STATE |  | default | 0 |  |
| `053E` | GET_RANDOM_CAR_OF_TYPE_IN_AREA_NO_SAVE | World | default | 6 | Loops through the pool of vehicles to retrieve one that matches the specified model in the specified 2D area |
| `053F` | SET_CAN_BURST_CAR_TYRES | Car | default | 2 | Sets whether the car's tires can be deflated |
| `0540` | SET_PLAYER_AUTO_AIM |  | default | 0 |  |
| `0541` | FIRE_HUNTER_GUN | Heli | default | 1 | Makes the Hunter helicopter fire cannon gun |
| `0542` | SET_PROPERTY_AS_OWNED |  | default | 0 |  |
| `0543` | ADD_BLOOD_RING_KILLS |  | default | 0 |  |
| `0544` | SET_LONGEST_TIME_IN_BLOOD_RING |  | default | 0 |  |
| `0545` | REMOVE_EVERYTHING_FOR_HUGE_CUTSCENE |  | default | 0 | Does nothing |
| `0546` | IS_PLAYER_TOUCHING_VEHICLE |  | default | 0 |  |
| `0547` | IS_CHAR_TOUCHING_VEHICLE | Char | default | 2 | Returns true if the character is colliding with a car |
| `0548` | CHECK_FOR_PED_MODEL_AROUND_PLAYER |  | default | 0 | Does nothing |
| `0549` | CLEAR_CHAR_FOLLOW_PATH |  | default | 0 |  |
| `054A` | SET_CHAR_CAN_BE_SHOT_IN_VEHICLE | Char | default | 2 | Makes the character immune to a damage while in a vehicle |
| `054B` | ATTACH_CUTSCENE_OBJECT_TO_VEHICLE |  | default | 0 | Does nothing |
| `054C` | LOAD_MISSION_TEXT | Text | default | 1 | Makes the game use GXT Entries from the specified GXT Table |
| `054D` | SET_TONIGHTS_EVENT |  | default | 0 | Sets whether to display a message at the stadium |
| `054E` | CLEAR_CHAR_LAST_DAMAGE_ENTITY | Char | default | 1 |  |
| `054F` | CLEAR_CAR_LAST_DAMAGE_ENTITY | Car | default | 1 | Clears the car's last damage entity |
| `0550` | FREEZE_OBJECT_POSITION | Object | default | 2 | Sets whether the object's position remains unchanged |
| `0551` | SET_PLAYER_HAS_MET_DEBBIE_HARRY |  | default | 0 |  |
| `0552` | SET_RIOT_INTENSITY |  | default | 0 |  |
| `0553` | IS_CAR_IN_ANGLED_AREA_2D |  | default | 0 |  |
| `0554` | IS_CAR_IN_ANGLED_AREA_3D |  | default | 0 |  |
| `0555` | REMOVE_WEAPON_FROM_CHAR | Char | default | 2 | Removes the weapon from the character |
| `0556` | SET_UP_TAXI_SHORTCUT |  | default | 0 |  |
| `0557` | CLEAR_TAXI_SHORTCUT |  | default | 0 |  |
| `0558` | SET_CHAR_OBJ_GOTO_CAR_ON_FOOT |  | default | 0 |  |
| `0559` | GET_CLOSEST_WATER_NODE |  | default | 0 |  |
| `055A` | ADD_PORN_LEAFLET_TO_RUBBISH |  | default | 0 |  |
| `055B` | CREATE_CLOTHES_PICKUP |  | default | 0 | Does nothing |
| `055C` | CHANGE_BLIP_THRESHOLD |  | default | 0 |  |
| `055D` | MAKE_PLAYER_FIRE_PROOF | Player | default | 2 | Makes the player immune to fire |
| `055E` | INCREASE_PLAYER_MAX_HEALTH | Player | default | 2 | Increases the player's max health by the specified value and changes current health to the new maximum |
| `055F` | INCREASE_PLAYER_MAX_ARMOUR | Player | default | 2 | Increases the player's max armor by the specified value and changes current armor to the new maximum |
| `0560` | CREATE_RANDOM_CHAR_AS_DRIVER | Char | default | 2 | Creates a driver in the vehicle |
| `0561` | CREATE_RANDOM_CHAR_AS_PASSENGER | Char | default | 3 | Creates a random character in the passenger seat of the vehicle |
| `0562` | SET_CHAR_IGNORE_THREATS_BEHIND_OBJECTS |  | default | 0 |  |
| `0563` | ENSURE_PLAYER_HAS_DRIVE_BY_WEAPON | Player | default | 2 | Sets the amount of ammo a player has during a driveby |
| `0564` | MAKE_HELI_COME_CRASHING_DOWN | Heli | default | 1 | Makes helicopter simulate crash landing, exploding on the way if high up |
| `0565` | ADD_EXPLOSION_NO_SOUND | Fx | default | 4 | Creates an explosion with no sound |
| `0566` | SET_OBJECT_AREA_VISIBLE | Object | default | 2 | Sets the visibility of the object to the specified interior |
| `0567` | WAS_VEHICLE_EVER_POLICE |  | default | 0 |  |
| `0568` | SET_CHAR_NEVER_TARGETTED | Char | default | 2 | Sets whether the character won't be targeted by the autoaim system |
| `0569` | LOAD_UNCOMPRESSED_ANIM |  | default | 0 | Does nothing |
| `056A` | WAS_CUTSCENE_SKIPPED | Cutscene | default | 0 | Returns true if the cutscene was skipped |
| `056B` | SET_CHAR_CROUCH_WHEN_THREATENED |  | default | 0 |  |
| `056C` | IS_CHAR_IN_ANY_POLICE_VEHICLE | Char | default | 1 | Returns true if the character is driving a police vehicle |
| `056D` | DOES_CHAR_EXIST | Char | default | 1 | Returns true if the handle is a valid character handle |
| `056E` | DOES_VEHICLE_EXIST | Car | default | 1 | Returns true if the handle is a valid vehicle handle |
| `056F` | ADD_SHORT_RANGE_BLIP_FOR_CONTACT_POINT |  | default | 0 |  |
| `0570` | ADD_SHORT_RANGE_SPRITE_BLIP_FOR_CONTACT_POINT | Blip | default | 5 | Adds a short range sprite blip and sphere to the contact point that is not displayed while on mission |
| `0571` | IS_CHAR_STUCK |  | default | 0 |  |
| `0572` | SET_ALL_TAXIS_HAVE_NITRO | Game | default | 1 | Toggles whether all taxis have nitrous |
| `0573` | SET_CHAR_STOP_SHOOT_DONT_SEEK_ENTITY |  | default | 0 |  |
| `0574` | FREEZE_CAR_POSITION_AND_DONT_LOAD_COLLISION | Car | default | 2 | Makes the car maintain its position |
| `0575` | FREEZE_CHAR_POSITION_AND_DONT_LOAD_COLLISION | Char | default | 2 |  |
| `0576` | FREEZE_OBJECT_POSITION_AND_DONT_LOAD_COLLISION |  | default | 0 |  |
| `0577` | SET_FADE_AND_JUMPCUT_AFTER_RC_EXPLOSION |  | default | 0 |  |
| `0578` | REGISTER_VIGILANTE_LEVEL |  | default | 0 |  |
| `0579` | CLEAR_ALL_CHAR_ANIMS |  | default | 0 |  |
| `057A` | SET_MAXIMUM_NUMBER_OF_CARS_IN_GARAGE |  | default | 0 |  |
| `057B` | WANTED_STARS_ARE_FLASHING |  | default | 0 | Does nothing |
| `057C` | SET_ALLOW_HURRICANES |  | default | 0 |  |
| `057D` | PLAY_ANNOUNCEMENT |  | default | 0 | Plays an announcement audio |
| `057E` | SET_PLAYER_IS_IN_STADIUM | Game | default | 1 | Greys out the radar |
| `057F` | GET_BUS_FARES_COLLECTED_BY_PLAYER |  | default | 0 | Returns the number of coach passengers |
| `0580` | SET_CHAR_OBJ_BUY_ICE_CREAM |  | default | 0 |  |
| `0581` | DISPLAY_RADAR | Hud | default | 1 | Displays or hides the radar |
| `0582` | REGISTER_BEST_POSITION | Stat | default | 2 | Updates the race best position |
| `0583` | IS_PLAYER_IN_INFO_ZONE | Player | default | 2 | Returns true if the player is in the specified zone |
| `0584` | CLEAR_CHAR_ICE_CREAM_PURCHASE |  | default | 0 |  |
| `0585` | IS_IN_CAR_FIRE_BUTTON_PRESSED |  | default | 0 | Returns true if the attack button is being pressed |
| `0586` | HAS_CHAR_ATTEMPTED_ATTRACTOR |  | default | 0 |  |
| `0587` | SET_LOAD_COLLISION_FOR_CAR_FLAG | Car | default | 2 |  |
| `0588` | SET_LOAD_COLLISION_FOR_CHAR_FLAG | Char | default | 2 |  |
| `0589` | SET_LOAD_COLLISION_FOR_OBJECT_FLAG |  | default | 0 |  |
| `058A` | ADD_BIG_GUN_FLASH | Fx | default | 6 | Creates a gun flash particle effect |
| `058B` | HAS_CHAR_BOUGHT_ICE_CREAM |  | default | 0 |  |
| `058C` | GET_PROGRESS_PERCENTAGE | Stat | default | 1 | Gets the progress of completion as a percentage |
| `058D` | SET_SHORTCUT_PICKUP_POINT |  | default | 0 | Does nothing |
| `058E` | SET_SHORTCUT_DROPOFF_POINT_FOR_MISSION |  | default | 0 |  |
| `058F` | GET_RANDOM_ICE_CREAM_CUSTOMER_IN_AREA |  | default | 0 |  |
| `0590` | GET_RANDOM_ICE_CREAM_CUSTOMER_IN_ZONE |  | default | 0 |  |
| `0591` | UNLOCK_ALL_CAR_DOORS_IN_AREA |  | default | 0 |  |
| `0592` | SET_GANG_ATTACK_PLAYER_WITH_COPS |  | default | 0 |  |
| `0593` | SET_CHAR_FRIGHTENED_IN_JACKED_CAR |  | default | 0 |  |
| `0594` | SET_VEHICLE_TO_FADE_IN | Car | default | 2 | Sets the alpha transparency of a distant vehicle |
| `0595` | REGISTER_ODDJOB_MISSION_PASSED | Stat | default | 0 | Sets the latest odd job mission passed |
| `0596` | IS_PLAYER_IN_SHORTCUT_TAXI |  | default | 1 |  |
| `0597` | IS_CHAR_DUCKING | Char | default | 1 | Returns true if the specified character is crouching |
| `0598` | CREATE_DUST_EFFECT_FOR_CUTSCENE_HELI |  | default | 0 |  |
| `0599` | REGISTER_FIRE_LEVEL |  | default | 0 |  |
| `059A` | IS_AUSTRALIAN_GAME | Game | default | 0 | Returns true if the current game is an Australian release |
| `059B` | DISARM_CAR_BOMB |  | default | 0 | Does nothing |
| `059C` | SET_ONSCREEN_COUNTER_FLASH_WHEN_FIRST_DISPLAYED | Hud | default | 2 |  |
| `059D` | SHUFFLE_CARD_DECKS | CardDecks | default | 1 |  |
| `059E` | FETCH_NEXT_CARD | CardDecks | default | 1 | Returns a random number between 1 and 52, inclusive |
| `059F` | GET_OBJECT_VELOCITY | Object | default | 4 | Returns the object's X, Y, and Z velocity |
| `05A0` | IS_DEBUG_CAMERA_ON | Debugger | default | 0 |  |
| `05A1` | ADD_TO_OBJECT_ROTATION_VELOCITY | Object | default | 4 | Sets the object's rotation velocity from the center of its body |
| `05A2` | SET_OBJECT_ROTATION_VELOCITY | Object | default | 4 | Sets the object's rotation velocity with frame sync applied? |
| `05A3` | IS_OBJECT_STATIC | Object | default | 1 | Returns true if the object is not moving |
| `05A4` | GET_ANGLE_BETWEEN_2D_VECTORS | Math | default | 5 | Gets the angle between the two 2D vectors |
| `05A5` | DO_2D_RECTANGLES_COLLIDE | Math | default | 8 | Returns true if rectangle1 is inside rectangle2 or partially intersects it |
| `05A6` | GET_OBJECT_ROTATION_VELOCITY | Object | default | 4 |  |
| `05A7` | ADD_VELOCITY_RELATIVE_TO_OBJECT_VELOCITY | Object | default | 4 | Sets the object's velocity |
| `05A8` | GET_OBJECT_SPEED | Object | default | 2 | Gets the speed of the object |
| `05A9` | SET_VAR_TEXT_LABEL |  | default | 2 | Copies up to 8 characters from src to dest |
| `05AA` | SET_LVAR_TEXT_LABEL |  | default | 2 | Copies up to 8 characters from src to dest |
| `05AB` | VAR_TEXT_LABEL |  | default | 0 |  |
| `05AC` | LVAR_TEXT_LABEL |  | default | 0 |  |
| `05AD` | IS_VAR_TEXT_LABEL_EQUAL_TO_TEXT_LABEL |  | default | 2 | Returns true if the two null-terminated strings are equivalent |
| `05AE` | IS_LVAR_TEXT_LABEL_EQUAL_TO_TEXT_LABEL |  | default | 2 | Returns true if the two null-terminated strings are equivalent |
| `05AF` | DO_2D_LINES_INTERSECT |  | default | 0 |  |
| `05B0` | GET_2D_LINES_INTERSECT_POINT | Math | default | 10 | Returns the point of intersection of two lines. If they do not intersect, both returned values are -1000000.0 and the condition result is false |
| `05B1` | IS_2D_POINT_IN_TRIANGLE |  | default | 0 | Does nothing |
| `05B2` | IS_2D_POINT_IN_RECTANGLE_ON_LEFT_SIDE_OF_LINE |  | default | 0 | Does nothing |
| `05B3` | IS_2D_POINT_ON_LEFT_SIDE_OF_2D_LINE |  | default | 0 | Does nothing |
| `05B4` | CHAR_LOOK_AT_OBJECT_ALWAYS |  | default | 0 |  |
| `05B5` | APPLY_COLLISION_ON_OBJECT |  | default | 0 | Does nothing |
| `05B6` | SAVE_STRING_TO_DEBUG_FILE | Debugger | default | 1 | Makes the current script skip the next 128 bytes of the code |
| `05B7` | TASK_PLAYER_ON_FOOT |  | default | 0 | Does nothing |
| `05B8` | TASK_PLAYER_IN_CAR |  | default | 0 | Does nothing |
| `05B9` | TASK_PAUSE | Task | default | 2 | Makes the character pause for the specified amount of time |
| `05BA` | TASK_STAND_STILL | Task | default | 2 | Makes the character stand still |
| `05BB` | TASK_FALL_AND_GET_UP | Task | default | 3 | Makes char fall to the ground and stay there for the specified time |
| `05BC` | TASK_JUMP | Task | default | 2 | Makes the char perform a jump |
| `05BD` | TASK_TIRED | Task | default | 2 | Makes the char stop to regain breath |
| `05BE` | TASK_DIE | Task | default | 1 | Kills the character |
| `05BF` | TASK_LOOK_AT_CHAR | Task | default | 3 | Makes the character look at another character |
| `05C0` | TASK_LOOK_AT_VEHICLE | Task | default | 3 | Makes the char look at the specified vehicle |
| `05C1` | TASK_SAY | Task | default | 2 | Makes the character say a phrase from the specified audio table |
| `05C2` | TASK_SHAKE_FIST | Task | default | 1 | Makes the char lift their hand up in the air angrily |
| `05C3` | TASK_COWER | Task | default | 1 | Makes the char stumble backwards with their arms in front of their face as if he is backing away from something in fear |
| `05C4` | TASK_HANDS_UP | Task | default | 2 | Makes the char put their hands in the air |
| `05C5` | TASK_DUCK | Task | default | 2 | Makes a character duck with their arms over head |
| `05C6` | TASK_DETONATE |  | default | 0 |  |
| `05C7` | TASK_USE_ATM | Task | default | 1 | Makes a character use an ATM machine |
| `05C8` | TASK_SCRATCH_HEAD | Task | default | 1 | Makes a character scratch their head while looking around |
| `05C9` | TASK_LOOK_ABOUT | Task | default | 2 | Makes a character look out ahead |
| `05CA` | TASK_ENTER_CAR_AS_PASSENGER | Task | default | 4 | Makes a character approach the car and occupy the specified passenger seat |
| `05CB` | TASK_ENTER_CAR_AS_DRIVER | Task | default | 3 | Makes a character approach the car and occupy the driver seat |
| `05CC` | TASK_STEAL_CAR |  | default | 0 |  |
| `05CD` | TASK_LEAVE_CAR | Task | default | 2 | Makes the character exit the specified vehicle, if they are currently in it |
| `05CE` | TASK_LEAVE_CAR_AND_DIE |  | default | 0 | Does nothing |
| `05CF` | TASK_LEAVE_CAR_AND_FLEE | Task | default | 5 | Makes the character exit the vehicle and flee to the specified position |
| `05D0` | TASK_CAR_DRIVE |  | default | 0 | Does nothing |
| `05D1` | TASK_CAR_DRIVE_TO_COORD | Task | default | 9 |  |
| `05D2` | TASK_CAR_DRIVE_WANDER | Task | default | 4 | Makes the character drive around aimlessly in a vehicle |
| `05D3` | TASK_GO_STRAIGHT_TO_COORD | Task | default | 6 | Makes the character walk to the specified coordinates |
| `05D4` | TASK_ACHIEVE_HEADING | Task | default | 2 | Rotates a character to the specified angle |
| `05D5` | SET_CHAR_IN_DISGUISE |  | default | 0 |  |
| `05D6` | FLUSH_ROUTE | Path | default | 0 | Flushes the task route |
| `05D7` | EXTEND_ROUTE | Path | default | 3 | Adds a point to the task route |
| `05D8` | TASK_FOLLOW_POINT_ROUTE | Task | default | 3 | Makes the character follow the path route |
| `05D9` | TASK_GOTO_CHAR | Task | default | 4 | Approaches the character from any direction within the specified radius |
| `05DA` | TASK_FLEE_POINT | Task | default | 6 | Makes the character run away from a point, scared and often screaming |
| `05DB` | TASK_FLEE_CHAR | Task | default | 4 | Makes the character run away from another character |
| `05DC` | TASK_SMART_FLEE_POINT | Task | default | 6 | Makes the character run away from the specified coordinates |
| `05DD` | TASK_SMART_FLEE_CHAR | Task | default | 4 | Makes the character flee from another character |
| `05DE` | TASK_WANDER_STANDARD | Task | default | 1 | Makes the character walk around the ped path |
| `05DF` | TASK_WANDER_COP |  | default | 0 |  |
| `05E0` | TASK_WANDER_CRIMINAL |  | default | 0 | Reads the game memory and stores the result to a variable |
| `05E1` | TASK_FOLLOW_LEADER_IN_FORMATION |  | default | 0 |  |
| `05E2` | TASK_KILL_CHAR_ON_FOOT | Task | default | 2 | Makes a character attack another character on foot |
| `05E3` | START_ADDING_STUNT_POINTS |  | default | 0 |  |
| `05E4` | ADD_STUNT_POINT |  | default | 0 |  |
| `05E5` | START_PLAYING_STUNT |  | default | 0 | Gets the ID version of the game |
| `05E6` | HAS_STUNT_ENDED |  | default | 0 | Gets a pointer to the structure of the char on the handle |
| `05E7` | HAS_STUNT_FAILED |  | default | 0 | Gets a pointer to the structure of the vehicle on the handle |
| `05E8` | START_RECORDING_STUNT |  | default | 0 | Gets a pointer to the structure of the object on the handle |
| `05E9` | START_RECORDING_CAR |  | default | 2 | Gets the handle to the char, which is located in the pool of actors |
| `05EA` | STOP_RECORDING_CARS |  | default | 0 | Gets the handle of a vehicle located in a pool of vehicle |
| `05EB` | START_PLAYBACK_RECORDED_CAR | Car | default | 2 | Assigns a car to a path |
| `05EC` | STOP_PLAYBACK_RECORDED_CAR | Car | default | 1 | Stops car from following path |
| `05ED` | PAUSE_PLAYBACK_RECORDED_CAR | Car | default | 1 | Freezes the car on its path |
| `05EE` | UNPAUSE_PLAYBACK_RECORDED_CAR | Car | default | 1 | Unfreezes the vehicle on its path |
| `05EF` | SET_CAR_PROTECT_CAR_REAR |  | default | 0 | Performs a search for an char, which is located in a specified radius around the point |
| `05F0` | SET_CAR_PROTECT_CAR_FRONT |  | default | 0 | Performs a search for a vehicle, located in a specified radius around the point |
| `05F1` | SET_CAR_ESCORT_CAR_LEFT | Car | default | 2 | Makes the vehicle stay on the other vehicle's left side, keeping parallel |
| `05F2` | SET_CAR_ESCORT_CAR_RIGHT | Car | default | 2 | Makes the vehicle stay by the right side of the other vehicle, keeping parallel |
| `05F3` | SET_CAR_ESCORT_CAR_REAR | Car | default | 2 | Makes the vehicle stay behind the other car, keeping parallel |
| `05F4` | SET_CAR_ESCORT_CAR_FRONT | Car | default | 2 | Makes the vehicle stay in front of the other, keeping parallel |
| `05F5` | TASK_FOLLOW_PATH_NODES_TO_COORD | Task | default | 6 | Makes the character go to the specified coordinates |
| `05F6` | IS_CHAR_IN_ANGLED_AREA_2D | Char | default | 7 | Checks if the character is within the angled 2D area |
| `05F7` | IS_CHAR_IN_ANGLED_AREA_ON_FOOT_2D | Char | default | 7 | Checks if the character is within the angled 2D area |
| `05F8` | IS_CHAR_IN_ANGLED_AREA_IN_CAR_2D | Char | default | 7 | Checks if the character is in a car which is within the angled 2D area |
| `05F9` | IS_CHAR_STOPPED_IN_ANGLED_AREA_2D | Char | default | 7 | Checks if the character is within the angled 2D area and is motionless |
| `05FA` | IS_CHAR_STOPPED_IN_ANGLED_AREA_ON_FOOT_2D | Char | default | 7 | Checks if the character is within the angled 2D area |
| `05FB` | IS_CHAR_STOPPED_IN_ANGLED_AREA_IN_CAR_2D | Char | default | 7 | Checks if the character is in a motionless car within the angled 2D area |
| `05FC` | IS_CHAR_IN_ANGLED_AREA_3D | Char | default | 9 | Checks if the character is within the angled 3D area |
| `05FD` | IS_CHAR_IN_ANGLED_AREA_ON_FOOT_3D | Char | default | 9 | Checks if the character is within the angled 3D area |
| `05FE` | IS_CHAR_IN_ANGLED_AREA_IN_CAR_3D | Char | default | 9 | Checks if the character is in a car which is within the angled 3D area |
| `05FF` | IS_CHAR_STOPPED_IN_ANGLED_AREA_3D | Char | default | 9 | Checks if the character is within the angled 3D area and is motionless |
| `0600` | IS_CHAR_STOPPED_IN_ANGLED_AREA_ON_FOOT_3D | Char | default | 9 | Checks if the character is on foot within the angled 3D area and is motionless |
| `0601` | IS_CHAR_STOPPED_IN_ANGLED_AREA_IN_CAR_3D | Char | default | 9 | Checks if the character is in a motionless car within the angled 3D area |
| `0602` | IS_CHAR_IN_TAXI | Char | default | 1 | Returns true if the character is driving a taxi |
| `0603` | TASK_GO_TO_COORD_ANY_MEANS | Task | default | 6 | Assigns the character the task of getting to the specified coordinates |
| `0604` | GET_HEADING_FROM_VECTOR_2D | Math | default | 3 | Gets the angle for the XY offset |
| `0605` | TASK_PLAY_ANIM | Task | default | 9 | Makes the character perform an animation |
| `0606` | LOAD_PATH_NODES_IN_AREA | Path | default | 4 | Adds an area where script created cars will avoid driving in |
| `0607` | RELEASE_PATH_NODES | Path | default | 0 | Removes areas forbidden for scripted cars set up by 0606 |
| `0608` | HAVE_PATH_NODES_BEEN_LOADED |  | default | 0 | Does nothing |
| `0609` | LOAD_ALL_PATH_NODES_FOR_DEBUG |  | default | 0 | Does nothing |
| `060A` | LOAD_CHAR_DECISION_MAKER | DecisionMakerChar | default | 2 | Creates a decision maker with the specified type and adds it to mission cleanup list. Otherwise should be released with REMOVE_DECISION_MAKER |
| `060B` | SET_CHAR_DECISION_MAKER | Char | default | 2 | Sets the decision maker for the character |
| `060C` | CLEAR_ALL_DECISION_MAKERS |  | default | 0 |  |
| `060D` | SET_TEXT_DROPSHADOW | Text | default | 5 | Sets shadow for the current text draw |
| `060E` | IS_PLAYBACK_GOING_ON_FOR_CAR | Car | default | 1 | Returns true if the car is assigned to a path |
| `060F` | SET_SENSE_RANGE | Char | default | 2 | Sets the seeing and hearing range for the specified character or for all mission characters when handle is -1 |
| `0610` | SET_HEARING_RANGE |  | default | 0 | Does nothing |
| `0611` | IS_CHAR_PLAYING_ANIM | Char | default | 2 | Returns true if character is performing the specified animation |
| `0612` | SET_CHAR_ANIM_PLAYING_FLAG | Char | default | 3 | Sets whether the animation is playing |
| `0613` | GET_CHAR_ANIM_CURRENT_TIME | Char | default | 3 | Returns the progress of the animation on the char, ranging from 0.0 to 1.0 |
| `0614` | SET_CHAR_ANIM_CURRENT_TIME | Char | default | 3 | Sets how far through the animation the character is, with 1 |
| `0615` | OPEN_SEQUENCE_TASK | Sequence | default | 1 | Begins a sequence of up to 8 tasks |
| `0616` | CLOSE_SEQUENCE_TASK | Sequence | default | 1 | Ends the task sequence |
| `0617` | SCRIPT_EVENT |  | default | 0 | Does nothing |
| `0618` | PERFORM_SEQUENCE_TASK | Char | default | 2 | Assigns the character to the specified action sequence |
| `0619` | SET_CHAR_COLLISION | Char | default | 2 | Sets whether collision detection is enabled for the character |
| `061A` | GET_CHAR_ANIM_TOTAL_TIME | Char | default | 3 | Returns a float of the length of the animation in milliseconds |
| `061B` | CLEAR_SEQUENCE_TASK | Sequence | default | 1 | Clears the task sequence |
| `061C` | CLEAR_ALL_SEQUENCE_TASKS |  | default | 0 |  |
| `061D` | ADD_ATTRACTOR | Attractor | default | 7 | Adds a ped attractor |
| `061E` | CLEAR_ATTRACTOR | Attractor | default | 1 |  |
| `061F` | CLEAR_ALL_ATTRACTORS |  | default | 0 | Does nothing |
| `0620` | TASK_PLAY_ANIM_FOR_TIME |  | default | 0 | Does nothing |
| `0621` | CREATE_CHAR_AT_ATTRACTOR | Char | default | 5 |  |
| `0622` | TASK_LEAVE_CAR_IMMEDIATELY | Task | default | 2 | Makes the character jump out of the vehicle while it is in motion |
| `0623` | INCREMENT_INT_STAT | Stat | default | 2 | Increases the integer stat by the value given |
| `0624` | INCREMENT_FLOAT_STAT | Stat | default | 2 | Increases the float stat by the value specified |
| `0625` | DECREMENT_INT_STAT | Stat | default | 2 | Decreases the integer stat by the value given |
| `0626` | DECREMENT_FLOAT_STAT | Stat | default | 2 | Decreases the float stat by the value given |
| `0627` | REGISTER_INT_STAT | Stat | default | 2 | Updates the specified integer stat |
| `0628` | REGISTER_FLOAT_STAT | Stat | default | 2 | Sets the specified stat to the specified value, if the specified value is greater than the current stat value |
| `0629` | SET_INT_STAT | Stat | default | 2 | Sets the integer stat to the specified value |
| `062A` | SET_FLOAT_STAT | Stat | default | 2 | Sets the float stat to the specified value |
| `062B` | GET_ATTEMPTS_FOR_THIS_MISSION |  | default | 0 | Does nothing |
| `062C` | REGISTER_THIS_MISSION_HAS_BEEN_ATTEMPTED |  | default | 0 | Does nothing |
| `062D` | REGISTER_THIS_MISSION_HAS_BEEN_PASSED |  | default | 0 | Does nothing |
| `062E` | GET_SCRIPT_TASK_STATUS | Char | default | 3 | Returns the status of the specified script task of the character |
| `062F` | CREATE_GROUP | Group | default | 2 | Creates a new group, which multiple characters can be assigned to, allowing control over all of them as a group |
| `0630` | SET_GROUP_LEADER | Group | default | 2 | Puts the specified character into the group as the leader |
| `0631` | SET_GROUP_MEMBER | Group | default | 2 | Puts the specified character into the group as a member |
| `0632` | REMOVE_GROUP | Group | default | 1 | Releases the group |
| `0633` | TASK_LEAVE_ANY_CAR | Task | default | 1 | Makes the char exit the car, if he is in one |
| `0634` | TASK_KILL_CHAR_ON_FOOT_WHILE_DUCKING | Task | default | 5 |  |
| `0635` | TASK_AIM_GUN_AT_CHAR | Task | default | 3 | Makes a character aim at another character |
| `0636` | TASK_SIDE_STEP_AND_SHOOT |  | default | 9 | Does nothing |
| `0637` | TASK_GO_TO_COORD_WHILE_SHOOTING | Task | default | 8 | Makes a character go to the location while shooting at another character |
| `0638` | TASK_STAY_IN_SAME_PLACE | Task | default | 2 | Makes the character stay in the same place |
| `0639` | TASK_TURN_CHAR_TO_FACE_CHAR | Task | default | 2 | Makes a character face another character |
| `063A` | OPEN_THREAT_LIST |  | default | 0 |  |
| `063B` | CLOSE_THREAT_LIST |  | default | 0 |  |
| `063C` | SET_PEDMODEL_AS_THREAT |  | default | 0 |  |
| `063D` | SET_CHAR_THREAT_LIST |  | default | 0 |  |
| `063E` | REMOVE_THREAT_LIST |  | default | 0 |  |
| `063F` | PERFORM_SEQUENCE_TASK_REPEATEDLY |  | default | 0 |  |
| `0640` | SET_PEDTYPE_AS_THREAT |  | default | 0 |  |
| `0641` | CLEAR_CHAR_THREATS |  | default | 0 |  |
| `0642` | IS_CHAR_AT_SCRIPTED_ATTRACTOR | Char | default | 2 |  |
| `0643` | SET_SEQUENCE_TO_REPEAT | Sequence | default | 2 | Sets whether the task sequence repeats continuously |
| `0644` | CREATE_PED_GENERATOR |  | default | 0 |  |
| `0645` | SWITCH_PED_GENERATOR |  | default | 0 |  |
| `0646` | GET_SEQUENCE_PROGRESS | Char | default | 2 | Gets the characters task sequence progress, as started by 0618 |
| `0647` | CLEAR_LOOK_AT | Char | default | 1 | Clears the char's look task, making them stop looking at whatever they were assigned to look at |
| `0648` | SET_FOLLOW_NODE_THRESHOLD_DISTANCE | Char | default | 2 | Sets the range within which the char responds to events |
| `0649` | SET_CHAR_ZONE_DISTANCE |  | default | 0 |  |
| `064A` | ADD_PEDMODEL_AS_ATTRACTOR_USER |  | default | 0 | Does nothing |
| `064B` | CREATE_FX_SYSTEM | Particle | default | 6 | Creates a particle effect |
| `064C` | PLAY_FX_SYSTEM | Particle | default | 1 | Makes the specified particle visible |
| `064D` | PAUSE_FX_SYSTEM |  | default | 0 | Does nothing |
| `064E` | STOP_FX_SYSTEM | Particle | default | 1 | Stops the specified particle at the source |
| `064F` | PLAY_AND_KILL_FX_SYSTEM | Particle | default | 1 | Starts the particle effect and relinquishes script control over it |
| `0650` | KILL_FX_SYSTEM | Particle | default | 1 | Stops the particle and deletes it |
| `0651` | CREATE_FX_SYSTEM_WITH_DIRECTION |  | default | 0 | Does nothing |
| `0652` | GET_INT_STAT | Stat | default | 2 | Returns the value of the specified integer stat |
| `0653` | GET_FLOAT_STAT | Stat | default | 2 | Returns the value of the specified float stat |
| `0654` | SET_OBJECT_RENDER_SCORCHED | Object | default | 2 | Makes the object look like it has been burnt |
| `0655` | TASK_LOOK_AT_OBJECT | Task | default | 3 | Makes the character look at an object |
| `0656` | LIMIT_ANGLE | Math | default | 2 | Gets the exact angle of an angle |
| `0657` | OPEN_CAR_DOOR | Car | default | 2 | Opens the specified car door |
| `0658` | SET_GROUP_DEFAULT_LEADER_TASK |  | default | 0 |  |
| `0659` | SET_ATTRACTOR_PAIR |  | default | 0 | Does nothing |
| `065A` | PLACE_CHAR_AT_ATTRACTOR |  | default | 0 | Does nothing |
| `065B` | GET_PICKUP_COORDINATES | Pickup | default | 4 | Returns the X, Y and Z coordinates of the pickup |
| `065C` | REMOVE_DECISION_MAKER | DecisionMaker | default | 1 | Removes the decision maker |
| `065D` | VIEW_INTEGER_VARIABLE |  | default | 2 | Outputs an integer with a string |
| `065E` | VIEW_FLOAT_VARIABLE |  | default | 2 | Outputs a float with a string |
| `065F` | WATCH_INTEGER_VARIABLE |  | default | 2 | Does nothing |
| `0660` | WATCH_FLOAT_VARIABLE |  | default | 2 | Does nothing |
| `0661` | BREAKPOINT |  | default | 1 | Does nothing |
| `0662` | WRITE_DEBUG |  | debug | 1 |  |
| `0662` | WRITE_DEBUG |  | default | 1 | Outputs debug text |
| `0663` | WRITE_DEBUG_WITH_INT |  | debug | 2 |  |
| `0663` | WRITE_DEBUG_WITH_INT |  | default | 2 | Outputs a string with an integer |
| `0664` | WRITE_DEBUG_WITH_FLOAT |  | debug | 2 |  |
| `0664` | WRITE_DEBUG_WITH_FLOAT |  | default | 2 | Does nothing |
| `0665` | GET_CHAR_MODEL | Char | default | 2 | Returns the characters model |
| `0666` | IS_CHAR_TOUCHING_ANY_OBJECT |  | default | 0 | Does nothing |
| `0667` | TASK_AIM_GUN_AT_COORD | Task | default | 5 | Makes the character aim at the specified coordinates |
| `0668` | TASK_SHOOT_AT_COORD | Task | default | 5 | Makes the character turn round and shoot at the specified coordinates |
| `0669` | CREATE_FX_SYSTEM_ON_CHAR | Particle | default | 7 | Creates a particle attached to a character |
| `066A` | CREATE_FX_SYSTEM_ON_CHAR_WITH_DIRECTION | Particle | default | 10 | Creates a particle effect attached to a character |
| `066B` | CREATE_FX_SYSTEM_ON_CAR | Particle | default | 7 | Creates a particle effect attached to a vehicle |
| `066C` | CREATE_FX_SYSTEM_ON_CAR_WITH_DIRECTION | Particle | default | 10 | Creates a particle and attaches it to the specified vehicle with the specified offset and direction |
| `066D` | CREATE_FX_SYSTEM_ON_OBJECT | Particle | default | 7 | Creates a particle effect on an object |
| `066E` | CREATE_FX_SYSTEM_ON_OBJECT_WITH_DIRECTION | Particle | default | 10 | Creates particle effect on an object |
| `066F` | ADD_QUEUED_DIALOGUE |  | default | 0 | Does nothing |
| `0670` | IS_DIALOGUE_FINISHED |  | default | 0 | Does nothing |
| `0671` | IS_DIALOGUE_PLAYING |  | default | 0 | Does nothing |
| `0672` | TASK_DESTROY_CAR | Task | default | 2 | Makes the character attack a vehicle |
| `0673` | TASK_DIVE_AND_GET_UP | Task | default | 4 | Makes the character perform a dive in the specified direction |
| `0674` | CUSTOM_PLATE_FOR_NEXT_CAR | Car | default | 2 | Sets the numberplate of the next car to be spawned with the specified model |
| `0675` | CREATE_PED_GENERATOR_AT_ATTRACTOR |  | default | 0 | Does nothing |
| `0676` | TASK_SHUFFLE_TO_NEXT_CAR_SEAT | Task | default | 2 | Makes the character move to the seat on the right |
| `0677` | TASK_CHAT_WITH_CHAR | Task | default | 4 | Makes the character chat with another character |
| `0678` | GET_CHAR_AT_SCRIPTED_ATTRACTOR |  | default | 0 | Does nothing |
| `0679` | ATTACH_CAMERA_TO_VEHICLE | Camera | default | 9 | Keeps the camera relative to the car with the specified offset |
| `067A` | ATTACH_CAMERA_TO_VEHICLE_LOOK_AT_VEHICLE | Camera | default | 7 | Puts the camera on the vehicle like in 0679 |
| `067B` | ATTACH_CAMERA_TO_VEHICLE_LOOK_AT_CHAR | Camera | default | 7 | Attaches the camera to the vehicle and points it at the specified character |
| `067C` | ATTACH_CAMERA_TO_CHAR | Camera | default | 9 | Keeps the camera relative to the char with the specified offset |
| `067D` | ATTACH_CAMERA_TO_CHAR_LOOK_AT_VEHICLE | Camera | default | 7 |  |
| `067E` | ATTACH_CAMERA_TO_CHAR_LOOK_AT_CHAR | Camera | default | 7 | Puts the camera on the character like with 067C |
| `067F` | FORCE_CAR_LIGHTS | Car | default | 2 | Sets an override for the car's lights |
| `0680` | ADD_PEDTYPE_AS_ATTRACTOR_USER | Attractor | default | 2 |  |
| `0681` | ATTACH_OBJECT_TO_CAR | Object | default | 8 |  |
| `0682` | DETACH_OBJECT | Object | default | 5 | Detaches the object with optional rotation and force |
| `0683` | ATTACH_CAR_TO_CAR | Car | default | 8 |  |
| `0684` | DETACH_CAR | Car | default | 5 | Detaches the car with optional rotation and force |
| `0685` | IS_OBJECT_ATTACHED | Object | default | 1 |  |
| `0686` | IS_VEHICLE_ATTACHED | Car | default | 1 |  |
| `0687` | CLEAR_CHAR_TASKS | Char | default | 1 | Clears the char's task, making them quit whatever they were doing |
| `0688` | TASK_TOGGLE_PED_THREAT_SCANNER | Task | default | 4 |  |
| `0689` | POP_CAR_DOOR | Car | default | 3 | Removes the specified car door component from the car |
| `068A` | FIX_CAR_DOOR | Car | default | 2 | Repairs the car door |
| `068B` | TASK_EVERYONE_LEAVE_CAR | Car | default | 1 | Makes all passengers of the car leave it |
| `068C` | IS_PLAYER_TARGETTING_ANYTHING | Player | default | 1 | Returns true if the specified player is auto-aiming at a ped or object |
| `068D` | GET_ACTIVE_CAMERA_COORDINATES | Camera | default | 3 | Stores the cameras coordinates |
| `068E` | GET_ACTIVE_CAMERA_POINT_AT | Camera | default | 3 | Gets the coordinates the camera is pointing to |
| `068F` | GET_CLOSEST_BUYABLE_OBJECT_TO_PLAYER |  | default | 0 | Does nothing |
| `0690` | OPEN_FRIEND_LIST |  | default | 0 |  |
| `0691` | CLOSE_FRIEND_LIST |  | default | 0 |  |
| `0692` | REMOVE_FRIEND_LIST |  | default | 0 |  |
| `0693` | SET_PEDMODEL_AS_FRIEND |  | default | 0 |  |
| `0694` | SET_PEDTYPE_AS_FRIEND |  | default | 0 |  |
| `0695` | CLEAR_CHAR_FRIENDS |  | default | 0 |  |
| `0696` | SET_CHAR_FRIEND_LIST |  | default | 0 |  |
| `0697` | POP_CAR_PANEL | Car | default | 3 | Detatches or deletes car's body part |
| `0698` | FIX_CAR_PANEL | Car | default | 2 | Repairs or reinstalls car's body part |
| `0699` | FIX_CAR_TYRE | Car | default | 2 | Repairs a car's tire |
| `069A` | ATTACH_OBJECT_TO_OBJECT | Object | default | 8 |  |
| `069B` | ATTACH_OBJECT_TO_CHAR | Object | default | 8 |  |
| `069C` | ATTACH_CAMERA_TO_OBJECT |  | default | 0 | Does nothing |
| `069D` | ATTACH_CAMERA_TO_OBJECT_LOOK_AT_VEHICLE |  | default | 0 | Does nothing |
| `069E` | ATTACH_CAMERA_TO_OBJECT_LOOK_AT_CHAR |  | default | 0 | Does nothing |
| `069F` | ATTACH_CAMERA_TO_OBJECT_LOOK_AT_OBJECT |  | default | 0 | Does nothing |
| `06A0` | ATTACH_CAMERA_TO_CHAR_LOOK_AT_OBJECT |  | default | 0 | Does nothing |
| `06A1` | ATTACH_CAMERA_TO_VEHICLE_LOOK_AT_OBJECT |  | default | 0 | Does nothing |
| `06A2` | GET_CAR_SPEED_VECTOR | Car | default | 4 |  |
| `06A3` | GET_CAR_MASS | Car | default | 2 | Returns the vehicle's mass |
| `06A4` | TASK_KILL_THREATS_ON_FOOT_WHILE_DUCKING |  | default | 0 | Does nothing |
| `06A5` | TASK_DIVE_FROM_ATTACHMENT_AND_GET_UP | Task | default | 2 | Makes character detach from host, perform dive then get up |
| `06A6` | TASK_PLAY_ANIM_WITH_VELOCITY_EXTRACTION |  | default | 0 | Does nothing |
| `06A7` | ATTACH_CHAR_TO_BIKE | Char | default | 9 |  |
| `06A8` | TASK_GOTO_CHAR_OFFSET | Task | default | 5 | Approaches the char at the specified offset, specified by the radius and angle |
| `06A9` | TASK_LOOK_AT_COORD | Task | default | 5 | Makes the char look at the specified coordinates |
| `06AA` | IS_RECORDING_GOING_ON_FOR_CAR |  | default | 1 | Does nothing |
| `06AB` | HIDE_CHAR_WEAPON_FOR_SCRIPTED_CUTSCENE | Char | default | 2 | Hides all of the specified char's weapons |
| `06AC` | GET_CHAR_SPEED | Char | default | 2 | Returns the char's movement speed |
| `06AD` | SET_GROUP_DECISION_MAKER | Group | default | 2 | Sets the decision maker for a group of characters |
| `06AE` | LOAD_GROUP_DECISION_MAKER | DecisionMakerGroup | default | 2 | Creates a decision maker for use on groups of actors |
| `06AF` | DISABLE_PLAYER_SPRINT | Player | default | 2 |  |
| `06B0` | TASK_SIT_DOWN | Task | default | 2 | Makes the char sit down for the specified amount of time |
| `06B1` | CREATE_SEARCHLIGHT | Searchlight | default | 9 |  |
| `06B2` | DELETE_SEARCHLIGHT | Searchlight | default | 1 |  |
| `06B3` | DOES_SEARCHLIGHT_EXIST | Searchlight | default | 1 | Returns true if the handle is a valid searchlight handle |
| `06B4` | MOVE_SEARCHLIGHT_BETWEEN_COORDS | Searchlight | default | 8 | Makes the specified searchlight travel between the two specified points with the specified speed |
| `06B5` | POINT_SEARCHLIGHT_AT_COORD | Searchlight | default | 5 | Makes the searchlight target move/travel to the specified coords |
| `06B6` | POINT_SEARCHLIGHT_AT_CHAR | Searchlight | default | 3 | Makes the searchlight follow the specified char |
| `06B7` | IS_CHAR_IN_SEARCHLIGHT | Searchlight | default | 2 | Returns true if the searchlight has spotted the char |
| `06B8` | SET_GROUP_DEFAULT_TASK |  | default | 0 |  |
| `06B9` | HAS_CUTSCENE_LOADED | Cutscene | default | 0 | Returns true if the cutscene has finished loading |
| `06BA` | TASK_TURN_CHAR_TO_FACE_COORD | Task | default | 4 |  |
| `06BB` | TASK_DRIVE_POINT_ROUTE | Task | default | 3 |  |
| `06BC` | FIRE_SINGLE_BULLET | World | default | 7 | Creates firearm projectile effect between two coordinates. Leaves visible trace and deals damage on hit |
| `06BD` | IS_LINE_OF_SIGHT_CLEAR | World | default | 11 | Checks if there is something in the range of the two specified points |
| `06BE` | GET_CAR_ROLL | Car | default | 2 | Returns the Y Angle of the vehicle |
| `06BF` | POINT_SEARCHLIGHT_AT_VEHICLE | Searchlight | default | 3 |  |
| `06C0` | IS_VEHICLE_IN_SEARCHLIGHT | Searchlight | default | 2 | Returns true if the searchlights light is on the vehicle |
| `06C1` | CREATE_SEARCHLIGHT_ON_VEHICLE | Searchlight | default | 10 | Creates a searchlight-styled light cone on a car with the specified offset and points to a certain point |
| `06C2` | TASK_GO_TO_COORD_WHILE_AIMING | Task | default | 11 |  |
| `06C3` | GET_NUMBER_OF_FIRES_IN_RANGE | World | default | 5 |  |
| `06C4` | ADD_BLIP_FOR_SEARCHLIGHT | Blip | default | 2 | Creates a blip indicating the searchlights position on the radar |
| `06C5` | SKIP_TO_END_AND_STOP_PLAYBACK_RECORDED_CAR | Car | default | 1 |  |
| `06C6` | TASK_OPEN_DRIVER_DOOR |  | default | 0 | Does nothing |
| `06C7` | TASK_CAR_TEMP_ACTION | Task | default | 4 | Makes the AI driver perform the action in the vehicle for the specified period of time |
| `06C8` | SET_LA_RIOTS | Game | default | 1 | Enables the LS Riots, making smoke appear on houses, random car fires occur, peds stealing things and attacking each other in a frenzy |
| `06C9` | REMOVE_CHAR_FROM_GROUP | Char | default | 1 | Removes the character from their current group |
| `06CA` | ATTACH_SEARCHLIGHT_TO_SEARCHLIGHT_OBJECT | Searchlight | default | 7 | Attaches the searchlight to the specified objects |
| `06CB` | SET_VEHICLE_RECORDS_COLLISIONS |  | default | 0 | Does nothing |
| `06CC` | DRAW_CROSS_IN_FRONT_OF_DEBUG_CAMERA |  | default | 0 |  |
| `06CD` | DRAW_DEBUG_CUBE |  | default | 0 |  |
| `06CE` | GET_CAR_LAST_ROUTE_COORDS |  | default | 0 | Does nothing |
| `06CF` | DISPLAY_TIMER_BARS |  | default | 1 | Does nothing |
| `06D0` | SWITCH_EMERGENCY_SERVICES | Game | default | 1 | Sets whether emergency traffic spawns |
| `06D1` | SET_VAR_TEXT_LABEL16 |  | default | 2 | Copies up to 16 characters from src to dest |
| `06D2` | SET_LVAR_TEXT_LABEL16 |  | default | 2 | Copies up to 16 characters from src to dest |
| `06D3` | VAR_TEXT_LABEL16 |  | default | 0 |  |
| `06D4` | LVAR_TEXT_LABEL16 |  | default | 0 |  |
| `06D5` | CREATE_CHECKPOINT | Checkpoint | default | 9 | Creates racing/flight style red checkpoint object |
| `06D6` | DELETE_CHECKPOINT | Checkpoint | default | 1 |  |
| `06D7` | SWITCH_RANDOM_TRAINS | Game | default | 1 | Sets whether trains are generated |
| `06D8` | CREATE_MISSION_TRAIN | Train | default | 6 | Creates a script handled train from a predefined type (the type dictates how long the train is and the varieties of carriages) and sets the direction for the train to head in |
| `06D9` | DELETE_MISSION_TRAINS | World | default | 0 | Destroys all script-created trains |
| `06DA` | MARK_MISSION_TRAINS_AS_NO_LONGER_NEEDED | Streaming | default | 0 | Marks the train as no longer needed by the script, allowing it to be deleted by the game |
| `06DB` | DELETE_ALL_TRAINS | World | default | 0 | Destroys all trains, including those that are not created by the script |
| `06DC` | SET_TRAIN_SPEED | Train | default | 2 | Sets the trains acceleration |
| `06DD` | SET_TRAIN_CRUISE_SPEED | Train | default | 2 | Sets the trains speed |
| `06DE` | GET_TRAIN_CABOOSE | Train | default | 2 | Gets the handle of the last carriage (known as the "caboose") |
| `06DF` | DELETE_PLAYER | Player | default | 1 | Removes the specified player |
| `06E0` | SET_TWO_PLAYER_CAMERA_MODE | Camera | default | 1 | Enables the cooperative camera mode |
| `06E1` | TASK_CAR_MISSION | Task | default | 6 | Sets the car's current mission with various parameters |
| `06E2` | TASK_GO_TO_OBJECT | Task | default | 4 | Makes the character go to an object |
| `06E3` | TASK_WEAPON_ROLL | Task | default | 2 |  |
| `06E4` | TASK_CHAR_ARREST_CHAR | Task | default | 2 | Makes the character attempt to arrest another character |
| `06E5` | GET_AVAILABLE_VEHICLE_MOD | Car | default | 3 | Returns a model id available for the vehicle's mod slot, or -1 otherwise |
| `06E6` | GET_VEHICLE_MOD_TYPE | Streaming | default | 2 | Returns a slot the upgrade model is for |
| `06E7` | ADD_VEHICLE_MOD | Car | default | 3 | Adds a new mod with the model to the vehicle |
| `06E8` | REMOVE_VEHICLE_MOD | Car | default | 2 | Removes the vehicle's mod with the specified model |
| `06E9` | REQUEST_VEHICLE_MOD | Streaming | default | 1 | Loads the upgrade model and any associated models |
| `06EA` | HAS_VEHICLE_MOD_LOADED | Streaming | default | 1 | Returns true if the vehicle upgrade model has loaded |
| `06EB` | MARK_VEHICLE_MOD_AS_NO_LONGER_NEEDED | Streaming | default | 1 | Marks the vehicle upgrade model as no longer needed, allowing it to be unloaded by the streamer |
| `06EC` | GET_NUM_AVAILABLE_PAINTJOBS | Car | default | 2 | Gets the number of possible paintjobs that can be applied to the car |
| `06ED` | GIVE_VEHICLE_PAINTJOB | Car | default | 2 | Sets the car's paintjob |
| `06EE` | IS_GROUP_MEMBER | Char | default | 2 | Returns true if the character is a member of the specified group |
| `06EF` | IS_GROUP_LEADER | Char | default | 2 | Returns true if the character is the leader of the specified group |
| `06F0` | SET_GROUP_SEPARATION_RANGE | Group | default | 2 | Sets how far members of the group can be from the leader before they are removed from the group |
| `06F1` | LIMIT_TWO_PLAYER_DISTANCE | Game | default | 1 | Sets how far apart players can get on 2-player mode |
| `06F2` | RELEASE_TWO_PLAYER_DISTANCE | Game | default | 0 | Releases the distance limit set by LIMIT_TWO_PLAYER_DISTANCE |
| `06F3` | SET_PLAYER_PLAYER_TARGETTING | Game | default | 1 | Enables each player to target the other player |
| `06F4` | CREATE_SCRIPT_GANG_ROADBLOCK |  | default | 0 | Does nothing |
| `06F5` | GET_SCRIPT_FIRE_COORDS | ScriptFire | default | 4 | Gets the coordinates of the fire |
| `06F6` | CLEAR_TWO_PLAYER_CAMERA_MODE |  | default | 0 | Does nothing |
| `06F7` | SET_PLAYER_PASSENGER_CAN_SHOOT |  | default | 0 | Does nothing |
| `06F8` | GET_NTH_CLOSEST_CAR_NODE_WITH_HEADING | Path | default | 8 |  |
| `06F9` | GET_HEIGHT_OF_CAR_WHEELS_FROM_GROUND |  | default | 0 | Does nothing |
| `06FA` | SET_PLAYERS_CAN_BE_IN_SEPARATE_CARS | Game | default | 1 | Sets whether the players can be in separate cars during a 2-player mission |
| `06FB` | SWITCH_PLAYER_CROSSHAIR |  | default | 0 | Does nothing |
| `06FC` | DOES_CAR_HAVE_STUCK_CAR_CHECK | Car | default | 1 | Returns true if the car has car stuck check enabled |
| `06FD` | SET_PLAYBACK_SPEED | Car | default | 2 | Sets the playback speed of the car playing a car recording |
| `06FE` | GET_CAR_VALUE |  | default | 0 | Does nothing |
| `06FF` | ARE_ANY_CHARS_NEAR_CHAR | Char | default | 2 | Returns true if any characters are within range of the character |
| `0700` | SKIP_CUTSCENE_START |  | default | 0 | Does nothing |
| `0701` | SKIP_CUTSCENE_END |  | default | 0 |  |
| `0702` | GET_PERCENTAGE_TAGGED_IN_AREA | World | default | 5 | Gets the percentage of the number of tags sprayed in the area |
| `0703` | SET_TAG_STATUS_IN_AREA | World | default | 5 | Sets whether all tags in the area are sprayed |
| `0704` | CAR_GOTO_COORDINATES_RACING | Car | default | 4 | Makes the AI drive to the destination as fast as possible, trying to overtake other vehicles |
| `0705` | START_PLAYBACK_RECORDED_CAR_USING_AI | Car | default | 2 | Starts the playback of a recorded car with driver AI enabled |
| `0706` | SKIP_IN_PLAYBACK_RECORDED_CAR | Car | default | 2 | Advances the recorded car playback by the specified amount |
| `0707` | SKIP_CUTSCENE_START_INTERNAL |  | default | 1 | Enables skipping of the current scene |
| `0708` | CLEAR_CHAR_DECISION_MAKER_EVENT_RESPONSE | DecisionMakerChar | default | 2 | Resets the task for the event of the specified decision maker |
| `0709` | ADD_CHAR_DECISION_MAKER_EVENT_RESPONSE | DecisionMakerChar | default | 9 | Sets which action should occur according to the event on the following parameters |
| `070A` | TASK_PICK_UP_OBJECT | Task | default | 10 | Attaches the specified char to an object with the optional addition of having it perform an animation |
| `070B` | DROP_OBJECT | Char | default | 2 |  |
| `070C` | EXPLODE_CAR_IN_CUTSCENE | Car | default | 1 | Makes the vehicle explode without affecting its surroundings |
| `070D` | BUILD_PLAYER_MODEL | Player | default | 1 | Rebuilds the player model, applying any required texture changes |
| `070E` | PLANE_ATTACK_PLAYER | Plane | default | 3 | Sets the planes mission to attack the player |
| `070F` | PLANE_FLY_IN_DIRECTION | Plane | default | 4 |  |
| `0710` | PLANE_FOLLOW_ENTITY | Plane | default | 4 |  |
| `0711` | ALLOCATE_SCRIPT_TO_PED_GENERATOR |  | default | 0 | Does nothing |
| `0712` | ALLOCATE_SCRIPT_TO_RANDOM_PED |  | default | 0 | Does nothing |
| `0713` | TASK_DRIVE_BY | Task | default | 10 |  |
| `0714` | SET_CAR_STAY_IN_SLOW_LANE | Car | default | 2 |  |
| `0715` | TAKE_REMOTE_CONTROL_OF_CAR | Rc | default | 2 | Puts the specified player in control of a remote-control vehicle |
| `0716` | IS_CLOSEST_OBJECT_OF_TYPE_SMASHED_OR_DAMAGED | World | default | 7 |  |
| `0717` | START_SETTING_UP_CONVERSATION | Conversation | default | 1 | Starts a conversation between the character and the player and clears the conversation lines |
| `0718` | SET_UP_CONVERSATION_NODE |  | default | 0 | Does nothing |
| `0719` | FINISH_SETTING_UP_CONVERSATION | Conversation | default | 0 | Finalizes the current conversation sequence started with 0717. Selected answers will be subtitled |
| `071A` | IS_CONVERSATION_AT_NODE | Conversation | default | 2 | Returns true if the conversation is at the specified node |
| `071B` | CLEAR_ALL_CONVERSATIONS |  | default | 0 | Does nothing |
| `071C` | GET_CHAR_LIGHTING |  | default | 0 | Does nothing |
| `071D` | SET_CLOSEST_OBJECT_OF_TYPE_RENDER_SCORCHED |  | default | 0 | Does nothing |
| `071E` | GET_OBJECT_HEALTH | Object | default | 2 |  |
| `071F` | SET_OBJECT_HEALTH | Object | default | 2 |  |
| `0720` | GET_VEHICLE_WHEEL_UPGRADE_CLASS |  | default | 0 | Does nothing |
| `0721` | GET_NUM_WHEELS_IN_UPGRADE_CLASS |  | default | 0 | Does nothing |
| `0722` | GET_WHEEL_IN_UPGRADE_CLASS |  | default | 0 | Does nothing |
| `0723` | BREAK_OBJECT | Object | default | 2 | Smashes the object to pieces |
| `0724` | HELI_ATTACK_PLAYER | Heli | default | 3 | Makes the heli follow and attack the current player in the given radius |
| `0725` | HELI_FLY_IN_DIRECTION |  | default | 0 | Does nothing |
| `0726` | HELI_FOLLOW_ENTITY | Heli | default | 4 | Makes the heli follow the specified char or vehicle in the air |
| `0727` | POLICE_HELI_CHASE_ENTITY | Heli | default | 4 | Makes the helicopter hunt down the character or the vehicle within the specified radius |
| `0728` | SET_UP_CONVERSATION_END_NODE |  | default | 0 | Does nothing |
| `0729` | TASK_USE_MOBILE_PHONE | Task | default | 2 | Makes a character pull out a cellphone, answer it, and hold it to their ear |
| `072A` | TASK_WARP_CHAR_INTO_CAR_AS_DRIVER | Task | default | 2 | Warps the character into the specified vehicle's driver seat |
| `072B` | TASK_WARP_CHAR_INTO_CAR_AS_PASSENGER | Task | default | 3 |  |
| `072C` | SWITCH_COPS_ON_BIKES | Game | default | 1 | Disables the game from creating police bikes and their riders on the roads |
| `072D` | IS_FLAME_IN_ANGLED_AREA_2D | World | default | 6 | Returns true if there's any fire particles within the specified area |
| `072E` | IS_FLAME_IN_ANGLED_AREA_3D | World | default | 8 | Returns true if there's any flames within the specified area |
| `072F` | ADD_STUCK_CAR_CHECK_WITH_WARP | StuckCarCheck | default | 7 | Attempts to automatically restore vehicles that get stuck or flipped |
| `0730` | DAMAGE_CAR_PANEL | Car | default | 2 | Damages a panel on the car |
| `0731` | SET_CAR_ROLL | Car | default | 2 | Sets the Y Angle of the vehicle to the specified value |
| `0732` | SUPPRESS_CAR_MODEL | CarGenerator | default | 1 | Prevents the specified car model from spawning for car generators |
| `0733` | DONT_SUPPRESS_CAR_MODEL | CarGenerator | default | 1 | Allows the specified car model to spawn for car generators |
| `0734` | DONT_SUPPRESS_ANY_CAR_MODELS | CarGenerator | default | 0 | Resets the disabled car model list for car generators |
| `0735` | IS_PS2_KEYBOARD_KEY_PRESSED |  | default | 1 | Does nothing |
| `0736` | IS_PS2_KEYBOARD_KEY_JUST_PRESSED |  | default | 1 | Does nothing |
| `0737` | IS_CHAR_HOLDING_OBJECT | Char | default | 2 | Returns true if the char is lifting the specified object |
| `0738` | SET_ZONE_RADAR_COLOURS |  | default | 0 | Does nothing |
| `0739` | GIVE_LOWRIDER_SUSPENSION_TO_CAR |  | default | 0 | Does nothing |
| `073A` | DOES_CAR_HAVE_LOWRIDER_SUSPENSION |  | default | 0 | Does nothing |
| `073B` | SET_CAR_CAN_GO_AGAINST_TRAFFIC | Car | default | 2 | Sets whether the vehicle will drive the wrong way on roads |
| `073C` | DAMAGE_CAR_DOOR | Car | default | 2 | Damages a component on the vehicle |
| `073D` | GET_RANDOM_CAR_IN_SPHERE |  | default | 0 | Does nothing |
| `073E` | GET_RANDOM_CAR_IN_SPHERE_NO_SAVE | World | default | 6 |  |
| `073F` | GET_RANDOM_CHAR_IN_SPHERE | World | default | 8 |  |
| `0740` | GET_COORDS_OF_CLOSEST_COLLECTABLE1 |  | default | 0 | Does nothing |
| `0741` | HAS_CHAR_BEEN_ARRESTED | Char | default | 1 | Returns true if the character has been arrested |
| `0742` | SET_PLANE_THROTTLE | Plane | default | 2 |  |
| `0743` | HELI_LAND_AT_COORDS | Heli | default | 6 |  |
| `0744` | GET_STAT_CHANGE_AMOUNT |  | default | 0 | Does nothing |
| `0745` | PLANE_STARTS_IN_AIR | Plane | default | 1 | Provides the aircraft with full power so it can start flying mid-air |
| `0746` | SET_RELATIONSHIP | Game | default | 3 | Sets the attitude of peds with one pedtype towards peds of another pedtype |
| `0747` | CLEAR_RELATIONSHIP | Game | default | 3 |  |
| `0748` | CLEAR_ALL_RELATIONSHIPS |  | default | 0 | Does nothing |
| `0749` | CLEAR_GROUP_DECISION_MAKER_EVENT_RESPONSE | DecisionMakerGroup | default | 2 | Resets the task for the event of the specified group decision maker |
| `074A` | ADD_GROUP_DECISION_MAKER_EVENT_RESPONSE | DecisionMakerGroup | default | 9 | Sets which action should occur according to the event on the following parameters |
| `074B` | DRAW_SPRITE_WITH_ROTATION | Hud | default | 10 | This is an extended version of 038D with scale and angle parameters |
| `074C` | TASK_USE_ATTRACTOR | Task | default | 2 |  |
| `074D` | TASK_SHOOT_AT_CHAR | Task | default | 3 |  |
| `074E` | SET_INFORM_RESPECTED_FRIENDS | Char | default | 3 |  |
| `074F` | IS_CHAR_RESPONDING_TO_EVENT | Char | default | 2 | Returns true if the character is responding to the specified ped event |
| `0750` | SET_OBJECT_VISIBLE | Object | default | 2 | Sets whether the object is visible |
| `0751` | TASK_FLEE_CHAR_ANY_MEANS | Task | default | 8 |  |
| `0752` | STOP_RECORDING_CAR |  | default | 1 | Does nothing |
| `0753` | SET_ALERTNESS |  | default | 0 |  |
| `0754` | FLUSH_PATROL_ROUTE | Path | default | 0 | Clears all previous patrol data to start a new patrol route, which can be used in combination with 0755 to create patrol routes |
| `0755` | EXTEND_PATROL_ROUTE | Path | default | 5 | Adds a new point to the patrol route |
| `0756` | TASK_GO_ON_PATROL |  | default | 0 |  |
| `0757` | GET_PATROL_ALERTNESS |  | default | 0 |  |
| `0758` | SET_CHAR_SPECIAL_EVENT |  | default | 0 | Does nothing |
| `0759` | SET_ATTRACTOR_AS_COVER_NODE |  | default | 0 | Does nothing |
| `075A` | PLAY_OBJECT_ANIM | Object | default | 6 | Plays an object animation |
| `075B` | SET_RADAR_ZOOM | Hud | default | 1 |  |
| `075C` | DOES_BLIP_EXIST | Blip | default | 1 | Returns true if the handle is a valid blip handle |
| `075D` | LOAD_PRICES | Shopping | default | 1 |  |
| `075E` | LOAD_SHOP | Shopping | default | 1 |  |
| `075F` | GET_NUMBER_OF_ITEMS_IN_SHOP | Shopping | default | 1 |  |
| `0760` | GET_ITEM_IN_SHOP | Shopping | default | 2 | Returns an identifier for an item associated with the shopping data entry |
| `0761` | GET_PRICE_OF_ITEM | Shopping | default | 2 |  |
| `0762` | TASK_DEAD | Task | default | 1 | Kills the character |
| `0763` | SET_CAR_AS_MISSION_CAR | Car | default | 1 | Sets the script as the owner of the vehicle and adds it to the mission cleanup list |
| `0764` | IS_SEARCHLIGHT_IN_ANGLED_AREA_2D |  | default | 0 | Does nothing |
| `0765` | IS_SEARCHLIGHT_IN_ANGLED_AREA_3D |  | default | 0 | Does nothing |
| `0766` | SWITCH_SEARCHLIGHT_BULB |  | default | 0 | Does nothing |
| `0767` | SET_ZONE_POPULATION_TYPE | Zone | default | 2 | Sets which population type from popcycle.dat will inhabit this zone |
| `0768` | SET_ZONE_GANG_CAP |  | default | 0 |  |
| `0769` | GET_ZONE_GANG_CAP |  | default | 0 |  |
| `076A` | SET_ZONE_DEALER_STRENGTH | Zone | default | 2 | Sets the total number of drug dealers in the zone |
| `076B` | GET_ZONE_DEALER_STRENGTH | Zone | default | 2 | Returns the drug dealer density of the specified zone |
| `076C` | SET_ZONE_GANG_STRENGTH | Zone | default | 3 | Sets the density of the gang members in the specified zone |
| `076D` | GET_ZONE_GANG_STRENGTH | Zone | default | 3 | Returns the density of the gang members in the specified zone |
| `076E` | SET_NO_POLICE_DURING_LA_RIOTS |  | default | 0 | Does nothing |
| `076F` | IS_MESSAGE_BEING_DISPLAYED | Text | default | 0 | Returns true if a priority GXT string is displayed on screen |
| `0770` | SET_CHAR_IS_TARGET_PRIORITY | Char | default | 2 | Causes the auto aim to be more likely to target the specified char than actors without this flag |
| `0771` | CUSTOM_PLATE_DESIGN_FOR_NEXT_CAR | Streaming | default | 2 | Sets the town ID of the license plate which is created on the specified model, affecting which texture is chosen for the plate |
| `0772` | TASK_GOTO_CAR | Task | default | 4 |  |
| `0773` | CLEAR_HELP_WITH_THIS_LABEL |  | default | 0 |  |
| `0774` | IS_SEARCHLIGHT_BULB_ON |  | default | 0 | Does nothing |
| `0775` | CREATE_OIL_PUDDLE |  | default | 0 | Does nothing |
| `0776` | REQUEST_IPL | Streaming | default | 1 |  |
| `0777` | REMOVE_IPL | Streaming | default | 1 |  |
| `0778` | REMOVE_IPL_DISCREETLY | Streaming | default | 1 |  |
| `0779` | TASK_OPEN_PASSENGER_DOOR |  | default | 0 | Does nothing |
| `077A` | SET_CHAR_RELATIONSHIP | Char | default | 3 |  |
| `077B` | CLEAR_CHAR_RELATIONSHIP | Char | default | 3 |  |
| `077C` | CLEAR_ALL_CHAR_RELATIONSHIPS | Char | default | 2 |  |
| `077D` | GET_CAR_PITCH | Car | default | 2 | Returns the X Angle of the vehicle |
| `077E` | GET_AREA_VISIBLE | Streaming | default | 1 | Gets the current interior ID |
| `077F` | ADD_INT_TO_VAR_CONSOLE |  | default | 0 | Does nothing |
| `0780` | HELI_KEEP_ENTITY_IN_VIEW | Heli | default | 5 |  |
| `0781` | GET_WEAPONTYPE_MODEL | Weapon | default | 2 | Gets the model ID of the weapon according to the weapon type |
| `0782` | GET_WEAPONTYPE_SLOT | Weapon | default | 2 |  |
| `0783` | GET_SHOPPING_EXTRA_INFO | Shopping | default | 3 |  |
| `0784` | GIVE_PLAYER_CLOTHES | Player | default | 4 |  |
| `0785` | GIVE_PLAYER_TATTOO |  | default | 0 | Does nothing |
| `0786` | GET_NUMBER_OF_FIRES_IN_AREA | World | default | 7 | Gets the number of fires within the specified area |
| `0787` | SET_CHAR_TYRES_CAN_BE_BURST |  | default | 0 | Does nothing |
| `0788` | ATTACH_WINCH_TO_HELI | Heli | default | 2 |  |
| `0789` | RELEASE_ENTITY_FROM_WINCH | Heli | default | 1 |  |
| `078A` | GET_TRAIN_CARRIAGE | Train | default | 3 | Gets the nth train carriage |
| `078B` | GRAB_ENTITY_ON_WINCH | Heli | default | 4 | Retrieves the entity attached to the heli's magnet and returns to specific variables depending on the entities type |
| `078C` | GET_NAME_OF_ITEM | Shopping | default | 2 |  |
| `078D` | ADD_FLOAT_TO_VAR_CONSOLE |  | default | 0 | Does nothing |
| `078E` | TASK_DRAG_CHAR_FROM_CAR |  | default | 0 | Does nothing |
| `078F` | TASK_CLIMB | Task | default | 2 | Makes the character jump and climb on an object |
| `0790` | BUY_ITEM | Shopping | default | 1 | Charges the player for the purchase of the item and in many cases, automatically gives the item to the player |
| `0791` | BUY_TATTOO |  | default | 0 | Does nothing |
| `0792` | CLEAR_CHAR_TASKS_IMMEDIATELY | Char | default | 1 | Clears all the characters tasks immediately, resetting the character to an idle state |
| `0793` | STORE_CLOTHES_STATE | Player | default | 0 | Stores the players current clothes to later be restored with 0794 |
| `0794` | RESTORE_CLOTHES_STATE | Player | default | 0 | Restores the players clothes stored with 0793 |
| `0795` | DELETE_WINCH_FOR_HELI |  | default | 0 | Does nothing |
| `0796` | GET_ROPE_HEIGHT_FOR_OBJECT | Object | default | 2 |  |
| `0797` | SET_ROPE_HEIGHT_FOR_OBJECT | Object | default | 2 |  |
| `0798` | GRAB_ENTITY_ON_ROPE_FOR_OBJECT | Object | default | 4 |  |
| `0799` | RELEASE_ENTITY_FROM_ROPE_FOR_OBJECT | Object | default | 1 |  |
| `079A` | ATTACH_CAR_TO_ROPE_FOR_OBJECT |  | default | 0 | Does nothing |
| `079B` | ATTACH_CHAR_TO_ROPE_FOR_OBJECT |  | default | 0 | Does nothing |
| `079C` | ATTACH_OBJECT_TO_ROPE_FOR_OBJECT |  | default | 0 | Does nothing |
| `079D` | PLAYER_ENTERED_DOCK_CRANE | Crane | default | 0 | Puts the player in the San Fierro dock crane |
| `079E` | PLAYER_ENTERED_BUILDINGSITE_CRANE | Crane | default | 0 | Puts the player in the San Fierro building site crane |
| `079F` | PLAYER_LEFT_CRANE | Crane | default | 0 | Removes the player from the current crane |
| `07A0` | PERFORM_SEQUENCE_TASK_FROM_PROGRESS | Char | default | 4 |  |
| `07A1` | SET_NEXT_DESIRED_MOVE_STATE | Char | default | 1 | Sets how the character chooses to go to their destination in the next task without a parameter specifying this |
| `07A2` | SET_NEXT_EVENT_RESPONSE_SEQUENCE |  | default | 0 | Does nothing |
| `07A3` | TASK_GOTO_CHAR_AIMING | Task | default | 4 |  |
| `07A4` | GET_SEQUENCE_PROGRESS_RECURSIVE | Char | default | 3 |  |
| `07A5` | TASK_KILL_CHAR_ON_FOOT_TIMED | Task | default | 3 | Makes the character attack the specified character |
| `07A6` | GET_NEAREST_TAG_POSITION | World | default | 6 |  |
| `07A7` | TASK_JETPACK | Task | default | 1 |  |
| `07A8` | SET_AREA51_SAM_SITE | Game | default | 1 | Enables or disables the SAM site at the Area 51 |
| `07A9` | IS_CHAR_IN_ANY_SEARCHLIGHT | Char | default | 2 | Returns the handle for the searchlight that's targeting the character |
| `07AA` | GET_SEARCHLIGHT_COORDS |  | default | 0 | Does nothing |
| `07AB` | IS_TRAILER_ATTACHED_TO_CAB | Trailer | default | 2 | Returns true if CAR A has CAR B attached to it like a trailer |
| `07AC` | DETACH_TRAILER_FROM_CAB | Trailer | default | 2 | Detaches the trailer from the car which it is attached to |
| `07AD` | GET_TRAILER_ATTACHED_TO_CAB |  | default | 0 | Does nothing |
| `07AE` | GET_CAB_ATTACHED_TO_TRAILER |  | default | 0 | Does nothing |
| `07AF` | GET_PLAYER_GROUP | Player | default | 2 |  |
| `07B0` | GET_LOADED_SHOP | Shopping | default | 1 | Returns the name of currently loaded subsection in shopping |
| `07B1` | GET_BEAT_PROXIMITY | Audio | default | 4 | Returns information about a beat offset from the current playback position of the active beat track (0954) |
| `07B2` | SET_BEAT_ZONE_SIZE |  | default | 0 | Does nothing |
| `07B3` | SET_GROUP_DEFAULT_TASK_ALLOCATOR | Group | default | 2 |  |
| `07B4` | SET_PLAYER_GROUP_RECRUITMENT | Player | default | 2 | Sets the player's ability to recruit new members to the group |
| `07B5` | DISPLAY_TWO_ONSCREEN_COUNTERS |  | default | 0 | Does nothing |
| `07B6` | DISPLAY_TWO_ONSCREEN_COUNTERS_WITH_STRING |  | default | 0 | Does nothing |
| `07B7` | DISPLAY_NTH_TWO_ONSCREEN_COUNTERS |  | default | 0 | Does nothing |
| `07B8` | DISPLAY_NTH_TWO_ONSCREEN_COUNTERS_WITH_STRING |  | default | 0 | Does nothing |
| `07B9` | TASK_KILL_CHAR_ON_FOOT_PATROL |  | default | 0 |  |
| `07BA` | HELI_AIM_AHEAD_OF_TARGET_ENTITY |  | default | 0 | Does nothing |
| `07BB` | ACTIVATE_HELI_SPEED_CHEAT | Heli | default | 2 | Provides the heli with extra thrust power |
| `07BC` | TASK_SET_CHAR_DECISION_MAKER | Task | default | 2 | Sets the decision maker used by the specified char |
| `07BD` | DELETE_MISSION_TRAIN | Train | default | 1 | Removes the specified script created train |
| `07BE` | MARK_MISSION_TRAIN_AS_NO_LONGER_NEEDED | Train | default | 1 | Removes the specified script created train from the list of trains that the game shouldn't delete |
| `07BF` | SET_BLIP_ALWAYS_DISPLAY_ON_ZOOMED_RADAR | Blip | default | 2 | Sets whether the tracking blip will remain regardless of the entities existance |
| `07C0` | REQUEST_CAR_RECORDING | Streaming | default | 1 | Loads the specified car recording |
| `07C1` | HAS_CAR_RECORDING_BEEN_LOADED | Streaming | default | 1 | Returns true if the car recording has finished loading |
| `07C2` | DISPLAY_PLAYBACK_RECORDED_CAR |  | default | 0 | Does nothing |
| `07C3` | GET_OBJECT_QUATERNION | Object | default | 5 | Gets the object's quaternion |
| `07C4` | SET_OBJECT_QUATERNION | Object | default | 5 | Sets the object's quaternion |
| `07C5` | GET_VEHICLE_QUATERNION | Car | default | 5 | Gets the quaternion values of the car |
| `07C6` | SET_VEHICLE_QUATERNION | Car | default | 5 | Sets the rotation of a vehicle using quaternion values |
| `07C7` | SET_MISSION_TRAIN_COORDINATES | Train | default | 4 | Puts the train on the rails nearest to the specified coordinates |
| `07C8` | DISPLAY_DEBUG_MESSAGE |  | default | 0 | Does nothing |
| `07C9` | TASK_COMPLEX_PICKUP_OBJECT | Task | default | 2 | Makes character walk to the object and pick it up |
| `07CA` | TASK_SIMPLE_PUTDOWN_OBJECT |  | default | 0 | Does nothing |
| `07CB` | LISTEN_TO_PLAYER_GROUP_COMMANDS | Char | default | 2 |  |
| `07CC` | SET_PLAYER_ENTER_CAR_BUTTON | Pad | default | 2 | Sets whether the player can enter and exit vehicles |
| `07CD` | TASK_CHAR_SLIDE_TO_COORD | Task | default | 6 |  |
| `07CE` | SET_BULLET_WHIZZ_BY_DISTANCE |  | default | 0 | Does nothing |
| `07CF` | SET_TWO_PLAYER_CAM_MODE_SEPARATE_CARS |  | default | 0 | Does nothing |
| `07D0` | GET_CURRENT_DAY_OF_WEEK | Clock | default | 1 | Returns an integer representation of the in-game day of the week |
| `07D1` | SET_CURRENT_DAY_OF_WEEK |  | default | 0 | Does nothing |
| `07D2` | ACTIVATE_INTERIORS |  | default | 0 | Does nothing |
| `07D3` | REGISTER_SCRIPT_BRAIN_FOR_CODE_USE | StreamedScript | default | 2 | Allows the game to start a new ambient script by name, e.g. to control behavior of peds in interiors |
| `07D4` | REGISTER_OBJECT_SCRIPT_BRAIN_FOR_CODE_USE |  | default | 0 | Does nothing |
| `07D5` | APPLY_FORCE_TO_CAR | Car | default | 7 | Applies force to car with offset from its center of mass |
| `07D6` | IS_INT_LVAR_EQUAL_TO_INT_VAR |  | default | 2 | Returns true if the integer value of the local variable is equivalent to the integer value of the global variable |
| `07D7` | IS_FLOAT_LVAR_EQUAL_TO_FLOAT_VAR |  | default | 2 | Returns true if the float value of the local variable is equivalent to the float value of the global variable |
| `07D8` | IS_INT_LVAR_NOT_EQUAL_TO_INT_VAR |  | default | 0 |  |
| `07D9` | IS_FLOAT_LVAR_NOT_EQUAL_TO_FLOAT_VAR |  | default | 0 |  |
| `07DA` | ADD_TO_CAR_ROTATION_VELOCITY | Car | default | 4 |  |
| `07DB` | SET_CAR_ROTATION_VELOCITY | Car | default | 4 |  |
| `07DC` | GET_CAR_ROTATION_VELOCITY |  | default | 0 | Does nothing |
| `07DD` | SET_CHAR_SHOOT_RATE | Char | default | 2 | Sets the attack rate of the char |
| `07DE` | IS_MODEL_IN_CDIMAGE | Streaming | default | 1 | Returns true if a file for the model exists |
| `07DF` | REMOVE_OIL_PUDDLES_IN_AREA | World | default | 4 |  |
| `07E0` | SET_BLIP_AS_FRIENDLY | Blip | default | 2 |  |
| `07E1` | TASK_SWIM_TO_COORD | Task | default | 4 |  |
| `07E2` | TASK_GO_STRAIGHT_TO_COORD_WITHOUT_STOPPING |  | default | 0 | Does nothing |
| `07E3` | GET_BEAT_INFO_FOR_CURRENT_TRACK |  | default | 0 | Does nothing |
| `07E4` | GET_MODEL_DIMENSIONS | Streaming | default | 7 |  |
| `07E5` | COPY_CHAR_DECISION_MAKER | DecisionMakerChar | default | 2 | Copies a decision makers data to another decision maker |
| `07E6` | COPY_GROUP_DECISION_MAKER | DecisionMakerGroup | default | 2 | Creates copy of group decision maker and adds it to mission cleanup list. Otherwise should be released with REMOVE_DECISION_MAKER |
| `07E7` | TASK_DRIVE_POINT_ROUTE_ADVANCED | Task | default | 6 |  |
| `07E8` | IS_RELATIONSHIP_SET | Game | default | 3 | Returns true if the specified relationship between ped types is set |
| `07E9` | HAS_CHAR_SPOTTED_CAR |  | default | 0 | Does nothing |
| `07EA` | SET_ROPE_HEIGHT_FOR_HELI |  | default | 0 | Does nothing |
| `07EB` | GET_ROPE_HEIGHT_FOR_HELI |  | default | 0 | Does nothing |
| `07EC` | IS_CAR_LOWRIDER |  | default | 0 | Does nothing |
| `07ED` | IS_PERFORMANCE_CAR |  | default | 0 | Does nothing |
| `07EE` | SET_CAR_ALWAYS_CREATE_SKIDS | Car | default | 2 |  |
| `07EF` | GET_CITY_FROM_COORDS | World | default | 4 | Returns the city the specified location is within |
| `07F0` | HAS_OBJECT_OF_TYPE_BEEN_SMASHED | World | default | 5 |  |
| `07F1` | IS_PLAYER_PERFORMING_WHEELIE | Player | default | 1 |  |
| `07F2` | IS_PLAYER_PERFORMING_STOPPIE | Player | default | 1 | Returns true if the player is performing a stoppie |
| `07F3` | SET_CHECKPOINT_COORDS | Checkpoint | default | 4 |  |
| `07F4` | SET_ONSCREEN_TIMER_DISPLAY |  | default | 0 | Does nothing |
| `07F5` | CONTROL_CAR_HYDRAULICS | Car | default | 5 | Changes the car wheels' suspension level |
| `07F6` | GET_GROUP_SIZE | Group | default | 3 |  |
| `07F7` | SET_OBJECT_COLLISION_DAMAGE_EFFECT | Object | default | 2 | Sets whether the object can be destroyed or not |
| `07F8` | SET_CAR_FOLLOW_CAR | Car | default | 3 |  |
| `07F9` | PLAYER_ENTERED_QUARRY_CRANE | Crane | default | 0 | Puts the player in the crane at the quarry near Las Venturras |
| `07FA` | PLAYER_ENTERED_LAS_VEGAS_CRANE | Crane | default | 0 | Puts the player in the crane at the building site in Las Venturras |
| `07FB` | SWITCH_ENTRY_EXIT | World | default | 2 | Locates the enex marker via the specified name and sets whether it is visible and usable |
| `07FC` | DISPLAY_TEXT_WITH_FLOAT | Text | default | 5 | Converts the float to two separate numbers to use in a 2-numbered GXT entry, and draws the text |
| `07FD` | DOES_GROUP_EXIST | Group | default | 1 | Returns true if the handle is a valid group handle |
| `07FE` | GIVE_MELEE_ATTACK_TO_CHAR | Char | default | 3 | Sets the specified characters fighting style and moves |
| `07FF` | SET_CAR_HYDRAULICS | Car | default | 2 | Enables hydraulic suspension on the car |
| `0800` | IS_2PLAYER_GAME_GOING_ON | Game | default | 0 | Returns true if the game is in 2-player mode |
| `0801` | GET_CAMERA_FOV | Camera | default | 1 | Returns the cameras field of view |
| `0802` | SET_GLOBAL_PED_SEARCH_PARAMS |  | default | 0 |  |
| `0803` | DOES_CAR_HAVE_HYDRAULICS | Car | default | 1 | Returns true if the car has hydraulics installed |
| `0804` | TASK_CHAR_SLIDE_TO_COORD_AND_PLAY_ANIM | Task | default | 14 | Makes a character walk to the specified point, trun to heading, then play an animation |
| `0805` | ALLOCATE_SCRIPT_TO_OBJECT |  | default | 0 | Does nothing |
| `0806` | GET_TOTAL_NUMBER_OF_PEDS_KILLED_BY_PLAYER | Player | default | 2 | Returns the number of peds killed by the player since the last reset (0297) |
| `0807` | SET_TWO_PLAYER_CAM_MODE_SAME_CAR_SHOOTING |  | default | 0 | Does nothing |
| `0808` | SET_TWO_PLAYER_CAM_MODE_SAME_CAR_NO_SHOOTING |  | default | 0 | Does nothing |
| `0809` | SET_TWO_PLAYER_CAM_MODE_NOT_BOTH_IN_CAR |  | default | 0 | Does nothing |
| `080A` | GET_LEVEL_DESIGN_COORDS_FOR_OBJECT | Object | default | 5 |  |
| `080B` | SAVE_TEXT_LABEL_TO_DEBUG_FILE |  | default | 1 | Does nothing |
| `080C` | GET_CHAR_BREATH |  | default | 0 | Does nothing |
| `080D` | SET_CHAR_BREATH |  | default | 0 | Does nothing |
| `080E` | GET_CHAR_HIGHEST_PRIORITY_EVENT | Char | default | 2 | Gets the characters active ped event |
| `080F` | ARE_PATHS_LOADED_FOR_CAR |  | default | 0 | Does nothing |
| `0810` | GET_PARKING_NODE_IN_AREA | World | default | 9 | Stores the coordinates of the nearest car park node in the specified area |
| `0811` | GET_CAR_CHAR_IS_USING | Char | default | 2 | Stores a handle for the vehicle the character is in or entering (alts: 00D9,03C0,0484) |
| `0812` | TASK_PLAY_ANIM_NON_INTERRUPTABLE | Task | default | 9 | Makes the character perform an animation like TASK_PLAY_ANIM, except it will not be disturbed by any events |
| `0813` | FORCE_NEXT_DIE_ANIM |  | default | 0 | Does nothing |
| `0814` | ADD_STUNT_JUMP | World | default | 16 | Creates a trigger for a Unique Jump bonus |
| `0815` | SET_OBJECT_COORDINATES_AND_VELOCITY | Object | default | 4 | Sets the object's coordinates without affecting the rotation |
| `0816` | SET_CHAR_KINDA_STAY_IN_SAME_PLACE | Char | default | 2 | Sets whether the character shouldn't chase their victim far (to attempt a melee attack or get in weapon range) |
| `0817` | TASK_FOLLOW_PATROL_ROUTE | Task | default | 3 | Assigns the character to the patrol path |
| `0818` | IS_CHAR_IN_AIR | Char | default | 1 | Returns true if the character is in the air |
| `0819` | GET_CHAR_HEIGHT_ABOVE_GROUND | Char | default | 2 | Returns the char's distance from ground |
| `081A` | SET_CHAR_WEAPON_SKILL | Char | default | 2 | Sets the character's fire arms wielding style |
| `081B` | ARE_PATHS_LOADED_IN_AREA |  | default | 0 | Does nothing |
| `081C` | SET_TEXT_EDGE | Text | default | 5 | Adds an outline to the next text drawn using a text draw command |
| `081D` | SET_CAR_ENGINE_BROKEN | Car | default | 2 | Sets whether the car's engine is broken |
| `081E` | IS_THIS_MODEL_A_BOAT | Streaming | default | 1 | Returns true if the model is the model of a boat |
| `081F` | IS_THIS_MODEL_A_PLANE | Streaming | default | 1 | Returns true if the model is the model of a plane |
| `0820` | IS_THIS_MODEL_A_HELI | Streaming | default | 1 | Returns true if the model is the model of a helicopter |
| `0821` | IS_3D_COORD_IN_ZONE |  | default | 0 | Does nothing |
| `0822` | SET_FIRST_PERSON_IN_CAR_CAMERA_MODE | Camera | default | 1 | Enables vehicle bumper view for the camera |
| `0823` | TASK_GREET_PARTNER | Task | default | 4 | Makes a character greet another character with a handshake |
| `0824` | GET_CLOSEST_PICKUP_COORDS_TO_COORD |  | default | 0 | Does nothing |
| `0825` | SET_HELI_BLADES_FULL_SPEED | Heli | default | 1 | Makes the helicopter rotor spin at full speed instantly |
| `0826` | DISPLAY_HUD | Hud | default | 1 | Sets whether the HUD displays |
| `0827` | CONNECT_LODS | Object | default | 2 | Sets which LOD object should show when the object is being viewed from far away |
| `0828` | SET_MAX_FIRE_GENERATIONS | Game | default | 1 | Sets the limit on how many fires can be created from other fires when "propagation" was enabled on 02CF |
| `0829` | TASK_DIE_NAMED_ANIM | Task | default | 5 | Makes the char perform an animation similarly to 0605 |
| `082A` | SET_PLAYER_DUCK_BUTTON | Pad | default | 2 | Sets whether the player can use the crouch button |
| `082B` | FIND_NEAREST_MULTIBUILDING |  | default | 0 |  |
| `082C` | SET_MULTIBUILDING_MODEL |  | default | 0 |  |
| `082D` | GET_NUMBER_MULTIBUILDING_MODELS |  | default | 0 |  |
| `082E` | GET_MULTIBUILDING_MODEL_INDEX |  | default | 0 |  |
| `082F` | SET_CURRENT_BUYABLE_PROPERTY |  | default | 0 |  |
| `0830` | SET_POOL_TABLE_COORDS | World | default | 6 | Creates a pool collision object |
| `0831` | IS_AUDIO_BUILD |  | default | 0 | Does nothing |
| `0832` | CLEAR_QUEUED_DIALOGUE |  | default | 0 | Does nothing |
| `0833` | HAS_OBJECT_BEEN_PHOTOGRAPHED | Object | default | 1 | Returns true if the object has been photographed |
| `0834` | DO_CAMERA_BUMP | Camera | default | 2 | Bumps the camera in the specified direction as if it had collided |
| `0835` | GET_CURRENT_DATE | Clock | default | 2 | Returns the in-game day of the month and month of the year |
| `0836` | SET_OBJECT_ANIM_SPEED | Object | default | 3 | Sets the object's animation speed |
| `0837` | IS_OBJECT_PLAYING_ANIM | Object | default | 2 | Returns true if the object is playing the specified animation |
| `0838` | SET_OBJECT_ANIM_PLAYING_FLAG |  | default | 0 | Does nothing |
| `0839` | GET_OBJECT_ANIM_CURRENT_TIME | Object | default | 3 | Gets the current progress of the object's animation |
| `083A` | SET_OBJECT_ANIM_CURRENT_TIME | Object | default | 3 | Sets the progress of an animation, with 0 |
| `083B` | GET_OBJECT_ANIM_TOTAL_TIME |  | default | 0 | Does nothing |
| `083C` | SET_CHAR_VELOCITY | Char | default | 4 | Sets the characters velocity |
| `083D` | GET_CHAR_VELOCITY | Char | default | 4 | Gets the characters velocity |
| `083E` | SET_CHAR_ROTATION | Char | default | 4 | Sets the characters rotation |
| `083F` | GET_CAR_UPRIGHT_VALUE | Car | default | 2 | Gets the car's vertical angle |
| `0840` | SET_VEHICLE_AREA_VISIBLE | Car | default | 2 |  |
| `0841` | SELECT_WEAPONS_FOR_VEHICLE | Car | default | 2 | Sets the vehicle to use its secondary guns |
| `0842` | GET_CITY_PLAYER_IS_IN | Player | default | 2 | Gets the player's current city |
| `0843` | GET_NAME_OF_ZONE | Zone | default | 4 | Returns the GXT key associated with the zone at the specified coordinates |
| `0844` | IS_VAR_TEXT_LABEL_EMPTY | Text | default | 1 | Returns true if the string is empty |
| `0845` | IS_LVAR_TEXT_LABEL_EMPTY | Text | default | 1 | Returns true if the string is empty |
| `0846` | IS_VAR_TEXT_LABEL16_EMPTY | Text | default | 1 | Returns true if the string is empty |
| `0847` | IS_LVAR_TEXT_LABEL16_EMPTY | Text | default | 1 | Returns true if the string is empty |
| `0848` | SWITCH |  | default | 0 |  |
| `0849` | ENDSWITCH |  | default | 0 |  |
| `084A` | CASE |  | default | 0 |  |
| `084B` | DEFAULT |  | default | 0 |  |
| `084C` | BREAK |  | default | 0 |  |
| `084D` | ACTIVATE_INTERIOR_PEDS | Game | default | 1 | Enables ped spawning in interiors |
| `084E` | SET_VEHICLE_CAN_BE_TARGETTED | Car | default | 2 | Sets whether the vehicle can be targeted |
| `084F` | GET_GROUP_LEADER |  | default | 0 | Does nothing |
| `0850` | TASK_FOLLOW_FOOTSTEPS | Task | default | 2 | Makes one char follow another |
| `0851` | DAMAGE_CHAR | Char | default | 3 | Decreases the characters health |
| `0852` | SET_CAR_CAN_BE_VISIBLY_DAMAGED | Car | default | 2 | Sets whether the vehicle can be visibly damaged |
| `0853` | SET_HELI_REACHED_TARGET_DISTANCE | Heli | default | 2 |  |
| `0854` | BLOCK_NODES_IN_AREA |  | default | 0 |  |
| `0855` | GET_SOUND_LEVEL_AT_COORDS | World | default | 5 | Gets the level that the character can hear noise at the specified position |
| `0856` | SET_CHAR_ALLOWED_TO_DUCK | Char | default | 2 | Sets whether the character can crouch |
| `0857` | SET_WATER_CONFIGURATION |  | default | 0 | Does nothing |
| `0858` | SET_HEADING_FOR_ATTACHED_PLAYER | Player | default | 3 | Sets the view angle for the player attached to an object or vehicle |
| `0859` | TASK_WALK_ALONGSIDE_CHAR | Task | default | 2 | Makes the character walk alongside the specified character |
| `085A` | CREATE_EMERGENCY_SERVICES_CAR | World | default | 4 | Creates an emergency service vehicle on the closest road to the specified coordinates |
| `085B` | TASK_KINDA_STAY_IN_SAME_PLACE | Task | default | 2 | Makes the character stay near their current position |
| `085C` | TASK_USE_ATTRACTOR_ADVANCED |  | default | 0 | Does nothing |
| `085D` | TASK_FOLLOW_PATH_NODES_TO_COORD_SHOOTING |  | default | 0 | Does nothing |
| `085E` | START_PLAYBACK_RECORDED_CAR_LOOPED | Car | default | 2 | Starts looped playback of a recorded car path |
| `085F` | START_PLAYBACK_RECORDED_CAR_USING_AI_LOOPED |  | default | 0 | Does nothing |
| `0860` | SET_CHAR_AREA_VISIBLE | Char | default | 2 | Sets the interior that the char is in |
| `0861` | IS_ATTACHED_PLAYER_HEADING_ACHIEVED | Player | default | 1 | Returns true if the heading has finished being applied, as started by 0858 |
| `0862` | GET_MODEL_NAME_FOR_DEBUG_ONLY |  | default | 0 | Does nothing |
| `0863` | TASK_USE_NEARBY_ENTRY_EXIT |  | default | 0 | Does nothing |
| `0864` | ENABLE_ENTRY_EXIT_PLAYER_GROUP_WARPING | Game | default | 4 | Enables the entry/exit marker in the specified radius of the coordinates |
| `0865` | FREEZE_STATE_OF_INTERIORS |  | default | 0 |  |
| `0866` | GET_CLOSEST_STEALABLE_OBJECT | World | default | 5 | Gets the closest object which can be stolen for burglary missions |
| `0867` | IS_PROCEDURAL_INTERIOR_ACTIVE | Game | default | 1 | Returns true in interactive interiors |
| `0868` | CLEAR_THIS_VIEW_INTEGER_VARIABLE |  | default | 1 | Does nothing |
| `0869` | CLEAR_THIS_VIEW_FLOAT_VARIABLE |  | default | 1 | Does nothing |
| `086A` | CLEAR_ALL_VIEW_VARIABLES |  | default | 0 | Does nothing |
| `086B` | CLEAR_THIS_INTEGER_WATCHPOINT |  | default | 1 | Does nothing |
| `086C` | CLEAR_THIS_FLOAT_WATCHPOINT |  | default | 1 | Does nothing |
| `086D` | CLEAR_ALL_BREAKPOINTS |  | default | 0 | Does nothing |
| `086E` | CLEAR_ALL_WATCHPOINTS |  | default | 0 | Does nothing |
| `086F` | IS_THIS_MODEL_A_TRAIN |  | default | 0 | Does nothing |
| `0870` | GET_VEHICLE_CHAR_IS_STANDING_ON |  | default | 0 | Does nothing |
| `0871` | SWITCH_START |  | default | 18 | Takes an input value and uses it to determine which label to go to in the code |
| `0872` | SWITCH_CONTINUED |  | default | 18 | Accompanies 0871, increasing the number of possible cases (max 75) |
| `0873` | REMOVE_CAR_RECORDING | Streaming | default | 1 | Unloads the car recording |
| `0874` | SET_ZONE_POPULATION_RACE | Zone | default | 2 | Sets which races will inhabit this zone |
| `0875` | SET_OBJECT_ONLY_DAMAGED_BY_PLAYER | Object | default | 2 | Makes the object damageable only by the player |
| `0876` | CREATE_BIRDS | World | default | 8 | Creates a flock of birds flying in the specified direction |
| `0877` | GET_VEHICLE_DIRT_LEVEL |  | default | 0 | Does nothing |
| `0878` | SET_VEHICLE_DIRT_LEVEL | Car | default | 2 | Sets the dirt level of the car |
| `0879` | SET_GANG_WARS_ACTIVE | Game | default | 1 | Sets whether gang wars can be started by the player or enemy gangs |
| `087A` | IS_GANG_WAR_GOING_ON | Game | default | 0 | Returns true if there is a gang war happening |
| `087B` | GIVE_PLAYER_CLOTHES_OUTSIDE_SHOP | Player | default | 4 | Sets the players clothing |
| `087C` | CLEAR_LOADED_SHOP | Shopping | default | 0 | Releases the loaded shopping data |
| `087D` | SET_GROUP_SEQUENCE | Group | default | 2 | Sets the default task sequence for members of the group |
| `087E` | SET_CHAR_DROPS_WEAPONS_WHEN_DEAD | Char | default | 2 | Sets whether the character will drop any of their weapons when they die |
| `087F` | SET_CHAR_NEVER_LEAVES_GROUP | Char | default | 2 | Prevents the character from leaving their group |
| `0880` | DRAW_RECT_WITH_TITLE |  | default | 0 | Does nothing |
| `0881` | SET_PLAYER_FIRE_BUTTON | Pad | default | 2 | Sets whether the player is able to use weapons |
| `0882` | SET_ATTRACTOR_RADIUS |  | default | 0 | Does nothing |
| `0883` | ATTACH_FX_SYSTEM_TO_CHAR_BONE | Particle | default | 3 | Attaches the specified particle to the specified character |
| `0884` | REGISTER_ATTRACTOR_SCRIPT_BRAIN_FOR_CODE_USE | StreamedScript | default | 2 | Allows the game to start a new ambient script for the ped using the map attractor, e.g. shoppers |
| `0885` | CONST_INT |  | default | 0 | Does nothing |
| `0886` | CONST_FLOAT |  | default | 0 | Does nothing |
| `0887` | SET_HEADING_LIMIT_FOR_ATTACHED_CHAR | Char | default | 3 | Sets the heading limit for a character attached to an object or vehicle |
| `0888` | ADD_BLIP_FOR_DEAD_CHAR | Blip | default | 2 | Adds a blip and a marker to the character (identical to 0187) |
| `0889` | GET_DEAD_CHAR_COORDINATES | Char | default | 4 |  |
| `088A` | TASK_PLAY_ANIM_WITH_FLAGS | Task | default | 11 | Makes the char perform an animation |
| `088B` | SET_VEHICLE_AIR_RESISTANCE_MULTIPLIER | Car | default | 2 | Sets the air resistance for the vehicle |
| `088C` | SET_CAR_COORDINATES_NO_OFFSET | Car | default | 4 | Sets the vehicle coordinates without applying offsets to account for the height of the vehicle |
| `088D` | SET_USES_COLLISION_OF_CLOSEST_OBJECT_OF_TYPE | World | default | 6 | Toggles collision of the object closest to the given coordinates and matching the model |
| `088E` | SET_TIME_ONE_DAY_FORWARD | Clock | default | 0 | Progresses the game to the next day |
| `088F` | SET_TIME_ONE_DAY_BACK |  | default | 0 | Does nothing |
| `0890` | SET_TIMER_BEEP_COUNTDOWN_TIME | Hud | default | 2 | Starts a sound when the countdown timer reaches the specified number of seconds |
| `0891` | TASK_SIT_IN_RESTAURANT |  | default | 0 | Does nothing |
| `0892` | GET_RANDOM_ATTRACTOR_ON_CLOSEST_OBJECT_OF_TYPE |  | default | 0 | Does nothing |
| `0893` | ATTACH_TRAILER_TO_CAB | Trailer | default | 2 |  |
| `0894` | ADD_INTERESTING_ENTITY_FOR_CHAR |  | default | 0 | Does nothing |
| `0895` | CLEAR_INTERESTING_ENTITIES_FOR_CHAR |  | default | 0 | Does nothing |
| `0896` | GET_CLOSEST_ATTRACTOR |  | default | 0 | Does nothing |
| `0897` | IS_VEHICLE_TOUCHING_OBJECT | Car | default | 2 | Returns true if the vehicle is in contact with the object |
| `0898` | ENABLE_CRANE_CONTROLS | Crane | default | 3 | Enables/disables individual crane controls |
| `0899` | ALLOCATE_SCRIPT_TO_ATTRACTOR |  | default | 0 | Does nothing |
| `089A` | GET_CLOSEST_ATTRACTOR_WITH_THIS_SCRIPT |  | default | 0 | Does nothing |
| `089B` | IS_PLAYER_IN_POSITION_FOR_CONVERSATION | Conversation | default | 1 | Returns true if there is a conversation going on between the character and the player and both the character and the player are able to communicate with one another |
| `089C` | ENABLE_CONVERSATION | Conversation | default | 2 | Pauses the scripted conversation assigned to the specified character |
| `089D` | GET_CONVERSATION_STATUS |  | default | 0 | Does nothing |
| `089E` | GET_RANDOM_CHAR_IN_SPHERE_ONLY_DRUGS_BUYERS | World | default | 5 | Loops through the ped pool and returns the first character that is within the specified radius and has the "buys drugs" flag set in peds |
| `089F` | GET_PED_TYPE | Char | default | 2 | Gets the ped type of the character |
| `08A0` | TASK_USE_CLOSEST_MAP_ATTRACTOR | Task | default | 7 |  |
| `08A1` | GET_CHAR_MAP_ATTRACTOR_STATUS |  | default | 0 | Does nothing |
| `08A2` | PLANE_ATTACK_PLAYER_USING_DOG_FIGHT | Plane | default | 3 | Sets the plane mission to attack the player while maintaining the minimum altitude |
| `08A3` | CAN_TRIGGER_GANG_WAR_WHEN_ON_A_MISSION | Game | default | 1 | Allows the player to provoke turf wars while a mission is active |
| `08A4` | CONTROL_MOVABLE_VEHICLE_PART | Car | default | 2 | Sets the angle of a vehicle's extra |
| `08A5` | WINCH_CAN_PICK_VEHICLE_UP | Car | default | 2 | Sets whether the vehicle can be picked up using the magnocrane |
| `08A6` | OPEN_CAR_DOOR_A_BIT | Car | default | 3 | Sets the angle of a car door |
| `08A7` | IS_CAR_DOOR_FULLY_OPEN | Car | default | 2 |  |
| `08A8` | SET_ALWAYS_DRAW_3D_MARKERS | Game | default | 1 | Enables an increase in the distance that markers hovering above entities can be seen from |
| `08A9` | STREAM_SCRIPT | StreamedScript | default | 1 | Loads the ambient script with the specified ID from the script.img file |
| `08AA` | STREAM_SCRIPT_INTERNAL |  | default | 0 | Does nothing |
| `08AB` | HAS_STREAMED_SCRIPT_LOADED | StreamedScript | default | 1 | Returns true if the ambient script has finished loading (08A9) |
| `08AC` | SET_GANG_WARS_TRAINING_MISSION | Game | default | 1 | Disables highlighting of gang territory on the map and radar |
| `08AD` | SET_CHAR_HAS_USED_ENTRY_EXIT | Char | default | 4 | Locates the entry/exit marker in the specified radius of the specified coordinates and links it to the character, also setting the appropriate interior ID for the character and setting the appropriate sky color if the character is player-controlled |
| `08AE` | DRAW_WINDOW_TEXT |  | default | 0 | Does nothing |
| `08AF` | SET_CHAR_MAX_HEALTH | Char | default | 2 | Sets the characters max health |
| `08B0` | SET_CAR_PITCH |  | default | 0 | Does nothing |
| `08B1` | SET_NIGHT_VISION | Game | default | 1 | Enables night vision effects |
| `08B2` | SET_INFRARED_VISION | Game | default | 1 | Enables thermal vision effects |
| `08B3` | SET_ZONE_FOR_GANG_WARS_TRAINING | Zone | default | 1 | Sets the zone as the only zone where a turf war can be provoked |
| `08B4` | IS_GLOBAL_VAR_BIT_SET_CONST | Math | default | 2 | Checks if the nth bit of the number is set |
| `08B5` | IS_GLOBAL_VAR_BIT_SET_VAR | Math | default | 2 | Checks if the nth bit of the number is set |
| `08B6` | IS_GLOBAL_VAR_BIT_SET_LVAR | Math | default | 2 | Checks if the nth bit of the number is set |
| `08B7` | IS_LOCAL_VAR_BIT_SET_CONST | Math | default | 2 | Checks if the nth bit of the number is set |
| `08B8` | IS_LOCAL_VAR_BIT_SET_VAR | Math | default | 2 | Checks if the nth bit of the number is set |
| `08B9` | IS_LOCAL_VAR_BIT_SET_LVAR | Math | default | 2 | Checks if the nth bit of the number is set |
| `08BA` | SET_GLOBAL_VAR_BIT_CONST | Math | default | 2 | Sets the nth bit of the number |
| `08BB` | SET_GLOBAL_VAR_BIT_VAR | Math | default | 2 | Sets the nth bit of the number |
| `08BC` | SET_GLOBAL_VAR_BIT_LVAR | Math | default | 2 | Sets the nth bit of the number |
| `08BD` | SET_LOCAL_VAR_BIT_CONST | Math | default | 2 | Sets the nth bit of the number |
| `08BE` | SET_LOCAL_VAR_BIT_VAR | Math | default | 2 | Sets the nth bit of the number |
| `08BF` | SET_LOCAL_VAR_BIT_LVAR | Math | default | 2 | Sets the nth bit of the number |
| `08C0` | CLEAR_GLOBAL_VAR_BIT_CONST | Math | default | 2 | Clears the nth bit of the number |
| `08C1` | CLEAR_GLOBAL_VAR_BIT_VAR | Math | default | 2 | Clears the nth bit of the number |
| `08C2` | CLEAR_GLOBAL_VAR_BIT_LVAR | Math | default | 2 | Clears the nth bit of the number |
| `08C3` | CLEAR_LOCAL_VAR_BIT_CONST | Math | default | 2 | Clears the nth bit of the number |
| `08C4` | CLEAR_LOCAL_VAR_BIT_VAR | Math | default | 2 | Clears the nth bit of the number |
| `08C5` | CLEAR_LOCAL_VAR_BIT_LVAR | Math | default | 2 | Clears the nth bit of the number |
| `08C6` | SET_CHAR_CAN_BE_KNOCKED_OFF_BIKE | Char | default | 2 | Sets whether the character always stays on bike in collisions |
| `08C7` | SET_CHAR_COORDINATES_DONT_WARP_GANG | Char | default | 4 | Sets the character's coordinates without warping the rest of their group |
| `08C8` | ADD_PRICE_MODIFIER | Shopping | default | 2 | Sets a new base price for the shopping.dat item |
| `08C9` | REMOVE_PRICE_MODIFIER | Shopping | default | 1 | Restores the base price for a shopping.dat item altered by ADD_PRICE_MODIFIER |
| `08CA` | INIT_ZONE_POPULATION_SETTINGS | Zone | default | 0 | Resets all changes made to the zone info |
| `08CB` | EXPLODE_CAR_IN_CUTSCENE_SHAKE_AND_BITS | Car | default | 4 | Causes the vehicle to explode, without damage to surrounding entities |
| `08CC` | PICK_UP_OBJECT_WITH_WINCH |  | default | 0 | Does nothing |
| `08CD` | PICK_UP_VEHICLE_WITH_WINCH |  | default | 0 | Does nothing |
| `08CE` | PICK_UP_CHAR_WITH_WINCH |  | default | 0 | Does nothing |
| `08CF` | STORE_CAR_IN_NEAREST_IMPOUNDING_GARAGE |  | default | 0 | Does nothing |
| `08D0` | IS_SKIP_CUTSCENE_BUTTON_PRESSED | Pad | default | 0 | Returns true if the player is pressing a key used to skip cutscenes or the game has been minimised |
| `08D1` | GET_CUTSCENE_OFFSET | Cutscene | default | 3 | Stores the offset of the currently loaded cutscene |
| `08D2` | SET_OBJECT_SCALE | Object | default | 2 | Sets the scale of the object |
| `08D3` | GET_CURRENT_POPULATION_ZONE_TYPE | Zone | default | 1 | Returns the population type in the zone the player is currently in |
| `08D4` | CREATE_MENU | Menu | default | 9 | Creates the specified panel on the screen with basic settings |
| `08D5` | CONSTANT_INT |  | default | 0 | Does nothing |
| `08D6` | SET_MENU_COLUMN_ORIENTATION | Menu | default | 3 |  |
| `08D7` | GET_MENU_ITEM_SELECTED | Menu | default | 2 | Returns the currently highlighted row in a panel |
| `08D8` | GET_MENU_ITEM_ACCEPTED | Menu | default | 2 | Returns the last row of a panel selected with the sprint key |
| `08D9` | ACTIVATE_MENU_ITEM | Menu | default | 3 |  |
| `08DA` | DELETE_MENU | Menu | default | 1 | Removes the specified panel from the screen |
| `08DB` | SET_MENU_COLUMN | Menu | default | 15 |  |
| `08DC` | SET_BLIP_ENTRY_EXIT | Blip | default | 4 | Assigns the blip to the specified entrance/exit marker |
| `08DD` | SWITCH_DEATH_PENALTIES | Game | default | 1 | Sets whether or not the player loses their weapons and inventory when taken to hospital |
| `08DE` | SWITCH_ARREST_PENALTIES | Game | default | 1 | Sets whether or not the player loses their weapons and inventory when busted |
| `08DF` | SET_EXTRA_HOSPITAL_RESTART_POINT | Restart | default | 5 |  |
| `08E0` | SET_EXTRA_POLICE_STATION_RESTART_POINT | Restart | default | 5 |  |
| `08E1` | FIND_NUMBER_TAGS_TAGGED | Stat | default | 1 | Gets the number of spraytags painted over |
| `08E2` | GET_TERRITORY_UNDER_CONTROL_PERCENTAGE | Stat | default | 1 |  |
| `08E3` | IS_OBJECT_IN_ANGLED_AREA_2D | Object | default | 7 | Checks if the object is within the angled 2D area |
| `08E4` | IS_OBJECT_IN_ANGLED_AREA_3D | Object | default | 9 | Checks if the object is within the angled 3D area |
| `08E5` | GET_RANDOM_CHAR_IN_SPHERE_NO_BRAIN | World | default | 5 | Finds the nearest character to the specified point, in the specified radius |
| `08E6` | SET_PLANE_UNDERCARRIAGE_UP | Plane | default | 2 | Sets whether the plane's landing wheels are up |
| `08E7` | DISABLE_ALL_ENTRY_EXITS | World | default | 1 | Disables all entry/exit markers |
| `08E8` | ATTACH_ANIMS_TO_MODEL | Streaming | default | 2 | Sets an animation pack to be loaded along with the specified model |
| `08E9` | SET_OBJECT_AS_STEALABLE | Object | default | 2 | Sets whether the object can be picked up and carried |
| `08EA` | SET_CREATE_RANDOM_GANG_MEMBERS | Game | default | 1 | Sets whether gang members will spawn |
| `08EB` | ADD_SPARKS | Fx | default | 7 | Creates single burst of spark particles |
| `08EC` | GET_VEHICLE_CLASS | Car | default | 2 | Returns the vehicle's class as defined in vehicles.ide |
| `08ED` | CLEAR_CONVERSATION_FOR_CHAR | Conversation | default | 1 |  |
| `08EE` | SET_MENU_ITEM_WITH_NUMBER | Menu | default | 5 | Sets the numbered GXT of the specified panel row |
| `08EF` | SET_MENU_ITEM_WITH_2_NUMBERS | Menu | default | 6 |  |
| `08F0` | APPEND_TO_NEXT_CUTSCENE | Cutscene | default | 2 |  |
| `08F1` | GET_NAME_OF_INFO_ZONE | Zone | default | 4 | Returns the name of the zone at the specified coordinates |
| `08F2` | VEHICLE_CAN_BE_TARGETTED_BY_HS_MISSILE | Car | default | 2 | Sets whether the player can target this vehicle with a heatseeking rocket launcher |
| `08F3` | SET_FREEBIES_IN_VEHICLE | Car | default | 2 | Sets whether the player can receive items from this vehicle, such as shotgun ammo from a police car and cash from a taxi |
| `08F4` | SET_SCRIPT_LIMIT_TO_GANG_SIZE | Game | default | 1 | Sets the maximum number of members that the player can recruit |
| `08F5` | MAKE_PLAYER_GANG_DISAPPEAR | Player | default | 0 |  |
| `08F6` | MAKE_PLAYER_GANG_REAPPEAR | Player | default | 0 |  |
| `08F7` | GET_CLOTHES_ITEM | Player | default | 4 |  |
| `08F8` | SHOW_UPDATE_STATS | Stat | default | 1 | Displays help boxes indicating that the players stats have been updated |
| `08F9` | IS_VAR_TEXT_LABEL16_EQUAL_TO_TEXT_LABEL |  | default | 2 | Returns true if the two strings are equivalent |
| `08FA` | IS_LVAR_TEXT_LABEL16_EQUAL_TO_TEXT_LABEL |  | default | 2 | Returns true if the two strings are equivalent |
| `08FB` | SET_COORD_BLIP_APPEARANCE | Blip | default | 2 | Works similar to 0165, except this command does not work on tracking blips, has different colors and does not support direct RGBA setting |
| `08FC` | GET_MENU_POSITION |  | default | 0 | Does nothing |
| `08FD` | SET_HEATHAZE_EFFECT | Weather | default | 1 | Specifies whether the heat haze effect should be enabled in sunny conditions |
| `08FE` | IS_HELP_MESSAGE_BEING_DISPLAYED | Text | default | 0 | Returns true if any help message is being displayed |
| `08FF` | HAS_OBJECT_BEEN_DAMAGED_BY_WEAPON | Object | default | 2 | Returns true if the object has been damaged by the specified weapon or damage type |
| `0900` | CLEAR_OBJECT_LAST_WEAPON_DAMAGE | Object | default | 1 | Clears the object's last damaging weapon ID |
| `0901` | SET_PLAYER_JUMP_BUTTON | Pad | default | 2 | Sets whether the player can jump |
| `0902` | SET_OBJECT_BEEN_PHOTOGRAPHED_FLAG |  | default | 0 | Does nothing |
| `0903` | SET_CHAR_BEEN_PHOTOGRAPHED_FLAG |  | default | 0 | Does nothing |
| `0904` | GET_HUD_COLOUR | Hud | default | 5 | Returns the RGBA of the specified HUD color |
| `0905` | LOCK_DOOR | Object | default | 2 | Sets whether the door object is locked at its current rotation and allows it to be pushed open by entities once |
| `0906` | SET_OBJECT_MASS | Object | default | 2 | Sets the object's mass |
| `0907` | GET_OBJECT_MASS | Object | default | 2 | Returns the object's mass |
| `0908` | SET_OBJECT_TURN_MASS | Object | default | 2 | Sets the object's turn mass |
| `0909` | GET_OBJECT_TURN_MASS | Object | default | 2 | Returns the object's turn mass |
| `090A` | IS_PLAYBACK_FOR_CAR_PAUSED |  | default | 0 | Does nothing |
| `090B` | TRIGGER_PED_BOUNCE |  | default | 0 | Does nothing |
| `090C` | SET_SPECIFIC_ZONE_TO_TRIGGER_GANG_WAR | Zone | default | 1 |  |
| `090D` | CLEAR_SPECIFIC_ZONES_TO_TRIGGER_GANG_WAR | Game | default | 0 | Enables turf wars to be provoked in all zones |
| `090E` | SET_ACTIVE_MENU_ITEM | Menu | default | 2 |  |
| `090F` | MARK_STREAMED_SCRIPT_AS_NO_LONGER_NEEDED | StreamedScript | default | 1 | Ends the specified script brain |
| `0910` | REMOVE_STREAMED_SCRIPT | StreamedScript | default | 1 | Releases the ambient script with the specified ID, freeing game memory |
| `0911` | REGISTER_STREAMED_SCRIPT |  | default | 0 | Does nothing |
| `0912` | SET_MESSAGE_FORMATTING | Text | default | 3 | Overrides the position of the text on screen |
| `0913` | START_NEW_STREAMED_SCRIPT | StreamedScript | default | 2 | Runs the ambient script with the specified ID |
| `0914` | REGISTER_STREAMED_SCRIPT_INTERNAL |  | default | 1 | Does nothing |
| `0915` | SET_WEATHER_TO_APPROPRIATE_TYPE_NOW | Weather | default | 0 | Sets the weather appropriate to the weather region the player is currently in |
| `0916` | WINCH_CAN_PICK_OBJECT_UP | Object | default | 2 | Sets whether the object can be picked up with the magnocrane |
| `0917` | SWITCH_AUDIO_ZONE | Zone | default | 2 | Sets whether the IPL defined audio for the specified area should play |
| `0918` | SET_CAR_ENGINE_ON | Car | default | 2 | Sets whether the vehicle's engine is turned on or off |
| `0919` | SET_CAR_LIGHTS_ON | Car | default | 2 | Sets whether the vehicle's lights are on |
| `091A` | GET_LATEST_CONSOLE_COMMAND |  | default | 1 | Does nothing |
| `091B` | RESET_LATEST_CONSOLE_COMMAND |  | default | 0 | Does nothing |
| `091C` | GET_USER_OF_CLOSEST_MAP_ATTRACTOR | World | default | 7 | Returns the character using a map attractor with the specified model in the specified area |
| `091D` | SWITCH_ROADS_BACK_TO_ORIGINAL | Path | default | 6 | Reverts all changes to car paths done with SWITCH_ROADS_ON and SWITCH_ROADS_OFF |
| `091E` | SWITCH_PED_ROADS_BACK_TO_ORIGINAL | Path | default | 6 | Reverts all changes to ped paths done with SWITCH_PED_ROADS_ON and SWITCH_PED_ROADS_OFF |
| `091F` | GET_PLANE_UNDERCARRIAGE_POSITION | Plane | default | 2 |  |
| `0920` | CAMERA_SET_VECTOR_TRACK | Camera | default | 8 | Makes the camera point at the first coordinates and then rotate to point at the second coordinates |
| `0921` | CAMERA_SET_SHAKE_SIMULATION |  | default | 0 | Does nothing |
| `0922` | CAMERA_SET_LERP_FOV | Camera | default | 4 | Sets the cameras zoom factors |
| `0923` | SWITCH_AMBIENT_PLANES | Game | default | 1 | Enables or disables planes |
| `0924` | SET_DARKNESS_EFFECT | Camera | default | 2 | Darkens the game |
| `0925` | CAMERA_RESET_NEW_SCRIPTABLES | Camera | default | 0 | Stops the camera propagating, interpolating, shaking and zooming |
| `0926` | GET_NUMBER_OF_INSTANCES_OF_STREAMED_SCRIPT | StreamedScript | default | 2 | Gets the number of instances of a script |
| `0927` | ALLOCATE_STREAMED_SCRIPT_TO_PED_GENERATOR |  | default | 0 | Does nothing |
| `0928` | ALLOCATE_STREAMED_SCRIPT_TO_RANDOM_PED | StreamedScript | default | 3 | Makes the game start an ambient script when the player is nearby a character of the specified model |
| `0929` | ALLOCATE_STREAMED_SCRIPT_TO_OBJECT | StreamedScript | default | 5 | Makes the game start an ambient script when the player is nearby an object of the specified model |
| `092A` | SET_PLAYER_CAN_BE_DAMAGED |  | default | 0 | Does nothing |
| `092B` | GET_GROUP_MEMBER | Group | default | 3 | Returns the nth group member |
| `092C` | GET_PLAYERS_GANG_IN_CAR_ACTIVE |  | default | 0 | Does nothing |
| `092D` | SET_PLAYERS_GANG_IN_CAR_ACTIVE |  | default | 0 | Does nothing |
| `092E` | GET_WATER_HEIGHT_AT_COORDS | World | default | 4 | Gets the height of the water at the specified 2D coordinates |
| `092F` | CAMERA_PERSIST_TRACK | Camera | default | 1 | Locks the camera target point in position after propagating |
| `0930` | CAMERA_PERSIST_POS | Camera | default | 1 | Locks the cameras position |
| `0931` | CAMERA_PERSIST_FOV | Camera | default | 1 | Locks the zoom level after the camera has finished zooming |
| `0932` | CAMERA_IS_FOV_RUNNING |  | default | 0 | Does nothing |
| `0933` | CAMERA_IS_VECTOR_MOVE_RUNNING | Camera | default | 0 | Returns true if the camera is moving in position |
| `0934` | CAMERA_IS_VECTOR_TRACK_RUNNING | Camera | default | 0 | Returns true if the camera is moving in angle |
| `0935` | CAMERA_IS_SHAKE_RUNNING |  | default | 0 | Does nothing |
| `0936` | CAMERA_SET_VECTOR_MOVE | Camera | default | 8 | Puts the camera at the position of the first passed coordinates and moves it to the second passed coordinates |
| `0937` | DRAW_WINDOW | Hud | default | 6 | Draws a black box with styled text from corner A to corner B |
| `0938` | CLEAR_ALL_QUEUED_DIALOGUE |  | default | 0 | Does nothing |
| `0939` | ATTACH_CAR_TO_OBJECT | Car | default | 8 | Attaches the car to object with offset and rotation |
| `093A` | SET_GARAGE_RESPRAY_FREE | Garage | default | 2 |  |
| `093B` | SET_CHAR_BULLETPROOF_VEST | Char | default | 2 | Specifies that the character should only use upper-body damage animations, meaning they can still run if shot in the legs etc |
| `093C` | SET_ONSCREEN_COUNTER_COLOUR |  | default | 0 | Does nothing |
| `093D` | SET_CINEMA_CAMERA | Camera | default | 1 | Locks the camera on cinematic vehicle mode |
| `093E` | SET_CHAR_FIRE_DAMAGE_MULTIPLIER |  | default | 2 | Does nothing |
| `093F` | IS_FIRE_BUTTON_PRESSED |  | default | 0 | Does nothing |
| `0940` | SET_GROUP_FOLLOW_STATUS | Group | default | 2 | Sets whether the group members enter a car when the leader does |
| `0941` | SET_SEARCHLIGHT_CLIP_IF_COLLIDING | Searchlight | default | 2 |  |
| `0942` | HAS_PLAYER_BOUGHT_ITEM | Shopping | default | 1 | Returns true if the shopping item has been bought |
| `0943` | SET_CAMERA_BEHIND_CHAR |  | default | 0 | Does nothing |
| `0944` | SET_CAMERA_IN_FRONT_OF_CHAR | Camera | default | 1 | Puts the camera in front of the specified character |
| `0945` | GET_PLAYER_MAX_ARMOUR | Player | default | 2 |  |
| `0946` | SET_CHAR_USES_UPPERBODY_DAMAGE_ANIMS_ONLY | Char | default | 2 |  |
| `0947` | SET_CHAR_SAY_CONTEXT | Char | default | 3 | Works similar to 05C1, but returns which phrase was spoken and is not run as a task |
| `0948` | ADD_EXPLOSION_VARIABLE_SHAKE | Fx | default | 5 | Creates an explosion at the specified coordinates |
| `0949` | ATTACH_MISSION_AUDIO_TO_CHAR | Audio | default | 2 | Sets the loaded audio to play at the char's location |
| `094A` | UPDATE_PICKUP_MONEY_PER_DAY | Pickup | default | 2 |  |
| `094B` | GET_NAME_OF_ENTRY_EXIT_CHAR_USED | Char | default | 2 | Gets the name of the characters interior |
| `094C` | GET_POSITION_OF_ENTRY_EXIT_CHAR_USED | Char | default | 5 | Returns the coordinates and heading of the entry (enex) marker the character used to get to the current interior |
| `094D` | IS_CHAR_TALKING | Char | default | 1 | Returns true if the character is playing any speech |
| `094E` | DISABLE_CHAR_SPEECH | Char | default | 2 | Prevents any character speech from playing |
| `094F` | ENABLE_CHAR_SPEECH | Char | default | 1 | Enables pain audio if it was disabled using 094E |
| `0950` | SET_UP_SKIP | Skip | default | 4 | Fades out the screen and teleports the player to the specified coordinates and angle |
| `0951` | CLEAR_SKIP | Skip | default | 0 |  |
| `0952` | PRELOAD_BEAT_TRACK | Audio | default | 1 | Loads the soundtrack audio that is stored in the audio\streams\BEATS file |
| `0953` | GET_BEAT_TRACK_STATUS | Audio | default | 1 | Returns the status of the currenly active beat track (0954) |
| `0954` | PLAY_BEAT_TRACK | Audio | default | 0 | Plays the last soundtrack loaded by PRELOAD_BEAT_TRACK |
| `0955` | STOP_BEAT_TRACK | Audio | default | 0 | Stops any currently active beat track |
| `0956` | FIND_MAX_NUMBER_OF_GROUP_MEMBERS | Game | default | 1 | Returns a number of group members the player can recruit with the current respect |
| `0957` | VEHICLE_DOES_PROVIDE_COVER | Car | default | 2 | Sets whether characters in combat will choose to use the vehicle as cover from gunfire |
| `0958` | CREATE_SNAPSHOT_PICKUP | Pickup | default | 4 | Creates a collectible snapshot at the specified coordinates |
| `0959` | CREATE_HORSESHOE_PICKUP | Pickup | default | 4 | Creates a collectible horseshoe at the specified coordinates |
| `095A` | CREATE_OYSTER_PICKUP | Pickup | default | 4 | Creates a collectible oyster at the specified coordinates |
| `095B` | HAS_OBJECT_BEEN_UPROOTED | Object | default | 1 | Returns true if the object has been made moveable by the 0392 |
| `095C` | ADD_SMOKE_PARTICLE | Fx | default | 12 |  |
| `095D` | IS_CHAR_STUCK_UNDER_CAR | Char | default | 1 | Returns true if the char is stuck under a car |
| `095E` | CONTROL_CAR_DOOR | Car | default | 4 | Sets the car's door angle and latch state |
| `095F` | GET_DOOR_ANGLE_RATIO | Car | default | 3 | Gets the specified car doors angle, relative to the hinge |
| `0960` | SET_PLAYER_DISPLAY_VITAL_STATS_BUTTON | Pad | default | 2 | Sets whether a player can use the ACTION key to display their stats |
| `0961` | SET_CHAR_KEEP_TASK | Char | default | 2 | Sets whether the character should keep their tasks after mission cleanup (basically cleanup will be skipped for this character) |
| `0962` | DOES_CAR_HAVE_ROOF |  | default | 0 | Does nothing |
| `0963` | SET_BLIP_FADE |  | default | 0 | Does nothing |
| `0964` | CREATE_MENU_GRID | MenuGrid | default | 9 | Creates the same color chart that you see in car modification shops |
| `0965` | IS_CHAR_SWIMMING | Char | default | 1 |  |
| `0966` | GET_CHAR_SWIM_STATE | Char | default | 2 |  |
| `0967` | START_CHAR_FACIAL_TALK | Char | default | 2 | Makes a character move their mouth as if they were talking |
| `0968` | STOP_CHAR_FACIAL_TALK | Char | default | 1 | Stops the character moving their mouth as if they were talking |
| `0969` | IS_BIG_VEHICLE | Car | default | 1 | Returns true if the specified vehicle has the 'is big' flag set in vehicles |
| `096A` | SWITCH_POLICE_HELIS | Game | default | 1 | Sets whether ghetto birds spawn |
| `096B` | STORE_CAR_MOD_STATE | Car | default | 0 |  |
| `096C` | RESTORE_CAR_MOD_STATE | Car | default | 0 |  |
| `096D` | GET_CURRENT_CAR_MOD | Car | default | 3 | Returns the model of the component installed on the specified slot of the vehicle, or -1 otherwise |
| `096E` | IS_CAR_LOW_RIDER | Car | default | 1 | Returns true if the vehicle is a low rider |
| `096F` | IS_CAR_STREET_RACER | Car | default | 1 | Returns true if the vehicle is a street racer |
| `0970` | FORCE_DEATH_RESTART | Game | default | 0 | Triggers usual after player death game bahavior (respawn in front of the hospital, weapons taken away, etc.) |
| `0971` | SYNC_WATER | World | default | 0 | Flattens water waves |
| `0972` | SET_CHAR_COORDINATES_NO_OFFSET | Char | default | 4 | Puts the characters at the coordinates by the center of body instead of the feet |
| `0973` | DOES_SCRIPT_FIRE_EXIST | ScriptFire | default | 1 | Returns true if the handle is a valid script fire handle |
| `0974` | RESET_STUFF_UPON_RESURRECTION | Game | default | 0 | Emulates the shared effects of being wasted or busted |
| `0975` | IS_EMERGENCY_SERVICES_VEHICLE | Car | default | 1 | Returns true if the vehicle is an emergency vehicle |
| `0976` | KILL_FX_SYSTEM_NOW | Particle | default | 1 | Destroys the specified particle |
| `0977` | IS_OBJECT_WITHIN_BRAIN_ACTIVATION_RANGE | Object | default | 1 | Returns true if the object is within the external script trigger radius |
| `0978` | COPY_SHARED_CHAR_DECISION_MAKER | DecisionMakerChar | default | 2 | Creates decision maker instance based on template. Adds itself to mission cleanup list. Otherwise should be released with REMOVE_DECISION_MAKER |
| `0979` | LOAD_SHARED_CHAR_DECISION_MAKER |  | default | 0 | Does nothing |
| `097A` | REPORT_MISSION_AUDIO_EVENT_AT_POSITION | Audio | default | 4 |  |
| `097B` | REPORT_MISSION_AUDIO_EVENT_AT_OBJECT | Audio | default | 2 |  |
| `097C` | ATTACH_MISSION_AUDIO_TO_OBJECT | Audio | default | 2 | Sets the loaded audio to play at the object's location |
| `097D` | GET_NUM_CAR_COLOURS | Car | default | 2 | Returns number of color variations defined for the model of this car in carcols.dat |
| `097E` | IS_POLICE_VEHICLE_IN_PURSUIT |  | default | 0 | Does nothing |
| `097F` | GET_CAR_COLOUR_FROM_MENU_INDEX |  | default | 0 | Does nothing |
| `0980` | EXTINGUISH_FIRE_AT_POINT | World | default | 4 | Removes all fires within the specified area |
| `0981` | HAS_TRAIN_DERAILED | Train | default | 1 | Returns true if the train has derailed (usually from going too fast) |
| `0982` | SET_CHAR_FORCE_DIE_IN_CAR | Char | default | 2 | Makes a character remain in the car upon death |
| `0983` | SET_ONLY_CREATE_GANG_MEMBERS | Game | default | 1 | Sets whether gangs appear everywhere, like when "Gangs control the streets" cheat is activated |
| `0984` | GET_OBJECT_MODEL | Object | default | 2 | Returns the object's model index |
| `0985` | SET_CHAR_USES_COLLISION_CLOSEST_OBJECT_OF_TYPE | World | default | 7 | Sets whether collision of the object closest to the given coordinates and matching the model applies to the target character |
| `0986` | CLEAR_ALL_SCRIPT_FIRE_FLAGS | World | default | 0 | Marks all fires as no longer needed, allowing them to disappear |
| `0987` | GET_CAR_BLOCKING_CAR | Car | default | 2 | Returns a handle of the vehicle preventing this car from getting to its destination |
| `0988` | GET_CURRENT_VEHICLE_PAINTJOB | Car | default | 2 | Gets the car's paintjob |
| `0989` | SET_HELP_MESSAGE_BOX_SIZE | Text | default | 1 | Sets the global width of text boxes displayed on screen |
| `098A` | SET_GUNSHOT_SENSE_RANGE_FOR_RIOT2 | Game | default | 1 |  |
| `098B` | STRING_CAT16 |  | default | 3 | Combines two null-terminated strings and stores the result to a string variable. The final string can not exceed 16 characters |
| `098C` | STRING_CAT8 |  | default | 3 | Combines two null-terminated strings and stores the result to a string variable. The final string can not exceed 8 characters |
| `098D` | GET_CAR_MOVING_COMPONENT_OFFSET | Car | default | 2 | Sets the angle of a vehicle's extra |
| `098E` | SET_NAMED_ENTRY_EXIT_FLAG | Game | default | 3 | Sets the specified enex flag |
| `098F` | RADIANS_TO_DEGREES |  | default | 0 | Does nothing |
| `0990` | DEGREES_TO_RADIANS |  | default | 0 | Does nothing |
| `0991` | PAUSE_CURRENT_BEAT_TRACK | Audio | default | 1 | Sets whether the loaded soundtrack is paused |
| `0992` | SET_PLAYER_CYCLE_WEAPON_BUTTON | Pad | default | 2 |  |
| `0993` | SET_CHAR_AIR_RESISTANCE_MULTIPLIER |  | default | 0 | Does nothing |
| `0994` | MARK_ROAD_NODE_AS_DONT_WANDER | Path | default | 3 |  |
| `0995` | UNMARK_ALL_ROAD_NODES_AS_DONT_WANDER | Path | default | 0 |  |
| `0996` | SET_CHECKPOINT_HEADING | Checkpoint | default | 2 |  |
| `0997` | SET_MISSION_RESPECT_TOTAL | Stat | default | 1 | Sets the total value of mission respect points (stat 228) |
| `0998` | AWARD_PLAYER_MISSION_RESPECT | Stat | default | 1 | Increments the earned mission respect points (stat 224) by the given value |
| `0999` | SET_PLAYER_FIRE_WITH_SHOULDER_BUTTON |  | default | 0 | Does nothing |
| `099A` | SET_CAR_COLLISION | Car | default | 2 |  |
| `099B` | CHANGE_PLAYBACK_TO_USE_AI | Car | default | 1 | Changes vehicle control from playback to AI driven |
| `099C` | CAMERA_SET_SHAKE_SIMULATION_SIMPLE | Camera | default | 3 | Jiggles the camera in a variety of different ways |
| `099D` | IS_NIGHT_VISION_ACTIVE | Game | default | 0 | Returns true if night vision is active |
| `099E` | SET_CREATE_RANDOM_COPS | Game | default | 1 |  |
| `099F` | TASK_SET_IGNORE_WEAPON_RANGE_FLAG | Task | default | 2 |  |
| `09A0` | TASK_PICK_UP_SECOND_OBJECT | Task | default | 10 |  |
| `09A1` | DROP_SECOND_OBJECT | Char | default | 2 |  |
| `09A2` | REMOVE_OBJECT_ELEGANTLY | Object | default | 1 | Fades the object out of existence, freeing game memory |
| `09A3` | DRAW_CROSSHAIR | Hud | default | 1 | Sets whether the HUD should always display weapon aiming crosshairs, used in the mission 'Catalyst' where the player must throw crates of ammo to Ryder |
| `09A4` | SET_UP_CONVERSATION_NODE_WITH_SPEECH | Conversation | default | 6 | Specifies the dialogue GXT's and audio ID's |
| `09A5` | SET_CCTV_EFFECT |  | default | 0 | Does nothing |
| `09A6` | SHOW_BLIPS_ON_ALL_LEVELS | Game | default | 1 | Enables entity blips showing on the radar and map while in interiors |
| `09A7` | SET_CHAR_DRUGGED_UP | Char | default | 2 |  |
| `09A8` | IS_CHAR_HEAD_MISSING | Char | default | 1 | Returns true if the character has had its head shot off |
| `09A9` | GET_HASH_KEY | Text | default | 2 | Returns the CRC hash of the input string |
| `09AA` | SET_UP_CONVERSATION_END_NODE_WITH_SPEECH | Conversation | default | 2 | Sets the speech sound for the specified conversation response node |
| `09AB` | RANDOM_PASSENGER_SAY | Car | default | 2 | Makes a passenger in the vehicle speak from an ambient speech ID, if one exists for the character |
| `09AC` | HIDE_ALL_FRONTEND_BLIPS | Game | default | 1 |  |
| `09AD` | SET_PLAYER_IN_CAR_CAMERA_MODE | Camera | default | 1 | Changes the camera mode on the current vehicle, just like when the user presses the 'change view' key |
| `09AE` | IS_CHAR_IN_ANY_TRAIN | Char | default | 1 | Returns true if the specified character is in a train |
| `09AF` | SET_UP_SKIP_AFTER_MISSION | Skip | default | 4 | Fades the screen out and teleports the player to the specified coordinates and angle |
| `09B0` | SET_VEHICLE_IS_CONSIDERED_BY_PLAYER | Car | default | 2 | Makes player character ignore the car when enter vehicle key is used |
| `09B1` | GET_CPU_LEVEL |  | default | 0 | Does nothing |
| `09B2` | GET_RANDOM_CAR_MODEL_IN_MEMORY | Streaming | default | 3 |  |
| `09B3` | GET_CAR_DOOR_LOCK_STATUS | Car | default | 2 | Returns the door lock mode of the vehicle |
| `09B4` | SET_CLOSEST_ENTRY_EXIT_FLAG | World | default | 5 | This command is like 098E, except it finds the appropriate enex marker via its position instead of its name |
| `09B5` | SET_CHAR_SIGNAL_AFTER_KILL | Char | default | 2 | Sets whether the character signals after killing |
| `09B6` | SET_CHAR_WANTED_BY_POLICE | Char | default | 2 | Sets whether police should chase the character |
| `09B7` | SET_ZONE_NO_COPS | Zone | default | 2 | Sets whether cops should be prevented from spawning in the specified area |
| `09B8` | ADD_BLOOD | Fx | default | 8 | Creates blood spray and ground splatter effects |
| `09B9` | DISPLAY_CAR_NAMES | Hud | default | 1 | Sets whether the name of the current vehicle should be displayed |
| `09BA` | DISPLAY_ZONE_NAMES | Hud | default | 1 | Sets whether the area text for the current area should show |
| `09BB` | IS_CAR_DOOR_DAMAGED | Car | default | 2 | Returns true if the specified vehicle part is visibly damaged |
| `09BC` | SET_CHAR_COORDINATES_DONT_WARP_GANG_NO_OFFSET | Char | default | 4 | This command is a combination of 0972 and 08C7 |
| `09BD` | SET_MINIGAME_IN_PROGRESS | Game | default | 1 | Disables displaying help messages in other scripts |
| `09BE` | IS_MINIGAME_IN_PROGRESS | Game | default | 0 | Returns true if 09BD has been used in any script to disable help messages |
| `09BF` | SET_FORCE_RANDOM_CAR_MODEL | Game | default | 1 | Forces all cars spawned to be of the specified model |
| `09C0` | GET_RANDOM_CAR_OF_TYPE_IN_ANGLED_AREA_NO_SAVE | World | default | 7 |  |
| `09C1` | ADD_NEXT_MESSAGE_TO_PREVIOUS_BRIEFS | Text | default | 1 | Sets whether the next text is added to the brief in the menu |
| `09C2` | FAIL_KILL_FRENZY | KillFrenzy | default | 0 | Cancels current rampage, setting the rampage status to failed |
| `09C3` | IS_COP_VEHICLE_IN_AREA_3D_NO_SAVE | World | default | 6 | Returns true if there's any kind of police vehicle in the specified 3D area |
| `09C4` | SET_PETROL_TANK_WEAKPOINT | Car | default | 2 | Sets whether the car can be blown up by shooting at the petrol tank |
| `09C5` | IS_CHAR_USING_MAP_ATTRACTOR | Char | default | 1 | Returns true if the character is using a map attractor |
| `09C6` | SET_ALL_CARS_IN_AREA_VISIBLE |  | default | 0 | Does nothing |
| `09C7` | SET_PLAYER_MODEL | Player | default | 2 | Changes the player to use the specified model |
| `09C8` | ARE_SUBTITLES_SWITCHED_ON | Game | default | 0 | Returns true if subtitles are switched on in the settings menu |
| `09C9` | REMOVE_CHAR_FROM_CAR_MAINTAIN_POSITION | Char | default | 2 | Removes the character from the vehicle |
| `09CA` | SET_OBJECT_PROOFS | Object | default | 6 | Sets what immunities the object has |
| `09CB` | IS_CAR_TOUCHING_CAR | Car | default | 2 | Returns true if the car is touching the other car |
| `09CC` | DOES_OBJECT_HAVE_THIS_MODEL | Object | default | 2 | Returns true if the object's model is the model specified |
| `09CD` | IS_ITALIAN_GAME |  | default | 0 |  |
| `09CE` | IS_SPANISH_GAME |  | default | 0 |  |
| `09CF` | SET_TRAIN_FORCED_TO_SLOW_DOWN | Train | default | 2 | Sets whether the train should stop at each station it encounters |
| `09D0` | IS_VEHICLE_ON_ALL_WHEELS | Car | default | 1 | Returns true if all the vehicle's wheels are touching the ground |
| `09D1` | DOES_PICKUP_EXIST | Pickup | default | 1 | Returns true if the handle is a valid pickup handle |
| `09D2` | ENABLE_AMBIENT_CRIME | Game | default | 1 | Sets whether cops will chase and kill criminals when their task is 'TASK_COMPLEX_KILL_CRIMINAL' |
| `09D3` | IS_AMBIENT_CRIME_ENABLED |  | default | 0 | Does nothing |
| `09D4` | CLEAR_WANTED_LEVEL_IN_GARAGE | Game | default | 0 | Suspends the current players wanted level |
| `09D5` | SET_CHAR_SAY_CONTEXT_IMPORTANT | Char | default | 6 |  |
| `09D6` | SET_CHAR_SAY_SCRIPT | Char | default | 5 |  |
| `09D7` | FORCE_INTERIOR_LIGHTING_FOR_PLAYER | Player | default | 2 |  |
| `09D8` | DISABLE_2ND_PAD_FOR_DEBUG |  | default | 1 | Does nothing |
| `09D9` | USE_DETONATOR | Player | default | 0 | Detonates all satchel charges and car bombs planted by the player |
| `09DA` | IS_MONEY_PICKUP_AT_COORDS | World | default | 3 | Returns true if a money pickup exists near the specified coordinates |
| `09DB` | SET_MENU_COLUMN_WIDTH | Menu | default | 3 | Sets the width of the specified menu column |
| `09DC` | SET_CHAR_CAN_CLIMB_OUT_WATER |  | default | 0 | Does nothing |
| `09DD` | MAKE_ROOM_IN_PLAYER_GANG_FOR_MISSION_PEDS | Game | default | 1 | Ensures there is x amount of space for new members to be added to the players gang |
| `09DE` | IS_CHAR_GETTING_IN_TO_A_CAR | Char | default | 1 | Returns true if the character is entering a car, but is not in the car |
| `09DF` | RESTORE_PLAYER_AFTER_2P_GAME |  | default | 0 |  |
| `09E0` | SET_UP_SKIP_FOR_SPECIFIC_VEHICLE | Skip | default | 5 | Teleports the player to the specified coordinates and sets the specified angle when in the specified car |
| `09E1` | GET_CAR_MODEL_VALUE | Car | default | 2 | Returns the value of the specified car model |
| `09E2` | CREATE_CAR_GENERATOR_WITH_PLATE | CarGenerator | default | 14 | Creates a parked car generator with a number plate (modelId -1 selects a random vehicle from the local popcycle) |
| `09E3` | FIND_TRAIN_DIRECTION | Train | default | 1 | Returns true if the train is travelling clockwise, around San Andreas |
| `09E4` | SET_AIRCRAFT_CARRIER_SAM_SITE | Game | default | 1 | Enables missiles to be fired from the aircraft carrier by Easter Bay Naval Station, San Fierro |
| `09E5` | DRAW_LIGHT_WITH_RANGE | Fx | default | 7 | Draws colored light in radius of the specified point |
| `09E6` | ENABLE_BURGLARY_HOUSES | Game | default | 1 | Switches enex markers used for burglary missions on or off |
| `09E7` | IS_PLAYER_CONTROL_ON | Player | default | 1 | Returns true if the player control hasn't been disabled using 01B4 |
| `09E8` | GET_CHAR_AREA_VISIBLE | Char | default | 2 | Returns the interior ID that the character is in |
| `09E9` | GIVE_NON_PLAYER_CAR_NITRO | Car | default | 1 | Makes the car have one nitro |
| `09EA` | PLAYER_PUT_ON_GOGGLES |  | default | 0 | Does nothing |
| `09EB` | PLAYER_TAKE_OFF_GOGGLES | Player | default | 2 | Removes the players Goggles and disables night/heat vision |
| `09EC` | ALLOW_FIXED_CAMERA_COLLISION | Camera | default | 1 | Makes the camera remain behind the player when in any garage |
| `09ED` | HAS_CHAR_SPOTTED_CHAR_IN_FRONT | Char | default | 2 | Returns true if the character can see the other character in front of them |
| `09EE` | FORCE_BIG_MESSAGE_AND_COUNTER | Hud | default | 1 | Prevents timers and big texts from being hidden if there is another conflicting type of text on screen |
| `09EF` | SET_VEHICLE_CAMERA_TWEAK | Camera | default | 4 | Sets the position the camera automatically moves to while driving a vehicle of the specified type |
| `09F0` | RESET_VEHICLE_CAMERA_TWEAK | Camera | default | 0 | Resets any changes made with 09EF |
| `09F1` | REPORT_MISSION_AUDIO_EVENT_AT_CHAR | Audio | default | 2 |  |
| `09F2` | DOES_DECISION_MAKER_EXIST | DecisionMaker | default | 1 | Returns true if the handle is a valid decision maker handle |
| `09F3` | GET_RANDOM_TRAIN_IN_SPHERE_NO_SAVE |  | default | 0 | Does nothing |
| `09F4` | IGNORE_HEIGHT_DIFFERENCE_FOLLOWING_NODES | Char | default | 2 |  |
| `09F5` | SHUT_ALL_CHARS_UP | Game | default | 1 | Prevents all peds from attempting to start conversations with the player |
| `09F6` | SET_CHAR_GET_OUT_UPSIDE_DOWN_CAR | Char | default | 2 | Controls whether the character will try to exit an upside-down car until it is on fire |
| `09F7` | REPORT_MISSION_AUDIO_EVENT_AT_CAR | Audio | default | 2 | Plays the audio event at the car's position |
| `09F8` | DO_WEAPON_STUFF_AT_START_OF_2P_GAME | Game | default | 0 | Gives all the weapons of player 1 to player 2 during a cooperative mission |
| `09F9` | SET_MENU_HEADER_ORIENTATION |  | default | 0 | Does nothing |
| `09FA` | HAS_GAME_JUST_RETURNED_FROM_FRONTEND | Game | default | 0 | Returns true if the player just exited the menu on the last frame |
| `09FB` | GET_CURRENT_LANGUAGE | Game | default | 1 | Returns the current language set in the menu language settings |
| `09FC` | IS_OBJECT_INTERSECTING_WORLD | Object | default | 1 | Appears to return true if something had entered the object's position since it was created or its position was changed |
| `09FD` | GET_STRING_WIDTH | Text | default | 2 | Gets the width of the GXT entry string |
| `09FE` | RESET_VEHICLE_HYDRAULICS | Car | default | 1 | This resets all the hydraulics on the car, making it "sit" |
| `09FF` | SET_RESPAWN_POINT_FOR_DURATION_OF_MISSION | Restart | default | 3 | Overrides the respawn point |
| `0A00` | IS_THIS_MODEL_A_BIKE |  | default | 0 | Does nothing |
| `0A01` | IS_THIS_MODEL_A_CAR | Streaming | default | 1 | Returns true if a valid car model is passed |
| `0A02` | SWITCH_ON_GROUND_SEARCHLIGHT | Searchlight | default | 2 | Sets whether the searchlight shows a shadow effect on the surface it hits |
| `0A03` | IS_GANG_WAR_FIGHTING_GOING_ON | Game | default | 0 | Returns true if the player provoked a gang war or is defending territory |
| `0A04` | SET_VEHICLE_FIRING_RATE_MULTIPLIER |  | default | 0 | Does nothing |
| `0A05` | GET_VEHICLE_FIRING_RATE_MULTIPLIER |  | default | 0 | Does nothing |
| `0A06` | IS_NEXT_STATION_ALLOWED | Train | default | 1 | Returns true if the next station is accessible (at the start of the game, railroad blocks prevent the player from travelling to stations whose area is not unlocked) |
| `0A07` | SKIP_TO_NEXT_ALLOWED_STATION | Train | default | 1 | Puts the script created train at the next allowed station |
| `0A08` | GET_STRING_WIDTH_WITH_NUMBER | Text | default | 3 | Gets the width of the GXT entry string with the specified number |
| `0A09` | SHUT_CHAR_UP_FOR_SCRIPTED_SPEECH | Char | default | 2 | Works similar to 0489, but mutes more things, including ambient speeches (needs confirming) |
| `0A0A` | ENABLE_DISABLED_ATTRACTORS_ON_OBJECT | Object | default | 2 | Sets whether the object attracts spawned peds to interact with it |
| `0A0B` | LOAD_SCENE_IN_DIRECTION | Streaming | default | 4 |  |
| `0A0C` | IS_PLAYER_USING_JETPACK | Player | default | 1 | Returns true if player is using a jetpack |
| `0A0D` | BLOCK_VEHICLE_MODEL |  | default | 0 | Does nothing |
| `0A0E` | CLEAR_THIS_PRINT_BIG_NOW | Text | default | 1 | Removes the print big text with the specified style from the screen |
| `0A0F` | HAS_LANGUAGE_CHANGED | Game | default | 0 | Returns true if the current language set is different from the previous language set |
| `0A10` | INCREMENT_INT_STAT_NO_MESSAGE | Stat | default | 2 | Increases the integer stat by the value given without displaying popup message |
| `0A11` | SET_EXTRA_CAR_COLOURS | Car | default | 3 | Sets the car's ternary and quaternary colors. See also 0229 |
| `0A12` | GET_EXTRA_CAR_COLOURS | Car | default | 3 | Returns the car's tertiary and quaternary colors. See also 03F3 |
| `0A13` | MANAGE_ALL_POPULATION | Game | default | 0 | Deletes distant, no longer needed, objects and world dummy objects |
| `0A14` | SET_NO_RESPRAYS | Game | default | 1 | Disables respray garages from opening for the player |
| `0A15` | HAS_CAR_BEEN_RESPRAYED | Car | default | 1 | Returns true if the vehicle was resprayed in the last frame AND resets the resprayed state to false |
| `0A16` | ATTACH_MISSION_AUDIO_TO_CAR | Audio | default | 2 | Sets the loaded audio to play at the vehicle's location |
| `0A17` | SET_HAS_BEEN_OWNED_FOR_CAR_GENERATOR | CarGenerator | default | 2 | Sets whether the player will not receive a wanted level when entering a vehicle from this generator when the police is around |
| `0A18` | SET_UP_CONVERSATION_NODE_WITH_SCRIPTED_SPEECH | Conversation | default | 6 | Adds a new line to the scripted conversation |
| `0A19` | SET_AREA_NAME | Text | default | 1 | Displays the text of the specified GXT entry using San Andreas' area name text style |
| `0A1A` | TASK_PLAY_ANIM_SECONDARY | Task | default | 9 | Makes a character play an animation that affects only the upper half of their body |
| `0A1B` | IS_CHAR_TOUCHING_CHAR | Char | default | 2 | Returns true if the character is touching the other character |
| `0A1C` | DISABLE_HELI_AUDIO | Heli | default | 2 | Sets whether the helicopter sound is muted |
| `0A1D` | TASK_HAND_GESTURE | Task | default | 2 | Makes a character face the other character and make a gesture |
| `0A1E` | TAKE_PHOTO | Camera | default | 1 | Takes a screenshot of the screen without any HUD elements and stores the file in the "GTA San Andreas User FilesGallery" folder |
| `0A1F` | INCREMENT_FLOAT_STAT_NO_MESSAGE | Stat | default | 2 | Increases the float stat by the value given without displaying popup message |
| `0A20` | SET_PLAYER_GROUP_TO_FOLLOW_ALWAYS | Player | default | 2 | Controls the players ability to tell their group to wait and automatically orders any group members to continue following |
| `0A21` | IMPROVE_CAR_BY_CHEATING | Car | default | 2 | Sets whether a ped driven vehicle's handling is affected by the 'perfect handling' cheat |
| `0A22` | CHANGE_CAR_COLOUR_FROM_MENU | Menu | default | 4 |  |
| `0A23` | HIGHLIGHT_MENU_ITEM | Menu | default | 3 | Highlights the menu item - used to indicate an owned shopping item |
| `0A24` | SET_DISABLE_MILITARY_ZONES | Zone | default | 1 | Causes the players wanted level to be set at 4 when in restricted areas |
| `0A25` | SET_CAMERA_POSITION_UNFIXED | Camera | default | 2 | Sets the position of the camera to an offset of the targeted entity |
| `0A26` | SET_RADIO_TO_PLAYERS_FAVOURITE_STATION | Audio | default | 0 | Sets the radio station of the vehicle the player is currently in to the favourite station, retrieved from the stats (ID 326) |
| `0A27` | SET_DEATH_WEAPONS_PERSIST | Char | default | 2 | Prevents pickups, which are created when this character dies, from disappearing until picked up by the player |
| `0A28` | SET_SWIM_SPEED | Char | default | 2 | Sets the speed that the character swims at, changing their swimming animation speed |
| `0A29` | IS_PLAYER_CLIMBING | Player | default | 1 | Returns true if the player is climbing |
| `0A2A` | IS_THIS_HELP_MESSAGE_BEING_DISPLAYED | Text | default | 1 | Returns true if a help message with the specified GXT entry is being displayed |
| `0A2B` | IS_WIDESCREEN_ON_IN_OPTIONS | Game | default | 0 | Returns true if widescreen is switched on in the display settings |
| `0A2C` | DRAW_SUBTITLES_BEFORE_FADE | Text | default | 1 | Sets whether the text stays on the screen when it fades out |
| `0A2D` | DRAW_ODDJOB_TITLE_BEFORE_FADE | Text | default | 1 | Sets whether the styled text stays on the screen when it fades out |
| `0A2E` | TASK_FOLLOW_PATH_NODES_TO_COORD_WITH_RADIUS | Task | default | 7 | Makes the specified character run in panic to the specified position |
| `0A2F` | SET_PHOTO_CAMERA_EFFECT | Camera | default | 1 | Puts the camera in first-person mode if the player is holding a weapon with a first-person shooting mode (such as a sniper rifle or camera) |
| `0A30` | FIX_CAR | Car | default | 1 | Restores the vehicle to full health and removes the damage |
| `0A31` | SET_PLAYER_GROUP_TO_FOLLOW_NEVER | Player | default | 2 | Sets whether the player's group stops following the player, even if the player uses the "group follow" button |
| `0A32` | IS_CHAR_ATTACHED_TO_ANY_CAR | Char | default | 1 | Returns true if the char is turreted on any vehicle |
| `0A33` | STORE_CAR_CHAR_IS_ATTACHED_TO_NO_SAVE | Char | default | 2 | Returns the vehicle the character is attached to |
| `0A34` | SET_UP_SKIP_TO_BE_FINISHED_BY_SCRIPT |  | default | 0 | Does nothing |
| `0A35` | SET_UP_SKIP_FOR_VEHICLE_FINISHED_BY_SCRIPT | Skip | default | 5 | Teleports the player to the specified coordinates and sets the specified angle with the screen fading in when in the specified car |
| `0A36` | IS_SKIP_WAITING_FOR_SCRIPT_TO_FADE_IN | Skip | default | 0 | Returns true if the trip skip created with 0A35 has finished teleporting the vehicle and is ready to allow the script to fade in |
| `0A37` | FORCE_ALL_VEHICLE_LIGHTS_OFF | Game | default | 1 | Disables all vehicle lights from being rendered if enabled |
| `0A38` | SET_RENDER_PLAYER_WEAPON |  | default | 0 | Does nothing |
| `0A39` | GET_PLAYER_IN_CAR_CAMERA_MODE | Camera | default | 1 | Gets the players chosen camera mode of the current vehicle |
| `0A3A` | IS_LAST_BUILDING_MODEL_SHOT_BY_PLAYER | Player | default | 2 | Returns true if the player's last shot model is the model specified |
| `0A3B` | CLEAR_LAST_BUILDING_MODEL_SHOT_BY_PLAYER | Player | default | 1 | Resets the status of the last model the player has shot |
| `0A3C` | SET_UP_CONVERSATION_END_NODE_WITH_SCRIPTED_SPEECH | Conversation | default | 2 | Sets the script audio ID (see 03CF) for the specified conversation response node |
| `0A3D` | ACTIVATE_PIMP_CHEAT | Game | default | 1 | Sets whether sleeping with a prostitute earns you money instead of taking it away from you |
| `0A3E` | GET_RANDOM_CHAR_IN_AREA_OFFSET_NO_SAVE | World | default | 7 | Returns the first char in the ped pool within radius of the specified point |
| `0A3F` | SET_SCRIPT_COOP_GAME | Game | default | 1 | Sets an unused flag at address 0x96A8A8 |
| `0A40` | CREATE_USER_3D_MARKER | User3DMarker | default | 5 | Creates a marker similar to the yellow enex markers |
| `0A41` | REMOVE_USER_3D_MARKER | User3DMarker | default | 1 | Destroys a marker created with 0A40 |
| `0A42` | REMOVE_ALLUSER_3D_MARKERS |  | default | 0 | Does nothing |
| `0A43` | GET_RID_OF_PLAYER_PROSTITUTE | Game | default | 0 | Cancels any prostitute invitations received in-game and makes any current prostitutes quit |
| `0A44` | DISPLAY_NON_MINIGAME_HELP_MESSAGES | Text | default | 1 | Overrides the text block set by 09BD |
| `0A45` | SET_RAILTRACK_RESISTANCE_MULT | World | default | 1 | Sets the friction/slowdown rate on all rail tracks |
| `0A46` | SWITCH_OBJECT_BRAINS | Game | default | 2 | Enables or disables all object triggers with the specified grouping id (set with 0929) |
| `0A47` | FINISH_SETTING_UP_CONVERSATION_NO_SUBTITLES | Conversation | default | 0 | Finalizes the current conversation sequence started with 0717. Selected answers will not be subtitled |
| `0A48` | ALLOW_PAUSE_IN_WIDESCREEN | Game | default | 1 | Enables the player to access the pause menu while widescreen is enabled |
| `0A49` | IS_XBOX_VERSION |  | default | 0 | Returns true for Xbox versions of the game |
| `0A4A` | GET_PC_MOUSE_MOVEMENT | Mouse | default | 2 | Gives the offset of the mouse or right thumbstick movement |
| `0A4B` | IS_PC_USING_JOYPAD | Game | default | 0 | Returns true if players controls are set to joystick and not mouse+keyboard |
| `0A4C` | IS_MOUSE_USING_VERTICAL_INVERSION | Mouse | default | 0 | Returns true if the players settings are set to invert the mouse |
| `0A4D` | IS_JAPANESE_VERSION |  | default | 0 | Returns true for Japanese versions of the game |
| `0A4E` | DO_DEBUG_STUFF |  | default | 0 | Increments an unused counter, likely used in the debug version of the game |
| `0A8C` | WRITE_MEMORY | Memory | CLEO | 4 | Writes the value at the memory address |
| `0A8D` | READ_MEMORY | Memory | CLEO | 4 | Reads a value from the game memory |
| `0A8E` | INT_ADD |  | CLEO | 3 | Adds together two integer values and writes the result into the variable |
| `0A8F` | INT_SUB |  | CLEO | 3 | Subtracts the integer value from another integer value and writes the result into the variable |
| `0A90` | INT_MUL |  | CLEO | 3 | Multiplies two integer values and writes the result into the variable |
| `0A91` | INT_DIV |  | CLEO | 3 | Divides the integer value by another integer value and writes the result into the variable |
| `0A92` | STREAM_CUSTOM_SCRIPT |  | CLEO | 2 | Loads a file with compiled SCM instructions at the given path and runs a new custom script |
| `0A93` | TERMINATE_THIS_CUSTOM_SCRIPT |  | CLEO | 0 | Ends the current custom script, preventing further execution |
| `0A94` | LOAD_AND_LAUNCH_CUSTOM_MISSION |  | CLEO | 2 |  |
| `0A95` | SAVE_THIS_CUSTOM_SCRIPT |  | CLEO | 0 | Marks this script to be saved whenever game is saved. After savegame load all local variables are restored and execution continues from saved position |
| `0A96` | GET_PED_POINTER | Memory | CLEO | 2 | Gets the address of the ped struct in the game memory by its handle |
| `0A97` | GET_VEHICLE_POINTER | Memory | CLEO | 2 | Gets the address of the vehicle struct in the game memory by its handle |
| `0A98` | GET_OBJECT_POINTER | Memory | CLEO | 2 | Gets the address of the object struct in the game memory by its handle |
| `0A99` | SET_CURRENT_DIRECTORY | Fs | CLEO | 1 | Sets the current working directory (cwd) to a predefined location with a value of 0 or 1, or to an arbitrary path with a string value |
| `0A9A` | OPEN_FILE | File | CLEO | 3 | Opens the file in the specified mode, sets the condition result to True if the open operation has been successful, or to False otherwise, and writes the file handle to the variable |
| `0A9B` | CLOSE_FILE | File | CLEO | 1 | Closes the file and frees the memory |
| `0A9C` | GET_FILE_SIZE | File | CLEO | 2 | Gets the file size in bytes |
| `0A9D` | READ_FROM_FILE | File | CLEO | 3 | Reads the specified number of bytes from the opened file and writes them to the memory region starting from the address of the destination variable |
| `0A9E` | WRITE_TO_FILE | File | CLEO | 3 | Copies the specified number of bytes of the memory region starting from the address of the source variable to the file |
| `0A9F` | GET_THIS_SCRIPT_STRUCT | Memory | CLEO | 1 | Gets the address of the current script structure in the game memory |
| `0AA0` | GOSUB_IF_FALSE |  | CLEO | 1 | Transfers the script execution to the label as a subroutine if the result of the condition is false |
| `0AA1` | RETURN_IF_FALSE |  | CLEO | 0 | Returns from the current subroutine if the result of the condition is false |
| `0AA2` | LOAD_DYNAMIC_LIBRARY | DynamicLibrary | CLEO | 2 | Loads the specified module (usually a dynamic-link library (DLL)) into the address space of the game |
| `0AA3` | FREE_DYNAMIC_LIBRARY | DynamicLibrary | CLEO | 1 | Frees the loaded dynamic-link library (DLL) module and unloads it from the address space of the game |
| `0AA4` | GET_DYNAMIC_LIBRARY_PROCEDURE | DynamicLibrary | CLEO | 3 | Retrieves the address of an exported function or variable from the specified dynamic-link library (DLL) |
| `0AA5` | CALL_FUNCTION | Memory | CLEO | 4 | Calls a function at the address with the given arguments and the calling convention defined by the pop parameter where 0 means 'stdcall' and a value equal to numParams means  'cdecl' |
| `0AA6` | CALL_METHOD | Memory | CLEO | 5 | Calls a method of the object (struct) with the given arguments and the 'thiscall' calling convention (pop is always 0) |
| `0AA7` | CALL_FUNCTION_RETURN | Memory | CLEO | 5 | Calls a function similarly to 0AA5 and writes the result into the variable following the arguments list |
| `0AA8` | CALL_METHOD_RETURN | Memory | CLEO | 6 | Calls a method of the object (struct) similarly to 0AA6 and writes the result into the variable following the arguments list |
| `0AA9` | IS_GAME_VERSION_ORIGINAL | Game | CLEO | 0 | Returns true if the game version is vanilla 1.0 |
| `0AAA` | GET_SCRIPT_STRUCT_NAMED | Memory | CLEO | 2 | Gets the address of a running script which name matches the given string or 0 otherwise |
| `0AAB` | DOES_FILE_EXIST | Fs | CLEO | 1 | Returns true if a file at the given path exists |
| `0AAC` | LOAD_AUDIO_STREAM | AudioStream | audio | 2 | Loads an audio file and creates a new audio stream (see 0AC1) |
| `0AAD` | SET_AUDIO_STREAM_STATE | AudioStream | audio | 2 | Sets the state of the audio stream |
| `0AAE` | REMOVE_AUDIO_STREAM | AudioStream | audio | 1 | Unloads the audio stream and frees the memory |
| `0AAF` | GET_AUDIO_STREAM_LENGTH | AudioStream | audio | 2 | Gets the audio stream length in seconds |
| `0AB0` | IS_KEY_PRESSED | Pad | CLEO | 1 | Returns true if the player is pressing a keyboard button with the specified code |
| `0AB1` | CLEO_CALL |  | CLEO | 3 | Starts the execution of the SCM function with given params, optionally receiving one or more numbers as the result. Return from function is performed with 0051, 0AB2, or 2002 |
| `0AB2` | CLEO_RETURN |  | CLEO | 2 | Returns the flow of the execution to the last CLEO_CALL instruction, optionally returning one or more numbers as the result |
| `0AB3` | SET_CLEO_SHARED_VAR |  | CLEO | 2 | Sets the value of an element in the global array maintained by CLEO (index is between 0-1023) |
| `0AB4` | GET_CLEO_SHARED_VAR |  | CLEO | 2 | Reads the value of an element in the global array maintained by CLEO (index is between 0-1023) |
| `0AB5` | STORE_CLOSEST_ENTITIES | Char | CLEO | 3 | Stores the handles of a vehicle and ped closest to the char or -1 otherwise. Ignores script created entities |
| `0AB6` | GET_TARGET_BLIP_COORDS | World | CLEO | 3 | Gets the coordinates of the location targeted in the game map |
| `0AB7` | GET_CAR_NUMBER_OF_GEARS | Car | CLEO | 2 | Gets the total number of gears of the vehicle and stores it to the variable |
| `0AB8` | GET_CAR_CURRENT_GEAR | Car | CLEO | 2 | Returns the current gear of the vehicle |
| `0AB9` | GET_AUDIO_STREAM_STATE | AudioStream | audio | 2 | Returns the state of the audio stream |
| `0ABA` | TERMINATE_ALL_CUSTOM_SCRIPTS_WITH_THIS_NAME |  | CLEO | 1 | Ends the custom CLEO scripts with the specified name, freeing game memory |
| `0ABB` | GET_AUDIO_STREAM_VOLUME | AudioStream | audio | 2 | Returns the audio stream volume (from 0.0 to 1.0) |
| `0ABC` | SET_AUDIO_STREAM_VOLUME | AudioStream | audio | 2 | Sets the audio stream volume (default is 1.0). Pauses/Starts stream playback if neccesarry |
| `0ABD` | IS_CAR_SIREN_ON | Car | CLEO | 1 |  |
| `0ABE` | IS_CAR_ENGINE_ON | Car | CLEO | 1 |  |
| `0ABF` | CLEO_SET_CAR_ENGINE_ON | Car | CLEO | 2 | Sets whether the vehicle's engine is turned on or off |
| `0AC0` | SET_AUDIO_STREAM_LOOPED | AudioStream | audio | 2 | Makes the audio stream repeat endlessly |
| `0AC1` | LOAD_3D_AUDIO_STREAM | AudioStream3D | audio | 2 | Loads an audio file and creates a new 3d audio stream (see 0AAC) |
| `0AC2` | SET_PLAY_3D_AUDIO_STREAM_AT_COORDS | AudioStream3D | audio | 4 | Sets sound source position to specific world location |
| `0AC3` | SET_PLAY_3D_AUDIO_STREAM_AT_OBJECT | AudioStream3D | audio | 2 | Attaches sound source to the object |
| `0AC4` | SET_PLAY_3D_AUDIO_STREAM_AT_CHAR | AudioStream3D | audio | 2 | Attaches sound source to the character |
| `0AC5` | SET_PLAY_3D_AUDIO_STREAM_AT_CAR | AudioStream3D | audio | 2 | Attaches sound source to the vehicle |
| `0AC6` | GET_LABEL_POINTER | Memory | CLEO | 2 | Stores the absolute address of a code location marked with the label |
| `0AC7` | GET_VAR_POINTER | Memory | CLEO | 2 | Stores the absolute address of the variable |
| `0AC8` | ALLOCATE_MEMORY | Memory | CLEO | 2 | Allocates a chunk of memory of the given size and stores its address to the variable |
| `0AC9` | FREE_MEMORY | Memory | CLEO | 1 | Frees the memory allocated with 0AC8 |
| `0ACA` | PRINT_HELP_STRING | Text | CLEO | 1 | Displays a custom text (provided as a literal or an address) in a black box similarly to PRINT_HELP |
| `0ACB` | PRINT_BIG_STRING | Text | CLEO | 3 | Displays a custom text (provided as a literal or an address) similarly to PRINT_BIG |
| `0ACC` | PRINT_STRING | Text | CLEO | 2 | Displays a custom text (provided as a literal or an address) similarly to PRINT |
| `0ACD` | PRINT_STRING_NOW | Text | CLEO | 2 | Displays a custom text (provided as a literal or an address) similarly to PRINT_NOW |
| `0ACE` | PRINT_HELP_FORMATTED | Text | CLEO | 2 | Displays a black text box for a few seconds respecting the format of the String entered |
| `0ACF` | PRINT_BIG_FORMATTED | Text | CLEO | 4 | Formats args according to the format string, then displays it similarly to PRINT_BIG |
| `0AD0` | PRINT_FORMATTED | Text | CLEO | 3 | Formats args according to the format string, then displays it similarly to PRINT |
| `0AD1` | PRINT_FORMATTED_NOW | Text | CLEO | 3 | Formats args according to the format string, then displays it similarly to PRINT_NOW |
| `0AD2` | GET_CHAR_PLAYER_IS_TARGETING | Player | CLEO | 2 |  |
| `0AD3` | STRING_FORMAT | Text | CLEO | 3 | Formats a text according to the format string and given arguments and writes it in the result |
| `0AD4` | SCAN_STRING | Text | CLEO | 4 | Extracts data from a string using sscanf |
| `0AD5` | FILE_SEEK | File | CLEO | 3 | Sets the position of the file to the given offset from the origin |
| `0AD6` | IS_END_OF_FILE_REACHED | File | CLEO | 1 | Returns true if all data has been read or any file error occurred |
| `0AD7` | READ_STRING_FROM_FILE | File | CLEO | 3 | Reads up to maxLength-1 text characters from the file until the newline or the end-of-file is reached. Result will be null-terminated string |
| `0AD8` | WRITE_STRING_TO_FILE | File | CLEO | 2 | Copies data from the source string to the file up to but not including the null character |
| `0AD9` | WRITE_FORMATTED_STRING_TO_FILE | File | CLEO | 3 | Writes a formatted string to the file |
| `0ADA` | SCAN_FILE | File | CLEO | 4 | Extracts data from a file using fscanf |
| `0ADB` | GET_NAME_OF_VEHICLE_MODEL | Streaming | CLEO | 2 |  |
| `0ADC` | TEST_CHEAT | Pad | CLEO | 1 | Returns true if the specified string of letters has been typed on the keyboard |
| `0ADD` | SPAWN_VEHICLE_BY_CHEATING | World | CLEO | 1 | Creates a vehicle with the model (no pre-loading needed) in front of the player |
| `0ADE` | GET_TEXT_LABEL_STRING | Text | CLEO | 2 | Returns the text associated with the GXT key |
| `0ADF` | ADD_TEXT_LABEL | Text | CLEO | 2 | Adds or updates the text associated with the dynamic GXT key. It does nothing if the same key is defined in a FXT file |
| `0AE0` | REMOVE_TEXT_LABEL | Text | CLEO | 1 | Deletes the key and associated text created with ADD_TEXT_LABEL or defined in a FXT file |
| `0AE1` | GET_RANDOM_CHAR_IN_SPHERE_NO_SAVE_RECURSIVE | World | CLEO | 7 |  |
| `0AE2` | GET_RANDOM_CAR_IN_SPHERE_NO_SAVE_RECURSIVE | World | CLEO | 7 |  |
| `0AE3` | GET_RANDOM_OBJECT_IN_SPHERE_NO_SAVE_RECURSIVE | World | CLEO | 6 |  |
| `0AE4` | DOES_DIRECTORY_EXIST | Fs | CLEO | 1 | Returns true if a directory at the given path exists |
| `0AE5` | CREATE_DIRECTORY | Fs | CLEO | 1 | Creates a directory at the given path |
| `0AE6` | FIND_FIRST_FILE | FindFile | CLEO | 3 | Searches a directory for a file or subdirectory with a name that matches a specific name (or partial name if wildcards are used) |
| `0AE7` | FIND_NEXT_FILE | FindFile | CLEO | 2 | Continues a file search from a previous call to 0AE6 |
| `0AE8` | FIND_CLOSE | FindFile | CLEO | 1 | Closes a file search handle opened by 0AE6 |
| `0AE9` | POP_FLOAT | Memory | CLEO | 1 | Returns a floating-point number stored as the result of the function called (0AA5, 0AA6, 0AA7, 0AA8) immediately before this command |
| `0AEA` | GET_PED_REF | Memory | CLEO | 2 | Gets the corresponding handle of the char located at the given address in memory |
| `0AEB` | GET_VEHICLE_REF | Memory | CLEO | 2 | Gets the corresponding handle of the vehicle located at the given address in memory |
| `0AEC` | GET_OBJECT_REF | Memory | CLEO | 2 | Gets the corresponding handle of the object located at the given address in memory |
| `0AED` | STRING_FLOAT_FORMAT | Text | CLEO | 3 |  |
| `0AEE` | POW | Math | CLEO | 3 | Returns the specified number raised to the specified power |
| `0AEF` | LOG | Math | CLEO | 3 | Returns the logarithm of the specified number in the specified base |
| `0AF0` | READ_INT_FROM_INI_FILE | IniFile | ini | 4 | Reads an integer value from the ini file |
| `0AF1` | WRITE_INT_TO_INI_FILE | IniFile | ini | 4 | Writes the integer value to the ini file |
| `0AF2` | READ_FLOAT_FROM_INI_FILE | IniFile | ini | 4 | Reads a floating-point value from the ini file |
| `0AF3` | WRITE_FLOAT_TO_INI_FILE | IniFile | ini | 4 | Writes the floating-point value to the ini file |
| `0AF4` | READ_STRING_FROM_INI_FILE | IniFile | ini | 4 | Reads a string value from the ini file |
| `0AF5` | WRITE_STRING_TO_INI_FILE | IniFile | ini | 4 | Writes the string value to the ini file |
| `0AF6` | SAMP_FORCE_SPAWN_MY_PLAYER | SampMyPlayer | SAMPFUNCS | 0 | Sends SampRpc.Spawn to SAMP Server. Teleports our character to spawn as well |
| `0AF7` | SAMP_GET_BASE_ADDRESS | SampClient | SAMPFUNCS | 1 | Returns a pointer to the memory address of samp.dll |
| `0AF8` | SAMP_ADD_MESSAGE_TO_CHAT | SampChat | SAMPFUNCS | 3 | Adds one line of colored message to the chat |
| `0AF9` | SAMP_SEND_CHAT_MESSAGE | SampRaknet | SAMPFUNCS | 2 | Sends SampRpc.Chat containing the message or command to the server |
| `0AFA` | SAMP_IS_AVAILABLE | SampClient | SAMPFUNCS | 0 | Evaluates as logical true if SAMP structures was initialized. Used when checking if gta sa is running on SAMP or in Single Player |
| `0AFB` | SAMP_SEND_REQUEST_CLASS | SampRaknet | SAMPFUNCS | 1 | Sends SampRpc.RequestClass to Server |
| `0AFC` | SAMP_SEND_SCM_EVENT | SampRaknet | SAMPFUNCS | 4 | Sends SampRpc.ScmEvent information about car modification to the server |
| `0AFD` | SAMP_SET_SPECIAL_ACTION | SampClient | SAMPFUNCS | 1 | Sets the special action for our Player |
| `0AFE` | SAMP_SEND_DEATH_BY_PLAYER | SampRaknet | SAMPFUNCS | 2 | Sends SampRpc.Death to Server without our character actually dying |
| `0AFF` | SAMP_GET_CAR_BY_ID | SampClient | SAMPFUNCS | 2 | Returns the vehicle handle using its samp vehicle id. Returns 0 If the car is not in the stream zone |
| `0B00` | DELETE_FILE | Fs | file | 1 | Deletes a file at the given path and returns true if the operation is successful |
| `0B01` | DELETE_DIRECTORY | Fs | file | 2 | Deletes a directory at the given path and returns true if the operation is successful |
| `0B02` | MOVE_FILE | Fs | file | 2 | Moves an existing file and returns true if the operation is successful |
| `0B03` | MOVE_DIRECTORY | Fs | file | 2 | Moves an existing directory and returns true if the operation is successful |
| `0B04` | COPY_FILE | Fs | file | 2 | Copies an existing file to a new file and returns true if the operation is successful |
| `0B05` | COPY_DIRECTORY | Fs | file | 2 | Copies an existing directory to a new directory and returns true if the operation is successful |
| `0B10` | BIT_AND |  | bitwise | 3 | Returns a result of the bitwise AND operation on the corresponding bits of the first and second operands |
| `0B11` | BIT_OR |  | bitwise | 3 | Returns a result of the bitwise OR operation on the corresponding bits of the first and second operands |
| `0B12` | BIT_XOR |  | bitwise | 3 | Returns a result of the bitwise XOR operation on the corresponding bits of the first and second operands |
| `0B13` | BIT_NOT |  | bitwise | 2 | Returns a signed number calculated by logical negation of each bit of the input value |
| `0B14` | MOD |  | bitwise | 3 | Returns the modulo; remainder of a division, after the first number is divided by the second number |
| `0B15` | BIT_SHR |  | bitwise | 3 | Returns a number calculated by shifting right all the bits of the value by n bits |
| `0B16` | BIT_SHL |  | bitwise | 3 | Returns a number calculated by shifting left all the bits of the value by n bits |
| `0B17` | BIT_AND_COMPOUND |  | bitwise | 2 | Reads a value from the variable, performs bitwise AND operation on it and the operand (BIT_AND) and stores the result back to the variable |
| `0B18` | BIT_OR_COMPOUND |  | bitwise | 2 | Reads a value from the variable, performs bitwise OR operation on it and the operand (BIT_OR) and stores the result back to the variable |
| `0B19` | BIT_XOR_COMPOUND |  | bitwise | 2 | Reads a value from the variable, performs bitwise XOR operation on it and the operand (BIT_XOR) and stores the result back to the variable |
| `0B1A` | BIT_NOT_COMPOUND |  | bitwise | 1 | Reads a value from the variable, performs bitwise NOT operation on it (BIT_NOT) and stores the result back to the variable |
| `0B1B` | MOD_COMPOUND |  | bitwise | 2 | Reads a value from the variable, divides it by the number and stores the remainder (MOD) back to the variable |
| `0B1C` | BIT_SHR_COMPOUND |  | bitwise | 2 | Reads a value from the variable, shifts right by n bits (BIT_SHR) and stores the result back to the variable |
| `0B1D` | BIT_SHL_COMPOUND |  | bitwise | 2 | Reads a value from the variable, shifts left by n bits (BIT_SHL) and stores the result back to the variable |
| `0B1E` | SIGN_EXTEND | Math | bitwise | 2 | Extends a 1-, 2- or 3-byte long integer value to a 4-byte (32-bit), while preserving the sign (+/-) |
| `0B20` | READ_CLIPBOARD_DATA | Clipboard | CLEO+ | 2 | Copies the specified number of bytes of text from the clipboard to the address |
| `0B20` | SAMP_GET_PLAYER_CHAR_BY_ID | SampPlayer | SAMPFUNCS | 2 | Returns the character handle using the Player ID. Returns -1 if the player is not in the stream zone |
| `0B20` | READ_CLIPBOARD_DATA | Clipboard | clipboard | 2 | Copies the specified number of bytes of text from the clipboard to the address |
| `0B21` | WRITE_CLIPBOARD_DATA | Clipboard | CLEO+ | 2 |  |
| `0B21` | SAMP_IS_CHAT_INPUT_VISIBLE | SampChatInput | SAMPFUNCS | 0 | Checks if the chat box input is open/visible |
| `0B21` | WRITE_CLIPBOARD_DATA | Clipboard | clipboard | 2 | Copies  the specified number of bytes of text from the address to the clipboard |
| `0B22` | SAMP_SET_SEND_RATE | SampClient | SAMPFUNCS | 2 | Sets the periodic delay (in milliseconds) of sending specific data type to Server |
| `0B23` | SAMP_IS_REMOTE_PLAYER_CONNECTED | SampPlayer | SAMPFUNCS | 1 | Returns true if REMOTE Player with the given ID is connected |
| `0B24` | SAMP_GET_PLAYER_POINTER | SampPlayer | SAMPFUNCS | 2 | Returns the player's samp structure. Returns 0 (NULL Pointer) if player isn't connected |
| `0B25` | SAMP_GET_PLAYER_HEALTH | SampPlayer | SAMPFUNCS | 2 | Returns the amount of health the specified player has |
| `0B26` | SAMP_GET_PLAYER_ARMOR | SampPlayer | SAMPFUNCS | 2 | Returns the amount of armor the specified player has |
| `0B27` | SAMP_SET_GAMESTATE | SampClient | SAMPFUNCS | 1 | Sets the connection status to the server. Useful when attempting to reconnect or disconnect to server |
| `0B28` | SAMP_SEND_DISCONNECTED | SampRaknet | SAMPFUNCS | 1 | Sends SampRpc.ScrServerQuit to the server without actually disconnecting our client to the server |
| `0B29` | SAMP_SET_MY_NICKNAME | SampMyPlayer | SAMPFUNCS | 1 | Changes our nickname (visually) |
| `0B2A` | SAMP_GET_PLAYER_PING | SampPlayer | SAMPFUNCS | 2 | Returns the ping of the specified player with ID |
| `0B2B` | SAMP_GET_PLAYER_ID | Char | SAMPFUNCS | 2 | Returns the samp player's id controlling the character handle. Returns -1 if the character isn't controlled by any Player |
| `0B2C` | SAMP_GET_CAR_ID | Car | SAMPFUNCS | 2 | Returns the SAMP vehicle ID using its car handle |
| `0B2D` | SAMP_WRITE_SAMP_MEMORY_WITH_OFFSET | SampClient | SAMPFUNCS | 3 | Writes the value with size to samp.dll+offset |
| `0B2E` | SAMP_READ_SAMP_MEMORY_WITH_OFFSET | SampClient | SAMPFUNCS | 3 | Reads the value with size from samp.dll+offset |
| `0B2F` | SAMP_GET_STREAMED_OUT_PLAYER_COORDS | SampPlayer | SAMPFUNCS | 4 | Returns the 3D Coordinates of a player who is outside the stream zone, if the server allows it |
| `0B30` | SAMP_SEND_ENTER_CAR | SampRaknet | SAMPFUNCS | 2 | Sends SampRpc.EnterCar to Server |
| `0B31` | SAMP_SEND_EXIT_CAR | SampRaknet | SAMPFUNCS | 1 | Sends SampRpc.ExitCar to Server |
| `0B32` | SAMP_SEND_SPAWN | SampRaknet | SAMPFUNCS | 0 | Sends a SampRpc.Spawn to SAMP Server without spawning our character |
| `0B33` | SAMP_SEND_DAMAGE_CAR | SampRaknet | SAMPFUNCS | 5 | Sends a SampRpc.DamageCar to the Server |
| `0B34` | SAMP_HOOK_CHAT_COMMAND_AS_LOCAL | SampLocalChatCmd | SAMPFUNCS | 2 | Registers a callback hooked from a client sided chat command |
| `0B35` | SF_GET_PARAMS_OF_LAST_TRIGGERED_COMMAND | Sf | SAMPFUNCS | 1 | Returns a pointer to a string containing the parameters of the last command entered at console or SAMP Chat |
| `0B36` | SAMP_GET_PLAYER_NICKNAME | SampPlayer | SAMPFUNCS | 2 | Returns a pointer to the nickname of the specified player |
| `0B37` | SAMP_GET_PLAYER_COLOR | SampPlayer | SAMPFUNCS | 2 | Returns the color of the specified player in 0xAARRGGBB format |
| `0B38` | SAMP_CONNECT | SampRaknet | SAMPFUNCS | 2 | Connects to the specified samp server information |
| `0B39` | SAMP_GET_SERVER_ADDRESS | SampClient | SAMPFUNCS | 2 | Returns the server's port and stores server's IP address to buffer |
| `0B3A` | SAMP_GET_SERVER_NAME | SampClient | SAMPFUNCS | 1 | Stores the server name to buffer |
| `0B3B` | SAMP_SHOW_DIALOG | SampClient | SAMPFUNCS | 6 | Shows an artificial SAMP dialog with specified parameter attributes |
| `0B3C` | SAMP_HAS_DIALOG_RESPONDED | SampClient | SAMPFUNCS | 4 | Returns logical true if the last submitted SAMP Dialog is equal to the specified dialogid |
| `0B3D` | SAMP_RAKNET_CREATE_BITSTREAM | SampBitstream | SAMPFUNCS | 1 | Creates a new raknet bitstream object |
| `0B3E` | SAMP_RAKNET_DELETE_BITSTREAM | SampBitstream | SAMPFUNCS | 1 | Remove's the specified bitstream object, freeing it from memory |
| `0B3F` | SAMP_RAKNET_RESET_BITSTREAM | SampBitstream | SAMPFUNCS | 1 | Resets all parameters/clears BitStream |
| `0B40` | SAMP_RAKNET_BITSTREAM_WRITE | SampBitstream | SAMPFUNCS | 4 | Writes a specified value with datatype and datasize at the "write pointer" of the specified bitstream, then advances its "write pointer" by the same size |
| `0B41` | SAMP_RAKNET_SEND_RPC_WITH_PARAMS | SampBitstream | SAMPFUNCS | 6 | Sends a BitStream as an RPC with the specified parameters |
| `0B42` | SAMP_RAKNET_SEND_PACKET_WITH_PARAMS | SampBitstream | SAMPFUNCS | 4 | Sends a Packet BitStream with the specified parameters. Commonly used to send dacket data to server |
| `0B43` | SF_COMMAND_RETURN | Sf | SAMPFUNCS | 0 | Marks the end of a command callback. Used as its returning statement |
| `0B44` | SAMP_CREATE_3D_TEXT | SampTextLabel3D | SAMPFUNCS | 10 | Creates an artificial SAMP 3D text with the specified parameter attributes |
| `0B45` | SAMP_DELETE_3D_TEXT | SampTextLabel3D | SAMPFUNCS | 1 | Destroys a 3D text using it's ID |
| `0B46` | SAMP_DOES_3D_TEXT_EXIST | SampTextLabel3D | SAMPFUNCS | 1 | Returns logical true if the specified 3D text exists |
| `0B47` | SAMP_CLOSE_ACTIVE_DIALOG_WITH_BUTTON | SampClient | SAMPFUNCS | 1 | Closes the active dialog by pressing the specified button programmatically |
| `0B48` | SAMP_GET_ACTIVE_DIALOG_SELECTED_LIST_ITEM | SampClient | SAMPFUNCS | 1 | Returns the ID of the currently selected item on the list |
| `0B49` | SAMP_SELECT_ACTIVE_DIALOG_LIST_ITEM | SampClient | SAMPFUNCS | 1 | Selects the id of an element in the dialog list |
| `0B4A` | SAMP_GET_ACTIVE_DIALOG_EDITBOX_TEXT | SampClient | SAMPFUNCS | 1 | Stores the text from the input field of the active dialog to the buffer |
| `0B4B` | SAMP_SET_ACTIVE_DIALOG_EDITBOX_TEXT | SampClient | SAMPFUNCS | 1 | Sets the text of the edit field of the active dialog's box |
| `0B4C` | SAMP_IS_DIALOG_ACTIVE | SampClient | SAMPFUNCS | 1 | Evaluates as logical true if the specified dialog with id is currently visible |
| `0B4D` | SAMP_GET_DIALOG_STYLE | SampClient | SAMPFUNCS | 1 | Returns the style of the active dialog. If the dialog is not opened, returns the style of the last opened dialog instead |
| `0B4E` | SAMP_GET_DIALOG_ID | SampClient | SAMPFUNCS | 1 | Returns the ID of the active dialog. If the dialog is not opened, returns the ID of the last opened dialog instead |
| `0B4F` | SAMP_GET_GAMESTATE | SampClient | SAMPFUNCS | 1 | Returns our connection status towards the server |
| `0B50` | SAMP_GET_OBJECT_BY_ID | SampClient | SAMPFUNCS | 2 | Returns the handle of an object using its SAMP ID |
| `0B51` | SAMP_GET_PICKUP_BY_ID | SampClient | SAMPFUNCS | 2 | Returns the handle of a pickup using its SAMP ID |
| `0B52` | SAMP_GET_OBJECT_ID | Object | SAMPFUNCS | 2 | Returns the SAMP ID of an object using its handle |
| `0B53` | SAMP_GET_PICKUP_ID | Pickup | SAMPFUNCS | 2 | Returns the SAMP ID of a pickup using its handle |
| `0B54` | SAMP_GET_DIALOG_LIST_ITEMS_COUNT | SampClient | SAMPFUNCS | 1 | Returns the total number of items found on the active dialog's list. If the dialog is not opened, the last opened dialog is used instead |
| `0B55` | SF_WORLD_COORDS_TO_WINDOW_SCREEN_COORDS | Sf | SAMPFUNCS | 5 | Converts 3D coordinates from the world into window screen coordinates (pixels) |
| `0B56` | SF_SET_BUTTON | Sf | SAMPFUNCS | 2 | Sets the press status of a game (NOT keyboard) key |
| `0B57` | SAMP_GET_PLAYER_ANIMATION | SampPlayer | SAMPFUNCS | 2 | Returns the SAMP ID of the animation currently being played by the specified player |
| `0B58` | SAMP_GET_ANIMATION_NAME | SampClient | SAMPFUNCS | 3 | Stores the filename and animname of the animation using its SAMP ID |
| `0B59` | SAMP_GET_ANIMATION_ID | SampClient | SAMPFUNCS | 3 | Returns the Animation SAMP ID using its name and the file it was loaded from |
| `0B5A` | SF_GET_SCREEN_RESOLUTION | Sf | SAMPFUNCS | 2 | Returns the current window screen resolution in pixels |
| `0B5B` | SAMP_GET_DIALOG_LIST_ITEM_TEXT | SampClient | SAMPFUNCS | 2 | Stores the text of an item with specific id from the active dialog's list, to buffer. If the dialog is not opened, the last opened dialog is evaluated instead |
| `0B5C` | SAMP_IS_PLAYER_PAUSED | SampPlayer | SAMPFUNCS | 1 | Evaluates as logical true if the specified player is in paused state (or AFK) |
| `0B5D` | SAMP_SET_CURSOR_VISIBILITY | SampClient | SAMPFUNCS | 1 | Sets the visibility status of mouse cursor |
| `0B5E` | SF_GET_CURSOR_COORD | Sf | SAMPFUNCS | 2 | Returns the mouse cursor's window screen coordinates in pixels |
| `0B5F` | SF_WINDOW_SCREEN_COORDS_TO_GAME_SCREEN_COORDS | Sf | SAMPFUNCS | 4 | Returns the GameScreen Coordinates counterpart of the specified WindowScreen Coordinates |
| `0B60` | SF_GAME_SCREEN_COORDS_TO_WINDOW_SCREEN_COORDS | Sf | SAMPFUNCS | 4 | Returns the WindowScreen Coordinates counterpart of the specified GameScreen Coordinates |
| `0B61` | SAMP_IS_MY_PLAYER_SPAWNED | SampMyPlayer | SAMPFUNCS | 0 | Evaluates as logical true if our player has been spawned already |
| `0B62` | SAMP_GET_PLAYER_SPECIAL_ACTION | SampPlayer | SAMPFUNCS | 2 | Returns the special action ID of the specified player |
| `0B63` | SAMP_UNHOOK_LOCAL_CHAT_COMMAND | SampLocalChatCmd | SAMPFUNCS | 1 | Removes all callbacks hooked from a chatCommand created by SAMP_REGISTER_CLIENTSIDE_COMMAND, suppressing all its callback's operation  |
| `0B64` | SAMP_IS_PLAYER_NPC | SampPlayer | SAMPFUNCS | 1 | Checks if the specified player is an NPC |
| `0B65` | SAMP_GET_PLAYER_SCORE | SampPlayer | SAMPFUNCS | 2 | Returns the current score of the specified player |
| `0B66` | SF_HEX_TO_ARGB | Sf | SAMPFUNCS | 5 | Splits 0xAARRGGBB colorcode format into individial color channels |
| `0B67` | SF_ARGB_TO_HEX | Sf | SAMPFUNCS | 5 | mixes color channels into 0xAARRGGBB colorcode format |
| `0B68` | SF_D3D_DRAW_LINE | SfD3D | SAMPFUNCS | 6 | Draws a line between two window screen coordinates |
| `0B69` | SF_D3D_DRAW_BORDERLESS_BOX | SfD3D | SAMPFUNCS | 5 | Draws a rectangular area at the specified coordinates |
| `0B6A` | SF_D3D_DRAW_BORDERED_BOX | SfD3D | SAMPFUNCS | 7 | Draws a rectangular area with border at the specified coordinates |
| `0B6B` | SF_D3D_GET_DRAW_WIDTH_OF_TEXT_WITH_FONT | SfD3DFont | SAMPFUNCS | 3 | Returns the width (in pixels) that will be occupied by the text with font |
| `0B6C` | SF_D3D_GET_FONT_DRAW_HEIGHT | SfD3DFont | SAMPFUNCS | 2 | Returns the height (in pixels) occupied by any text that uses the specified font |
| `0B6D` | SF_D3D_CREATE_FONT | SfD3DFont | SAMPFUNCS | 4 | Creates a D3DFont Object |
| `0B6E` | SF_D3D_DELETE_FONT | SfD3DFont | SAMPFUNCS | 1 | Destroys the specified font object, freeing it from memory |
| `0B6F` | SF_D3D_DRAW_TEXT_WITH_FONT | SfD3DFont | SAMPFUNCS | 5 | Draws text using the specified font |
| `0B70` | SF_D3D_DRAW_POLYGON | SfD3D | SAMPFUNCS | 7 | Draws a polygon with the specified parameters |
| `0B71` | SF_D3D_LOAD_TEXTURE_FROM_FILE | SfD3DTexture | SAMPFUNCS | 2 | Loads a file (any image, or txd) as D3DTexture Object |
| `0B72` | SF_D3D_RELEASE_TEXTURE | SfD3DTexture | SAMPFUNCS | 1 | Releases the D3DTexture Object, freeing it from memory |
| `0B73` | SF_D3D_DRAW_TEXTURE | SfD3DTexture | SAMPFUNCS | 7 | Draws the texture on the screen |
| `0B74` | SAMP_SET_CHAT_LINE | SampChat | SAMPFUNCS | 5 | Changes the chat line's text into a custom one |
| `0B75` | SAMP_GET_CHAT_LINE | SampChat | SAMPFUNCS | 5 | Returns the chat line's text parameters |
| `0B76` | SAMP_SET_CHAT_INPUT_TEXT | SampChatInput | SAMPFUNCS | 1 | Overwrites the content written at the chat input box |
| `0B77` | SAMP_GET_CHAT_INPUT_TEXT | SampChatInput | SAMPFUNCS | 1 | Returns the current text in the chat input box |
| `0B78` | SF_LOG_TO_CONSOLE | SfConsole | SAMPFUNCS | 2 | Adds a line to the SAMPFUNCS console and logs it |
| `0B79` | SAMP_SET_CHAT_INPUT_VISIBILITY | SampChatInput | SAMPFUNCS | 1 | Sets the visibility status (open/closed) of the chat input box |
| `0B7A` | SAMP_GET_RAKCLIENT_INTERFACE | SampClient | SAMPFUNCS | 1 | Returns a pointer to a RakClientInterface object |
| `0B7B` | SAMP_GET_RAKPEER | SampClient | SAMPFUNCS | 1 | Returns a pointer to RakPeer |
| `0B7C` | SAMP_GET_RAKCLIENT_FUNC_BY_INDEX | SampClient | SAMPFUNCS | 2 | Returns the address of the RakClientInterface virtual method table function by index |
| `0B7D` | SAMP_GET_RPC_FUNC_BY_INDEX | SampClient | SAMPFUNCS | 2 | Returns the RPC callback address by index |
| `0B7E` | SAMP_GET_RPC_NODE_BY_INDEX | SampClient | SAMPFUNCS | 2 | Returns a pointer to the RPC structure at index |
| `0B7F` | SAMP_GET_INFO_POINTER | SampClient | SAMPFUNCS | 1 | Returns a pointer to a SampInfo structure |
| `0B80` | SF_DXUT_CREATE_DIALOG | SfDxutDialog | SAMPFUNCS | 2 | Creates a DXUTDialog Object with Title |
| `0B81` | SF_DXUT_DIALOG_POP | SfDxutDialog | SAMPFUNCS | 3 | Returns the last event and component ID that occurred with the specified dialog |
| `0B82` | SF_DXUT_DIALOG_ADD_BUTTON | SfDxutDialog | SAMPFUNCS | 7 | Adds a button on the DXUTDialog |
| `0B83` | SF_DXUT_DIALOG_ADD_CHECKBOX | SfDxutDialog | SAMPFUNCS | 7 | Creates a checkbox on the DxutDialog |
| `0B84` | SF_DXUT_DIALOG_SET_COORDS_AND_DIMS | SfDxutDialog | SAMPFUNCS | 5 | Sets the coordinates and dimensions of the DxutDialog |
| `0B85` | SF_DXUT_DIALOG_GET_COORDS_AND_DIMS | SfDxutDialog | SAMPFUNCS | 5 | Returns the Coordinates and Dimensions of the DxutDialog |
| `0B86` | SF_DXUT_DIALOG_SET_VISIBILITY | SfDxutDialog | SAMPFUNCS | 2 | Sets the visibility status of the DxutDialog |
| `0B87` | SF_DXUT_DIALOG_IS_VISIBLE | SfDxutDialog | SAMPFUNCS | 1 | Checks if the DxutDialog is visible |
| `0B88` | SF_DXUT_DIALOG_ADD_EDITBOX | SfDxutDialog | SAMPFUNCS | 7 | Creates a text input field on a DxutDialog |
| `0B89` | SF_DXUT_DIALOG_GET_TEXT_OF_CONTROL | SfDxutDialog | SAMPFUNCS | 3 | Returns the text of a control using its ID |
| `0B8A` | SAMP_RAKNET_SEND_RPC | SampBitstream | SAMPFUNCS | 2 | Sends BitStream as RPC to Server |
| `0B8B` | SAMP_RAKNET_SEND_PACKET | SampBitstream | SAMPFUNCS | 1 | Sends Packet BitStream to Server |
| `0B8C` | SAMP_IS_CURSOR_ACTIVE | SampClient | SAMPFUNCS | 0 | Checks if the mouse cursor were both visible and movable |
| `0B8D` | SAMP_SET_CURSOR_MODE | SampClient | SAMPFUNCS | 1 | Sets the cursor mode |
| `0B8E` | SAMP_GET_CURSOR_MODE | SampClient | SAMPFUNCS | 1 | Returns the current mouse cursor mode |
| `0B8F` | SF_WINDOW_SCREEN_COORDS_TO_WORLD_COORDS | Sf | SAMPFUNCS | 6 | Converts window screen coordinates (pixels) to world's 3D coordinates with the specified depth |
| `0B90` | SF_DXUT_DIALOG_SET_VISIBILITY_OF_CONTROL | SfDxutDialog | SAMPFUNCS | 3 | Sets the visibility of the DXUTDialog's control element with ID |
| `0B91` | SF_DXUT_DIALOG_ADD_STATIC_TEXT | SfDxutDialog | SAMPFUNCS | 7 | Adds a static text control in the DxutDialog |
| `0B92` | SF_DXUT_DIALOG_IS_CHECKBOX_CHECKED | SfDxutDialog | SAMPFUNCS | 2 | Evaluates as logical true if the checkbox control of the DxutDialog is checked |
| `0B93` | SF_DXUT_DIALOG_SET_BACKGROUND_COLOR | SfDxutDialog | SAMPFUNCS | 2 | Sets the background color of the DxutDialog |
| `0B94` | SF_DXUT_DIALOG_SET_TEXT_OF_CONTROL | SfDxutDialog | SAMPFUNCS | 3 | Sets the text of a control using its ID |
| `0B95` | SF_DXUT_DIALOG_IS_CONTROL_VISIBLE | SfDxutDialog | SAMPFUNCS | 2 | Evaluates as true if the DxutDialog's control element with ID is visible |
| `0B96` | SF_DXUT_DIALOG_ADD_SLIDER | SfDxutDialog | SAMPFUNCS | 7 | Creates a horizontal slider on the DxutDialog |
| `0B97` | SF_DXUT_DIALOG_GET_SLIDER_VALUE | SfDxutDialog | SAMPFUNCS | 3 | Returns the thumb position value of the DxutDialog's slider with ID |
| `0B98` | SF_DXUT_DIALOG_SET_SLIDER_VALUE | SfDxutDialog | SAMPFUNCS | 3 | Sets the thumb position value of the DxutDialog's slider with ID |
| `0B99` | SF_DXUT_DIALOG_ADD_LISTBOX | SfDxutDialog | SAMPFUNCS | 6 | Creates a listbox on the dialog |
| `0B9A` | SF_DXUT_DIALOG_INSERT_LISTBOX_ELEMENT | SfDxutDialog | SAMPFUNCS | 5 | Inserts a new element into the DxutDialog's listbox with ID |
| `0B9B` | SF_DXUT_DIALOG_GET_SELECTED_LISTBOX_ELEMENT | SfDxutDialog | SAMPFUNCS | 4 | Returns the index of the selected element and the count/number of elements in the DxutDialog's listbox with ID |
| `0B9C` | SF_DXUT_DIALOG_DELETE_LISTBOX_ELEMENT | SfDxutDialog | SAMPFUNCS | 3 | Removes the element found at the specified index from the DxutDialog's listbox with ID |
| `0B9D` | SF_DXUT_DIALOG_GET_LISTBOX_ELEMENT | SfDxutDialog | SAMPFUNCS | 5 | Returns the text and data associated with the DxutDialog's listbox element by index |
| `0B9E` | SF_DXUT_DIALOG_SET_STATUS_OF_CHECKBOX | SfDxutDialog | SAMPFUNCS | 3 | Sets the status of a checkbox |
| `0B9F` | SF_DXUT_DIALOG_SET_TITLE_VISIBILITY | SfDxutDialog | SAMPFUNCS | 2 | Sets the visibility of the DxutDialog's title |
| `0BA0` | SF_DXUT_DIALOG_IS_TITLE_VISIBLE | SfDxutDialog | SAMPFUNCS | 1 | Evaluates as logical true if the DxutDialog's title is visible |
| `0BA1` | SF_DXUT_DIALOG_SET_MINIMIZED | SfDxutDialog | SAMPFUNCS | 2 | Sets the minimized status of the DxutDialog |
| `0BA2` | SF_DXUT_DIALOG_IS_MINIMIZED | SfDxutDialog | SAMPFUNCS | 1 | Returns logical true if the DxutDialog is minimized |
| `0BA3` | SF_DXUT_DIALOG_DELETE_CONTROL | SfDxutDialog | SAMPFUNCS | 2 | Removes a DxutDialog's control with ID and frees the memory allocated for it |
| `0BA4` | SF_DXUT_DIALOG_DELETE | SfDxutDialog | SAMPFUNCS | 1 | Deletes the DxutDialog and frees the memory allocated for it |
| `0BA5` | SF_DXUT_DIALOG_SET_FOCUSED_CONTROL | SfDxutDialog | SAMPFUNCS | 2 | Sets the focus of user interaction to a specific DxutDialog control with ID |
| `0BA6` | SF_DXUT_DIALOG_SET_DIMS_OF_CONTROL | SfDxutDialog | SAMPFUNCS | 4 | Changes the dimensions of the DxutDialog control with ID |
| `0BA7` | SF_DXUT_DIALOG_GET_DIMS_OF_CONTROL | SfDxutDialog | SAMPFUNCS | 4 | Returns the dimensions of the DxutDialog control with ID |
| `0BA8` | SF_DXUT_DIALOG_SET_COORDS_OF_CONTROL | SfDxutDialog | SAMPFUNCS | 4 | Sets the window position of the DxutDialog control with ID |
| `0BA9` | SF_DXUT_DIALOG_GET_COORDS_OF_CONTROL | SfDxutDialog | SAMPFUNCS | 4 | Returns the window position of a DxutDialog control |
| `0BAA` | SF_DXUT_DIALOG_SET_COLOR_OF_CHECKBOX | SfDxutDialog | SAMPFUNCS | 3 | Sets the color of DxutDialog's checkbox control with ID |
| `0BAB` | SF_DXUT_DIALOG_EXIST | SfDxutDialog | SAMPFUNCS | 1 | Evaluates as logical true if the specified DxutDialog exists |
| `0BAC` | SAMP_GET_SERVER_SETTINGS_POINTER | SampClient | SAMPFUNCS | 1 | Returns the pointer to server settings structure |
| `0BAD` | SAMP_GET_POOLS_POINTER | SampClient | SAMPFUNCS | 1 | Returns the pointer to samp pools structure |
| `0BAE` | SAMP_GET_CHAT_INFO_POINTER | SampClient | SAMPFUNCS | 1 | Returns the pointer to samp chat information structure |
| `0BAF` | SAMP_GET_CHAT_INPUT_INFO_POINTER | SampClient | SAMPFUNCS | 1 | Returns the pointer to samp chat input field structure |
| `0BB0` | SAMP_GET_DIALOG_INFO_POINTER | SampClient | SAMPFUNCS | 1 | Returns the pointer to samp dialog structure |
| `0BB1` | SAMP_GET_KILL_INFO_POINTER | SampClient | SAMPFUNCS | 1 | Returns the pointer to samp kill list structure |
| `0BB2` | SAMP_GET_MISC_INFO_POINTER | SampClient | SAMPFUNCS | 1 | Returns the pointer to a structure of various samp miscellaneous data |
| `0BB3` | SAMP_GET_TEXTDRAW_POOL_POINTER | SampClient | SAMPFUNCS | 1 | Returns the pointer to samp textdraw pool structure |
| `0BB4` | SAMP_GET_OBJECT_POOL_POINTER | SampClient | SAMPFUNCS | 1 | Returns the pointer to samp object pool structure |
| `0BB5` | SAMP_GET_GANGZONE_POOL_POINTER | SampClient | SAMPFUNCS | 1 | Returns a pointer to the pool of samp allocated territories (gang territories) |
| `0BB6` | SAMP_GET_TEXTLABEL_POOL_POINTER | SampClient | SAMPFUNCS | 1 | Returns the pointer to 3D text pool structure |
| `0BB7` | SAMP_GET_PLAYER_POOL_POINTER | SampClient | SAMPFUNCS | 1 | Returns the pointer to player pool structure |
| `0BB8` | SAMP_GET_CAR_POOL_POINTER | SampClient | SAMPFUNCS | 1 | Returns the pointer to samp car pool structure |
| `0BB9` | SAMP_GET_PICKUP_POOL_POINTER | SampClient | SAMPFUNCS | 1 | Returns the pointer to samp pickup pool structure |
| `0BBA` | SAMP_STORE_PLAYER_ONFOOT_DATA | SampPlayer | SAMPFUNCS | 2 | Stores the current player's onFootData structure to the buffer |
| `0BBB` | SAMP_STORE_PLAYER_DRIVING_DATA | SampPlayer | SAMPFUNCS | 2 | Stores the player's current inCarData structure to the buffer |
| `0BBC` | SAMP_STORE_PLAYER_PASSENGER_DATA | SampPlayer | SAMPFUNCS | 2 | Stores the current passengerData structure of the player to the buffer |
| `0BBD` | SAMP_STORE_PLAYER_TRAILER_DATA | SampPlayer | SAMPFUNCS | 2 | Stores the player's current trailerData structure to the buffer |
| `0BBE` | SAMP_STORE_PLAYER_AIM_DATA | SampPlayer | SAMPFUNCS | 2 | Stores the specified player's aimData structure to the buffer |
| `0BBF` | SAMP_SEND_RCON_COMMAND | SampRaknet | SAMPFUNCS | 1 | Sends an RCON command to the server |
| `0BC0` | SAMP_SEND_ONFOOT_DATA | SampRaknet | SAMPFUNCS | 1 | Sends SampPacket.OnFootSync containing stOnFootData payload to the server |
| `0BC1` | SAMP_SEND_DRIVING_DATA | SampRaknet | SAMPFUNCS | 1 | Sends SampPacket.DrivingSync containing stInCarData payload to the server |
| `0BC2` | SAMP_SEND_PASSENGER_DATA | SampRaknet | SAMPFUNCS | 1 | Sends SampPacket.PassengerSync containing stPassengerData payload to the server |
| `0BC3` | SAMP_SEND_AIM_DATA | SampRaknet | SAMPFUNCS | 1 | Sends SampPacket.AimSync containing stAimData payload to the server  |
| `0BC4` | SAMP_SEND_BULLET_DATA | SampRaknet | SAMPFUNCS | 1 | Sends SampPacket.BulletSync containing stBulletData payload to the server |
| `0BC5` | SAMP_SEND_TRAILER_DATA | SampRaknet | SAMPFUNCS | 1 | Sends SampPacket.TrailerSync containing stTrailerData payload to the server |
| `0BC6` | SAMP_SEND_UNOCCUPIEDCAR_DATA | SampRaknet | SAMPFUNCS | 1 | Sends SampPacket.UnoccupiedCarSync containing stUnoccupiedData payload to the server |
| `0BC7` | SAMP_SEND_SPECTATOR_DATA | SampRaknet | SAMPFUNCS | 1 | Sends SampPacket.SpectatorSync containing stSpectatorData  payload to the server |
| `0BC8` | SAMP_SEND_CLICK_PLAYER | SampRaknet | SAMPFUNCS | 2 | Sends SampRpc.ClickPlayer about double click on player (from Scoreboard for example) |
| `0BC9` | SAMP_SEND_DIALOG_RESPONSE | SampRaknet | SAMPFUNCS | 4 | Sends an SampRpc.DialogResponse to the server |
| `0BCA` | SAMP_SEND_CLICK_TEXTDRAW | SampRaknet | SAMPFUNCS | 1 | Sends an SampRpc.ClickTextDraw to the server |
| `0BCB` | SAMP_SEND_GIVE_DAMAGE | SampRaknet | SAMPFUNCS | 4 | Sends an SampRpc.GiveTakeDamage to the server about damage dealt by another player |
| `0BCC` | SAMP_SEND_TAKE_DAMAGE | SampRaknet | SAMPFUNCS | 4 | Sends an SampRpc.GiveTakeDamage to the server about damage taken from another player |
| `0BCD` | SAMP_SEND_EDIT_OBJECT | SampRaknet | SAMPFUNCS | 9 | Sends an SampRpc.EditObject about changing the structure of an object in its editing mode |
| `0BCE` | SAMP_SEND_EDIT_ATTACHED_OBJECT | SampRaknet | SAMPFUNCS | 13 | Sends SampRpc.EditAttachedObject about a change to an attached object in object edit mode |
| `0BCF` | SAMP_SEND_REQUEST_INTERIOR_CHANGE | SampRaknet | SAMPFUNCS | 1 | Sends SampRpc.RequestInteriorChange |
| `0BD0` | SAMP_SEND_REQUEST_SPAWN | SampRaknet | SAMPFUNCS | 0 | Sends SampRpc.RequestSpawn |
| `0BD1` | SAMP_SEND_PICKED_UP_PICKUP | SampRaknet | SAMPFUNCS | 1 | Sends SampRpc.PickedUpPickup to take a pickup |
| `0BD2` | SAMP_SEND_MENU_SELECT_ROW | SampRaknet | SAMPFUNCS | 1 | Sends SampRpc.MenuSelect about selecting an item in a menu (GTA:SA menu) |
| `0BD3` | SAMP_SEND_QUIT_MENU | SampRaknet | SAMPFUNCS | 0 | Sends SampRpc.MenuQuit to tell the server we exited the menu (GTA:SA menu) |
| `0BD4` | SAMP_SEND_CAR_DESTROYED | SampRaknet | SAMPFUNCS | 1 | Sends SampRpc.CarDestroyed about destruction of a specific car (exploded or drenched in water) |
| `0BD5` | SAMP_IS_SCOREBOARD_VISIBLE | SampClient | SAMPFUNCS | 0 | Evaluates as logical true if the scoreboard is visible |
| `0BD6` | SAMP_SET_SCOREBOARD_VISIBILITY | SampClient | SAMPFUNCS | 1 | Sets the visibility of the scoreboard |
| `0BD7` | SAMP_GET_DIALOG_CONTENT | SampClient | SAMPFUNCS | 1 | Returns the content of the active dialog to buffer. If the dialog is not opened, the last opened dialog is evaluated instead |
| `0BD8` | SAMP_GET_DIALOG_TITLE | SampClient | SAMPFUNCS | 1 | Stores the title of the active dialog to buffer. If the dialog is not opened, the last opened dialog is evaluated instead |
| `0BD9` | SAMP_SET_ACTIVE_DIALOG_ENVIRONMENT | SampClient | SAMPFUNCS | 1 | Sets whether interactions with the active dialog would sync to the server(server-sided dialog) or not(client-sided dialog) |
| `0BDA` | SAMP_IS_ACTIVE_DIALOG_CLIENTSIDE | SampClient | SAMPFUNCS | 0 | Evaluates as logical true if the active dialog is has a client side attribute |
| `0BDB` | SAMP_IS_CHAT_VISIBLE | SampChat | SAMPFUNCS | 0 | Evaluates as logical true if chat lines are visible |
| `0BDC` | SAMP_GET_CHAT_DISPLAY_MODE | SampChat | SAMPFUNCS | 1 | Returns the current chat display mode |
| `0BDD` | SAMP_SET_CHAT_DISPLAY_MODE | SampChat | SAMPFUNCS | 1 | Sets the chat display mode |
| `0BDE` | SF_PAUSE_SCRIPT | Sf | SAMPFUNCS | 1 | Sets the specified script's isActive parameter to 0 |
| `0BDF` | SF_RESUME_SCRIPT | Sf | SAMPFUNCS | 1 | Sets the specified script's isActive parameter to 1 |
| `0BE0` | SAMP_RAKNET_HOOK_RETURN | SampRaknet | SAMPFUNCS | 1 | Returns the flow of control to RakNet and decides whether the currently intercepted data will be processed by RakNet or not |
| `0BE1` | SAMP_RAKNET_HOOK_OUTCOMING_RPC | SampRaknet | SAMPFUNCS | 1 | Redirects all outgoing RPCs to the specified callback for subsequent processing before sending to the server |
| `0BE2` | SAMP_RAKNET_HOOK_OUTCOMING_PACKET | SampRaknet | SAMPFUNCS | 1 | Redirects all outgoing Packets to the specified callback for subsequent processing before sending to the server |
| `0BE3` | SAMP_RAKNET_HOOK_INCOMING_RPC | SampRaknet | SAMPFUNCS | 1 | Redirects all incoming RPCs to the specified callback for subsequent processing before acceptance on the local client |
| `0BE4` | SAMP_RAKNET_HOOK_INCOMING_PACKET | SampRaknet | SAMPFUNCS | 1 | Redirects all incoming packets to the specified callback for subsequent processing before acceptance on the local client |
| `0BE5` | SAMP_RAKNET_HOOK_GET_PARAM | SampRaknet | SAMPFUNCS | 2 | Returns the hook parameter's value of the currently executing callback |
| `0BE6` | SAMP_RAKNET_SET_HOOK_PARAM | SampRaknet | SAMPFUNCS | 2 | Sets the hook parameter's value of the currently executing callback |
| `0BE7` | SAMP_RAKNET_BITSTREAM_READ | SampBitstream | SAMPFUNCS | 3 | Reads a value with datatype and datasize at the "read pointer" of the specified bitstream , then advances its "read pointer" by the same size |
| `0BE8` | SAMP_RAKNET_BITSTREAM_READ_ARRAY | SampBitstream | SAMPFUNCS | 3 | Stores an array of bytes from the Bitstream to buffer |
| `0BE9` | SAMP_RAKNET_BITSTREAM_RESET_READ_POINTER | SampBitstream | SAMPFUNCS | 1 | Resets the read pointer of the BitStream. Setting "write offset = 0" |
| `0BEA` | SAMP_RAKNET_BITSTREAM_RESET_WRITE_POINTER | SampBitstream | SAMPFUNCS | 1 | Resets (THIS COMMAND IS BUGGED, SETS THE WRITE POINTER AT THE BEGINNING OF THE DATA ( WRITE OFFSET = 0) WHICH IS WRONG. DO NOT USE) the value write pointer in the BitStream |
| `0BEB` | SAMP_RAKNET_BITSTREAM_SKIP_BITS | SampBitstream | SAMPFUNCS | 2 | Increases both its "read pointer" and "write pointer" of the Bitstream by the specified bit count |
| `0BEC` | SAMP_RAKNET_BITSTREAM_SET_WRITE_OFFSET | SampBitstream | SAMPFUNCS | 2 | Sets the write offset of the BitStream |
| `0BED` | SAMP_RAKNET_BITSTREAM_SET_READ_OFFSET | SampBitstream | SAMPFUNCS | 2 | Sets the read offset of the BitStream |
| `0BEE` | SAMP_RAKNET_BITSTREAM_GET_NUMBER_OF_BITS_USED | SampBitstream | SAMPFUNCS | 2 | Returns the number of used bits in the BitStream |
| `0BEF` | SAMP_RAKNET_BITSTREAM_GET_NUMBER_OF_BYTES_USED | SampBitstream | SAMPFUNCS | 2 | Returns the number of bytes used in the BitStream |
| `0BF0` | SAMP_RAKNET_BITSTREAM_GET_NUMBER_OF_UNREAD_BITS | SampBitstream | SAMPFUNCS | 2 | Returns the number of unread bits in the BitStream |
| `0BF1` | SAMP_RAKNET_BITSTREAM_GET_WRITE_OFFSET | SampBitstream | SAMPFUNCS | 2 | Returns the current write offset of the BitStream |
| `0BF2` | SAMP_RAKNET_BITSTREAM_GET_READ_OFFSET | SampBitstream | SAMPFUNCS | 2 | Returns the current read offset of the BitStream |
| `0BF3` | SAMP_RAKNET_BITSTREAM_GET_DATA_POINTER | SampBitstream | SAMPFUNCS | 2 | Returns a pointer to the BitStream's data |
| `0BF4` | SAMP_RAKNET_BITSTREAM_DECODE_COMPRESSED_STRING | SampBitstream | SAMPFUNCS | 3 | Decrypts a compressed string (CString) from the bitstream then stores this to the buffer |
| `0BF5` | SAMP_RAKNET_BITSTREAM_ENCODE_STRING | SampBitstream | SAMPFUNCS | 3 | Encrypts a string stored in the buffer then stores this compressed string (CString) to the bitstream |
| `0BF6` | SAMP_RAKNET_BITSTREAM_EMULATE_AS_INCOMING_RPC | SampBitstream | SAMPFUNCS | 2 | Emulates the BitStream's data like an incoming RPC |
| `0BF7` | SAMP_RAKNET_BITSTREAM_EMULATE_AS_INCOMING_PACKET | SampBitstream | SAMPFUNCS | 2 | Emulates the BitStream's data like an Incoming Packet |
| `0BF8` | SAMP_RAKNET_GET_RPC_NAME | SampRaknet | SAMPFUNCS | 2 | Returns a pointer to the RPC ID's Name |
| `0BF9` | SAMP_RAKNET_GET_PACKET_NAME | SampRaknet | SAMPFUNCS | 2 | Returns a pointer to the Packet ID's Name |
| `0BFA` | SF_PUSH_LOCAL_VARIABLES | Sf | SAMPFUNCS | 0 | Saves the values of all local variables from the currently executing script (Main Script or a Function) to a separate memory that can be recovered later on by SF_POP_LOCAL_VARIABLES |
| `0BFB` | SF_POP_LOCAL_VARIABLES | Sf | SAMPFUNCS | 0 | Restores all previously saved local variables by SF_PUSH_LOCAL_VARIABLES to the local variables of the currently executing script (Main Script or a Function) |
| `0BFC` | SF_SET_CUSTOM_GLOBAL_VARIABLE | SfGVar | SAMPFUNCS | 2 | Sets the value of the custom global variable with name |
| `0BFD` | SF_GET_CUSTOM_GLOBAL_VARIABLE | SfGVar | SAMPFUNCS | 2 | Returns the value of the custom global variable with name |
| `0BFE` | SF_GET_TICK_COUNT | Sf | SAMPFUNCS | 1 | Returns the OS's current uptime in milliseconds. Recommended substitute for TIMERA and TIMERB when requiring precise timing operations |
| `0BFF` | SF_PROCESS_LINE_OF_SIGHT | Sf | SAMPFUNCS | 15 | Checks for collisions using flags from the start of the vector to its end |
| `0C00` | SF_ABS | Sf | SAMPFUNCS | 2 | Returns the absolute value of a number (float or integer) |
| `0C01` | SF_RADIANS_TO_DEGREES | Sf | SAMPFUNCS | 2 | Converts radians to degrees |
| `0C02` | SF_DEGREES_TO_RADIANS | Sf | SAMPFUNCS | 2 | Converts degrees to radians |
| `0C03` | SF_SIN | Sf | SAMPFUNCS | 2 | Returns the sine of the specified radians |
| `0C04` | SF_ASIN | Sf | SAMPFUNCS | 2 | Returns the radian arcsine of the specified ratio |
| `0C05` | SF_COS | Sf | SAMPFUNCS | 2 | Returns the cosine of the specified radians |
| `0C06` | SF_ACOS | Sf | SAMPFUNCS | 2 | Returns the radian arccosine of the specified ratio |
| `0C07` | SF_TAN | Sf | SAMPFUNCS | 2 | Returns the tangent of the specified radians |
| `0C08` | SF_ATAN | Sf | SAMPFUNCS | 2 | Returns the radian arctangent of the specified ratio |
| `0C09` | SF_POW | Sf | SAMPFUNCS | 3 | Raises a number to the specified power |
| `0C0A` | SF_CEIL | Sf | SAMPFUNCS | 2 | Returns the rounded-up result the specified number |
| `0C0B` | SF_FLOOR | Sf | SAMPFUNCS | 2 | Returns the rounded-down result the specified number |
| `0C0C` | SF_READ_MEMORY_WITH_OFFSET | Sf | SAMPFUNCS | 4 | Reads the value with size from memory address with offset |
| `0C0D` | SF_WRITE_MEMORY_WITH_OFFSET | Sf | SAMPFUNCS | 4 | Writes the value with size to memory address with offset |
| `0C0E` | SF_READ_ELEMENT_OF_4BYTES_ARRAY | Sf | SAMPFUNCS | 3 | Reads the value from the specified element index of an array |
| `0C0F` | SF_WRITE_ELEMENT_OF_4BYTES_ARRAY | Sf | SAMPFUNCS | 3 | Writes the value to the specified element index of an array |
| `0C10` | SF_MEMCPY | Sf | SAMPFUNCS | 3 | Copies a memory block with size from source address to destination address |
| `0C11` | SF_MEMFILL | Sf | SAMPFUNCS | 3 | Fills a sized memory block with value byte-by-byte |
| `0C12` | SF_MEMEQ | Sf | SAMPFUNCS | 3 | Evaluates as logical true if both memory blocks have the same content |
| `0C13` | SF_STRCPY | Sf | SAMPFUNCS | 2 | Copies the string from source to destination |
| `0C14` | SF_STREQ | Sf | SAMPFUNCS | 2 | Evaluates as logical true if both case-sensitive strings are equal |
| `0C15` | SF_STRCAT | Sf | SAMPFUNCS | 2 | Appends the appendedString at the end of the string found at the stringBuffer |
| `0C16` | SF_STRTOK | Sf | SAMPFUNCS | 3 | Searches the stringBuffer for any delimiters then replaces the first hit with a NULL terminator (0x00). Returns the (token) pointer next to the first hit. Can be used as a condition which evaluates as logical false if none of the delimiters were found at the string |
| `0C17` | SF_STRLEN | Sf | SAMPFUNCS | 2 | Returns the length of a string |
| `0C18` | SF_STRSTR | Sf | SAMPFUNCS | 3 | Returns a pointer to the first occurence of a specified substring in the source string |
| `0C19` | SF_STRCSPN | Sf | SAMPFUNCS | 3 | Searches the string for any matching characters at the characterList. Returns the character index of the first occurence from the string and evaluates as logical true if used as a condition. Returns the length of the string if nothing matched the characterSet |
| `0C1A` | SF_ATOI | Sf | SAMPFUNCS | 2 | Converts an ascii string into a decimal integer |
| `0C1B` | SF_ATOF | Sf | SAMPFUNCS | 2 | Converts an ascii string into a floating point number |
| `0C1C` | SF_ITOA | Sf | SAMPFUNCS | 3 | Converts a baseN integer into an ascii string then stores it to stringBuffer |
| `0C1D` | SF_READ_ELEMENT_OF_SIZED_ARRAY | Sf | SAMPFUNCS | 4 | Reads the value of the sized array's element at index. The size per element is constrained between 1 to 4 |
| `0C1E` | SF_WRITE_ELEMENT_OF_SIZED_ARRAY | Sf | SAMPFUNCS | 4 | Writes the value to the specified element index of a sized array. The size per element is constrained between 1 to 4 |
| `0C1F` | SF_GET_ELEMENT_POINTER_OF_BUFFER_ARRAY | Sf | SAMPFUNCS | 4 | Returns a pointer to the element of an array of sized buffers using its element index |
| `0C20` | SF_WRITE_STRING_TO_ELEMENT_OF_BUFFER_ARRAY | Sf | SAMPFUNCS | 4 | Writes a string at the buffer element of an array of sized buffers using its element index |
| `0C21` | SF_STRIEQ | Sf | SAMPFUNCS | 2 | Evaluates as logical true if both case-insensitive strings are equal |
| `0C22` | SF_BIN_TO_HEX | Sf | SAMPFUNCS | 3 | Converts binary text to hexadecimal text and stores at stringBuffer. Can be used as a condition which evaluates as logical false if the bufferSize is not enough to contain the converted hexadecimal text |
| `0C23` | SF_HEX_TO_BIN | Sf | SAMPFUNCS | 3 | Converts hexadecimal text to binary text and stores at stringBuffer. Can be used as a condition which evaluates as logical false if the bufferSize is not enough to contain the converted binary text |
| `0C24` | SF_STRNCPY | Sf | SAMPFUNCS | 3 | Copies the string safely from source to stringBuffer. The copied string will be truncated if the occupied size is beyond the specified bufferSize |
| `0C25` | SF_STRNEQ | Sf | SAMPFUNCS | 3 | Evaluates as logical true if all characters with length at the beginning of both case-sensitive strings are equal |
| `0C26` | SF_STRUPR | Sf | SAMPFUNCS | 2 | Converts all letters of the source's string into CAPITAL LETTERS stored at destination |
| `0C27` | SF_STRNCAT | Sf | SAMPFUNCS | 3 | Appends a appendedString safely at the end of the string found at the stringBuffer. The appendedString will be truncated if the overall size is beyond the specified bufferSize |
| `0C28` | SF_STRLWR | Sf | SAMPFUNCS | 2 | Converts all letters of the source's string into non-capital letters stored at destination |
| `0C29` | SF_STRISTR | Sf | SAMPFUNCS | 3 | Returns a pointer to the first case-insensitive occurence of the specified substring in the source string |
| `0C2A` | SF_STRCHR | Sf | SAMPFUNCS | 3 | Returns a pointer to the first occurence of the specified ascii character in the source string |
| `0C2B` | SF_STRPBRK | Sf | SAMPFUNCS | 3 | Searches the source's string for any matching characters at the characterList. Returns a pointer to the first occurence from the source's string and evaluates as logical true if used as a condition |
| `0C2C` | SF_STRRCHR | Sf | SAMPFUNCS | 3 | Returns a pointer to the last occurence of the specified ascii character in the source string |
| `0C2D` | SF_STRREV | Sf | SAMPFUNCS | 2 | Reverses the source's string, changing the positions of characters, then stores it to the destination |
| `0C2E` | SF_STRSPN | Sf | SAMPFUNCS | 3 | Searches the source's string then returns the index of the first character that does not match any of the specified characters in the characterList and evaluates as logical true if used as a condition. Returns the length of the string if all characters matches any characters at the characterList |
| `0C2F` | SF_STRTOL | Sf | SAMPFUNCS | 4 | Ignores any whitespace at the beginning of the source's string, converting the next characters into a baseN longInteger. The scanning stops when it comes across the first non-integer character, stores its pointer to unscannedAddress |
| `0C30` | SF_MATRIX_TO_QUAT | Sf | SAMPFUNCS | 2 | Converts a matrix structure into a quaternion structure stored at quaternionBuffer |
| `0C31` | SF_QUAT_TO_MATRIX | Sf | SAMPFUNCS | 2 | Converts a quaternion structure into a matrix structure stored at matrixBuffer |
| `0C32` | SF_AXES_TO_QUAT | Sf | SAMPFUNCS | 13 | Converts the basis vectors of a rotation matrix into quaternion values |
| `0C33` | SF_QUAT_TO_AXES | Sf | SAMPFUNCS | 13 | Converts the quaternion values into basis vectors of a rotation matrix |
| `0C34` | SF_REGISTER_CUSTOM_GLOBAL_FUNCTION | SfGFunc | SAMPFUNCS | 2 | Registers the name of a custom global function allowing other scripts to call it using SF_CALL_CUSTOM_GLOBAL_FUNCTION command |
| `0C35` | SF_CALL_CUSTOM_GLOBAL_FUNCTION | SfGFunc | SAMPFUNCS | 3 | Calls a registered custom global function with name |
| `0C36` | SF_CUSTOM_GLOBAL_FUNCTION_RETURN | SfGFunc | SAMPFUNCS | 2 | Returns the flow of the execution to the next instruction after the custom global function call, optionally returning one or more parameters as result |
| `0C37` | SF_IS_CUSTOM_GLOBAL_FUNCTION_REGISTERED | SfGFunc | SAMPFUNCS | 1 | Evaluates as logical true if the specified name is registered a custom global function |
| `0C38` | SF_CUSTOM_GLOBAL_FUNCTION_GET_ORIGIN | SfGFunc | SAMPFUNCS | 3 | Returns the origin informations of a custom global function with name |
| `0C39` | SF_UNREGISTER_CUSTOM_GLOBAL_FUNCTION | SfGFunc | SAMPFUNCS | 1 | Removes the currently registered custom global function. Allowing its name to be re-registered by SF_REGISTER_CUSTOM_GLOBAL_FUNCTION command |
| `0C3A` | SF_STRING_POINTER | Sf | SAMPFUNCS | 3 | Stores a pointer to the specified string into the variable |
| `0C3B` | SF_D3D_BEGIN |  | SAMPFUNCS | 1 | Begins the D3D primitiveType used for rendering |
| `0C3C` | SF_D3D_END |  | SAMPFUNCS | 0 | Calls the D3D EndScene method |
| `0C3D` | SF_D3D_COLOR |  | SAMPFUNCS | 1 | Sets the D3D's current drawing color |
| `0C3E` | SF_D3D_VERTEX |  | SAMPFUNCS | 2 | Sets a vertex using the currently used primitive type specified by SF_D3D_BEGIN |
| `0C3F` | SF_D3D_SET_TEXTURE_COORDS |  | SAMPFUNCS | 2 | Sets the Texture Coordinates of the D3D primitive |
| `0C40` | SF_D3D_BIND_TEXTURE |  | SAMPFUNCS | 1 | Binds a Texture to our D3D primitive |
| `0C41` | SF_D3D_TEXTURE_STRUCT |  | SAMPFUNCS | 2 | This command has no documention provided by the SF author |
| `0C42` | SF_D3D_TEXTURE_SPRITE |  | SAMPFUNCS | 2 | This command has no documention provided by the SF author |
| `0C43` | SF_D3D_GET_TEXTURE_SIZE |  | SAMPFUNCS | 3 | Returns the dimensions occupied by texture structure |
| `0C44` | SF_D3D_SET_RENDER_STATE |  | SAMPFUNCS | 2 | Sets the rendering status of a D3D primitiveType |
| `0C45` | SAMP_CREATE_3D_TEXT_WITH_ID | SampTextLabel3D | SAMPFUNCS | 10 | Creates/overwrites a 3D text with the specified ID |
| `0C46` | SAMP_GET_3D_TEXT_PARAMS | SampTextLabel3D | SAMPFUNCS | 10 | Returns all the informations about a SampTextLabel3D using its ID |
| `0C47` | SAMP_SET_3D_TEXT | SampTextLabel3D | SAMPFUNCS | 2 | Sets new text for 3D text |
| `0C48` | SAMP_CREATE_TEXTDRAW | SampTextDraw | SAMPFUNCS | 4 | Modifies a textdraw with the specified parameters, creating it if it doesn't exist |
| `0C49` | SAMP_SET_TEXTDRAW_BOX | SampTextDraw | SAMPFUNCS | 5 | Sets the parameters of the "box" (rectangle) of the text draw |
| `0C4A` | SAMP_SET_TEXTDRAW_ALIGNMENT | SampTextDraw | SAMPFUNCS | 2 | Sets the alignment of the text in the textdraw |
| `0C4B` | SAMP_SET_TEXTDRAW_PROPORTIONALITY | SampTextDraw | SAMPFUNCS | 2 | Sets whether the text scaling status is proportional to the text draw or not |
| `0C4C` | SAMP_SET_TEXTDRAW_STYLE | SampTextDraw | SAMPFUNCS | 2 | Sets the text draw style |
| `0C4D` | SAMP_SET_TEXTDRAW_SHADOW | SampTextDraw | SAMPFUNCS | 3 | Sets a shadow on the text draw |
| `0C4E` | SAMP_SET_TEXTDRAW_OUTLINE | SampTextDraw | SAMPFUNCS | 3 | Sets the outline of the text draw |
| `0C4F` | SAMP_SET_TEXTDRAW_MODEL | SampTextDraw | SAMPFUNCS | 8 | Sets the model (object, auto) of the text draw for style 5 |
| `0C50` | SAMP_SET_TEXTDRAW_TEXT | SampTextDraw | SAMPFUNCS | 2 | Sets the text of the textdraw |
| `0C51` | SAMP_SET_TEXTDRAW_COORDS | SampTextDraw | SAMPFUNCS | 3 | Sets the gamescreen coordinates of the textdraw |
| `0C52` | SAMP_SET_TEXTDRAW_CHARACTER_PROPERTIES | SampTextDraw | SAMPFUNCS | 4 | Sets the size and color property of all characters in the textdraw |
| `0C53` | SAMP_GET_TEXTDRAW_BOX | SampTextDraw | SAMPFUNCS | 5 | Returns the parameters of the "box" (rectangle) of the specified text draw |
| `0C54` | SAMP_GET_TEXTDRAW_ALIGNMENT | SampTextDraw | SAMPFUNCS | 2 | Sets the alignment of the text in the textdraw |
| `0C55` | SAMP_GET_TEXTDRAW_PROPORTIONALITY | SampTextDraw | SAMPFUNCS | 2 | Returns true if the text scaling status is proportional to the text draw |
| `0C56` | SAMP_GET_TEXTDRAW_STYLE | SampTextDraw | SAMPFUNCS | 2 | Returns the text draw style |
| `0C57` | SAMP_GET_TEXTDRAW_SHADOW | SampTextDraw | SAMPFUNCS | 3 | Returns the tickness and color property of the text draw's shadow |
| `0C58` | SAMP_GET_TEXTDRAW_OUTLINE | SampTextDraw | SAMPFUNCS | 3 | Returns the tickness and color property of the text draw's outline |
| `0C59` | SAMP_GET_TEXTDRAW_MODEL | SampTextDraw | SAMPFUNCS | 8 | Returns the properties of the text draw as a model (style 5) |
| `0C5A` | SAMP_STORE_TEXTDRAW_TEXT | SampTextDraw | SAMPFUNCS | 2 | Stores the textdraw's text to stringBuffer |
| `0C5B` | SAMP_GET_TEXTDRAW_COORDS | SampTextDraw | SAMPFUNCS | 3 | Returns the gamescreen coordinates of the textdraw |
| `0C5C` | SAMP_GET_TEXTDRAW_CHARACTER_PROPERTIES | SampTextDraw | SAMPFUNCS | 4 | Returns the size and color property of all characters in the textdraw |
| `0C5D` | SAMP_DOES_TEXTDRAW_EXIST | SampTextDraw | SAMPFUNCS | 1 | Evaluates as logical true if the specified textdraw exists |
| `0C5E` | SAMP_DELETE_TEXTDRAW | SampTextDraw | SAMPFUNCS | 1 | Deletes the specified textdraw |
| `0C5F` | SF_DOES_CUSTOM_GLOBAL_VARIABLE_EXIST | SfGVar | SAMPFUNCS | 1 | Evaluates as logical true if a custom global variable with specified name existed |
| `0C60` | SF_SET_CUSTOM_GLOBAL_VARIABLE_SCOPE | SfGVar | SAMPFUNCS | 4 | Sets whether the specified script can read or write to the specified custom global variable |
| `0C61` | SF_GET_CUSTOM_GLOBAL_VARIABLE_SCOPE | SfGVar | SAMPFUNCS | 4 | Returns the specified script's read/write permissions to the specified custom global variable |
| `0C62` | SF_EXECUTE_CONSOLE_COMMAND | SfConsole | SAMPFUNCS | 1 | Executes the specified command in the SAMPFUNCS console |
| `0C63` | SF_REGISTER_CONSOLE_COMMAND | SfConsole | SAMPFUNCS | 2 | Registers a callback hooked on a SAMPFUNCS console command with maximum length of 64 characters |
| `0C64` | SF_UNREGISTER_CONSOLE_COMMAND | SfConsole | SAMPFUNCS | 1 | Removes the specified SAMPFUNCS console command. This command does nothing if the the specified command isn't a registered in the SAMPFUNCS console then evaluates as logical false if used as a condition |
| `0C65` | SF_DOWNLOAD_FILE | SfDownload | SAMPFUNCS | 3 | Downloads a file from the specified url source asynchronosly then saves it to filepath. Returns a handle to this file's SfDownload object for tracking purposes |
| `0C66` | SF_GET_DOWNLOAD_STATE | SfDownload | SAMPFUNCS | 2 | Returns the download status of the SfDownload object |
| `0C67` | SF_STORE_OS_ENVIRONMENT_VARIABLE | Sf | SAMPFUNCS | 3 | Stores the contents of the specified Windows variable (or environment variable) name to buffer |
| `0C68` | SF_UNICODE_TO_ANSI | Sf | SAMPFUNCS | 3 | Converts a Unicode string to ANSI string then stores it to ansiStringBuffer |
| `0C69` | SF_ANSI_TO_UNICODE | Sf | SAMPFUNCS | 3 | Converts an ANSI string to Unicode string then stores it to ansiStringBuffer |
| `0C6A` | SF_START_NEW_SCRIPT_FROM_LABEL | SfScript | SAMPFUNCS | 3 | Starts a new script from the specified scriptLabel then stores its pointer at newScriptPtrTo parameter |
| `0C6B` | SF_START_NEW_SCRIPT_FROM_POINTER | SfScript | SAMPFUNCS | 3 | Starts a new script from the specified memory location where a script binary data is stored (scriptBin) then stores its pointer at newScriptPtrTo parameter |
| `0C6C` | SF_SET_SCRIPT_LOCAL_VARIABLE | SfScript | SAMPFUNCS | 3 | Sets the values for a local variable in the specified script |
| `0C6D` | SF_GET_SCRIPT_LOCAL_VARIABLE | SfScript | SAMPFUNCS | 3 | Returns the value of a local variable in the specified script |
| `0C6E` | SF_TERMINATE_SCRIPT | SfScript | SAMPFUNCS | 1 | Terminates a script pointed by the address |
| `0C6F` | SF_RESTART_SCRIPT | SfScript | SAMPFUNCS | 2 | Restarts a script pointed by the address |
| `0C70` | SF_GET_LOADED_MODULE | Sf | SAMPFUNCS | 2 | Returns the handle of a loaded module with name (moduleName) |
| `0C71` | SF_GET_MODULE_PROCEDURE | Sf | SAMPFUNCS | 3 | Returns a pointer (functionPtr) to specified functionName inside the moduleHandle |
| `0C72` | SF_SET_KEY_STATUS | Sf | SAMPFUNCS | 2 | Sets whether a specific virtual key code is pressed or not |
| `0C73` | SF_SET_CHARACTER_KEY_STATUS | Sf | SAMPFUNCS | 2 | Sets whether a specific virtual key represented in ascii character format is pressed or not |
| `0C74` | SF_CREATE_TIMER | SfTimer | SAMPFUNCS | 3 | Creates and starts an SfTimer object that periodically executes its callback upon expiration |
| `0C75` | SF_DELETE_TIMER | SfTimer | SAMPFUNCS | 1 | Removes the specified SfTimer object, freeing it from memory |
| `0C76` | SF_RESET_TIMER | SfTimer | SAMPFUNCS | 1 | Resets the expiration time of the SfTimer, restarting its trigger countdown |
| `0C77` | SF_SET_TIMER_INTERVAL | SfTimer | SAMPFUNCS | 2 | Sets a new interval for the SfTimer |
| `0C78` | SF_SET_TIMER_STATUS | SfTimer | SAMPFUNCS | 2 | Activates or pauses an SfTimer's functionality |
| `0C79` | SF_IS_TIMER_ACTIVE | SfTimer | SAMPFUNCS | 1 | Evaluates as logical true if the SfTimer is active |
| `0C7A` | SF_GET_TIMER_INTERVAL | SfTimer | SAMPFUNCS | 2 | Returns the SfTimer's configured interval |
| `0C7B` | SF_GET_TIMER_ELAPSED_TIME | SfTimer | SAMPFUNCS | 2 | Returns the number of milliseconds that have passed since the last SfTimer reset (including after the interval has passed) |
| `0C7C` | SF_GET_TIMER_TIME_LEFT | SfTimer | SAMPFUNCS | 2 | Returns the number of milliseconds remaining before the SfTimer expires (decremented if the timer is active) |
| `0C7D` | SF_RELEASE_DOWNLOAD | SfDownload | SAMPFUNCS | 1 | Frees an SfDownload object from memory |
| `0C7E` | SF_IS_CONSOLE_OPEN | SfConsole | SAMPFUNCS | 0 | Evaluates as logical true if the SAMPFUNCS console is open |
| `0C7F` | SAMP_SET_LOCAL_CHAT_COMMAND_DESCRIPTION | SampLocalChatCmd | SAMPFUNCS | 2 | Sets the description for the local command |
| `0C80` | SF_SET_CONSOLE_COMMAND_DESCRIPTION | SfConsole | SAMPFUNCS | 2 | Sets the description for the console command |
| `0C81` | SAMP_FORCE_DRIVING_SYNC | SampRaknet | SAMPFUNCS | 1 | Sends SampPacket.DrivingSync to server about our character driving a car with ID |
| `0C82` | SAMP_FORCE_UNOCCUPIED_SYNC | SampRaknet | SAMPFUNCS | 2 | Sends SampPacket.UnoccupiedCarSync to server about a seatId of a car with carId being unoccupied |
| `0C83` | SAMP_FORCE_ONFOOT_SYNC | SampRaknet | SAMPFUNCS | 0 | Sends SampPacket.OnFootSync to server about our character being onfoot |
| `0C84` | SAMP_FORCE_AIM_SYNC | SampRaknet | SAMPFUNCS | 0 | Sends SampPacket.AimSync containing our current aim data, to server |
| `0C85` | SAMP_FORCE_TRAILER_SYNC | SampRaknet | SAMPFUNCS | 1 | Sends SampPacket.TrailerSync to server about a trailer with ID being attached to our player |
| `0C86` | SAMP_FORCE_PASSENGER_SYNC | SampRaknet | SAMPFUNCS | 2 | Sends SampPacket.PassengerSync to server about our character sitting at seatId of a car with carId |
| `0C87` | SAMP_FORCE_STATS_SYNC | SampRaknet | SAMPFUNCS | 0 | Sends SampPacket.StatsUpdate containing our current money and drunk level, to server |
| `0C88` | SAMP_FORCE_WEAPONS_SYNC | SampRaknet | SAMPFUNCS | 0 | Sends SampPacket.WeaponsUpdate containing our character's current weapons, to server |
| `0C89` | SF_KEY_JUST_PRESSED | Sf | SAMPFUNCS | 1 | Evaluates as logical true if the specified virtual keyCode has been pressed just now |
| `0C8A` | SAMP_GET_MAX_PLAYER_ID | SampClient | SAMPFUNCS | 2 | Returns the maximum player ID currently streamed if streamedOnly = true. Else, returns the maximum player ID allowed in the server |
| `0C8B` | SAMP_GET_PLAYER_COUNT | SampClient | SAMPFUNCS | 2 | Returns the number of players that are currently streamed if streamedOnly = true. Else, returns the number of players allowed in the server |
| `0C8C` | SF_D3D_LOAD_TEXTURE_FROM_FILE_IN_MEMORY | SfD3DTexture | SAMPFUNCS | 3 | Loads a texture from a file located in memory buffer |
| `0C8D` | SF_WRITE_TEXT_TO_CLIPBOARD | Sf | SAMPFUNCS | 1 | Sets the text on the clipboard |
| `0C8E` | SF_READ_DATA_FROM_CLIPBOARD | Sf | SAMPFUNCS | 2 | Copies raw binary or text from the clipboard to buffer |
| `0C8F` | SAMP_PROCESS_CHAT_INPUT | SampChatInput | SAMPFUNCS | 1 | Processes a message by SAMPFUNCS callbacks, then sent to server as SampRpc.Chat |
| `0C90` | SAMP_IS_CHAT_COMMAND_HOOKED | SampLocalChatCmd | SAMPFUNCS | 1 | Evaluates as logical true if the specified command is localized by a callback hook |
| `0C91` | SF_IS_CONSOLE_COMMAND_REGISTERED | SfConsole | SAMPFUNCS | 1 | Returns logical true if the specified console command is registered |
| `0C92` | SF_GET_CLEO_LIBRARY_VERSION | Sf | SAMPFUNCS | 1 | Returns the installed version of CLEO |
| `0D00` | MULTIPLY_MATRICES | Matrix | NewOpcodes | 3 | Multiplies matrices |
| `0D01` | ROTATE_MATRIX_ON_AXIS |  | CLEO+ | 6 |  |
| `0D01` | ROTATE_MATRIX_ON_AXIS | Matrix | NewOpcodes | 6 | Rotates matrix on axis |
| `0D02` | GET_MATRIX_X_ANGLE |  | CLEO+ | 2 |  |
| `0D02` | GET_MATRIX_X_ANGLE | Matrix | NewOpcodes | 2 | Gets the X angle of matrix (in degrees) |
| `0D03` | GET_MATRIX_Y_ANGLE |  | CLEO+ | 2 |  |
| `0D03` | GET_MATRIX_Y_ANGLE | Matrix | NewOpcodes | 2 | Gets the Y angle of matrix (in degrees) |
| `0D04` | GET_MATRIX_Z_ANGLE |  | CLEO+ | 2 |  |
| `0D04` | GET_MATRIX_Z_ANGLE | Matrix | NewOpcodes | 2 | Gets the Z angle of matrix (in degrees) |
| `0D05` | SET_MATRIX_POSITION | Matrix | NewOpcodes | 4 | Sets position for matrix |
| `0D06` | GET_MATRIX_POSITION |  | NewOpcodes | 4 | Gets position of matrix |
| `0D07` | GET_COORDS_OFFSETS_RELATIVE_TO_MATRIX |  | NewOpcodes | 7 | Gets point relative offset on matrix |
| `0D08` | SET_MATRIX_ROTATION | Matrix | NewOpcodes | 4 | Sets matrix angles |
| `0D09` | COPY_MATRIX | Matrix | NewOpcodes | 2 | Copies matrix to another matrix |
| `0D0A` | GET_OFFSET_FROM_MATRIX_IN_WORLD_COORDS |  | CLEO+ | 7 |  |
| `0D0A` | GET_OFFSET_FROM_MATRIX_IN_WORLD_COORDS | Matrix | NewOpcodes | 7 | Gets coords on offset from matrix |
| `0D0B` | GET_CHAR_BONE_MATRIX | Char | CLEO+ | 3 | Returns the address of the character's specified bone matrix |
| `0D0B` | GET_CHAR_BONE_MATRIX |  | NewOpcodes | 3 | Gets char's bone world matrix |
| `0D0C` | GET_CAR_COMPONENT_MATRIX | Car | NewOpcodes | 3 | Gets matrix of car component |
| `0D0D` | GET_CAR_COMPONENT | Car | NewOpcodes | 3 | Gets car component by name |
| `0D0E` | SET_CAR_COMPONENT_STATE |  | NewOpcodes | 3 | Sets component state |
| `0D0F` | SET_CAR_MODEL_ALPHA | Car | CLEO+ | 2 | Set's the specified car's transparency alpha |
| `0D0F` | SET_CAR_MODEL_ALPHA |  | NewOpcodes | 2 | Sets alpha value for car's model |
| `0D10` | SET_CHAR_MODEL_ALPHA | Char | CLEO+ | 2 | Set's the specified character's transparency alpha |
| `0D10` | SET_CHAR_MODEL_ALPHA |  | NewOpcodes | 2 | Sets alpha value for char's model |
| `0D11` | SET_OBJECT_MODEL_ALPHA | Object | CLEO+ | 2 | Set's the specified object's transparency alpha |
| `0D11` | SET_OBJECT_MODEL_ALPHA |  | NewOpcodes | 2 | Sets alpha value for object's model |
| `0D12` | SET_CAR_COMPONENT_MODEL_ALPHA | Car | NewOpcodes | 3 | Sets alpha value for car's component model |
| `0D13` | SET_MATRIX_X_ROTATION |  | NewOpcodes | 2 | Sets matrix x angle |
| `0D14` | SET_MATRIX_Y_ROTATION |  | NewOpcodes | 2 | Sets matrix y angle |
| `0D15` | SET_MATRIX_Z_ROTATION |  | NewOpcodes | 2 | Sets matrix z angle |
| `0D16` | SET_MATRIX_ROTATION_FROM_QUAT |  | CLEO+ | 2 |  |
| `0D16` | SET_MATRIX_ROTATION_FROM_QUAT |  | NewOpcodes | 2 | Sets matrix rotation from quaternion |
| `0D17` | SET_QUAT_FROM_MATRIX |  | CLEO+ | 2 |  |
| `0D17` | SET_QUAT_FROM_MATRIX |  | NewOpcodes | 2 | Sets quaternion from matrix |
| `0D18` | ROTATE_QUAT_ON_AXIS |  | CLEO+ | 6 |  |
| `0D18` | ROTATE_QUAT_ON_AXIS |  | NewOpcodes | 6 | Rotates quaternion |
| `0D19` | GET_NORMALISED_QUAT |  | CLEO+ | 2 |  |
| `0D19` | GET_NORMALISED_QUAT |  | NewOpcodes | 2 | Normalizes quaternion |
| `0D1A` | MULTIPLY_QUATS |  | CLEO+ | 3 |  |
| `0D1A` | MULTIPLY_QUATS |  | NewOpcodes | 3 | Multiplies quaternions |
| `0D1B` | GET_ENTITY_TYPE_AND_CLASS |  | NewOpcodes | 3 | Gets information about entity type |
| `0D1C` | NORMALISE_VECTOR |  | NewOpcodes | 1 | Normalizes vector |
| `0D1D` | INTERPOLATE_MATRIX |  | NewOpcodes | 4 | Performs matrix slerp |
| `0D1E` | QUAT_SLERP |  | CLEO+ | 4 |  |
| `0D1E` | QUAT_SLERP |  | NewOpcodes | 4 | Performs quaternion slerp |
| `0D1F` | GET_COMPONENT_CHILD_COMPONENT | Component | NewOpcodes | 2 | Gets component child component |
| `0D20` | GET_COMPONENT_NEXT_COMPONENT | Component | NewOpcodes | 2 | Gets component next component |
| `0D21` | GET_COMPONENT_NAME | Component | NewOpcodes | 2 | Gets component name component |
| `0D22` | GET_COMPONENT_WORLD_MATRIX | Component | NewOpcodes | 2 | Gets component world matrix |
| `0D23` | GET_COMPONENT_MODELLING_MATRIX | Component | NewOpcodes | 2 | Gets component modelling matrix |
| `0D24` | INITIALISE_QUAT |  | CLEO+ | 5 |  |
| `0D24` | INITIALISE_QUAT |  | NewOpcodes | 5 | Sets quaternion elements |
| `0D25` | INITIALISE_MATRIX |  | NewOpcodes | 17 | Sets matrix elements |
| `0D26` | INITIALISE_VECTOR |  | NewOpcodes | 4 | Sets vector elements |
| `0D27` | COPY_MEMORY | Memory | CLEO+ | 3 | Copies each memory byte from src address to dest address |
| `0D27` | MEMCPY |  | NewOpcodes | 3 | Copies block of memory |
| `0D28` | GET_VECTOR_ELEMENTS |  | NewOpcodes | 4 | Gets vector elements |
| `0D29` | GET_QUAT_ELEMENTS |  | CLEO+ | 5 |  |
| `0D29` | GET_QUAT_ELEMENTS |  | NewOpcodes | 5 | Gets quaternion elements |
| `0D2A` | GET_CAR_NUM_COLLIDED_ENTITIES |  | NewOpcodes | 2 | Gets car number of collided entities |
| `0D2B` | GET_CHAR_NUM_COLLIDED_ENTITIES |  | NewOpcodes | 2 | Gets char number of collided entities |
| `0D2C` | GET_OBJECT_NUM_COLLIDED_ENTITIES |  | NewOpcodes | 2 | Gets object number of collided entities |
| `0D2D` | GET_LOCAL_TIME | Clock | CLEO+ | 8 | Returns the full local time of the player's PC |
| `0D2D` | GET_LOCAL_TIME |  | NewOpcodes | 8 | Gets current time from OS |
| `0D2E` | SET_SCRIPT_VAR |  | CLEO+ | 3 | Sets value for script variable in index |
| `0D2E` | SET_THREAD_VAR |  | NewOpcodes | 3 | Sets value of thread's local variable |
| `0D2F` | GET_SCRIPT_VAR |  | CLEO+ | 3 | Gets value from script variable index |
| `0D2F` | GET_THREAD_VAR |  | NewOpcodes | 3 | Gets value of thread's local variable |
| `0D30` | GET_CHAR_BONE | Char | CLEO+ | 3 |  |
| `0D30` | GET_CHAR_BONE |  | NewOpcodes | 3 | Gets char's bone |
| `0D31` | GET_BONE_OFFSET_VECTOR | Char | CLEO+ | 2 |  |
| `0D31` | GET_BONE_OFFSET |  | NewOpcodes | 2 | Gets bone offset |
| `0D32` | GET_BONE_QUAT | Char | CLEO+ | 2 | Returns pointer to the quaterion under bone address obtained with GET_CHAR_BONE |
| `0D32` | GET_BONE_QUAT |  | NewOpcodes | 2 | Returns pointer to the quaterion under bone address obtained with GET_CHAR_BONE |
| `0D33` | SET_CAR_DOOR_WINDOW_STATE | Car | CLEO+ | 3 | Sets the window state of the specified door of the car |
| `0D33` | SET_CAR_DOOR_WINDOW_STATE |  | NewOpcodes | 3 | Sets car window state |
| `0D34` | GET_CAR_COLLIDED_ENTITIES |  | NewOpcodes | 7 | Stores car collided entities |
| `0D35` | GET_CHAR_COLLIDED_ENTITIES |  | NewOpcodes | 7 | Stores char collided entities |
| `0D36` | GET_OBJECT_COLLIDED_ENTITIES |  | NewOpcodes | 7 | Stores object collided entities |
| `0D37` | WRITE_STRUCT_PARAM | Memory | CLEO+ | 3 | Writes the dword value to the struct address by index (index*4+address) see: 0E28 |
| `0D37` | SET_STRUCT_PARAM |  | NewOpcodes | 3 | Sets struct with 4b alignment param value |
| `0D38` | READ_STRUCT_PARAM | Memory | CLEO+ | 3 | Reads the dword value from the struct address by index (index*4+address) see: 0D4E |
| `0D38` | GET_STRUCT_PARAM |  | NewOpcodes | 3 | Gets struct with 4b alignment param value |
| `0D39` | GET_CHAR_MAX_HEALTH | Char | CLEO+ | 2 | Returns the character's maximum health (08AF) |
| `0D39` | GET_CHAR_MAX_HEALTH |  | NewOpcodes | 2 | Gets char max health value |
| `0D3A` | GET_COLLISION_BETWEEN_POINTS | ColPoint | CLEO+ | 20 | Returns the colPoint, coordinates, and collision entity between two points |
| `0D3A` | GET_COLLISION_BETWEEN_POINTS |  | NewOpcodes | 20 | Gets collision data between two points |
| `0D3B` | GET_COLPOINT_NORMAL_VECTOR | ColPoint | CLEO+ | 4 | Returns the vector of the specified ColPoint |
| `0D3B` | GET_COL_DATA_NORMAL_VECTOR |  | NewOpcodes | 4 | Gets colpoint normal vector |
| `0D3C` | GET_COLPOINT_SURFACE | ColPoint | CLEO+ | 2 | Returns the surfaceType of the specified ColPoint |
| `0D3C` | GET_COL_DATA_SURFACE |  | NewOpcodes | 2 | Gets colpoint data surface ID |
| `0D3D` | GET_COL_DATA_LIGHTING |  | NewOpcodes | 2 | Gets colpoint data lighting value |
| `0D3E` | GET_COLPOINT_DEPTH | ColPoint | CLEO+ | 2 | Returns the depth of the specified ColPoint |
| `0D3E` | GET_COL_DATA_DEPTH |  | NewOpcodes | 2 | Gets colpoint data depth value |
| `0D3F` | FIND_INTERSECTION_BETWEEN_CIRCLES |  | NewOpcodes | 10 | Finds intersection coordinates between two circles |
| `0D40` | DRAW_SHAPE |  | NewOpcodes | 8 | Draws 2D shape |
| `0D41` | SETUP_SHAPE_VERTEX |  | NewOpcodes | 14 | Sets vertex params |
| `0D42` | LOAD_TXD |  | NewOpcodes | 2 | Loads txd from file |
| `0D43` | GET_TXD_ID |  | NewOpcodes | 2 | Gets txd's id |
| `0D44` | FIND_TEXTURE_IN_TXD_WITH_NAME |  | NewOpcodes | 3 | Finds texture in txd |
| `0D45` | ROTATE_SHAPE_VERTICES |  | NewOpcodes | 5 | Rotates vertices of 2D shape around point |
| `0D46` | FIND_TEXTURE_IN_TXD_WITH_ID |  | NewOpcodes | 3 | Finds texture in txd |
| `0D47` | GET_MODEL_TXD_ID |  | NewOpcodes | 2 | Gets txd's id for model |
| `0D48` | GET_MODEL_CRC |  | NewOpcodes | 2 | Gets model's CRC32 key |
| `0D49` | STRING_CMP |  | NewOpcodes | 3 | Compares two strings |
| `0D4A` | STRING_CAT |  | NewOpcodes | 2 | Concatenates two strings |
| `0D4B` | STRING_STR |  | NewOpcodes | 3 | Finds the first occurrence of a string |
| `0D4C` | GET_STRING_LENGTH | Text | CLEO+ | 2 | Returns the string length |
| `0D4C` | STRING_LEN |  | NewOpcodes | 2 | Gets string length |
| `0D4D` | COPY_STRING | Text | CLEO+ | 2 | Copies the string to the specified address |
| `0D4D` | STRING_CPY |  | NewOpcodes | 2 | Copies string to another string |
| `0D4E` | READ_STRUCT_OFFSET | Memory | CLEO+ | 4 | Reads a value from the given offset from the memory address (see: 0D38) |
| `0D4E` | GET_STRUCT_FIELD |  | NewOpcodes | 4 | Gets value at struct offset |
| `0D4F` | SET_STRUCT_FIELD |  | NewOpcodes | 4 | Sets value at struct offset |
| `0D50` | DRAW_TEMPORARY_SHADOW |  | NewOpcodes | 14 | Draws shadow |
| `0D51` | DRAW_PERMANENT_SHADOW |  | NewOpcodes | 14 | Draws permanent shadow |
| `0D52` | DRAW_TEMPORARY_LIGHT |  | NewOpcodes | 12 | Draws light |
| `0D53` | DRAW_TEMPORARY_CORONA |  | NewOpcodes | 10 | Draws corona |
| `0D54` | DRAW_TEMPORARY_CORONA_EX |  | NewOpcodes | 18 | Draws corona with some extra parameters |
| `0D55` | GET_SUN_COLORS |  | NewOpcodes | 6 | Gets sun colors |
| `0D56` | GET_SUN_SCREEN_COORS |  | NewOpcodes | 2 | Gets sun 2D position |
| `0D57` | GET_SUN_WORLD_COORS |  | NewOpcodes | 3 | Gets sun 3D position |
| `0D58` | GET_SUN_SIZE |  | NewOpcodes | 2 | Gets sun size |
| `0D59` | GET_CURRENT_WEATHER | Weather | CLEO+ | 1 | Gets weather type that is being blended from |
| `0D59` | GET_CURRENT_WEATHER |  | NewOpcodes | 1 | Gets current weather |
| `0D5A` | GET_TRAFFICLIGHTS_CURRENT_COLOR |  | NewOpcodes | 2 | Gets trafficlight colors |
| `0D5B` | DRAW_SPOTLIGHT |  | NewOpcodes | 12 | Draws spotlight |
| `0D5C` | GET_CAR_LIGHT_DAMAGE_STATUS |  | NewOpcodes | 3 | Gets car light damaging state |
| `0D5D` | SET_CAR_LIGHT_DAMAGE_STATUS |  | NewOpcodes | 3 | Sets car light damaging state |
| `0D5E` | GET_VEHICLE_CLASS_AND_SUBCLASS |  | NewOpcodes | 3 | Gets vehicle class and subclass |
| `0D5F` | GET_VEHICLE_DUMMY_POSN |  | NewOpcodes | 7 | Gets vehicle dummy position |
| `0D60` | CREATE_PROJECTILE |  | NewOpcodes | 10 | Creates projectile |
| `0D61` | LOAD_TEXTURE_FROM_BMP_FILE | Texture | NewOpcodes | 3 | Loads texture from BMP file. Can be used with texture memory option to load file from memory |
| `0D64` | LOAD_TEXTURE_FROM_PNG_FILE | Texture | NewOpcodes | 2 | Loads texture from PNG file. Can be used with texturememory option to load file from memory |
| `0D65` | PRINT_TEMPORARY_TEXT |  | NewOpcodes | 6 | Prints a text into display ("light" version) |
| `0D66` | PRINT_TEMPORARY_TEXT_EX |  | NewOpcodes | 25 | Prints a text into display |
| `0D72` | GET_GAME_VOLUME |  | NewOpcodes | 3 | Gets game sfx and radio volume |
| `0D73` | GET_SCREEN_WIDTH_AND_HEIGHT |  | NewOpcodes | 3 | Gets screen width and height |
| `0D74` | GET_COMPONENT_PARENT_COMPONENT | Component | NewOpcodes | 2 | Gets component parent component |
| `0D75` | GET_COMPONENT_NUM_OBJECTS | Component | NewOpcodes | 2 | Gets component number of objects |
| `0D76` | GET_COMPONENT_OBJECT |  | NewOpcodes | 3 | Gets component object |
| `0D77` | HIDE_OBJECT_ATOMIC |  | NewOpcodes | 2 | Hides object atomic |
| `0D78` | GET_OBJECT_ATOMIC_FLAG |  | NewOpcodes | 3 | Gets object atomic flag |
| `0D79` | SET_OBJECT_ATOMIC_FLAG |  | NewOpcodes | 3 | Sets object atomic flag |
| `0D7A` | GET_OBJECT_ATOMIC_NUM_MATERIALS |  | NewOpcodes | 2 | Gets object atomic material texture |
| `0D7B` | GET_OBJECT_ATOMIC_MATERIAL_TEXTURE |  | NewOpcodes | 3 | Gets object atomic material texture |
| `0D7C` | LOAD_TEXTURE_FROM_DDS_FILE | Texture | NewOpcodes | 2 | Loads texture from DDS file |
| `0D7D` | CLEAN_LOADED_TEXTURE | Texture | NewOpcodes | 1 | Cleans loaded texture |
| `0D7E` | DRAW_2D_SPRITE | Sprite | NewOpcodes | 10 | Draws 2D sprite |
| `0D7F` | DRAW_2D_SPRITE_WITH_GRADIENT | Sprite | NewOpcodes | 22 | Draws 2D sprite with gradient |
| `0DD5` | GET_PLATFORM | Game | CLEO | 1 | Returns platform type info (device/operating system) |
| `0E00` | GET_CAR_ALARM | Car | CLEO+ | 2 | Returns the status of the car's alarm |
| `0E01` | CREATE_OBJECT_NO_SAVE | Object | CLEO+ | 7 | Creates an no save game object at the specified location, with the specified model |
| `0E02` | SET_CAR_GENERATOR_NO_SAVE | CarGenerator | CLEO+ | 1 |  |
| `0E03` | PERLIN_NOISE | Math | CLEO+ | 2 | Calculates the 1D Perlin simplex noise |
| `0E04` | GET_NEXT_WEATHER | Weather | CLEO+ | 1 | Gets weather type that is being blended to |
| `0E05` | SET_NEXT_WEATHER | Weather | CLEO+ | 1 | Sets weather type which will be blend to |
| `0E06` | GET_RAIN_INTENSITY | Weather | CLEO+ | 1 | Gets rain intensity in range of 0.0 to 1.0 |
| `0E07` | SET_RAIN_INTENSITY | Weather | CLEO+ | 1 | Sets rain intensity in range of 0.0 to 1.0 |
| `0E08` | IS_CAR_SCRIPT_CONTROLLED | Car | CLEO+ | 1 | Returns true if the specified vehicle is controlled by script |
| `0E09` | MARK_CAR_AS_NEEDED | Car | CLEO+ | 1 | Marks the vehicle as script controlled |
| `0E0A` | IS_CHAR_SCRIPT_CONTROLLED | Char | CLEO+ | 1 | Returns true if the specified character is controlled by script |
| `0E0B` | MARK_CHAR_AS_NEEDED | Char | CLEO+ | 1 | Marks the character as script controlled |
| `0E0C` | IS_OBJECT_SCRIPT_CONTROLLED | Object | CLEO+ | 1 | Returns true if the specified object is controlled by a script |
| `0E0D` | MARK_OBJECT_AS_NEEDED | Object | CLEO+ | 1 | marks object as script controlled |
| `0E0E` | GET_CURRENT_RESOLUTION | Game | CLEO+ | 2 | Gets the game window width and height resolution |
| `0E0F` | GET_FIXED_XY_ASPECT_RATIO | Hud | CLEO+ | 4 | Gets x and y values based on window aspect ratio, useful for text and hud scaling |
| `0E10` | IS_MOUSE_WHEEL_UP | Mouse | CLEO+ | 0 | Returns true if the mouse wheel has been scrolled up |
| `0E11` | IS_MOUSE_WHEEL_DOWN | Mouse | CLEO+ | 0 | Returns true if the mouse wheel has been scrolled down |
| `0E12` | GET_VEHICLE_SUBCLASS | Car | CLEO+ | 2 | Returns vehicle subclass, useful to check if vehicle is motorbike, bicycle, trailer etc |
| `0E13` | GET_ENTITY_TYPE | Entity | CLEO+ | 2 | Gets the type of the entity |
| `0E14` | INIT_EXTENDED_CHAR_VARS | Char | CLEO+ | 3 | Inits additional variables for this char. Identifier can be "AUTO" for unique ID based on script pointer |
| `0E15` | SET_EXTENDED_CHAR_VAR | Char | CLEO+ | 4 | Sets extended var value for this char. Requires initialization (0E14), otherwise returns false |
| `0E16` | GET_EXTENDED_CHAR_VAR | Char | CLEO+ | 4 | Gets extended var value for this char. Returns false if not initialized (0E14) |
| `0E17` | INIT_EXTENDED_CAR_VARS | Car | CLEO+ | 3 | Inits additional variables for this car. Identifier can be "AUTO" for unique ID based on script pointer |
| `0E18` | SET_EXTENDED_CAR_VAR | Car | CLEO+ | 4 | Sets extended var value for this car. Requires initialization (0E17), otherwise returns false |
| `0E19` | GET_EXTENDED_CAR_VAR | Car | CLEO+ | 4 | Gets extended var value for this car. Returns false if not initialized (0E17) |
| `0E1A` | INIT_EXTENDED_OBJECT_VARS | Object | CLEO+ | 3 | Inits additional variables for this object. Identifier can be "AUTO" for unique ID based on script pointer |
| `0E1B` | SET_EXTENDED_OBJECT_VAR | Object | CLEO+ | 4 | Sets extended var value for this object. Requires initialization (0E1A), otherwise returns false |
| `0E1C` | GET_EXTENDED_OBJECT_VAR | Object | CLEO+ | 4 | Gets extended var value for this char. Returns false if not initialized (0E1A) |
| `0E1D` | IS_ON_MISSION | Mission | CLEO+ | 0 | Returns true if the player is on a mission (the variable set in 0180 is not zero) |
| `0E1E` | DRAW_TEXTURE_PLUS | Txd | CLEO+ | 15 | Draws RwTexture or spriteSlot once on specific drawing event and optional mask, no limits |
| `0E1F` | EASE | Math | CLEO+ | 4 | Eases k value in range of 0.0 to 1.0, resulting in a easing value based on mode and way, useful for smooth animations |
| `0E20` | IS_ON_SAMP | Game | CLEO+ | 0 | Returns true if the current game runs on San Andreas Multiplayer (SA-MP) |
| `0E21` | GET_AUDIO_SFX_VOLUME | Audio | CLEO+ | 1 | Gets the SFX volume set in the game options |
| `0E22` | GET_AUDIO_RADIO_VOLUME | Audio | CLEO+ | 1 | Gets the radio volume set in the game options |
| `0E23` | GET_MOUSE_SENSIBILITY | Mouse | CLEO+ | 1 | Gets the mouse sensibility set in the game options |
| `0E24` | FIX_CHAR_GROUND_BRIGHTNESS_AND_FADE_IN | Char | CLEO+ | 4 |  |
| `0E25` | IS_ON_CUTSCENE | Cutscene | CLEO+ | 0 | Returns true if a cutscene is active (02E7) |
| `0E26` | IS_WEAPON_FIRE_TYPE | Weapon | CLEO+ | 2 | Checks if the weapon has the specified fire type |
| `0E27` | GET_ANGLE_FROM_TWO_COORDS | Math | CLEO+ | 5 |  |
| `0E28` | WRITE_STRUCT_OFFSET | Memory | CLEO+ | 4 | Writes the value at the given offset from the memory address (see: 0D37) |
| `0E29` | PERLIN_NOISE_FRACTAL | Math | CLEO+ | 7 | Calculates the Fractal Brownian Motion (fBm) summation of 1D Perlin Simplex noise |
| `0E2A` | ADD_CLEO_BLIP | CleoBlip | CLEO+ | 9 | Creates a blip that don't saves, supports any texture, alpha and don't hits the blip limit |
| `0E2B` | REMOVE_CLEO_BLIP | CleoBlip | CLEO+ | 1 | Removes a cleo blip |
| `0E2C` | GET_CURRENT_SAVE_SLOT | Game | CLEO+ | 1 | Gets loaded save slot number. 0 if new game |
| `0E2D` | IS_GAME_FIRST_START | Game | CLEO+ | 0 | Is first gameplay start (game was not reloaded) |
| `0E2E` | CREATE_RENDER_OBJECT_TO_CHAR_BONE | RenderObject | CLEO+ | 10 | Creates renderObject to character bone |
| `0E2F` | DELETE_RENDER_OBJECT | RenderObject | CLEO+ | 1 | Deletes the renderObject |
| `0E30` | SET_RENDER_OBJECT_AUTO_HIDE | Char | CLEO+ | 4 | Sets the renderObject to AutoHide if the character is dead, is using a weapon, or enters a car |
| `0E31` | SET_RENDER_OBJECT_VISIBLE | RenderObject | CLEO+ | 2 | Sets the visible status of the renderObject |
| `0E32` | SET_CHAR_COORDINATES_SIMPLE | Char | CLEO+ | 4 | Sets the character's coordinates without exception protocols |
| `0E33` | GET_PICKUP_THIS_COORD | World | CLEO+ | 5 | Returns the handle of a pickup at the specified coordinates |
| `0E34` | GET_PICKUP_MODEL | Pickup | CLEO+ | 2 | Returns the model of a specified pickup |
| `0E35` | SET_RENDER_OBJECT_POSITION | RenderObject | CLEO+ | 4 | Sets the position of a renderObject |
| `0E36` | SET_RENDER_OBJECT_ROTATION | RenderObject | CLEO+ | 4 | Sets the rotation of the renderObject |
| `0E37` | SET_RENDER_OBJECT_SCALE | RenderObject | CLEO+ | 4 | Sets the scale of the renderObject |
| `0E38` | GET_PICKUP_POINTER | Pickup | CLEO+ | 2 | Returns a pointer to the struct of a specified pickup |
| `0E39` | GET_PICKUP_TYPE | Pickup | CLEO+ | 2 | Returns the type of a specified pickup |
| `0E3A` | SET_RENDER_OBJECT_DISTORTION | RenderObject | CLEO+ | 5 | Sets the renderObject's distortion |
| `0E3B` | GET_AUDIOSTREAM_INTERNAL | AudioStream | CLEO+ | 2 | Returns the internal reference of a given AUDIOSTREAM to be used in bass.dll functions |
| `0E3C` | GET_TEXTURE_FROM_SPRITE | Txd | CLEO+ | 2 | Returns the rwTexture pointer from sprite index |
| `0E3D` | IS_KEY_JUST_PRESSED | Pad | CLEO+ | 1 | Returns true if the player has just started to press a specified key this frame |
| `0E3E` | IS_BUTTON_JUST_PRESSED | Pad | CLEO+ | 2 | Returns true if the pad's button has just started to be pressed this frame |
| `0E3F` | CONVERT_3D_TO_SCREEN_2D | World | CLEO+ | 9 | Returns 2D screen position and distance related text size for world coordinates between nearClip and farClip |
| `0E40` | GET_CURRENT_HOUR | Clock | CLEO+ | 1 | Returns the clock's current hour |
| `0E41` | GET_CURRENT_MINUTE | Clock | CLEO+ | 1 | Returns the clock's current minute |
| `0E42` | IS_CHAR_DOING_TASK_ID | Char | CLEO+ | 2 | Returns true if the character is performing the specified task |
| `0E43` | GET_CHAR_TASK_POINTER_BY_ID | Char | CLEO+ | 3 | Returns the address of the character's task by taskId |
| `0E44` | GET_CHAR_KILL_TARGET_CHAR | Char | CLEO+ | 2 | Returns the handle of the killTarget of the specified character |
| `0E45` | FRAME_MOD | Game | CLEO+ | 1 | Returns True every mod number of frames |
| `0E46` | IS_CHAR_USING_GUN | Char | CLEO+ | 1 | Returns true if the specified character is using a gun |
| `0E47` | IS_CHAR_FIGHTING | Char | CLEO+ | 1 | Returns true if the specified character is fighting |
| `0E48` | IS_CHAR_FALLEN_ON_GROUND | Char | CLEO+ | 1 | Returns true if the specified character has fallen on the ground |
| `0E49` | IS_CHAR_ENTERING_ANY_CAR | Char | CLEO+ | 1 | Returns true if the specified character is entering any car |
| `0E4A` | IS_CHAR_EXITING_ANY_CAR | Char | CLEO+ | 1 | Returns true if the specified character is exiting any car |
| `0E4B` | IS_CHAR_PLAYING_ANY_SCRIPT_ANIMATION | Char | CLEO+ | 2 | Returns true if the specified character is playing any script animation |
| `0E4C` | IS_CHAR_DOING_ANY_IMPORTANT_TASK | Char | CLEO+ | 2 | Returns true if the specified character is doing any important task |
| `0E4D` | RANDOM_PERCENT | Math | CLEO+ | 1 | Returns randomly True the specified percent of the time |
| `0E4E` | DISPLAY_ONSCREEN_TIMER_LOCAL | Hud | CLEO+ | 2 | Creates a countdown or countup onscreen timer |
| `0E4F` | DISPLAY_ONSCREEN_TIMER_WITH_STRING_LOCAL | Hud | CLEO+ | 3 | Creates a countdown or countup onscreen timer with the text |
| `0E50` | DISPLAY_ONSCREEN_COUNTER_LOCAL | Hud | CLEO+ | 2 | Displays an onscreen counter, either shown in numbers or as a bar |
| `0E51` | DISPLAY_ONSCREEN_COUNTER_WITH_STRING_LOCAL | Hud | CLEO+ | 3 | Displays an onscreen counter with the text, either shown in numbers or as a bar |
| `0E52` | DISPLAY_TWO_ONSCREEN_COUNTERS_LOCAL | Hud | CLEO+ | 2 | Displays two onscreen counters separated by a slash |
| `0E53` | DISPLAY_TWO_ONSCREEN_COUNTERS_WITH_STRING_LOCAL | Hud | CLEO+ | 3 | Displays two onscreen counters separated by a slash with the text |
| `0E54` | CLEAR_ONSCREEN_TIMER_LOCAL | Hud | CLEO+ | 1 | Removes the local onscreen timer |
| `0E55` | CLEAR_ONSCREEN_COUNTER_LOCAL | Hud | CLEO+ | 1 | Removes the local onscreen counter |
| `0E56` | SET_ONSCREEN_COUNTER_FLASH_WHEN_FIRST_DISPLAYED_LOCAL | Hud | CLEO+ | 2 | Sets the local counter to flash when first displayed |
| `0E57` | SET_TIMER_BEEP_COUNTDOWN_TIME_LOCAL | Hud | CLEO+ | 2 | Starts a sound when the countdown timer reaches the specified number of seconds |
| `0E58` | SET_ONSCREEN_COUNTER_COLOUR_LOCAL | Hud | CLEO+ | 2 | Sets the color of the specified local counter |
| `0E59` | GET_TRAILER_FROM_CAR | Car | CLEO+ | 2 | Returns the handle of a trailer towed by this car |
| `0E5A` | GET_CAR_FROM_TRAILER | Car | CLEO+ | 2 | Returns the handle of a tractor towing this car |
| `0E5B` | GET_CAR_DUMMY_COORD | Car | CLEO+ | 7 | Returns the coordinates of the specified car's vehicleDummy |
| `0E5C` | GET_CHAR_HEALTH_PERCENT | Char | CLEO+ | 2 | Returns the character's health as a floating-point percentage |
| `0E5D` | IS_CHEAT_ACTIVE | Game | CLEO+ | 1 | Returns True if the specified cheat is togglable and active |
| `0E5E` | CHANGE_PLAYER_MONEY | Player | CLEO+ | 3 | Changes player money by set, add or remove |
| `0E5F` | CAR_HORN | Car | CLEO+ | 1 | Plays the car's horn (if the player is driving the car) |
| `0E60` | SET_CAMERA_CONTROL | Camera | CLEO+ | 1 | Enables rotational control of the camera |
| `0E61` | SET_CAR_ALARM | Car | CLEO+ | 2 | Sets the status of the car's alarm |
| `0E62` | DRAW_STRING | Text | CLEO+ | 8 | Draws string once on specific drawing event |
| `0E63` | DRAW_STRING_EXT | Text | CLEO+ | 27 | Draws string once on specific drawing event with extended text styling |
| `0E64` | GET_CURRENT_CAMERA_MODE | Camera | CLEO+ | 1 | Returns the current camera mode |
| `0E65` | GET_CAR_COLLISION_INTENSITY | Car | CLEO+ | 2 | Returns the intensity of the last collision of the specified car |
| `0E66` | GET_CAR_COLLISION_COORDINATES | Car | CLEO+ | 4 | Returns the coordinates of the last collision of the specified car |
| `0E67` | IS_AIM_BUTTON_PRESSED | Pad | CLEO+ | 1 | Returns True if the pad's aim button is pressed |
| `0E68` | SET_PLAYER_CONTROL_PAD | Pad | CLEO+ | 2 | Enables the specified control pad |
| `0E69` | SET_PLAYER_CONTROL_PAD_MOVEMENT | Pad | CLEO+ | 2 | Enables the specified control pad's movement |
| `0E6A` | MAKE_NOP | Memory | CLEO+ | 2 | Fills memory address with 0x90 with given size |
| `0E6B` | GET_COLPOINT_LIGHTING | ColPoint | CLEO+ | 3 | Returns the lighting of the specified ColPoint |
| `0E6C` | GET_DAY_NIGHT_BALANCE | Weather | CLEO+ | 1 | Returns the intensity of the night filter |
| `0E6D` | GET_UNDERWATERNESS | Weather | CLEO+ | 1 | Returns the intensity of the underwater filter |
| `0E6E` | IS_SELECT_MENU_JUST_PRESSED | Game | CLEO+ | 0 | Returns True if menu Select was just pressed |
| `0E6F` | STREAM_CUSTOM_SCRIPT_FROM_LABEL |  | CLEO+ | 2 | Loads a custom script at the specified label |
| `0E70` | GET_LAST_CREATED_CUSTOM_SCRIPT | Memory | CLEO+ | 1 | Gets the address of the last created custom script |
| `0E71` | GET_OBJECT_CENTRE_OF_MASS_TO_BASE_OF_MODEL | Object | CLEO+ | 2 | Gets the distance between the object model's center of mass to its base |
| `0E72` | CREATE_LIST | List | CLEO+ | 2 | Creates a list of the specified type |
| `0E73` | DELETE_LIST | List | CLEO+ | 1 | Deletes the specified list |
| `0E74` | LIST_ADD | List | CLEO+ | 2 | Adds a numerical value to the specified list |
| `0E75` | LIST_REMOVE_VALUE | List | CLEO+ | 2 | Removes a numerical value from the specified list |
| `0E76` | LIST_REMOVE_INDEX | List | CLEO+ | 2 | Removes an entry from the specified list by index |
| `0E77` | GET_LIST_SIZE | List | CLEO+ | 2 | Returns the number of entries in the specified list |
| `0E78` | GET_LIST_VALUE_BY_INDEX | List | CLEO+ | 3 | Returns a numerical value from the specified list by index |
| `0E79` | RESET_LIST | List | CLEO+ | 1 | Resets all entries within the specified list |
| `0E7A` | GET_LIST_STRING_VALUE_BY_INDEX | List | CLEO+ | 3 | Returns a string value from the specified list by index |
| `0E7B` | LIST_ADD_STRING | List | CLEO+ | 2 | Adds a string value to the specified list |
| `0E7C` | LIST_REMOVE_STRING_VALUE | List | CLEO+ | 2 | Removes a string value from the specified list |
| `0E7D` | LIST_REMOVE_INDEX_RANGE | List | CLEO+ | 3 | Removes entries from the specified list by index range |
| `0E7E` | REVERSE_LIST | List | CLEO+ | 1 | Reverses the order of entries within the specified list |
| `0E7F` | GET_MODEL_TYPE | Streaming | CLEO+ | 2 | Returns the type of the specified model |
| `0E80` | IS_STRING_EQUAL | Text | CLEO+ | 5 | Returns True if string1 and string2 match |
| `0E81` | IS_STRING_COMMENT | Text | CLEO+ | 1 | Returns True if the string starts with a hash (#), semicolon (;) or double slash (//) |
| `0E82` | DOES_CAR_HAVE_PART_NODE | Car | CLEO+ | 2 | Returns True if the car has the specified carNode part |
| `0E83` | GET_CURRENT_CHAR_WEAPONINFO | Char | CLEO+ | 2 | Returns a pointer to the character's current weaponInfo struct |
| `0E84` | GET_WEAPONINFO | Weapon | CLEO+ | 3 | Returns a pointer to the CWeaponInfo struct of the the specified weaponType and weaponSkill |
| `0E85` | GET_WEAPONINFO_MODELS | WeaponInfo | CLEO+ | 3 | Returns the model1 and model2 of the current weaponInfo struct |
| `0E86` | GET_WEAPONINFO_FLAGS | WeaponInfo | CLEO+ | 2 | Returns the flags of the specified WeaponInfo struct |
| `0E87` | GET_WEAPONINFO_ANIMGROUP | WeaponInfo | CLEO+ | 2 | Returns the FireType of the current weaponInfo struct |
| `0E88` | GET_WEAPONINFO_TOTAL_CLIP | WeaponInfo | CLEO+ | 2 | Returns the totalClip size for the current weaponInfo struct |
| `0E89` | GET_WEAPONINFO_FIRE_TYPE | WeaponInfo | CLEO+ | 2 | Returns the FireType of the current weaponInfo struct |
| `0E8A` | GET_WEAPONINFO_SLOT | WeaponInfo | CLEO+ | 2 | Returns the weaponSlot of the current weaponInfo struct |
| `0E8B` | GET_CHAR_WEAPON_STATE | Char | CLEO+ | 2 | Returns the character's current weaponState |
| `0E8C` | GET_CHAR_WEAPON_CLIP | Char | CLEO+ | 2 | Returns the character's current WeaponClip |
| `0E8D` | IS_ANY_FIRE_BUTTON_PRESSED | Pad | CLEO+ | 1 | Returns True if the pad's primary or secondary fire button is pressed |
| `0E8E` | GET_CHAR_COLLISION_SURFACE | Char | CLEO+ | 2 | Returns the specified character's collision surfaceType |
| `0E8F` | GET_CHAR_COLLISION_LIGHTING | Char | CLEO+ | 2 | Returns the specified character's collision lighting |
| `0E90` | GET_CAR_COLLISION_SURFACE | Car | CLEO+ | 2 | Returns the specified car's collision surfaceType |
| `0E91` | GET_CAR_COLLISION_LIGHTING | Car | CLEO+ | 2 | Returns the specified car's collision lighting |
| `0E92` | IS_CHAR_REALLY_IN_AIR | Char | CLEO+ | 1 | Returns True when the character is really in air, including while using a parachute or jetpack |
| `0E93` | IS_CAR_REALLY_IN_AIR | Car | CLEO+ | 1 | Returns True if the specified car is really in the air, and False for boats floating on water |
| `0E94` | IS_OBJECT_REALLY_IN_AIR | Object | CLEO+ | 1 | Returns True if the specified object is not on a solid surface and not submerged |
| `0E95` | SIMULATE_OBJECT_DAMAGE | Object | CLEO+ | 3 | Simulates the specified damage amount and weaponType on the object |
| `0E96` | CLEAR_CHAR_PRIMARY_TASKS | Char | CLEO+ | 1 | Clears the specified character's primary tasks |
| `0E97` | CLEAR_CHAR_SECONDARY_TASKS | Char | CLEO+ | 1 | Clears the character's secondary tasks |
| `0E98` | REQUEST_PRIORITY_MODEL | Streaming | CLEO+ | 1 | Requests a priority modelID to be loaded |
| `0E99` | LOAD_ALL_PRIORITY_MODELS_NOW | Streaming | CLEO+ | 0 | This is a duplicate of LOAD_ALL_MODELS_NOW |
| `0E9A` | LOAD_SPECIAL_CHARACTER_FOR_ID | Streaming | CLEO+ | 2 |  |
| `0E9B` | UNLOAD_SPECIAL_CHARACTER_FROM_ID | Streaming | CLEO+ | 1 |  |
| `0E9C` | GET_MODEL_BY_NAME | Streaming | CLEO+ | 2 | Returns the modelID by name |
| `0E9D` | IS_MODEL_AVAILABLE_BY_NAME | Streaming | CLEO+ | 1 | Returns true if the specified model name is available as a valid special character |
| `0E9E` | GET_MODEL_DOESNT_EXIST_IN_RANGE |  | CLEO+ | 3 |  |
| `0E9F` | REMOVE_ALL_UNUSED_MODELS | Streaming | CLEO+ | 0 |  |
| `0EA0` | SET_CHAR_SECOND_PLAYER | Char | CLEO+ | 3 | Sets this char as controlled by player two |
| `0EA1` | DISABLE_SECOND_PLAYER | Game | CLEO+ | 1 |  |
| `0EA2` | FIX_TWO_PLAYERS_SEPARATED_CARS | Game | CLEO+ | 0 | Enables fixes for making two players use separated cars |
| `0EA3` | REMOVE_MODEL_IF_UNUSED | Streaming | CLEO+ | 1 | Removes the specified ModelID from memory if unused |
| `0EA4` | IS_CHAR_ON_FIRE | Char | CLEO+ | 1 | Returns True if the character is on fire |
| `0EA5` | GET_CLOSEST_COP_NEAR_CHAR | Char | CLEO+ | 7 | Returns the handle of the closestCop to the specified character |
| `0EA6` | GET_CLOSEST_COP_NEAR_POS | World | CLEO+ | 8 | Returns the closestCop to the specified coordinates |
| `0EA7` | GET_ANY_CHAR_NO_SAVE_RECURSIVE | World | CLEO+ | 3 | Returns the handle of anyChar in the pool, starting at the previously returned progress index |
| `0EA8` | GET_ANY_CAR_NO_SAVE_RECURSIVE | World | CLEO+ | 3 | Returns the handle of anyCar in the pool, starting at the previously returned progress index |
| `0EA9` | GET_ANY_OBJECT_NO_SAVE_RECURSIVE | World | CLEO+ | 3 | Returns the handle of anyObject in the pool, starting at the previously returned progress index |
| `0EAA` | SET_CHAR_ARRESTED | Char | CLEO+ | 1 | Sets the specified character's pedState to Arrested |
| `0EAB` | GET_CHAR_PEDSTATE | Char | CLEO+ | 2 | Returns the specified character's pedState |
| `0EAC` | GET_CHAR_PROOFS | Char | CLEO+ | 6 | Returns the specified character's damage proofs |
| `0EAD` | GET_CAR_PROOFS | Car | CLEO+ | 6 | Returns the specified car's damage proofs |
| `0EAE` | GET_OBJECT_PROOFS | Object | CLEO+ | 6 | Returns the specified object's damage proofs |
| `0EAF` | IS_CHAR_WEAPON_VISIBLE_SET | Char | CLEO+ | 1 | Returns true if the specified character has weapon visible set |
| `0EB0` | GET_FORCED_WEATHER | Weather | CLEO+ | 1 | Returns the forced weather type |
| `0EB1` | GET_CHAR_STAT_ID | Char | CLEO+ | 2 | Returns the specified character's pedStat ID (data\pedstats.dat) |
| `0EB2` | GET_OFFSET_FROM_CAMERA_IN_WORLD_COORDS | Camera | CLEO+ | 6 | Returns world coordinates for the offset from the camera |
| `0EB3` | CONVERT_DIRECTION_TO_QUAT |  | CLEO+ | 4 |  |
| `0EB4` | SET_CAR_COORDINATES_SIMPLE | Car | CLEO+ | 4 | Sets the specified car's coordinates without exception protocols |
| `0EB5` | GET_CHAR_DAMAGE_LAST_FRAME | Char | CLEO+ | 5 | Returns the character's damaging entity and weaponType, bodyPart damaged, and intensity of damage last frame |
| `0EB6` | GET_CAR_WEAPON_DAMAGE_LAST_FRAME | Car | CLEO+ | 4 | Gets car damage by weapon last frame. Char can be invalid, and returns false if no damage last frame |
| `0EB7` | IS_ON_SCRIPTED_CUTSCENE | Mission | CLEO+ | 0 | Checks if is playing scripted mission cutscene, that is, original widescreen borders are toggled on |
| `0EB8` | IS_RADAR_VISIBLE | Hud | CLEO+ | 0 |  |
| `0EB9` | IS_HUD_VISIBLE | Hud | CLEO+ | 0 |  |
| `0EBA` | GET_MODEL_PED_TYPE_AND_STAT |  | CLEO+ | 3 | Returns the pedType and pedStat ID for the specified modelID |
| `0EBB` | PASS_TIME | Clock | CLEO+ | 1 | Simulates the passage of time on the clock, calendar and environment |
| `0EBC` | GENERATE_RANDOM_INT_IN_RANGE_WITH_SEED | Math | CLEO+ | 4 | Generates a randomInteger from min to < max with seed |
| `0EBD` | GENERATE_RANDOM_FLOAT_IN_RANGE_WITH_SEED | Math | CLEO+ | 4 | Generates a randomFloat from min to < max with seed |
| `0EBE` | LOCATE_CAMERA_DISTANCE_TO_COORDINATES | Camera | CLEO+ | 4 | Returns True if the camera is located within the specified radius of the coordinates |
| `0EBF` | GET_FX_SYSTEM_POINTER | Fx | CLEO+ | 2 | Returns the address of the specified FX system associated with the given particle, or 0 if handle is invalid |
| `0EC0` | ADD_FX_SYSTEM_PARTICLE | Fx | CLEO+ | 14 | Adds an FX system particle |
| `0EC1` | IS_FX_SYSTEM_AVAILABLE_WITH_NAME | Fx | CLEO+ | 1 | Returns True if an FX system with the specified name is available |
| `0EC2` | SET_STRING_UPPER | Text | CLEO+ | 1 | Sets the string at the specified address to all upper case |
| `0EC3` | SET_STRING_LOWER | Text | CLEO+ | 1 | Sets the string at the specified address to all lower case |
| `0EC4` | STRING_FIND | Text | CLEO+ | 4 | Returns the character index where strFind is found within stringOrigin |
| `0EC5` | CUT_STRING_AT | Text | CLEO+ | 2 | Cuts stringAddress at the specified character index |
| `0EC6` | IS_STRING_CHARACTER_AT | Text | CLEO+ | 3 | Returns True if the specified characters are found at the index of the string |
| `0EC7` | GET_FADE_ALPHA | Camera | CLEO+ | 1 | Returns the current alpha of the fade being performed ( < 255.0 max ) |
| `0EC8` | GET_CHAR_RANDOM_SEED | Char | CLEO+ | 2 | Returns the randomSeed of the specified character |
| `0EC9` | GET_CAR_RANDOM_SEED | Car | CLEO+ | 2 | Returns the randomSeed of the specified car |
| `0ECA` | GET_OBJECT_RANDOM_SEED | Object | CLEO+ | 2 | Returns the randomSeed of the specified object |
| `0ECB` | GET_CHAR_MOVE_STATE | Char | CLEO+ | 2 |  |
| `0ECC` | DONT_DELETE_CHAR_UNTIL_TIME | Char | CLEO+ | 2 | Prevents the deletion of the specified character until MsFromNow |
| `0ECD` | DONT_DELETE_CAR_UNTIL_TIME | Car | CLEO+ | 2 | Prevents the deletion of the specified car until MsFromNow |
| `0ECE` | GET_TIME_CHAR_IS_DEAD | Char | CLEO+ | 2 | Returns the TimeIsDead in milliseconds since the specified character is dead |
| `0ECF` | GET_TIME_CAR_IS_DEAD | Car | CLEO+ | 2 | Returns the TimeIsDead in milliseconds since the specified car is dead |
| `0ED0` | RETURN_SCRIPT_EVENT |  | CLEO+ | 0 | Returns from script event |
| `0ED1` | SET_SCRIPT_EVENT_SAVE_CONFIRMATION |  | CLEO+ | 3 | Toggles script event during save, just before the game is saved |
| `0ED2` | SET_SCRIPT_EVENT_CHAR_DELETE |  | CLEO+ | 3 | Toggles script event just after varChar is deleted |
| `0ED3` | SET_SCRIPT_EVENT_CHAR_CREATE |  | CLEO+ | 3 | Toggles script event just after varChar is created |
| `0ED4` | SET_SCRIPT_EVENT_CAR_DELETE |  | CLEO+ | 3 | Toggles script event just before some car is being deleted |
| `0ED5` | SET_SCRIPT_EVENT_CAR_CREATE |  | CLEO+ | 3 | Toggles script event just after some car is created |
| `0ED6` | SET_SCRIPT_EVENT_OBJECT_DELETE |  | CLEO+ | 3 | Toggles script event just before some object is being deleted |
| `0ED7` | SET_SCRIPT_EVENT_OBJECT_CREATE |  | CLEO+ | 3 | Toggles script event just after some object is created |
| `0ED8` | SET_SCRIPT_EVENT_ON_MENU |  | CLEO+ | 3 | Toggles script event to run during pause menu, or when just paused the game |
| `0ED9` | SET_CHAR_IGNORE_DAMAGE_ANIMS | Char | CLEO+ | 2 |  |
| `0EDA` | SET_SCRIPT_EVENT_CHAR_PROCESS |  | CLEO+ | 3 | Toggles script event to run on each char once per frame |
| `0EDB` | SET_SCRIPT_EVENT_CAR_PROCESS |  | CLEO+ | 3 | Toggles script event to run on each car once per frame |
| `0EDC` | SET_SCRIPT_EVENT_OBJECT_PROCESS |  | CLEO+ | 3 | Toggles script event to run on each object once per frame. May be slow |
| `0EDD` | SET_SCRIPT_EVENT_BUILDING_PROCESS |  | CLEO+ | 3 | Toggles script event to run on each building (CBuilding/Entity) once per frame. CAUTION! Very slow |
| `0EDE` | SET_SCRIPT_EVENT_CHAR_DAMAGE |  | CLEO+ | 3 | Toggles script event when some char receives any damage. Use 0EB5 to get damage data |
| `0EDF` | SET_SCRIPT_EVENT_CAR_WEAPON_DAMAGE |  | CLEO+ | 3 | Toggles script event to run when some car is damaged by weapon. Use 0EB6 to get damage data |
| `0EE0` | SET_SCRIPT_EVENT_BULLET_IMPACT |  | CLEO+ | 6 | Toggles script event to run when bullet impact. Char and entity can be invalid |
| `0EE1` | GET_COLPOINT_COORDINATES | ColPoint | CLEO+ | 4 | Returns the coordinates of the specified ColPoint |
| `0EE2` | READ_STRUCT_OFFSET_MULTI | Memory | CLEO+ | 5 | Reads a value from the given offset from the memory address multiple times as array/vector |
| `0EE3` | WRITE_STRUCT_OFFSET_MULTI | Memory | CLEO+ | 5 | Writes the value at the given offset from the memory address multiple times as array/vector |
| `0EE4` | LOCATE_CHAR_DISTANCE_TO_CHAR | Char | CLEO+ | 3 | Returns True if the character(self) is within the radius of the specified character |
| `0EE5` | LOCATE_CHAR_DISTANCE_TO_CAR | Char | CLEO+ | 3 | Returns True if the character is within the radius of the specified car |
| `0EE6` | LOCATE_CHAR_DISTANCE_TO_OBJECT | Char | CLEO+ | 3 | Returns True if the character is within the radius of the specified object |
| `0EE7` | LOCATE_CAR_DISTANCE_TO_OBJECT | Car | CLEO+ | 3 | Returns True if the car is within the radius of the specified object |
| `0EE8` | LOCATE_CAR_DISTANCE_TO_CAR | Car | CLEO+ | 3 | Returns True if the car(self) is within the radius of the specified car |
| `0EE9` | LOCATE_OBJECT_DISTANCE_TO_OBJECT | Object | CLEO+ | 3 | Returns True if the object(self) is within the radius of the specified object |
| `0EEA` | LOCATE_CHAR_DISTANCE_TO_COORDINATES | Char | CLEO+ | 5 | Returns True if the character is within the radius of the specified coordinates |
| `0EEB` | LOCATE_CAR_DISTANCE_TO_COORDINATES | Car | CLEO+ | 5 | Returns True if the car is within the radius of the specified coordinates |
| `0EEC` | LOCATE_OBJECT_DISTANCE_TO_COORDINATES | Object | CLEO+ | 5 | Returns True if the object is within the radius of the specified coordinates |
| `0EED` | LOCATE_ENTITY_DISTANCE_TO_ENTITY | Entity | CLEO+ | 3 | Returns True if entityB is within the radius of entityA |
| `0EEE` | GET_ENTITY_COORDINATES | Entity | CLEO+ | 4 | Returns the coordinates of the entity at the specified address |
| `0EEF` | GET_ENTITY_HEADING | Entity | CLEO+ | 2 | Returns the heading of the entity at the specified address |
| `0EF0` | GET_COORD_FROM_ANGLED_DISTANCE | World | CLEO+ | 6 | Returns 2D coordinates for a location relative to x and y at the specified angle and distance |
| `0EF1` | PERLIN_NOISE_FRACTAL_2D | Math | CLEO+ | 8 | Calculates the Fractal Brownian Motion (fBm) summation of 2D Perlin Simplex noise |
| `0EF2` | PERLIN_NOISE_FRACTAL_3D | Math | CLEO+ | 9 | Calculates the Fractal Brownian Motion (fBm) summation of 3D Perlin Simplex noise |
| `0EF3` | LERP |  | CLEO+ | 4 |  |
| `0EF4` | CLAMP_FLOAT | Math | CLEO+ | 4 | Returns the clamped value of the specified float between the min and max values |
| `0EF5` | IS_CAR_OWNED_BY_PLAYER | Car | CLEO+ | 1 | Returns True if the specified car is owned by the player |
| `0EF6` | SET_CAR_OWNED_BY_PLAYER | Car | CLEO+ | 2 | Sets the specified car as OwnedByPlayer |
| `0EF7` | CLAMP_INT | Math | CLEO+ | 4 | Returns the clamped value of the specified integer between the min and max values |
| `0EF8` | GET_MODEL_INFO | Streaming | CLEO+ | 2 | Returns the address of the modelInfo of the specified modelId |
| `0EF9` | GET_CAR_ANIMGROUP | Car | CLEO+ | 2 | Returns the carAnimGroup of the specified car |
| `0EFA` | GET_CHAR_FEAR | Char | CLEO+ | 2 | Returns the specified character's fear level (see pedstats.dat) |
| `0EFB` | IS_CAR_CONVERTIBLE | Car | CLEO+ | 1 | Returns True if the specified car is a convertible |
| `0EFC` | GET_CAR_VALUE | Car | CLEO+ | 2 | Returns the monetary value of the car |
| `0EFD` | GET_CAR_PEDALS | Car | CLEO+ | 3 | Returns the value of the car's gas and brake pedals |
| `0EFE` | GET_LOADED_LIBRARY | DynamicLibrary | CLEO+ | 2 | Returns the address of a loaded dynamic-link library (DLL) |
| `0EFF` | GET_CHAR_SIMPLEST_ACTIVE_TASK | Char | CLEO+ | 3 | Returns the character's simplest active taskId and the address of the task |
| `0F00` | LOAD_SPECIAL_MODEL | Streaming | CLEO+ | 3 |  |
| `0F01` | REMOVE_SPECIAL_MODEL | Streaming | CLEO+ | 1 |  |
| `0F02` | CREATE_RENDER_OBJECT_TO_CHAR_BONE_FROM_SPECIAL | Char | CLEO+ | 10 |  |
| `0F03` | CREATE_RENDER_OBJECT_TO_OBJECT | Object | CLEO+ | 9 |  |
| `0F04` | CREATE_RENDER_OBJECT_TO_OBJECT_FROM_SPECIAL | Object | CLEO+ | 9 |  |
| `0F05` | GET_SPECIAL_MODEL_DATA | Streaming | CLEO+ | 4 |  |
| `0F06` | REPLACE_LIST_VALUE_BY_INDEX | List | CLEO+ | 3 | Replaces a value on a list by index |
| `0F07` | REPLACE_LIST_STRING_VALUE_BY_INDEX | List | CLEO+ | 3 | Replaces a string value on a list by index |
| `0F08` | INSERT_LIST_VALUE_BY_INDEX | List | CLEO+ | 3 | Inserts a value into a list by index |
| `0F09` | INSERT_LIST_STRING_VALUE_BY_INDEX | List | CLEO+ | 3 | Inserts a string value into a list by index |
| `0F0A` | RETURN_TIMES |  | CLEO+ | 1 | Returns runReturns number of gosub levels |
| `0F0B` | SET_SCRIPT_EVENT_BEFORE_GAME_PROCESS |  | CLEO+ | 2 |  |
| `0F0C` | SET_SCRIPT_EVENT_AFTER_GAME_PROCESS |  | CLEO+ | 2 |  |
| `0F0D` | SET_MATRIX_LOOK_DIRECTION |  | CLEO+ | 7 | Sets the matrix look direction |
| `0F0E` | GET_THIRD_PERSON_CAMERA_TARGET | Camera | CLEO+ | 10 | Returns the third person camera target |
| `0F0F` | GET_DISTANCE_MULTIPLIER |  | CLEO+ | 2 | Returns the games drawing and generating distance multipliers |
| `0F10` | GET_ACTIVE_CAMERA_ROTATION | Camera | CLEO+ | 3 | Returns the active camera rotation |
| `0F11` | GET_CLOSEST_WATER_DISTANCE |  | CLEO+ | 2 | Returns the closest water distance and z level |
| `0F12` | GET_CAMERA_STRUCT | Camera | CLEO+ | 2 | Returns the address of TheCamera (CCamera) and ActiveCam (CCam) |
| `0F13` | GET_TIME_NOT_TOUCHING_PAD | Pad | CLEO+ | 2 | Returns the time in milliseconds since the pad has been touched |
| `0F14` | GET_CAMERA_ROTATION_INPUT_VALUES | Camera | CLEO+ | 2 | Returns the camera's rotation input values |
| `0F15` | SET_CAMERA_ROTATION_INPUT_VALUES | Camera | CLEO+ | 2 | Sets the camera's rotation Input values |
| `0F16` | SET_ON_MISSION | Game | CLEO+ | 1 | Sets the game's On Mission status without referencing a global variable |
| `0F17` | GET_MODEL_NAME_POINTER |  | CLEO+ | 2 | Returns the address of the name of any modelId |
| `1337` | SF_MAKE_SCRIPT_PRIVATE | Sf | SAMPFUNCS | 1 | Makes the script where this command is executed invisible across other scripts |
| `2000` | GET_CLEO_ARG_COUNT |  | CLEO | 1 | Gets argument count used to call current cleo function (0AB1) |
| `2002` | CLEO_RETURN_WITH |  | CLEO | 2 | Returns from the current SCM function (0AB1) and sets the condition result to specified value |
| `2003` | CLEO_RETURN_FAIL |  | CLEO | 1 | Returns from the current SCM function (0AB1) and sets the condition result to false, skipping variables in 0AB1 |
| `2080` | IS_KEY_JUST_PRESSED | Pad | input | 1 | Returns true if the player has just started to press a specified key this frame |
| `2081` | GET_KEY_PRESSED_IN_RANGE | Pad | input | 3 | Gets code of first currently hold down key in range between minKeyCode and maxKeyCode. If no key is pressed return value is unmodified and logical result is set to false |
| `2082` | GET_KEY_JUST_PRESSED_IN_RANGE | Pad | input | 3 | Gets code of first just pressed key in range between minKeyCode and maxKeyCode. If no key was pressed return value is unmodified and logical result is set to false |
| `2083` | EMULATE_KEY_PRESS | Pad | input | 1 | Simulates key press event |
| `2084` | EMULATE_KEY_RELEASE | Pad | input | 1 | Simulates key release event |
| `2085` | GET_CONTROLLER_KEY | Pad | input | 3 | Returns n-th alternate key assigned to pad's action. If no key is bound then return value is unchanged and logical result is false |
| `2086` | GET_KEY_NAME | Pad | input | 2 | Returns keyboard/mouse key name text of specified keyCode. If key code has no name return value is unchanged and logical result is false |
| `2100` | BREAKPOINT | Debugger | debug | 3 | Creates a debug breakpoint in script |
| `2101` | TRACE | Debugger | debug | 2 | Prints a debug message on screen and adds it to .cleo.log |
| `2102` | LOG_TO_FILE | Debugger | debug | 4 | Appends new line to file. Timestamp parameter decides if datetime prefix in format 'DD/MM/YYYY hh:mm:ss.fraction' will be added. Command is not affected by debug mode status |
| `2200` | IMGUI_BEGIN_FRAME | ImGui | imgui | 1 | Creates a unique frame with its own space in memory. Must be enclosed with IMGUI_END_FRAME |
| `2201` | IMGUI_END_FRAME | ImGui | imgui | 0 | Ends unique ImGui frame created with IMGUI_BEGIN_FRAME |
| `2202` | IMGUI_BEGIN | ImGui | imgui | 7 | Creates the window |
| `2203` | IMGUI_END | ImGui | imgui | 0 | Ends the window |
| `2204` | IMGUI_BEGIN_MAINMENUBAR | ImGui | imgui | 1 | Creates the main menu bar |
| `2205` | IMGUI_END_MAINMENUBAR | ImGui | imgui | 0 | Ends the main menu bar |
| `2206` | IMGUI_BEGIN_CHILD | ImGui | imgui | 1 | Creates a child window widget inside the main window |
| `2207` | IMGUI_END_CHILD | ImGui | imgui | 0 | Ends the child window widget created with 0C25 |
| `2208` | IMGUI_TABS | ImGui | imgui | 3 | Pass tab names separated by comma. Returns the index of the visible tab |
| `2209` | IMGUI_COLLAPSING_HEADER | ImGui | imgui | 1 | Adds the collapsing header |
| `220A` | IMGUI_SET_WINDOW_POS | ImGui | imgui | 3 | Sets the current window position. Must be called inside Begin()...End() |
| `220B` | IMGUI_SET_WINDOW_SIZE | ImGui | imgui | 3 | Sets the current window size. Must be called inside Begin()...End() |
| `220C` | IMGUI_SET_NEXT_WINDOW_POS | ImGui | imgui | 3 | Sets the current window position. Applies to the next window ( aka Begin() ) |
| `220D` | IMGUI_SET_NEXT_WINDOW_SIZE | ImGui | imgui | 3 | Sets the current window size. Applies to the next window ( aka Begin() ) |
| `220E` | IMGUI_TEXT | ImGui | imgui | 1 | Creates the text line |
| `220F` | IMGUI_TEXT_CENTERED | ImGui | imgui | 1 | Displays a center aligned ImGui text widget |
| `2210` | IMGUI_TEXT_DISABLED | ImGui | imgui | 1 | Creates the text line with the disabled color ( Grayish by default ) |
| `2211` | IMGUI_TEXT_WRAPPED | ImGui | imgui | 1 | Creates the text line that wraps to a newline if the text goes beyond the window width |
| `2212` | IMGUI_TEXT_COLORED | ImGui | imgui | 5 | Creates the text line of the given RGBA color (0.0f-1.0f) |
| `2213` | IMGUI_BULLET_TEXT | ImGui | imgui | 1 | Creates the text line with a bullet point |
| `2214` | IMGUI_BULLET | ImGui | imgui | 0 | Creates a bullet point |
| `2215` | IMGUI_CHECKBOX | ImGui | imgui | 3 | Creates the checkbox |
| `2216` | IMGUI_COMBO | ImGui | imgui | 4 | Creates a combo box widget. Pass options separated by commas "item1,item2,item3" |
| `2217` | IMGUI_SET_TOOLTIP | ImGui | imgui | 1 | Creates the popup window with the given text |
| `2218` | IMGUI_BUTTON | ImGui | imgui | 3 | Creates the button |
| `2219` | IMGUI_IMAGE_BUTTON | ImGui | imgui | 4 | Creates a ImGui button with specified image |
| `221A` | IMGUI_INVISIBLE_BUTTON | ImGui | imgui | 3 | Creates the invisible button |
| `221B` | IMGUI_COLOR_BUTTON | ImGui | imgui | 7 | Creates the button with custom colors |
| `221C` | IMGUI_ARROW_BUTTON | ImGui | imgui | 2 | Creates the arrow button in the specified direction |
| `221D` | IMGUI_SLIDER_INT | ImGui | imgui | 5 | Creates the int slider input |
| `221E` | IMGUI_SLIDER_FLOAT | ImGui | imgui | 5 | Creates the float slider input |
| `221F` | IMGUI_INPUT_INT | ImGui | imgui | 5 | Creates the int input |
| `2220` | IMGUI_INPUT_FLOAT | ImGui | imgui | 5 | Creates the float input |
| `2221` | IMGUI_INPUT_TEXT | ImGui | imgui | 2 | Creates the text input |
| `2222` | IMGUI_RADIO_BUTTON | ImGui | imgui | 4 | Creates the radio button |
| `2223` | IMGUI_COLOR_PICKER | ImGui | imgui | 5 | Creates the color picker and sets the default color (0-255) |
| `2224` | IMGUI_MENU_ITEM | ImGui | imgui | 3 | Adds the menu item |
| `2225` | IMGUI_SELECTABLE | ImGui | imgui | 2 | Adds the selectable widget |
| `2226` | IMGUI_DUMMY | ImGui | imgui | 2 | Creates the dummy widget. Used for spacing |
| `2227` | IMGUI_SAMELINE | ImGui | imgui | 0 | Appends the next widget to the same line as the previous widget |
| `2228` | IMGUI_NEWLINE | ImGui | imgui | 0 | Creates a new line for the next widget |
| `2229` | IMGUI_COLUMNS | ImGui | imgui | 1 | Divides the window width into N columns. Close this with Columns(1) |
| `222A` | IMGUI_NEXT_COLUMN | ImGui | imgui | 0 | Puts the next widgets on the next column. Used alongside 0C16 |
| `222B` | IMGUI_SPACING | ImGui | imgui | 0 | Adds some spacing after the previous widget |
| `222C` | IMGUI_SEPARATOR | ImGui | imgui | 0 | Adds a horizontal separator line |
| `222D` | IMGUI_PUSH_ITEM_WIDTH | ImGui | imgui | 1 | Sets the item width for the next widgets |
| `222E` | IMGUI_POP_ITEM_WIDTH | ImGui | imgui | 0 | Removes the pushed item width (0C27) from the stack |
| `222F` | IMGUI_IS_ITEM_ACTIVE | ImGui | imgui | 1 | Returns true if the previous widget is in active state |
| `2230` | IMGUI_IS_ITEM_CLICKED | ImGui | imgui | 1 | Returns true if the previous widget is clicked |
| `2231` | IMGUI_IS_ITEM_FOCUSED | ImGui | imgui | 1 | Returns true if the previous widget is focused |
| `2232` | IMGUI_IS_ITEM_HOVERED | ImGui | imgui | 1 | Returns true if the previous widget is hovered with mouse |
| `2233` | IMGUI_SET_ITEM_INT | ImGui | imgui | 2 | Sets the value of input int & slider int widget |
| `2234` | IMGUI_SET_ITEM_FLOAT | ImGui | imgui | 2 | Sets the value of input float & slider float widget |
| `2235` | IMGUI_SET_ITEM_TEXT | ImGui | imgui | 2 | Sets value of input text widget |
| `2236` | IMGUI_SET_IMAGE_BG_COLOR | ImGui | imgui | 4 | Sets image background color |
| `2237` | IMGUI_SET_IMAGE_TINT_COLOR | ImGui | imgui | 4 | Sets image tint color |
| `2238` | IMGUI_LOAD_IMAGE | ImGui | imgui | 2 | Loads a image file from disk. Relative to CLEO directory |
| `2239` | IMGUI_FREE_IMAGE | ImGui | imgui | 1 | Frees a loaded image data |
| `223A` | IMGUI_PUSH_STYLE_VAR | ImGui | imgui | 2 | Pushes a ImGuiStyleVar value to the stack. Use PopStyleVar to undo the effect |
| `223B` | IMGUI_PUSH_STYLE_VAR2 | ImGui | imgui | 3 | Pushes a ImGuiStyleVar value to the stack. Use PopStyleVar to undo the effect |
| `223C` | IMGUI_PUSH_STYLE_COLOR | ImGui | imgui | 5 | Pushes a ImGuiCol value to the stack. Use PopStyleColor to undo the effect |
| `223D` | IMGUI_POP_STYLE_VAR | ImGui | imgui | 1 | Removes the recent imGuiStyleVar from the stack |
| `223E` | IMGUI_POP_STYLE_COLOR | ImGui | imgui | 1 | Removes the recent ImGuiCol from the stack |
| `223F` | IMGUI_GET_FOREGROUND_DRAWLIST | ImGui | imgui | 1 | Returns pointer to foreground draw list |
| `2240` | IMGUI_GET_BACKGROUND_DRAWLIST | ImGui | imgui | 1 | Returns pointer to ImGui background drawlist |
| `2241` | IMGUI_GET_WINDOW_DRAWLIST | ImGui | imgui | 1 | Returns pointer to ImGui window drawList |
| `2242` | IMGUI_DRAWLIST_ADD_TEXT | ImGui | imgui | 8 | Adds text at specified position |
| `2243` | IMGUI_DRAWLIST_ADD_LINE | ImGui | imgui | 10 | Adds a line form point A to B |
| `2244` | GET_FRAMERATE | Game | imgui | 1 | Returns game FPS |
| `2245` | IMGUI_GET_VERSION | ImGui | imgui | 1 | Returns the ImGui version |
| `2246` | IMGUI_GET_PLUGIN_VERSION | ImGui | imgui | 1 | Returns the ImGuiRedux version |
| `2247` | IMGUI_SET_CURSOR_VISIBLE | ImGui | imgui | 1 | Toggles the cursor |
| `2248` | IMGUI_GET_FRAME_HEIGHT | ImGui | imgui | 1 | Returns the ImGui frame height |
| `2249` | IMGUI_GET_WINDOW_POS | ImGui | imgui | 3 | Returns the x,y coordinates of the window on the screen |
| `224A` | IMGUI_GET_WINDOW_SIZE | ImGui | imgui | 3 | Returns the width and height of the window |
| `224B` | IMGUI_CALC_TEXT_SIZE | ImGui | imgui | 3 | Returns the width and height of the given text |
| `224C` | IMGUI_GET_WINDOW_CONTENT_REGION_WIDTH | ImGui | imgui | 2 | Returns the content region width of the window |
| `224D` | IMGUI_GET_SCALING_SIZE | ImGui | imgui | 5 | Returns the width and height scaling factor based on the window size |
| `224E` | IMGUI_GET_DISPLAY_SIZE | ImGui | imgui | 2 | Returns the width & height of the display |
| `224F` | IMGUI_SET_NEXT_WINDOW_TRANSPARENCY | ImGui | imgui | 1 | Sets the background transparency of next window (0.0f-1.0f) |
| `2250` | IMGUI_SET_MESSAGE | ImGui | imgui | 1 | Displays a text message on top left corner of the screen. Useful for games without `showTextBox(...)` support |
| `2251` | IMGUI_SET_COLUMN_WIDTH | ImGui | imgui | 2 | Sets the width of the column |
| `2252` | IMGUI_BEGIN_CHILDEX | ImGui | imgui | 5 | Creates a child window widget inside the main window |
| `2253` | IMGUI_BEGIN_DISABLED | ImGui | imgui | 1 | Disables ImGui widgets inside this block |
| `2254` | IMGUI_END_DISABLED | ImGui | imgui | 0 | Closes the ImGui disable block |
| `2255` | IMGUI_BEGIN_MENU | ImGui | imgui | 2 | Begins a ImGui menu block |
| `2256` | IMGUI_END_MENU | ImGui | imgui | 0 | Ends a ImGui menu block |
| `2300` | GET_FILE_POSITION | File | file | 2 | Gets current offset of read-write carret within the file stream |
| `2301` | READ_BLOCK_FROM_FILE | File | file | 3 | Reads data from file into buffer at specified address |
| `2302` | WRITE_BLOCK_TO_FILE | File | file | 3 | Writes data from memory address into file |
| `2303` | RESOLVE_FILEPATH | Fs | file | 2 | Resolves absolute filepath. Input path can be relative, starts with 'virtual path' prefix or be already absolute filepath |
| `2304` | GET_SCRIPT_FILENAME | Fs | file | 3 | Returns a file name or full file path of a script at the address (0A9F, 0AAA, 2404). If the address is -1 then this script is used. If no script with a given pointer is found, then the condition result is set to false and output argument is not modified |
| `2305` | GET_FILE_WRITE_TIME | Fs | file | 8 | Gets last modification time of the file. On fail condition result is set to false, output parameters remain unchanged |
| `2400` | COPY_MEMORY | Memory | memory | 3 | Copies a block of memory from src address to dest address. src and dest regions may overlap (memmove behavior) |
| `2401` | READ_MEMORY_WITH_OFFSET | Memory | memory | 4 | Reads a value from the given offset from the memory address (see: 2402) |
| `2402` | WRITE_MEMORY_WITH_OFFSET | Memory | memory | 4 | Writes the value at the given offset from the memory address (see: 2401) |
| `2403` | FORGET_MEMORY | Memory | memory | 1 | Makes the memory chunk allocated with 0AC8 persistent across load/start new game events. The memory is still released when game closes causing no leaks |
| `2404` | GET_SCRIPT_STRUCT_JUST_CREATED | Memory | memory | 1 | Returns the address of a most recently (globally) created script (004F, 00D7, 0A92, 0A94) |
| `2405` | IS_SCRIPT_RUNNING | Memory | memory | 1 | Checks if address points at valid and running script |
| `2407` | IS_MEMORY_EQUAL | Memory | memory | 3 | Compares two memory blocks |
| `2408` | TERMINATE_SCRIPT |  | memory | 1 | Terminates script pointed by the address |
| `2500` | IS_AUDIO_STREAM_PLAYING | AudioStream | audio | 1 | Checks if audio stream is currently in 'play' state |
| `2501` | GET_AUDIO_STREAM_DURATION | AudioStream | audio | 2 | Gets the audio stream total duration considering its speed (see 2505) |
| `2502` | GET_AUDIO_STREAM_SPEED | AudioStream | audio | 2 | Gets audio stream playback speed multiplier |
| `2503` | SET_AUDIO_STREAM_SPEED | AudioStream | audio | 2 | Sets audio stream playback speed multiplier |
| `2504` | SET_AUDIO_STREAM_VOLUME_WITH_TRANSITION | AudioStream | audio | 3 | Changes stream volume with smooth transition |
| `2505` | SET_AUDIO_STREAM_SPEED_WITH_TRANSITION | AudioStream | audio | 3 | Changes stream speed with smooth transition. Pauses/Starts stream playback if neccesarry |
| `2506` | SET_AUDIO_STREAM_SOURCE_SIZE | AudioStream3D | audio | 2 | Sets size of 3d audio stream sound source in the world. Volume will not decay within the specified distance |
| `2507` | GET_AUDIO_STREAM_PROGRESS | AudioStream | audio | 2 | Gets audio stream playback progress as value from 0.0 to 1.0 |
| `2508` | SET_AUDIO_STREAM_PROGRESS | AudioStream | audio | 2 | Sets audio stream playback position. Progress range is from 0.0 to 1.0 |
| `2509` | GET_AUDIO_STREAM_TYPE | AudioStream | audio | 2 | Returns current volume settings type group of the stream |
| `250A` | SET_AUDIO_STREAM_TYPE | AudioStream | audio | 2 | Sets which game's master volume settings the stream should follow |
| `250B` | GET_AUDIO_STREAM_PROGRESS_SECONDS | AudioStream | audio | 2 | Returns current playback progress in seconds. Does not take in consideration current stream's playback speed |
| `250C` | SET_AUDIO_STREAM_PROGRESS_SECONDS | AudioStream | audio | 2 | Sets current playback progress in seconds. Does not take in consideration current stream's playback speed |
| `2600` | IS_TEXT_EMPTY | Text | text | 1 | Checks if string length is equal to zero |
| `2601` | IS_TEXT_EQUAL | Text | text | 3 | Compares two texts |
| `2602` | IS_TEXT_IN_TEXT | Text | text | 3 | Checks if text contains specified text |
| `2603` | IS_TEXT_PREFIX | Text | text | 3 | Checks if text starts with specified prefix text |
| `2604` | IS_TEXT_SUFFIX | Text | text | 3 | Checks if text ends with specified suffix text |
| `2605` | DISPLAY_TEXT_FORMATTED | Text | text | 4 | Formats args according to the format string then draws text at the specified on-screen position. See 033E |
| `2606` | LOAD_FXT | Text | text | 1 | Loads GXT texts from selected FXT dictionary file |
| `2607` | UNLOAD_FXT | Text | text | 1 | Unloads GXT labels defined in selected Fxt file |
| `2608` | GET_TEXT_LENGTH | Text | text | 2 | Returns count of characters in the text |
| `2609` | ADD_TEXT_LABEL_FORMATTED | Text | text | 3 | Adds or updates the text associated with the dynamic GXT key. It does nothing if the same key is defined in a FXT file |
| `2700` | IS_BIT_SET | Math | math | 2 | Checks if n-th bit of the number is set |
| `2701` | SET_BIT | Math | math | 2 | Sets n-th bit of the number |
| `2702` | CLEAR_BIT | Math | math | 2 | Clears n-th bit of the number |
| `2703` | TOGGLE_BIT | Math | math | 3 | Sets state of n-th bit in the number |
| `2704` | IS_TRUTHY | Math | math | 1 | Checks if value contains number different than 0 or not empty string |
| `2705` | PICK_RANDOM_INT | Math | math | 2 | Selects one random integer from provided values |
| `2706` | PICK_RANDOM_FLOAT | Math | math | 2 | Selects one random float from provided values |
| `2707` | PICK_RANDOM_TEXT | Math | math | 2 | Selects one random text from provided values |
| `2708` | RANDOM_CHANCE | Math | math | 1 | Sets random condition result, with percent chance to be true |
| `2709` | FLOAT_ADD |  | math | 3 | Adds together two float values and writes the result into the variable |
| `270A` | FLOAT_SUB |  | math | 3 | Subtracts the float value from another float value and writes the result into the variable |
| `270B` | FLOAT_MUL |  | math | 3 | Multiplies two float values and writes the result into the variable |
| `270C` | FLOAT_DIV |  | math | 3 | Divides the float value by another float value and writes the result into the variable |
| `2800` | DELETE_SECTION_FROM_INI_FILE | IniFile | ini | 2 | Deletes the section from the ini file |
| `2801` | DELETE_KEY_FROM_INI_FILE | IniFile | ini | 3 | Deletes the key from the ini file |
| `2880` | SET_SPHERE_COLOR | Sphere | Sphere | 4 | Changes the color of the sphere |
| `290B` | FLOAT_MUL |  | CLEO | 3 | Multiplies two float values and writes the result into the variable |
