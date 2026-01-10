import unittest

from metta.definitions.wrappers.state_wrapper_definition import StateWrapperDefinition
from metta.patterns.functions.trigger_function_pattern import TriggerFunctionPattern
from metta.patterns.wrappers.log_wrapper_pattern import LogWrapperPattern
from metta.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern
from metta.patterns.facts.tick_fact_pattern import TickFactPattern
from tests.utils.metta import get_test_metta

from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.patterns.facts.character_fact_pattern import CharacterFactPattern
from metta.patterns.events.pickup_event_pattern import PickUpEventPattern
from metta.definitions.functions.trigger_function_definition import (
    TriggerFunctionDefinition,
)
from metta.definitions.side_effects.on_pickup_update_at import OnPickUpUpdateAt
from tests.utils.utils import unwrap_first_match, count_atoms


class TestOnPickUpUpdateAt(unittest.TestCase):
    def test_to_metta(self):
        metta = get_test_metta()

        character = CharacterFactPattern("player", "John")

        tick_state = StateWrapperPattern(TickFactPattern("0"))
        metta.run(tick_state.to_metta())
        metta.run(
            StateWrapperDefinition(AtFactPattern("coin", "glade")).to_metta()
        )

        trigger = TriggerFunctionDefinition(
            PickUpEventPattern("$what", "$where"), [OnPickUpUpdateAt(character)]
        )
        metta.run(trigger.to_metta())

        log_pickup = LogWrapperPattern("$tick", PickUpEventPattern("$what", "$where"))
        state_at = StateWrapperPattern(AtFactPattern("coin", "$where"))

        trigger_pickup = TriggerFunctionPattern(PickUpEventPattern("coin", "glade"))
        metta.run(f"!{trigger_pickup.to_metta()}")

        result_log = metta.run(
            f"!(match &self {log_pickup.to_metta()} {log_pickup.to_metta()})"
        )
        self.assertEqual(
            unwrap_first_match(result_log),
            LogWrapperPattern("0", PickUpEventPattern("coin", "glade")).to_metta(),
        )
        self.assertEqual(count_atoms(result_log), 1)

        result_state = metta.run(
            f"!(match &self {state_at.to_metta()} {state_at.to_metta()})"
        )
        self.assertEqual(
            unwrap_first_match(result_state),
            StateWrapperPattern(AtFactPattern("coin", character.key)).to_metta(),
        )
        self.assertEqual(count_atoms(result_state), 1)

        result_old_state = metta.run(
            f"!(match &self {StateWrapperPattern(AtFactPattern('coin', 'glade')).to_metta()} True)"
        )
        self.assertEqual(result_old_state, [[]])


if __name__ == "__main__":
    unittest.main()
