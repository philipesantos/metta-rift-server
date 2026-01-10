import unittest

from core.patterns.events.move_event_pattern import MoveEventPattern
from core.patterns.events.pickup_event_pattern import PickUpEventPattern


class TestPickUpEventPattern(unittest.TestCase):
    def test_to_metta(self):
        what = "compass"
        where = "glade"
        pickup_event = PickUpEventPattern(what, where)
        self.assertEqual(pickup_event.to_metta(), f"(PickUp {what} {where})")


if __name__ == "__main__":
    unittest.main()
