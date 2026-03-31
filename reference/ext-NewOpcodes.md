# NewOpcodes Extension Opcodes

> 115 opcodes

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0D00` | MULTIPLY_MATRICES | Multiplies matrices |
| `0D01` | ROTATE_MATRIX_ON_AXIS | Rotates matrix on axis |
| `0D02` | GET_MATRIX_X_ANGLE | Gets the X angle of matrix (in degrees) |
| `0D03` | GET_MATRIX_Y_ANGLE | Gets the Y angle of matrix (in degrees) |
| `0D04` | GET_MATRIX_Z_ANGLE | Gets the Z angle of matrix (in degrees) |
| `0D05` | SET_MATRIX_POSITION | Sets position for matrix |
| `0D06` | GET_MATRIX_POSITION | Gets position of matrix |
| `0D07` | GET_COORDS_OFFSETS_RELATIVE_TO_MATRIX | Gets point relative offset on matrix |
| `0D08` | SET_MATRIX_ROTATION | Sets matrix angles |
| `0D09` | COPY_MATRIX | Copies matrix to another matrix |
| `0D0A` | GET_OFFSET_FROM_MATRIX_IN_WORLD_COORDS | Gets coords on offset from matrix |
| `0D0B` | GET_CHAR_BONE_MATRIX | Gets char's bone world matrix |
| `0D0C` | GET_CAR_COMPONENT_MATRIX | Gets matrix of car component |
| `0D0D` | GET_CAR_COMPONENT | Gets car component by name |
| `0D0E` | SET_CAR_COMPONENT_STATE | Sets component state |
| `0D0F` | SET_CAR_MODEL_ALPHA | Sets alpha value for car's model |
| `0D10` | SET_CHAR_MODEL_ALPHA | Sets alpha value for char's model |
| `0D11` | SET_OBJECT_MODEL_ALPHA | Sets alpha value for object's model |
| `0D12` | SET_CAR_COMPONENT_MODEL_ALPHA | Sets alpha value for car's component model |
| `0D13` | SET_MATRIX_X_ROTATION | Sets matrix x angle |
| `0D14` | SET_MATRIX_Y_ROTATION | Sets matrix y angle |
| `0D15` | SET_MATRIX_Z_ROTATION | Sets matrix z angle |
| `0D16` | SET_MATRIX_ROTATION_FROM_QUAT | Sets matrix rotation from quaternion |
| `0D17` | SET_QUAT_FROM_MATRIX | Sets quaternion from matrix |
| `0D18` | ROTATE_QUAT_ON_AXIS | Rotates quaternion |
| `0D19` | GET_NORMALISED_QUAT | Normalizes quaternion |
| `0D1A` | MULTIPLY_QUATS | Multiplies quaternions |
| `0D1B` | GET_ENTITY_TYPE_AND_CLASS | Gets information about entity type |
| `0D1C` | NORMALISE_VECTOR | Normalizes vector |
| `0D1D` | INTERPOLATE_MATRIX | Performs matrix slerp |
| `0D1E` | QUAT_SLERP | Performs quaternion slerp |
| `0D1F` | GET_COMPONENT_CHILD_COMPONENT | Gets component child component |
| `0D20` | GET_COMPONENT_NEXT_COMPONENT | Gets component next component |
| `0D21` | GET_COMPONENT_NAME | Gets component name component |
| `0D22` | GET_COMPONENT_WORLD_MATRIX | Gets component world matrix |
| `0D23` | GET_COMPONENT_MODELLING_MATRIX | Gets component modelling matrix |
| `0D24` | INITIALISE_QUAT | Sets quaternion elements |
| `0D25` | INITIALISE_MATRIX | Sets matrix elements |
| `0D26` | INITIALISE_VECTOR | Sets vector elements |
| `0D27` | MEMCPY | Copies block of memory |
| `0D28` | GET_VECTOR_ELEMENTS | Gets vector elements |
| `0D29` | GET_QUAT_ELEMENTS | Gets quaternion elements |
| `0D2A` | GET_CAR_NUM_COLLIDED_ENTITIES | Gets car number of collided entities |
| `0D2B` | GET_CHAR_NUM_COLLIDED_ENTITIES | Gets char number of collided entities |
| `0D2C` | GET_OBJECT_NUM_COLLIDED_ENTITIES | Gets object number of collided entities |
| `0D2D` | GET_LOCAL_TIME | Gets current time from OS |
| `0D2E` | SET_THREAD_VAR | Sets value of thread's local variable |
| `0D2F` | GET_THREAD_VAR | Gets value of thread's local variable |
| `0D30` | GET_CHAR_BONE | Gets char's bone |
| `0D31` | GET_BONE_OFFSET | Gets bone offset |
| `0D32` | GET_BONE_QUAT | Returns pointer to the quaterion under bone address obtained with GET_CHAR_BONE |
| `0D33` | SET_CAR_DOOR_WINDOW_STATE | Sets car window state |
| `0D34` | GET_CAR_COLLIDED_ENTITIES | Stores car collided entities |
| `0D35` | GET_CHAR_COLLIDED_ENTITIES | Stores char collided entities |
| `0D36` | GET_OBJECT_COLLIDED_ENTITIES | Stores object collided entities |
| `0D37` | SET_STRUCT_PARAM | Sets struct with 4b alignment param value |
| `0D38` | GET_STRUCT_PARAM | Gets struct with 4b alignment param value |
| `0D39` | GET_CHAR_MAX_HEALTH | Gets char max health value |
| `0D3A` | GET_COLLISION_BETWEEN_POINTS | Gets collision data between two points |
| `0D3B` | GET_COL_DATA_NORMAL_VECTOR | Gets colpoint normal vector |
| `0D3C` | GET_COL_DATA_SURFACE | Gets colpoint data surface ID |
| `0D3D` | GET_COL_DATA_LIGHTING | Gets colpoint data lighting value |
| `0D3E` | GET_COL_DATA_DEPTH | Gets colpoint data depth value |
| `0D3F` | FIND_INTERSECTION_BETWEEN_CIRCLES | Finds intersection coordinates between two circles |
| `0D40` | DRAW_SHAPE | Draws 2D shape |
| `0D41` | SETUP_SHAPE_VERTEX | Sets vertex params |
| `0D42` | LOAD_TXD | Loads txd from file |
| `0D43` | GET_TXD_ID | Gets txd's id |
| `0D44` | FIND_TEXTURE_IN_TXD_WITH_NAME | Finds texture in txd |
| `0D45` | ROTATE_SHAPE_VERTICES | Rotates vertices of 2D shape around point |
| `0D46` | FIND_TEXTURE_IN_TXD_WITH_ID | Finds texture in txd |
| `0D47` | GET_MODEL_TXD_ID | Gets txd's id for model |
| `0D48` | GET_MODEL_CRC | Gets model's CRC32 key |
| `0D49` | STRING_CMP | Compares two strings |
| `0D4A` | STRING_CAT | Concatenates two strings |
| `0D4B` | STRING_STR | Finds the first occurrence of a string |
| `0D4C` | STRING_LEN | Gets string length |
| `0D4D` | STRING_CPY | Copies string to another string |
| `0D4E` | GET_STRUCT_FIELD | Gets value at struct offset |
| `0D4F` | SET_STRUCT_FIELD | Sets value at struct offset |
| `0D50` | DRAW_TEMPORARY_SHADOW | Draws shadow |
| `0D51` | DRAW_PERMANENT_SHADOW | Draws permanent shadow |
| `0D52` | DRAW_TEMPORARY_LIGHT | Draws light |
| `0D53` | DRAW_TEMPORARY_CORONA | Draws corona |
| `0D54` | DRAW_TEMPORARY_CORONA_EX | Draws corona with some extra parameters |
| `0D55` | GET_SUN_COLORS | Gets sun colors |
| `0D56` | GET_SUN_SCREEN_COORS | Gets sun 2D position |
| `0D57` | GET_SUN_WORLD_COORS | Gets sun 3D position |
| `0D58` | GET_SUN_SIZE | Gets sun size |
| `0D59` | GET_CURRENT_WEATHER | Gets current weather |
| `0D5A` | GET_TRAFFICLIGHTS_CURRENT_COLOR | Gets trafficlight colors |
| `0D5B` | DRAW_SPOTLIGHT | Draws spotlight |
| `0D5C` | GET_CAR_LIGHT_DAMAGE_STATUS | Gets car light damaging state |
| `0D5D` | SET_CAR_LIGHT_DAMAGE_STATUS | Sets car light damaging state |
| `0D5E` | GET_VEHICLE_CLASS_AND_SUBCLASS | Gets vehicle class and subclass |
| `0D5F` | GET_VEHICLE_DUMMY_POSN | Gets vehicle dummy position |
| `0D60` | CREATE_PROJECTILE | Creates projectile |
| `0D61` | LOAD_TEXTURE_FROM_BMP_FILE | Loads texture from BMP file. Can be used with texture memory option to load file |
| `0D64` | LOAD_TEXTURE_FROM_PNG_FILE | Loads texture from PNG file. Can be used with texturememory option to load file  |
| `0D65` | PRINT_TEMPORARY_TEXT | Prints a text into display ("light" version) |
| `0D66` | PRINT_TEMPORARY_TEXT_EX | Prints a text into display |
| `0D72` | GET_GAME_VOLUME | Gets game sfx and radio volume |
| `0D73` | GET_SCREEN_WIDTH_AND_HEIGHT | Gets screen width and height |
| `0D74` | GET_COMPONENT_PARENT_COMPONENT | Gets component parent component |
| `0D75` | GET_COMPONENT_NUM_OBJECTS | Gets component number of objects |
| `0D76` | GET_COMPONENT_OBJECT | Gets component object |
| `0D77` | HIDE_OBJECT_ATOMIC | Hides object atomic |
| `0D78` | GET_OBJECT_ATOMIC_FLAG | Gets object atomic flag |
| `0D79` | SET_OBJECT_ATOMIC_FLAG | Sets object atomic flag |
| `0D7A` | GET_OBJECT_ATOMIC_NUM_MATERIALS | Gets object atomic material texture |
| `0D7B` | GET_OBJECT_ATOMIC_MATERIAL_TEXTURE | Gets object atomic material texture |
| `0D7C` | LOAD_TEXTURE_FROM_DDS_FILE | Loads texture from DDS file |
| `0D7D` | CLEAN_LOADED_TEXTURE | Cleans loaded texture |
| `0D7E` | DRAW_2D_SPRITE | Draws 2D sprite |
| `0D7F` | DRAW_2D_SPRITE_WITH_GRADIENT | Draws 2D sprite with gradient |

## Detailed Reference

### Car

### `0D0C` GET_CAR_COMPONENT_MATRIX
Gets matrix of car component

**Class:** `Car.GetComponentMatrix`
**Flags:** condition

**Input:**
- `self: Car`
- `componentName: string`

**Output:**
- `handle: Matrix (variable)`

---

### `0D0D` GET_CAR_COMPONENT
Gets car component by name

**Class:** `Car.GetComponent`
**Flags:** condition

**Input:**
- `self: Car`
- `name: string`

**Output:**
- `handle: Component (variable)`

---

### `0D12` SET_CAR_COMPONENT_MODEL_ALPHA
Sets alpha value for car's component model

**Class:** `Car.SetComponentModelAlpha`
**Flags:** condition

**Input:**
- `self: Car`
- `componentName: string`
- `alpha: int`

---

### Component

### `0D1F` GET_COMPONENT_CHILD_COMPONENT
Gets component child component

**Class:** `Component.GetChildComponent`

**Input:**
- `self: Component`

**Output:**
- `child: Component (variable)`

---

### `0D20` GET_COMPONENT_NEXT_COMPONENT
Gets component next component

**Class:** `Component.GetNextComponent`

**Input:**
- `self: Component`

**Output:**
- `nextComponent: Component (variable)`

---

### `0D21` GET_COMPONENT_NAME
Gets component name component

**Class:** `Component.GetName`

**Input:**
- `self: Component`

**Output:**
- `name: string (variable)`

---

### `0D22` GET_COMPONENT_WORLD_MATRIX
Gets component world matrix

**Class:** `Component.GetWorldMatrix`

**Input:**
- `self: Component`

**Output:**
- `worldMatrix: any (variable)`

---

### `0D23` GET_COMPONENT_MODELLING_MATRIX
Gets component modelling matrix

**Class:** `Component.GetModellingMatrix`

**Input:**
- `self: Component`

**Output:**
- `modellingMatrix: any (variable)`

---

### `0D74` GET_COMPONENT_PARENT_COMPONENT
Gets component parent component

**Class:** `Component.GetParentComponent`

**Input:**
- `self: Component`

**Output:**
- `parentComponent: Component (variable)`

---

### `0D75` GET_COMPONENT_NUM_OBJECTS
Gets component number of objects

**Class:** `Component.GetNumObjects`

**Input:**
- `self: Component`

**Output:**
- `numObjects: int (variable)`

---

### Matrix

### `0D00` MULTIPLY_MATRICES
Multiplies matrices

**Class:** `Matrix.Multiply`
**Flags:** constructor, static

**Input:**
- `matrixA: Matrix`
- `matrixB: Matrix`

**Output:**
- `handle: Matrix (variable)`

---

### `0D01` ROTATE_MATRIX_ON_AXIS
Rotates matrix on axis

**Class:** `Matrix.RotateOnAxis`

**Input:**
- `self: Matrix`
- `axisX: float`
- `axisY: float`
- `axisZ: float`
- `angle: float`
- `combineOp: RwCombine`

---

### `0D02` GET_MATRIX_X_ANGLE
Gets the X angle of matrix (in degrees)

**Class:** `Matrix.GetXAngle`

**Input:**
- `self: Matrix`

**Output:**
- `xAngle: float (variable)`

---

### `0D03` GET_MATRIX_Y_ANGLE
Gets the Y angle of matrix (in degrees)

**Class:** `Matrix.GetYAngle`

**Input:**
- `self: Matrix`

**Output:**
- `yAngle: float (variable)`

---

### `0D04` GET_MATRIX_Z_ANGLE
Gets the Z angle of matrix (in degrees)

**Class:** `Matrix.GetZAngle`

**Input:**
- `self: Matrix`

**Output:**
- `zAngle: float (variable)`

---

### `0D05` SET_MATRIX_POSITION
Sets position for matrix

**Class:** `Matrix.SetPosition`

**Input:**
- `self: Matrix`
- `x: float`
- `y: float`
- `z: float`

---

### `0D08` SET_MATRIX_ROTATION
Sets matrix angles

**Class:** `Matrix.Rotate`

**Input:**
- `self: Matrix`
- `x: float`
- `y: float`
- `z: float`

---

### `0D09` COPY_MATRIX
Copies matrix to another matrix

**Class:** `Matrix.Copy`

**Input:**
- `self: Matrix`
- `destination: Matrix`

---

### `0D0A` GET_OFFSET_FROM_MATRIX_IN_WORLD_COORDS
Gets coords on offset from matrix

**Class:** `Matrix.GetOffset`

**Input:**
- `self: Matrix`
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### Sprite

### `0D7E` DRAW_2D_SPRITE
Draws 2D sprite

**Class:** `Sprite.Draw2D`
**Flags:** static

**Input:**
- `texture: int`
- `cornerAx: float`
- `cornerAy: float`
- `cornerBx: float`
- `cornerBy: float`
- `red: int`
- `blue: int`
- `green: int`
- `aplha: int`
- `angle: float`

---

### `0D7F` DRAW_2D_SPRITE_WITH_GRADIENT
Draws 2D sprite with gradient

**Class:** `Sprite.Draw2DWithGradient`
**Flags:** static

**Input:**
- `texture: int`
- `cornerAx: float`
- `cornerAy: float`
- `cornerBx: float`
- `cornerBy: float`
- `red0: int`
- `green0: int`
- `blue0: int`
- `alpha0: int`
- `red1: int`
- `green1: int`
- `blue1: int`
- `alpha1: int`
- `red2: int`
- `green2: int`
- `blue2: int`
- `alpha2: int`
- `red3: int`
- `green3: int`
- `blue3: int`
- `alpha3: int`
- `angle: float`

---

### Texture

### `0D61` LOAD_TEXTURE_FROM_BMP_FILE
Loads texture from BMP file. Can be used with texture memory option to load file from memory

**Class:** `Texture.LoadFromBmpFile`
**Flags:** condition, static

**Input:**
- `bmp: string`
- `mask: string`

**Output:**
- `texture: any (variable)`

---

### `0D64` LOAD_TEXTURE_FROM_PNG_FILE
Loads texture from PNG file. Can be used with texturememory option to load file from memory

**Class:** `Texture.LoadFromPngFile`
**Flags:** condition, static

**Input:**
- `png: string`

**Output:**
- `texture: any (variable)`

---

### `0D7C` LOAD_TEXTURE_FROM_DDS_FILE
Loads texture from DDS file

**Class:** `Texture.LoadFromDdsFile`
**Flags:** static, condition

**Input:**
- `dds: string`

**Output:**
- `texture: any (variable)`

---

### `0D7D` CLEAN_LOADED_TEXTURE
Cleans loaded texture

**Class:** `Texture.CleanLoaded`

**Input:**
- `self: Texture`

---

### `0D06` GET_MATRIX_POSITION
Gets position of matrix


**Input:**
- `matrix: Matrix`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0D07` GET_COORDS_OFFSETS_RELATIVE_TO_MATRIX
Gets point relative offset on matrix

