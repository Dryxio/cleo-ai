from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_workspace", ROOT / "tools" / "validate_workspace.py"
)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)


class ValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = VALIDATOR.load_catalog(ROOT / "source_data" / "sa.json")
        cls.profile = VALIDATOR.load_json(ROOT / "config" / "target-profile.json")

    def validate(self, source: str):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.txt"
            path.write_text(source, encoding="utf-8")
            return VALIDATOR.validate_file(path, self.catalog, self.profile)

    def test_valid_minimal_script(self) -> None:
        findings = self.validate(
            """{$CLEO .cs}
script_name {name} 'valid'
while true
    wait {time} 0
end
"""
        )
        self.assertEqual([], [item for item in findings if item.severity == "ERROR"])

    def test_unknown_opcode_is_rejected(self) -> None:
        findings = self.validate(
            """{$CLEO .cs}
script_name {name} 'badop'
invented_opcode
"""
        )
        self.assertTrue(any("unknown opcode name" in item.message for item in findings))

    def test_unknown_single_word_opcode_is_rejected(self) -> None:
        findings = self.validate(
            """{$CLEO .cs}
script_name {name} 'badword'
heal
"""
        )
        self.assertTrue(any("unknown opcode name" in item.message for item in findings))

    def test_requested_model_requires_release(self) -> None:
        findings = self.validate(
            """{$CLEO .cs}
script_name {name} 'models'
request_model {modelId} 411
load_all_models_now
"""
        )
        self.assertTrue(any("never marked as no longer needed" in item.message for item in findings))

    def test_display_text_rejects_literal(self) -> None:
        findings = self.validate(
            """{$CLEO .cs}
script_name {name} 'text'
display_text {pos} 10.0 10.0 {text} "literal"
"""
        )
        self.assertTrue(any("expects a GXT key" in item.message for item in findings))

    def test_opt_in_extension_requires_use_directive(self) -> None:
        findings = self.validate(
            """{$CLEO .cs}
script_name {name} 'plus'
get_current_weather
"""
        )
        self.assertTrue(any("extension is not enabled" in item.message for item in findings))

    def test_unbounded_loop_requires_wait(self) -> None:
        findings = self.validate(
            """{$CLEO .cs}
script_name {name} 'loop'
while true
    print_help_string {text} "busy"
end
"""
        )
        self.assertTrue(any("while loop has no wait" in item.message for item in findings))


if __name__ == "__main__":
    unittest.main()
