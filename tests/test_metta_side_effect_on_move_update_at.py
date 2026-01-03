import unittest

from metta.atoms.wrappers.state import State
from metta.atoms.tick import Tick
from tests.utils.metta import get_test_metta

from metta.atoms.at import At
from metta.atoms.character import Character
from metta.atoms.current_at import CurrentAt
from metta.events.move_event import MoveEvent
from metta.functions.trigger import Trigger
from metta.side_effects.on_move_update_at import OnMoveUpdateAt
from tests.utils.utils import unwrap_first_match, count_atoms, unwrap_match


class TestMettaSideEffectOnMoveUpdateAt(unittest.TestCase):

    def test_to_metta_definition(self):
        metta = get_test_metta()

        character = Character("player", "John")
        tick_state = State(Tick("0").to_metta_definition())

        metta.run(tick_state.to_metta_definition())
        metta.run(CurrentAt(character.key, "glade").to_metta_definition())

        trigger = Trigger(MoveEvent("$from", "$to"), [OnMoveUpdateAt(character)])
        metta.run(trigger.to_metta_definition())

        at_usage = At.to_metta_usage("$tick", character.key, "$where")
        current_at_usage = CurrentAt.to_metta_usage(character.key, "$where")

        trigger_metta_usage_1 = Trigger.to_metta_usage(MoveEvent("glade", "cave"))
        metta.run(f"!{trigger_metta_usage_1}")

        result_1_1 = metta.run(f"!(match &self {at_usage} {at_usage})")
        self.assertEqual(unwrap_first_match(result_1_1), At.to_metta_usage("0", character.key, "cave"))
        self.assertEqual(count_atoms(result_1_1), 1)

        result_1_2 = metta.run(f"!(match &self {current_at_usage} {current_at_usage})")
        self.assertEqual(unwrap_first_match(result_1_2), CurrentAt.to_metta_usage(character.key, "cave"))
        self.assertEqual(count_atoms(result_1_2), 1)

        metta.run(f"!(remove-atom &self {tick_state.to_metta_definition()})")
        metta.run(f"!(add-atom &self {State(Tick("1").to_metta_definition()).to_metta_definition()})")

        trigger_metta_usage_2 = Trigger.to_metta_usage(MoveEvent("cave", "beach"))
        metta.run(f"!{trigger_metta_usage_2}")

        result_2_1 = metta.run(f"!(match &self {at_usage} {at_usage})")
        self.assertIn(unwrap_match(result_2_1, 0),[
            At.to_metta_usage("0", character.key, "cave"),
            At.to_metta_usage("1", character.key, "beach")
        ])
        self.assertIn(unwrap_match(result_2_1, 1),[
            At.to_metta_usage("0", character.key, "cave"),
            At.to_metta_usage("1", character.key, "beach")
        ])
        self.assertEqual(count_atoms(result_2_1), 2)

        result_2_2 = metta.run(f"!(match &self {current_at_usage} {current_at_usage})")
        self.assertEqual(unwrap_first_match(result_2_2), CurrentAt.to_metta_usage(character.key, "beach"))
        self.assertEqual(count_atoms(result_2_2), 1)


if __name__ == "__main__":
    unittest.main()
