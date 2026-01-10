import unittest

from core.patterns.functions.move_towards_function_pattern import (
    MoveTowardsFunctionPattern,
)

from utils.direction import Direction


class TestMoveTowardsFunctionPattern(unittest.TestCase):
    def test_to_metta(self):
        direction = Direction.WEST
        move_towards = MoveTowardsFunctionPattern(direction)
        self.assertEqual(move_towards.to_metta(), f"(move-towards ({direction.value}))")


if __name__ == "__main__":
    unittest.main()
