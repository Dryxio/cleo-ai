# CLEO AI benchmark

`prompts.json` is a stable prompt set for measuring script-generation quality.
For each generated source file:

1. run `python3 tools/validate_workspace.py generated.txt --strict`;
2. compile it with the pinned Sanny Builder profile;
3. record first-pass compile success and success after one repair;
4. verify the listed manual checks in game.

Do not compare generated scripts byte-for-byte. Score observable requirements,
declared dependencies, validation, compilation, cleanup, and runtime behavior.
