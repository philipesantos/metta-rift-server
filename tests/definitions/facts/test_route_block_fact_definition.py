import unittest

from core.definitions.facts.route_block_fact_definition import RouteBlockFactDefinition
from core.patterns.facts.route_block_fact_pattern import RouteBlockFactPattern
from tests.utils.metta import get_test_metta
from tests.utils.utils import unwrap_first_match


class TestRouteBlockFactDefinition(unittest.TestCase):
    def test_to_metta(self):
        metta = get_test_metta()

        location_from = "glade"
        location_to = "cave"
        reason = "The cave door is closed."

        metta.run(RouteBlockFactDefinition(location_from, location_to, reason).to_metta())

        route_block_from = RouteBlockFactPattern("$from", location_to, reason)
        result_from = metta.run(f"!(match &self {route_block_from.to_metta()} $from)")
        self.assertEqual(unwrap_first_match(result_from), location_from)

        route_block_to = RouteBlockFactPattern(location_from, "$to", reason)
        result_to = metta.run(f"!(match &self {route_block_to.to_metta()} $to)")
        self.assertEqual(unwrap_first_match(result_to), location_to)

        route_block_reason = RouteBlockFactPattern(location_from, location_to, "$reason")
        result_reason = metta.run(
            f"!(match &self {route_block_reason.to_metta()} $reason)"
        )
        self.assertEqual(unwrap_first_match(result_reason), "The cave door is closed.")

        route_block_no_match = RouteBlockFactPattern("beach", location_to, reason)
        result_no_match = metta.run(
            f"!(match &self {route_block_no_match.to_metta()} True)"
        )
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
