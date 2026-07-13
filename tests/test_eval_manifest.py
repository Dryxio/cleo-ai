from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class EvalManifestTests(unittest.TestCase):
    def test_manifest_has_stable_unique_cases(self) -> None:
        cases = json.loads((ROOT / "evals" / "prompts.json").read_text(encoding="utf-8"))
        self.assertGreaterEqual(len(cases), 20)
        ids = [case["id"] for case in cases]
        self.assertEqual(len(ids), len(set(ids)))
        for case in cases:
            self.assertTrue(case["prompt"])
            self.assertIsInstance(case["extensions"], list)
            self.assertGreaterEqual(len(case["manual_checks"]), 1)


if __name__ == "__main__":
    unittest.main()
