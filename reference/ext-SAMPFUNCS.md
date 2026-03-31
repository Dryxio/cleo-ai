# SAMPFUNCS Extension Opcodes

> 382 opcodes

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0AF6` | SAMP_FORCE_SPAWN_MY_PLAYER | Sends SampRpc.Spawn to SAMP Server. Teleports our character to spawn as well |
| `0AF7` | SAMP_GET_BASE_ADDRESS | Returns a pointer to the memory address of samp.dll |
| `0AF8` | SAMP_ADD_MESSAGE_TO_CHAT | Adds one line of colored message to the chat |
| `0AF9` | SAMP_SEND_CHAT_MESSAGE | Sends SampRpc.Chat containing the message or command to the server |
| `0AFA` | SAMP_IS_AVAILABLE | Evaluates as logical true if SAMP structures was initialized. Used when checking |
| `0AFB` | SAMP_SEND_REQUEST_CLASS | Sends SampRpc.RequestClass to Server |
| `0AFC` | SAMP_SEND_SCM_EVENT | Sends SampRpc.ScmEvent information about car modification to the server |
| `0AFD` | SAMP_SET_SPECIAL_ACTION | Sets the special action for our Player |
| `0AFE` | SAMP_SEND_DEATH_BY_PLAYER | Sends SampRpc.Death to Server without our character actually dying |
| `0AFF` | SAMP_GET_CAR_BY_ID | Returns the vehicle handle using its samp vehicle id. Returns 0 If the car is no |
| `0B20` | SAMP_GET_PLAYER_CHAR_BY_ID | Returns the character handle using the Player ID. Returns -1 if the player is no |
| `0B21` | SAMP_IS_CHAT_INPUT_VISIBLE | Checks if the chat box input is open/visible |
| `0B22` | SAMP_SET_SEND_RATE | Sets the periodic delay (in milliseconds) of sending specific data type to Serve |
| `0B23` | SAMP_IS_REMOTE_PLAYER_CONNECTED | Returns true if REMOTE Player with the given ID is connected |
| `0B24` | SAMP_GET_PLAYER_POINTER | Returns the player's samp structure. Returns 0 (NULL Pointer) if player isn't co |
| `0B25` | SAMP_GET_PLAYER_HEALTH | Returns the amount of health the specified player has |
| `0B26` | SAMP_GET_PLAYER_ARMOR | Returns the amount of armor the specified player has |
| `0B27` | SAMP_SET_GAMESTATE | Sets the connection status to the server. Useful when attempting to reconnect or |
| `0B28` | SAMP_SEND_DISCONNECTED | Sends SampRpc.ScrServerQuit to the server without actually disconnecting our cli |
| `0B29` | SAMP_SET_MY_NICKNAME | Changes our nickname (visually) |
| `0B2A` | SAMP_GET_PLAYER_PING | Returns the ping of the specified player with ID |
| `0B2B` | SAMP_GET_PLAYER_ID | Returns the samp player's id controlling the character handle. Returns -1 if the |
| `0B2C` | SAMP_GET_CAR_ID | Returns the SAMP vehicle ID using its car handle |
| `0B2D` | SAMP_WRITE_SAMP_MEMORY_WITH_OFFSET | Writes the value with size to samp.dll+offset |
| `0B2E` | SAMP_READ_SAMP_MEMORY_WITH_OFFSET | Reads the value with size from samp.dll+offset |
| `0B2F` | SAMP_GET_STREAMED_OUT_PLAYER_COORDS | Returns the 3D Coordinates of a player who is outside the stream zone, if the se |
| `0B30` | SAMP_SEND_ENTER_CAR | Sends SampRpc.EnterCar to Server |
| `0B31` | SAMP_SEND_EXIT_CAR | Sends SampRpc.ExitCar to Server |
| `0B32` | SAMP_SEND_SPAWN | Sends a SampRpc.Spawn to SAMP Server without spawning our character |
| `0B33` | SAMP_SEND_DAMAGE_CAR | Sends a SampRpc.DamageCar to the Server |
| `0B34` | SAMP_HOOK_CHAT_COMMAND_AS_LOCAL | Registers a callback hooked from a client sided chat command |
| `0B35` | SF_GET_PARAMS_OF_LAST_TRIGGERED_COMMAND | Returns a pointer to a string containing the parameters of the last command ente |
| `0B36` | SAMP_GET_PLAYER_NICKNAME | Returns a pointer to the nickname of the specified player |
| `0B37` | SAMP_GET_PLAYER_COLOR | Returns the color of the specified player in 0xAARRGGBB format |
| `0B38` | SAMP_CONNECT | Connects to the specified samp server information |
| `0B39` | SAMP_GET_SERVER_ADDRESS | Returns the server's port and stores server's IP address to buffer |
| `0B3A` | SAMP_GET_SERVER_NAME | Stores the server name to buffer |
| `0B3B` | SAMP_SHOW_DIALOG | Shows an artificial SAMP dialog with specified parameter attributes |
| `0B3C` | SAMP_HAS_DIALOG_RESPONDED | Returns logical true if the last submitted SAMP Dialog is equal to the specified |
| `0B3D` | SAMP_RAKNET_CREATE_BITSTREAM | Creates a new raknet bitstream object |
| `0B3E` | SAMP_RAKNET_DELETE_BITSTREAM | Remove's the specified bitstream object, freeing it from memory |
| `0B3F` | SAMP_RAKNET_RESET_BITSTREAM | Resets all parameters/clears BitStream |
| `0B40` | SAMP_RAKNET_BITSTREAM_WRITE | Writes a specified value with datatype and datasize at the "write pointer" of th |
| `0B41` | SAMP_RAKNET_SEND_RPC_WITH_PARAMS | Sends a BitStream as an RPC with the specified parameters |
| `0B42` | SAMP_RAKNET_SEND_PACKET_WITH_PARAMS | Sends a Packet BitStream with the specified parameters. Commonly used to send da |
| `0B43` | SF_COMMAND_RETURN | Marks the end of a command callback. Used as its returning statement |
| `0B44` | SAMP_CREATE_3D_TEXT | Creates an artificial SAMP 3D text with the specified parameter attributes |
| `0B45` | SAMP_DELETE_3D_TEXT | Destroys a 3D text using it's ID |
| `0B46` | SAMP_DOES_3D_TEXT_EXIST | Returns logical true if the specified 3D text exists |
| `0B47` | SAMP_CLOSE_ACTIVE_DIALOG_WITH_BUTTON | Closes the active dialog by pressing the specified button programmatically |
| `0B48` | SAMP_GET_ACTIVE_DIALOG_SELECTED_LIST_ITEM | Returns the ID of the currently selected item on the list |
| `0B49` | SAMP_SELECT_ACTIVE_DIALOG_LIST_ITEM | Selects the id of an element in the dialog list |
| `0B4A` | SAMP_GET_ACTIVE_DIALOG_EDITBOX_TEXT | Stores the text from the input field of the active dialog to the buffer |
| `0B4B` | SAMP_SET_ACTIVE_DIALOG_EDITBOX_TEXT | Sets the text of the edit field of the active dialog's box |
| `0B4C` | SAMP_IS_DIALOG_ACTIVE | Evaluates as logical true if the specified dialog with id is currently visible |
| `0B4D` | SAMP_GET_DIALOG_STYLE | Returns the style of the active dialog. If the dialog is not opened, returns the |
| `0B4E` | SAMP_GET_DIALOG_ID | Returns the ID of the active dialog. If the dialog is not opened, returns the ID |
| `0B4F` | SAMP_GET_GAMESTATE | Returns our connection status towards the server |
| `0B50` | SAMP_GET_OBJECT_BY_ID | Returns the handle of an object using its SAMP ID |
| `0B51` | SAMP_GET_PICKUP_BY_ID | Returns the handle of a pickup using its SAMP ID |
| `0B52` | SAMP_GET_OBJECT_ID | Returns the SAMP ID of an object using its handle |
| `0B53` | SAMP_GET_PICKUP_ID | Returns the SAMP ID of a pickup using its handle |
| `0B54` | SAMP_GET_DIALOG_LIST_ITEMS_COUNT | Returns the total number of items found on the active dialog's list. If the dial |
| `0B55` | SF_WORLD_COORDS_TO_WINDOW_SCREEN_COORDS | Converts 3D coordinates from the world into window screen coordinates (pixels) |
| `0B56` | SF_SET_BUTTON | Sets the press status of a game (NOT keyboard) key |
| `0B57` | SAMP_GET_PLAYER_ANIMATION | Returns the SAMP ID of the animation currently being played by the specified pla |
| `0B58` | SAMP_GET_ANIMATION_NAME | Stores the filename and animname of the animation using its SAMP ID |
| `0B59` | SAMP_GET_ANIMATION_ID | Returns the Animation SAMP ID using its name and the file it was loaded from |
| `0B5A` | SF_GET_SCREEN_RESOLUTION | Returns the current window screen resolution in pixels |
| `0B5B` | SAMP_GET_DIALOG_LIST_ITEM_TEXT | Stores the text of an item with specific id from the active dialog's list, to bu |
| `0B5C` | SAMP_IS_PLAYER_PAUSED | Evaluates as logical true if the specified player is in paused state (or AFK) |
| `0B5D` | SAMP_SET_CURSOR_VISIBILITY | Sets the visibility status of mouse cursor |
| `0B5E` | SF_GET_CURSOR_COORD | Returns the mouse cursor's window screen coordinates in pixels |
| `0B5F` | SF_WINDOW_SCREEN_COORDS_TO_GAME_SCREEN_COORDS | Returns the GameScreen Coordinates counterpart of the specified WindowScreen Coo |
| `0B60` | SF_GAME_SCREEN_COORDS_TO_WINDOW_SCREEN_COORDS | Returns the WindowScreen Coordinates counterpart of the specified GameScreen Coo |
| `0B61` | SAMP_IS_MY_PLAYER_SPAWNED | Evaluates as logical true if our player has been spawned already |
| `0B62` | SAMP_GET_PLAYER_SPECIAL_ACTION | Returns the special action ID of the specified player |
| `0B63` | SAMP_UNHOOK_LOCAL_CHAT_COMMAND | Removes all callbacks hooked from a chatCommand created by SAMP_REGISTER_CLIENTS |
| `0B64` | SAMP_IS_PLAYER_NPC | Checks if the specified player is an NPC |
| `0B65` | SAMP_GET_PLAYER_SCORE | Returns the current score of the specified player |
| `0B66` | SF_HEX_TO_ARGB | Splits 0xAARRGGBB colorcode format into individial color channels |
| `0B67` | SF_ARGB_TO_HEX | mixes color channels into 0xAARRGGBB colorcode format |
| `0B68` | SF_D3D_DRAW_LINE | Draws a line between two window screen coordinates |
| `0B69` | SF_D3D_DRAW_BORDERLESS_BOX | Draws a rectangular area at the specified coordinates |
| `0B6A` | SF_D3D_DRAW_BORDERED_BOX | Draws a rectangular area with border at the specified coordinates |
| `0B6B` | SF_D3D_GET_DRAW_WIDTH_OF_TEXT_WITH_FONT | Returns the width (in pixels) that will be occupied by the text with font |
| `0B6C` | SF_D3D_GET_FONT_DRAW_HEIGHT | Returns the height (in pixels) occupied by any text that uses the specified font |
| `0B6D` | SF_D3D_CREATE_FONT | Creates a D3DFont Object |
| `0B6E` | SF_D3D_DELETE_FONT | Destroys the specified font object, freeing it from memory |
| `0B6F` | SF_D3D_DRAW_TEXT_WITH_FONT | Draws text using the specified font |
| `0B70` | SF_D3D_DRAW_POLYGON | Draws a polygon with the specified parameters |
| `0B71` | SF_D3D_LOAD_TEXTURE_FROM_FILE | Loads a file (any image, or txd) as D3DTexture Object |
| `0B72` | SF_D3D_RELEASE_TEXTURE | Releases the D3DTexture Object, freeing it from memory |
| `0B73` | SF_D3D_DRAW_TEXTURE | Draws the texture on the screen |
| `0B74` | SAMP_SET_CHAT_LINE | Changes the chat line's text into a custom one |
| `0B75` | SAMP_GET_CHAT_LINE | Returns the chat line's text parameters |
| `0B76` | SAMP_SET_CHAT_INPUT_TEXT | Overwrites the content written at the chat input box |
| `0B77` | SAMP_GET_CHAT_INPUT_TEXT | Returns the current text in the chat input box |
| `0B78` | SF_LOG_TO_CONSOLE | Adds a line to the SAMPFUNCS console and logs it |
| `0B79` | SAMP_SET_CHAT_INPUT_VISIBILITY | Sets the visibility status (open/closed) of the chat input box |
| `0B7A` | SAMP_GET_RAKCLIENT_INTERFACE | Returns a pointer to a RakClientInterface object |
| `0B7B` | SAMP_GET_RAKPEER | Returns a pointer to RakPeer |
| `0B7C` | SAMP_GET_RAKCLIENT_FUNC_BY_INDEX | Returns the address of the RakClientInterface virtual method table function by i |
| `0B7D` | SAMP_GET_RPC_FUNC_BY_INDEX | Returns the RPC callback address by index |
| `0B7E` | SAMP_GET_RPC_NODE_BY_INDEX | Returns a pointer to the RPC structure at index |
| `0B7F` | SAMP_GET_INFO_POINTER | Returns a pointer to a SampInfo structure |
| `0B80` | SF_DXUT_CREATE_DIALOG | Creates a DXUTDialog Object with Title |
| `0B81` | SF_DXUT_DIALOG_POP | Returns the last event and component ID that occurred with the specified dialog |
| `0B82` | SF_DXUT_DIALOG_ADD_BUTTON | Adds a button on the DXUTDialog |
| `0B83` | SF_DXUT_DIALOG_ADD_CHECKBOX | Creates a checkbox on the DxutDialog |
| `0B84` | SF_DXUT_DIALOG_SET_COORDS_AND_DIMS | Sets the coordinates and dimensions of the DxutDialog |
| `0B85` | SF_DXUT_DIALOG_GET_COORDS_AND_DIMS | Returns the Coordinates and Dimensions of the DxutDialog |
| `0B86` | SF_DXUT_DIALOG_SET_VISIBILITY | Sets the visibility status of the DxutDialog |
| `0B87` | SF_DXUT_DIALOG_IS_VISIBLE | Checks if the DxutDialog is visible |
| `0B88` | SF_DXUT_DIALOG_ADD_EDITBOX | Creates a text input field on a DxutDialog |
| `0B89` | SF_DXUT_DIALOG_GET_TEXT_OF_CONTROL | Returns the text of a control using its ID |
| `0B8A` | SAMP_RAKNET_SEND_RPC | Sends BitStream as RPC to Server |
| `0B8B` | SAMP_RAKNET_SEND_PACKET | Sends Packet BitStream to Server |
| `0B8C` | SAMP_IS_CURSOR_ACTIVE | Checks if the mouse cursor were both visible and movable |
| `0B8D` | SAMP_SET_CURSOR_MODE | Sets the cursor mode |
| `0B8E` | SAMP_GET_CURSOR_MODE | Returns the current mouse cursor mode |
| `0B8F` | SF_WINDOW_SCREEN_COORDS_TO_WORLD_COORDS | Converts window screen coordinates (pixels) to world's 3D coordinates with the s |
| `0B90` | SF_DXUT_DIALOG_SET_VISIBILITY_OF_CONTROL | Sets the visibility of the DXUTDialog's control element with ID |
| `0B91` | SF_DXUT_DIALOG_ADD_STATIC_TEXT | Adds a static text control in the DxutDialog |
| `0B92` | SF_DXUT_DIALOG_IS_CHECKBOX_CHECKED | Evaluates as logical true if the checkbox control of the DxutDialog is checked |
| `0B93` | SF_DXUT_DIALOG_SET_BACKGROUND_COLOR | Sets the background color of the DxutDialog |
| `0B94` | SF_DXUT_DIALOG_SET_TEXT_OF_CONTROL | Sets the text of a control using its ID |
| `0B95` | SF_DXUT_DIALOG_IS_CONTROL_VISIBLE | Evaluates as true if the DxutDialog's control element with ID is visible |
| `0B96` | SF_DXUT_DIALOG_ADD_SLIDER | Creates a horizontal slider on the DxutDialog |
| `0B97` | SF_DXUT_DIALOG_GET_SLIDER_VALUE | Returns the thumb position value of the DxutDialog's slider with ID |
| `0B98` | SF_DXUT_DIALOG_SET_SLIDER_VALUE | Sets the thumb position value of the DxutDialog's slider with ID |
| `0B99` | SF_DXUT_DIALOG_ADD_LISTBOX | Creates a listbox on the dialog |
| `0B9A` | SF_DXUT_DIALOG_INSERT_LISTBOX_ELEMENT | Inserts a new element into the DxutDialog's listbox with ID |
| `0B9B` | SF_DXUT_DIALOG_GET_SELECTED_LISTBOX_ELEMENT | Returns the index of the selected element and the count/number of elements in th |
| `0B9C` | SF_DXUT_DIALOG_DELETE_LISTBOX_ELEMENT | Removes the element found at the specified index from the DxutDialog's listbox w |
| `0B9D` | SF_DXUT_DIALOG_GET_LISTBOX_ELEMENT | Returns the text and data associated with the DxutDialog's listbox element by in |
| `0B9E` | SF_DXUT_DIALOG_SET_STATUS_OF_CHECKBOX | Sets the status of a checkbox |
| `0B9F` | SF_DXUT_DIALOG_SET_TITLE_VISIBILITY | Sets the visibility of the DxutDialog's title |
| `0BA0` | SF_DXUT_DIALOG_IS_TITLE_VISIBLE | Evaluates as logical true if the DxutDialog's title is visible |
| `0BA1` | SF_DXUT_DIALOG_SET_MINIMIZED | Sets the minimized status of the DxutDialog |
| `0BA2` | SF_DXUT_DIALOG_IS_MINIMIZED | Returns logical true if the DxutDialog is minimized |
| `0BA3` | SF_DXUT_DIALOG_DELETE_CONTROL | Removes a DxutDialog's control with ID and frees the memory allocated for it |
| `0BA4` | SF_DXUT_DIALOG_DELETE | Deletes the DxutDialog and frees the memory allocated for it |
| `0BA5` | SF_DXUT_DIALOG_SET_FOCUSED_CONTROL | Sets the focus of user interaction to a specific DxutDialog control with ID |
| `0BA6` | SF_DXUT_DIALOG_SET_DIMS_OF_CONTROL | Changes the dimensions of the DxutDialog control with ID |
| `0BA7` | SF_DXUT_DIALOG_GET_DIMS_OF_CONTROL | Returns the dimensions of the DxutDialog control with ID |
| `0BA8` | SF_DXUT_DIALOG_SET_COORDS_OF_CONTROL | Sets the window position of the DxutDialog control with ID |
| `0BA9` | SF_DXUT_DIALOG_GET_COORDS_OF_CONTROL | Returns the window position of a DxutDialog control |
| `0BAA` | SF_DXUT_DIALOG_SET_COLOR_OF_CHECKBOX | Sets the color of DxutDialog's checkbox control with ID |
| `0BAB` | SF_DXUT_DIALOG_EXIST | Evaluates as logical true if the specified DxutDialog exists |
| `0BAC` | SAMP_GET_SERVER_SETTINGS_POINTER | Returns the pointer to server settings structure |
| `0BAD` | SAMP_GET_POOLS_POINTER | Returns the pointer to samp pools structure |
| `0BAE` | SAMP_GET_CHAT_INFO_POINTER | Returns the pointer to samp chat information structure |
| `0BAF` | SAMP_GET_CHAT_INPUT_INFO_POINTER | Returns the pointer to samp chat input field structure |
| `0BB0` | SAMP_GET_DIALOG_INFO_POINTER | Returns the pointer to samp dialog structure |
| `0BB1` | SAMP_GET_KILL_INFO_POINTER | Returns the pointer to samp kill list structure |
| `0BB2` | SAMP_GET_MISC_INFO_POINTER | Returns the pointer to a structure of various samp miscellaneous data |
| `0BB3` | SAMP_GET_TEXTDRAW_POOL_POINTER | Returns the pointer to samp textdraw pool structure |
| `0BB4` | SAMP_GET_OBJECT_POOL_POINTER | Returns the pointer to samp object pool structure |
| `0BB5` | SAMP_GET_GANGZONE_POOL_POINTER | Returns a pointer to the pool of samp allocated territories (gang territories) |
| `0BB6` | SAMP_GET_TEXTLABEL_POOL_POINTER | Returns the pointer to 3D text pool structure |
| `0BB7` | SAMP_GET_PLAYER_POOL_POINTER | Returns the pointer to player pool structure |
| `0BB8` | SAMP_GET_CAR_POOL_POINTER | Returns the pointer to samp car pool structure |
| `0BB9` | SAMP_GET_PICKUP_POOL_POINTER | Returns the pointer to samp pickup pool structure |
| `0BBA` | SAMP_STORE_PLAYER_ONFOOT_DATA | Stores the current player's onFootData structure to the buffer |
| `0BBB` | SAMP_STORE_PLAYER_DRIVING_DATA | Stores the player's current inCarData structure to the buffer |
| `0BBC` | SAMP_STORE_PLAYER_PASSENGER_DATA | Stores the current passengerData structure of the player to the buffer |
| `0BBD` | SAMP_STORE_PLAYER_TRAILER_DATA | Stores the player's current trailerData structure to the buffer |
| `0BBE` | SAMP_STORE_PLAYER_AIM_DATA | Stores the specified player's aimData structure to the buffer |
| `0BBF` | SAMP_SEND_RCON_COMMAND | Sends an RCON command to the server |
| `0BC0` | SAMP_SEND_ONFOOT_DATA | Sends SampPacket.OnFootSync containing stOnFootData payload to the server |
| `0BC1` | SAMP_SEND_DRIVING_DATA | Sends SampPacket.DrivingSync containing stInCarData payload to the server |
| `0BC2` | SAMP_SEND_PASSENGER_DATA | Sends SampPacket.PassengerSync containing stPassengerData payload to the server |
| `0BC3` | SAMP_SEND_AIM_DATA | Sends SampPacket.AimSync containing stAimData payload to the server  |
| `0BC4` | SAMP_SEND_BULLET_DATA | Sends SampPacket.BulletSync containing stBulletData payload to the server |
| `0BC5` | SAMP_SEND_TRAILER_DATA | Sends SampPacket.TrailerSync containing stTrailerData payload to the server |
| `0BC6` | SAMP_SEND_UNOCCUPIEDCAR_DATA | Sends SampPacket.UnoccupiedCarSync containing stUnoccupiedData payload to the se |
| `0BC7` | SAMP_SEND_SPECTATOR_DATA | Sends SampPacket.SpectatorSync containing stSpectatorData  payload to the server |
| `0BC8` | SAMP_SEND_CLICK_PLAYER | Sends SampRpc.ClickPlayer about double click on player (from Scoreboard for exam |
| `0BC9` | SAMP_SEND_DIALOG_RESPONSE | Sends an SampRpc.DialogResponse to the server |
| `0BCA` | SAMP_SEND_CLICK_TEXTDRAW | Sends an SampRpc.ClickTextDraw to the server |
| `0BCB` | SAMP_SEND_GIVE_DAMAGE | Sends an SampRpc.GiveTakeDamage to the server about damage dealt by another play |
| `0BCC` | SAMP_SEND_TAKE_DAMAGE | Sends an SampRpc.GiveTakeDamage to the server about damage taken from another pl |
| `0BCD` | SAMP_SEND_EDIT_OBJECT | Sends an SampRpc.EditObject about changing the structure of an object in its edi |
| `0BCE` | SAMP_SEND_EDIT_ATTACHED_OBJECT | Sends SampRpc.EditAttachedObject about a change to an attached object in object  |
| `0BCF` | SAMP_SEND_REQUEST_INTERIOR_CHANGE | Sends SampRpc.RequestInteriorChange |
| `0BD0` | SAMP_SEND_REQUEST_SPAWN | Sends SampRpc.RequestSpawn |
| `0BD1` | SAMP_SEND_PICKED_UP_PICKUP | Sends SampRpc.PickedUpPickup to take a pickup |
| `0BD2` | SAMP_SEND_MENU_SELECT_ROW | Sends SampRpc.MenuSelect about selecting an item in a menu (GTA:SA menu) |
| `0BD3` | SAMP_SEND_QUIT_MENU | Sends SampRpc.MenuQuit to tell the server we exited the menu (GTA:SA menu) |
| `0BD4` | SAMP_SEND_CAR_DESTROYED | Sends SampRpc.CarDestroyed about destruction of a specific car (exploded or dren |
| `0BD5` | SAMP_IS_SCOREBOARD_VISIBLE | Evaluates as logical true if the scoreboard is visible |
| `0BD6` | SAMP_SET_SCOREBOARD_VISIBILITY | Sets the visibility of the scoreboard |
| `0BD7` | SAMP_GET_DIALOG_CONTENT | Returns the content of the active dialog to buffer. If the dialog is not opened, |
| `0BD8` | SAMP_GET_DIALOG_TITLE | Stores the title of the active dialog to buffer. If the dialog is not opened, th |
| `0BD9` | SAMP_SET_ACTIVE_DIALOG_ENVIRONMENT | Sets whether interactions with the active dialog would sync to the server(server |
| `0BDA` | SAMP_IS_ACTIVE_DIALOG_CLIENTSIDE | Evaluates as logical true if the active dialog is has a client side attribute |
| `0BDB` | SAMP_IS_CHAT_VISIBLE | Evaluates as logical true if chat lines are visible |
| `0BDC` | SAMP_GET_CHAT_DISPLAY_MODE | Returns the current chat display mode |
| `0BDD` | SAMP_SET_CHAT_DISPLAY_MODE | Sets the chat display mode |
| `0BDE` | SF_PAUSE_SCRIPT | Sets the specified script's isActive parameter to 0 |
| `0BDF` | SF_RESUME_SCRIPT | Sets the specified script's isActive parameter to 1 |
| `0BE0` | SAMP_RAKNET_HOOK_RETURN | Returns the flow of control to RakNet and decides whether the currently intercep |
| `0BE1` | SAMP_RAKNET_HOOK_OUTCOMING_RPC | Redirects all outgoing RPCs to the specified callback for subsequent processing  |
| `0BE2` | SAMP_RAKNET_HOOK_OUTCOMING_PACKET | Redirects all outgoing Packets to the specified callback for subsequent processi |
| `0BE3` | SAMP_RAKNET_HOOK_INCOMING_RPC | Redirects all incoming RPCs to the specified callback for subsequent processing  |
| `0BE4` | SAMP_RAKNET_HOOK_INCOMING_PACKET | Redirects all incoming packets to the specified callback for subsequent processi |
| `0BE5` | SAMP_RAKNET_HOOK_GET_PARAM | Returns the hook parameter's value of the currently executing callback |
| `0BE6` | SAMP_RAKNET_SET_HOOK_PARAM | Sets the hook parameter's value of the currently executing callback |
| `0BE7` | SAMP_RAKNET_BITSTREAM_READ | Reads a value with datatype and datasize at the "read pointer" of the specified  |
| `0BE8` | SAMP_RAKNET_BITSTREAM_READ_ARRAY | Stores an array of bytes from the Bitstream to buffer |
| `0BE9` | SAMP_RAKNET_BITSTREAM_RESET_READ_POINTER | Resets the read pointer of the BitStream. Setting "write offset = 0" |
| `0BEA` | SAMP_RAKNET_BITSTREAM_RESET_WRITE_POINTER | Resets (THIS COMMAND IS BUGGED, SETS THE WRITE POINTER AT THE BEGINNING OF THE D |
| `0BEB` | SAMP_RAKNET_BITSTREAM_SKIP_BITS | Increases both its "read pointer" and "write pointer" of the Bitstream by the sp |
| `0BEC` | SAMP_RAKNET_BITSTREAM_SET_WRITE_OFFSET | Sets the write offset of the BitStream |
| `0BED` | SAMP_RAKNET_BITSTREAM_SET_READ_OFFSET | Sets the read offset of the BitStream |
| `0BEE` | SAMP_RAKNET_BITSTREAM_GET_NUMBER_OF_BITS_USED | Returns the number of used bits in the BitStream |
| `0BEF` | SAMP_RAKNET_BITSTREAM_GET_NUMBER_OF_BYTES_USED | Returns the number of bytes used in the BitStream |
| `0BF0` | SAMP_RAKNET_BITSTREAM_GET_NUMBER_OF_UNREAD_BITS | Returns the number of unread bits in the BitStream |
| `0BF1` | SAMP_RAKNET_BITSTREAM_GET_WRITE_OFFSET | Returns the current write offset of the BitStream |
| `0BF2` | SAMP_RAKNET_BITSTREAM_GET_READ_OFFSET | Returns the current read offset of the BitStream |
| `0BF3` | SAMP_RAKNET_BITSTREAM_GET_DATA_POINTER | Returns a pointer to the BitStream's data |
| `0BF4` | SAMP_RAKNET_BITSTREAM_DECODE_COMPRESSED_STRING | Decrypts a compressed string (CString) from the bitstream then stores this to th |
| `0BF5` | SAMP_RAKNET_BITSTREAM_ENCODE_STRING | Encrypts a string stored in the buffer then stores this compressed string (CStri |
| `0BF6` | SAMP_RAKNET_BITSTREAM_EMULATE_AS_INCOMING_RPC | Emulates the BitStream's data like an incoming RPC |
| `0BF7` | SAMP_RAKNET_BITSTREAM_EMULATE_AS_INCOMING_PACKET | Emulates the BitStream's data like an Incoming Packet |
| `0BF8` | SAMP_RAKNET_GET_RPC_NAME | Returns a pointer to the RPC ID's Name |
| `0BF9` | SAMP_RAKNET_GET_PACKET_NAME | Returns a pointer to the Packet ID's Name |
| `0BFA` | SF_PUSH_LOCAL_VARIABLES | Saves the values of all local variables from the currently executing script (Mai |
| `0BFB` | SF_POP_LOCAL_VARIABLES | Restores all previously saved local variables by SF_PUSH_LOCAL_VARIABLES to the  |
| `0BFC` | SF_SET_CUSTOM_GLOBAL_VARIABLE | Sets the value of the custom global variable with name |
| `0BFD` | SF_GET_CUSTOM_GLOBAL_VARIABLE | Returns the value of the custom global variable with name |
| `0BFE` | SF_GET_TICK_COUNT | Returns the OS's current uptime in milliseconds. Recommended substitute for TIME |
| `0BFF` | SF_PROCESS_LINE_OF_SIGHT | Checks for collisions using flags from the start of the vector to its end |
| `0C00` | SF_ABS | Returns the absolute value of a number (float or integer) |
| `0C01` | SF_RADIANS_TO_DEGREES | Converts radians to degrees |
| `0C02` | SF_DEGREES_TO_RADIANS | Converts degrees to radians |
| `0C03` | SF_SIN | Returns the sine of the specified radians |
| `0C04` | SF_ASIN | Returns the radian arcsine of the specified ratio |
| `0C05` | SF_COS | Returns the cosine of the specified radians |
| `0C06` | SF_ACOS | Returns the radian arccosine of the specified ratio |
| `0C07` | SF_TAN | Returns the tangent of the specified radians |
| `0C08` | SF_ATAN | Returns the radian arctangent of the specified ratio |
| `0C09` | SF_POW | Raises a number to the specified power |
| `0C0A` | SF_CEIL | Returns the rounded-up result the specified number |
| `0C0B` | SF_FLOOR | Returns the rounded-down result the specified number |
| `0C0C` | SF_READ_MEMORY_WITH_OFFSET | Reads the value with size from memory address with offset |
| `0C0D` | SF_WRITE_MEMORY_WITH_OFFSET | Writes the value with size to memory address with offset |
| `0C0E` | SF_READ_ELEMENT_OF_4BYTES_ARRAY | Reads the value from the specified element index of an array |
| `0C0F` | SF_WRITE_ELEMENT_OF_4BYTES_ARRAY | Writes the value to the specified element index of an array |
| `0C10` | SF_MEMCPY | Copies a memory block with size from source address to destination address |
| `0C11` | SF_MEMFILL | Fills a sized memory block with value byte-by-byte |
| `0C12` | SF_MEMEQ | Evaluates as logical true if both memory blocks have the same content |
| `0C13` | SF_STRCPY | Copies the string from source to destination |
| `0C14` | SF_STREQ | Evaluates as logical true if both case-sensitive strings are equal |
| `0C15` | SF_STRCAT | Appends the appendedString at the end of the string found at the stringBuffer |
| `0C16` | SF_STRTOK | Searches the stringBuffer for any delimiters then replaces the first hit with a  |
| `0C17` | SF_STRLEN | Returns the length of a string |
| `0C18` | SF_STRSTR | Returns a pointer to the first occurence of a specified substring in the source  |
| `0C19` | SF_STRCSPN | Searches the string for any matching characters at the characterList. Returns th |
| `0C1A` | SF_ATOI | Converts an ascii string into a decimal integer |
| `0C1B` | SF_ATOF | Converts an ascii string into a floating point number |
| `0C1C` | SF_ITOA | Converts a baseN integer into an ascii string then stores it to stringBuffer |
| `0C1D` | SF_READ_ELEMENT_OF_SIZED_ARRAY | Reads the value of the sized array's element at index. The size per element is c |
| `0C1E` | SF_WRITE_ELEMENT_OF_SIZED_ARRAY | Writes the value to the specified element index of a sized array. The size per e |
| `0C1F` | SF_GET_ELEMENT_POINTER_OF_BUFFER_ARRAY | Returns a pointer to the element of an array of sized buffers using its element  |
| `0C20` | SF_WRITE_STRING_TO_ELEMENT_OF_BUFFER_ARRAY | Writes a string at the buffer element of an array of sized buffers using its ele |
| `0C21` | SF_STRIEQ | Evaluates as logical true if both case-insensitive strings are equal |
| `0C22` | SF_BIN_TO_HEX | Converts binary text to hexadecimal text and stores at stringBuffer. Can be used |
| `0C23` | SF_HEX_TO_BIN | Converts hexadecimal text to binary text and stores at stringBuffer. Can be used |
| `0C24` | SF_STRNCPY | Copies the string safely from source to stringBuffer. The copied string will be  |
| `0C25` | SF_STRNEQ | Evaluates as logical true if all characters with length at the beginning of both |
| `0C26` | SF_STRUPR | Converts all letters of the source's string into CAPITAL LETTERS stored at desti |
| `0C27` | SF_STRNCAT | Appends a appendedString safely at the end of the string found at the stringBuff |
| `0C28` | SF_STRLWR | Converts all letters of the source's string into non-capital letters stored at d |
| `0C29` | SF_STRISTR | Returns a pointer to the first case-insensitive occurence of the specified subst |
| `0C2A` | SF_STRCHR | Returns a pointer to the first occurence of the specified ascii character in the |
| `0C2B` | SF_STRPBRK | Searches the source's string for any matching characters at the characterList. R |
| `0C2C` | SF_STRRCHR | Returns a pointer to the last occurence of the specified ascii character in the  |
| `0C2D` | SF_STRREV | Reverses the source's string, changing the positions of characters, then stores  |
| `0C2E` | SF_STRSPN | Searches the source's string then returns the index of the first character that  |
| `0C2F` | SF_STRTOL | Ignores any whitespace at the beginning of the source's string, converting the n |
| `0C30` | SF_MATRIX_TO_QUAT | Converts a matrix structure into a quaternion structure stored at quaternionBuff |
| `0C31` | SF_QUAT_TO_MATRIX | Converts a quaternion structure into a matrix structure stored at matrixBuffer |
| `0C32` | SF_AXES_TO_QUAT | Converts the basis vectors of a rotation matrix into quaternion values |
| `0C33` | SF_QUAT_TO_AXES | Converts the quaternion values into basis vectors of a rotation matrix |
| `0C34` | SF_REGISTER_CUSTOM_GLOBAL_FUNCTION | Registers the name of a custom global function allowing other scripts to call it |
| `0C35` | SF_CALL_CUSTOM_GLOBAL_FUNCTION | Calls a registered custom global function with name |
| `0C36` | SF_CUSTOM_GLOBAL_FUNCTION_RETURN | Returns the flow of the execution to the next instruction after the custom globa |
| `0C37` | SF_IS_CUSTOM_GLOBAL_FUNCTION_REGISTERED | Evaluates as logical true if the specified name is registered a custom global fu |
| `0C38` | SF_CUSTOM_GLOBAL_FUNCTION_GET_ORIGIN | Returns the origin informations of a custom global function with name |
| `0C39` | SF_UNREGISTER_CUSTOM_GLOBAL_FUNCTION | Removes the currently registered custom global function. Allowing its name to be |
| `0C3A` | SF_STRING_POINTER | Stores a pointer to the specified string into the variable |
| `0C3B` | SF_D3D_BEGIN | Begins the D3D primitiveType used for rendering |
| `0C3C` | SF_D3D_END | Calls the D3D EndScene method |
| `0C3D` | SF_D3D_COLOR | Sets the D3D's current drawing color |
| `0C3E` | SF_D3D_VERTEX | Sets a vertex using the currently used primitive type specified by SF_D3D_BEGIN |
| `0C3F` | SF_D3D_SET_TEXTURE_COORDS | Sets the Texture Coordinates of the D3D primitive |
| `0C40` | SF_D3D_BIND_TEXTURE | Binds a Texture to our D3D primitive |
| `0C41` | SF_D3D_TEXTURE_STRUCT | This command has no documention provided by the SF author |
| `0C42` | SF_D3D_TEXTURE_SPRITE | This command has no documention provided by the SF author |
| `0C43` | SF_D3D_GET_TEXTURE_SIZE | Returns the dimensions occupied by texture structure |
| `0C44` | SF_D3D_SET_RENDER_STATE | Sets the rendering status of a D3D primitiveType |
| `0C45` | SAMP_CREATE_3D_TEXT_WITH_ID | Creates/overwrites a 3D text with the specified ID |
| `0C46` | SAMP_GET_3D_TEXT_PARAMS | Returns all the informations about a SampTextLabel3D using its ID |
| `0C47` | SAMP_SET_3D_TEXT | Sets new text for 3D text |
| `0C48` | SAMP_CREATE_TEXTDRAW | Modifies a textdraw with the specified parameters, creating it if it doesn't exi |
| `0C49` | SAMP_SET_TEXTDRAW_BOX | Sets the parameters of the "box" (rectangle) of the text draw |
| `0C4A` | SAMP_SET_TEXTDRAW_ALIGNMENT | Sets the alignment of the text in the textdraw |
| `0C4B` | SAMP_SET_TEXTDRAW_PROPORTIONALITY | Sets whether the text scaling status is proportional to the text draw or not |
| `0C4C` | SAMP_SET_TEXTDRAW_STYLE | Sets the text draw style |
| `0C4D` | SAMP_SET_TEXTDRAW_SHADOW | Sets a shadow on the text draw |
| `0C4E` | SAMP_SET_TEXTDRAW_OUTLINE | Sets the outline of the text draw |
| `0C4F` | SAMP_SET_TEXTDRAW_MODEL | Sets the model (object, auto) of the text draw for style 5 |
| `0C50` | SAMP_SET_TEXTDRAW_TEXT | Sets the text of the textdraw |
| `0C51` | SAMP_SET_TEXTDRAW_COORDS | Sets the gamescreen coordinates of the textdraw |
| `0C52` | SAMP_SET_TEXTDRAW_CHARACTER_PROPERTIES | Sets the size and color property of all characters in the textdraw |
| `0C53` | SAMP_GET_TEXTDRAW_BOX | Returns the parameters of the "box" (rectangle) of the specified text draw |
| `0C54` | SAMP_GET_TEXTDRAW_ALIGNMENT | Sets the alignment of the text in the textdraw |
| `0C55` | SAMP_GET_TEXTDRAW_PROPORTIONALITY | Returns true if the text scaling status is proportional to the text draw |
| `0C56` | SAMP_GET_TEXTDRAW_STYLE | Returns the text draw style |
| `0C57` | SAMP_GET_TEXTDRAW_SHADOW | Returns the tickness and color property of the text draw's shadow |
| `0C58` | SAMP_GET_TEXTDRAW_OUTLINE | Returns the tickness and color property of the text draw's outline |
| `0C59` | SAMP_GET_TEXTDRAW_MODEL | Returns the properties of the text draw as a model (style 5) |
| `0C5A` | SAMP_STORE_TEXTDRAW_TEXT | Stores the textdraw's text to stringBuffer |
| `0C5B` | SAMP_GET_TEXTDRAW_COORDS | Returns the gamescreen coordinates of the textdraw |
| `0C5C` | SAMP_GET_TEXTDRAW_CHARACTER_PROPERTIES | Returns the size and color property of all characters in the textdraw |
| `0C5D` | SAMP_DOES_TEXTDRAW_EXIST | Evaluates as logical true if the specified textdraw exists |
| `0C5E` | SAMP_DELETE_TEXTDRAW | Deletes the specified textdraw |
| `0C5F` | SF_DOES_CUSTOM_GLOBAL_VARIABLE_EXIST | Evaluates as logical true if a custom global variable with specified name existe |
| `0C60` | SF_SET_CUSTOM_GLOBAL_VARIABLE_SCOPE | Sets whether the specified script can read or write to the specified custom glob |
| `0C61` | SF_GET_CUSTOM_GLOBAL_VARIABLE_SCOPE | Returns the specified script's read/write permissions to the specified custom gl |
| `0C62` | SF_EXECUTE_CONSOLE_COMMAND | Executes the specified command in the SAMPFUNCS console |
| `0C63` | SF_REGISTER_CONSOLE_COMMAND | Registers a callback hooked on a SAMPFUNCS console command with maximum length o |
| `0C64` | SF_UNREGISTER_CONSOLE_COMMAND | Removes the specified SAMPFUNCS console command. This command does nothing if th |
| `0C65` | SF_DOWNLOAD_FILE | Downloads a file from the specified url source asynchronosly then saves it to fi |
| `0C66` | SF_GET_DOWNLOAD_STATE | Returns the download status of the SfDownload object |
| `0C67` | SF_STORE_OS_ENVIRONMENT_VARIABLE | Stores the contents of the specified Windows variable (or environment variable)  |
| `0C68` | SF_UNICODE_TO_ANSI | Converts a Unicode string to ANSI string then stores it to ansiStringBuffer |
| `0C69` | SF_ANSI_TO_UNICODE | Converts an ANSI string to Unicode string then stores it to ansiStringBuffer |
| `0C6A` | SF_START_NEW_SCRIPT_FROM_LABEL | Starts a new script from the specified scriptLabel then stores its pointer at ne |
| `0C6B` | SF_START_NEW_SCRIPT_FROM_POINTER | Starts a new script from the specified memory location where a script binary dat |
| `0C6C` | SF_SET_SCRIPT_LOCAL_VARIABLE | Sets the values for a local variable in the specified script |
| `0C6D` | SF_GET_SCRIPT_LOCAL_VARIABLE | Returns the value of a local variable in the specified script |
| `0C6E` | SF_TERMINATE_SCRIPT | Terminates a script pointed by the address |
| `0C6F` | SF_RESTART_SCRIPT | Restarts a script pointed by the address |
| `0C70` | SF_GET_LOADED_MODULE | Returns the handle of a loaded module with name (moduleName) |
| `0C71` | SF_GET_MODULE_PROCEDURE | Returns a pointer (functionPtr) to specified functionName inside the moduleHandl |
| `0C72` | SF_SET_KEY_STATUS | Sets whether a specific virtual key code is pressed or not |
| `0C73` | SF_SET_CHARACTER_KEY_STATUS | Sets whether a specific virtual key represented in ascii character format is pre |
| `0C74` | SF_CREATE_TIMER | Creates and starts an SfTimer object that periodically executes its callback upo |
| `0C75` | SF_DELETE_TIMER | Removes the specified SfTimer object, freeing it from memory |
| `0C76` | SF_RESET_TIMER | Resets the expiration time of the SfTimer, restarting its trigger countdown |
| `0C77` | SF_SET_TIMER_INTERVAL | Sets a new interval for the SfTimer |
| `0C78` | SF_SET_TIMER_STATUS | Activates or pauses an SfTimer's functionality |
| `0C79` | SF_IS_TIMER_ACTIVE | Evaluates as logical true if the SfTimer is active |
| `0C7A` | SF_GET_TIMER_INTERVAL | Returns the SfTimer's configured interval |
| `0C7B` | SF_GET_TIMER_ELAPSED_TIME | Returns the number of milliseconds that have passed since the last SfTimer reset |
| `0C7C` | SF_GET_TIMER_TIME_LEFT | Returns the number of milliseconds remaining before the SfTimer expires (decreme |
| `0C7D` | SF_RELEASE_DOWNLOAD | Frees an SfDownload object from memory |
| `0C7E` | SF_IS_CONSOLE_OPEN | Evaluates as logical true if the SAMPFUNCS console is open |
| `0C7F` | SAMP_SET_LOCAL_CHAT_COMMAND_DESCRIPTION | Sets the description for the local command |
| `0C80` | SF_SET_CONSOLE_COMMAND_DESCRIPTION | Sets the description for the console command |
| `0C81` | SAMP_FORCE_DRIVING_SYNC | Sends SampPacket.DrivingSync to server about our character driving a car with ID |
| `0C82` | SAMP_FORCE_UNOCCUPIED_SYNC | Sends SampPacket.UnoccupiedCarSync to server about a seatId of a car with carId  |
| `0C83` | SAMP_FORCE_ONFOOT_SYNC | Sends SampPacket.OnFootSync to server about our character being onfoot |
| `0C84` | SAMP_FORCE_AIM_SYNC | Sends SampPacket.AimSync containing our current aim data, to server |
| `0C85` | SAMP_FORCE_TRAILER_SYNC | Sends SampPacket.TrailerSync to server about a trailer with ID being attached to |
| `0C86` | SAMP_FORCE_PASSENGER_SYNC | Sends SampPacket.PassengerSync to server about our character sitting at seatId o |
| `0C87` | SAMP_FORCE_STATS_SYNC | Sends SampPacket.StatsUpdate containing our current money and drunk level, to se |
| `0C88` | SAMP_FORCE_WEAPONS_SYNC | Sends SampPacket.WeaponsUpdate containing our character's current weapons, to se |
| `0C89` | SF_KEY_JUST_PRESSED | Evaluates as logical true if the specified virtual keyCode has been pressed just |
| `0C8A` | SAMP_GET_MAX_PLAYER_ID | Returns the maximum player ID currently streamed if streamedOnly = true. Else, r |
| `0C8B` | SAMP_GET_PLAYER_COUNT | Returns the number of players that are currently streamed if streamedOnly = true |
| `0C8C` | SF_D3D_LOAD_TEXTURE_FROM_FILE_IN_MEMORY | Loads a texture from a file located in memory buffer |
| `0C8D` | SF_WRITE_TEXT_TO_CLIPBOARD | Sets the text on the clipboard |
| `0C8E` | SF_READ_DATA_FROM_CLIPBOARD | Copies raw binary or text from the clipboard to buffer |
| `0C8F` | SAMP_PROCESS_CHAT_INPUT | Processes a message by SAMPFUNCS callbacks, then sent to server as SampRpc.Chat |
| `0C90` | SAMP_IS_CHAT_COMMAND_HOOKED | Evaluates as logical true if the specified command is localized by a callback ho |
| `0C91` | SF_IS_CONSOLE_COMMAND_REGISTERED | Returns logical true if the specified console command is registered |
| `0C92` | SF_GET_CLEO_LIBRARY_VERSION | Returns the installed version of CLEO |
| `1337` | SF_MAKE_SCRIPT_PRIVATE | Makes the script where this command is executed invisible across other scripts |

## Detailed Reference

### Car

### `0B2C` SAMP_GET_CAR_ID
Returns the SAMP vehicle ID using its car handle

**Class:** `Car.GetSampId`

**Input:**
- `self: Car`

**Output:**
- `id: int (variable)`

---

### Char

### `0B2B` SAMP_GET_PLAYER_ID
Returns the samp player's id controlling the character handle. Returns -1 if the character isn't controlled by any Player

**Class:** `Char.GetSampId`

**Input:**
- `self: Char`

**Output:**
- `idAsHandle: SampPlayer (variable)`

---

### Object

### `0B52` SAMP_GET_OBJECT_ID
Returns the SAMP ID of an object using its handle

**Class:** `Object.GetSampId`
**Flags:** condition

**Input:**
- `self: Object`

**Output:**
- `id: int (variable)`

**Details:**

Can be used as a condition which evaluates as true it's from the SAMP Object Pool

---

### Pickup

### `0B53` SAMP_GET_PICKUP_ID
Returns the SAMP ID of a pickup using its handle

**Class:** `Pickup.GetSampId`
**Flags:** condition

**Input:**
- `self: Pickup`

**Output:**
- `id: int (variable)`

**Details:**

Can be used as a condition which evaluates as true it's from the SAMP Pickup Pool

---

### SampBitstream

### `0B3D` SAMP_RAKNET_CREATE_BITSTREAM
Creates a new raknet bitstream object

**Class:** `SampBitstream.Create`
**Flags:** constructor

**Output:**
- `handle: SampBitstream (variable)`

**Details:**

This command allocates memory for the object, and needs to be manually destroyed when not used by executing command SAMP_RAKNET_DELETE_BITSTREAM to free it from memory

---

### `0B3E` SAMP_RAKNET_DELETE_BITSTREAM
Remove's the specified bitstream object, freeing it from memory

**Class:** `SampBitstream.Delete`
**Flags:** condition, destructor

**Input:**
- `self: SampBitstream`

**Details:**

Can be used as a condition which evaluates as false if the bitstream is invalid, or cannot be deleted.

---

### `0B3F` SAMP_RAKNET_RESET_BITSTREAM
Resets all parameters/clears BitStream

**Class:** `SampBitstream.Reset`
**Flags:** condition

**Input:**
- `self: SampBitstream`

**Details:**

Can be used as a condition which evaluates as true if the bitstream is valid.

---

### `0B40` SAMP_RAKNET_BITSTREAM_WRITE
Writes a specified value with datatype and datasize at the "write pointer" of the specified bitstream, then advances its "write pointer" by the same size

**Class:** `SampBitstream.Write`
**Flags:** condition

**Input:**
- `self: SampBitstream`
- `value: any`
- `dataType: SampBitStreamDataType`
- `dataSize: int`

**Details:**

Can be used as a condition which evaluates as true if the bitstream is valid.

---

### `0B41` SAMP_RAKNET_SEND_RPC_WITH_PARAMS
Sends a BitStream as an RPC with the specified parameters

**Class:** `SampBitstream.SendAsRpcWithParams`
**Flags:** condition

**Input:**
- `rpc: SampRpc`
- `self: SampBitstream`
- `priority: SampPriority`
- `reliability: SampReliability`
- `orderingChannel: int`
- `shiftTimeStamp: int`

---

### `0B42` SAMP_RAKNET_SEND_PACKET_WITH_PARAMS
Sends a Packet BitStream with the specified parameters. Commonly used to send dacket data to server

**Class:** `SampBitstream.SendAsPacketWithParams`
**Flags:** condition

**Input:**
- `self: SampBitstream`
- `priority: SampPriority`
- `reliability: SampReliability`
- `orderingChannel: int`

---

### `0B8A` SAMP_RAKNET_SEND_RPC
Sends BitStream as RPC to Server

**Class:** `SampBitstream.SendAsRpc`
**Flags:** condition

**Input:**
- `rpcId: SampRpc`
- `self: SampBitstream`

**Details:**

Can be used as a condition which evaluates as true if this RPC Bitstream has been sent successfully

---

### `0B8B` SAMP_RAKNET_SEND_PACKET
Sends Packet BitStream to Server

**Class:** `SampBitstream.SendAsPacket`
**Flags:** condition

**Input:**
- `self: SampBitstream`

**Details:**

Can be used as a condition which evaluates as true if this Bitstream has been sent successfully

---

### `0BE7` SAMP_RAKNET_BITSTREAM_READ
Reads a value with datatype and datasize at the "read pointer" of the specified bitstream , then advances its "read pointer" by the same size

**Class:** `SampBitstream.Read`
**Flags:** condition

**Input:**
- `self: SampBitstream`
- `dataType: SampBitStreamDataType`

**Output:**
- `value: any (variable)`

---

### `0BE8` SAMP_RAKNET_BITSTREAM_READ_ARRAY
Stores an array of bytes from the Bitstream to buffer

**Class:** `SampBitstream.ReadArray`
**Flags:** condition

**Input:**
- `self: SampBitstream`
- `buffer: int`
- `size: int`

---

### `0BE9` SAMP_RAKNET_BITSTREAM_RESET_READ_POINTER
Resets the read pointer of the BitStream. Setting "write offset = 0"

**Class:** `SampBitstream.ResetReadPtr`
**Flags:** condition

**Input:**
- `self: SampBitstream`

---

### `0BEA` SAMP_RAKNET_BITSTREAM_RESET_WRITE_POINTER
Resets (THIS COMMAND IS BUGGED, SETS THE WRITE POINTER AT THE BEGINNING OF THE DATA ( WRITE OFFSET = 0) WHICH IS WRONG. DO NOT USE) the value write pointer in the BitStream

**Class:** `SampBitstream.ResetWritePtr`
**Flags:** condition

**Input:**
- `self: SampBitstream`

---

### `0BEB` SAMP_RAKNET_BITSTREAM_SKIP_BITS
Increases both its "read pointer" and "write pointer" of the Bitstream by the specified bit count

**Class:** `SampBitstream.SkipBits`
**Flags:** condition

**Input:**
- `self: SampBitstream`
- `bitCount: int`

---

### `0BEC` SAMP_RAKNET_BITSTREAM_SET_WRITE_OFFSET
Sets the write offset of the BitStream

**Class:** `SampBitstream.SetWriteOffset`
**Flags:** condition

**Input:**
- `self: SampBitstream`
- `offset: int`

---

### `0BED` SAMP_RAKNET_BITSTREAM_SET_READ_OFFSET
Sets the read offset of the BitStream

**Class:** `SampBitstream.SetReadPtr`
**Flags:** condition

**Input:**
- `self: SampBitstream`
- `offset: int`

---

### `0BEE` SAMP_RAKNET_BITSTREAM_GET_NUMBER_OF_BITS_USED
Returns the number of used bits in the BitStream

**Class:** `SampBitstream.GetBitsUsed`

**Input:**
- `self: SampBitstream`

**Output:**
- `usedBits: int (variable)`

---

### `0BEF` SAMP_RAKNET_BITSTREAM_GET_NUMBER_OF_BYTES_USED
Returns the number of bytes used in the BitStream

**Class:** `SampBitstream.GetBytesUsed`
**Flags:** condition

**Input:**
- `self: SampBitstream`

**Output:**
- `usedBytes: int (variable)`

---

### `0BF0` SAMP_RAKNET_BITSTREAM_GET_NUMBER_OF_UNREAD_BITS
Returns the number of unread bits in the BitStream

**Class:** `SampBitstream.GetUnreadBits`
**Flags:** condition

**Input:**
- `self: SampBitstream`

**Output:**
- `unreadBits: int (variable)`

---

### `0BF1` SAMP_RAKNET_BITSTREAM_GET_WRITE_OFFSET
Returns the current write offset of the BitStream

**Class:** `SampBitstream.GetWriteOffset`
**Flags:** condition

**Input:**
- `self: SampBitstream`

**Output:**
- `offset: int (variable)`

---

### `0BF2` SAMP_RAKNET_BITSTREAM_GET_READ_OFFSET
Returns the current read offset of the BitStream

**Class:** `SampBitstream.GetReadOffset`
**Flags:** condition

**Input:**
- `self: SampBitstream`

**Output:**
- `offset: int (variable)`

---

### `0BF3` SAMP_RAKNET_BITSTREAM_GET_DATA_POINTER
Returns a pointer to the BitStream's data

**Class:** `SampBitstream.GetDataPtr`
**Flags:** condition

**Input:**
- `self: SampBitstream`

**Output:**
- `address: int (variable)`

---

### `0BF4` SAMP_RAKNET_BITSTREAM_DECODE_COMPRESSED_STRING
Decrypts a compressed string (CString) from the bitstream then stores this to the buffer

**Class:** `SampBitstream.DecodeCString`
**Flags:** condition

**Input:**
- `self: SampBitstream`
- `buffer: int`
- `buffersize: int`

**Details:**

* The Decompressed string has a maximum length of 4096 characters, which means the maximum reasonable buffer size is 4097 (including the null terminator). 
* The start of the **CString** must be found bitstream's **read offset**.
* The **read offset** increases by the length of the **CString**.
* Can be used as a condition which evaluates as true if the **CString** has been decompressed and the buffer has enough space to fit the entire decompressed string (including its null terminator).

---

### `0BF5` SAMP_RAKNET_BITSTREAM_ENCODE_STRING
Encrypts a string stored in the buffer then stores this compressed string (CString) to the bitstream

**Class:** `SampBitstream.EncodeString`
**Flags:** condition

**Input:**
- `self: SampBitstream`
- `buffer: int`
- `bufferSize: int`

**Details:**

* The **CString** will be written at the bitstream's **write offset**.
* The **write offset** increases by the length of the **CString**.
* Can be used as a condition which evaluates as true if the string has been compressed into a **CString** and was written at the bitstream.

---

### `0BF6` SAMP_RAKNET_BITSTREAM_EMULATE_AS_INCOMING_RPC
Emulates the BitStream's data like an incoming RPC

**Class:** `SampBitstream.EmulateAsRpcIn`
**Flags:** condition

**Input:**
- `id: SampRpc`
- `self: SampBitstream`

**Details:**

* This command **does not** trigger all callbacks created by SAMP_RAKNET_HOOK_INCOMING_RPC.
* Can be used as a condition which evaluates as true if this Fake RPC Data has been marked by RakNet as a valid data.

---

### `0BF7` SAMP_RAKNET_BITSTREAM_EMULATE_AS_INCOMING_PACKET
Emulates the BitStream's data like an Incoming Packet

**Class:** `SampBitstream.EmulateAsPacketIn`
**Flags:** condition

**Input:**
- `id: SampPacket`
- `self: SampBitstream`

**Details:**

* This command **does not** trigger all callbacks created by SAMP_RAKNET_HOOK_INCOMING_PACKET.
* Can be used as a condition which evaluates as true if this Fake Packet Data has been marked by RakNet as a valid data.

---

### SampChat

### `0AF8` SAMP_ADD_MESSAGE_TO_CHAT
Adds one line of colored message to the chat

**Class:** `SampChat.AddMsg`
**Flags:** static

**Input:**
- `format: string`
- `color: int`
- `args: arguments`

**Details:**

* This chat message is local sided and is not sent to server.
* Can process formatted string.
* The color must be in 0xAARRGGBB format where A = Alpha, R = Red, G = Green, B = Blue.

---

### `0B74` SAMP_SET_CHAT_LINE
Changes the chat line's text into a custom one

**Class:** `SampChat.SetLine`
**Flags:** condition, static

**Input:**
- `chatLineid: int`
- `body: string`
- `prefix: string`
- `bodyColor: int`
- `prefixColor: int`

**Details:**

* chatlineid value must range between 0-99. Where:
    * chatlineid = 0 indicates the latest viewable chat message (when you fully crolled down).
    * chatlineid = 99 indicates the oldest viewable chat message (when you fully scrolled up).
* textcolor and prefixcolor must be in 0xAARRGGBB format where A = Alpha, R = Red, G = Green, B = Blue.
* Can be used as a condition which evaluates as true if chatlineid is valid.

---

### `0B75` SAMP_GET_CHAT_LINE
Returns the chat line's text parameters

**Class:** `SampChat.GetLine`
**Flags:** condition, static

**Input:**
- `index: int`

**Output:**
- `bodyBuffer: string (variable)`
- `prefixBuffer: string (variable)`
- `bodyColor: int (variable)`
- `prefixColor: int (variable)`

**Details:**

* chatLineId value must range between 0-99. Where:
    * chatLineId = 0 indicates the latest viewable chat message (when you fully crolled down).
    * chatLineId = 99 indicates the oldest viewable chat message (when you fully scrolled up).
* bodyBuffer and prefixBuffer must be a memory buffer where the string will be written.
* textColor and prefixColor are in 0xAARRGGBB format where A = Alpha, R = Red, G = Green, B = Blue.
* Can be used as a condition which evaluates as true if chatLineId is valid.

---

### `0BDB` SAMP_IS_CHAT_VISIBLE
Evaluates as logical true if chat lines are visible

**Class:** `SampChat.IsVisible`
**Flags:** condition, static

---

### `0BDC` SAMP_GET_CHAT_DISPLAY_MODE
Returns the current chat display mode

**Class:** `SampChat.GetDisplayMode`
**Flags:** static

**Output:**
- `mode: SampChatDisplayMode (variable)`

---

### `0BDD` SAMP_SET_CHAT_DISPLAY_MODE
Sets the chat display mode

**Class:** `SampChat.SetDisplayMode`
**Flags:** static

**Input:**
- `mode: SampChatDisplayMode`

---

### SampChatInput

### `0B21` SAMP_IS_CHAT_INPUT_VISIBLE
Checks if the chat box input is open/visible

**Class:** `SampChatInput.IsVisible`
**Flags:** condition, static

---

### `0B76` SAMP_SET_CHAT_INPUT_TEXT
Overwrites the content written at the chat input box

**Class:** `SampChatInput.SetText`
**Flags:** static

**Input:**
- `text: string`

---

### `0B77` SAMP_GET_CHAT_INPUT_TEXT
Returns the current text in the chat input box

**Class:** `SampChatInput.GetText`
**Flags:** condition, static

**Output:**
- `buffer: string (variable)`

**Details:**

Can be used as a condition which evaluates as false if stringbuffertext cannot be written to or is invalid.

---

### `0B79` SAMP_SET_CHAT_INPUT_VISIBILITY
Sets the visibility status (open/closed) of the chat input box

**Class:** `SampChatInput.SetVisibility`
**Flags:** static

**Input:**
- `isVisible: bool`

---

### `0C8F` SAMP_PROCESS_CHAT_INPUT
Processes a message by SAMPFUNCS callbacks, then sent to server as SampRpc.Chat

**Class:** `SampChatInput.Process`
**Flags:** static

**Input:**
- `text: string`

---

### SampClient

### `0AF7` SAMP_GET_BASE_ADDRESS
Returns a pointer to the memory address of samp.dll

**Class:** `SampClient.GetBaseAddress`
**Flags:** static

**Output:**
- `pointer: int (variable)`

---

### `0AFA` SAMP_IS_AVAILABLE
Evaluates as logical true if SAMP structures was initialized. Used when checking if gta sa is running on SAMP or in Single Player

**Class:** `SampClient.IsAvailable`
**Flags:** condition, static

---

### `0AFD` SAMP_SET_SPECIAL_ACTION
Sets the special action for our Player

**Class:** `SampClient.SetSpecialAction`
**Flags:** static

**Input:**
- `id: SampSpecialAction`

**Details:**

Our character will perform this special action as well. Executing this opcocommandde is like receiving a SampRpc.ScrSetPlayerSpecialAction from the Server

---

### `0AFF` SAMP_GET_CAR_BY_ID
Returns the vehicle handle using its samp vehicle id. Returns 0 If the car is not in the stream zone

**Class:** `SampClient.GetCar`
**Flags:** static

**Input:**
- `id: int`

**Output:**
- `handle: Car (variable)`

---

### `0B22` SAMP_SET_SEND_RATE
Sets the periodic delay (in milliseconds) of sending specific data type to Server

**Class:** `SampClient.SetSendRate`
**Flags:** static

**Input:**
- `type: SampSendRateType`
- `delay: int`

---

### `0B27` SAMP_SET_GAMESTATE
Sets the connection status to the server. Useful when attempting to reconnect or disconnect to server

**Class:** `SampClient.SetGameState`
**Flags:** static

**Input:**
- `id: SampGameState`

---

### `0B2D` SAMP_WRITE_SAMP_MEMORY_WITH_OFFSET
Writes the value with size to samp.dll+offset

**Class:** `SampClient.WriteMemoryWithOffset`
**Flags:** static

**Input:**
- `offset: int`
- `value: any`
- `size: int`

---

### `0B2E` SAMP_READ_SAMP_MEMORY_WITH_OFFSET
Reads the value with size from samp.dll+offset

**Class:** `SampClient.ReadMemoryWithOffset`
**Flags:** static

**Input:**
- `offset: int`
- `size: int`

**Output:**
- `value: any (variable)`

---

### `0B39` SAMP_GET_SERVER_ADDRESS
Returns the server's port and stores server's IP address to buffer

**Class:** `SampClient.GetServerAddress`
**Flags:** static

**Output:**
- `buffer: string (variable)`
- `port: int (variable)`

**Details:**

The server ip written to the string buffer is always in ip address format (not in domain name format)

---

### `0B3A` SAMP_GET_SERVER_NAME
Stores the server name to buffer

**Class:** `SampClient.GetServerName`
**Flags:** static

**Output:**
- `buffer: string (variable)`

---

### `0B3B` SAMP_SHOW_DIALOG
Shows an artificial SAMP dialog with specified parameter attributes

**Class:** `SampClient.ShowDialog`
**Flags:** static

**Input:**
- `id: int`
- `title: string`
- `content: string`
- `leftOrMiddleButtonName: string`
- `rightButtonName: string`
- `style: SampDialogStyle`

---

### `0B3C` SAMP_HAS_DIALOG_RESPONDED
Returns logical true if the last submitted SAMP Dialog is equal to the specified dialogid

**Class:** `SampClient.HasDialogResponded`
**Flags:** condition, static

**Input:**
- `dialogId: int`

**Output:**
- `buttonId: int (variable)`
- `listItemId: int (variable)`
- `inputTextBuffer: int (variable)`

**Details:**

* Passing a variable to ***buttonidstore*** will return the pressed button id to this variable. You can Pass a **NULL Pointer** *(buttonidstore = 0)* to indicate that you don't need this.
* Passing a variable to ***listitemidstore*** will return the id of the selected item of its list to this variable. You can Pass a **NULL Pointer** *(listitemidstore = 0)* to indicate that you don't need this.
* Passing a variable to ***inputtextwritetostringbuffer*** will write the input text as string into this variable. You can Pass a **NULL Pointer** *(inputtextwritetostringbuffer = 0)* to indicate that you don't need this.

---

### `0B47` SAMP_CLOSE_ACTIVE_DIALOG_WITH_BUTTON
Closes the active dialog by pressing the specified button programmatically

**Class:** `SampClient.CloseDialog`
**Flags:** condition, static

**Input:**
- `button: SampDialogButton`

**Details:**

* This command will send SampRpc.DialogResponse to the Server as well.
* Can be used as a condition which evaluates as true if the dialog is opened before being closed by this command.
* Most servers commonly interprets:
    * buttonid = 0 as cancel/no/reject
    * buttonid = 1 as submit/yes/accept

---

### `0B48` SAMP_GET_ACTIVE_DIALOG_SELECTED_LIST_ITEM
Returns the ID of the currently selected item on the list

**Class:** `SampClient.GetDialogSelectedItem`
**Flags:** condition, static

**Output:**
- `itemId: int (variable)`

**Details:**

Can be used as a condition which evaluates as true if a dialog is opened and has a list style attribute

---

### `0B49` SAMP_SELECT_ACTIVE_DIALOG_LIST_ITEM
Selects the id of an element in the dialog list

**Class:** `SampClient.SelectDialogItem`
**Flags:** condition, static

**Input:**
- `itemId: int`

**Details:**

Can be used as a condition which evaluates as true if the dialog is opened, has a list style attribute, and has that itemid

---

### `0B4A` SAMP_GET_ACTIVE_DIALOG_EDITBOX_TEXT
Stores the text from the input field of the active dialog to the buffer

**Class:** `SampClient.GetDialogEditboxText`
**Flags:** condition, static

**Output:**
- `buffer: string (variable)`

**Details:**

Can be used as a condition which evaluates as true if a dialog is opened and has an edit style attribute

---

### `0B4B` SAMP_SET_ACTIVE_DIALOG_EDITBOX_TEXT
Sets the text of the edit field of the active dialog's box

**Class:** `SampClient.SetDialogEditboxText`
**Flags:** condition, static

**Input:**
- `text: string`

**Details:**

Can be used as a condition which evaluates as true if a dialog is opened and has an edit style attribute

---

### `0B4C` SAMP_IS_DIALOG_ACTIVE
Evaluates as logical true if the specified dialog with id is currently visible

**Class:** `SampClient.IsDialogActive`
**Flags:** condition, static

**Input:**
- `id: int`

---

### `0B4D` SAMP_GET_DIALOG_STYLE
Returns the style of the active dialog. If the dialog is not opened, returns the style of the last opened dialog instead

**Class:** `SampClient.GetDialogStyle`
**Flags:** condition, static

**Output:**
- `style: SampDialogStyle (variable)`

**Details:**

Can be used as a condition that evaluates as false if no dialog has been opened since the start of the game

---

### `0B4E` SAMP_GET_DIALOG_ID
Returns the ID of the active dialog. If the dialog is not opened, returns the ID of the last opened dialog instead

**Class:** `SampClient.GetDialogId`
**Flags:** condition, static

**Output:**
- `id: int (variable)`

**Details:**

Can be used as a condition that evaluates as false if no dialog has been opened since the start of the game

---

### `0B4F` SAMP_GET_GAMESTATE
Returns our connection status towards the server

**Class:** `SampClient.GetGamestate`
**Flags:** static

**Output:**
- `statusId: SampGameState (variable)`

---

### `0B50` SAMP_GET_OBJECT_BY_ID
Returns the handle of an object using its SAMP ID

**Class:** `SampClient.GetObject`
**Flags:** condition, static

**Input:**
- `id: int`

**Output:**
- `handle: Object (variable)`

**Details:**

Can be used as a condition which evaluates as true if the object is streamed

---

### `0B51` SAMP_GET_PICKUP_BY_ID
Returns the handle of a pickup using its SAMP ID

**Class:** `SampClient.GetPickup`
**Flags:** condition, static

**Input:**
- `id: int`

**Output:**
- `handle: Pickup (variable)`

**Details:**

Can be used as a condition which evaluates as true if the pickup is streamed

---

### `0B54` SAMP_GET_DIALOG_LIST_ITEMS_COUNT
Returns the total number of items found on the active dialog's list. If the dialog is not opened, the last opened dialog is used instead

**Class:** `SampClient.GetDialogItemsCount`
**Flags:** condition, static

**Output:**
- `itemsCount: int (variable)`

**Details:**

Can be used as a condition which evaluates as false if, the dialog does not have a list style attribute, or no dialog has been opened since the start of the game

---

### `0B58` SAMP_GET_ANIMATION_NAME
Stores the filename and animname of the animation using its SAMP ID

**Class:** `SampClient.GetAnimName`
**Flags:** condition, static

**Input:**
- `animId: int`

**Output:**
- `fileName: int (variable)`
- `animName: int (variable)`

**Details:**

Can be used as a condition which evaluates as true if animid is valid

---

### `0B59` SAMP_GET_ANIMATION_ID
Returns the Animation SAMP ID using its name and the file it was loaded from

**Class:** `SampClient.GetAnimId`
**Flags:** condition, static

**Input:**
- `animName: string`
- `fileName: string`

**Output:**
- `animId: int (variable)`

**Details:**

Can be used as a condition that returns false if the provided filename and animname has no corresponding animid

---

### `0B5B` SAMP_GET_DIALOG_LIST_ITEM_TEXT
Stores the text of an item with specific id from the active dialog's list, to buffer. If the dialog is not opened, the last opened dialog is evaluated instead

**Class:** `SampClient.GetDialogItemText`
**Flags:** condition, static

**Input:**
- `itemId: int`

**Output:**
- `buffer: string (variable)`

**Details:**

Can be used as a condition which evaluates as true if the evaluated dialog has the itemid.

---

### `0B5D` SAMP_SET_CURSOR_VISIBILITY
Sets the visibility status of mouse cursor

**Class:** `SampClient.SetCursorVisibility`
**Flags:** static

**Input:**
- `isVisible: bool`

---

### `0B7A` SAMP_GET_RAKCLIENT_INTERFACE
Returns a pointer to a RakClientInterface object

**Class:** `SampClient.GetRakClientInterface`
**Flags:** static

**Output:**
- `pointer: int (variable)`

---

### `0B7B` SAMP_GET_RAKPEER
Returns a pointer to RakPeer

**Class:** `SampClient.GetRakPeer`
**Flags:** static

**Output:**
- `pointer: int (variable)`

---

### `0B7C` SAMP_GET_RAKCLIENT_FUNC_BY_INDEX
Returns the address of the RakClientInterface virtual method table function by index

**Class:** `SampClient.GetRakClientFunc`
**Flags:** static

**Input:**
- `index: int`

**Output:**
- `address: int (variable)`

---

### `0B7D` SAMP_GET_RPC_FUNC_BY_INDEX
Returns the RPC callback address by index

**Class:** `SampClient.GetRpcFunc`
**Flags:** condition, static

**Input:**
- `index: int`

**Output:**
- `address: int (variable)`

---

### `0B7E` SAMP_GET_RPC_NODE_BY_INDEX
Returns a pointer to the RPC structure at index

**Class:** `SampClient.GetRpcNode`
**Flags:** condition, static

**Input:**
- `index: int`

**Output:**
- `address: int (variable)`

---

### `0B7F` SAMP_GET_INFO_POINTER
Returns a pointer to a SampInfo structure

**Class:** `SampClient.GetInfoPtr`
**Flags:** static

**Output:**
- `address: int (variable)`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stSAMP** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L181)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L184)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L184)

---

### `0B8C` SAMP_IS_CURSOR_ACTIVE
Checks if the mouse cursor were both visible and movable

**Class:** `SampClient.IsCursorActive`
**Flags:** condition, static

---

### `0B8D` SAMP_SET_CURSOR_MODE
Sets the cursor mode

**Class:** `SampClient.SetCursorMode`
**Flags:** static

**Input:**
- `mode: SampCursorMode`

---

### `0B8E` SAMP_GET_CURSOR_MODE
Returns the current mouse cursor mode

**Class:** `SampClient.GetCursorMode`
**Flags:** condition, static

**Output:**
- `mode: SampCursorMode (variable)`

---

### `0BAC` SAMP_GET_SERVER_SETTINGS_POINTER
Returns the pointer to server settings structure

**Class:** `SampClient.GetServerSettingsPtr`
**Flags:** static

**Output:**
- `address: int (variable)`

---

### `0BAD` SAMP_GET_POOLS_POINTER
Returns the pointer to samp pools structure

**Class:** `SampClient.GetPoolsPtr`
**Flags:** static

**Output:**
- `address: int (variable)`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stSAMPPools** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L168)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L171)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L171)

---

### `0BAE` SAMP_GET_CHAT_INFO_POINTER
Returns the pointer to samp chat information structure

**Class:** `SampClient.GetChatInfoPtr`
**Flags:** static

**Output:**
- `address: int (variable)`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stChatInfo** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L798)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L818)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L817)

---

### `0BAF` SAMP_GET_CHAT_INPUT_INFO_POINTER
Returns the pointer to samp chat input field structure

**Class:** `SampClient.GetChatInfoPtr`
**Flags:** static

**Output:**
- `address: int (variable)`

---

### `0BB0` SAMP_GET_DIALOG_INFO_POINTER
Returns the pointer to samp dialog structure

**Class:** `SampClient.GetDialogInfoPtr`
**Flags:** static

**Output:**
- `address: int (variable)`

---

### `0BB1` SAMP_GET_KILL_INFO_POINTER
Returns the pointer to samp kill list structure

**Class:** `SampClient.GetKillInfoPtr`
**Flags:** static

**Output:**
- `address: int (variable)`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stKillInfo** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L875)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L895)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L894)

---

### `0BB2` SAMP_GET_MISC_INFO_POINTER
Returns the pointer to a structure of various samp miscellaneous data

**Class:** `SampClient.GetMiscInfoPtr`
**Flags:** static

**Output:**
- `address: int (variable)`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stSAMPPools** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L168)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L171)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L171)

---

### `0BB3` SAMP_GET_TEXTDRAW_POOL_POINTER
Returns the pointer to samp textdraw pool structure

**Class:** `SampClient.GetTextDrawPoolPtr`
**Flags:** static

**Output:**
- `address: int (variable)`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stTextdrawPool** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L333)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L340)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L340)

---

### `0BB4` SAMP_GET_OBJECT_POOL_POINTER
Returns the pointer to samp object pool structure

**Class:** `SampClient.GetObjectPoolPtr`
**Flags:** static

**Output:**
- `address: int (variable)`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stObjectPool** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L738)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L758)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L757)

---

### `0BB5` SAMP_GET_GANGZONE_POOL_POINTER
Returns a pointer to the pool of samp allocated territories (gang territories)

**Class:** `SampClient.GetGangZonePoolPtr`
**Flags:** static

**Output:**
- `address: int (variable)`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stGangzonePool** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L752)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L772)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L771)

---

### `0BB6` SAMP_GET_TEXTLABEL_POOL_POINTER
Returns the pointer to 3D text pool structure

**Class:** `SampClient.GetTextLabelPoolPtr`
**Flags:** static

**Output:**
- `address: int (variable)`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stTextLabelPool** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L769)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L789)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L788)

---

### `0BB7` SAMP_GET_PLAYER_POOL_POINTER
Returns the pointer to player pool structure

**Class:** `SampClient.GetPlayerPoolPtr`
**Flags:** static

**Output:**
- `address: int (variable)`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stPlayerPool** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L358)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L365)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L365)

---

### `0BB8` SAMP_GET_CAR_POOL_POINTER
Returns the pointer to samp car pool structure

**Class:** `SampClient.GetCarPoolPtr`
**Flags:** static

**Output:**
- `address: int (variable)`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stVehiclePool** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L691)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L711)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L710)

---

### `0BB9` SAMP_GET_PICKUP_POOL_POINTER
Returns the pointer to samp pickup pool structure

**Class:** `SampClient.GetPickupPoolPtr`
**Flags:** static

**Output:**
- `address: int (variable)`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stPickupPool** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L348)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L355)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L355)

---

### `0BD5` SAMP_IS_SCOREBOARD_VISIBLE
Evaluates as logical true if the scoreboard is visible

**Class:** `SampClient.IsScoreboardVisible`
**Flags:** condition, static

---

### `0BD6` SAMP_SET_SCOREBOARD_VISIBILITY
Sets the visibility of the scoreboard

**Class:** `SampClient.SetScoreboardVisibility`
**Flags:** static

**Input:**
- `isVisible: bool`

---

### `0BD7` SAMP_GET_DIALOG_CONTENT
Returns the content of the active dialog to buffer. If the dialog is not opened, the last opened dialog is evaluated instead

**Class:** `SampClient.GetDialogContent`
**Flags:** static

**Input:**
- `buffer: string`

---

### `0BD8` SAMP_GET_DIALOG_TITLE
Stores the title of the active dialog to buffer. If the dialog is not opened, the last opened dialog is evaluated instead

**Class:** `SampClient.GetDialogTitle`
**Flags:** static

**Input:**
- `buffer: string`

---

### `0BD9` SAMP_SET_ACTIVE_DIALOG_ENVIRONMENT
Sets whether interactions with the active dialog would sync to the server(server-sided dialog) or not(client-sided dialog)

**Class:** `SampClient.SetDialogEnv`
**Flags:** static

**Input:**
- `isClientSide: bool`

---

### `0BDA` SAMP_IS_ACTIVE_DIALOG_CLIENTSIDE
Evaluates as logical true if the active dialog is has a client side attribute

**Class:** `SampClient.IsDialogClientSide`
**Flags:** condition, static

---

### `0C8A` SAMP_GET_MAX_PLAYER_ID
Returns the maximum player ID currently streamed if streamedOnly = true. Else, returns the maximum player ID allowed in the server

**Class:** `SampClient.MaxPlayerId`
**Flags:** condition, static

**Input:**
- `streamedOnly: bool`

**Output:**
- `maxPlayerId: int (variable)`

---

### `0C8B` SAMP_GET_PLAYER_COUNT
Returns the number of players that are currently streamed if streamedOnly = true. Else, returns the number of players allowed in the server

**Class:** `SampClient.GetPlayerCount`
**Flags:** static

**Input:**
- `streamedOnly: bool`

**Output:**
- `playerCount: int (variable)`

---

### SampLocalChatCmd

### `0B34` SAMP_HOOK_CHAT_COMMAND_AS_LOCAL
Registers a callback hooked from a client sided chat command

**Class:** `SampLocalChatCmd.Hook`
**Flags:** condition, static

**Input:**
- `chatCommand: string`
- `callback: label`

**Details:**

* When a callback is hooked on a chatcommand, then everytime we type this chatcommand, it will not be sent to the server. To reverse this behavior, execute **SAMP_UNHOOK_LOCAL_CHAT_COMMAND** for the affected chatcommand.
* The chat command trigger text will be **/\<chatcommand\>** . For example:
  * if chatcommand = **"killme"** then you need to type **/killme** in chat
  * if chatcommand = **"/killme"** then you need to type **//killme** in chat
* You must pass an offset label as the callback parameter. Like For example, **@ChatCallback_GiveWeapon**
* The callback label must contain the callback's body.
* Construct the callback's flow of execution with caution.
  * Like subroutines, callbacks uses the variable space of the script's main thread.
  * Callbacks have higher priority than the custom script's main thread. Meaning, eveytime the script encounters the **WAIT** command at the main thread, the script will execute all callbacks first(if interrupt flag was fired by a callback), then continues to execute the main thread's commands after where the **WAIT** command was encountered.
  * Avoid executing too much commands inside the callback. Doing so would lead to undersirable script behavior, like failing to detect interrupts from other registered callbacks or event handlers.
  * **WAIT** command inside a Callback **WILL NOT WORK!** Because callbacks are designed to finish as soon as possible.
  * All callbacks hooked by this command must use **SF_COMMAND_RETURN** command as returning statement, indicating the end of callback.

---

### `0B63` SAMP_UNHOOK_LOCAL_CHAT_COMMAND
Removes all callbacks hooked from a chatCommand created by SAMP_REGISTER_CLIENTSIDE_COMMAND, suppressing all its callback's operation 

**Class:** `SampLocalChatCmd.Unhook`
**Flags:** condition, static

**Input:**
- `chatCommand: string`

**Details:**

By default, our inputted chatcommands are received by the server. But when a callback is hooked on a chatcommand, then that chatcommand will not be sent to the server. This poses a problem if that chatcommand has server sided meaning. So Calling this command will allow the server to receive that chatcommand once again.

---

### `0C7F` SAMP_SET_LOCAL_CHAT_COMMAND_DESCRIPTION
Sets the description for the local command

**Class:** `SampLocalChatCmd.SetDescription`
**Flags:** static

**Input:**
- `chatCommand: string`
- `decription: string`

---

### `0C90` SAMP_IS_CHAT_COMMAND_HOOKED
Evaluates as logical true if the specified command is localized by a callback hook

**Class:** `SampLocalChatCmd.IsHooked`
**Flags:** condition, static

**Input:**
- `chatCommand: string`

---

### SampMyPlayer

### `0AF6` SAMP_FORCE_SPAWN_MY_PLAYER
Sends SampRpc.Spawn to SAMP Server. Teleports our character to spawn as well

**Class:** `SampMyPlayer.ForceSpawn`
**Flags:** static

---

### `0B29` SAMP_SET_MY_NICKNAME
Changes our nickname (visually)

**Class:** `SampMyPlayer.SetNickname`
**Flags:** static

**Input:**
- `nickname: string`

**Details:**

This new nickname will only be visible at our client, meaning that the server is unaffected and the remote players will not see our nickname changed

---

### `0B61` SAMP_IS_MY_PLAYER_SPAWNED
Evaluates as logical true if our player has been spawned already

**Class:** `SampMyPlayer.IsSpawned`
**Flags:** condition, static

---

### SampPlayer

### `0B20` SAMP_GET_PLAYER_CHAR_BY_ID
Returns the character handle using the Player ID. Returns -1 if the player is not in the stream zone

**Class:** `SampPlayer.GetChar`

**Input:**
- `self: SampPlayer`

**Output:**
- `handle: Char (variable)`

---

### `0B23` SAMP_IS_REMOTE_PLAYER_CONNECTED
Returns true if REMOTE Player with the given ID is connected

**Class:** `SampPlayer.IsRemotelyConnected`
**Flags:** condition

**Input:**
- `self: SampPlayer`

**Details:**

Our LOCAL Player is not a REMOTE Player. So Passing the ID of our local player to this command will return false

---

### `0B24` SAMP_GET_PLAYER_POINTER
Returns the player's samp structure. Returns 0 (NULL Pointer) if player isn't connected

**Class:** `SampPlayer.GetPtr`

**Input:**
- `self: SampPlayer`

**Output:**
- `address: int (variable)`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* This command returns **stLocalPlayer** structure pointer if the specified player is our **Local Player**. See **stLocalPlayer** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L548)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L575)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L574)
* This command returns **stRemotePlayerData** structure pointer if the specified player ID is a **Remote Player** (the other players). See **stRemotePlayerData** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L609)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L629)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L628)

---

### `0B25` SAMP_GET_PLAYER_HEALTH
Returns the amount of health the specified player has

**Class:** `SampPlayer.GetHealth`

**Input:**
- `self: SampPlayer`

**Output:**
- `health: int (variable)`

**Details:**

Character Health is Different from Player Health. It is possible for both of them to have different values. But the server uses the Player Health value

---

### `0B26` SAMP_GET_PLAYER_ARMOR
Returns the amount of armor the specified player has

**Class:** `SampPlayer.GetArmor`

**Input:**
- `self: SampPlayer`

**Output:**
- `armor: int (variable)`

**Details:**

Character Armor is Different from Player Armor. In SAMP, It is possible for both of them to have different values. But the server uses the Player Armor value

---

### `0B2A` SAMP_GET_PLAYER_PING
Returns the ping of the specified player with ID

**Class:** `SampPlayer.GetPing`

**Input:**
- `self: SampPlayer`

**Output:**
- `ping: int (variable)`

---

### `0B2F` SAMP_GET_STREAMED_OUT_PLAYER_COORDS
Returns the 3D Coordinates of a player who is outside the stream zone, if the server allows it

**Class:** `SampPlayer.GetStreamedOutCoords`

**Input:**
- `self: SampPlayer`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

**Details:**

The returned coordinates of this command have some discrepancies compared to the correct coordinates because the server rounds down the streamed-out coordinate values sent to our client for data compression purposes.

---

### `0B36` SAMP_GET_PLAYER_NICKNAME
Returns a pointer to the nickname of the specified player

**Class:** `SampPlayer.GetName`

**Input:**
- `self: SampPlayer`

**Output:**
- `nickname: int (variable)`

---

### `0B37` SAMP_GET_PLAYER_COLOR
Returns the color of the specified player in 0xAARRGGBB format

**Class:** `SampPlayer.GetColor`

**Input:**
- `self: SampPlayer`

**Output:**
- `color: int (variable)`

---

### `0B57` SAMP_GET_PLAYER_ANIMATION
Returns the SAMP ID of the animation currently being played by the specified player

**Class:** `SampPlayer.GetAnim`
**Flags:** condition

**Input:**
- `self: SampPlayer`

**Output:**
- `animId: int (variable)`

**Details:**

Can be used as a condition which evaluates as true if the player is streamed

---

### `0B5C` SAMP_IS_PLAYER_PAUSED
Evaluates as logical true if the specified player is in paused state (or AFK)

**Class:** `SampPlayer.IsPaused`
**Flags:** condition

**Input:**
- `self: SampPlayer`

---

### `0B62` SAMP_GET_PLAYER_SPECIAL_ACTION
Returns the special action ID of the specified player

**Class:** `SampPlayer.GetSpecialAction`
**Flags:** condition

**Input:**
- `self: SampPlayer`

**Output:**
- `specialActionId: SampSpecialAction (variable)`

**Details:**

Can be used as a condition which evaluates as true if the specified player exists.

---

### `0B64` SAMP_IS_PLAYER_NPC
Checks if the specified player is an NPC

**Class:** `SampPlayer.IsNpc`
**Flags:** condition

**Input:**
- `self: SampPlayer`

---

### `0B65` SAMP_GET_PLAYER_SCORE
Returns the current score of the specified player

**Class:** `SampPlayer.GetScore`
**Flags:** condition

**Input:**
- `self: SampPlayer`

**Output:**
- `score: int (variable)`

**Details:**

Can be used as a condition which evaluates as true if the specified player exists.

---

### `0BBA` SAMP_STORE_PLAYER_ONFOOT_DATA
Stores the current player's onFootData structure to the buffer

**Class:** `SampPlayer.StoreOnFootData`
**Flags:** condition

**Input:**
- `self: SampPlayer`

**Output:**
- `buffer: int (variable)`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* The memory size of the buffer must be greater than or equal to the size of **stOnFootData** structure
* See **stOnFootData** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L392)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L400)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L399)

---

### `0BBB` SAMP_STORE_PLAYER_DRIVING_DATA
Stores the player's current inCarData structure to the buffer

**Class:** `SampPlayer.StoreDrivingData`
**Flags:** condition

**Input:**
- `self: SampPlayer`

**Output:**
- `buffer: int (variable)`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* The memory size of the buffer must be greater than or equal to the size of **stInCarData** structure
* See **stInCarData** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L414)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L422)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L421)

---

### `0BBC` SAMP_STORE_PLAYER_PASSENGER_DATA
Stores the current passengerData structure of the player to the buffer

**Class:** `SampPlayer.StorePassengerData`
**Flags:** condition

**Input:**
- `self: SampPlayer`

**Output:**
- `buffer: int (variable)`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* The memory size of the buffer must be greater than or equal to the size of **stPassengerData** structure
* See **stPassengerData** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L461)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L470)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L469)

---

### `0BBD` SAMP_STORE_PLAYER_TRAILER_DATA
Stores the player's current trailerData structure to the buffer

**Class:** `SampPlayer.StoreTrailerData`
**Flags:** condition

**Input:**
- `self: SampPlayer`

**Output:**
- `buffer: int (variable)`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* The memory size of the buffer must be greater than or equal to the size of **stTrailerData** structure
* See **stTrailerData** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L452)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L461)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L460)

---

### `0BBE` SAMP_STORE_PLAYER_AIM_DATA
Stores the specified player's aimData structure to the buffer

**Class:** `SampPlayer.StoreAimData`
**Flags:** condition

**Input:**
- `self: SampPlayer`

**Output:**
- `buffer: int (variable)`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* The memory size of the buffer must be greater than or equal to the size of **stAimData** structure
* See **stAimData** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L441)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L450)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L449)

---

### SampRaknet

### `0AF9` SAMP_SEND_CHAT_MESSAGE
Sends SampRpc.Chat containing the message or command to the server

**Class:** `SampRaknet.SendRpcChat`
**Flags:** static

**Input:**
- `format: string`
- `args: arguments`

**Details:**

Can process formatted string.

Unlike SAMP_PROCESS_CHAT_INPUT, this command will not processed by SAMPFUNCS callbacks such as RakNet Hooks and SAMP Chat Hooks. Directly sending the SampRpc.Chat to server

---

### `0AFB` SAMP_SEND_REQUEST_CLASS
Sends SampRpc.RequestClass to Server

**Class:** `SampRaknet.SendRpcRequestClass`
**Flags:** static

**Input:**
- `classId: int`

---

### `0AFC` SAMP_SEND_SCM_EVENT
Sends SampRpc.ScmEvent information about car modification to the server

**Class:** `SampRaknet.SendRpcScmEvent`
**Flags:** static

**Input:**
- `carId: int`
- `type: SampScmEvent`
- `param1: int`
- `param2: int`

**Details:**

Types:
* SCMEVENT_PAINTJOB = 1 (paint jobs)
* SCMEVENT_UPGRADE = 2 (upgrades)
* SCMEVENT_COLOR = 3 (color)
* SCMEVENT_MODSHOPENTEREXIT = 4 (exit/entrance to the garage for buying modifications)

---

### `0AFE` SAMP_SEND_DEATH_BY_PLAYER
Sends SampRpc.Death to Server without our character actually dying

**Class:** `SampRaknet.SendRpcDeath`
**Flags:** static

**Input:**
- `playerId: int`
- `weaponId: WeaponType`

**Details:**

* This will tell the server that our local player got killed by the specified player using a specific weapon.
* Set PlayerID = 0xFFFF to indicate that our local player died by natural means (falling, drowned/toxicated).
* This command will not actually kill our local character (Fake RPC). Use Separate command to do so, like:
    * TASK_DIE
    * EXPLODE_CHAR_HEAD

---

### `0B28` SAMP_SEND_DISCONNECTED
Sends SampRpc.ScrServerQuit to the server without actually disconnecting our client to the server

**Class:** `SampRaknet.SendRpcDisconnected`
**Flags:** static

**Input:**
- `id: SampDisconnectReason`

**Details:**

Servers does not normally receive a disconnection RPC with reason = SampDisconnectReason.TimeoutOrCrashed

---

### `0B30` SAMP_SEND_ENTER_CAR
Sends SampRpc.EnterCar to Server

**Class:** `SampRaknet.SendRpcEnterCar`
**Flags:** static

**Input:**
- `carId: int`
- `isPassenger: bool`

**Details:**

This command does not instruct our character to actually enter the car(Fake RPC). Execute a separate command to do so, like:
* TASK_ENTER_CAR_AS_DRIVER
* TASK_ENTER_CAR_AS_PASSENGER

---

### `0B31` SAMP_SEND_EXIT_CAR
Sends SampRpc.ExitCar to Server

**Class:** `SampRaknet.SendRpcExitCar`
**Flags:** static

**Input:**
- `carId: int`

**Details:**

This opcode does not instruct our character to actually exit the car(Fake RPC). Execute a separate command to do so, like:
* TASK_LEAVE_CAR
* TASK_LEAVE_ANY_CAR
* TASK_LEAVE_CAR_AND_FLEE
* SET_CHAR_GET_OUT_UPSIDE_DOWN_CAR

---

### `0B32` SAMP_SEND_SPAWN
Sends a SampRpc.Spawn to SAMP Server without spawning our character

**Class:** `SampRaknet.SendRpcSpawn`
**Flags:** static

**Details:**

* Unlike SAMP_FORCE_SPAWN_MY_PLAYER command, this command does not actually teleport our Player Character to Spawn(Fake RPC).
* Fact: Our client naturally sends this RPC, 2 seconds before our player spawns automatically.

---

### `0B33` SAMP_SEND_DAMAGE_CAR
Sends a SampRpc.DamageCar to the Server

**Class:** `SampRaknet.SendRpcDamageCar`
**Flags:** static

**Input:**
- `carId: int`
- `bodyFlags: int`
- `doorFlags: int`
- `lightFlags: int`
- `wheelFlags: int`

**Details:**

* This command updates the server about the component damage flags of a specified car, but this does not mean that this car has the actual damage(Fake RPC).
* Damage Flags are bitfields. Where for each bitfield, 0 = functional, 1 = damaged.

---

### `0B38` SAMP_CONNECT
Connects to the specified samp server information

**Class:** `SampRaknet.Connect`
**Flags:** static

**Input:**
- `serverIp: string`
- `port: int`

**Details:**

* Our client will force disconnect to the currently connected server. 
* You can use domain name instead of ip address

---

### `0BBF` SAMP_SEND_RCON_COMMAND
Sends an RCON command to the server

**Class:** `SampRaknet.SendRpcRconCmd`
**Flags:** static

**Input:**
- `command: string`

---

### `0BC0` SAMP_SEND_ONFOOT_DATA
Sends SampPacket.OnFootSync containing stOnFootData payload to the server

**Class:** `SampRaknet.SendPktOnFootData`
**Flags:** static

**Input:**
- `payloadPointer: int`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stOnFootData** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L392)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L400)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L399)

---

### `0BC1` SAMP_SEND_DRIVING_DATA
Sends SampPacket.DrivingSync containing stInCarData payload to the server

**Class:** `SampRaknet.SendPktDrivingData`
**Flags:** static

**Input:**
- `payloadPointer: int`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stInCarData** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L414)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L422)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L421)

---

### `0BC2` SAMP_SEND_PASSENGER_DATA
Sends SampPacket.PassengerSync containing stPassengerData payload to the server

**Class:** `SampRaknet.SendPktPassengerData`
**Flags:** static

**Input:**
- `payloadPointer: int`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stPassengerData** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L461)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L470)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L469)

---

### `0BC3` SAMP_SEND_AIM_DATA
Sends SampPacket.AimSync containing stAimData payload to the server 

**Class:** `SampRaknet.SendPktAimData`
**Flags:** static

**Input:**
- `payloadPointer: int`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stAimData** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L441)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L450)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L449)

---

### `0BC4` SAMP_SEND_BULLET_DATA
Sends SampPacket.BulletSync containing stBulletData payload to the server

**Class:** `SampRaknet.SendPktBulletData`
**Flags:** static

**Input:**
- `payloadPointer: int`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stBulletData** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L513)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L520)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L519)

---

### `0BC5` SAMP_SEND_TRAILER_DATA
Sends SampPacket.TrailerSync containing stTrailerData payload to the server

**Class:** `SampRaknet.SendPktTrailerData`
**Flags:** static

**Input:**
- `payloadPointer: int`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stTrailerData** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L452)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L461)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L460)

---

### `0BC6` SAMP_SEND_UNOCCUPIEDCAR_DATA
Sends SampPacket.UnoccupiedCarSync containing stUnoccupiedData payload to the server

**Class:** `SampRaknet.SendPktUnoccupiedCarData`
**Flags:** static

**Input:**
- `payloadPointer: int`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stUnoccupiedData** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L501)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L508)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L507)

---

### `0BC7` SAMP_SEND_SPECTATOR_DATA
Sends SampPacket.SpectatorSync containing stSpectatorData  payload to the server

**Class:** `SampRaknet.SendPktSpectatorData`
**Flags:** static

**Input:**
- `payloadPointer: int`

**Details:**

* Different versions of SAMP have different Pointers and Structures.
* See **stSpectatorData** structure for:
    * [SAMP 0.3.7 R1](https://github.com/BlastHackNet/mod_sa/blob/master/src/samp.h#L523)
    * [SAMP 0.3.7 R5](https://github.com/BlastHackNet/mod_sa/blob/samp-037r5/src/samp.h#L530)
    * [SAMP 0.3DL](https://github.com/BlastHackNet/mod_sa/blob/samp-03dl/src/samp.h#L529)

---

### `0BC8` SAMP_SEND_CLICK_PLAYER
Sends SampRpc.ClickPlayer about double click on player (from Scoreboard for example)

**Class:** `SampRaknet.SendRpcClickPlayer`
**Flags:** static

**Input:**
- `playerId: int`
- `clickSourceId: int`

**Details:**

Call locations:
* CLICK_SOURCE_SCOREBOARD = 0

---

### `0BC9` SAMP_SEND_DIALOG_RESPONSE
Sends an SampRpc.DialogResponse to the server

**Class:** `SampRaknet.SendRpcDialogResponse`
**Flags:** static

**Input:**
- `dialogId: int`
- `whichButton: SampDialogButton`
- `itemId: int`
- `inputText: string`

**Details:**

Most servers commonly interprets:
* buttonid = 0 as cancel/no/reject
* buttonid = 1 as submit/yes/accept

---

### `0BCA` SAMP_SEND_CLICK_TEXTDRAW
Sends an SampRpc.ClickTextDraw to the server

**Class:** `SampRaknet.SendRpcClickTextDraw`
**Flags:** static

**Input:**
- `textDrawId: int`

---

### `0BCB` SAMP_SEND_GIVE_DAMAGE
Sends an SampRpc.GiveTakeDamage to the server about damage dealt by another player

**Class:** `SampRaknet.SendRpcGiveDamage`
**Flags:** static

**Input:**
- `playerId: int`
- `floatDamage: SampWeaponDamage`
- `weapon: WeaponType`
- `bodyPart: BodyPart`

---

### `0BCC` SAMP_SEND_TAKE_DAMAGE
Sends an SampRpc.GiveTakeDamage to the server about damage taken from another player

**Class:** `SampRaknet.SendRpcTakeDamage`
**Flags:** static

**Input:**
- `playerId: int`
- `floatDamage: SampWeaponDamage`
- `weapon: WeaponType`
- `bodyPart: SampBodyPart`

---

### `0BCD` SAMP_SEND_EDIT_OBJECT
Sends an SampRpc.EditObject about changing the structure of an object in its editing mode

**Class:** `SampRaknet.SendRpcEditObject`
**Flags:** static

**Input:**
- `isLocalObject: bool`
- `id: int`
- `response: SampEditObjectResponse`
- `coordX: float`
- `coordY: float`
- `coordZ: float`
- `pitch: float`
- `roll: float`
- `yaw: float`

---

### `0BCE` SAMP_SEND_EDIT_ATTACHED_OBJECT
Sends SampRpc.EditAttachedObject about a change to an attached object in object edit mode

**Class:** `SampRaknet.SendRpcEditAttachedObject`
**Flags:** static

**Input:**
- `response: SampEditObjectResponse`
- `index: int`
- `model: model_object`
- `pedBone: PedBone`
- `offsetX: float`
- `offsetY: float`
- `offsetZ: float`
- `pitch: float`
- `roll: float`
- `yaw: float`
- `scaleX: float`
- `scaleY: float`
- `scaleZ: float`

---

### `0BCF` SAMP_SEND_REQUEST_INTERIOR_CHANGE
Sends SampRpc.RequestInteriorChange

**Class:** `SampRaknet.SendRpcRequestInteriorChange`
**Flags:** static

**Input:**
- `id: int`

---

### `0BD0` SAMP_SEND_REQUEST_SPAWN
Sends SampRpc.RequestSpawn

**Class:** `SampRaknet.SendRpcRequestSpawn`
**Flags:** static

---

### `0BD1` SAMP_SEND_PICKED_UP_PICKUP
Sends SampRpc.PickedUpPickup to take a pickup

**Class:** `SampRaknet.SendRpcPickedupPickup`
**Flags:** static

**Input:**
- `id: int`

---

### `0BD2` SAMP_SEND_MENU_SELECT_ROW
Sends SampRpc.MenuSelect about selecting an item in a menu (GTA:SA menu)

**Class:** `SampRaknet.SendRpcMenuSelectRow`
**Flags:** static

**Input:**
- `elementId: int`

---

### `0BD3` SAMP_SEND_QUIT_MENU
Sends SampRpc.MenuQuit to tell the server we exited the menu (GTA:SA menu)

**Class:** `SampRaknet.SendRpcQuitMenu`
**Flags:** static

---

### `0BD4` SAMP_SEND_CAR_DESTROYED
Sends SampRpc.CarDestroyed about destruction of a specific car (exploded or drenched in water)

**Class:** `SampRaknet.SendRpcCarDestroyed`
**Flags:** static

**Input:**
- `id: int`

---

### `0BE0` SAMP_RAKNET_HOOK_RETURN
Returns the flow of control to RakNet and decides whether the currently intercepted data will be processed by RakNet or not

**Class:** `SampRaknet.Return`
**Flags:** static

**Input:**
- `processData: bool`

---

### `0BE1` SAMP_RAKNET_HOOK_OUTCOMING_RPC
Redirects all outgoing RPCs to the specified callback for subsequent processing before sending to the server

**Class:** `SampRaknet.HookRpcOut`
**Flags:** condition, static

**Input:**
- `callback: label`

**Details:**

* The callback will intercept RakNet's attempt to transmit RPC. This gives us the priviledge to either cancel RakNet's RPC transmission, or manipulate the RPC's data before being sent to the server.
* When a callback is hooked by this command, there is no command unhook it. You need to terminate the script were the callback label is found.
* You must pass an offset label to callbacklabel. Like For example, **@RPC_Out**
* Construct the callback's flow of execution with caution.
  * Like subroutines, callbacks uses the variable space of the script's main thread.
  * Callbacks have higher priority than the custom script's main thread. Meaning, eveytime the script encounters the **WAIT** command at the main thread, the script will execute all callbacks first(if interrupt flag was fired by a callback), then continues to execute the main thread's commands after where the **WAIT** command was encountered.
  * RakNet's functionality is temporarily stopped while a RakNet callback hook is executing. Meaning, all datas that were supposed to be transmitted/received during the callback's interruption will be wasted as if they were not transmitted/received in the first place. So Avoid executing too much work inside the callback. Doing so would lead to undersirable behavior.
  * **WAIT** command inside a Callback **WILL NOT WORK!** Because callbacks are designed to finish as soon as possible.
* All callbacks hooked by this command must use **RAKNET_HOOK_RETURN** command as returning statement, indicating the end of callback.
* Can be used as a condition which evaluates as true if the hook was successful.

---

### `0BE2` SAMP_RAKNET_HOOK_OUTCOMING_PACKET
Redirects all outgoing Packets to the specified callback for subsequent processing before sending to the server

**Class:** `SampRaknet.HookPacketOut`
**Flags:** condition, static

**Input:**
- `callback: label`

**Details:**

* The callback will intercept RakNet's attempt to transmit a Packet. This gives us the priviledge to either cancel RakNet's Packet transmission, or manipulate the Packet's data before being sent to the server.
* When a callback is hooked by this command, there is no command unhook it. You need to terminate the script were the callback label is found.
* You must pass an offset label to callbacklabel. Like For example, **@Packet_Out**
* Construct the callback's flow of execution with caution.
  * Like subroutines, callbacks uses the variable space of the script's main thread.
  * Callbacks have higher priority than the custom script's main thread. Meaning, eveytime the script encounters the **WAIT** command at the main thread, the script will execute all callbacks first(if interrupt flag was fired by a callback), then continues to execute the main thread's commands after where the **WAIT** command was encountered.
  * RakNet's functionality is temporarily stopped while a RakNet callback hook is executing. Meaning, all datas that were supposed to be transmitted/received during the callback's interruption will be wasted as if they were not transmitted/received in the first place. So Avoid executing too much work inside the callback. Doing so would lead to undersirable behavior.
  * **WAIT** command inside a Callback **WILL NOT WORK!** Because callbacks are designed to finish as soon as possible.
* All callbacks hooked by this command must use **RAKNET_HOOK_RETURN** command as returning statement, indicating the end of callback.
* Can be used as a condition which evaluates as true if the hook was successful.

---

### `0BE3` SAMP_RAKNET_HOOK_INCOMING_RPC
Redirects all incoming RPCs to the specified callback for subsequent processing before acceptance on the local client

**Class:** `SampRaknet.HookRpcIn`
**Flags:** condition, static

**Input:**
- `callback: label`

**Details:**

* The callback will intercept RakNet's attempt to store the received RPC. This gives us the priviledge to either block the received RakNet RPC, or manipulate the RPC's data before being stored in our client's samp structure.
* When a callback is hooked by this command, there is no command unhook it. You need to terminate the script were the callback label is found.
* You must pass an offset label to callbacklabel. Like For example, **@RPC_In**
* Construct the callback's flow of execution with caution.
  * Like subroutines, callbacks uses the variable space of the script's main thread.
  * Callbacks have higher priority than the custom script's main thread. Meaning, eveytime the script encounters the **WAIT** command at the main thread, the script will execute all callbacks first(if interrupt flag was fired by a callback), then continues to execute the main thread's commands after where the **WAIT** command was encountered.
  * RakNet's functionality is temporarily stopped while a RakNet callback hook is executing. Meaning, all datas that were supposed to be transmitted/received during the callback's interruption will be wasted as if they were not transmitted/received in the first place. So Avoid executing too much work inside the callback. Doing so would lead to undersirable behavior.
  * **WAIT** command inside a Callback **WILL NOT WORK!** Because callbacks are designed to finish as soon as possible.
* All callbacks hooked by this command must use **RAKNET_HOOK_RETURN** command as returning statement, indicating the end of callback.
* Can be used as a condition which evaluates as true if the hook was successful.

---

### `0BE4` SAMP_RAKNET_HOOK_INCOMING_PACKET
Redirects all incoming packets to the specified callback for subsequent processing before acceptance on the local client

**Class:** `SampRaknet.HookPacketIn`
**Flags:** condition, static

**Input:**
- `callback: label`

**Details:**

* The callback will intercept RakNet's attempt to store the received Packet. This gives us the priviledge to either block the received RakNet Packet, or manipulate the Packet's data before being stored in our client's samp structure.
* When a callback is hooked by this command, there is no command unhook it. You need to terminate the script were the callback label is found.
* You must pass an offset label to callbacklabel. Like For example, **@Packet_In**
* Construct the callback's flow of execution with caution.
  * Like subroutines, callbacks uses the variable space of the script's main thread.
  * Callbacks have higher priority than the custom script's main thread. Meaning, eveytime the script encounters the **WAIT** command at the main thread, the script will execute all callbacks first(if interrupt flag was fired by a callback), then continues to execute the main thread's commands after where the **WAIT** command was encountered.
  * RakNet's functionality is temporarily stopped while a RakNet callback hook is executing. Meaning, all datas that were supposed to be transmitted/received during the callback's interruption will be wasted as if they were not transmitted/received in the first place. So Avoid executing too much work inside the callback. Doing so would lead to undersirable behavior.
  * **WAIT** command inside a Callback **WILL NOT WORK!** Because callbacks are designed to finish as soon as possible.
* All callbacks hooked by this command must use **RAKNET_HOOK_RETURN** command as returning statement, indicating the end of callback.
* Can be used as a condition which evaluates as true if the hook was successful.

---

### `0BE5` SAMP_RAKNET_HOOK_GET_PARAM
Returns the hook parameter's value of the currently executing callback

**Class:** `SampRaknet.GetHookParam`
**Flags:** condition, static

**Input:**
- `type: SampRakNetHookParam`

**Output:**
- `value: any (variable)`

---

### `0BE6` SAMP_RAKNET_SET_HOOK_PARAM
Sets the hook parameter's value of the currently executing callback

**Class:** `SampRaknet.SetHookParam`
**Flags:** condition, static

**Input:**
- `type: SampRakNetHookParam`
- `value: any`

---

### `0BF8` SAMP_RAKNET_GET_RPC_NAME
Returns a pointer to the RPC ID's Name

**Class:** `SampRaknet.GetRpcName`
**Flags:** condition, static

**Input:**
- `id: int`

**Output:**
- `name: string (variable)`

---

### `0BF9` SAMP_RAKNET_GET_PACKET_NAME
Returns a pointer to the Packet ID's Name

**Class:** `SampRaknet.GetPacketName`
**Flags:** condition, static

**Input:**
- `id: int`

**Output:**
- `name: int (variable)`

---

### `0C81` SAMP_FORCE_DRIVING_SYNC
Sends SampPacket.DrivingSync to server about our character driving a car with ID

**Class:** `SampRaknet.ForceDrivingSync`
**Flags:** static

**Input:**
- `id: int`

---

### `0C82` SAMP_FORCE_UNOCCUPIED_SYNC
Sends SampPacket.UnoccupiedCarSync to server about a seatId of a car with carId being unoccupied

**Class:** `SampRaknet.ForceUnnocupiedSync`
**Flags:** static

**Input:**
- `carId: int`
- `seatId: SeatId`

---

### `0C83` SAMP_FORCE_ONFOOT_SYNC
Sends SampPacket.OnFootSync to server about our character being onfoot

**Class:** `SampRaknet.ForceOnfootSync`
**Flags:** static

---

### `0C84` SAMP_FORCE_AIM_SYNC
Sends SampPacket.AimSync containing our current aim data, to server

**Class:** `SampRaknet.ForceAimSync`
**Flags:** static

---

### `0C85` SAMP_FORCE_TRAILER_SYNC
Sends SampPacket.TrailerSync to server about a trailer with ID being attached to our player

**Class:** `SampRaknet.ForceTrailerSync`
**Flags:** static

**Input:**
- `id: int`

---

### `0C86` SAMP_FORCE_PASSENGER_SYNC
Sends SampPacket.PassengerSync to server about our character sitting at seatId of a car with carId

**Class:** `SampRaknet.ForcePassengerSync`
**Flags:** static

**Input:**
- `carId: int`
- `seatId: SeatId`

---

### `0C87` SAMP_FORCE_STATS_SYNC
Sends SampPacket.StatsUpdate containing our current money and drunk level, to server

**Class:** `SampRaknet.ForceStatsSync`
**Flags:** static

---

### `0C88` SAMP_FORCE_WEAPONS_SYNC
Sends SampPacket.WeaponsUpdate containing our character's current weapons, to server

**Class:** `SampRaknet.ForceWeaponsSync`
**Flags:** static

---

### SampTextDraw

### `0C48` SAMP_CREATE_TEXTDRAW
Modifies a textdraw with the specified parameters, creating it if it doesn't exist

**Class:** `SampTextDraw.Create`
**Flags:** condition, static

**Input:**
- `id: SampTextDraw`
- `text: string`
- `coordX: float`
- `coordY: float`

**Details:**

* TextDraws uses gamescreen coordinates:
    * coordX max value = 640.0
    * coordY max value = 448.0
* Can be used as a condition which evaluates as false if the textdraw ID is out of bounds

---

### `0C49` SAMP_SET_TEXTDRAW_BOX
Sets the parameters of the "box" (rectangle) of the text draw

**Class:** `SampTextDraw.SetBox`
**Flags:** condition

**Input:**
- `self: SampTextDraw`
- `isVisible: bool`
- `color: int`
- `width: float`
- `height: float`

**Details:**

* TextDraws uses gamescreen coordinates:
    * width  max value = 640.0
    * height max value = 448.0
* color must be in 0xAARRGGBB format where A = Alpha, R = Red, G = Green, B = Blue.

---

### `0C4A` SAMP_SET_TEXTDRAW_ALIGNMENT
Sets the alignment of the text in the textdraw

**Class:** `SampTextDraw.SetAlignment`
**Flags:** condition

**Input:**
- `self: SampTextDraw`
- `alignment: SampTextDrawAlignment`

---

### `0C4B` SAMP_SET_TEXTDRAW_PROPORTIONALITY
Sets whether the text scaling status is proportional to the text draw or not

**Class:** `SampTextDraw.SetProportionality`
**Flags:** condition

**Input:**
- `self: SampTextDraw`
- `isProportional: bool`

---

### `0C4C` SAMP_SET_TEXTDRAW_STYLE
Sets the text draw style

**Class:** `SampTextDraw.SetStyle`
**Flags:** condition

**Input:**
- `self: SampTextDraw`
- `style: int`

**Details:**

Styles:
* 1-4 - txd fonts (client)
* 5 - model

Other values may cause crash or not display.

---

### `0C4D` SAMP_SET_TEXTDRAW_SHADOW
Sets a shadow on the text draw

**Class:** `SampTextDraw.SetShadow`
**Flags:** condition

**Input:**
- `self: SampTextDraw`
- `tickness: int`
- `color: int`

**Details:**

* color must be in 0xAARRGGBB format where A = Alpha, R = Red, G = Green, B = Blue.

---

### `0C4E` SAMP_SET_TEXTDRAW_OUTLINE
Sets the outline of the text draw

**Class:** `SampTextDraw.SetOutline`
**Flags:** condition

**Input:**
- `self: SampTextDraw`
- `tickness: int`
- `color: int`

---

### `0C4F` SAMP_SET_TEXTDRAW_MODEL
Sets the model (object, auto) of the text draw for style 5

**Class:** `SampTextDraw.SetModel`
**Flags:** condition

**Input:**
- `self: SampTextDraw`
- `model: model_any`
- `rotPitch: float`
- `rotRoll: float`
- `rotYaw: float`
- `camZoomRange: float`
- `primaryColor: int`
- `secondaryColor: int`

**Details:**

* This command only changes the parameters of how the model is projected as a TextDraw Model and does not implicitly change the TextDraw's Style into a model style (style = 5).
* You will only see the effect of this command when the TextDraw Style = 5 . You can explicitly change the TextDraw Style by executing SAMP_SET_TEXTDRAW_STYLE command with style = 5.
* primaryColor and primaryColor must be in 0xAARRGGBB format where A = Alpha, R = Red, G = Green, B = Blue.

---

### `0C50` SAMP_SET_TEXTDRAW_TEXT
Sets the text of the textdraw

**Class:** `SampTextDraw.SetText`
**Flags:** condition

**Input:**
- `self: SampTextDraw`
- `text: string`

---

### `0C51` SAMP_SET_TEXTDRAW_COORDS
Sets the gamescreen coordinates of the textdraw

**Class:** `SampTextDraw.SetCoords`
**Flags:** condition

**Input:**
- `self: SampTextDraw`
- `coordX: float`
- `coordY: float`

**Details:**

* TextDraws uses gamescreen coordinates:
    * coordX max value = 640.0
    * coordY max value = 448.0
* Can be used as a condition which evaluates as false if the textdraw ID is out of bounds

---

### `0C52` SAMP_SET_TEXTDRAW_CHARACTER_PROPERTIES
Sets the size and color property of all characters in the textdraw

**Class:** `SampTextDraw.SetCharProps`
**Flags:** condition

**Input:**
- `self: SampTextDraw`
- `width: float`
- `height: float`
- `color: int`

**Details:**

* TextDraws uses gamescreen values:
    * width max value = 640.0
    * height max value = 448.0
* color must be in 0xAARRGGBB format where A = Alpha, R = Red, G = Green, B = Blue.
* Can be used as a condition which evaluates as false if the textdraw ID is out of bounds

---

### `0C53` SAMP_GET_TEXTDRAW_BOX
Returns the parameters of the "box" (rectangle) of the specified text draw

**Class:** `SampTextDraw.GetBox`
**Flags:** condition

**Input:**
- `self: SampTextDraw`

**Output:**
- `isVisible: bool (variable)`
- `color: int (variable)`
- `width: float (variable)`
- `height: float (variable)`

**Details:**

* TextDraws uses gamescreen coordinates:
    * width  max value = 640.0
    * height max value = 448.0
* color is in 0xAARRGGBB format where A = Alpha, R = Red, G = Green, B = Blue.

---

### `0C54` SAMP_GET_TEXTDRAW_ALIGNMENT
Sets the alignment of the text in the textdraw

**Class:** `SampTextDraw.GetAlignment`
**Flags:** condition

**Input:**
- `self: SampTextDraw`

**Output:**
- `alignment: SampTextDrawAlignment (variable)`

---

### `0C55` SAMP_GET_TEXTDRAW_PROPORTIONALITY
Returns true if the text scaling status is proportional to the text draw

**Class:** `SampTextDraw.GetProportionality`
**Flags:** condition

**Input:**
- `self: SampTextDraw`

**Output:**
- `isProportional: bool (variable)`

---

### `0C56` SAMP_GET_TEXTDRAW_STYLE
Returns the text draw style

**Class:** `SampTextDraw.GetStyle`
**Flags:** condition

**Input:**
- `self: SampTextDraw`

**Output:**
- `style: int (variable)`

**Details:**

Known Styles:
* 1-4 - txd fonts (client)
* 5 - model

---

### `0C57` SAMP_GET_TEXTDRAW_SHADOW
Returns the tickness and color property of the text draw's shadow

**Class:** `SampTextDraw.GetShadow`
**Flags:** condition

**Input:**
- `self: SampTextDraw`

**Output:**
- `tickness: int (variable)`
- `color: int (variable)`

**Details:**

color is in 0xAARRGGBB format where A = Alpha, R = Red, G = Green, B = Blue.

---

### `0C58` SAMP_GET_TEXTDRAW_OUTLINE
Returns the tickness and color property of the text draw's outline

**Class:** `SampTextDraw.GetOutline`
**Flags:** condition

**Input:**
- `self: SampTextDraw`

**Output:**
- `tickness: int (variable)`
- `color: int (variable)`

---

### `0C59` SAMP_GET_TEXTDRAW_MODEL
Returns the properties of the text draw as a model (style 5)

**Class:** `SampTextDraw.GetModel`
**Flags:** condition

**Input:**
- `self: SampTextDraw`

**Output:**
- `model: model_any (variable)`
- `rotPitch: float (variable)`
- `rotRoll: float (variable)`
- `rotYaw: float (variable)`
- `camZoomRange: float (variable)`
- `primaryColor: int (variable)`
- `secondaryColor: int (variable)`

**Details:**

primaryColor and primaryColor are in 0xAARRGGBB format where A = Alpha, R = Red, G = Green, B = Blue.

---

### `0C5A` SAMP_STORE_TEXTDRAW_TEXT
Stores the textdraw's text to stringBuffer

**Class:** `SampTextDraw.StoreText`
**Flags:** condition

**Input:**
- `self: SampTextDraw`

**Output:**
- `stringBuffer: string (variable)`

---

### `0C5B` SAMP_GET_TEXTDRAW_COORDS
Returns the gamescreen coordinates of the textdraw

**Class:** `SampTextDraw.GetCoords`
**Flags:** condition

**Input:**
- `self: SampTextDraw`

**Output:**
- `coordX: float (variable)`
- `coordY: float (variable)`

**Details:**

* TextDraws uses gamescreen coordinates:
    * coordX max value = 640.0
    * coordY max value = 448.0
* Can be used as a condition which evaluates as false if the textdraw ID is out of bounds

---

### `0C5C` SAMP_GET_TEXTDRAW_CHARACTER_PROPERTIES
Returns the size and color property of all characters in the textdraw

**Class:** `SampTextDraw.GetCharProps`
**Flags:** condition

**Input:**
- `self: SampTextDraw`

**Output:**
- `width: float (variable)`
- `height: float (variable)`
- `color: int (variable)`

**Details:**

* TextDraws uses gamescreen values:
    * width max value = 640.0
    * height max value = 448.0
* color is in 0xAARRGGBB format where A = Alpha, R = Red, G = Green, B = Blue.
* Can be used as a condition which evaluates as false if the textdraw ID is out of bounds

---

### `0C5D` SAMP_DOES_TEXTDRAW_EXIST
Evaluates as logical true if the specified textdraw exists

**Class:** `SampTextDraw.DoesExist`
**Flags:** condition

**Input:**
- `self: SampTextDraw`

---

### `0C5E` SAMP_DELETE_TEXTDRAW
Deletes the specified textdraw

**Class:** `SampTextDraw.Delete`
**Flags:** condition, destructor

**Input:**
- `self: SampTextDraw`

---

### SampTextLabel3D

### `0B44` SAMP_CREATE_3D_TEXT
Creates an artificial SAMP 3D text with the specified parameter attributes

**Class:** `SampTextLabel3D.Create`
**Flags:** condition, constructor

**Input:**
- `text: string`
- `color: int`
- `coordX: float`
- `coordY: float`
- `coordZ: float`
- `visibilityRadius: float`
- `showBehindWalls: bool`
- `attachedPlayerId: int`
- `attachedCarId: int`

**Output:**
- `handle: SampTextLabel3D (variable)`

**Details:**

* The returned handle is actually the 3DText's ID.
* Can be used as a condition which evaluated as true if the 3D Text has been created.
* color variable must be in 0xAARRGGBB format.
* If this 3D text is attached to something, then the coord variables (coordx, coordy, coordz) must be offsets relative to this entity's position.
* If this 3D text isn't attached to something, then the coord variables (coordx, coordy, coordz) must be the 3D coordinates at the world where we want it to appear.
* if this 3D text isn't attached to a player, then attachedplayerid must set to -1.
* if this 3D text isn't attached to a car, then attachedcarid must set to -1.

---

### `0B45` SAMP_DELETE_3D_TEXT
Destroys a 3D text using it's ID

**Class:** `SampTextLabel3D.Delete`
**Flags:** condition, destructor

**Input:**
- `self: SampTextLabel3D`

**Details:**

Can be used as a condition which evaluates as true if the 3D text existed before being destroyed

---

### `0B46` SAMP_DOES_3D_TEXT_EXIST
Returns logical true if the specified 3D text exists

**Class:** `SampTextLabel3D.DoesExist`
**Flags:** condition

**Input:**
- `self: SampTextLabel3D`

---

### `0C45` SAMP_CREATE_3D_TEXT_WITH_ID
Creates/overwrites a 3D text with the specified ID

**Class:** `SampTextLabel3D.CreateWithId`
**Flags:** static

**Input:**
- `idAsHandle: SampTextLabel3D`
- `text: int`
- `color: int`
- `coordX: float`
- `coordY: float`
- `coordZ: float`
- `visibilityRadius: float`
- `showBehindWalls: bool`
- `attachedPlayerId: int`
- `attachedCarId: int`

**Details:**

* The passed ID will act as the 3D Text's handle as well.
* If an existing 3D Text has the same ID, this command will just replace the informations of that 3D Text.
* color variable must be in 0xAARRGGBB format.
* If this 3D text is attached to something, then the coord variables (coordx, coordy, coordz) must be offsets relative to this entity's position.
* If this 3D text isn't attached to something, then the coord variables (coordx, coordy, coordz) must be the 3D coordinates at the world where we want it to appear.
* if this 3D text isn't attached to a player, then attachedplayerid must set to -1.
* if this 3D text isn't attached to a car, then attachedcarid must set to -1.

---

### `0C46` SAMP_GET_3D_TEXT_PARAMS
Returns all the informations about a SampTextLabel3D using its ID

**Class:** `SampTextLabel3D.GetParams`
**Flags:** condition

**Input:**
- `self: SampTextLabel3D`

**Output:**
- `text: string (variable)`
- `color: int (variable)`
- `coordX: float (variable)`
- `coordY: float (variable)`
- `coordZ: float (variable)`
- `visibilityRadius: float (variable)`
- `showBehindWalls: bool (variable)`
- `attachedPlayerId: int (variable)`
- `attachedCarId: int (variable)`

**Details:**

* Can be used as a condition which evaluated as true if the 3D Text exists.
* color variable must be in 0xAARRGGBB format.
* If this 3D text is attached to something, then the coord variables (coordx, coordy, coordz) must be offsets relative to this entity's position.
* If this 3D text isn't attached to something, then the coord variables (coordx, coordy, coordz) must be the 3D coordinates at the world where we want it to appear.
* if this 3D text isn't attached to a player, then attachedplayerid must set to -1.
* if this 3D text isn't attached to a car, then attachedcarid must set to -1.

---

### `0C47` SAMP_SET_3D_TEXT
Sets new text for 3D text

**Class:** `SampTextLabel3D.SetText`
**Flags:** condition

**Input:**
- `self: SampTextLabel3D`
- `text: string`

---

### Sf

### `0B35` SF_GET_PARAMS_OF_LAST_TRIGGERED_COMMAND
Returns a pointer to a string containing the parameters of the last command entered at console or SAMP Chat

**Class:** `Sf.GetCmdParams`
**Flags:** condition, static

**Output:**
- `pointer: int (variable)`

**Details:**

When used as a logical condition, this command is evaluated as true if parameters were provided after the command keyword

---

### `0B43` SF_COMMAND_RETURN
Marks the end of a command callback. Used as its returning statement

**Class:** `Sf.CmdRet`
**Flags:** static

---

### `0B55` SF_WORLD_COORDS_TO_WINDOW_SCREEN_COORDS
Converts 3D coordinates from the world into window screen coordinates (pixels)

**Class:** `Sf.From3DTo2DCoords`
**Flags:** condition, static

**Input:**
- `worldCoordX: float`
- `worldCoordY: float`
- `worldCoordZ: float`

**Output:**
- `screenCoordX: int (variable)`
- `screenCoordY: int (variable)`

**Details:**

screencoordx = 0 and screencoordy = 0 is found at top-left of the screen while the max coord values are found at the bottom-right of the screen

---

### `0B56` SF_SET_BUTTON
Sets the press status of a game (NOT keyboard) key

**Class:** `Sf.SetButton`
**Flags:** static

**Input:**
- `buttonId: Button`
- `behaviorValue: int`

**Details:**

* See the list of Button IDs at the SB Offline Documentation
* If the specified buttonid has only one action:
    * behaviorvalue **= 0** will release its corresponding action
    * behaviorvalue **= 255** will trigger its corresponding action
* If the specified buttonid has two actions:
    * behaviorvalue **= 0** will release its corresponding action
    * behaviorvalue **= -128** will trigger its first action
    * behaviorvalue **= 128** will trigger its second action

---

### `0B5A` SF_GET_SCREEN_RESOLUTION
Returns the current window screen resolution in pixels

**Class:** `Sf.GetScreenRes`
**Flags:** static

**Output:**
- `width: int (variable)`
- `height: int (variable)`

---

### `0B5E` SF_GET_CURSOR_COORD
Returns the mouse cursor's window screen coordinates in pixels

**Class:** `Sf.GetCursorCoord`
**Flags:** static

**Output:**
- `windowScreenCoordX: int (variable)`
- `windowScreenCoordY: int (variable)`

---

### `0B5F` SF_WINDOW_SCREEN_COORDS_TO_GAME_SCREEN_COORDS
Returns the GameScreen Coordinates counterpart of the specified WindowScreen Coordinates

**Class:** `Sf.FromWindowToGameScreenCoords`
**Flags:** static

**Input:**
- `windowScreenCoordX: int`
- `windowScreenCoordY: int`

**Output:**
- `gameScreenCoordX: float (variable)`
- `gameScreenCoordY: float (variable)`

**Details:**

* GameScreen Coordinates have fixed resolution:
    * gamescreencoordx (Width ) ranges from **0.0** to **640.0**
    * gamescreencoordy (Height) ranges from **0.0** to **448.0**
* GameScreen Coordinate System is useful if you want values that have predefined minimum and maximum values. It's easy to manipulate expressions this way.

---

### `0B60` SF_GAME_SCREEN_COORDS_TO_WINDOW_SCREEN_COORDS
Returns the WindowScreen Coordinates counterpart of the specified GameScreen Coordinates

**Class:** `Sf.FromGameToWindowScreenCoords`
**Flags:** static

**Input:**
- `gameScreenCoordX: float`
- `gameScreenCoordY: float`

**Output:**
- `windowScreenCoordX: int (variable)`
- `windowScreenCoordY: int (variable)`

**Details:**

* GameScreen Coordinates have fixed resolution:
    * gamescreencoordx (Width ) ranges from **0.0** to **640.0**
    * gamescreencoordy (Height) ranges from **0.0** to **448.0**

---

### `0B66` SF_HEX_TO_ARGB
Splits 0xAARRGGBB colorcode format into individial color channels

**Class:** `Sf.HexToArgb`
**Flags:** static

**Input:**
- `color: int`

**Output:**
- `alpha: int (variable)`
- `red: int (variable)`
- `green: int (variable)`
- `blue: int (variable)`

---

### `0B67` SF_ARGB_TO_HEX
mixes color channels into 0xAARRGGBB colorcode format

**Class:** `Sf.ArgbToHex`
**Flags:** static

**Input:**
- `alpha: int`
- `red: int`
- `green: int`
- `blue: int`

**Output:**
- `color: int (variable)`

---

### `0B8F` SF_WINDOW_SCREEN_COORDS_TO_WORLD_COORDS
Converts window screen coordinates (pixels) to world's 3D coordinates with the specified depth

**Class:** `Sf.From2DTo3DCoords`
**Flags:** static

**Input:**
- `screenCoordX: int`
- `screenCoordY: int`
- `depth: float`

**Output:**
- `worldCoordX: float (variable)`
- `worldCoordY: float (variable)`
- `worldCoordZ: float (variable)`

**Details:**

screencoordx = 0 and screencoordy = 0 is found at top-left of the screen while the max coord values are found at the bottom-right of the screen

---

### `0BDE` SF_PAUSE_SCRIPT
Sets the specified script's isActive parameter to 0

**Class:** `Sf.PauseScript`
**Flags:** static

**Input:**
- `scriptId: int`

---

### `0BDF` SF_RESUME_SCRIPT
Sets the specified script's isActive parameter to 1

**Class:** `Sf.ResumeScript`
**Flags:** static

**Input:**
- `scriptId: int`

---

### `0BFA` SF_PUSH_LOCAL_VARIABLES
Saves the values of all local variables from the currently executing script (Main Script or a Function) to a separate memory that can be recovered later on by SF_POP_LOCAL_VARIABLES

**Class:** `Sf.PushLocalVars`
**Flags:** static

---

### `0BFB` SF_POP_LOCAL_VARIABLES
Restores all previously saved local variables by SF_PUSH_LOCAL_VARIABLES to the local variables of the currently executing script (Main Script or a Function)

**Class:** `Sf.PopLocalVars`
**Flags:** static

---

### `0BFE` SF_GET_TICK_COUNT
Returns the OS's current uptime in milliseconds. Recommended substitute for TIMERA and TIMERB when requiring precise timing operations

**Class:** `Sf.GetTickCount`
**Flags:** static

**Output:**
- `tickCount: int (variable)`

---

### `0BFF` SF_PROCESS_LINE_OF_SIGHT
Checks for collisions using flags from the start of the vector to its end

**Class:** `Sf.ProcessLineOfSight`
**Flags:** condition, static

**Input:**
- `fromCoordX: float`
- `fromCoordY: float`
- `fromCoordZ: float`
- `toCoordX: float`
- `toCoordY: float`
- `toCoordZ: float`
- `checkBuildings: bool`
- `checkCars: bool`
- `checkChars: bool`
- `checkObjects: bool`
- `checkParticles: bool`
- `seeThrough: bool`
- `ignoreCameras: bool`

**Output:**
- `colPointPtr: any (variable)`
- `entityPtr: any (variable)`

---

### `0C00` SF_ABS
Returns the absolute value of a number (float or integer)

**Class:** `Sf.Abs`
**Flags:** static

**Input:**
- `number: any`

**Output:**
- `result: any (variable)`

---

### `0C01` SF_RADIANS_TO_DEGREES
Converts radians to degrees

**Class:** `Sf.RadToDeg`
**Flags:** static

**Input:**
- `radians: float`

**Output:**
- `degrees: float (variable)`

---

### `0C02` SF_DEGREES_TO_RADIANS
Converts degrees to radians

**Class:** `Sf.DegToRad`
**Flags:** static

**Input:**
- `degrees: float`

**Output:**
- `radians: float (variable)`

---

### `0C03` SF_SIN
Returns the sine of the specified radians

**Class:** `Sf.Sin`
**Flags:** static

**Input:**
- `radians: float`

**Output:**
- `ratio: float (variable)`

---

### `0C04` SF_ASIN
Returns the radian arcsine of the specified ratio

**Class:** `Sf.ASin`
**Flags:** static

**Input:**
- `ratio: float`

**Output:**
- `radians: float (variable)`

---

### `0C05` SF_COS
Returns the cosine of the specified radians

**Class:** `Sf.Cos`
**Flags:** static

**Input:**
- `radians: float`

**Output:**
- `ratio: float (variable)`

---

### `0C06` SF_ACOS
Returns the radian arccosine of the specified ratio

**Class:** `Sf.ACos`
**Flags:** static

**Input:**
- `ratio: float`

**Output:**
- `radians: float (variable)`

---

### `0C07` SF_TAN
Returns the tangent of the specified radians

**Class:** `Sf.Tan`
**Flags:** static

**Input:**
- `radians: float`

**Output:**
- `ratio: float (variable)`

---

### `0C08` SF_ATAN
Returns the radian arctangent of the specified ratio

**Class:** `Sf.ATan`
**Flags:** static

**Input:**
- `ratio: float`

**Output:**
- `radians: float (variable)`

---

### `0C09` SF_POW
Raises a number to the specified power

**Class:** `Sf.Pow`
**Flags:** static

**Input:**
- `coefficient: float`
- `exponent: float`

**Output:**
- `power: float (variable)`

---

### `0C0A` SF_CEIL
Returns the rounded-up result the specified number

**Class:** `Sf.Ceil`
**Flags:** static

**Input:**
- `number: float`

**Output:**
- `result: float (variable)`

---

### `0C0B` SF_FLOOR
Returns the rounded-down result the specified number

**Class:** `Sf.Floor`
**Flags:** static

**Input:**
- `number: float`

**Output:**
- `result: float (variable)`

---

### `0C0C` SF_READ_MEMORY_WITH_OFFSET
Reads the value with size from memory address with offset

**Class:** `Sf.ReadMemoryWithOffset`
**Flags:** condition, static

**Input:**
- `address: int`
- `offset: int`
- `size: int`

**Output:**
- `value: any (variable)`

---

### `0C0D` SF_WRITE_MEMORY_WITH_OFFSET
Writes the value with size to memory address with offset

**Class:** `Sf.WriteMemoryWithOffset`
**Flags:** condition, static

**Input:**
- `address: int`
- `offset: int`
- `size: int`
- `value: any`

---

### `0C0E` SF_READ_ELEMENT_OF_4BYTES_ARRAY
Reads the value from the specified element index of an array

**Class:** `Sf.ReadElementOf4BytesArray`
**Flags:** condition, static

**Input:**
- `array: int`
- `index: int`

**Output:**
- `value: any (variable)`

---

### `0C0F` SF_WRITE_ELEMENT_OF_4BYTES_ARRAY
Writes the value to the specified element index of an array

**Class:** `Sf.WriteElementOf4BytesArray`
**Flags:** condition, static

**Input:**
- `array: int`
- `index: int`
- `value: any`

---

### `0C10` SF_MEMCPY
Copies a memory block with size from source address to destination address

**Class:** `Sf.MemCpy`
**Flags:** condition, static

**Input:**
- `destination: int`
- `source: int`
- `size: int`

---

### `0C11` SF_MEMFILL
Fills a sized memory block with value byte-by-byte

**Class:** `Sf.MemFill`
**Flags:** condition, static

**Input:**
- `address: int`
- `byteValue: int`
- `size: int`

---

### `0C12` SF_MEMEQ
Evaluates as logical true if both memory blocks have the same content

**Class:** `Sf.MemEq`
**Flags:** condition, static

**Input:**
- `addressA: int`
- `addressB: int`
- `size: int`

---

### `0C13` SF_STRCPY
Copies the string from source to destination

**Class:** `Sf.StrCpy`
**Flags:** static

**Input:**
- `destination: string`
- `source: string`

---

### `0C14` SF_STREQ
Evaluates as logical true if both case-sensitive strings are equal

**Class:** `Sf.StrEq`
**Flags:** condition, static

**Input:**
- `stringA: string`
- `stringB: string`

---

### `0C15` SF_STRCAT
Appends the appendedString at the end of the string found at the stringBuffer

**Class:** `Sf.StrCat`
**Flags:** static

**Input:**
- `stringBuffer: string`
- `appendedString: string`

---

### `0C16` SF_STRTOK
Searches the stringBuffer for any delimiters then replaces the first hit with a NULL terminator (0x00). Returns the (token) pointer next to the first hit. Can be used as a condition which evaluates as logical false if none of the delimiters were found at the string

**Class:** `Sf.StrTok`
**Flags:** condition, static

**Input:**
- `stringBuffer: string`
- `delimiters: string`

**Output:**
- `token: string (variable)`

---

### `0C17` SF_STRLEN
Returns the length of a string

**Class:** `Sf.StrLen`
**Flags:** static

**Input:**
- `string: string`

**Output:**
- `length: int (variable)`

---

### `0C18` SF_STRSTR
Returns a pointer to the first occurence of a specified substring in the source string

**Class:** `Sf.StrStr`
**Flags:** condition, static

**Input:**
- `source: string`
- `subString: string`

**Output:**
- `matchAddress: string (variable)`

---

### `0C19` SF_STRCSPN
Searches the string for any matching characters at the characterList. Returns the character index of the first occurence from the string and evaluates as logical true if used as a condition. Returns the length of the string if nothing matched the characterSet

**Class:** `Sf.StrCspn`
**Flags:** condition, static

**Input:**
- `source: string`
- `characterList: string`

**Output:**
- `index: int (variable)`

---

### `0C1A` SF_ATOI
Converts an ascii string into a decimal integer

**Class:** `Sf.AtoI`
**Flags:** static

**Input:**
- `ascii: string`

**Output:**
- `integer: int (variable)`

---

### `0C1B` SF_ATOF
Converts an ascii string into a floating point number

**Class:** `Sf.AtoF`
**Flags:** static

**Input:**
- `ascii: string`

**Output:**
- `float: float (variable)`

---

### `0C1C` SF_ITOA
Converts a baseN integer into an ascii string then stores it to stringBuffer

**Class:** `Sf.ItoA`
**Flags:** static

**Input:**
- `integer: int`
- `radix: int`

**Output:**
- `stringBuffer: string (variable)`

---

### `0C1D` SF_READ_ELEMENT_OF_SIZED_ARRAY
Reads the value of the sized array's element at index. The size per element is constrained between 1 to 4

**Class:** `Sf.ReadElementOfSizedArray`
**Flags:** condition, static

**Input:**
- `array: int`
- `index: int`
- `size: int`

**Output:**
- `value: any (variable)`

---

### `0C1E` SF_WRITE_ELEMENT_OF_SIZED_ARRAY
Writes the value to the specified element index of a sized array. The size per element is constrained between 1 to 4

**Class:** `Sf.WriteElementOfSizedArray`
**Flags:** condition, static

**Input:**
- `array: int`
- `index: int`
- `size: int`
- `value: any`

---

### `0C1F` SF_GET_ELEMENT_POINTER_OF_BUFFER_ARRAY
Returns a pointer to the element of an array of sized buffers using its element index

**Class:** `Sf.GetElementPointerOfBufferArray`
**Flags:** static

**Input:**
- `array: int`
- `index: int`
- `size: int`

**Output:**
- `address: int (variable)`

---

### `0C20` SF_WRITE_STRING_TO_ELEMENT_OF_BUFFER_ARRAY
Writes a string at the buffer element of an array of sized buffers using its element index

**Class:** `Sf.WriteStringToElementOfBufferArray`
**Flags:** static

**Input:**
- `array: int`
- `index: int`
- `size: int`
- `string: string`

---

### `0C21` SF_STRIEQ
Evaluates as logical true if both case-insensitive strings are equal

**Class:** `Sf.StriEq`
**Flags:** condition, static

**Input:**
- `stringA: string`
- `stringB: string`

---

### `0C22` SF_BIN_TO_HEX
Converts binary text to hexadecimal text and stores at stringBuffer. Can be used as a condition which evaluates as logical false if the bufferSize is not enough to contain the converted hexadecimal text

**Class:** `Sf.BintoHex`
**Flags:** condition, static

**Input:**
- `binaryString: string`
- `stringBuffer: string`
- `bufferSize: int`

---

### `0C23` SF_HEX_TO_BIN
Converts hexadecimal text to binary text and stores at stringBuffer. Can be used as a condition which evaluates as logical false if the bufferSize is not enough to contain the converted binary text

**Class:** `Sf.HextoBin`
**Flags:** condition, static

**Input:**
- `hexString: string`
- `stringBuffer: string`
- `bufferSize: int`

---

### `0C24` SF_STRNCPY
Copies the string safely from source to stringBuffer. The copied string will be truncated if the occupied size is beyond the specified bufferSize

**Class:** `Sf.StrnCpy`
**Flags:** static

**Input:**
- `stringBuffer: int`
- `source: int`
- `bufferSize: int`

---

### `0C25` SF_STRNEQ
Evaluates as logical true if all characters with length at the beginning of both case-sensitive strings are equal

**Class:** `Sf.StrnEq`
**Flags:** condition, static

**Input:**
- `stringA: string`
- `stringB: string`
- `length: int`

---

### `0C26` SF_STRUPR
Converts all letters of the source's string into CAPITAL LETTERS stored at destination

**Class:** `Sf.StrUpr`
**Flags:** static

**Input:**
- `source: string`

**Output:**
- `destination: string (variable)`

---

### `0C27` SF_STRNCAT
Appends a appendedString safely at the end of the string found at the stringBuffer. The appendedString will be truncated if the overall size is beyond the specified bufferSize

**Class:** `Sf.StrnCat`
**Flags:** static

**Input:**
- `stringBuffer: string`
- `appendedString: string`
- `bufferSize: int`

---

### `0C28` SF_STRLWR
Converts all letters of the source's string into non-capital letters stored at destination

**Class:** `Sf.StrLwr`
**Flags:** static

**Input:**
- `source: string`

**Output:**
- `destination: string (variable)`

---

### `0C29` SF_STRISTR
Returns a pointer to the first case-insensitive occurence of the specified substring in the source string

**Class:** `Sf.StriStr`
**Flags:** condition, static

**Input:**
- `source: string`
- `subString: string`

**Output:**
- `matchAddress: string (variable)`

---

### `0C2A` SF_STRCHR
Returns a pointer to the first occurence of the specified ascii character in the source string

**Class:** `Sf.StrChr`
**Flags:** condition, static

**Input:**
- `source: string`
- `character: int`

**Output:**
- `matchAddress: int (variable)`

---

### `0C2B` SF_STRPBRK
Searches the source's string for any matching characters at the characterList. Returns a pointer to the first occurence from the source's string and evaluates as logical true if used as a condition

**Class:** `Sf.StrPBrk`
**Flags:** condition, static

**Input:**
- `source: string`
- `characterList: string`

**Output:**
- `matchAddress: string (variable)`

---

### `0C2C` SF_STRRCHR
Returns a pointer to the last occurence of the specified ascii character in the source string

**Class:** `Sf.StrRChr`
**Flags:** condition, static

**Input:**
- `source: string`
- `character: int`

**Output:**
- `matchAddress: string (variable)`

---

### `0C2D` SF_STRREV
Reverses the source's string, changing the positions of characters, then stores it to the destination

**Class:** `Sf.StrRev`
**Flags:** static

**Input:**
- `source: string`

**Output:**
- `destination: string (variable)`

---

### `0C2E` SF_STRSPN
Searches the source's string then returns the index of the first character that does not match any of the specified characters in the characterList and evaluates as logical true if used as a condition. Returns the length of the string if all characters matches any characters at the characterList

**Class:** `Sf.StrSpn`
**Flags:** condition, static

**Input:**
- `source: string`
- `characterList: string`

**Output:**
- `index: int (variable)`

---

### `0C2F` SF_STRTOL
Ignores any whitespace at the beginning of the source's string, converting the next characters into a baseN longInteger. The scanning stops when it comes across the first non-integer character, stores its pointer to unscannedAddress

**Class:** `Sf.StrTol`
**Flags:** static

**Input:**
- `source: int`
- `radix: int`

**Output:**
- `unscannedAddress: int (variable)`
- `longInteger: int (variable)`

---

### `0C30` SF_MATRIX_TO_QUAT
Converts a matrix structure into a quaternion structure stored at quaternionBuffer

**Class:** `Sf.MatrixToQuat`
**Flags:** static

**Input:**
- `matrix: int`

**Output:**
- `quaternionBuffer: int (variable)`

**Details:**

* This command follows the [GTA SA's Matrix Structure](https://github.com/DK22Pac/plugin-sdk/blob/master/plugin_sa/game_sa/CMatrix.h). But only requires the basis vectors ***right** (Pitch Axis)*, ***up** (Roll Axis)*, and ***at** (Yaw Axis)*.
* Unlike [GTA SA's Quaternion Structure](https://github.com/DK22Pac/plugin-sdk/blob/master/plugin_sa/game_sa/CQuaternion.h), this command uses a different Quaternion Structure which the ordering of its members were interchanged:
```c
struct Quaternion{
    float real;
    CVector imag;
}
```
* quaternionBuffer's size must be **at least** 16 bytes (Quaternion structure's size) to avoid memory corruption.

---

### `0C31` SF_QUAT_TO_MATRIX
Converts a quaternion structure into a matrix structure stored at matrixBuffer

**Class:** `Sf.QuatToMatrix`
**Flags:** static

**Input:**
- `quaternion: int`

**Output:**
- `matrixBuffer: int (variable)`

**Details:**

* Unlike [GTA SA's Quaternion Structure](https://github.com/DK22Pac/plugin-sdk/blob/master/plugin_sa/game_sa/CQuaternion.h), this command uses a different Quaternion Structure which the ordering of its members were interchanged:
```c
struct Quaternion{
    float real;
    CVector imag;
}
```
* This command follows the [GTA SA's Matrix Structure](https://github.com/DK22Pac/plugin-sdk/blob/master/plugin_sa/game_sa/CMatrix.h). But only requires the basis vectors ***right** (Pitch Axis)*, ***up** (Roll Axis)*, and ***at** (Yaw Axis)*.
* matrixBuffer's size must be **at least** 48 bytes (Matrix structure's size) to avoid memory corruption.

---

### `0C32` SF_AXES_TO_QUAT
Converts the basis vectors of a rotation matrix into quaternion values

**Class:** `Sf.AxesToQuat`
**Flags:** static

**Input:**
- `pitchVectorX: float`
- `pitchVectorY: float`
- `pitchVectorZ: float`
- `rollVectorX: float`
- `rollVectorY: float`
- `rollVectorZ: float`
- `yawVectorX: float`
- `yawVectorY: float`
- `yawVectorZ: float`

**Output:**
- `quaternionW: float (variable)`
- `quaternionX: float (variable)`
- `quaternionY: float (variable)`
- `quaternionZ: float (variable)`

---

### `0C33` SF_QUAT_TO_AXES
Converts the quaternion values into basis vectors of a rotation matrix

**Class:** `Sf.MathQuatToMatrixVectors`
**Flags:** static

**Input:**
- `quaternionW: float`
- `quaternionX: float`
- `quaternionY: float`
- `pitchVectorZ: float`

**Output:**
- `pitchVectorX: float (variable)`
- `pitchVectorY: float (variable)`
- `pitchVectorZ: float (variable)`
- `rollVectorX: float (variable)`
- `rollVectorY: float (variable)`
- `rollVectorZ: float (variable)`
- `yawVectorX: float (variable)`
- `yawVectorY: float (variable)`
- `yawVectorZ: float (variable)`

---

### `0C3A` SF_STRING_POINTER
Stores a pointer to the specified string into the variable

**Class:** `Sf.StrPtr`
**Flags:** static

**Input:**
- `variable: int (variable)`
- `string: string`
- `unused: arguments`

---

### `0C67` SF_STORE_OS_ENVIRONMENT_VARIABLE
Stores the contents of the specified Windows variable (or environment variable) name to buffer

**Class:** `Sf.GetOsEnv`
**Flags:** condition, static

**Input:**
- `varName: string`
- `stringBuffer: string`
- `buffersize: int`

**Details:**

The stored string is truncated if its size(length + null terminator) is greater than the buffersize.

---

### `0C68` SF_UNICODE_TO_ANSI
Converts a Unicode string to ANSI string then stores it to ansiStringBuffer

**Class:** `Sf.UnicodeToAnsi`
**Flags:** condition, static

**Input:**
- `unicodeString: int`
- `ansiStringBuffer: string`
- `bufferSize: int`

**Details:**

The stored ANSI string is truncated if its size(length + null terminator) is greater than the buffersize.

---

### `0C69` SF_ANSI_TO_UNICODE
Converts an ANSI string to Unicode string then stores it to ansiStringBuffer

**Class:** `Sf.AnsiToUnicode`
**Flags:** condition, static

**Input:**
- `ansiString: string`
- `unicodeStringBuffer: int`
- `buffersize: int`

**Details:**

The stored Unicode string is truncated if its size(length + null terminator) is greater than the buffersize.

---

### `0C70` SF_GET_LOADED_MODULE
Returns the handle of a loaded module with name (moduleName)

**Class:** `Sf.GetModule`
**Flags:** condition, static

**Input:**
- `moduleName: string`

**Output:**
- `handle: int (variable)`

**Details:**

Unlike LOAD_DYNAMIC_LIBRARY, this command does not load the module if it's not yet loaded/running and will evaluate as logical false if used as a condition

---

### `0C71` SF_GET_MODULE_PROCEDURE
Returns a pointer (functionPtr) to specified functionName inside the moduleHandle

**Class:** `Sf.GetModuleProc`
**Flags:** condition, static

**Input:**
- `moduleHandle: int`
- `functionName: string`

**Output:**
- `functionPtr: int (variable)`

**Details:**

Unlike LOAD_DYNAMIC_LIBRARY, this command does not load the module if it's not yet loaded/running and will evaluate as logical false if used as a condition

---

### `0C72` SF_SET_KEY_STATUS
Sets whether a specific virtual key code is pressed or not

**Class:** `Sf.SetKeyStatus`
**Flags:** static

**Input:**
- `keyCode: KeyCode`
- `isPressed: bool`

---

### `0C73` SF_SET_CHARACTER_KEY_STATUS
Sets whether a specific virtual key represented in ascii character format is pressed or not

**Class:** `Sf.SetCharKeyStatus`
**Flags:** static

**Input:**
- `ascii: int`
- `isPressed: bool`

**Details:**

Unlike SF_SET_KEY_STATUS, this command is limited to keyboard characters defined in the ascii table, and cannot process special keys like CTRL, F1, PRTSCR.

---

### `0C89` SF_KEY_JUST_PRESSED
Evaluates as logical true if the specified virtual keyCode has been pressed just now

**Class:** `Sf.KeyJustPressed`
**Flags:** condition, static

**Input:**
- `keyCode: KeyCode`

**Details:**

1. Initially, while the user isn't pressing the key, this command waits for the user to press the key
2. Once the user holds down the key just now, this command will be evaluated as logical true on all conditional statements during this frame
3. After this frame, waits for the user to release the key
3.1. While waiting, this command will always be evaluated as logical false on all conditional statements
4. When the user releases the key, then process repeats again

---

### `0C8D` SF_WRITE_TEXT_TO_CLIPBOARD
Sets the text on the clipboard

**Class:** `Sf.ClipboardWriteText`
**Flags:** static

**Input:**
- `text: string`

---

### `0C8E` SF_READ_DATA_FROM_CLIPBOARD
Copies raw binary or text from the clipboard to buffer

**Class:** `Sf.ClipboardReadData`
**Flags:** condition, static

**Input:**
- `buffer: int`
- `size: int`

---

### `0C92` SF_GET_CLEO_LIBRARY_VERSION
Returns the installed version of CLEO

**Class:** `Sf.GetCleoLibVer`
**Flags:** static

**Output:**
- `version: int (variable)`

---

### `1337` SF_MAKE_SCRIPT_PRIVATE
Makes the script where this command is executed invisible across other scripts

**Class:** `Sf.MakeScriptPrivate`
**Flags:** static

**Input:**
- `isPrivate: int`

---

### SfConsole

### `0B78` SF_LOG_TO_CONSOLE
Adds a line to the SAMPFUNCS console and logs it

**Class:** `SfConsole.Log`
**Flags:** static

**Input:**
- `format: string`
- `args: arguments`

---

### `0C62` SF_EXECUTE_CONSOLE_COMMAND
Executes the specified command in the SAMPFUNCS console

**Class:** `SfConsole.ExecCmd`
**Flags:** static

**Input:**
- `command: string`

---

### `0C63` SF_REGISTER_CONSOLE_COMMAND
Registers a callback hooked on a SAMPFUNCS console command with maximum length of 64 characters

**Class:** `SfConsole.RegisterCmd`
**Flags:** condition, static

**Input:**
- `command: string`
- `callback: label`

**Details:**

* You must pass an offset label as the callback parameter. Like For example, **@ConsoleCallback_SetHP**
* The callback label must contain the callback's body.
* Construct the callback's flow of execution with caution.
  * Like subroutines, callbacks uses the variable space of the script's main thread.
  * Callbacks have higher priority than the custom script's main thread. Meaning, eveytime the script encounters the **WAIT** command at the main thread, the script will execute all callbacks first(if interrupt flag was fired by a callback), then continues to execute the main thread's commands after where the **WAIT** command was encountered.
  * Avoid executing too much commands inside the callback. Doing so would lead to undersirable script behavior, like failing to detect interrupts from other registered callbacks or event handlers.
  * **WAIT** command inside a Callback **WILL NOT WORK!** Because callbacks are designed to finish as soon as possible.
  * All callbacks hooked by this command must use **SF_COMMAND_RETURN** command as returning statement, indicating the end of callback.

---

### `0C64` SF_UNREGISTER_CONSOLE_COMMAND
Removes the specified SAMPFUNCS console command. This command does nothing if the the specified command isn't a registered in the SAMPFUNCS console then evaluates as logical false if used as a condition

**Class:** `SfConsole.UnregisterCmd`
**Flags:** condition, static

**Input:**
- `command: string`

---

### `0C7E` SF_IS_CONSOLE_OPEN
Evaluates as logical true if the SAMPFUNCS console is open

**Class:** `SfConsole.IsOpen`
**Flags:** condition, static

---

### `0C80` SF_SET_CONSOLE_COMMAND_DESCRIPTION
Sets the description for the console command

**Class:** `SfConsole.SetCmdDesc`
**Flags:** static

**Input:**
- `command: string`
- `description: string`

---

### `0C91` SF_IS_CONSOLE_COMMAND_REGISTERED
Returns logical true if the specified console command is registered

**Class:** `SfConsole.IsCmdRegistered`
**Flags:** condition, static

**Input:**
- `command: string`

---

### SfD3D

### `0B68` SF_D3D_DRAW_LINE
Draws a line between two window screen coordinates

**Class:** `SfD3D.DrawLine`
**Flags:** static

**Input:**
- `fromCoordX: int`
- `fromCoordY: int`
- `toCoordX: int`
- `toCoordY: int`
- `tickness: int`
- `color: int`

**Details:**

* fromcoord and tocoord must not be equal. Doing so will crash the D3D interface of SAMPFUNCS.
* fromcoord and tocoord must be in window screen coordinate format
* tickness is approximately by pixels on a straight line
* color is in 0xAARRGGBB format

---

### `0B69` SF_D3D_DRAW_BORDERLESS_BOX
Draws a rectangular area at the specified coordinates

**Class:** `SfD3D.DrawBorderlessBox`
**Flags:** static

**Input:**
- `coordX: int`
- `coordY: int`
- `width: int`
- `height: int`
- `color: int`

**Details:**

* coordx and coordy values must be in window screen coordinate system format.
* coordx and coordy is found at the center of the rectangle.
* color must be in 0xAARRGGBB format where A = Alpha, R = Red, G = Green B, = Blue.
* All Render commands will malfunction if coordx == coordy.

---

### `0B6A` SF_D3D_DRAW_BORDERED_BOX
Draws a rectangular area with border at the specified coordinates

**Class:** `SfD3D.DrawBorderedBox`
**Flags:** static

**Input:**
- `coordX: int`
- `coordY: int`
- `width: int`
- `height: int`
- `color: int`
- `borderSize: int`
- `borderColor: int`

**Details:**

* coordx and coordy values must be in window screen coordinate system format.
* coordx and coordy is found at the center of the rectangle.
* box color and bordercolor must be in 0xAARRGGBB format where A = Alpha, R = Red, G = Green B, = Blue.
* All Render commands will malfunction if coordx == coordy.

---

### `0B70` SF_D3D_DRAW_POLYGON
Draws a polygon with the specified parameters

**Class:** `SfD3D.DrawPolygon`
**Flags:** static

**Input:**
- `coordX: int`
- `coordY: int`
- `width: int`
- `height: int`
- `cornerCount: int`
- `heading: float`
- `color: int`

**Details:**

* Avoid using high cornercount values as this could lag the game. Keep the cornercount value to minimal
* coordx, coordy, width, height are window screen values.
* color must be in 0xAARRGGBB format where A = Alpha, R = Red, G = Green, B = Blue

---

### SfD3DFont

### `0B6B` SF_D3D_GET_DRAW_WIDTH_OF_TEXT_WITH_FONT
Returns the width (in pixels) that will be occupied by the text with font

**Class:** `SfD3DFont.GetDrawWidth`

**Input:**
- `self: SfD3DFont`
- `text: string`

**Output:**
- `width: int (variable)`

---

### `0B6C` SF_D3D_GET_FONT_DRAW_HEIGHT
Returns the height (in pixels) occupied by any text that uses the specified font

**Class:** `SfD3DFont.GetDrawHeight`

**Input:**
- `self: SfD3DFont`

**Output:**
- `height: int (variable)`

---

### `0B6D` SF_D3D_CREATE_FONT
Creates a D3DFont Object

**Class:** `SfD3DFont.Create`
**Flags:** constructor

**Input:**
- `fontName: string`
- `size: int`
- `styleFlags: SampTextStyle`

**Output:**
- `handle: SfD3DFont (variable)`

**Details:**

* For more info about fontname and styleFlags, read the Font API's by Microsoft.
* RenderFont objects created by this command allocate memory and need to be manually destroyed by SF_D3D_DELETE_FONT if not used anymore to free them from memory.

SampTextStyle enum consists of common styleFlags you could use. Multiple styles are allowed as long as you Add/OR them together. For example:
```go
// font text will be written in italic with bold thickness and a border between it 
SampTextStyle myTextStyleFlags = SampTextStyle.FCRBold
SampTextStyle myTextStyleFlags |= SampTextStyle.FCRItalic
SampTextStyle myTextStyleFlags |= SampTextStyle.FCRBorder
```

---

### `0B6E` SF_D3D_DELETE_FONT
Destroys the specified font object, freeing it from memory

**Class:** `SfD3DFont.Delete`
**Flags:** condition, destructor

**Input:**
- `self: SfD3DFont`

**Details:**

Can be used as a condition which evaluates as false if the specified renderfont object is invalid or does not exist.

---

### `0B6F` SF_D3D_DRAW_TEXT_WITH_FONT
Draws text using the specified font

**Class:** `SfD3DFont.DrawText`

**Input:**
- `self: SfD3DFont`
- `text: string`
- `coordX: int`
- `coordY: int`
- `color: int`

**Details:**

* coordx and coordy must be in window screen coordinate system format
* color must be in 0xAARRGGBB format where A = Alpha, R = Red, G = Green, B = Blue

---

### SfD3DTexture

### `0B71` SF_D3D_LOAD_TEXTURE_FROM_FILE
Loads a file (any image, or txd) as D3DTexture Object

**Class:** `SfD3DTexture.Load`
**Flags:** condition, constructor

**Input:**
- `filePath: string`

**Output:**
- `handle: SfD3DTexture (variable)`

**Details:**

* filepath accepts cleo5 relative path keywords like "cleo:\<filepath>" or "root:\<filepath>"
* RenderTexture Objects created by this command requires manual cleanup when not used anymore. Use SF_D3D_RELEASE_TEXTURE to do so.
* Can be used as a condition which evaluates as true if the texture has been loaded successfully.

---

### `0B72` SF_D3D_RELEASE_TEXTURE
Releases the D3DTexture Object, freeing it from memory

**Class:** `SfD3DTexture.Release`
**Flags:** condition, destructor

**Input:**
- `self: SfD3DTexture`

**Details:**

* Can be used as a condition which evaluates as false if the specified RenderTexture Object is invalid or does not exist.

---

### `0B73` SF_D3D_DRAW_TEXTURE
Draws the texture on the screen

**Class:** `SfD3DTexture.Draw`

**Input:**
- `self: SfD3DTexture`
- `coordX: int`
- `coordY: int`
- `width: int`
- `height: int`
- `heading: float`
- `contrast: int`

**Details:**

* coordx, coordy, width, height are window screen values.
* contrast must be in 0xAARRGGBB format where A = Alpha, R = Red, G = Green, B = Blue

---

### `0C8C` SF_D3D_LOAD_TEXTURE_FROM_FILE_IN_MEMORY
Loads a texture from a file located in memory buffer

**Class:** `SfD3DTexture.LoadTextureFromFileMemory`
**Flags:** condition, constructor

**Input:**
- `buffer: int`
- `bufferSize: int`

**Output:**
- `handle: SfD3DTexture (variable)`

**Details:**

* buffer must contain the File Object before executing this command
* This command will replace the buffer's contents into the D3DTexture Object's structure
* Can be used as a condition which evaluates as false if buffer does not contain a valid File Object, or if bufferSize is not enough to contain the D3DTexture Object.

---

### SfDownload

### `0C65` SF_DOWNLOAD_FILE
Downloads a file from the specified url source asynchronosly then saves it to filepath. Returns a handle to this file's SfDownload object for tracking purposes

**Class:** `SfDownload.File`
**Flags:** constructor

**Input:**
- `url: string`
- `filePath: string`

**Output:**
- `handle: SfDownload (variable)`

**Details:**

* filePath parameter doesn't resolve cleo's prefix in file path, and must be in microsoft file path format:
    * Absolute Path
        * `C:\Program Files\somefolder\conf.ini`
        * `C:\Users\Public\Pictures\somefolder\pic.jpg`
    * Relative Path prefix "**.\\**"

|             cleoFileFormat           |                   msFileFormat                  |
|             -------------            |                  -------------                  |
| `"root:\somefolder\thisfile.txt"`    | `".\somefolder\thisfile.txt"`                   |
| `"cleo:\somefolder\thisfile.txt"`    | `".\cleo\somefolder\thisfile.txt"`              |
| `"modules:\somefolder\thisfile.txt"` | `".\cleo\cleo_modules\somefolder\thisfile.txt"` |

* Execute SF_GET_DOWNLOAD_STATE to know the download status
* When the SfDownload object is on Do-Nothing mode (status >= 0), you must manually execute SF_RELEASE_DOWNLOAD to free the SfDownload object from memory and avoid memory leak

---

### `0C66` SF_GET_DOWNLOAD_STATE
Returns the download status of the SfDownload object

**Class:** `SfDownload.GetState`
**Flags:** condition

**Input:**
- `self: SfDownload`

**Output:**
- `state: SfDownloadState (variable)`

**Details:**

The download status can be:
* -1 = download in progress
* 0 = download complete
* Other values are​ ErrorCodes indicating the download failed due to a certain reason:
    * 0x8007000E = E_OUTOFMEMORY: File cannot be created due to insufficient memory storage
    * 0x800C0008 = INET_E_DOWNLOAD_FAILURE: Connection has been interrupted (No Internet, Insufficient Create/Write File permission at filePath)
    * etc.

---

### `0C7D` SF_RELEASE_DOWNLOAD
Frees an SfDownload object from memory

**Class:** `SfDownload.Release`
**Flags:** condition, destructor

**Input:**
- `self: SfDownload`

---

### SfDxutDialog

### `0B80` SF_DXUT_CREATE_DIALOG
Creates a DXUTDialog Object with Title

**Class:** `SfDxutDialog.Create`
**Flags:** constructor

**Input:**
- `title: string`

**Output:**
- `handle: SfDxutDialog (variable)`

---

### `0B81` SF_DXUT_DIALOG_POP
Returns the last event and component ID that occurred with the specified dialog

**Class:** `SfDxutDialog.Pop`
**Flags:** condition

**Input:**
- `self: SfDxutDialog`

**Output:**
- `eventId: int (variable)`
- `controlId: int (variable)`

**Details:**

Can be used as a condition which evaluates as false if DxutDialog object is invalid.

---

### `0B82` SF_DXUT_DIALOG_ADD_BUTTON
Adds a button on the DXUTDialog

**Class:** `SfDxutDialog.AddButton`

**Input:**
- `self: SfDxutDialog`
- `id: int`
- `text: string`
- `relCoordX: int`
- `relCoordY: int`
- `width: int`
- `height: int`

**Details:**

* id must be unique to all elements of this DXUTDialog, else SF won't be able to interact with all old elements with the same id.
* relcoordx, relcoordx, width, height are window screen values.
* relcoordx, relcoordx are relative to the coordinates of the DXUTDialog.

---

### `0B83` SF_DXUT_DIALOG_ADD_CHECKBOX
Creates a checkbox on the DxutDialog

**Class:** `SfDxutDialog.AddCheckbox`

**Input:**
- `self: SfDxutDialog`
- `id: int`
- `text: string`
- `relCoordX: int`
- `relCoordY: int`
- `width: int`
- `height: int`

**Details:**

* id must be unique to all elements of this DXUTDialog, else SF won't be able to interact with all old elements with the same id.
* relcoordx, relcoordx, width, height are window screen values.
* relcoordx, relcoordx are relative to the coordinates of the DXUTDialog.

---

### `0B84` SF_DXUT_DIALOG_SET_COORDS_AND_DIMS
Sets the coordinates and dimensions of the DxutDialog

**Class:** `SfDxutDialog.SetCoordsAndDims`

**Input:**
- `self: SfDxutDialog`
- `coordX: int`
- `coordY: int`
- `width: int`
- `height: int`

**Details:**

* coordx, coordy, width, height are window screen values.

---

### `0B85` SF_DXUT_DIALOG_GET_COORDS_AND_DIMS
Returns the Coordinates and Dimensions of the DxutDialog

**Class:** `SfDxutDialog.GetCoordsAndDims`

**Input:**
- `self: SfDxutDialog`

**Output:**
- `coordX: int (variable)`
- `coordY: int (variable)`
- `width: int (variable)`
- `height: int (variable)`

**Details:**

* coordx, coordy, width, height are window screen values.

---

### `0B86` SF_DXUT_DIALOG_SET_VISIBILITY
Sets the visibility status of the DxutDialog

**Class:** `SfDxutDialog.Visibility`

**Input:**
- `self: SfDxutDialog`
- `isVisible: bool`

---

### `0B87` SF_DXUT_DIALOG_IS_VISIBLE
Checks if the DxutDialog is visible

**Class:** `SfDxutDialog.IsVisible`
**Flags:** condition

**Input:**
- `self: SfDxutDialog`

---

### `0B88` SF_DXUT_DIALOG_ADD_EDITBOX
Creates a text input field on a DxutDialog

**Class:** `SfDxutDialog.AddEditbox`

**Input:**
- `self: SfDxutDialog`
- `id: int`
- `initialText: string`
- `coordX: int`
- `coordY: int`
- `width: int`
- `height: int`

**Details:**

* id must be unique to all elements of this DXUTDialog, else SF won't be able to interact with all old elements with the same id.
* relcoordx, relcoordx, width, height are window screen values.
* relcoordx, relcoordx are relative to the coordinates of the DXUTDialog.

---

### `0B89` SF_DXUT_DIALOG_GET_TEXT_OF_CONTROL
Returns the text of a control using its ID

**Class:** `SfDxutDialog.GetControlText`
**Flags:** condition

**Input:**
- `self: SfDxutDialog`
- `id: int`

**Output:**
- `text: int (variable)`

**Details:**

Can be used as a condition which evaluates as true if the control's text has been retrieved successfully.

---

### `0B90` SF_DXUT_DIALOG_SET_VISIBILITY_OF_CONTROL
Sets the visibility of the DXUTDialog's control element with ID

**Class:** `SfDxutDialog.SetVisibilityOfControl`

**Input:**
- `self: SfDxutDialog`
- `controlId: int`
- `isVisible: int`

---

### `0B91` SF_DXUT_DIALOG_ADD_STATIC_TEXT
Adds a static text control in the DxutDialog

**Class:** `SfDxutDialog.AddStaticText`

**Input:**
- `self: SfDxutDialog`
- `id: int`
- `text: string`
- `relCoordX: int`
- `relCoordY: int`
- `width: int`
- `height: int`

**Details:**

* id must be unique to all elements of this DXUTDialog, else SF won't be able to interact with all old elements with the same id.
* relcoordx, relcoordx, width, height are window screen values.
* relcoordx, relcoordx are relative to the coordinates of the DXUTDialog.

---

### `0B92` SF_DXUT_DIALOG_IS_CHECKBOX_CHECKED
Evaluates as logical true if the checkbox control of the DxutDialog is checked

**Class:** `SfDxutDialog.IsCheckBoxChecked`
**Flags:** condition

**Input:**
- `self: SfDxutDialog`
- `checkboxId: int`

---

### `0B93` SF_DXUT_DIALOG_SET_BACKGROUND_COLOR
Sets the background color of the DxutDialog

**Class:** `SfDxutDialog.SetBgColor`

**Input:**
- `self: SfDxutDialog`
- `color: int`

**Details:**

color must be in 0xAARRGGBB format where A = Alpha, R = Red, G = Green, B = Blue

---

### `0B94` SF_DXUT_DIALOG_SET_TEXT_OF_CONTROL
Sets the text of a control using its ID

**Class:** `SfDxutDialog.SetControlText`
**Flags:** condition

**Input:**
- `self: SfDxutDialog`
- `id: int`
- `text: string`

**Details:**

Can be used as a condition which evaluates as true if the control's text has been changed successfully.

---

### `0B95` SF_DXUT_DIALOG_IS_CONTROL_VISIBLE
Evaluates as true if the DxutDialog's control element with ID is visible

**Class:** `SfDxutDialog.IsControlVisible`
**Flags:** condition

**Input:**
- `self: SfDxutDialog`
- `id: int`

---

### `0B96` SF_DXUT_DIALOG_ADD_SLIDER
Creates a horizontal slider on the DxutDialog

**Class:** `SfDxutDialog.AddSlider`

**Input:**
- `self: SfDxutDialog`
- `id: int`
- `relCoordX: int`
- `relCoordY: int`
- `width: int`
- `height: int`
- `maxValue: int`

**Details:**

* sliders are scrollable control elements that changes its slider value depending on how much it's been scrolled by the user. But this doesn't mean that the dialog's controls will be repositioned by it.
* a slider's value can be retrieved using SF_DXUT_DIALOG_GET_SLIDER_VALUE.
* a slider's value can be manually manipulated using SF_DXUT_DIALOG_SET_SLIDER_VALUE.
* id must be unique to all elements of this DXUTDialog, else SF won't be able to interact with all old elements with the same id.
* relcoordx, relcoordx, width, height are window screen values.
* relcoordx, relcoordx are relative to the coordinates of the DXUTDialog.

---

### `0B97` SF_DXUT_DIALOG_GET_SLIDER_VALUE
Returns the thumb position value of the DxutDialog's slider with ID

**Class:** `SfDxutDialog.GetSliderValue`

**Input:**
- `self: SfDxutDialog`
- `id: int`

**Output:**
- `value: int (variable)`

---

### `0B98` SF_DXUT_DIALOG_SET_SLIDER_VALUE
Sets the thumb position value of the DxutDialog's slider with ID

**Class:** `SfDxutDialog.SetSliderValue`

**Input:**
- `self: SfDxutDialog`
- `id: int`
- `value: int`

---

### `0B99` SF_DXUT_DIALOG_ADD_LISTBOX
Creates a listbox on the dialog

**Class:** `SfDxutDialog.AddListbox`

**Input:**
- `self: SfDxutDialog`
- `id: int`
- `relCoordX: int`
- `relCoordY: int`
- `width: int`
- `height: int`

**Details:**

* id must be unique to all elements of this DXUTDialog, else SF won't be able to interact with all old elements with the same id.
* relcoordx, relcoordx, width, height are window screen values.
* relcoordx, relcoordx are relative to the coordinates of the DXUTDialog.

---

### `0B9A` SF_DXUT_DIALOG_INSERT_LISTBOX_ELEMENT
Inserts a new element into the DxutDialog's listbox with ID

**Class:** `SfDxutDialog.InsertListboxElement`
**Flags:** condition

**Input:**
- `self: SfDxutDialog`
- `id: int`
- `text: int`
- `data: int`
- `index: int`

**Details:**

* index = -1 inserts the element at the end of the list
* Can be used as a condition which evaluates as true if the element has been inserted successfully.

---

### `0B9B` SF_DXUT_DIALOG_GET_SELECTED_LISTBOX_ELEMENT
Returns the index of the selected element and the count/number of elements in the DxutDialog's listbox with ID

**Class:** `SfDxutDialog.GetSelectedListboxElement`

**Input:**
- `self: SfDxutDialog`
- `id: int`

**Output:**
- `index: int (variable)`
- `count: int (variable)`

---

### `0B9C` SF_DXUT_DIALOG_DELETE_LISTBOX_ELEMENT
Removes the element found at the specified index from the DxutDialog's listbox with ID

**Class:** `SfDxutDialog.DeleteListboxElement`
**Flags:** condition

**Input:**
- `self: SfDxutDialog`
- `id: int`
- `index: int`

**Details:**

* Can be used as a condition which evaluates as true if the element has been removed successfully.

---

### `0B9D` SF_DXUT_DIALOG_GET_LISTBOX_ELEMENT
Returns the text and data associated with the DxutDialog's listbox element by index

**Class:** `SfDxutDialog.GetListboxElement`
**Flags:** condition

**Input:**
- `self: SfDxutDialog`
- `id: int`
- `index: int`

**Output:**
- `text: string (variable)`
- `data: int (variable)`

**Details:**

* Can be used as a condition which evaluates as true if the element has been removed successfully.

---

### `0B9E` SF_DXUT_DIALOG_SET_STATUS_OF_CHECKBOX
Sets the status of a checkbox

**Class:** `SfDxutDialog.SetCheckboxStatus`

**Input:**
- `self: SfDxutDialog`
- `id: int`
- `isChecked: bool`

---

### `0B9F` SF_DXUT_DIALOG_SET_TITLE_VISIBILITY
Sets the visibility of the DxutDialog's title

**Class:** `SfDxutDialog.SetTitleVisibility`

**Input:**
- `self: SfDxutDialog`
- `isVisible: bool`

---

### `0BA0` SF_DXUT_DIALOG_IS_TITLE_VISIBLE
Evaluates as logical true if the DxutDialog's title is visible

**Class:** `SfDxutDialog.IsTitleVisible`
**Flags:** condition

**Input:**
- `self: SfDxutDialog`

---

### `0BA1` SF_DXUT_DIALOG_SET_MINIMIZED
Sets the minimized status of the DxutDialog

**Class:** `SfDxutDialog.SetMinimized`

**Input:**
- `self: SfDxutDialog`
- `isMinimized: bool`

---

### `0BA2` SF_DXUT_DIALOG_IS_MINIMIZED
Returns logical true if the DxutDialog is minimized

**Class:** `SfDxutDialog.IsMinimized`
**Flags:** condition

**Input:**
- `self: SfDxutDialog`

---

### `0BA3` SF_DXUT_DIALOG_DELETE_CONTROL
Removes a DxutDialog's control with ID and frees the memory allocated for it

**Class:** `SfDxutDialog.DeleteControl`

**Input:**
- `self: SfDxutDialog`
- `id: int`

**Details:**

This command will not be able to delete old controls that has their ID duplicated by newly created controls

---

### `0BA4` SF_DXUT_DIALOG_DELETE
Deletes the DxutDialog and frees the memory allocated for it

**Class:** `SfDxutDialog.Delete`
**Flags:** destructor

**Input:**
- `self: SfDxutDialog`

---

### `0BA5` SF_DXUT_DIALOG_SET_FOCUSED_CONTROL
Sets the focus of user interaction to a specific DxutDialog control with ID

**Class:** `SfDxutDialog.ToggleControlFocus`

**Input:**
- `self: SfDxutDialog`
- `id: int`

---

### `0BA6` SF_DXUT_DIALOG_SET_DIMS_OF_CONTROL
Changes the dimensions of the DxutDialog control with ID

**Class:** `SfDxutDialog.SetDims`

**Input:**
- `self: SfDxutDialog`
- `id: int`
- `width: int`
- `height: int`

**Details:**

width, height must be window screen values in pixels.

---

### `0BA7` SF_DXUT_DIALOG_GET_DIMS_OF_CONTROL
Returns the dimensions of the DxutDialog control with ID

**Class:** `SfDxutDialog.GetControlDims`

**Input:**
- `self: SfDxutDialog`
- `id: int`

**Output:**
- `width: int (variable)`
- `height: int (variable)`

**Details:**

width, height are window screen values in pixels.

---

### `0BA8` SF_DXUT_DIALOG_SET_COORDS_OF_CONTROL
Sets the window position of the DxutDialog control with ID

**Class:** `SfDxutDialog.SetControlCoords`

**Input:**
- `self: SfDxutDialog`
- `id: int`
- `relCoordX: int`
- `relCoordY: int`

**Details:**

* relcoordx, relcoordx are window screen values.
* relcoordx, relcoordx are relative to the coordinates of the DXUTDialog.

---

### `0BA9` SF_DXUT_DIALOG_GET_COORDS_OF_CONTROL
Returns the window position of a DxutDialog control

**Class:** `SfDxutDialog.GetControlCoords`

**Input:**
- `self: SfDxutDialog`
- `id: int`

**Output:**
- `coordX: int (variable)`
- `coordY: int (variable)`

**Details:**

* relcoordx, relcoordx are window screen values.
* relcoordx, relcoordx are relative to the coordinates of the DXUTDialog.

---

### `0BAA` SF_DXUT_DIALOG_SET_COLOR_OF_CHECKBOX
Sets the color of DxutDialog's checkbox control with ID

**Class:** `SfDxutDialog.SetCheckboxColor`

**Input:**
- `self: SfDxutDialog`
- `id: int`
- `color: int`

**Details:**

* color must be in 0xAARRGGBB format where A = Alpha, R = Red, G = Green, B = Blue

---

### `0BAB` SF_DXUT_DIALOG_EXIST
Evaluates as logical true if the specified DxutDialog exists

**Class:** `SfDxutDialog.DoesExist`
**Flags:** condition

**Input:**
- `self: SfDxutDialog`

---

### SfGFunc

### `0C34` SF_REGISTER_CUSTOM_GLOBAL_FUNCTION
Registers the name of a custom global function allowing other scripts to call it using SF_CALL_CUSTOM_GLOBAL_FUNCTION command

**Class:** `SfGFunc.Register`
**Flags:** condition, static

**Input:**
- `name: string`
- `label: label`

**Details:**

* label must contain the function's body
* If the name was already registered:
    * The registration is cancelled then evaluates as logical false if used as a condition
    * Separately execute SF_UNREGISTER_CUSTOM_GLOBAL_FUNCTION first before executing this command
* All functions registered by this command must use **SF_CUSTOM_GLOBAL_FUNCTION_RETURN** command as returning statement

---

### `0C35` SF_CALL_CUSTOM_GLOBAL_FUNCTION
Calls a registered custom global function with name

**Class:** `SfGFunc.Call`
**Flags:** condition, static

**Input:**
- `name: string`
- `numArgs: int`
- `args: arguments`

**Details:**

**Global Functions** are like Local Functions
* Has its own local variable space.
* Can optionally accept input parameters
* Can optionally return output parameters

Unlike Local Functions that can manually set *logical* parameter upon return via **CLEO_RETURN_WITH**, **Global Functions** doesn't support a *logical* parameter that can manually be set. Instead, this command does nothing if the specified name isn't a registered custom global function then evaluates as logical false if used as a condition.

**Global Functions** specifically:
* Requires **SF_CUSTOM_GLOBAL_FUNCTION_RETURN** command as its returning statement.
* Can only be called using **SF_CALL_CUSTOM_GLOBAL_FUNCTION** command.
* Crashes the game when this script(where this function is defined) executes this function via **CLEO_CALL**.

---

### `0C36` SF_CUSTOM_GLOBAL_FUNCTION_RETURN
Returns the flow of the execution to the next instruction after the custom global function call, optionally returning one or more parameters as result

**Class:** `SfGFunc.Return`
**Flags:** condition, static

**Input:**
- `numRet: int`
- `retParams: arguments`

---

### `0C37` SF_IS_CUSTOM_GLOBAL_FUNCTION_REGISTERED
Evaluates as logical true if the specified name is registered a custom global function

**Class:** `SfGFunc.IsRegistered`
**Flags:** condition, static

**Input:**
- `name: string`

---

### `0C38` SF_CUSTOM_GLOBAL_FUNCTION_GET_ORIGIN
Returns the origin informations of a custom global function with name

**Class:** `SfGFunc.GetOrigin`
**Flags:** condition, static

**Input:**
- `name: string`

**Output:**
- `hostThreadAddress: int (variable)`
- `functionAddress: int (variable)`

---

### `0C39` SF_UNREGISTER_CUSTOM_GLOBAL_FUNCTION
Removes the currently registered custom global function. Allowing its name to be re-registered by SF_REGISTER_CUSTOM_GLOBAL_FUNCTION command

**Class:** `SfGFunc.Unregister`
**Flags:** static

**Input:**
- `name: string`

---

### SfGVar

### `0BFC` SF_SET_CUSTOM_GLOBAL_VARIABLE
Sets the value of the custom global variable with name

**Class:** `SfGVar.Set`
**Flags:** condition, static

**Input:**
- `name: string`
- `value: any`

---

### `0BFD` SF_GET_CUSTOM_GLOBAL_VARIABLE
Returns the value of the custom global variable with name

**Class:** `SfGVar.Get`
**Flags:** condition, static

**Input:**
- `name: string`

**Output:**
- `value: any (variable)`

---

### `0C5F` SF_DOES_CUSTOM_GLOBAL_VARIABLE_EXIST
Evaluates as logical true if a custom global variable with specified name existed

**Class:** `SfGVar.DoesExist`
**Flags:** condition, static

**Input:**
- `name: string`

---

### `0C60` SF_SET_CUSTOM_GLOBAL_VARIABLE_SCOPE
Sets whether the specified script can read or write to the specified custom global variable

**Class:** `SfGVar.SetScope`
**Flags:** condition, static

**Input:**
- `gVarName: string`
- `scriptPtr: int`
- `canRead: bool`
- `canWrite: bool`

---

### `0C61` SF_GET_CUSTOM_GLOBAL_VARIABLE_SCOPE
Returns the specified script's read/write permissions to the specified custom global variable

**Class:** `SfGVar.GetScope`
**Flags:** condition, static

**Input:**
- `gVarName: int`
- `scriptPtr: int`

**Output:**
- `canRead: bool (variable)`
- `canWrite: bool (variable)`

---

### SfScript

### `0C6A` SF_START_NEW_SCRIPT_FROM_LABEL
Starts a new script from the specified scriptLabel then stores its pointer at newScriptPtrTo parameter

**Class:** `SfScript.RunFromLabel`
**Flags:** static

**Input:**
- `scriptLabel: label`
- `newScriptPtrTo: SfScript (variable)`
- `passedValues: arguments`

**Details:**

Use this command with caution.
    * **Script** vs **Custom_Script** are two different types. Do not use any **Custom_Script** related commands inside the scriptLabel's body

newScriptPtrTo can be set to any constant value if this script's pointer isn't needed to be retrieved. Else, pass a variable to newScriptPtrTo parameter.
* `SF_START_NEW_SCRIPT_FROM_LABEL {scriptLabel} @MyRunnedScript {newScriptPtrTo} 0 ` Runs the script without retrieving its pointer
* `SF_START_NEW_SCRIPT_FROM_LABEL {scriptLabel} @MyRunnedScript {newScriptPtrTo} 5@` Runs the script then store its pointer to **5@**

The passedValues parameter are optional and can be used to set the initial values for the local variables of the new script. For example:
* `SF_START_NEW_SCRIPT_FROM_LABEL {scriptLabel} @MyRunnedScript {newScriptPtrTo} 0 {passedValues} 100 13.42 0x42352 18@` will start the script with `0@ = 100`, `1@ = 13.42`, `2@ = 0x42352`, and `3@ = starter's 18@ value`.

