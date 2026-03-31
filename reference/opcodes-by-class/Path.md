# Path Opcodes

> 20 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `01E7` | SWITCH_ROADS_ON | Enables all car paths in the given area |
| `01E8` | SWITCH_ROADS_OFF | Disables all car paths in the given area |
| `022A` | SWITCH_PED_ROADS_ON | Enables all ped paths in the given area |
| `022B` | SWITCH_PED_ROADS_OFF | Disables all ped paths in the given area |
| `02C0` | GET_CLOSEST_CHAR_NODE | Returns the nearest path node from the specified coordinates that a pedestrian c |
| `02C1` | GET_CLOSEST_CAR_NODE | Returns the nearest path note from the specified coordinates that a vehicle can  |
| `03D3` | GET_CLOSEST_CAR_NODE_WITH_HEADING | Returns the position and heading of the closest vehicle path node to the specifi |
| `04B9` | GET_CLOSEST_STRAIGHT_ROAD | Gets two closest path nodes within the specified distance range |
| `04D3` | GET_NTH_CLOSEST_CAR_NODE | Gets the coordinates of the nth car path node closest to the given coordinates |
| `05D6` | FLUSH_ROUTE | Flushes the task route |
| `05D7` | EXTEND_ROUTE | Adds a point to the task route |
| `0606` | LOAD_PATH_NODES_IN_AREA | Adds an area where script created cars will avoid driving in |
| `0607` | RELEASE_PATH_NODES | Removes areas forbidden for scripted cars set up by 0606 |
| `06F8` | GET_NTH_CLOSEST_CAR_NODE_WITH_HEADING |  |
| `0754` | FLUSH_PATROL_ROUTE | Clears all previous patrol data to start a new patrol route, which can be used i |
| `0755` | EXTEND_PATROL_ROUTE | Adds a new point to the patrol route |
| `091D` | SWITCH_ROADS_BACK_TO_ORIGINAL | Reverts all changes to car paths done with SWITCH_ROADS_ON and SWITCH_ROADS_OFF |
| `091E` | SWITCH_PED_ROADS_BACK_TO_ORIGINAL | Reverts all changes to ped paths done with SWITCH_PED_ROADS_ON and SWITCH_PED_RO |
| `0994` | MARK_ROAD_NODE_AS_DONT_WANDER |  |
| `0995` | UNMARK_ALL_ROAD_NODES_AS_DONT_WANDER |  |

## Detailed Reference

### `01E7` SWITCH_ROADS_ON
Enables all car paths in the given area

**Class:** `Path.SwitchRoadsOn`
**Flags:** static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`

---

### `01E8` SWITCH_ROADS_OFF
Disables all car paths in the given area

**Class:** `Path.SwitchRoadsOff`
**Flags:** static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`

---

### `022A` SWITCH_PED_ROADS_ON
Enables all ped paths in the given area

**Class:** `Path.SwitchPedRoadsOn`
**Flags:** static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`

---

### `022B` SWITCH_PED_ROADS_OFF
Disables all ped paths in the given area

**Class:** `Path.SwitchPedRoadsOff`
**Flags:** static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`

---

### `02C0` GET_CLOSEST_CHAR_NODE
Returns the nearest path node from the specified coordinates that a pedestrian can walk on

**Class:** `Path.GetClosestCharNode`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `nodeX: float (variable)`
- `nodeY: float (variable)`
- `nodeZ: float (variable)`

---

### `02C1` GET_CLOSEST_CAR_NODE
Returns the nearest path note from the specified coordinates that a vehicle can drive on

**Class:** `Path.GetClosestCarNode`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `nodeX: float (variable)`
- `nodeY: float (variable)`
- `nodeZ: float (variable)`

---

### `03D3` GET_CLOSEST_CAR_NODE_WITH_HEADING
Returns the position and heading of the closest vehicle path node to the specified position

**Class:** `Path.GetClosestCarNodeWithHeading`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `nodeX: float (variable)`
- `nodeY: float (variable)`
- `nodeZ: float (variable)`
- `angle: float (variable)`

---

### `04B9` GET_CLOSEST_STRAIGHT_ROAD
Gets two closest path nodes within the specified distance range

**Class:** `Path.GetClosestStraightRoad`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `minDist: float`
- `maxDist: float`

**Output:**
- `node1X: float (variable)`
- `node1Y: float (variable)`
- `node1Z: float (variable)`
- `node2X: float (variable)`
- `node2Y: float (variable)`
- `node2Z: float (variable)`
- `angle: float (variable)`

---

### `04D3` GET_NTH_CLOSEST_CAR_NODE
Gets the coordinates of the nth car path node closest to the given coordinates

**Class:** `Path.GetNthClosestCarNode`
**Flags:** static

**Input:**
- `fromX: float`
- `fromY: float`
- `fromZ: float`
- `n: int`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`

---

### `05D6` FLUSH_ROUTE
Flushes the task route

**Class:** `Path.FlushRoute`
**Flags:** static

---

### `05D7` EXTEND_ROUTE
Adds a point to the task route

**Class:** `Path.ExtendRoute`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`

---

### `0606` LOAD_PATH_NODES_IN_AREA
Adds an area where script created cars will avoid driving in

**Class:** `Path.LoadPathNodesInArea`
**Flags:** static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `rightTopX: float`
- `rightTopY: float`

---

### `0607` RELEASE_PATH_NODES
Removes areas forbidden for scripted cars set up by 0606

**Class:** `Path.ReleaseNodes`
**Flags:** static

---

### `06F8` GET_NTH_CLOSEST_CAR_NODE_WITH_HEADING

**Class:** `Path.GetNthClosestCarNodeWithHeading`
**Flags:** static

**Input:**
- `xCoord: float`
- `yCoord: float`
- `zCoord: float`
- `nth: int`

**Output:**
- `x: float (variable)`
- `y: float (variable)`
- `z: float (variable)`
- `heading: float (variable)`

---

### `0754` FLUSH_PATROL_ROUTE
Clears all previous patrol data to start a new patrol route, which can be used in combination with 0755 to create patrol routes

**Class:** `Path.FlushPatrolRoute`
**Flags:** static

---

### `0755` EXTEND_PATROL_ROUTE
Adds a new point to the patrol route

**Class:** `Path.ExtendPatrolRoute`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`
- `animationName: string`
- `animationFile: string`

---

### `091D` SWITCH_ROADS_BACK_TO_ORIGINAL
Reverts all changes to car paths done with SWITCH_ROADS_ON and SWITCH_ROADS_OFF

**Class:** `Path.SwitchRoadsBackToOriginal`
**Flags:** static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`

---

### `091E` SWITCH_PED_ROADS_BACK_TO_ORIGINAL
Reverts all changes to ped paths done with SWITCH_PED_ROADS_ON and SWITCH_PED_ROADS_OFF

**Class:** `Path.SwitchPedRoadsBackToOriginal`
**Flags:** static

**Input:**
- `leftBottomX: float`
- `leftBottomY: float`
- `leftBottomZ: float`
- `rightTopX: float`
- `rightTopY: float`
- `rightTopZ: float`

---

### `0994` MARK_ROAD_NODE_AS_DONT_WANDER

**Class:** `Path.MarkRoadNodeAsDontWander`
**Flags:** static

**Input:**
- `x: float`
- `y: float`
- `z: float`

---

### `0995` UNMARK_ALL_ROAD_NODES_AS_DONT_WANDER

**Class:** `Path.UnmarkAllRoadNodesAsDontWander`
**Flags:** static

---
