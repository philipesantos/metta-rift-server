import unittest

from hyperon import MeTTa

from metta.atoms.at import At
from metta.functions.exists import Exists
from metta.functions.trigger import Trigger
from tests.utils import some_event
from tests.utils.some_event import SomeEvent
from tests.utils.text_side_effect import TextSideEffect
from tests.utils.utils import unwrap_first_match


class TestMettaFunctionTrigger(unittest.TestCase):

    def test_to_metta_usage(self):
        event = SomeEvent("glade")
        trigger_metta_usage = Trigger.to_metta_usage(event)
        self.assertEqual(trigger_metta_usage, f"(trigger {event.to_metta()})")


    def test_to_metta_definition(self):
        metta = MeTTa()

        side_effect_text = "Trigger text"

        trigger = Trigger(SomeEvent("$value"), [TextSideEffect(side_effect_text)])
        metta.run(trigger.to_metta_definition())

        trigger_metta_usage = Trigger.to_metta_usage(SomeEvent("glade"))
        result = metta.run(f"!{trigger_metta_usage}")
        self.assertEqual(unwrap_first_match(result), side_effect_text)


if __name__ == "__main__":
    unittest.main()
