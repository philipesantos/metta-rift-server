import unittest

from core.patterns.facts.item_fact_pattern import ItemFactPattern
from utils.type import Type
from tests.utils.metta import get_test_metta

from core.patterns.facts.location_fact_pattern import LocationFactPattern
from core.patterns.events.move_event_pattern import MoveEventPattern
from core.definitions.functions.trigger_function_definition import (
    TriggerFunctionDefinition,
)
from tests.utils.utils import unwrap_first_match


class TestItemFactPattern(unittest.TestCase):
    def test_to_metta(self):
        key = "compass"
        item = ItemFactPattern(key)
        self.assertEqual(item.to_metta(), f"({Type.ITEM.value} {key})")


if __name__ == "__main__":
    unittest.main()
