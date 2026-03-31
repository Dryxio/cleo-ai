# imgui Extension Opcodes

> 87 opcodes

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `2200` | IMGUI_BEGIN_FRAME | Creates a unique frame with its own space in memory. Must be enclosed with IMGUI |
| `2201` | IMGUI_END_FRAME | Ends unique ImGui frame created with IMGUI_BEGIN_FRAME |
| `2202` | IMGUI_BEGIN | Creates the window |
| `2203` | IMGUI_END | Ends the window |
| `2204` | IMGUI_BEGIN_MAINMENUBAR | Creates the main menu bar |
| `2205` | IMGUI_END_MAINMENUBAR | Ends the main menu bar |
| `2206` | IMGUI_BEGIN_CHILD | Creates a child window widget inside the main window |
| `2207` | IMGUI_END_CHILD | Ends the child window widget created with 0C25 |
| `2208` | IMGUI_TABS | Pass tab names separated by comma. Returns the index of the visible tab |
| `2209` | IMGUI_COLLAPSING_HEADER | Adds the collapsing header |
| `220A` | IMGUI_SET_WINDOW_POS | Sets the current window position. Must be called inside Begin()...End() |
| `220B` | IMGUI_SET_WINDOW_SIZE | Sets the current window size. Must be called inside Begin()...End() |
| `220C` | IMGUI_SET_NEXT_WINDOW_POS | Sets the current window position. Applies to the next window ( aka Begin() ) |
| `220D` | IMGUI_SET_NEXT_WINDOW_SIZE | Sets the current window size. Applies to the next window ( aka Begin() ) |
| `220E` | IMGUI_TEXT | Creates the text line |
| `220F` | IMGUI_TEXT_CENTERED | Displays a center aligned ImGui text widget |
| `2210` | IMGUI_TEXT_DISABLED | Creates the text line with the disabled color ( Grayish by default ) |
| `2211` | IMGUI_TEXT_WRAPPED | Creates the text line that wraps to a newline if the text goes beyond the window |
| `2212` | IMGUI_TEXT_COLORED | Creates the text line of the given RGBA color (0.0f-1.0f) |
| `2213` | IMGUI_BULLET_TEXT | Creates the text line with a bullet point |
| `2214` | IMGUI_BULLET | Creates a bullet point |
| `2215` | IMGUI_CHECKBOX | Creates the checkbox |
| `2216` | IMGUI_COMBO | Creates a combo box widget. Pass options separated by commas "item1,item2,item3" |
| `2217` | IMGUI_SET_TOOLTIP | Creates the popup window with the given text |
| `2218` | IMGUI_BUTTON | Creates the button |
| `2219` | IMGUI_IMAGE_BUTTON | Creates a ImGui button with specified image |
| `221A` | IMGUI_INVISIBLE_BUTTON | Creates the invisible button |
| `221B` | IMGUI_COLOR_BUTTON | Creates the button with custom colors |
| `221C` | IMGUI_ARROW_BUTTON | Creates the arrow button in the specified direction |
| `221D` | IMGUI_SLIDER_INT | Creates the int slider input |
| `221E` | IMGUI_SLIDER_FLOAT | Creates the float slider input |
| `221F` | IMGUI_INPUT_INT | Creates the int input |
| `2220` | IMGUI_INPUT_FLOAT | Creates the float input |
| `2221` | IMGUI_INPUT_TEXT | Creates the text input |
| `2222` | IMGUI_RADIO_BUTTON | Creates the radio button |
| `2223` | IMGUI_COLOR_PICKER | Creates the color picker and sets the default color (0-255) |
| `2224` | IMGUI_MENU_ITEM | Adds the menu item |
| `2225` | IMGUI_SELECTABLE | Adds the selectable widget |
| `2226` | IMGUI_DUMMY | Creates the dummy widget. Used for spacing |
| `2227` | IMGUI_SAMELINE | Appends the next widget to the same line as the previous widget |
| `2228` | IMGUI_NEWLINE | Creates a new line for the next widget |
| `2229` | IMGUI_COLUMNS | Divides the window width into N columns. Close this with Columns(1) |
| `222A` | IMGUI_NEXT_COLUMN | Puts the next widgets on the next column. Used alongside 0C16 |
| `222B` | IMGUI_SPACING | Adds some spacing after the previous widget |
| `222C` | IMGUI_SEPARATOR | Adds a horizontal separator line |
| `222D` | IMGUI_PUSH_ITEM_WIDTH | Sets the item width for the next widgets |
| `222E` | IMGUI_POP_ITEM_WIDTH | Removes the pushed item width (0C27) from the stack |
| `222F` | IMGUI_IS_ITEM_ACTIVE | Returns true if the previous widget is in active state |
| `2230` | IMGUI_IS_ITEM_CLICKED | Returns true if the previous widget is clicked |
| `2231` | IMGUI_IS_ITEM_FOCUSED | Returns true if the previous widget is focused |
| `2232` | IMGUI_IS_ITEM_HOVERED | Returns true if the previous widget is hovered with mouse |
| `2233` | IMGUI_SET_ITEM_INT | Sets the value of input int & slider int widget |
| `2234` | IMGUI_SET_ITEM_FLOAT | Sets the value of input float & slider float widget |
| `2235` | IMGUI_SET_ITEM_TEXT | Sets value of input text widget |
| `2236` | IMGUI_SET_IMAGE_BG_COLOR | Sets image background color |
| `2237` | IMGUI_SET_IMAGE_TINT_COLOR | Sets image tint color |
| `2238` | IMGUI_LOAD_IMAGE | Loads a image file from disk. Relative to CLEO directory |
| `2239` | IMGUI_FREE_IMAGE | Frees a loaded image data |
| `223A` | IMGUI_PUSH_STYLE_VAR | Pushes a ImGuiStyleVar value to the stack. Use PopStyleVar to undo the effect |
| `223B` | IMGUI_PUSH_STYLE_VAR2 | Pushes a ImGuiStyleVar value to the stack. Use PopStyleVar to undo the effect |
| `223C` | IMGUI_PUSH_STYLE_COLOR | Pushes a ImGuiCol value to the stack. Use PopStyleColor to undo the effect |
| `223D` | IMGUI_POP_STYLE_VAR | Removes the recent imGuiStyleVar from the stack |
| `223E` | IMGUI_POP_STYLE_COLOR | Removes the recent ImGuiCol from the stack |
| `223F` | IMGUI_GET_FOREGROUND_DRAWLIST | Returns pointer to foreground draw list |
| `2240` | IMGUI_GET_BACKGROUND_DRAWLIST | Returns pointer to ImGui background drawlist |
| `2241` | IMGUI_GET_WINDOW_DRAWLIST | Returns pointer to ImGui window drawList |
| `2242` | IMGUI_DRAWLIST_ADD_TEXT | Adds text at specified position |
| `2243` | IMGUI_DRAWLIST_ADD_LINE | Adds a line form point A to B |
| `2244` | GET_FRAMERATE | Returns game FPS |
| `2245` | IMGUI_GET_VERSION | Returns the ImGui version |
| `2246` | IMGUI_GET_PLUGIN_VERSION | Returns the ImGuiRedux version |
| `2247` | IMGUI_SET_CURSOR_VISIBLE | Toggles the cursor |
| `2248` | IMGUI_GET_FRAME_HEIGHT | Returns the ImGui frame height |
| `2249` | IMGUI_GET_WINDOW_POS | Returns the x,y coordinates of the window on the screen |
| `224A` | IMGUI_GET_WINDOW_SIZE | Returns the width and height of the window |
| `224B` | IMGUI_CALC_TEXT_SIZE | Returns the width and height of the given text |
| `224C` | IMGUI_GET_WINDOW_CONTENT_REGION_WIDTH | Returns the content region width of the window |
| `224D` | IMGUI_GET_SCALING_SIZE | Returns the width and height scaling factor based on the window size |
| `224E` | IMGUI_GET_DISPLAY_SIZE | Returns the width & height of the display |
| `224F` | IMGUI_SET_NEXT_WINDOW_TRANSPARENCY | Sets the background transparency of next window (0.0f-1.0f) |
| `2250` | IMGUI_SET_MESSAGE | Displays a text message on top left corner of the screen. Useful for games witho |
| `2251` | IMGUI_SET_COLUMN_WIDTH | Sets the width of the column |
| `2252` | IMGUI_BEGIN_CHILDEX | Creates a child window widget inside the main window |
| `2253` | IMGUI_BEGIN_DISABLED | Disables ImGui widgets inside this block |
| `2254` | IMGUI_END_DISABLED | Closes the ImGui disable block |
| `2255` | IMGUI_BEGIN_MENU | Begins a ImGui menu block |
| `2256` | IMGUI_END_MENU | Ends a ImGui menu block |

