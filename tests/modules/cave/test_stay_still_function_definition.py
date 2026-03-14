import unittest

from core.definitions.functions.trigger_function_definition import (
    TriggerFunctionDefinition,
)
from core.definitions.side_effects.on_event_print import OnEventPrint
from core.definitions.wrappers.state_wrapper_definition import StateWrapperDefinition
from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.patterns.facts.character_fact_pattern import CharacterFactPattern
from modules.cave.functions.stay_still_function_definition import (
    StayStillFunctionDefinition,
)
from modules.cave.patterns.stay_still_event_pattern import StayStillEventPattern
from modules.cave.patterns.stay_still_function_pattern import (
    StayStillFunctionPattern,
)
from tests.utils.metta import get_test_metta
from tests.utils.utils import unwrap_first_match


class TestStayStillFunctionDefinition(unittest.TestCase):
    def test_triggers_event_with_current_location(self):
        metta = get_test_metta()

        character = CharacterFactPattern("player", "John")

        metta.run(StayStillFunctionDefinition(character).to_metta())
        metta.run(
            TriggerFunctionDefinition(
                StayStillEventPattern("glade"),
                [OnEventPrint("Stayed still in the glade.")],
            ).to_metta()
        )
        metta.run(
            StateWrapperDefinition(AtFactPattern(character.key, "glade")).to_metta()
        )

        stay_still = StayStillFunctionPattern()
        result = metta.run(f"!{stay_still.to_metta()}")

        self.assertEqual(
            unwrap_first_match(result).text,
            "Stayed still in the glade.",
        )


if __name__ == "__main__":
    unittest.main()
