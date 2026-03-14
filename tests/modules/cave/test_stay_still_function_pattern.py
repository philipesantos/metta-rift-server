import unittest

from modules.cave.patterns.stay_still_function_pattern import (
    StayStillFunctionPattern,
)


class TestStayStillFunctionPattern(unittest.TestCase):
    def test_to_metta(self):
        stay_still = StayStillFunctionPattern()
        self.assertEqual(stay_still.to_metta(), "(stay-still)")


if __name__ == "__main__":
    unittest.main()
