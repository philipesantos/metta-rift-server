import unittest

from core.definitions.wrappers.state_wrapper_definition import StateWrapperDefinition
from core.patterns.functions.trigger_function_pattern import TriggerFunctionPattern
from core.patterns.wrappers.log_wrapper_pattern import LogWrapperPattern
from core.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern
from core.patterns.facts.tick_fact_pattern import TickFactPattern
from tests.utils.metta import get_test_metta

from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.patterns.facts.character_fact_pattern import CharacterFactPattern
from core.patterns.events.move_event_pattern import MoveEventPattern
from core.definitions.functions.trigger_function_definition import (
    TriggerFunctionDefinition,
)
from core.definitions.side_effects.on_move_update_at import OnMoveUpdateAt
from tests.utils.utils import unwrap_first_match, count_atoms, unwrap_match


class TestOnMoveUpdateAt(unittest.TestCase):
    def test_to_metta(self):
        metta = get_test_metta()

        character = CharacterFactPattern("player", "John")
        tick_state = StateWrapperPattern(TickFactPattern("0"))

        metta.run(tick_state.to_metta())
        metta.run(
            StateWrapperDefinition(AtFactPattern(character.key, "glade")).to_metta()
        )

        trigger = TriggerFunctionDefinition(
            MoveEventPattern("$from", "$to"), [OnMoveUpdateAt(character)]
        )
        metta.run(trigger.to_metta())

        log_move = LogWrapperPattern("$tick", MoveEventPattern("$from", "$to"))
        state_at = StateWrapperPattern(AtFactPattern(character.key, "$where"))

        trigger_1 = TriggerFunctionPattern(MoveEventPattern("glade", "cave"))
        metta.run(f"!{trigger_1.to_metta()}")

        result_1_1 = metta.run(
            f"!(match &self {log_move.to_metta()} {log_move.to_metta()})"
        )
        self.assertEqual(
            unwrap_first_match(result_1_1),
            LogWrapperPattern("0", MoveEventPattern("glade", "cave")).to_metta(),
        )
        self.assertEqual(count_atoms(result_1_1), 1)

        result_1_2 = metta.run(
            f"!(match &self {state_at.to_metta()} {state_at.to_metta()})"
        )
        self.assertEqual(
            unwrap_first_match(result_1_2),
            StateWrapperPattern(AtFactPattern(character.key, "cave")).to_metta(),
        )
        self.assertEqual(count_atoms(result_1_2), 1)

        metta.run(f"!(remove-atom &self {tick_state.to_metta()})")
        metta.run(
            f"!(add-atom &self {StateWrapperPattern(TickFactPattern('1')).to_metta()})"
        )

        trigger_metta_usage_2 = TriggerFunctionPattern(
            MoveEventPattern("cave", "beach")
        )
        metta.run(f"!{trigger_metta_usage_2.to_metta()}")

        result_2_1 = metta.run(
            f"!(match &self {log_move.to_metta()} {log_move.to_metta()})"
        )
        self.assertIn(
            unwrap_match(result_2_1, 0),
            [
                LogWrapperPattern("0", MoveEventPattern("glade", "cave")).to_metta(),
                LogWrapperPattern("1", MoveEventPattern("cave", "beach")).to_metta(),
            ],
        )
        self.assertIn(
            unwrap_match(result_2_1, 1),
            [
                LogWrapperPattern("0", MoveEventPattern("glade", "cave")).to_metta(),
                LogWrapperPattern("1", MoveEventPattern("cave", "beach")).to_metta(),
            ],
        )
        self.assertEqual(count_atoms(result_2_1), 2)

        result_2_2 = metta.run(
            f"!(match &self {state_at.to_metta()} {state_at.to_metta()})"
        )
        self.assertEqual(
            unwrap_first_match(result_2_2),
            StateWrapperPattern(AtFactPattern(character.key, "beach")).to_metta(),
        )
        self.assertEqual(count_atoms(result_2_2), 1)


if __name__ == "__main__":
    unittest.main()
