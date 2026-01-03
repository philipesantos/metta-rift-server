import unittest

from tests.utils.metta import get_test_metta

from metta.atoms.at import At
from metta.atoms.out_of_date_tick import OutOfDateTick
from metta.events.move_event import MoveEvent
from metta.functions.exists import Exists
from metta.functions.trigger import Trigger
from metta.side_effects.on_move_describe_location import OnMoveDescribeLocation
from metta.side_effects.on_move_update_tick import OnMoveUpdateTick
from tests.utils import some_event
from tests.utils.some_event import SomeEvent
from tests.utils.text_side_effect import TextSideEffect
from tests.utils.utils import unwrap_first_match, count_atoms


class TestMettaSideEffectOnMoveUpdateTick(unittest.TestCase):

    def test_to_metta_definition(self):
        metta = get_test_metta()

        metta.run(Exists().to_metta_definition())

        trigger = Trigger(MoveEvent("$from", "$to"), [OnMoveUpdateTick()])
        metta.run(trigger.to_metta_definition())

        trigger_metta_usage_1 = Trigger.to_metta_usage(MoveEvent("cave", "glade"))
        metta.run(f"!{trigger_metta_usage_1}")

        result_1 = metta.run(f"!(match &self {OutOfDateTick.to_metta_usage()} True)")
        self.assertEqual(unwrap_first_match(result_1), True)
        self.assertEqual(count_atoms(result_1), 1)

        trigger_metta_usage_2 = Trigger.to_metta_usage(MoveEvent("glade", "beach"))
        metta.run(f"!{trigger_metta_usage_2}")

        result_2 = metta.run(f"!(match &self {OutOfDateTick.to_metta_usage()} True)")
        self.assertEqual(unwrap_first_match(result_2), True)
        self.assertEqual(count_atoms(result_2), 1)


if __name__ == "__main__":
    unittest.main()
