import unittest

from tests.utils.metta import get_test_metta

from metta.patterns.facts.at_fact_pattern import AtFactPattern
from tests.utils.utils import unwrap_first_match


class TestAtFactPattern(unittest.TestCase):
    def test_to_metta(self):
        tick = 0
        what = "player"
        where = "glade"
        at = AtFactPattern(str(tick), what, where)
        self.assertEqual(at.to_metta(), f"(At {str(tick)} {what} {where})")


if __name__ == "__main__":
    unittest.main()
