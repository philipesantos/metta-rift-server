import unittest

from core.definitions.wrappers.stale_wrapper_definition import StaleWrapperDefinition
from core.patterns.facts.tick_fact_pattern import TickFactPattern
from core.patterns.wrappers.stale_wrapper_pattern import StaleWrapperPattern
from tests.utils.metta import get_test_metta

from tests.utils.utils import unwrap_first_match


class TestStaleWrapperDefinition(unittest.TestCase):
    def test_to_metta(self):
        metta = get_test_metta()

        what = "Tick"

        metta.run(StaleWrapperDefinition(what).to_metta())

        stale_what = StaleWrapperPattern("$what")
        result_atom = metta.run(f"!(match &self {stale_what.to_metta()} $what)")
        self.assertEqual(unwrap_first_match(result_atom), what)

        state_no_match = StaleWrapperPattern("Other")
        result_no_match = metta.run(f"!(match &self {state_no_match.to_metta()} True)")
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
