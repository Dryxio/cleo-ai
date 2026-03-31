# Common CLEO Script Patterns

Reusable patterns for common scripting tasks. Copy and adapt these.

---

## 1. Script Boilerplate

Every CLEO script starts with this:

```
{$CLEO .cs}
script_name {name} 'mymod'
wait {time} 2000       // let game initialize
// ... your code ...
terminate_this_custom_script
```

## 2. Main Loop with Safety

```
while true
    wait {time} 0      // MANDATORY: prevents game freeze

    if
        not is_player_playing $player1
    then
        continue       // skip if wasted/busted/loading
    end

    // your per-frame logic here
end
```

## 3. Cheat Code Trigger

```
while true
    wait {time} 250    // no need to check every frame

    if and
        test_cheat "mycheat"
        is_player_playing $player1
        is_player_control_on $player1
    then
        // cheat activated!
    end
end
```

## 4. Keyboard Toggle

```
int enabled = 0

// In your loop:
if
    is_key_pressed {keyCode} KeyCode.F5
then
    enabled = 1 - enabled    // toggle 0 <-> 1

    if
        enabled == 1
    then
        // enable effect
    else
        // disable effect
    end

    // debounce: wait for key release
    while is_key_pressed {keyCode} KeyCode.F5
        wait {time} 0
    end
end
```

## 5. Spawn Vehicle

```
function SPAWN_CAR_AT_PLAYER(modelHash: int): int
    request_model {modelId} modelHash
    load_all_models_now

    float x, y, z
    x, y, z = get_offset_from_char_in_world_coords $scplayer {offset} 0.0 5.0 0.0

    int car = create_car {modelId} modelHash {pos} x y z
    mark_model_as_no_longer_needed {modelId} modelHash

    float heading = get_char_heading $scplayer
    set_car_heading car {heading} heading

    return car
end
```

## 6. Spawn Ped

```
function SPAWN_PED(modelHash: int, pedType: int, x: float, y: float, z: float): int
    request_model {modelId} modelHash
    load_all_models_now

    int ped = create_char {pedType} pedType {modelId} modelHash {pos} x y z
    mark_model_as_no_longer_needed {modelId} modelHash

    return ped
end
```

## 7. Teleport Player Safely

```
function TELEPORT(x: float, y: float, z: float)
    do_fade {time} 250 {direction} Fade.Out
    wait {time} 250

    if
        is_char_in_any_car $scplayer
    then
        warp_char_from_car_to_coord $scplayer {pos} x y z
    else
        set_char_coordinates $scplayer {xyz} x y z
    end

    request_collision {pos} x y
    load_all_models_now

    do_fade {time} 250 {direction} Fade.In
end
```

## 8. Model Loading Pattern

```
request_model #INFERNUS          // request by hash
load_all_models_now              // force synchronous load
// ... use the model ...
mark_model_as_no_longer_needed #INFERNUS  // allow unload
```

## 9. Proximity Check

```
if
    locate_char_on_foot_3d $scplayer {pos} targetX targetY targetZ {radius} 5.0 5.0 5.0 {drawSphere} false
then
    // player is within 5 units of target
end
```

## 10. Timer-Based Actions

```
TimerA = 0

// In loop:
if
    TimerA >= 3000     // every 3 seconds
then
    TimerA = 0
    // do periodic action
end
```

## 11. Screen Fade Transition

```
set_player_control $player1 {state} false
do_fade {time} 500 {direction} Fade.Out
wait {time} 500

// ... change state while screen is black ...

do_fade {time} 500 {direction} Fade.In
set_player_control $player1 {state} true
```

## 12. Audio Playback

```
int stream = load_audio_stream "cleo\mysound.mp3"
set_audio_stream_state stream AudioStreamAction.Play
set_audio_stream_volume stream 1.0

// Later, to stop and clean up:
set_audio_stream_state stream AudioStreamAction.Stop
remove_audio_stream stream
```

## 13. 3D Audio (Positional Sound)

```
int stream = load_3d_audio_stream "cleo\sound.mp3"
set_play_3d_audio_stream_at_coord stream {pos} x y z
set_audio_stream_looped stream true
set_audio_stream_state stream AudioStreamAction.Play
```

## 14. Memory Read/Write

```
// Read a value from game memory
int value = read_memory {address} 0xB7CE50 {size} 4 {vp} false

// Write a value
write_memory {address} 0xB7CE50 {size} 4 {value} 100 {vp} false

// Read with struct offset
int ptr = get_vehicle_pointer carHandle
int flags = read_memory_with_offset {address} ptr {offset} 0xCC {size} 4
```

## 15. Blip Management

```
int blip = add_blip_for_coord {pos} x y z
change_blip_colour blip {color} BlipColor.Red
change_blip_scale blip {size} 3

// Cleanup when done:
remove_blip blip
```

## 16. Object Creation

```
request_model {modelId} #ROADBARRIER1
load_all_models_now

int obj = create_object {modelId} #ROADBARRIER1 {xyz} x y z
mark_model_as_no_longer_needed {modelId} #ROADBARRIER1

set_object_heading obj {heading} 90.0
set_object_collision obj {state} true

// Cleanup:
delete_object obj
```

## 17. Weapon Management

```
// Give weapon (model must be loaded first)
int weaponModel = get_weapontype_model {weaponType} WeaponType.M4
request_model {modelId} weaponModel
load_all_models_now
give_weapon_to_char $scplayer {weaponType} WeaponType.M4 {ammo} 500
mark_model_as_no_longer_needed {modelId} weaponModel
```

## 18. Save-Persistent Script

```
{$CLEO .cs}
script_name {name} 'persist'

// This makes the script survive save/load
save_this_custom_script

wait {time} 0
wait {time} 0

int myState = 0    // will be restored after loading savegame

while true
    wait {time} 0
    // ... your persistent logic ...
end
```

## 19. Custom Mission

```
{$CLEO .cm}          // .cm = custom mission

script_name {name} 'mymiss'

// Mission scripts run one at a time
// Use mission-specific opcodes
set_player_control $player1 {state} false
do_fade {time} 500 {direction} Fade.Out
wait {time} 500

// ... setup mission environment ...

do_fade {time} 500 {direction} Fade.In
set_player_control $player1 {state} true

// Main mission loop
while true
    wait {time} 0
    // ... mission logic, objectives ...
end

// End mission
mission_cleanup
terminate_this_custom_script
```

## 20. Condition Result (CLEO5 Functions)

```
// Function that returns a condition (true/false) + values
function FIND_NEAREST_CAR(): int
    // ... search logic ...
    if
        found == true
    then
        cleo_return_with {conditionResult} true {retArgs} carHandle
    else
        cleo_return_with {conditionResult} false {retArgs} -1
    end
end

// Usage:
if
    carHandle = FIND_NEAREST_CAR()
then
    // found a car
end
```

---

## Text Formatting Codes

Use these in print strings:

| Code | Effect |
|------|--------|
| `~n~` | Newline |
| `~r~` | Red text |
| `~g~` | Green text |
| `~b~` | Blue text |
| `~y~` | Yellow text |
| `~p~` | Purple text |
| `~w~` | White text |
| `~s~` | Default (reset) |
| `~h~` | Brighter shade (stackable) |
| `~l~` | Darker shade |