## Detailed Reference

### Game

### `2244` GET_FRAMERATE
Returns game FPS

**Class:** `Game.GetFramerate`
**Flags:** static

**Output:**
- `fps: int (variable)`

---

### ImGui

### `2200` IMGUI_BEGIN_FRAME
Creates a unique frame with its own space in memory. Must be enclosed with IMGUI_END_FRAME

**Class:** `ImGui.BeginFrame`
**Flags:** static

**Input:**
- `uniqueId: string`

---

### `2201` IMGUI_END_FRAME
Ends unique ImGui frame created with IMGUI_BEGIN_FRAME

**Class:** `ImGui.EndFrame`
**Flags:** static

---

### `2202` IMGUI_BEGIN
Creates the window

**Class:** `ImGui.Begin`
**Flags:** static

**Input:**
- `windowName: string`
- `state: bool`
- `noTitleBar: bool`
- `noResize: bool`
- `noMove: bool`
- `autoResize: bool`

**Output:**
- `state: bool (variable)`

---

### `2203` IMGUI_END
Ends the window

**Class:** `ImGui.End`
**Flags:** static

---

### `2204` IMGUI_BEGIN_MAINMENUBAR
Creates the main menu bar

**Class:** `ImGui.BeginMainMenuBar`
**Flags:** static

