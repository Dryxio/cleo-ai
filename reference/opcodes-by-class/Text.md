# Text Opcodes

> 59 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `00BA` | PRINT_BIG | Displays a styled message for the specified time |
| `00BB` | PRINT | Displays a message positioned on the bottom of the screen for the specified time |
| `00BC` | PRINT_NOW | Displays a message positioned on the bottom of the screen for the specified time |
| `00BE` | CLEAR_PRINTS | Clears all priority text and some styles of big texts |
| `01E3` | PRINT_WITH_NUMBER_BIG | Displays a styled message in which the first string token~1~ is substituted with |
| `01E4` | PRINT_WITH_NUMBER | Displays a styled message in which the first string token ~1~ is substituted wit |
| `01E5` | PRINT_WITH_NUMBER_NOW | Displays a styled message in which the first string token ~1~ is substituted wit |
| `0217` | PRINT_BIG_Q | Displays a low-priority styled message for the specified time |
| `02FD` | PRINT_WITH_2_NUMBERS_NOW | Displays a styled message in which the first two ~1~ tokens are substituted with |
| `02FF` | PRINT_WITH_3_NUMBERS | Displays a styled message in which the first three ~1~ tokens are substituted wi |
| `0302` | PRINT_WITH_4_NUMBERS | Displays a styled message in which the first four ~1~ tokens are substituted wit |
| `0303` | PRINT_WITH_4_NUMBERS_NOW | Displays a styled message in which the first four ~1~ tokens are substituted wit |
| `0308` | PRINT_WITH_6_NUMBERS | Displays a styled message in which the first six ~1~ tokens are substituted with |
| `033E` | DISPLAY_TEXT | Draws text at the specified on-screen position |
| `033F` | SET_TEXT_SCALE | Scales the width and height of the text letters |
| `0340` | SET_TEXT_COLOUR | Sets the color of the text letters |
| `0341` | SET_TEXT_JUSTIFY | Sets the text to be drawn justified, which means the text will wrap in order to  |
| `0342` | SET_TEXT_CENTRE | Centers the text |
| `0343` | SET_TEXT_WRAPX | Sets the line width of the text |
| `0344` | SET_TEXT_CENTRE_SIZE | Sets the line width of the centered text |
| `0345` | SET_TEXT_BACKGROUND | Gives the text a background (0346) |
| `0348` | SET_TEXT_PROPORTIONAL | Makes the text size proportionate |
| `0349` | SET_TEXT_FONT | Sets the text draw font |
| `036D` | PRINT_WITH_2_NUMBERS_BIG | Displays a styled message in which the first two ~1~ tokens are substituted with |
| `0384` | PRINT_STRING_IN_STRING_NOW | Displays a styled message in which the first string token ~a~ is substituted wit |
| `03D5` | CLEAR_THIS_PRINT | Removes the priority text from the screen |
| `03D6` | CLEAR_THIS_BIG_PRINT | Removes the styled text from the screen |
| `03E0` | SET_TEXT_DRAW_BEFORE_FADE | Causes the next text to be drawn before the fade is drawn |
| `03E4` | SET_TEXT_RIGHT_JUSTIFY | Sets the text draw to be aligned to the right |
| `03E5` | PRINT_HELP | Displays a black text box for a few seconds |
| `03E6` | CLEAR_HELP | Removes the text box from the screen |
| `03EB` | CLEAR_SMALL_PRINTS | Clears small messages from the screen |
| `03F0` | USE_TEXT_COMMANDS | Enables text and texture drawing |
| `045A` | DISPLAY_TEXT_WITH_NUMBER | Draws text with one number |
| `045B` | DISPLAY_TEXT_WITH_2_NUMBERS | Draws text with two numbers |
| `0512` | PRINT_HELP_FOREVER | Shows a text box which stays on screen until it is removed by another command |
| `0513` | PRINT_HELP_FOREVER_WITH_NUMBER | Shows a text box with one number |
| `054C` | LOAD_MISSION_TEXT | Makes the game use GXT Entries from the specified GXT Table |
| `060D` | SET_TEXT_DROPSHADOW | Sets shadow for the current text draw |
| `076F` | IS_MESSAGE_BEING_DISPLAYED | Returns true if a priority GXT string is displayed on screen |
| `07FC` | DISPLAY_TEXT_WITH_FLOAT | Converts the float to two separate numbers to use in a 2-numbered GXT entry, and |
| `081C` | SET_TEXT_EDGE | Adds an outline to the next text drawn using a text draw command |
| `0844` | IS_VAR_TEXT_LABEL_EMPTY | Returns true if the string is empty |
| `0845` | IS_LVAR_TEXT_LABEL_EMPTY | Returns true if the string is empty |
| `0846` | IS_VAR_TEXT_LABEL16_EMPTY | Returns true if the string is empty |
| `0847` | IS_LVAR_TEXT_LABEL16_EMPTY | Returns true if the string is empty |
| `08FE` | IS_HELP_MESSAGE_BEING_DISPLAYED | Returns true if any help message is being displayed |
| `0912` | SET_MESSAGE_FORMATTING | Overrides the position of the text on screen |
| `0989` | SET_HELP_MESSAGE_BOX_SIZE | Sets the global width of text boxes displayed on screen |
| `09A9` | GET_HASH_KEY | Returns the CRC hash of the input string |
| `09C1` | ADD_NEXT_MESSAGE_TO_PREVIOUS_BRIEFS | Sets whether the next text is added to the brief in the menu |
| `09FD` | GET_STRING_WIDTH | Gets the width of the GXT entry string |
| `0A08` | GET_STRING_WIDTH_WITH_NUMBER | Gets the width of the GXT entry string with the specified number |
| `0A0E` | CLEAR_THIS_PRINT_BIG_NOW | Removes the print big text with the specified style from the screen |
| `0A19` | SET_AREA_NAME | Displays the text of the specified GXT entry using San Andreas' area name text s |
| `0A2A` | IS_THIS_HELP_MESSAGE_BEING_DISPLAYED | Returns true if a help message with the specified GXT entry is being displayed |
| `0A2C` | DRAW_SUBTITLES_BEFORE_FADE | Sets whether the text stays on the screen when it fades out |
| `0A2D` | DRAW_ODDJOB_TITLE_BEFORE_FADE | Sets whether the styled text stays on the screen when it fades out |
| `0A44` | DISPLAY_NON_MINIGAME_HELP_MESSAGES | Overrides the text block set by 09BD |

