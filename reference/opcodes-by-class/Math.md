# Math Opcodes

> 38 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0094` | ABS_VAR_INT | Returns the absolute value of the global integer variable |
| `0095` | ABS_LVAR_INT | Returns the absolute value of the local integer variable |
| `0096` | ABS_VAR_FLOAT | Returns the absolute value of the global float variable |
| `0097` | ABS_LVAR_FLOAT | Returns the absolute value of the local float variable |
| `0098` | GENERATE_RANDOM_FLOAT | Returns a random float between 0.0 to 1.0; excluding 1.0 |
| `0099` | GENERATE_RANDOM_INT | Returns a random integer between 0 and 32767 |
| `01FB` | SQRT | Returns the square root of a number |
| `0208` | GENERATE_RANDOM_FLOAT_IN_RANGE | Returns a random float within the specified range; including min and max values |
| `0209` | GENERATE_RANDOM_INT_IN_RANGE | Returns a random integer within the specified range; including min and excluding |
| `02F6` | SIN | Returns the sine of the angle |
| `02F7` | COS | Returns the cosine of the angle |
| `0425` | CONVERT_METRES_TO_FEET | Returns the result of converting meters to feet |
| `042D` | CONVERT_METRES_TO_FEET_INT | Returns the result of converting meters to feet |
| `0509` | GET_DISTANCE_BETWEEN_COORDS_2D | Gets the distance between two points |
| `050A` | GET_DISTANCE_BETWEEN_COORDS_3D | Gets the distance between two points |
| `05A4` | GET_ANGLE_BETWEEN_2D_VECTORS | Gets the angle between the two 2D vectors |
| `05A5` | DO_2D_RECTANGLES_COLLIDE | Returns true if rectangle1 is inside rectangle2 or partially intersects it |
| `05B0` | GET_2D_LINES_INTERSECT_POINT | Returns the point of intersection of two lines. If they do not intersect, both r |
| `0604` | GET_HEADING_FROM_VECTOR_2D | Gets the angle for the XY offset |
| `0656` | LIMIT_ANGLE | Gets the exact angle of an angle |
| `08B4` | IS_GLOBAL_VAR_BIT_SET_CONST | Checks if the nth bit of the number is set |
| `08B5` | IS_GLOBAL_VAR_BIT_SET_VAR | Checks if the nth bit of the number is set |
| `08B6` | IS_GLOBAL_VAR_BIT_SET_LVAR | Checks if the nth bit of the number is set |
| `08B7` | IS_LOCAL_VAR_BIT_SET_CONST | Checks if the nth bit of the number is set |
| `08B8` | IS_LOCAL_VAR_BIT_SET_VAR | Checks if the nth bit of the number is set |
| `08B9` | IS_LOCAL_VAR_BIT_SET_LVAR | Checks if the nth bit of the number is set |
| `08BA` | SET_GLOBAL_VAR_BIT_CONST | Sets the nth bit of the number |
| `08BB` | SET_GLOBAL_VAR_BIT_VAR | Sets the nth bit of the number |
| `08BC` | SET_GLOBAL_VAR_BIT_LVAR | Sets the nth bit of the number |
| `08BD` | SET_LOCAL_VAR_BIT_CONST | Sets the nth bit of the number |
| `08BE` | SET_LOCAL_VAR_BIT_VAR | Sets the nth bit of the number |
| `08BF` | SET_LOCAL_VAR_BIT_LVAR | Sets the nth bit of the number |
| `08C0` | CLEAR_GLOBAL_VAR_BIT_CONST | Clears the nth bit of the number |
| `08C1` | CLEAR_GLOBAL_VAR_BIT_VAR | Clears the nth bit of the number |
| `08C2` | CLEAR_GLOBAL_VAR_BIT_LVAR | Clears the nth bit of the number |
| `08C3` | CLEAR_LOCAL_VAR_BIT_CONST | Clears the nth bit of the number |
| `08C4` | CLEAR_LOCAL_VAR_BIT_VAR | Clears the nth bit of the number |
| `08C5` | CLEAR_LOCAL_VAR_BIT_LVAR | Clears the nth bit of the number |

## Detailed Reference

### `0094` ABS_VAR_INT
Returns the absolute value of the global integer variable

**Class:** `Math.Abs`
**Flags:** overload, static

**Output:**
- `number: int (global var)`

---

### `0095` ABS_LVAR_INT
Returns the absolute value of the local integer variable

**Class:** `Math.Abs`
**Flags:** overload, static

**Output:**
- `number: int (local var)`

---

### `0096` ABS_VAR_FLOAT
Returns the absolute value of the global float variable

**Class:** `Math.Abs`
**Flags:** overload, static

**Output:**
- `number: float (global var)`

---

### `0097` ABS_LVAR_FLOAT
Returns the absolute value of the local float variable

**Class:** `Math.Abs`
**Flags:** overload, static

**Output:**
- `number: float (local var)`

---

### `0098` GENERATE_RANDOM_FLOAT
Returns a random float between 0.0 to 1.0; excluding 1.0

**Class:** `Math.Random`
**Flags:** overload, static

**Output:**
- `float (variable)`

---

### `0099` GENERATE_RANDOM_INT
Returns a random integer between 0 and 32767

**Class:** `Math.Random`
**Flags:** overload, static

**Output:**
- `int (variable)`

**Details:**

This command was intended to return a random integer between `0` and `65535` and store the result to a variable. However due a bug it only returns a fixed range of `0` and `32767`. An unofficial patch for the PC version called "SilentPatch" fixes this problem. To return a custom range, use GENERATE_RANDOM_INT_IN_RANGE instead.

---

### `01FB` SQRT
Returns the square root of a number

**Class:** `Math.Sqrt`
**Flags:** static

**Input:**
- `num: float`

**Output:**
- `result: float (variable)`

---

### `0208` GENERATE_RANDOM_FLOAT_IN_RANGE
Returns a random float within the specified range; including min and max values

**Class:** `Math.RandomFloatInRange`
**Flags:** static

**Input:**
- `min: float`
- `max: float`

**Output:**
- `result: float (variable)`

---

### `0209` GENERATE_RANDOM_INT_IN_RANGE
Returns a random integer within the specified range; including min and excluding max values

**Class:** `Math.RandomIntInRange`
**Flags:** static

**Input:**
- `min: int`
- `max: int`

**Output:**
- `result: int (variable)`

---

### `02F6` SIN
Returns the sine of the angle

**Class:** `Math.Sin`
**Flags:** static

**Input:**
- `angle: float`

**Output:**
- `result: float (variable)`

---

### `02F7` COS
Returns the cosine of the angle

**Class:** `Math.Cos`
**Flags:** static

**Input:**
- `angle: float`

**Output:**
- `result: float (variable)`

---

### `0425` CONVERT_METRES_TO_FEET
Returns the result of converting meters to feet

**Class:** `Math.ConvertMetersToFeet`
**Flags:** static, overload

**Input:**
- `meters: float`

**Output:**
- `feet: float (variable)`

---

### `042D` CONVERT_METRES_TO_FEET_INT
Returns the result of converting meters to feet

**Class:** `Math.ConvertMetersToFeet`
**Flags:** static, overload

**Input:**
- `meters: int`

**Output:**
- `feet: int (variable)`

---

### `0509` GET_DISTANCE_BETWEEN_COORDS_2D
Gets the distance between two points

**Class:** `Math.GetDistanceBetweenCoords2D`
**Flags:** static

**Input:**
- `fromX: float`
- `fromY: float`
- `toX: float`
- `toZ: float`

**Output:**
- `distance: float (variable)`

---

### `050A` GET_DISTANCE_BETWEEN_COORDS_3D
Gets the distance between two points

**Class:** `Math.GetDistanceBetweenCoords3D`
**Flags:** static

**Input:**
- `fromX: float`
- `fromY: float`
- `fromZ: float`
- `toX: float`
- `toY: float`
- `toZ: float`

**Output:**
- `distance: float (variable)`

---

### `05A4` GET_ANGLE_BETWEEN_2D_VECTORS
Gets the angle between the two 2D vectors

**Class:** `Math.GetAngleBetween2DVectors`
**Flags:** static

**Input:**
- `x1: float`
- `y1: float`
- `x2: float`
- `y2: float`

**Output:**
- `angle: float (variable)`

---

### `05A5` DO_2D_RECTANGLES_COLLIDE
Returns true if rectangle1 is inside rectangle2 or partially intersects it

**Class:** `Math.Do2DRectanglesCollide`
**Flags:** static, condition

**Input:**
- `rectangle1PositionX: float`
- `rectangle1PositionY: float`
- `rectangle1SizeX: float`
- `rectangle1SizeY: float`
- `rectangle2PositionX: float`
- `rectangle2PositionY: float`
- `rectangle2SizeX: float`
- `rectangle2SizeY: float`

---

### `05B0` GET_2D_LINES_INTERSECT_POINT
Returns the point of intersection of two lines. If they do not intersect, both returned values are -1000000.0 and the condition result is false

**Class:** `Math.Get2DLinesIntersectPoint`
**Flags:** static, condition

**Input:**
- `line1StartX: float`
- `line1StartY: float`
- `line1EndX: float`
- `line1EndY: float`
- `line2StartX: float`
- `line2StartY: float`
- `line2EndX: float`
- `line2EndY: float`

**Output:**
- `intersectPointX: float (variable)`
- `intersectPointY: float (variable)`

**Details:**

This command checks if two lines share a common point and returns the X and Y coordinates of that point. If they don't intersect both returned values are equal to -1000000.0.

This command can be used as a condition. If the point of intersection exists, the condition is true. If the intersection point doesn't exist, the condition is false.

---

### `0604` GET_HEADING_FROM_VECTOR_2D
Gets the angle for the XY offset

**Class:** `Math.GetHeadingFromVector2D`
**Flags:** static

**Input:**
- `x: float`
- `y: float`

**Output:**
- `heading: float (variable)`

---

### `0656` LIMIT_ANGLE
Gets the exact angle of an angle

**Class:** `Math.LimitAngle`
**Flags:** static

**Input:**
- `value: float`

**Output:**
- `result: float (variable)`

---

### `08B4` IS_GLOBAL_VAR_BIT_SET_CONST
Checks if the nth bit of the number is set

**Class:** `Math.IsBitSet`
**Flags:** condition, static

**Input:**
- `number: int (global var)`
- `bitIndex: int (literal)`

---

### `08B5` IS_GLOBAL_VAR_BIT_SET_VAR
Checks if the nth bit of the number is set

**Class:** `Math.IsBitSet`
**Flags:** condition, static

**Input:**
- `number: int (global var)`
- `bitIndex: int (global var)`

---

### `08B6` IS_GLOBAL_VAR_BIT_SET_LVAR
Checks if the nth bit of the number is set

**Class:** `Math.IsBitSet`
**Flags:** condition, static

**Input:**
- `number: int (global var)`
- `bitIndex: int (local var)`

---

### `08B7` IS_LOCAL_VAR_BIT_SET_CONST
Checks if the nth bit of the number is set

**Class:** `Math.IsBitSet`
**Flags:** condition, static

**Input:**
- `number: int (local var)`
- `bitIndex: int (literal)`

---

### `08B8` IS_LOCAL_VAR_BIT_SET_VAR
Checks if the nth bit of the number is set

**Class:** `Math.IsBitSet`
**Flags:** condition, static

**Input:**
- `number: int (local var)`
- `bitIndex: int (global var)`

---

### `08B9` IS_LOCAL_VAR_BIT_SET_LVAR
Checks if the nth bit of the number is set

**Class:** `Math.IsBitSet`
**Flags:** condition, static

**Input:**
- `number: int (local var)`
- `bitIndex: int (local var)`

---

### `08BA` SET_GLOBAL_VAR_BIT_CONST
Sets the nth bit of the number

**Class:** `Math.SetBit`
**Flags:** static

**Input:**
- `number: int (global var)`
- `bitIndex: int (literal)`

---

### `08BB` SET_GLOBAL_VAR_BIT_VAR
Sets the nth bit of the number

**Class:** `Math.SetBit`
**Flags:** static

**Input:**
- `number: int (global var)`
- `bitIndex: int (global var)`

---

### `08BC` SET_GLOBAL_VAR_BIT_LVAR
Sets the nth bit of the number

**Class:** `Math.SetBit`
**Flags:** static

**Input:**
- `number: int (global var)`
- `bitIndex: int (local var)`

---

### `08BD` SET_LOCAL_VAR_BIT_CONST
Sets the nth bit of the number

**Class:** `Math.SetBit`
**Flags:** static

**Input:**
- `number: int (local var)`
- `bitIndex: int (literal)`

---

### `08BE` SET_LOCAL_VAR_BIT_VAR
Sets the nth bit of the number

**Class:** `Math.SetBit`
**Flags:** static

**Input:**
- `number: int (local var)`
- `bitIndex: int (global var)`

---

### `08BF` SET_LOCAL_VAR_BIT_LVAR
Sets the nth bit of the number

**Class:** `Math.SetBit`
**Flags:** static

**Input:**
- `number: int (local var)`
- `bitIndex: int (local var)`

---

### `08C0` CLEAR_GLOBAL_VAR_BIT_CONST
Clears the nth bit of the number

**Class:** `Math.ClearBit`
**Flags:** static

**Input:**
- `number: int (global var)`
- `bitIndex: int (literal)`

---

### `08C1` CLEAR_GLOBAL_VAR_BIT_VAR
Clears the nth bit of the number

**Class:** `Math.ClearBit`
**Flags:** static

**Input:**
- `number: int (global var)`
- `bitIndex: int (global var)`

---

### `08C2` CLEAR_GLOBAL_VAR_BIT_LVAR
Clears the nth bit of the number

**Class:** `Math.ClearBit`
**Flags:** static

**Input:**
- `number: int (global var)`
- `bitIndex: int (local var)`

---

### `08C3` CLEAR_LOCAL_VAR_BIT_CONST
Clears the nth bit of the number

**Class:** `Math.ClearBit`
**Flags:** static

**Input:**
- `number: int (local var)`
- `bitIndex: int (literal)`

---

### `08C4` CLEAR_LOCAL_VAR_BIT_VAR
Clears the nth bit of the number

**Class:** `Math.ClearBit`
**Flags:** static

**Input:**
- `number: int (local var)`
- `bitIndex: int (global var)`

---

### `08C5` CLEAR_LOCAL_VAR_BIT_LVAR
Clears the nth bit of the number

**Class:** `Math.ClearBit`
**Flags:** static

**Input:**
- `number: int (local var)`
- `bitIndex: int (local var)`

---
