import unittest

from hyperon import MeTTa

from metta.atoms.route import Route
from tests.utils.utils import unwrap_first_match
from utils.direction import Direction


class TestMettaAtomRoute(unittest.TestCase):

    def test_to_metta_usage(self):
        location_from = "glade"
        direction = Direction.SOUTH.value
        location_to = "cave"
        route_metta_usage = Route.to_metta_usage(location_from, direction, location_to)
        self.assertEqual(route_metta_usage, f"(Route {location_from} {direction} {location_to})")


    def test_to_metta_definition(self):
        metta = MeTTa()

        location_from = "glade"
        direction = Direction.SOUTH.value
        location_to = "cave"

        route_metta_definition = Route(location_from, direction, location_to).to_metta_definition()
        metta.run(route_metta_definition)

        route_metta_usage_from = Route.to_metta_usage("$from", direction, location_to)
        result_from = metta.run(f"!(match &self {route_metta_usage_from} $from)")
        self.assertEqual(unwrap_first_match(result_from), location_from)

        route_metta_usage_direction = Route.to_metta_usage(location_from, "$direction", location_to)
        result_direction = metta.run(f"!(match &self {route_metta_usage_direction} $direction)")
        self.assertEqual(unwrap_first_match(result_direction), direction)

        route_metta_usage_to = Route.to_metta_usage(location_from, direction, "$to")
        result_to = metta.run(f"!(match &self {route_metta_usage_to} $to)")
        self.assertEqual(unwrap_first_match(result_to), location_to)

        route_metta_usage_no_match = Route.to_metta_usage("beach", direction, location_to)
        result_no_match = metta.run(f"!(match &self {route_metta_usage_no_match} True)")
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