To terminate a script started by this command, use any on the following depending on the circumstances:
* TERMINATE_THIS_SCRIPT
* SF_TERMINATE_SCRIPT or TERMINATE_SCRIPT
* TERMINATE_ALL_SCRIPTS_WITH_THIS_NAME

This command has the same effect as START_NEW_SCRIPT

---

### `0C6B` SF_START_NEW_SCRIPT_FROM_POINTER
Starts a new script from the specified memory location where a script binary data is stored (scriptBin) then stores its pointer at newScriptPtrTo parameter

**Class:** `SfScript.RunFromPtr`
**Flags:** static

**Input:**
- `scriptBin: int`
- `newScriptPtrTo: SfScript (variable)`
- `passedValues: arguments`

**Details:**

Use this command with caution.
    * The game will crash if scriptBin isn't a Script Binary.
    * **Script** vs **Custom_Script** are two different types. Do not use any **Custom_Script** related commands inside the scriptLabel's body

newScriptPtrTo can be set to any constant value if this script's pointer isn't needed to be retrieved. Else, pass a variable to newScriptPtrTo parameter.
* `SF_START_NEW_SCRIPT_FROM_POINTER {scriptBin} csBin {newScriptPtrTo} 0 ` Runs the script without retrieving its pointer
* `SF_START_NEW_SCRIPT_FROM_POINTER {scriptBin} csBin {newScriptPtrTo} 5@` Runs the script then store its pointer to **5@**

