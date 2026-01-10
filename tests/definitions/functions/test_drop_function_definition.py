import unittest

from core.definitions.facts.location_fact_definition import LocationFactDefinition
from core.definitions.functions.drop_function_definition import (
    DropFunctionDefinition,
)
from core.definitions.functions.last_function_definition import (
    LastFunctionDefinition,
)
from core.definitions.functions.location_path_function_definition import (
    LocationPathFunctionDefinition,
)
from core.definitions.functions.trigger_function_definition import (
    TriggerFunctionDefinition,
)
from core.definitions.wrappers.state_wrapper_definition import StateWrapperDefinition
from core.patterns.events.drop_event_pattern import DropEventPattern
from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.patterns.facts.character_fact_pattern import CharacterFactPattern
from core.patterns.functions.drop_function_pattern import DropFunctionPattern
from tests.utils.metta import get_test_metta

from tests.utils.text_side_effect import TextSideEffectDefinition
from tests.utils.utils import unwrap_first_match


class TestDropFunctionDefinition(unittest.TestCase):
    def test_drop(self):
        metta = get_test_metta()

        character = CharacterFactPattern("player", "John")

        metta.run(LocationPathFunctionDefinition().to_metta())
        metta.run(LastFunctionDefinition().to_metta())
        metta.run(
            TriggerFunctionDefinition(
                DropEventPattern("$what", "$where"),
                [TextSideEffectDefinition("Dropped")],
            ).to_metta()
        )
        metta.run(DropFunctionDefinition(character).to_metta())

        metta.run(LocationFactDefinition("glade", "A quiet glade.").to_metta())
        metta.run(
            StateWrapperDefinition(AtFactPattern(character.key, "glade")).to_metta()
        )
        metta.run(
            StateWrapperDefinition(AtFactPattern("coin", character.key)).to_metta()
        )

        drop = DropFunctionPattern("coin")
        result_drop = metta.run(f"!{drop.to_metta()}")
        self.assertEqual(unwrap_first_match(result_drop), "Dropped")


if __name__ == "__main__":
    unittest.main()
