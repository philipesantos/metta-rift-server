import unittest

from metta.definitions.facts.current_at_fact_definition import CurrentAtFactDefinition
from metta.patterns.functions.trigger_function_pattern import TriggerFunctionPattern
from metta.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern
from metta.patterns.facts.tick_fact_pattern import TickFactPattern
from tests.utils.metta import get_test_metta

from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.patterns.facts.character_fact_pattern import CharacterFactPattern
from metta.patterns.facts.current_at_fact_pattern import CurrentAtFactPattern
from metta.patterns.events.move_event_pattern import MoveEventPattern
from metta.definitions.functions.trigger_function_definition import TriggerFunctionDefinition
from metta.definitions.side_effects.on_move_update_at import OnMoveUpdateAt
from tests.utils.utils import unwrap_first_match, count_atoms, unwrap_match


class TestOnMoveUpdateAt(unittest.TestCase):
    def test_to_metta(self):
        metta = get_test_metta()

        character = CharacterFactPattern("player", "John")
        tick_state = StateWrapperPattern(TickFactPattern("0"))

        metta.run(tick_state.to_metta())
        metta.run(CurrentAtFactDefinition(character.key, "glade").to_metta())

        trigger = TriggerFunctionDefinition(MoveEventPattern("$from", "$to"), [OnMoveUpdateAt(character)])
        metta.run(trigger.to_metta())

        at = AtFactPattern("$tick", character.key, "$where")
        current_at = CurrentAtFactPattern(character.key, "$where")

        trigger_1 = TriggerFunctionPattern(MoveEventPattern("glade", "cave"))
        metta.run(f"!{trigger_1.to_metta()}")

        result_1_1 = metta.run(f"!(match &self {at.to_metta()} {at.to_metta()})")
        self.assertEqual(
            unwrap_first_match(result_1_1),
            AtFactPattern("0", character.key, "cave").to_metta(),
        )
        self.assertEqual(count_atoms(result_1_1), 1)

        result_1_2 = metta.run(f"!(match &self {current_at.to_metta()} {current_at.to_metta()})")
        self.assertEqual(
            unwrap_first_match(result_1_2),
            CurrentAtFactPattern(character.key, "cave").to_metta(),
        )
        self.assertEqual(count_atoms(result_1_2), 1)

        metta.run(f"!(remove-atom &self {tick_state.to_metta()})")
        metta.run(
            f"!(add-atom &self {StateWrapperPattern(TickFactPattern('1')).to_metta()})"
        )

        trigger_metta_usage_2 = TriggerFunctionPattern(MoveEventPattern("cave", "beach"))
        metta.run(f"!{trigger_metta_usage_2.to_metta()}")

        result_2_1 = metta.run(f"!(match &self {at.to_metta()} {at.to_metta()})")
        self.assertIn(
            unwrap_match(result_2_1, 0),
            [
                AtFactPattern("0", character.key, "cave").to_metta(),
                AtFactPattern("1", character.key, "beach").to_metta(),
            ],
        )
        self.assertIn(
            unwrap_match(result_2_1, 1),
            [
                AtFactPattern("0", character.key, "cave").to_metta(),
                AtFactPattern("1", character.key, "beach").to_metta(),
            ],
        )
        self.assertEqual(count_atoms(result_2_1), 2)

        result_2_2 = metta.run(f"!(match &self {current_at.to_metta()} {current_at.to_metta()})")
        self.assertEqual(
            unwrap_first_match(result_2_2),
            CurrentAtFactPattern(character.key, "beach").to_metta(),
        )
        self.assertEqual(count_atoms(result_2_2), 1)


if __name__ == "__main__":
    unittest.main()