The passedValues parameter are optional and can be used to set the initial values for the local variables of the new script. For example:
* `SF_START_NEW_SCRIPT_FROM_POINTER {scriptBin} csBin {newScriptPtrTo} 0 {passedValues} 100 13.42 0x42352 18@` will start the script with `0@ = 100`, `1@ = 13.42`, `2@ = 0x42352`, and `3@ = starter's 18@ value`.

To terminate a script started by this command, use any on the following depending on the circumstances:
* TERMINATE_THIS_SCRIPT
* SF_TERMINATE_SCRIPT or TERMINATE_SCRIPT
* TERMINATE_ALL_SCRIPTS_WITH_THIS_NAME

This command is similar to SF_START_NEW_SCRIPT_FROM_LABEL, but the latter requires a label offset instead of a pointer

---

### `0C6C` SF_SET_SCRIPT_LOCAL_VARIABLE
Sets the values for a local variable in the specified script

**Class:** `SfScript.SetLVar`

**Input:**
- `self: SfScript`
- `varIndex: int`
- `value: any`

---

### `0C6D` SF_GET_SCRIPT_LOCAL_VARIABLE
Returns the value of a local variable in the specified script

**Class:** `SfScript.GetLVar`

**Input:**
- `self: SfScript`
- `varIndex: int`