**Input:**
- `uniqueId: string`

---

### `2205` IMGUI_END_MAINMENUBAR
Ends the main menu bar

**Class:** `ImGui.EndMainMenuBar`
**Flags:** static

---

### `2206` IMGUI_BEGIN_CHILD
Creates a child window widget inside the main window

**Class:** `ImGui.BeginChild`
**Flags:** static

**Input:**
- `uniqueId: string`

---

### `2207` IMGUI_END_CHILD
Ends the child window widget created with 0C25

**Class:** `ImGui.EndChild`
**Flags:** static

---

### `2208` IMGUI_TABS
Pass tab names separated by comma. Returns the index of the visible tab

**Class:** `ImGui.Tabs`
**Flags:** static

**Input:**
- `name: string`
- `tabNames: string`

**Output:**
- `index: int (variable)`

---

### `2209` IMGUI_COLLAPSING_HEADER
Adds the collapsing header

**Class:** `ImGui.CollapsingHeader`
**Flags:** static, condition

**Input:**
- `label: string`

---

### `220A` IMGUI_SET_WINDOW_POS
Sets the current window position. Must be called inside Begin()...End()

**Class:** `ImGui.SetWindowPos`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `imGuiCond: ImGuiCond`

---

### `220B` IMGUI_SET_WINDOW_SIZE
Sets the current window size. Must be called inside Begin()...End()

**Class:** `ImGui.SetWindowSize`
**Flags:** static

**Input:**
- `width: float`
- `height: float`
- `imGuiCond: ImGuiCond`

---

### `220C` IMGUI_SET_NEXT_WINDOW_POS
Sets the current window position. Applies to the next window ( aka Begin() )

**Class:** `ImGui.SetNextWindowPos`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `imGuiCond: ImGuiCond`

---

### `220D` IMGUI_SET_NEXT_WINDOW_SIZE
Sets the current window size. Applies to the next window ( aka Begin() )

**Class:** `ImGui.SetNextWindowSize`
**Flags:** static

**Input:**
- `width: float`
- `height: float`
- `imGuiCond: ImGuiCond`

---

### `220E` IMGUI_TEXT
Creates the text line

**Class:** `ImGui.Text`
**Flags:** static

**Input:**
- `text: string`

---

### `220F` IMGUI_TEXT_CENTERED
Displays a center aligned ImGui text widget

**Class:** `ImGui.TextCentered`
**Flags:** static