**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `matrix: Matrix`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0D0B` GET_CHAR_BONE_MATRIX
Gets char's bone world matrix

**Flags:** condition

**Input:**
- `char: Char`
- `bone: PedBone`

**Output:**
- `matrix: any (variable)`

---

### `0D0E` SET_CAR_COMPONENT_STATE
Sets component state

**Flags:** condition

**Input:**
- `car: Car`
- `component: string`
- `state: ComponentStates`

---

### `0D0F` SET_CAR_MODEL_ALPHA
Sets alpha value for car's model

**Flags:** condition

**Input:**
- `car: Car`
- `alpha: int`

---

### `0D10` SET_CHAR_MODEL_ALPHA
Sets alpha value for char's model

**Flags:** condition

**Input:**
- `char: Char`
- `alpha: int`

---

### `0D11` SET_OBJECT_MODEL_ALPHA
Sets alpha value for object's model

**Flags:** condition

**Input:**
- `object: Object`
- `alpha: any`

---

### `0D13` SET_MATRIX_X_ROTATION
Sets matrix x angle


**Input:**
- `matrix: any`
- `angle: float`

---

### `0D14` SET_MATRIX_Y_ROTATION
Sets matrix y angle


**Input:**
- `matrix: any`
- `angle: float`

---

### `0D15` SET_MATRIX_Z_ROTATION
Sets matrix z angle


**Input:**
- `matrix: any`
- `angle: float`

---

### `0D16` SET_MATRIX_ROTATION_FROM_QUAT
Sets matrix rotation from quaternion


**Input:**
- `matrix: any`
- `quat: any`

---

### `0D17` SET_QUAT_FROM_MATRIX
Sets quaternion from matrix


**Input:**
- `matrix: any`
- `quat: any`

---

### `0D18` ROTATE_QUAT_ON_AXIS
Rotates quaternion


**Input:**
- `quat: any`
- `x: float`
- `y: float`
- `z: float`
- `angle: float`
- `combineOp: RwCombine`

---

### `0D19` GET_NORMALISED_QUAT
Normalizes quaternion


**Input:**
- `quat: any`

**Output:**
- `quat: any (variable)`

---

### `0D1A` MULTIPLY_QUATS
Multiplies quaternions


**Input:**
- `quat1: any`
- `quat2: any`

**Output:**
- `quat: any (variable)`

---

### `0D1B` GET_ENTITY_TYPE_AND_CLASS
Gets information about entity type


**Input:**
- `entity: any`

**Output:**
- `type: EntityTypes (variable)`
- `class: EntityClasses (variable)`

---

### `0D1C` NORMALISE_VECTOR
Normalizes vector


**Input:**
- `vector: any`

---

### `0D1D` INTERPOLATE_MATRIX
Performs matrix slerp


**Input:**
- `slerp: any`
- `matrix1: any`
- `matrix2: any`
- `t: float`

---

### `0D1E` QUAT_SLERP
Performs quaternion slerp


**Input:**
- `quatSlerp: any`
- `fromQuat: any`
- `toQuat: any`
- `t: float`

---

### `0D24` INITIALISE_QUAT
Sets quaternion elements


**Input:**
- `quat: any`
- `x: float`
- `y: float`
- `z: float`
- `angle: float`

---

### `0D25` INITIALISE_MATRIX
Sets matrix elements


**Input:**
- `matrix: any`
- `a: float`
- `b: float`
- `c: float`
- `d: int`
- `e: float`
- `f: float`
- `g: float`
- `h: int`
- `i: float`
- `j: float`
- `k: float`
- `l: int`
- `m: float`
- `n: float`
- `o: float`
- `p: int`

---

### `0D26` INITIALISE_VECTOR
Sets vector elements


**Input:**
- `vector: any`
- `x: float`
- `y: float`
- `z: float`

---

### `0D27` MEMCPY
Copies block of memory


**Input:**
- `source: any`
- `destination: any`
- `size: int`

---

### `0D28` GET_VECTOR_ELEMENTS
Gets vector elements


**Input:**
- `vector: any`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0D29` GET_QUAT_ELEMENTS
Gets quaternion elements