**Output:**
- `value: any (variable)`

---

### `0C6E` SF_TERMINATE_SCRIPT
Terminates a script pointed by the address

**Class:** `SfScript.Terminate`
**Flags:** destructor

**Input:**
- `self: SfScript`

---

### `0C6F` SF_RESTART_SCRIPT
Restarts a script pointed by the address

**Class:** `SfScript.Restart`

**Input:**
- `self: SfScript`
- `passedValues: arguments`

**Details:**

Use this command with caution.
    * **Script** vs **Custom_Script** are two different types. Do not use any **Custom_Script** related commands inside the scriptLabel's body

The passedValues parameter are optional and can be used to set the initial values for the local variables of the new script. For example:
* `SF_RESTART_CUSTOM_SCRIPT {address} csPtr {passedValues} 100 13.42 0x42352 18@` will start the script with `0@ = 100`, `1@ = 13.42`, `2@ = 0x42352`, and `3@ = starter's 18@ value`.

To terminate a script started by this command, use any on the following depending on the circumstances:
* TERMINATE_THIS_SCRIPT
* SF_TERMINATE_SCRIPT or TERMINATE_SCRIPT
* TERMINATE_ALL_SCRIPTS_WITH_THIS_NAME

---

### SfTimer

### `0C74` SF_CREATE_TIMER
Creates and starts an SfTimer object that periodically executes its callback upon expiration