**Input:**
- `text: string`

---

### `2210` IMGUI_TEXT_DISABLED
Creates the text line with the disabled color ( Grayish by default )

**Class:** `ImGui.TextDisabled`
**Flags:** static

**Input:**
- `text: string`

---

### `2211` IMGUI_TEXT_WRAPPED
Creates the text line that wraps to a newline if the text goes beyond the window width

**Class:** `ImGui.TextWrapped`
**Flags:** static

**Input:**
- `text: string`

---

### `2212` IMGUI_TEXT_COLORED
Creates the text line of the given RGBA color (0.0f-1.0f)

**Class:** `ImGui.TextColored`
**Flags:** static

**Input:**
- `text: string`
- `red: float`
- `green: float`
- `blue: float`
- `alpha: float`

---

### `2213` IMGUI_BULLET_TEXT
Creates the text line with a bullet point

**Class:** `ImGui.TextWithBullet`
**Flags:** static

**Input:**
- `text: string`

---

### `2214` IMGUI_BULLET
Creates a bullet point

**Class:** `ImGui.Bullet`
**Flags:** static

---

### `2215` IMGUI_CHECKBOX
Creates the checkbox

**Class:** `ImGui.Checkbox`
**Flags:** static

**Input:**
- `label: string`
- `isChecked: bool`

**Output:**
- `state: bool (variable)`

---

### `2216` IMGUI_COMBO
Creates a combo box widget. Pass options separated by commas "item1,item2,item3"

**Class:** `ImGui.ComboBox`
**Flags:** static

**Input:**
- `name: string`
- `options: string`
- `selection: int`

**Output:**
- `selected: int (variable)`

---

### `2217` IMGUI_SET_TOOLTIP
Creates the popup window with the given text

**Class:** `ImGui.SetTooltip`
**Flags:** static

**Input:**
- `text: string`

---

### `2218` IMGUI_BUTTON
Creates the button

**Class:** `ImGui.Button`
**Flags:** static, condition

**Input:**
- `buttonName: string`
- `width: float`
- `height: float`

---

### `2219` IMGUI_IMAGE_BUTTON
Creates a ImGui button with specified image

**Class:** `ImGui.ButtonImage`
**Flags:** static, condition

**Input:**
- `name: string`
- `image: int`
- `width: float`
- `height: float`

---

### `221A` IMGUI_INVISIBLE_BUTTON
Creates the invisible button

**Class:** `ImGui.ButtonInvisible`
**Flags:** static, condition

**Input:**
- `buttonName: string`
- `width: float`
- `height: float`

---

### `221B` IMGUI_COLOR_BUTTON
Creates the button with custom colors

**Class:** `ImGui.ButtonColored`
**Flags:** static, condition

**Input:**
- `buttonName: string`
- `red: float`
- `green: float`
- `blue: float`
- `alpha: float`
- `width: float`
- `height: float`

---

### `221C` IMGUI_ARROW_BUTTON
Creates the arrow button in the specified direction

**Class:** `ImGui.ButtonArrow`
**Flags:** static, condition

**Input:**
- `name: string`
- `imGuiDir: ImGuiDir`

---

### `221D` IMGUI_SLIDER_INT
Creates the int slider input

**Class:** `ImGui.SliderInt`
**Flags:** static

**Input:**
- `label: string`
- `initValue: int`
- `min: int`
- `max: int`

**Output:**
- `val: int (variable)`

---

### `221E` IMGUI_SLIDER_FLOAT
Creates the float slider input

**Class:** `ImGui.SliderFloat`
**Flags:** static

**Input:**
- `label: string`
- `initValue: float`
- `min: float`
- `max: float`

**Output:**
- `val: float (variable)`

---

### `221F` IMGUI_INPUT_INT
Creates the int input

**Class:** `ImGui.InputInt`
**Flags:** static

**Input:**
- `label: string`
- `initValue: int`
- `min: int`
- `max: int`

**Output:**
- `val: int (variable)`

---

### `2220` IMGUI_INPUT_FLOAT
Creates the float input

**Class:** `ImGui.InputFloat`
**Flags:** static

**Input:**
- `label: string`
- `initValue: float`
- `min: float`
- `max: float`