**Input:**
- `quat: any`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`
- `angle: float (variable)`

---

### `0D2A` GET_CAR_NUM_COLLIDED_ENTITIES
Gets car number of collided entities


**Input:**
- `car: Car`

**Output:**
- `numCollidedEntities: int (variable)`

---

### `0D2B` GET_CHAR_NUM_COLLIDED_ENTITIES
Gets char number of collided entities


**Input:**
- `char: Char`

**Output:**
- `numCollidedEntities: int (variable)`

---

### `0D2C` GET_OBJECT_NUM_COLLIDED_ENTITIES
Gets object number of collided entities


**Input:**
- `object: Object`

**Output:**
- `numCollidedEntities: any (variable)`

---

### `0D2D` GET_LOCAL_TIME
Gets current time from OS


**Output:**
- `year: any (variable)`
- `month: any (variable)`
- `dayOfWeek: any (variable)`
- `day: any (variable)`
- `hour: any (variable)`
- `minute: any (variable)`
- `second: any (variable)`
- `milliseconds: any (variable)`

---

### `0D2E` SET_THREAD_VAR
Sets value of thread's local variable


**Input:**
- `thread: any`
- `var: int`
- `value: any`

---

### `0D2F` GET_THREAD_VAR
Gets value of thread's local variable


**Input:**
- `thread: any`
- `var: int`

**Output:**
- `result: any (variable)`

---

### `0D30` GET_CHAR_BONE
Gets char's bone

**Flags:** condition

**Input:**
- `char: Char`
- `bone: PedBone`

**Output:**
- `bone: PedBone (variable)`

---

### `0D31` GET_BONE_OFFSET
Gets bone offset


**Input:**
- `bone: any`

**Output:**
- `offsetVector: any (variable)`

---

### `0D32` GET_BONE_QUAT
Returns pointer to the quaterion under bone address obtained with GET_CHAR_BONE


**Input:**
- `bone: int`

**Output:**
- `quat: int (variable)`

---

### `0D33` SET_CAR_DOOR_WINDOW_STATE
Sets car window state


**Input:**
- `car: Car`
- `door: VehicleDoors`
- `windowState: WeaponState`

---

### `0D34` GET_CAR_COLLIDED_ENTITIES
Stores car collided entities


**Input:**
- `car: Car`

**Output:**
- `entity0: int (variable)`
- `entity1: int (variable)`
- `entity2: int (variable)`
- `entity3: int (variable)`
- `entity4: int (variable)`
- `entity5: int (variable)`

---

### `0D35` GET_CHAR_COLLIDED_ENTITIES
Stores char collided entities


**Input:**
- `char: Char`

**Output:**
- `entity0: int (variable)`
- `entity1: int (variable)`
- `entity2: int (variable)`
- `entity3: int (variable)`
- `entity4: int (variable)`
- `entity5: int (variable)`

---

### `0D36` GET_OBJECT_COLLIDED_ENTITIES
Stores object collided entities


**Input:**
- `object: Object`

**Output:**
- `entity0: int (variable)`
- `entity1: int (variable)`
- `entity2: int (variable)`
- `entity3: int (variable)`
- `entity4: int (variable)`
- `entity5: int (variable)`

---

### `0D37` SET_STRUCT_PARAM
Sets struct with 4b alignment param value


**Input:**
- `struct: int`
- `param: int`
- `value: any`

---

### `0D38` GET_STRUCT_PARAM
Gets struct with 4b alignment param value


**Input:**
- `struc: int`
- `param: int`

**Output:**
- `value: any (variable)`

---

### `0D39` GET_CHAR_MAX_HEALTH
Gets char max health value


**Input:**
- `char: Char`

**Output:**
- `maxHealth: float (variable)`

---

### `0D3A` GET_COLLISION_BETWEEN_POINTS
Gets collision data between two points


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
- `colPoint: any (variable)`
- `outX: float (variable)`
- `outY: float (variable)`
- `outZ: float (variable)`
- `entity: float (variable)`

---

### `0D3B` GET_COL_DATA_NORMAL_VECTOR
Gets colpoint normal vector


**Input:**
- `colPoint: any`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0D3C` GET_COL_DATA_SURFACE
Gets colpoint data surface ID


