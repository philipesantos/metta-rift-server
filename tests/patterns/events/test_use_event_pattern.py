import unittest

from core.patterns.events.use_event_pattern import UseEventPattern


class TestUseEventPattern(unittest.TestCase):
    def test_to_metta(self):
        use_event = UseEventPattern("crescent_rock", "cave_door")
        self.assertEqual(use_event.to_metta(), "(Use crescent_rock cave_door)")


if __name__ == "__main__":
    unittest.main()
