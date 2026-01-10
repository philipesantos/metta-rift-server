import unittest

from metta.patterns.functions.inventory_function_pattern import (
    InventoryFunctionPattern,
)


class TestInventoryFunctionPattern(unittest.TestCase):
    def test_to_metta(self):
        inventory = InventoryFunctionPattern()
        self.assertEqual(inventory.to_metta(), "(inventory)")


if __name__ == "__main__":
    unittest.main()