## Detailed Reference

### `00BA` PRINT_BIG
Displays a styled message for the specified time

**Class:** `Text.PrintBig`
**Flags:** static

**Input:**
- `key: gxt_key`
- `time: int`
- `style: TextStyle`

---

### `00BB` PRINT
Displays a message positioned on the bottom of the screen for the specified time

**Class:** `Text.Print`
**Flags:** static

**Input:**
- `key: gxt_key`
- `time: int`
- `flag: int`

**Details:**

This command displays a subtitle message looked up by a **GXT key**. The message is appended to the end of the game's subtitle queue. It becomes visible only when all previously queued messages have expired, so it has **lower priority** than PRINT_NOW.

The internal buffer is 400 characters; text longer than 399 characters is silently truncated.

Use PRINT_STRING or PRINT_FORMATTED to display arbitrary text strings.

## Queueing behaviour

Messages are placed in a circular queue of 8 slots. Only the first slot (the current message) is visible on screen. Each subsequent message waits until the one before it expires.

If all 8 slots are occupied, the next message is silently discarded.

## Brief History

- The message is recorded in **Brief** (up to 20 entries) at the moment it becomes the current (visible) message.
- Duplicate text is silently ignored.
- To suppress a single message from **Brief**, call `ADD_NEXT_MESSAGE_TO_PREVIOUS_BRIEFS false` immediately before `PRINT`. The flag is consumed and restored to `true` by the command itself.

## Disabling Subtitles with ~z~

Any text starting with the `~z~` GXT prefix will be hidden from the view and the brief, when the option "Show Subtitles" is disabled in the game settings. It is mainly used for mission dialogue lines.

---

