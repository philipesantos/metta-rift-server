import unittest

from core.definitions.functions.exists_function_definition import (
    ExistsFunctionDefinition,
)
from core.definitions.functions.trigger_function_definition import (
    TriggerFunctionDefinition,
)
from core.definitions.functions.use_item_function_definition import (
    UseItemFunctionDefinition,
)
from core.definitions.side_effects.on_event_print import OnEventPrint
from core.definitions.wrappers.state_wrapper_definition import StateWrapperDefinition
from core.patterns.events.use_item_event_pattern import UseItemEventPattern
from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.patterns.facts.character_fact_pattern import CharacterFactPattern
from core.patterns.functions.use_item_function_pattern import UseItemFunctionPattern
from tests.utils.metta import get_test_metta
from tests.utils.utils import unwrap_first_match


class TestUseItemFunctionDefinition(unittest.TestCase):
    def test_triggers_use_event_when_item_is_in_inventory(self):
        metta = get_test_metta()

        character = CharacterFactPattern("player", "John")

        metta.run(ExistsFunctionDefinition().to_metta())
        metta.run(UseItemFunctionDefinition(character).to_metta())
        metta.run(
            TriggerFunctionDefinition(
                UseItemEventPattern("$what"),
                [OnEventPrint("Used")],
            ).to_metta()
        )
        metta.run(
            StateWrapperDefinition(
                AtFactPattern("functioning_lantern", character.key)
            ).to_metta()
        )

        use_action = UseItemFunctionPattern("functioning_lantern")
        result = metta.run(f"!{use_action.to_metta()}")

        self.assertEqual(unwrap_first_match(result).text, "Used")

    def test_returns_message_when_item_missing(self):
        metta = get_test_metta()

        character = CharacterFactPattern("player", "John")

        metta.run(ExistsFunctionDefinition().to_metta())
        metta.run(UseItemFunctionDefinition(character).to_metta())

        use_action = UseItemFunctionPattern("functioning_lantern")
        result = metta.run(f"!{use_action.to_metta()}")

        self.assertEqual(unwrap_first_match(result).text, "You do not have that")


if __name__ == "__main__":
    unittest.main()
