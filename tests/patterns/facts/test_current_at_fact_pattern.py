import unittest

from tests.utils.metta import get_test_metta

from metta.patterns.facts.current_at_fact_pattern import CurrentAtFactPattern
from tests.utils.utils import unwrap_first_match


class TestCurrentAtFactPattern(unittest.TestCase):
    def test_to_metta(self):
        what = "player"
        where = "glade"
        current_at = CurrentAtFactPattern(what, where)
        self.assertEqual(current_at.to_metta(), f"(Current At {what} {where})")


if __name__ == "__main__":
    unittest.main()