**Class:** `SfTimer.Create`
**Flags:** condition, constructor

**Input:**
- `interval: int`
- `callback: label`

**Output:**
- `handle: SfTimer (variable)`

**Details:**

* The handle parameter can be set to any constant value if the SfTimer object's handle isn't needed to be retrieved. Else, pass a variable to handle parameter:
  * `SF_CREATE_TIMER {interval} 500 {callback} @TimerCallback_DoSomething {handleTo} 0 // legacy syntax` creates an SfTimer **without** retrieving its handle
  * `5@ = SF_CREATE_TIMER {interval} 500 {callback} @TimerCallback_DoSomething` creates an SfTimer then stores the handle to **5@**
* The callback parameter must be an offset label. For example, **@TimerCallback_DoSomething**
* The callback label must contain the callback's body.
* Construct the callback's flow of execution with caution.
  * Like subroutines, callbacks uses the variable space of the script's main thread.
  * Callbacks have higher priority than the custom script's main thread. Meaning, eveytime the script encounters the **WAIT** command at the main thread, the script will execute all callbacks first(if interrupt flag was fired by a callback), then continues to execute the main thread's commands after where the **WAIT** command was encountered.
  * Avoid executing too much commands inside the callback. Doing so would lead to undersirable script behavior, like failing to detect interrupts from other registered callbacks or event handlers.
  * **WAIT** command inside a Callback **WILL NOT WORK!** Because callbacks are designed to finish as soon as possible.
  * All callbacks hooked by this command must use **SF_COMMAND_RETURN** command as returning statement, indicating the end of callback.

