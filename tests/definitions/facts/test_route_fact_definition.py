import unittest

from tests.utils.metta import get_test_metta

from metta.patterns.facts.route_fact_pattern import RouteFactPattern
from tests.utils.utils import unwrap_first_match
from utils.direction import Direction


class TestRouteFactDefinition(unittest.TestCase):
    def test_to_metta(self):
        metta = get_test_metta()

        location_from = "glade"
        direction = Direction.SOUTH.value
        location_to = "cave"

        metta.run(RouteFactPattern(location_from, direction, location_to).to_metta())

        route_from = RouteFactPattern("$from", direction, location_to)
        result_from = metta.run(f"!(match &self {route_from.to_metta()} $from)")
        self.assertEqual(unwrap_first_match(result_from), location_from)

        route_direction = RouteFactPattern(location_from, "$direction", location_to)
        result_direction = metta.run(
            f"!(match &self {route_direction.to_metta()} $direction)"
        )
        self.assertEqual(unwrap_first_match(result_direction), direction)

        route_to = RouteFactPattern(location_from, direction, "$to")
        result_to = metta.run(f"!(match &self {route_to.to_metta()} $to)")
        self.assertEqual(unwrap_first_match(result_to), location_to)

        route_no_match = RouteFactPattern("beach", direction, location_to)
        result_no_match = metta.run(f"!(match &self {route_no_match.to_metta()} True)")
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