### `00BC` PRINT_NOW
Displays a message positioned on the bottom of the screen for the specified time

**Class:** `Text.PrintNow`
**Flags:** static

**Input:**
- `key: gxt_key`
- `time: int`
- `flag: int`

**Details:**

This command displays a subtitle message looked up by a **GXT key** with **immediate priority**. The message bypasses the queue and is placed at the front of the subtitle display, replacing whatever is currently shown.

The internal buffer is 400 characters; text longer than 399 characters is silently truncated.

Use PRINT_STRING_NOW or PRINT_FORMATTED_NOW to display arbitrary text strings with immediate priority. 

## Priority model

Unlike PRINT, this opcode clears any queued messages and places the new message at the front (slot 0) for immediate display. Use this variant when the subtitle must be seen immediately, regardless of what else may be in the queue.

## Brief History

- The message is recorded in **Brief** (up to 20 entries) **immediately**.
- Duplicate text is silently ignored.
- To suppress a single message from **Brief**, call `ADD_NEXT_MESSAGE_TO_PREVIOUS_BRIEFS false` immediately before `PRINT_NOW`. The flag is consumed and restored to `true` by the command itself.

## Disabling Subtitles with ~z~

Any text starting with the `~z~` GXT prefix will be hidden from the view and the brief, when the option "Show Subtitles" is disabled in the game settings. It is mainly used for mission dialogue lines.

---

### `00BE` CLEAR_PRINTS
Clears all priority text and some styles of big texts

**Class:** `Text.ClearPrints`
**Flags:** static

---

### `01E3` PRINT_WITH_NUMBER_BIG
Displays a styled message in which the first string token~1~ is substituted with the specified number

**Class:** `Text.PrintWithNumberBig`
**Flags:** static

**Input:**
- `key: gxt_key`
- `num: int`
- `duration: int`
- `style: TextStyle`

---

### `01E4` PRINT_WITH_NUMBER
Displays a styled message in which the first string token ~1~ is substituted with the specified number

**Class:** `Text.PrintWithNumber`
**Flags:** static

**Input:**
- `key: gxt_key`
- `num: int`
- `duration: int`
- `flag: int`

---

### `01E5` PRINT_WITH_NUMBER_NOW
Displays a styled message in which the first string token ~1~ is substituted with the specified number

**Class:** `Text.PrintWithNumberNow`
**Flags:** static

**Input:**
- `key: gxt_key`
- `num: int`
- `duration: int`
- `flag: int`

---

### `0217` PRINT_BIG_Q
Displays a low-priority styled message for the specified time

**Class:** `Text.PrintBigQ`
**Flags:** static

**Input:**
- `key: gxt_key`
- `duration: int`
- `style: TextStyle`

---

### `02FD` PRINT_WITH_2_NUMBERS_NOW
Displays a styled message in which the first two ~1~ tokens are substituted with the specified numbers

**Class:** `Text.PrintWith2NumbersNow`
**Flags:** static

**Input:**
- `key: gxt_key`
- `num1: int`
- `num2: int`
- `duration: int`
- `style: TextStyle`

---

### `02FF` PRINT_WITH_3_NUMBERS
Displays a styled message in which the first three ~1~ tokens are substituted with the specified numbers

**Class:** `Text.PrintWith3Numbers`
**Flags:** static

**Input:**
- `key: gxt_key`
- `num1: int`
- `num2: int`
- `num3: int`
- `duration: int`
- `style: TextStyle`

---

### `0302` PRINT_WITH_4_NUMBERS
Displays a styled message in which the first four ~1~ tokens are substituted with the specified numbers

**Class:** `Text.PrintWith4Numbers`
**Flags:** static

**Input:**
- `key: gxt_key`
- `num1: int`
- `num2: int`
- `num3: int`
- `num4: int`
- `duration: int`
- `style: TextStyle`

---

### `0303` PRINT_WITH_4_NUMBERS_NOW
Displays a styled message in which the first four ~1~ tokens are substituted with the specified numbers

**Class:** `Text.PrintWith4NumbersNow`
**Flags:** static

