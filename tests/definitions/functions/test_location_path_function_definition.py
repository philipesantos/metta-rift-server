import unittest

from core.definitions.facts.location_fact_definition import LocationFactDefinition
from core.definitions.functions.location_path_function_definition import (
    LocationPathFunctionDefinition,
)
from core.definitions.wrappers.state_wrapper_definition import StateWrapperDefinition
from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.patterns.functions.location_path_function_pattern import (
    LocationPathFunctionPattern,
)
from tests.utils.metta import get_test_metta

from tests.utils.utils import unwrap_first_match


class TestLocationPathFunctionDefinition(unittest.TestCase):
    def test_location_path_direct_location(self):
        metta = get_test_metta()

        metta.run(LocationPathFunctionDefinition().to_metta())
        metta.run(LocationFactDefinition("glade", "A quiet glade.").to_metta())
        metta.run(StateWrapperDefinition(AtFactPattern("player", "glade")).to_metta())

        location_path = LocationPathFunctionPattern("player")
        result_path = metta.run(f"!{location_path.to_metta()}")
        self.assertEqual(unwrap_first_match(result_path), "(Cons glade (Nil))")

    def test_location_path_nested_location(self):
        metta = get_test_metta()

        metta.run(LocationPathFunctionDefinition().to_metta())
        metta.run(LocationFactDefinition("glade", "A quiet glade.").to_metta())
        metta.run(StateWrapperDefinition(AtFactPattern("coin", "chest")).to_metta())
        metta.run(StateWrapperDefinition(AtFactPattern("chest", "glade")).to_metta())

        location_path = LocationPathFunctionPattern("coin")
        result_path = metta.run(f"!{location_path.to_metta()}")
        self.assertEqual(
            unwrap_first_match(result_path), "(Cons chest (Cons glade (Nil)))"
        )


if __name__ == "__main__":
    unittest.main()
