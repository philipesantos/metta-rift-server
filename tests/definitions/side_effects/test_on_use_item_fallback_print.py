import unittest

from core.definitions.functions.exists_function_definition import (
    ExistsFunctionDefinition,
)
from core.definitions.functions.trigger_function_definition import (
    TriggerFunctionDefinition,
)
from core.definitions.side_effects.on_event_print import OnEventPrint
from core.definitions.side_effects.on_use_item_fallback_print import (
    OnUseItemFallbackPrint,
)
from core.patterns.events.use_item_event_pattern import UseItemEventPattern
from core.patterns.functions.trigger_function_pattern import TriggerFunctionPattern
from tests.utils.metta import get_test_metta
from tests.utils.utils import unwrap_first_match


class TestOnUseItemFallbackPrint(unittest.TestCase):
    def test_prints_default_message_when_no_specific_rule_exists(self):
        metta = get_test_metta()

        metta.run(ExistsFunctionDefinition().to_metta())
        metta.run(
            TriggerFunctionDefinition(
                UseItemEventPattern("$what"),
                [OnUseItemFallbackPrint()],
            ).to_metta()
        )

        trigger_use = TriggerFunctionPattern(UseItemEventPattern("lantern"))
        result = metta.run(f"!{trigger_use.to_metta()}")

        self.assertEqual(
            unwrap_first_match(result).text, "That doesn't seem to do anything."
        )

    def test_skips_default_message_when_specific_rule_exists(self):
        metta = get_test_metta()

        metta.run(ExistsFunctionDefinition().to_metta())
        metta.run(
            TriggerFunctionDefinition(
                UseItemEventPattern("$what"),
                [OnUseItemFallbackPrint()],
            ).to_metta()
        )
        metta.run(
            TriggerFunctionDefinition(
                UseItemEventPattern("lantern"),
                [OnEventPrint("Specific")],
            ).to_metta()
        )

        trigger_use = TriggerFunctionPattern(UseItemEventPattern("lantern"))
        result = metta.run(f"!{trigger_use.to_metta()}")

        self.assertEqual(unwrap_first_match(result).text, "Specific")


if __name__ == "__main__":
    unittest.main()