**Input:**
- `colpoint: any`

**Output:**
- `surface: SurfaceType (variable)`

---

### `0D3D` GET_COL_DATA_LIGHTING
Gets colpoint data lighting value


**Input:**
- `colPoint: any`

**Output:**
- `lighting: int (variable)`

---

### `0D3E` GET_COL_DATA_DEPTH
Gets colpoint data depth value


**Input:**
- `colPoint: any`

**Output:**
- `depth: float (variable)`

---

### `0D3F` FIND_INTERSECTION_BETWEEN_CIRCLES
Finds intersection coordinates between two circles

**Flags:** condition

**Input:**
- `x1: float`
- `y1: float`
- `r1: float`
- `x2: float`
- `y2: float`
- `r2: float`

**Output:**
- `p1X: float (variable)`
- `p1Y: float (variable)`
- `p2X: float (variable)`
- `p2Y: float (variable)`

---

### `0D40` DRAW_SHAPE
Draws 2D shape


**Input:**
- `type: int`
- `texture: int`
- `numVerts: int`
- `pVerts: int`
- `vertexAlpha: int`
- `srcBlend: BlendValues`
- `dstBlend: BlendValues`
- `unused: int`

---

### `0D41` SETUP_SHAPE_VERTEX
Sets vertex params


**Input:**
- `shape: any`
- `vertex: int`
- `x: float`
- `y: float`
- `z: float`
- `rhw: float`
- `r: int`
- `g: int`
- `b: int`
- `a: int`
- `u: float`
- `v: float`
- `invertX: bool`
- `invertY: bool`

