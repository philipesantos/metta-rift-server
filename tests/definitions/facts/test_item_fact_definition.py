import unittest

from metta.definitions.facts.item_fact_definition import ItemFactDefinition
from metta.definitions.facts.location_fact_definition import LocationFactDefinition
from metta.patterns.facts.item_fact_pattern import ItemFactPattern
from metta.patterns.functions.trigger_function_pattern import TriggerFunctionPattern
from tests.utils.metta import get_test_metta

from metta.patterns.facts.location_fact_pattern import LocationFactPattern
from metta.patterns.events.move_event_pattern import MoveEventPattern
from metta.definitions.functions.trigger_function_definition import (
    TriggerFunctionDefinition,
)
from tests.utils.utils import unwrap_first_match
from utils.type import Type


class TestItemFactDefinition(unittest.TestCase):
    def test_to_metta(self):
        metta = get_test_metta()

        key = "compass"

        metta.run(ItemFactDefinition(key).to_metta())

        result_type = metta.run(f"!(get-type {key})")
        self.assertEqual(unwrap_first_match(result_type), Type.ITEM.value)

        item_key = ItemFactPattern("$key")
        result_key = metta.run(f"!(match &self {item_key.to_metta()} $key)")
        self.assertEqual(unwrap_first_match(result_key), key)

        item_no_match = LocationFactPattern("bottle")
        result_no_match = metta.run(f"!(match &self {item_no_match.to_metta()} True)")
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
