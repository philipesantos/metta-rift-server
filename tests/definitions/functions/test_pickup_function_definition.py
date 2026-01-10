import unittest

from core.definitions.facts.location_fact_definition import LocationFactDefinition
from core.definitions.functions.first_function_definition import (
    FirstFunctionDefinition,
)
from core.definitions.functions.last_function_definition import (
    LastFunctionDefinition,
)
from core.definitions.functions.location_path_function_definition import (
    LocationPathFunctionDefinition,
)
from core.definitions.functions.pickup_function_definition import (
    PickUpFunctionDefinition,
)
from core.definitions.functions.trigger_function_definition import (
    TriggerFunctionDefinition,
)
from core.definitions.wrappers.state_wrapper_definition import StateWrapperDefinition
from core.patterns.events.pickup_event_pattern import PickUpEventPattern
from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.patterns.facts.character_fact_pattern import CharacterFactPattern
from core.patterns.functions.pickup_function_pattern import PickUpFunctionPattern
from tests.utils.metta import get_test_metta

from tests.utils.text_side_effect import TextSideEffectDefinition
from tests.utils.utils import unwrap_first_match


class TestPickUpFunctionDefinition(unittest.TestCase):
    def test_pickup(self):
        metta = get_test_metta()

        character = CharacterFactPattern("player", "John")

        metta.run(LocationPathFunctionDefinition().to_metta())
        metta.run(FirstFunctionDefinition().to_metta())
        metta.run(LastFunctionDefinition().to_metta())
        metta.run(
            TriggerFunctionDefinition(
                PickUpEventPattern("$what", "$where"),
                [TextSideEffectDefinition("Picked up")],
            ).to_metta()
        )
        metta.run(PickUpFunctionDefinition(character).to_metta())

        metta.run(LocationFactDefinition("glade", "A quiet glade.").to_metta())
        metta.run(
            StateWrapperDefinition(AtFactPattern(character.key, "glade")).to_metta()
        )
        metta.run(StateWrapperDefinition(AtFactPattern("coin", "chest")).to_metta())
        metta.run(StateWrapperDefinition(AtFactPattern("chest", "glade")).to_metta())

        pickup = PickUpFunctionPattern("coin")
        result_pickup = metta.run(f"!{pickup.to_metta()}")
        self.assertEqual(unwrap_first_match(result_pickup), "Picked up")


if __name__ == "__main__":
    unittest.main()