---

### `0D42` LOAD_TXD
Loads txd from file

**Flags:** condition

**Input:**
- `txd: string`
- `path: string`

---

### `0D43` GET_TXD_ID
Gets txd's id


**Input:**
- `txd: string`

**Output:**
- `id: int (variable)`

---

### `0D44` FIND_TEXTURE_IN_TXD_WITH_NAME
Finds texture in txd

**Flags:** condition

**Input:**
- `texture: string`
- `dictionary: string`

**Output:**
- `texture: int (variable)`

---

### `0D45` ROTATE_SHAPE_VERTICES
Rotates vertices of 2D shape around point


**Input:**
- `shape: any`
- `numVerts: int`
- `x: float`
- `y: float`
- `angle: float`

---

### `0D46` FIND_TEXTURE_IN_TXD_WITH_ID
Finds texture in txd

**Flags:** condition

**Input:**
- `texture: string`
- `dictionary: int`

**Output:**
- `texture: int (variable)`

---

### `0D47` GET_MODEL_TXD_ID
Gets txd's id for model

**Flags:** condition

**Input:**
- `model: model_any`

**Output:**
- `txdId: int (variable)`

---

### `0D48` GET_MODEL_CRC
Gets model's CRC32 key

**Flags:** condition

**Input:**
- `model: model_any`

