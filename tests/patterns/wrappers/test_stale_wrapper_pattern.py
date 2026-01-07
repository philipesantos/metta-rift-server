import unittest

from metta.patterns.facts.tick_fact_pattern import TickFactPattern
from metta.patterns.wrappers.stale_wrapper_pattern import StaleWrapperPattern
from tests.utils.metta import get_test_metta

from tests.utils.utils import unwrap_first_match


class TestStaleWrapperPattern(unittest.TestCase):
    def test_to_metta_usage(self):
        what = "Tick"
        stale = StaleWrapperPattern(what)
        self.assertEqual(stale.to_metta(), f"(Stale {what})")


if __name__ == "__main__":
    unittest.main()