---

### `0C75` SF_DELETE_TIMER
Removes the specified SfTimer object, freeing it from memory

**Class:** `SfTimer.Delete`
**Flags:** condition, destructor

**Input:**
- `self: SfTimer`

---

### `0C76` SF_RESET_TIMER
Resets the expiration time of the SfTimer, restarting its trigger countdown

**Class:** `SfTimer.Reset`
**Flags:** condition

**Input:**
- `self: SfTimer`

---

### `0C77` SF_SET_TIMER_INTERVAL
Sets a new interval for the SfTimer

**Class:** `SfTimer.SetInterval`
**Flags:** condition

**Input:**
- `self: SfTimer`
- `interval: int`

---

### `0C78` SF_SET_TIMER_STATUS
Activates or pauses an SfTimer's functionality

**Class:** `SfTimer.SetStatus`
**Flags:** condition

**Input:**
- `self: SfTimer`
- `isActive: bool`

---

### `0C79` SF_IS_TIMER_ACTIVE
Evaluates as logical true if the SfTimer is active

**Class:** `SfTimer.IsActive`
**Flags:** condition

**Input:**
- `self: SfTimer`

---

### `0C7A` SF_GET_TIMER_INTERVAL
Returns the SfTimer's configured interval

**Class:** `SfTimer.GetInterval`
**Flags:** condition