**Output:**
- `val: float (variable)`

---

### `2221` IMGUI_INPUT_TEXT
Creates the text input

**Class:** `ImGui.InputText`
**Flags:** static

**Input:**
- `label: string`

**Output:**
- `text: string (variable)`

---

### `2222` IMGUI_RADIO_BUTTON
Creates the radio button

**Class:** `ImGui.RadioButton`
**Flags:** static

**Input:**
- `label: string`
- `selectedBtn: int`
- `btnNo: int`

**Output:**
- `val: int (variable)`

---

### `2223` IMGUI_COLOR_PICKER
Creates the color picker and sets the default color (0-255)

**Class:** `ImGui.ColorPicker`
**Flags:** static

**Input:**
- `label: string`

**Output:**
- `red: int (variable)`
- `green: int (variable)`
- `blue: int (variable)`
- `alpha: int (variable)`

---

### `2224` IMGUI_MENU_ITEM
Adds the menu item

**Class:** `ImGui.MenuItem`
**Flags:** static, condition

**Input:**
- `text: string`
- `selected: bool`
- `enabled: bool`

---

### `2225` IMGUI_SELECTABLE
Adds the selectable widget

**Class:** `ImGui.Selectable`
**Flags:** static, condition

**Input:**
- `text: string`
- `selected: bool`

---

### `2226` IMGUI_DUMMY
Creates the dummy widget. Used for spacing

**Class:** `ImGui.Dummy`
**Flags:** static

**Input:**
- `width: float`
- `height: float`

---

### `2227` IMGUI_SAMELINE
Appends the next widget to the same line as the previous widget

**Class:** `ImGui.SameLine`
**Flags:** static

---

### `2228` IMGUI_NEWLINE
Creates a new line for the next widget

**Class:** `ImGui.NewLine`
**Flags:** static

---

### `2229` IMGUI_COLUMNS
Divides the window width into N columns. Close this with Columns(1)

**Class:** `ImGui.Columns`
**Flags:** static

**Input:**
- `count: int`

---

### `222A` IMGUI_NEXT_COLUMN
Puts the next widgets on the next column. Used alongside 0C16

**Class:** `ImGui.NextColumn`
**Flags:** static

---

### `222B` IMGUI_SPACING
Adds some spacing after the previous widget

**Class:** `ImGui.Spacing`
**Flags:** static

---

### `222C` IMGUI_SEPARATOR
Adds a horizontal separator line

**Class:** `ImGui.Separator`
**Flags:** static

---

### `222D` IMGUI_PUSH_ITEM_WIDTH
Sets the item width for the next widgets

**Class:** `ImGui.PushItemWidth`
**Flags:** static

**Input:**
- `width: float`

---

### `222E` IMGUI_POP_ITEM_WIDTH
Removes the pushed item width (0C27) from the stack

**Class:** `ImGui.PopItemWidth`
**Flags:** static

---

### `222F` IMGUI_IS_ITEM_ACTIVE
Returns true if the previous widget is in active state

**Class:** `ImGui.IsItemActive`
**Flags:** static, condition

**Input:**
- `uniqueId: string`

---

### `2230` IMGUI_IS_ITEM_CLICKED
Returns true if the previous widget is clicked

**Class:** `ImGui.IsItemClicked`
**Flags:** static, condition

**Input:**
- `uniqueId: string`

---

### `2231` IMGUI_IS_ITEM_FOCUSED
Returns true if the previous widget is focused

**Class:** `ImGui.IsItemFocused`
**Flags:** static, condition

**Input:**
- `uniqueId: string`

---

### `2232` IMGUI_IS_ITEM_HOVERED
Returns true if the previous widget is hovered with mouse

**Class:** `ImGui.IsItemHovered`
**Flags:** static, condition

**Input:**
- `uniqueId: string`

---

### `2233` IMGUI_SET_ITEM_INT
Sets the value of input int & slider int widget

**Class:** `ImGui.SetItemValueInt`
**Flags:** static

**Input:**
- `id: string`
- `val: int`

---

### `2234` IMGUI_SET_ITEM_FLOAT
Sets the value of input float & slider float widget

**Class:** `ImGui.SetItemValueFloat`
**Flags:** static

