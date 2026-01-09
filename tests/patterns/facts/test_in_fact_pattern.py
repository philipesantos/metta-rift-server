import unittest

from metta.patterns.facts.in_fact_pattern import InFactPattern
from tests.utils.metta import get_test_metta

from metta.patterns.facts.at_fact_pattern import AtFactPattern
from tests.utils.utils import unwrap_first_match


class TestInFactPattern(unittest.TestCase):
    def test_to_metta(self):
        what = "compass"
        where = "glade"
        in_pattern = InFactPattern(what, where)
        self.assertEqual(in_pattern.to_metta(), f"(In {what} {where})")


if __name__ == "__main__":
    unittest.main()
