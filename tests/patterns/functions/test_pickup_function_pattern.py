import unittest

from metta.patterns.functions.pickup_function_pattern import PickUpFunctionPattern


class TestPickUpFunctionPattern(unittest.TestCase):
    def test_to_metta(self):
        what = "coin"
        pickup = PickUpFunctionPattern(what)
        self.assertEqual(pickup.to_metta(), f"(pickup ({what}))")


if __name__ == "__main__":
    unittest.main()