**Input:**
- `key: gxt_key`
- `num1: int`
- `num2: int`
- `num3: int`
- `num4: int`
- `duration: int`
- `style: TextStyle`

---

### `0308` PRINT_WITH_6_NUMBERS
Displays a styled message in which the first six ~1~ tokens are substituted with the specified numbers

**Class:** `Text.PrintWith6Numbers`
**Flags:** static

**Input:**
- `key: gxt_key`
- `num1: int`
- `num2: int`
- `num3: int`
- `num4: int`
- `num5: int`
- `num6: int`
- `duration: int`
- `style: TextStyle`

---

### `033E` DISPLAY_TEXT
Draws text at the specified on-screen position

**Class:** `Text.Display`
**Flags:** static

**Input:**
- `offsetLeft: float`
- `offsetTop: float`
- `key: gxt_key`

---

### `033F` SET_TEXT_SCALE
Scales the width and height of the text letters

**Class:** `Text.SetScale`
**Flags:** static

**Input:**
- `widthScale: float`
- `heightScale: float`

---

### `0340` SET_TEXT_COLOUR
Sets the color of the text letters

**Class:** `Text.SetColor`
**Flags:** static

**Input:**
- `red: int`
- `green: int`
- `blue: int`
- `alpha: int`

---

### `0341` SET_TEXT_JUSTIFY
Sets the text to be drawn justified, which means the text will wrap in order to fill an even rectangle of space

**Class:** `Text.SetJustify`
**Flags:** static

**Input:**
- `state: bool`

---

### `0342` SET_TEXT_CENTRE
Centers the text

**Class:** `Text.SetCenter`
**Flags:** static

**Input:**
- `state: bool`

---

### `0343` SET_TEXT_WRAPX
Sets the line width of the text

**Class:** `Text.SetWrapX`
**Flags:** static

**Input:**
- `width: float`

---

### `0344` SET_TEXT_CENTRE_SIZE
Sets the line width of the centered text

**Class:** `Text.SetCenterSize`
**Flags:** static

**Input:**
- `width: float`

---

### `0345` SET_TEXT_BACKGROUND
Gives the text a background (0346)

**Class:** `Text.SetBackground`
**Flags:** static

**Input:**
- `state: bool`

---

### `0348` SET_TEXT_PROPORTIONAL
Makes the text size proportionate

**Class:** `Text.SetProportional`
**Flags:** static

**Input:**
- `state: bool`

---

### `0349` SET_TEXT_FONT
Sets the text draw font

**Class:** `Text.SetFont`
**Flags:** static

**Input:**
- `font: Font`

---

### `036D` PRINT_WITH_2_NUMBERS_BIG
Displays a styled message in which the first two ~1~ tokens are substituted with the specified numbers

**Class:** `Text.PrintWith2NumbersBig`
**Flags:** static

**Input:**
- `key: gxt_key`
- `num1: int`
- `num2: int`
- `duration: int`
- `style: TextStyle`

---

### `0384` PRINT_STRING_IN_STRING_NOW
Displays a styled message in which the first string token ~a~ is substituted with the specified text

**Class:** `Text.PrintStringInStringNow`
**Flags:** static

**Input:**
- `templateKey: gxt_key`
- `replacementKey: gxt_key`
- `duration: int`
- `style: TextStyle`

---

### `03D5` CLEAR_THIS_PRINT
Removes the priority text from the screen

**Class:** `Text.ClearThisPrint`
**Flags:** static

**Input:**
- `key: gxt_key`

---

### `03D6` CLEAR_THIS_BIG_PRINT
Removes the styled text from the screen

**Class:** `Text.ClearThisBigPrint`
**Flags:** static

**Input:**
- `key: gxt_key`

---

### `03E0` SET_TEXT_DRAW_BEFORE_FADE
Causes the next text to be drawn before the fade is drawn

**Class:** `Text.SetDrawBeforeFade`
**Flags:** static

**Input:**
- `state: bool`

---

### `03E4` SET_TEXT_RIGHT_JUSTIFY
Sets the text draw to be aligned to the right

**Class:** `Text.SetRightJustify`
**Flags:** static

**Input:**
- `state: bool`