**Output:**
- `crc32Key: int (variable)`

---

### `0D49` STRING_CMP
Compares two strings

**Flags:** condition

**Input:**
- `strA: string`
- `strB: string`

**Output:**
- `result: bool (variable)`

---

### `0D4A` STRING_CAT
Concatenates two strings


**Input:**
- `string: string (variable)`
- `append: string`

---

### `0D4B` STRING_STR
Finds the first occurrence of a string

**Flags:** condition

**Input:**
- `string: string (variable)`
- `substring: string`

**Output:**
- `result: int (variable)`

---

### `0D4C` STRING_LEN
Gets string length


**Input:**
- `string: string`

**Output:**
- `length: int (variable)`

---

### `0D4D` STRING_CPY
Copies string to another string


**Input:**
- `source: string`
- `destination: string (variable)`

---

### `0D4E` GET_STRUCT_FIELD
Gets value at struct offset


**Input:**
- `struct: any`
- `offset: int`
- `size: int`

**Output:**
- `result: any (variable)`

---

### `0D4F` SET_STRUCT_FIELD
Sets value at struct offset


**Input:**
- `struct: int`
- `offset: int`
- `size: int`
- `value: any`

---

### `0D50` DRAW_TEMPORARY_SHADOW
Draws shadow


**Input:**
- `type: ShadowTypes`
- `x: float`
- `y: float`
- `z: float`
- `width: float`
- `height: float`
- `rotation: float`
- `distance: float`
- `texture: ShadowTextures`
- `intensity: int`
- `red: int`
- `blue: int`
- `green: int`
- `shadowData: any`

