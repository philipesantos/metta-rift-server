import unittest

from core.patterns.facts.route_block_fact_pattern import RouteBlockFactPattern
from utils.type import Type


class TestRouteBlockFactPattern(unittest.TestCase):
    def test_to_metta(self):
        location_from = "glade"
        location_to = "cave"
        reason = "The cave door is closed."
        route_block = RouteBlockFactPattern(location_from, location_to, reason)
        self.assertEqual(
            route_block.to_metta(),
            f'({Type.ROUTE_BLOCK.value} {location_from} {location_to} "{reason}")',
        )


if __name__ == "__main__":
    unittest.main()