---

### `03E5` PRINT_HELP
Displays a black text box for a few seconds

**Class:** `Text.PrintHelp`
**Flags:** static

**Input:**
- `key: gxt_key`

**Details:**

This command prints a help message. It will generate a sound effect and display for a few seconds before fading away. Use CLEAR_HELP to immediately remove the help message. SET_HELP_MESSAGE_BOX_SIZE can set the width of the message box. Help messages cannot be seen while widescreen is switched on. In the German version, the font size is smaller than other versions.

---

### `03E6` CLEAR_HELP
Removes the text box from the screen

**Class:** `Text.ClearHelp`
**Flags:** static

---

### `03EB` CLEAR_SMALL_PRINTS
Clears small messages from the screen

**Class:** `Text.ClearSmallPrints`
**Flags:** static

---

### `03F0` USE_TEXT_COMMANDS
Enables text and texture drawing

**Class:** `Text.UseCommands`
**Flags:** static

**Input:**
- `state: bool`

---

### `045A` DISPLAY_TEXT_WITH_NUMBER
Draws text with one number

**Class:** `Text.DisplayWithNumber`
**Flags:** static

**Input:**
- `offsetLeft: float`
- `offsetTop: float`
- `key: gxt_key`
- `num: int`

---

### `045B` DISPLAY_TEXT_WITH_2_NUMBERS
Draws text with two numbers

**Class:** `Text.DisplayWith2Numbers`
**Flags:** static

**Input:**
- `offsetLeft: float`
- `offsetTop: float`
- `key: gxt_key`
- `num1: int`
- `num2: int`

---

### `0512` PRINT_HELP_FOREVER
Shows a text box which stays on screen until it is removed by another command

**Class:** `Text.PrintHelpForever`
**Flags:** static

**Input:**
- `key: gxt_key`

---

### `0513` PRINT_HELP_FOREVER_WITH_NUMBER
Shows a text box with one number

**Class:** `Text.PrintHelpForeverWithNumber`
**Flags:** static

**Input:**
- `gxt: gxt_key`
- `number: int`

---

### `054C` LOAD_MISSION_TEXT
Makes the game use GXT Entries from the specified GXT Table

**Class:** `Text.LoadMissionText`
**Flags:** static

**Input:**
- `tableName: string`

---

### `060D` SET_TEXT_DROPSHADOW
Sets shadow for the current text draw

**Class:** `Text.SetDropshadow`
**Flags:** static

**Input:**
- `intensity: int`
- `red: int`
- `green: int`
- `blue: int`
- `alpha: int`

---

### `076F` IS_MESSAGE_BEING_DISPLAYED
Returns true if a priority GXT string is displayed on screen

**Class:** `Text.IsMessageBeingDisplayed`
**Flags:** condition, static

---

### `07FC` DISPLAY_TEXT_WITH_FLOAT
Converts the float to two separate numbers to use in a 2-numbered GXT entry, and draws the text

**Class:** `Text.DisplayWithFloat`
**Flags:** static

**Input:**
- `leftTopX: float`
- `leftTopY: float`
- `key: gxt_key`
- `value: float`
- `precision: int`

---

### `081C` SET_TEXT_EDGE
Adds an outline to the next text drawn using a text draw command

**Class:** `Text.SetEdge`
**Flags:** static

**Input:**
- `size: int`
- `red: int`
- `green: int`
- `blue: int`
- `alpha: int`

---

### `0844` IS_VAR_TEXT_LABEL_EMPTY
Returns true if the string is empty

**Class:** `Text.IsEmpty`
**Flags:** condition, static

**Input:**
- `text: string (global var)`

**Details:**

This conditional command returns true if the string represented by the global variable is empty, i.e. contains no characters, only zero bytes. 

IS_LVAR_TEXT_LABEL_EMPTY, IS_VAR_TEXT_LABEL16_EMPTY, and IS_LVAR_TEXT_LABEL16_EMPTY behave similarly to this command.

---

### `0845` IS_LVAR_TEXT_LABEL_EMPTY
Returns true if the string is empty

**Class:** `Text.IsEmpty`
**Flags:** condition, static

