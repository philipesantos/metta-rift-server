import unittest

from metta.definitions.wrappers.state_wrapper_definition import StateWrapperDefinition
from metta.patterns.facts.tick_fact_pattern import TickFactPattern
from metta.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern
from tests.utils.metta import get_test_metta

from tests.utils.utils import unwrap_first_match


class TestStateWrapperDefinition(unittest.TestCase):

    def test_to_metta(self):
        metta = get_test_metta()

        tick = 0
        pattern = TickFactPattern(str(tick))

        metta.run(StateWrapperDefinition(pattern).to_metta())

        state_tick = StateWrapperPattern(TickFactPattern("$tick"))
        result_atom = metta.run(f"!(match &self {state_tick.to_metta()} $tick)")
        self.assertEqual(unwrap_first_match(result_atom), tick)

        state_no_match = StateWrapperPattern(TickFactPattern("1"))
        result_no_match = metta.run(f"!(match &self {state_no_match.to_metta()} True)")
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
