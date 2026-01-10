import unittest

from core.definitions.facts.at_fact_definition import AtFactDefinition
from tests.utils.metta import get_test_metta

from core.patterns.facts.at_fact_pattern import AtFactPattern
from tests.utils.utils import unwrap_first_match


class TestAtFactDefinition(unittest.TestCase):
    def test_to_metta(self):
        metta = get_test_metta()

        what = "player"
        where = "glade"

        metta.run(AtFactDefinition(what, where).to_metta())

        at_what = AtFactPattern("$what", where)
        result_what = metta.run(f"!(match &self {at_what.to_metta()} $what)")
        self.assertEqual(unwrap_first_match(result_what), what)

        at_where = AtFactPattern(what, "$where")
        result_where = metta.run(f"!(match &self {at_where.to_metta()} $where)")
        self.assertEqual(unwrap_first_match(result_where), where)

        at_no_match = AtFactPattern(what, "cave")
        result_no_match = metta.run(f"!(match &self {at_no_match.to_metta()} True)")
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