---

### `0D51` DRAW_PERMANENT_SHADOW
Draws permanent shadow


**Input:**
- `type: ShadowTypes`
- `x: float`
- `y: float`
- `z: float`
- `width: float`
- `height: float`
- `rotation: float`
- `distance: float`
- `texture: ShadowTextures`
- `intensity: int`
- `red: int`
- `green: int`
- `blue: int`
- `time: int`

---

### `0D52` DRAW_TEMPORARY_LIGHT
Draws light


**Input:**
- `type: LightTypes`
- `x: float`
- `y: float`
- `z: float`
- `dirX: float`
- `dirY: float`
- `dirZ: float`
- `radius: float`
- `red: int`
- `blue: int`
- `green: int`
- `affectEntity: int`

---

### `0D53` DRAW_TEMPORARY_CORONA
Draws corona


**Input:**
- `texture: CoronaType`
- `red: int`
- `blue: int`
- `green: int`
- `alpha: int`
- `entity: int`
- `x: float`
- `y: float`
- `z: float`
- `size: float`

---

### `0D54` DRAW_TEMPORARY_CORONA_EX
Draws corona with some extra parameters


**Input:**
- `texture: CoronaType`
- `red: int`
- `green: int`
- `blue: int`
- `alpha: int`
- `entity: int`
- `x: float`
- `y: float`
- `z: float`
- `size: float`
- `farClip: float`
- `nearClip: float`
- `flare: int`
- `enableReflection: bool`
- `checkObstacles: bool`
- `flashWhileFading: bool`
- `fadeSpeed: float`
- `onlyFromBelow: bool`

---

### `0D55` GET_SUN_COLORS
Gets sun colors


**Output:**
- `coreRed: int (variable)`
- `coreBlue: int (variable)`
- `coreGreen: int (variable)`
- `glowRed: int (variable)`
- `glowBlue: int (variable)`
- `glowGreen: int (variable)`

---

### `0D56` GET_SUN_SCREEN_COORS
Gets sun 2D position


**Output:**
- `x: float (variable)`
- `y: float (variable)`

---

### `0D57` GET_SUN_WORLD_COORS
Gets sun 3D position

