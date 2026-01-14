import unittest

from core.definitions.side_effects.on_use_do_nothing import OnUseDoNothing
from core.patterns.events.use_event_pattern import UseEventPattern
from core.patterns.functions.trigger_function_pattern import TriggerFunctionPattern
from core.definitions.functions.trigger_function_definition import (
    TriggerFunctionDefinition,
)
from tests.utils.metta import get_test_metta
from tests.utils.utils import unwrap_first_match


class TestOnUseDoNothing(unittest.TestCase):
    def test_to_metta(self):
        metta = get_test_metta()

        trigger = TriggerFunctionDefinition(
            UseEventPattern("$what", "$with_what"),
            [OnUseDoNothing()],
        )
        metta.run(trigger.to_metta())

        trigger_use = TriggerFunctionPattern(
            UseEventPattern("crescent_rock", "cave_door")
        )
        result = metta.run(f"!{trigger_use.to_metta()}")

        self.assertEqual(result, [[]])


if __name__ == "__main__":
    unittest.main()
