# Conversation Opcodes

> 11 opcodes in this class

## Quick Reference

| Opcode | Name | Description |
|--------|------|-------------|
| `0717` | START_SETTING_UP_CONVERSATION | Starts a conversation between the character and the player and clears the conver |
| `0719` | FINISH_SETTING_UP_CONVERSATION | Finalizes the current conversation sequence started with 0717. Selected answers  |
| `071A` | IS_CONVERSATION_AT_NODE | Returns true if the conversation is at the specified node |
| `089B` | IS_PLAYER_IN_POSITION_FOR_CONVERSATION | Returns true if there is a conversation going on between the character and the p |
| `089C` | ENABLE_CONVERSATION | Pauses the scripted conversation assigned to the specified character |
| `08ED` | CLEAR_CONVERSATION_FOR_CHAR |  |
| `09A4` | SET_UP_CONVERSATION_NODE_WITH_SPEECH | Specifies the dialogue GXT's and audio ID's |
| `09AA` | SET_UP_CONVERSATION_END_NODE_WITH_SPEECH | Sets the speech sound for the specified conversation response node |
| `0A18` | SET_UP_CONVERSATION_NODE_WITH_SCRIPTED_SPEECH | Adds a new line to the scripted conversation |
| `0A3C` | SET_UP_CONVERSATION_END_NODE_WITH_SCRIPTED_SPEECH | Sets the script audio ID (see 03CF) for the specified conversation response node |
| `0A47` | FINISH_SETTING_UP_CONVERSATION_NO_SUBTITLES | Finalizes the current conversation sequence started with 0717. Selected answers  |

## Detailed Reference

### `0717` START_SETTING_UP_CONVERSATION
Starts a conversation between the character and the player and clears the conversation lines

**Class:** `Conversation.StartSettingUp`
**Flags:** static

**Input:**
- `handle: Char`

---

### `0719` FINISH_SETTING_UP_CONVERSATION
Finalizes the current conversation sequence started with 0717. Selected answers will be subtitled

**Class:** `Conversation.FinishSettingUp`
**Flags:** static

---

### `071A` IS_CONVERSATION_AT_NODE
Returns true if the conversation is at the specified node

**Class:** `Conversation.IsAtNode`
**Flags:** condition, static

**Input:**
- `handle: Char`
- `speech: gxt_key`

---

### `089B` IS_PLAYER_IN_POSITION_FOR_CONVERSATION
Returns true if there is a conversation going on between the character and the player and both the character and the player are able to communicate with one another

**Class:** `Conversation.IsPlayerInPosition`
**Flags:** condition, static

**Input:**
- `handle: Char`

---

### `089C` ENABLE_CONVERSATION
Pauses the scripted conversation assigned to the specified character

**Class:** `Conversation.Enable`
**Flags:** static

**Input:**
- `handle: Char`
- `state: bool`

---

### `08ED` CLEAR_CONVERSATION_FOR_CHAR

**Class:** `Conversation.ClearForChar`
**Flags:** static

**Input:**
- `handle: Char`

---

### `09A4` SET_UP_CONVERSATION_NODE_WITH_SPEECH
Specifies the dialogue GXT's and audio ID's

**Class:** `Conversation.SetUpNodeWithSpeech`
**Flags:** static

**Input:**
- `question: gxt_key`
- `positiveAnswer: gxt_key`
- `negativeAnswer: gxt_key`
- `questionPhrase: SpeechId`
- `positiveAnswerPhrase: SpeechId`
- `negativeAnswerPhrase: SpeechId`

---

### `09AA` SET_UP_CONVERSATION_END_NODE_WITH_SPEECH
Sets the speech sound for the specified conversation response node

**Class:** `Conversation.SetUpEndNodeWithSpeech`
**Flags:** static

**Input:**
- `text: gxt_key`
- `phrase: SpeechId`

---

### `0A18` SET_UP_CONVERSATION_NODE_WITH_SCRIPTED_SPEECH
Adds a new line to the scripted conversation

**Class:** `Conversation.SetUpNodeWithScriptedSpeech`
**Flags:** static

**Input:**
- `question: gxt_key`
- `positiveAnswer: gxt_key`
- `negativeAnswer: gxt_key`
- `questionSoundId: int`
- `positiveAnswerSoundId: int`
- `negativeAnswerSoundId: int`

---

### `0A3C` SET_UP_CONVERSATION_END_NODE_WITH_SCRIPTED_SPEECH
Sets the script audio ID (see 03CF) for the specified conversation response node

**Class:** `Conversation.SetUpEndNodeWithScriptedSpeech`
**Flags:** static

**Input:**
- `speech: gxt_key`
- `speechSoundId: int`

---

### `0A47` FINISH_SETTING_UP_CONVERSATION_NO_SUBTITLES
Finalizes the current conversation sequence started with 0717. Selected answers will not be subtitled

**Class:** `Conversation.FinishSettingUpNoSubtitles`
**Flags:** static

---