**Flags:** condition

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0D58` GET_SUN_SIZE
Gets sun size


**Output:**
- `core: float (variable)`
- `glow: float (variable)`

---

### `0D59` GET_CURRENT_WEATHER
Gets current weather


**Output:**
- `currentWeather: WeatherType (variable)`

---

### `0D5A` GET_TRAFFICLIGHTS_CURRENT_COLOR
Gets trafficlight colors


**Output:**
- `ns: TrafficLightColors (variable)`
- `we: TrafficLightColors (variable)`

---

### `0D5B` DRAW_SPOTLIGHT
Draws spotlight


**Input:**
- `fromX: float`
- `fromY: float`
- `fromZ: float`
- `toX: float`
- `toY: float`
- `toZ: float`
- `baseRadius: float`
- `targetRadius: float`
- `enableShadow: bool`
- `shadowIntensity: int`
- `flag1: bool`
- `flag2: bool`

---

### `0D5C` GET_CAR_LIGHT_DAMAGE_STATUS
Gets car light damaging state


**Input:**
- `car: Car`
- `light: LightTypesCar`

**Output:**
- `damageState: bool (variable)`

---

### `0D5D` SET_CAR_LIGHT_DAMAGE_STATUS
Sets car light damaging state


**Input:**
- `car: Car`
- `light: CarLights`
- `damageState: bool`

---

### `0D5E` GET_VEHICLE_CLASS_AND_SUBCLASS
Gets vehicle class and subclass


**Input:**
- `vehicle: Car`

**Output:**
- `class: VehicleClasses (variable)`
- `subclass: VehicleSubclass (variable)`

---

### `0D5F` GET_VEHICLE_DUMMY_POSN
Gets vehicle dummy position

**Flags:** condition

**Input:**
- `vehicle: Car`
- `dummyElement: VehicleDummy`
- `position: PositionTypes`
- `invertX: bool`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `0D60` CREATE_PROJECTILE
Creates projectile

**Flags:** condition

**Input:**
- `type: ProjectileTypes`
- `launchedFromEntity: int`
- `originX: float`
- `originY: float`
- `originZ: float`
- `targetX: float`
- `targetY: float`
- `targetZ: float`
- `targetEntity: int`
- `force: float`

---

### `0D65` PRINT_TEMPORARY_TEXT
Prints a text into display ("light" version)


**Input:**
- `text: string`
- `x: float`
- `y: float`
- `widthScale: float`
- `heightScale: float`
- `style: Font`

---

### `0D66` PRINT_TEMPORARY_TEXT_EX
Prints a text into display


**Input:**
- `text: string`
- `x: float`
- `y: float`
- `widthScale: float`
- `heightScale: float`
- `style: Font`
- `prop: bool`
- `align: Align`
- `wrap: float`
- `justify: int`
- `red: int`
- `green: int`
- `blue: int`
- `alpha: int`
- `outline: int`
- `shadow: int`
- `dropRed: int`
- `dropGreen: int`
- `dropBlue: int`
- `dropAlpha: int`
- `background: int`
- `backRed: int`
- `backGreen: int`
- `backBlue: int`
- `backAlpha: int`

---

### `0D72` GET_GAME_VOLUME
Gets game sfx and radio volume


**Input:**
- `type: ParamTypes`

**Output:**
- `sfxVolume: float (variable)`
- `radioVolume: float (variable)`

---

### `0D73` GET_SCREEN_WIDTH_AND_HEIGHT
Gets screen width and height


**Input:**
- `type: ParamTypes`

**Output:**
- `width: float (variable)`
- `height: float (variable)`

---

### `0D76` GET_COMPONENT_OBJECT
Gets component object

**Flags:** condition

**Input:**
- `component: any`
- `object: any`

**Output:**
- `componentObject: any (variable)`

---

### `0D77` HIDE_OBJECT_ATOMIC
Hides object atomic


**Input:**
- `objectAtomic: any`
- `hide: bool`

---

### `0D78` GET_OBJECT_ATOMIC_FLAG
Gets object atomic flag


**Input:**
- `object: Object`
- `atomicFlag: int`

**Output:**
- `state: bool (variable)`

---

### `0D79` SET_OBJECT_ATOMIC_FLAG
Sets object atomic flag


**Input:**
- `object: any`
- `atomicFlag: int`
- `state: bool`

---

### `0D7A` GET_OBJECT_ATOMIC_NUM_MATERIALS
Gets object atomic material texture

**Flags:** condition

**Input:**
- `object: any`

**Output:**
- `numMaterials: int (variable)`

---

### `0D7B` GET_OBJECT_ATOMIC_MATERIAL_TEXTURE
Gets object atomic material texture

**Flags:** condition

**Input:**
- `object: any`
- `material: int`

**Output:**
- `texture: any (variable)`

---
