import unittest

from metta.patterns.facts.tick_fact_pattern import TickFactPattern
from tests.utils.metta import get_test_metta

from tests.utils.utils import unwrap_first_match


class TestTickFactDefinition(unittest.TestCase):
    def test_to_metta(self):
        metta = get_test_metta()

        tick = 0

        metta.run(TickFactPattern(str(tick)).to_metta())

        result_tick = metta.run(
            f"!(match &self {TickFactPattern('$tick').to_metta()} $tick)"
        )
        self.assertEqual(unwrap_first_match(result_tick), tick)

        result_no_match = metta.run(
            f"!(match &self {TickFactPattern('1').to_metta()} True)"
        )
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
