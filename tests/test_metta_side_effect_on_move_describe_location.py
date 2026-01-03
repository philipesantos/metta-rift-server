import unittest

from hyperon import MeTTa

from metta.atoms.at import At
from metta.events.move_event import MoveEvent
from metta.functions.exists import Exists
from metta.functions.trigger import Trigger
from metta.side_effects.on_move_describe_location import OnMoveDescribeLocation
from tests.utils import some_event
from tests.utils.some_event import SomeEvent
from tests.utils.text_side_effect import TextSideEffect
from tests.utils.utils import unwrap_first_match


class TestMettaSideEffectOnMoveDescribeLocation(unittest.TestCase):

    def test_to_metta_definition(self):
        metta = MeTTa()

        text = "Location description"
        side_effect = OnMoveDescribeLocation(text)

        trigger = Trigger(MoveEvent("$from", "glade"), [side_effect])
        metta.run(trigger.to_metta_definition())

        trigger_metta_usage = Trigger.to_metta_usage(MoveEvent("cave", "glade"))
        result = metta.run(f"!{trigger_metta_usage}")
        self.assertEqual(unwrap_first_match(result), text)


if __name__ == "__main__":
    unittest.main()