**Input:**
- `text: string (local var)`

---

### `0846` IS_VAR_TEXT_LABEL16_EMPTY
Returns true if the string is empty

**Class:** `Text.IsEmpty`
**Flags:** condition, static

**Input:**
- `text: string (global var)`

---

### `0847` IS_LVAR_TEXT_LABEL16_EMPTY
Returns true if the string is empty

**Class:** `Text.IsEmpty`
**Flags:** condition, static

**Input:**
- `text: string (local var)`

---

### `08FE` IS_HELP_MESSAGE_BEING_DISPLAYED
Returns true if any help message is being displayed

**Class:** `Text.IsHelpMessageBeingDisplayed`
**Flags:** condition, static

---

### `0912` SET_MESSAGE_FORMATTING
Overrides the position of the text on screen

**Class:** `Text.SetMessageFormatting`
**Flags:** static

**Input:**
- `customPosition: bool`
- `margin: int`
- `width: int`

---

### `0989` SET_HELP_MESSAGE_BOX_SIZE
Sets the global width of text boxes displayed on screen

**Class:** `Text.SetHelpMessageBoxSize`
**Flags:** static

**Input:**
- `size: int`

---

### `09A9` GET_HASH_KEY
Returns the CRC hash of the input string

**Class:** `Text.GetHashKey`
**Flags:** static

**Input:**
- `text: string`

**Output:**
- `hash: int (variable)`

**Details:**

The hashing algorithm used here is called JAMCRC - a variation of the standard CRC32 algorithm where bits of the final result are not inverted. Read more here: https://gtamods.com/wiki/Cryptography#CRC32

The input string is automatically converted to uppercase. The hashing stops at the first null byte.

---

### `09C1` ADD_NEXT_MESSAGE_TO_PREVIOUS_BRIEFS
Sets whether the next text is added to the brief in the menu

**Class:** `Text.AddNextMessageToPreviousBriefs`
**Flags:** static

**Input:**
- `state: bool`

---

### `09FD` GET_STRING_WIDTH
Gets the width of the GXT entry string

**Class:** `Text.GetStringWidth`
**Flags:** static

**Input:**
- `entry: gxt_key`

**Output:**
- `width: int (variable)`

---

### `0A08` GET_STRING_WIDTH_WITH_NUMBER
Gets the width of the GXT entry string with the specified number

**Class:** `Text.GetStringWidthWithNumber`
**Flags:** static

**Input:**
- `gxtEntry: gxt_key`
- `number: any`

**Output:**
- `width: int (variable)`

---

### `0A0E` CLEAR_THIS_PRINT_BIG_NOW
Removes the print big text with the specified style from the screen

**Class:** `Text.ClearThisPrintBigNow`
**Flags:** static

**Input:**
- `textStyle: TextStyle`

---

### `0A19` SET_AREA_NAME
Displays the text of the specified GXT entry using San Andreas' area name text style

**Class:** `Text.SetAreaName`
**Flags:** static

**Input:**
- `name: string`

---

### `0A2A` IS_THIS_HELP_MESSAGE_BEING_DISPLAYED
Returns true if a help message with the specified GXT entry is being displayed

**Class:** `Text.IsThisHelpMessageBeingDisplayed`
**Flags:** condition, static

**Input:**
- `gxt: gxt_key`

---

### `0A2C` DRAW_SUBTITLES_BEFORE_FADE
Sets whether the text stays on the screen when it fades out

**Class:** `Text.DrawSubtitlesBeforeFade`
**Flags:** static

**Input:**
- `state: bool`

---

### `0A2D` DRAW_ODDJOB_TITLE_BEFORE_FADE
Sets whether the styled text stays on the screen when it fades out

**Class:** `Text.DrawOddjobTitleBeforeFade`
**Flags:** static

**Input:**
- `state: bool`

---

### `0A44` DISPLAY_NON_MINIGAME_HELP_MESSAGES
Overrides the text block set by 09BD

**Class:** `Text.DisplayNonMinigameHelpMessages`
**Flags:** static

**Input:**
- `state: bool`

---
