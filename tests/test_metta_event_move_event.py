import unittest

from metta.events.move_event import MoveEvent


class TestMettaEventMoveEvent(unittest.TestCase):
    def test_to_metta(self):
        from_location = "glade"
        to_location = "cave"
        move_event_metta = MoveEvent(from_location, to_location).to_metta()
        self.assertEqual(move_event_metta, f"(move {from_location} {to_location})")


if __name__ == "__main__":
    unittest.main()
