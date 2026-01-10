import unittest

from core.patterns.functions.move_to_function_pattern import MoveToFunctionPattern


class TestMoveToFunctionPattern(unittest.TestCase):
    def test_to_metta(self):
        where = "glade"
        move_to = MoveToFunctionPattern(where)
        self.assertEqual(move_to.to_metta(), f"(move-to ({where}))")


if __name__ == "__main__":
    unittest.main()
