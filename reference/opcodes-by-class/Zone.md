# Zone Opcodes

> 16 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `02DD` | GET_RANDOM_CHAR_IN_ZONE | Gets a random character in the specified zone whose pedtype matches the specifie |
| `0767` | SET_ZONE_POPULATION_TYPE | Sets which population type from popcycle.dat will inhabit this zone |
| `076A` | SET_ZONE_DEALER_STRENGTH | Sets the total number of drug dealers in the zone |
| `076B` | GET_ZONE_DEALER_STRENGTH | Returns the drug dealer density of the specified zone |
| `076C` | SET_ZONE_GANG_STRENGTH | Sets the density of the gang members in the specified zone |
| `076D` | GET_ZONE_GANG_STRENGTH | Returns the density of the gang members in the specified zone |
| `0843` | GET_NAME_OF_ZONE | Returns the GXT key associated with the zone at the specified coordinates |
| `0874` | SET_ZONE_POPULATION_RACE | Sets which races will inhabit this zone |
| `08B3` | SET_ZONE_FOR_GANG_WARS_TRAINING | Sets the zone as the only zone where a turf war can be provoked |
| `08CA` | INIT_ZONE_POPULATION_SETTINGS | Resets all changes made to the zone info |
| `08D3` | GET_CURRENT_POPULATION_ZONE_TYPE | Returns the population type in the zone the player is currently in |
| `08F1` | GET_NAME_OF_INFO_ZONE | Returns the name of the zone at the specified coordinates |
| `090C` | SET_SPECIFIC_ZONE_TO_TRIGGER_GANG_WAR |  |
| `0917` | SWITCH_AUDIO_ZONE | Sets whether the IPL defined audio for the specified area should play |
| `09B7` | SET_ZONE_NO_COPS | Sets whether cops should be prevented from spawning in the specified area |
| `0A24` | SET_DISABLE_MILITARY_ZONES | Causes the players wanted level to be set at 4 when in restricted areas |

## Detailed Reference

### `02DD` GET_RANDOM_CHAR_IN_ZONE
Gets a random character in the specified zone whose pedtype matches the specified values

**Class:** `Zone.GetRandomChar`
**Flags:** constructor

**Input:**
- `zone: zone_key`
- `civilian: bool`
- `gang: bool`
- `criminalOrProstitute: bool`

**Output:**
- `handle: Char (variable)`

---

### `0767` SET_ZONE_POPULATION_TYPE
Sets which population type from popcycle.dat will inhabit this zone

**Class:** `Zone.SetPopulationType`
**Flags:** static

**Input:**
- `zone: zone_key`
- `type: ZoneType`

---

### `076A` SET_ZONE_DEALER_STRENGTH
Sets the total number of drug dealers in the zone

**Class:** `Zone.SetDealerStrength`
**Flags:** static

**Input:**
- `zone: zone_key`
- `strength: int`

---

### `076B` GET_ZONE_DEALER_STRENGTH
Returns the drug dealer density of the specified zone

**Class:** `Zone.GetDealerStrength`
**Flags:** static

**Input:**
- `zone: zone_key`

**Output:**
- `density: int (variable)`

---

### `076C` SET_ZONE_GANG_STRENGTH
Sets the density of the gang members in the specified zone

**Class:** `Zone.SetGangStrength`
**Flags:** static

**Input:**
- `zoneId: zone_key`
- `gangId: GangType`
- `density: int`

---

### `076D` GET_ZONE_GANG_STRENGTH
Returns the density of the gang members in the specified zone

**Class:** `Zone.GetGangStrength`
**Flags:** static

**Input:**
- `zone: zone_key`
- `gangId: GangType`

**Output:**
- `density: int (variable)`

---

### `0843` GET_NAME_OF_ZONE
Returns the GXT key associated with the zone at the specified coordinates

**Class:** `Zone.GetTextKey`
**Flags:** static, overload

**Input:**
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `key: gxt_key (variable)`

---

### `0874` SET_ZONE_POPULATION_RACE
Sets which races will inhabit this zone

**Class:** `Zone.SetPopulationRace`
**Flags:** static

**Input:**
- `zone: zone_key`
- `races: RaceSet`

**Details:**

### Bitflags
* PedRace_Black = 1
* PedRace_White = 2
* PedRace_Asian = 4
* PedRace_Hispanic = 8

A ped model's race is determined by the first letter of the ped ID.
* Black = `B`
* White = `W`
* Asian = `O`,`I`
* Hispanic = `H`

In a zone with a PedRace setting of `0`, only peds that are neither Black, White, Asian, nor Hispanic will spawn; like MALE01, SFYPRO, SMYST1, SMYST2.

### Dealer ped streamer logic:

1. current weather zone is 2 -> entry 3 from dealer ped group is selected (biker in SF)
2. population race & 1 != 0 -> entry 0 is selected (black)
3. population race & 2 != 0 -> entry 1 is selected (white)
4. otherwise, entry 2 is selected (hispanic)

---

### `08B3` SET_ZONE_FOR_GANG_WARS_TRAINING
Sets the zone as the only zone where a turf war can be provoked

**Class:** `Zone.SetForGangWarsTraining`
**Flags:** static

**Input:**
- `zone: zone_key`

---

### `08CA` INIT_ZONE_POPULATION_SETTINGS
Resets all changes made to the zone info

**Class:** `Zone.InitPopulationSettings`
**Flags:** static

---

### `08D3` GET_CURRENT_POPULATION_ZONE_TYPE
Returns the population type in the zone the player is currently in

**Class:** `Zone.GetCurrentPopulationZoneType`
**Flags:** static

**Output:**
- `type: ZoneType (variable)`

---

### `08F1` GET_NAME_OF_INFO_ZONE
Returns the name of the zone at the specified coordinates

**Class:** `Zone.GetName`
**Flags:** static, overload

**Input:**
- `x: float`
- `y: float`
- `z: float`

**Output:**
- `name: string (variable)`

---

### `090C` SET_SPECIFIC_ZONE_TO_TRIGGER_GANG_WAR

**Class:** `Zone.SetTriggerGangWar`
**Flags:** static

**Input:**
- `zone: zone_key`

---

### `0917` SWITCH_AUDIO_ZONE
Sets whether the IPL defined audio for the specified area should play

**Class:** `Zone.SwitchAudio`
**Flags:** static

**Input:**
- `zone: zone_key`
- `state: bool`

---

### `09B7` SET_ZONE_NO_COPS
Sets whether cops should be prevented from spawning in the specified area

**Class:** `Zone.SetNoCops`
**Flags:** static

**Input:**
- `zone: zone_key`
- `state: bool`

---

### `0A24` SET_DISABLE_MILITARY_ZONES
Causes the players wanted level to be set at 4 when in restricted areas

**Class:** `Zone.SetDisableMilitaryZones`
**Flags:** static

**Input:**
- `state: bool`

---
