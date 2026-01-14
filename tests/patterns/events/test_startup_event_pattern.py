import unittest

from core.patterns.events.startup_event_pattern import StartupEventPattern


class TestStartupEventPattern(unittest.TestCase):
    def test_to_metta(self):
        startup_event = StartupEventPattern()
        self.assertEqual(startup_event.to_metta(), "(Startup)")


if __name__ == "__main__":
    unittest.main()
