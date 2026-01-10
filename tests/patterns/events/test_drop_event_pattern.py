import unittest

from core.patterns.events.drop_event_pattern import DropEventPattern
from core.patterns.events.move_event_pattern import MoveEventPattern
from core.patterns.events.pickup_event_pattern import PickUpEventPattern


class TestDropEventPattern(unittest.TestCase):
    def test_to_metta(self):
        what = "compass"
        where = "glade"
        drop_event = DropEventPattern(what, where)
        self.assertEqual(drop_event.to_metta(), f"(Drop {what} {where})")


if __name__ == "__main__":
    unittest.main()
