import unittest

from metta.definitions.facts.current_at_fact_definition import CurrentAtFactDefinition
from tests.utils.metta import get_test_metta

from metta.patterns.facts.current_at_fact_pattern import CurrentAtFactPattern
from tests.utils.utils import unwrap_first_match


class TestCurrentAtFactDefinition(unittest.TestCase):

    def test_to_metta(self):
        metta = get_test_metta()

        what = "player"
        where = "glade"

        metta.run(CurrentAtFactDefinition(what, where).to_metta())

        current_at_what = CurrentAtFactPattern("$what", where)
        result_what = metta.run(f"!(match &self {current_at_what.to_metta()} $what)")
        self.assertEqual(unwrap_first_match(result_what), what)

        current_at_where = CurrentAtFactPattern(what, "$where")
        result_where = metta.run(
            f"!(match &self {current_at_where.to_metta()} $where)"
        )
        self.assertEqual(unwrap_first_match(result_where), where)

        current_at_no_match = CurrentAtFactPattern(what, "cave")
        result_no_match = metta.run(
            f"!(match &self {current_at_no_match.to_metta()} True)"
        )
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
