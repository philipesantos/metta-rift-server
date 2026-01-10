import unittest

from metta.patterns.functions.location_path_function_pattern import (
    LocationPathFunctionPattern,
)


class TestLocationPathFunctionPattern(unittest.TestCase):
    def test_to_metta(self):
        location_path = LocationPathFunctionPattern("player")
        self.assertEqual(location_path.to_metta(), "(location-path (player))")


if __name__ == "__main__":
    unittest.main()
