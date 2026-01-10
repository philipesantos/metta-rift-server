import unittest

from core.patterns.facts.tick_fact_pattern import TickFactPattern
from core.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern
from tests.utils.metta import get_test_metta

from tests.utils.utils import unwrap_first_match


class TestStateWrapperPattern(unittest.TestCase):
    def test_to_metta_usage(self):
        pattern = TickFactPattern("0")
        state = StateWrapperPattern(pattern)
        self.assertEqual(state.to_metta(), f"(State {pattern.to_metta()})")


if __name__ == "__main__":
    unittest.main()
