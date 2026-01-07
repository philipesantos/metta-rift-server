import unittest

from metta.patterns.functions.trigger_function_pattern import TriggerFunctionPattern
from tests.utils.metta import get_test_metta

from metta.patterns.events.move_event_pattern import MoveEventPattern
from metta.definitions.functions.trigger_function_definition import TriggerFunctionDefinition
from metta.definitions.side_effects.on_move_describe_location import OnMoveDescribeLocation
from tests.utils.utils import unwrap_first_match


class TestOnMoveDescribeLocation(unittest.TestCase):
    def test_to_metta(self):
        metta = get_test_metta()

        text = "Location description"
        side_effect = OnMoveDescribeLocation(text)

        trigger = TriggerFunctionDefinition(MoveEventPattern("$from", "glade"), [side_effect])
        metta.run(trigger.to_metta())

        trigger_metta_usage = TriggerFunctionPattern(MoveEventPattern("cave", "glade"))
        result = metta.run(f"!{trigger_metta_usage.to_metta()}")
        self.assertEqual(unwrap_first_match(result), text)


if __name__ == "__main__":
    unittest.main()
