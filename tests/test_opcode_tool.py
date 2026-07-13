from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "opcode_tool", ROOT / "tools" / "opcode_lookup.py"
)
assert SPEC and SPEC.loader
OPCODE_TOOL = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = OPCODE_TOOL
SPEC.loader.exec_module(OPCODE_TOOL)


class OpcodeToolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.commands = OPCODE_TOOL.load_commands(ROOT / "source_data" / "sa.json")

    def test_show_can_disambiguate_extension(self) -> None:
        matches = OPCODE_TOOL.show(self.commands, "0F12", "CLEO+")
        self.assertEqual(1, len(matches))
        self.assertEqual("GET_CAMERA_STRUCT", matches[0]["name"])
        self.assertEqual("cCamera", matches[0]["output"][0]["name"])

    def test_search_prioritizes_exact_name(self) -> None:
        matches = OPCODE_TOOL.search(self.commands, "create car", 5)
        self.assertEqual("CREATE_CAR", matches[0]["name"])


if __name__ == "__main__":
    unittest.main()
