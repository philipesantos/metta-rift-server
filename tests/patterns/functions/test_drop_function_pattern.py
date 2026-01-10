import unittest

from core.patterns.functions.drop_function_pattern import DropFunctionPattern


class TestDropFunctionPattern(unittest.TestCase):
    def test_to_metta(self):
        what = "coin"
        drop = DropFunctionPattern(what)
        self.assertEqual(drop.to_metta(), f"(drop ({what}))")


if __name__ == "__main__":
    unittest.main()
