import unittest

from metta.definitions.facts.at_fact_definition import AtFactDefinition
from tests.utils.metta import get_test_metta

from metta.patterns.facts.at_fact_pattern import AtFactPattern
from tests.utils.utils import unwrap_first_match


class TestAtFactDefinition(unittest.TestCase):
    def test_to_metta(self):
        metta = get_test_metta()

        tick = 0
        what = "player"
        where = "glade"

        metta.run(AtFactDefinition(str(tick), what, where).to_metta())

        at_tick = AtFactPattern("$tick", what, where)
        result_tick = metta.run(f"!(match &self {at_tick.to_metta()} $tick)")
        self.assertEqual(unwrap_first_match(result_tick), tick)

        at_what = AtFactPattern(str(tick), "$what", where)
        result_what = metta.run(f"!(match &self {at_what.to_metta()} $what)")
        self.assertEqual(unwrap_first_match(result_what), what)

        at_where = AtFactPattern(str(tick), what, "$where")
        result_where = metta.run(f"!(match &self {at_where.to_metta()} $where)")
        self.assertEqual(unwrap_first_match(result_where), where)

        at_no_match = AtFactPattern(str(tick), what, "cave")
        result_no_match = metta.run(f"!(match &self {at_no_match.to_metta()} True)")
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
