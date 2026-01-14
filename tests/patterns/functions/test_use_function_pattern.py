import unittest

from core.patterns.functions.use_function_pattern import UseFunctionPattern


class TestUseFunctionPattern(unittest.TestCase):
    def test_to_metta(self):
        use_function = UseFunctionPattern("crescent_rock", "cave_door")
        self.assertEqual(use_function.to_metta(), "(use (crescent_rock cave_door))")


if __name__ == "__main__":
    unittest.main()
