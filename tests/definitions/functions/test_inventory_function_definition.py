import unittest

from metta.definitions.functions.inventory_function_definition import (
    InventoryFunctionPattern as InventoryFunctionDefinition,
)
from metta.definitions.wrappers.state_wrapper_definition import StateWrapperDefinition
from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.patterns.facts.character_fact_pattern import CharacterFactPattern
from metta.patterns.functions.inventory_function_pattern import (
    InventoryFunctionPattern,
)
from tests.utils.metta import get_test_metta

from tests.utils.utils import unwrap_atom


class TestInventoryFunctionDefinition(unittest.TestCase):
    def test_to_metta(self):
        metta = get_test_metta()

        character = CharacterFactPattern("player", "John")

        metta.run(InventoryFunctionDefinition(character).to_metta())

        inventory = InventoryFunctionPattern()
        result_empty = metta.run(f"!{inventory.to_metta()}")
        self.assertEqual(result_empty, [[]])

        metta.run(
            StateWrapperDefinition(AtFactPattern("sword", character.key)).to_metta()
        )
        metta.run(
            StateWrapperDefinition(AtFactPattern("apple", character.key)).to_metta()
        )
        metta.run(
            StateWrapperDefinition(AtFactPattern("coin", "cave")).to_metta()
        )

        result_inventory = metta.run(f"!{inventory.to_metta()}")
        items = {unwrap_atom(atom) for atom in result_inventory[0]}
        self.assertEqual(items, {"sword", "apple"})


if __name__ == "__main__":
    unittest.main()
