import unittest

from hyperon import MeTTa

from metta.atoms.at import At
from metta.atoms.character import Character
from metta.atoms.current_at import CurrentAt
from metta.atoms.current_tick import CurrentTick
from metta.atoms.out_of_date_tick import OutOfDateTick
from metta.events.move_event import MoveEvent
from metta.functions.exists import Exists
from metta.functions.trigger import Trigger
from metta.side_effects.on_move_describe_location import OnMoveDescribeLocation
from metta.side_effects.on_move_update_at import OnMoveUpdateAt
from metta.side_effects.on_move_update_tick import OnMoveUpdateTick
from tests.utils import some_event
from tests.utils.some_event import SomeEvent
from tests.utils.text_side_effect import TextSideEffect
from tests.utils.utils import unwrap_first_match, count_atoms, unwrap_match


class TestMettaSideEffectOnMoveUpdateAt(unittest.TestCase):

    def test_to_metta_definition(self):
        metta = MeTTa()

        character = Character("player", "John")
        current_tick = CurrentTick("0")

        metta.run(current_tick.to_metta_definition())
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

        metta.run(f"!(remove-atom &self {current_tick.to_metta_definition()})")
        metta.run(f"!(add-atom &self {CurrentTick("1").to_metta_definition()})")

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
