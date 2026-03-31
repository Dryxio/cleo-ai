# StreamedScript Opcodes

> 10 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `07D3` | REGISTER_SCRIPT_BRAIN_FOR_CODE_USE | Allows the game to start a new ambient script by name, e.g. to control behavior  |
| `0884` | REGISTER_ATTRACTOR_SCRIPT_BRAIN_FOR_CODE_USE | Allows the game to start a new ambient script for the ped using the map attracto |
| `08A9` | STREAM_SCRIPT | Loads the ambient script with the specified ID from the script.img file |
| `08AB` | HAS_STREAMED_SCRIPT_LOADED | Returns true if the ambient script has finished loading (08A9) |
| `090F` | MARK_STREAMED_SCRIPT_AS_NO_LONGER_NEEDED | Ends the specified script brain |
| `0910` | REMOVE_STREAMED_SCRIPT | Releases the ambient script with the specified ID, freeing game memory |
| `0913` | START_NEW_STREAMED_SCRIPT | Runs the ambient script with the specified ID |
| `0926` | GET_NUMBER_OF_INSTANCES_OF_STREAMED_SCRIPT | Gets the number of instances of a script |
| `0928` | ALLOCATE_STREAMED_SCRIPT_TO_RANDOM_PED | Makes the game start an ambient script when the player is nearby a character of  |
| `0929` | ALLOCATE_STREAMED_SCRIPT_TO_OBJECT | Makes the game start an ambient script when the player is nearby an object of th |

## Detailed Reference

### `07D3` REGISTER_SCRIPT_BRAIN_FOR_CODE_USE
Allows the game to start a new ambient script by name, e.g. to control behavior of peds in interiors

**Class:** `StreamedScript.RegisterScriptBrainForCodeUse`
**Flags:** static

**Input:**
- `id: script_id`
- `scriptName: string`

**Details:**

This command creates an association between an ambient script and its name, allowing the game to start the script from the code.

```
register_script_brain_for_code_use 23 'HOUSE'
```

The script starts when the game code calls the brain by its string name, e.g. when creating peds in interiors. The ped handle is passed to the script in the first local variable.

```
StartOrRequestNewStreamedScriptBrainWithThisName("HOUSE", pedHandle, CODE_PED)
```

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

### `0884` REGISTER_ATTRACTOR_SCRIPT_BRAIN_FOR_CODE_USE
Allows the game to start a new ambient script for the ped using the map attractor, e.g. shoppers

**Class:** `StreamedScript.RegisterAttractorScriptBrainForCodeUse`
**Flags:** static

**Input:**
- `id: script_id`
- `scriptName: string`

**Details:**

This command creates an association between an ambient script and its name, allowing the game to start the script when a ped uses a corresponding attractor.

```
register_attractor_script_brain_for_code_use {id} 41 (PCHAIR) {_p2} 'PCHAIR'
```

The script starts when a ped is tasked to use an attractor defined in the map data. The ped handle is passed to the script in the first local variable.

```
task_use_closest_map_attractor {handle} ped {radius} 20.0 {modelId} #NULL {fromX} 0.0 {fromY} 0.0 {fromZ} 0.0 {name} "PCHAIR"
```

The game can also spawn peds that use attractors defined in the map data, such as gym equipment, chairs, and dance spots. In this case, the second local variable of the script will be set to `1` to indicate that the ped was spawned by the game.

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

### `08A9` STREAM_SCRIPT
Loads the ambient script with the specified ID from the script.img file

**Class:** `StreamedScript.Stream`
**Flags:** static

**Input:**
- `id: script_id`

---

### `08AB` HAS_STREAMED_SCRIPT_LOADED
Returns true if the ambient script has finished loading (08A9)

**Class:** `StreamedScript.HasLoaded`
**Flags:** condition, static

**Input:**
- `id: script_id`

---

### `090F` MARK_STREAMED_SCRIPT_AS_NO_LONGER_NEEDED
Ends the specified script brain

**Class:** `StreamedScript.MarkAsNoLongerNeeded`
**Flags:** static

**Input:**
- `id: script_id`

---

### `0910` REMOVE_STREAMED_SCRIPT
Releases the ambient script with the specified ID, freeing game memory

**Class:** `StreamedScript.Remove`
**Flags:** static

**Input:**
- `id: script_id`

---

### `0913` START_NEW_STREAMED_SCRIPT
Runs the ambient script with the specified ID

**Class:** `StreamedScript.StartNew`
**Flags:** static

**Input:**
- `id: script_id`
- `args: arguments`

---

### `0926` GET_NUMBER_OF_INSTANCES_OF_STREAMED_SCRIPT
Gets the number of instances of a script

**Class:** `StreamedScript.GetNumberOfInstances`
**Flags:** static

**Input:**
- `id: script_id`

**Output:**
- `numScripts: int (variable)`

---

### `0928` ALLOCATE_STREAMED_SCRIPT_TO_RANDOM_PED
Makes the game start an ambient script when the player is nearby a character of the specified model

**Class:** `StreamedScript.AllocateToRandomPed`
**Flags:** static

**Input:**
- `id: script_id`
- `modelId: model_char`
- `priority: int`

**Details:**

This command creates an association between an ambient script and the pedestrian model, allowing the game to start the script when a ped of that model is created. It only affects random peds spawned by the game.

```
allocate_streamed_script_to_random_ped {id} 19 (DEALER) {modelId} #BMYDRUG {priority} 100
```

It starts the script when the game spawns a random ped with the specified model ID, if the player is within the radius of `5.0` of the ped. The ped handle is passed to the script in the first local variable.

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

### `0929` ALLOCATE_STREAMED_SCRIPT_TO_OBJECT
Makes the game start an ambient script when the player is nearby an object of the specified model

**Class:** `StreamedScript.AllocateToObject`
**Flags:** static

**Input:**
- `id: script_id`
- `modelId: model_object`
- `priority: int`
- `radius: float`
- `groupingId: int`

**Details:**

This command creates an association between an ambient script and the object model, allowing the game to start the script when an object of that model is created. The object has to be defined in the `object.dat` file.

```
allocate_streamed_script_to_object {id} 4 (SLOT_MACHINE) {modelId} #KB_BANDIT_U {priority} 100 {radius} 6.0 {type} 1
```

It triggers when the game spawns a random object with the specified model ID, if the player is within the defined radius of the object. The object handle is passed to the script in the first local variable.

The grouping ID is an optional attribute that allows similar triggers to be grouped together for quick toggling via SWITCH_OBJECT_BRAINS.

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
