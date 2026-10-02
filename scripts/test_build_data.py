import json
import runpy
import unittest
from pathlib import Path


builder = runpy.run_path(str(Path(__file__).with_name("build-data.py")))
validate_data = builder["validate_data"]
render_sources = builder["render_sources"]
ROOT = Path(__file__).resolve().parent.parent


class BuildDataTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "data/codes.json").read_text(encoding="utf-8"))

    def test_current_data_is_valid_and_generated_files_are_current(self):
        for path, content in render_sources(self.data).items():
            self.assertEqual(path.read_text(encoding="utf-8"), content, str(path))

    def test_rejects_invalid_records(self):
        invalid = [
            [],
            {},
            [{"city": "Mzuzu", "code": 3020, "region": "Northern"}],
            [{"city": " Mzuzu", "code": "3020", "region": "Northern"}],
            [{"city": "Mzuzu", "code": "٣٠٢٠", "region": "Northern"}],
            [{"city": "Mzuzu", "code": "3020", "region": []}],
            [{"city": "Mzuzu", "code": "3020", "region": "Northern", "other": 1}],
        ]
        for records in invalid:
            with self.subTest(records=records), self.assertRaises(ValueError):
                validate_data(records)

    def test_rejects_duplicate_codes_and_case_insensitive_cities(self):
        for duplicate in (
            {"city": "Another", "code": "3020", "region": "Northern"},
            {"city": "mZuZu", "code": "9999", "region": "Northern"},
        ):
            with self.subTest(duplicate=duplicate), self.assertRaises(ValueError):
                validate_data([self.data[0], duplicate])

    def test_escapes_go_string_literals(self):
        entry = {"city": 'A "quoted"\\ town', "code": "9999", "region": "Northern"}
        go = render_sources([entry])[ROOT / "go/codes.go"]
        self.assertIn('City: "A \\"quoted\\"\\\\ town"', go)


if __name__ == "__main__":
    unittest.main()