**Input:**
- `self: SfTimer`

**Output:**
- `interval: int (variable)`

---

### `0C7B` SF_GET_TIMER_ELAPSED_TIME
Returns the number of milliseconds that have passed since the last SfTimer reset (including after the interval has passed)

**Class:** `SfTimer.GetElapsedTime`
**Flags:** condition

**Input:**
- `self: SfTimer`

**Output:**
- `elapsedTime: int (variable)`

**Details:**

The elapsed time computed by this command isn't affected by the Sftimer's current status. you might notice that the returned elapsed time value is still changing from time to time despite the SfTimer is currently paused.

---

### `0C7C` SF_GET_TIMER_TIME_LEFT
Returns the number of milliseconds remaining before the SfTimer expires (decremented if the timer is active)

**Class:** `SfTimer.GetTimeLeft`
**Flags:** condition

**Input:**
- `self: SfTimer`

**Output:**
- `timeLeft: int (variable)`

**Details:**

The time left computed by this command isn't affected by the Sftimer's current status. you might notice that the returned time left value is still changing from time to time despite the SfTimer is currently paused.

---

### `0C3B` SF_D3D_BEGIN
Begins the D3D primitiveType used for rendering

**Flags:** static

**Input:**
- `primitiveType: int`

---

### `0C3C` SF_D3D_END
Calls the D3D EndScene method


