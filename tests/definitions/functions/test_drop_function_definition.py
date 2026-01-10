import unittest

from metta.definitions.facts.location_fact_definition import LocationFactDefinition
from metta.definitions.functions.drop_function_definition import (
    DropFunctionDefinition,
)
from metta.definitions.functions.last_function_definition import (
    LastFunctionDefinition,
)
from metta.definitions.functions.location_path_function_definition import (
    LocationPathFunctionDefinition,
)
from metta.definitions.functions.trigger_function_definition import (
    TriggerFunctionDefinition,
)
from metta.definitions.wrappers.state_wrapper_definition import StateWrapperDefinition
from metta.patterns.events.drop_event_pattern import DropEventPattern
from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.patterns.facts.character_fact_pattern import CharacterFactPattern
from metta.patterns.functions.drop_function_pattern import DropFunctionPattern
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
