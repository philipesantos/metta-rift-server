import unittest

from core.patterns.events.use_item_event_pattern import UseItemEventPattern


class TestUseItemEventPattern(unittest.TestCase):
    def test_to_metta(self):
        use_event = UseItemEventPattern("lantern")
        self.assertEqual(use_event.to_metta(), "(Use lantern)")


if __name__ == "__main__":
    unittest.main()
