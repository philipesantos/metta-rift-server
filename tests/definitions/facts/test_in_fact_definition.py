import unittest

from metta.definitions.facts.at_fact_definition import AtFactDefinition
from metta.definitions.facts.in_fact_definition import InFactDefinition
from metta.patterns.facts.in_fact_pattern import InFactPattern
from tests.utils.metta import get_test_metta

from metta.patterns.facts.at_fact_pattern import AtFactPattern
from tests.utils.utils import unwrap_first_match


class TestInFactDefinition(unittest.TestCase):
    def test_to_metta(self):
        metta = get_test_metta()

        what = "compass"
        where = "player"

        metta.run(InFactDefinition(what, where).to_metta())

        in_what = InFactPattern("$what", where)
        result_what = metta.run(f"!(match &self {in_what.to_metta()} $what)")
        self.assertEqual(unwrap_first_match(result_what), what)

        in_where = InFactPattern(what, "$where")
        result_where = metta.run(f"!(match &self {in_where.to_metta()} $where)")
        self.assertEqual(unwrap_first_match(result_where), where)

        in_no_match = InFactPattern(what, "cave")
        result_no_match = metta.run(f"!(match &self {in_no_match.to_metta()} True)")
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
