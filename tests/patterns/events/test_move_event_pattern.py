import unittest

from metta.patterns.events.move_event_pattern import MoveEventPattern


class TestMoveEventPattern(unittest.TestCase):
    def test_to_metta(self):
        from_location = "glade"
        to_location = "cave"
        move_event = MoveEventPattern(from_location, to_location)
        self.assertEqual(move_event.to_metta(), f"(Move {from_location} {to_location})")


if __name__ == "__main__":
    unittest.main()
