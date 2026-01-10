import unittest

from core.definitions.wrappers.stale_wrapper_definition import StaleWrapperDefinition
from core.patterns.functions.trigger_function_pattern import TriggerFunctionPattern
from core.patterns.wrappers.stale_wrapper_pattern import StaleWrapperPattern
from tests.utils.metta import get_test_metta

from core.patterns.events.move_event_pattern import MoveEventPattern
from core.definitions.functions.exists_function_definition import (
    ExistsFunctionDefinition,
)
from core.definitions.functions.trigger_function_definition import (
    TriggerFunctionDefinition,
)
from core.definitions.side_effects.on_move_update_tick import OnMoveUpdateTick
from tests.utils.utils import unwrap_first_match, count_atoms


class TestOnMoveUpdateTick(unittest.TestCase):
    def test_to_metta(self):
        metta = get_test_metta()

        metta.run(ExistsFunctionDefinition().to_metta())

        trigger = TriggerFunctionDefinition(
            MoveEventPattern("$from", "$to"), [OnMoveUpdateTick()]
        )
        metta.run(trigger.to_metta())

        trigger_1 = TriggerFunctionPattern(MoveEventPattern("cave", "glade"))
        metta.run(f"!{trigger_1.to_metta()}")

        result_1 = metta.run(
            f"!(match &self {StaleWrapperPattern('Tick').to_metta()} True)"
        )
        self.assertEqual(unwrap_first_match(result_1), True)
        self.assertEqual(count_atoms(result_1), 1)

        trigger_2 = TriggerFunctionPattern(MoveEventPattern("glade", "beach"))
        metta.run(f"!{trigger_2}")

        result_2 = metta.run(
            f"!(match &self {StaleWrapperPattern('Tick').to_metta()} True)"
        )
        self.assertEqual(unwrap_first_match(result_2), True)
        self.assertEqual(count_atoms(result_2), 1)


if __name__ == "__main__":
    unittest.main()
