import unittest

from tests.utils.metta import get_test_metta

from metta.atoms.location import Location
from metta.events.move_event import MoveEvent
from metta.functions.trigger import Trigger
from tests.utils.utils import unwrap_first_match


class TestMettaAtomLocation(unittest.TestCase):

    def test_to_metta_usage(self):
        key = "glade"
        location_metta_usage = Location.to_metta_usage(key)
        self.assertEqual(location_metta_usage, f'(Location {key})')


    def test_to_metta_definition(self):
        metta = get_test_metta()

        key = "glade"
        description = "The glade description"

        location_metta_definition = Location(key, description).to_metta_definition()
        metta.run(location_metta_definition)

        result_type = metta.run(f"!(get-type {key})")
        self.assertEqual(unwrap_first_match(result_type), "Location")

        location_metta_usage_key = Location.to_metta_usage("$key")
        result_key = metta.run(f"!(match &self {location_metta_usage_key} $key)")
        self.assertEqual(unwrap_first_match(result_key), key)

        location_metta_usage_move_trigger = Trigger.to_metta_usage(MoveEvent("cave", key))
        result_move_trigger = metta.run(f"!{location_metta_usage_move_trigger}")
        self.assertEqual(unwrap_first_match(result_move_trigger), description)

        location_metta_usage_no_match = Location.to_metta_usage("cave")
        result_no_match = metta.run(f"!(match &self {location_metta_usage_no_match} True)")
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
