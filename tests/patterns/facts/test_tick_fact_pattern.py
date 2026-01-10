import unittest

from core.patterns.facts.tick_fact_pattern import TickFactPattern
from tests.utils.metta import get_test_metta

from tests.utils.utils import unwrap_first_match


class TestTickFactPattern(unittest.TestCase):
    def test_to_metta(self):
        tick = TickFactPattern("0")
        self.assertEqual(tick.to_metta(), f"{tick.to_metta()}")


if __name__ == "__main__":
    unittest.main()
