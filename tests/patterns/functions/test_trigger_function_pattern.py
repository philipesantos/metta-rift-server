import unittest

from metta.patterns.events.move_event_pattern import MoveEventPattern
from metta.patterns.functions.trigger_function_pattern import TriggerFunctionPattern


class TestTriggerFunctionPattern(unittest.TestCase):
    def test_to_metta(self):
        event = MoveEventPattern("glade", "cave")
        trigger = TriggerFunctionPattern(event)
        self.assertEqual(trigger.to_metta(), f"(trigger {event.to_metta()})")


if __name__ == "__main__":
    unittest.main()