**Input:**
- `id: string`
- `val: float`

---

### `2235` IMGUI_SET_ITEM_TEXT
Sets value of input text widget

**Class:** `ImGui.SetItemValueText`
**Flags:** static

**Input:**
- `id: string`
- `val: string`

---

### `2236` IMGUI_SET_IMAGE_BG_COLOR
Sets image background color

**Class:** `ImGui.SetImageBgColor`
**Flags:** static

**Input:**
- `r: float`
- `g: float`
- `b: float`
- `a: float`

---

### `2237` IMGUI_SET_IMAGE_TINT_COLOR
Sets image tint color

**Class:** `ImGui.SetImageTintColor`
**Flags:** static

**Input:**
- `r: float`
- `g: float`
- `b: float`
- `a: float`

---

### `2238` IMGUI_LOAD_IMAGE
Loads a image file from disk. Relative to CLEO directory

**Class:** `ImGui.LoadImage`
**Flags:** static

**Input:**
- `path: string`

**Output:**
- `image: int (variable)`

---

### `2239` IMGUI_FREE_IMAGE
Frees a loaded image data

**Class:** `ImGui.FreeImage`
**Flags:** static

**Input:**
- `image: int`

---

### `223A` IMGUI_PUSH_STYLE_VAR
Pushes a ImGuiStyleVar value to the stack. Use PopStyleVar to undo the effect

**Class:** `ImGui.PushStyleVar`
**Flags:** static

**Input:**
- `imGuiStyleVar: ImGuiStyleVar`
- `val: float`

---

### `223B` IMGUI_PUSH_STYLE_VAR2
Pushes a ImGuiStyleVar value to the stack. Use PopStyleVar to undo the effect

**Class:** `ImGui.PushStyleVar2`
**Flags:** static

**Input:**
- `imGuiStyleVar: ImGuiStyleVar`
- `x: float`
- `y: float`

---

### `223C` IMGUI_PUSH_STYLE_COLOR
Pushes a ImGuiCol value to the stack. Use PopStyleColor to undo the effect

**Class:** `ImGui.PushStyleColor`
**Flags:** static

**Input:**
- `imGuiCol: ImGuiCol`
- `r: int`
- `g: int`
- `b: int`
- `a: int`

---

### `223D` IMGUI_POP_STYLE_VAR
Removes the recent imGuiStyleVar from the stack

**Class:** `ImGui.PopStyleVar`
**Flags:** static

**Input:**
- `count: int`

---

### `223E` IMGUI_POP_STYLE_COLOR
Removes the recent ImGuiCol from the stack

**Class:** `ImGui.PopStyleColor`
**Flags:** static

**Input:**
- `count: int`

---

### `223F` IMGUI_GET_FOREGROUND_DRAWLIST
Returns pointer to foreground draw list

**Class:** `ImGui.GetForegroundDrawList`
**Flags:** static

**Output:**
- `drawList: int (variable)`

---

### `2240` IMGUI_GET_BACKGROUND_DRAWLIST
Returns pointer to ImGui background drawlist

**Class:** `ImGui.GetBackgroundDrawList`
**Flags:** static

**Output:**
- `drawList: int (variable)`

---

### `2241` IMGUI_GET_WINDOW_DRAWLIST
Returns pointer to ImGui window drawList

**Class:** `ImGui.GetWindowDrawlist`
**Flags:** static

**Output:**
- `drawList: int (variable)`

---

### `2242` IMGUI_DRAWLIST_ADD_TEXT
Adds text at specified position

**Class:** `ImGui.AddText`
**Flags:** static

**Input:**
- `drawList: int`
- `posX: float`
- `posY: float`
- `r: int`
- `g: int`
- `b: int`
- `a: int`
- `text: string`

---

### `2243` IMGUI_DRAWLIST_ADD_LINE
Adds a line form point A to B

**Class:** `ImGui.AddLine`
**Flags:** static

**Input:**
- `drawList: int`
- `p1X: float`
- `p1Y: float`
- `p2X: float`
- `p2Y: float`
- `r: int`
- `g: int`
- `b: int`
- `a: int`
- `thickness: float`

---

### `2245` IMGUI_GET_VERSION
Returns the ImGui version

