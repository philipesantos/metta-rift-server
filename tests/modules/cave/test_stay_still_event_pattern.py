import unittest

from modules.cave.patterns.stay_still_event_pattern import StayStillEventPattern


class TestStayStillEventPattern(unittest.TestCase):
    def test_to_metta(self):
        event = StayStillEventPattern("glade")
        self.assertEqual(event.to_metta(), "(StayStill glade)")


if __name__ == "__main__":
    unittest.main()
