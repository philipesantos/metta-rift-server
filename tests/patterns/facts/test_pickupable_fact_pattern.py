import unittest

from core.patterns.facts.pickupable_fact_pattern import PickupableFactPattern
from utils.type import Type


class TestPickupableFactPattern(unittest.TestCase):
    def test_to_metta(self):
        key = "compass"
        pickupable = PickupableFactPattern(key)
        self.assertEqual(pickupable.to_metta(), f"({Type.PICKUPABLE.value} {key})")


if __name__ == "__main__":
    unittest.main()
