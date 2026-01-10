import unittest

from tests.utils.metta import get_test_metta

from metta.patterns.facts.route_fact_pattern import RouteFactPattern
from tests.utils.utils import unwrap_first_match
from utils.direction import Direction
from utils.type import Type


class TestRouteFactPattern(unittest.TestCase):
    def test_to_metta(self):
        location_from = "glade"
        direction = Direction.SOUTH.value
        location_to = "cave"
        route = RouteFactPattern(location_from, direction, location_to)
        self.assertEqual(
            route.to_metta(),
            f"({Type.ROUTE.value} {location_from} {direction} {location_to})",
        )


if __name__ == "__main__":
    unittest.main()
