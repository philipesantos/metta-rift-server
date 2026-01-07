import unittest

from tests.utils.metta import get_test_metta

from metta.patterns.facts.location_fact_pattern import LocationFactPattern
from metta.patterns.events.move_event_pattern import MoveEventPattern
from metta.definitions.functions.trigger_function_definition import TriggerFunctionDefinition
from tests.utils.utils import unwrap_first_match


class TestLocationFactPattern(unittest.TestCase):
    def test_to_metta(self):
        key = "glade"
        location = LocationFactPattern(key)
        self.assertEqual(location.to_metta(), f"(Location {key})")


if __name__ == "__main__":
    unittest.main()