**Class:** `ImGui.GetVersion`
**Flags:** static

**Output:**
- `version: int (variable)`

---

### `2246` IMGUI_GET_PLUGIN_VERSION
Returns the ImGuiRedux version

**Class:** `ImGui.GetPluginVersion`
**Flags:** static

**Output:**
- `version: int (variable)`

---

### `2247` IMGUI_SET_CURSOR_VISIBLE
Toggles the cursor

**Class:** `ImGui.SetCursorVisible`
**Flags:** static

**Input:**
- `show: bool`

---

### `2248` IMGUI_GET_FRAME_HEIGHT
Returns the ImGui frame height

**Class:** `ImGui.GetFrameHeight`
**Flags:** static

**Output:**
- `height: float (variable)`

---

### `2249` IMGUI_GET_WINDOW_POS
Returns the x,y coordinates of the window on the screen

**Class:** `ImGui.GetWindowPos`
**Flags:** static

**Input:**
- `uniqueId: string`

**Output:**
- `x: float (variable)`
- `y: float (variable)`

---

### `224A` IMGUI_GET_WINDOW_SIZE
Returns the width and height of the window

**Class:** `ImGui.GetWindowSize`
**Flags:** static

**Input:**
- `uniqueId: string`

**Output:**
- `width: float (variable)`
- `height: float (variable)`

---

### `224B` IMGUI_CALC_TEXT_SIZE
Returns the width and height of the given text

**Class:** `ImGui.CalcTextSize`
**Flags:** static

**Input:**
- `text: string`

**Output:**
- `width: float (variable)`
- `height: float (variable)`

---

### `224C` IMGUI_GET_WINDOW_CONTENT_REGION_WIDTH
Returns the content region width of the window

**Class:** `ImGui.GetWindowContentRegionWidth`
**Flags:** static

**Input:**
- `uniqueId: string`

**Output:**
- `width: float (variable)`

---

### `224D` IMGUI_GET_SCALING_SIZE
Returns the width and height scaling factor based on the window size

**Class:** `ImGui.GetScalingSize`
**Flags:** static

**Input:**
- `uniqueId: string`
- `count: int`
- `spacing: bool`

**Output:**
- `x: float (variable)`
- `y: float (variable)`

---

### `224E` IMGUI_GET_DISPLAY_SIZE
Returns the width & height of the display

**Class:** `ImGui.GetDisplaySize`
**Flags:** static

**Output:**
- `width: float (variable)`
- `height: float (variable)`

---

### `224F` IMGUI_SET_NEXT_WINDOW_TRANSPARENCY
Sets the background transparency of next window (0.0f-1.0f)

**Class:** `ImGui.SetNextWindowTransparency`
**Flags:** static

**Input:**
- `alpha: float`

---

### `2250` IMGUI_SET_MESSAGE
Displays a text message on top left corner of the screen. Useful for games without `showTextBox(...)` support

**Class:** `ImGui.SetMessage`
**Flags:** static

**Input:**
- `text: string`

---

### `2251` IMGUI_SET_COLUMN_WIDTH
Sets the width of the column

**Class:** `ImGui.SetColumnWidth`
**Flags:** static

**Input:**
- `index: int`
- `width: float`

---

### `2252` IMGUI_BEGIN_CHILDEX
Creates a child window widget inside the main window

**Class:** `ImGui.BeginChildEx`
**Flags:** static

**Input:**
- `uniqueId: string`
- `width: float`
- `height: float`
- `border: bool`
- `flags: int`

---

### `2253` IMGUI_BEGIN_DISABLED
Disables ImGui widgets inside this block

**Class:** `ImGui.BeginDisabled`
**Flags:** static

**Input:**
- `disabled: bool`

---

### `2254` IMGUI_END_DISABLED
Closes the ImGui disable block

**Class:** `ImGui.EndDisabled`
**Flags:** static

---

### `2255` IMGUI_BEGIN_MENU
Begins a ImGui menu block

**Class:** `ImGui.BeginMenu`
**Flags:** static, condition

**Input:**
- `label: string`
- `enabled: bool`

---

### `2256` IMGUI_END_MENU
Ends a ImGui menu block

**Class:** `ImGui.EndMenu`
**Flags:** static

---