---

### `0C3D` SF_D3D_COLOR
Sets the D3D's current drawing color


**Input:**
- `color: int`

---

### `0C3E` SF_D3D_VERTEX
Sets a vertex using the currently used primitive type specified by SF_D3D_BEGIN


**Input:**
- `startVertex: int`
- `primitiveCount: int`

---

### `0C3F` SF_D3D_SET_TEXTURE_COORDS
Sets the Texture Coordinates of the D3D primitive


**Input:**
- `coordX: int`
- `coordY: int`

---

### `0C40` SF_D3D_BIND_TEXTURE
Binds a Texture to our D3D primitive

**Flags:** condition

**Input:**
- `textureObjAdress: int`

---

### `0C41` SF_D3D_TEXTURE_STRUCT
This command has no documention provided by the SF author

**Flags:** condition

**Input:**
- `unknown1: int`
- `unknown2: int`

---

### `0C42` SF_D3D_TEXTURE_SPRITE
This command has no documention provided by the SF author

**Flags:** condition

**Input:**
- `unknown1: int`
- `unknown2: int`

---

### `0C43` SF_D3D_GET_TEXTURE_SIZE
Returns the dimensions occupied by texture structure

**Flags:** condition

**Input:**
- `textureObjAdress: int`

**Output:**
- `width: int (variable)`
- `height: int (variable)`

---

### `0C44` SF_D3D_SET_RENDER_STATE
Sets the rendering status of a D3D primitiveType


**Input:**
- `primitiveType: int`
- `state: bool`

---
