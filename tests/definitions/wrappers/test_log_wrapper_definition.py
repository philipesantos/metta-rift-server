import unittest

from metta.definitions.wrappers.log_wrapper_definition import LogWrapperDefinition
from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.patterns.wrappers.log_wrapper_pattern import LogWrapperPattern
from tests.utils.metta import get_test_metta

from tests.utils.utils import unwrap_first_match


class TestStateWrapperDefinition(unittest.TestCase):

    def test_to_metta(self):
        metta = get_test_metta()

        tick = 0
        at = AtFactPattern("0", "player", "glade")

        metta.run(LogWrapperDefinition(str(tick), at).to_metta())

        log_tick = LogWrapperPattern("$tick", at)
        result_tick = metta.run(f"!(match &self {log_tick.to_metta()} $tick)")
        self.assertEqual(unwrap_first_match(result_tick), tick)

        log_what = LogWrapperPattern(str(tick), AtFactPattern("0", "$what", "glade"))
        result_atom = metta.run(f"!(match &self {log_what.to_metta()} $what)")
        self.assertEqual(unwrap_first_match(result_atom), at.what)

        log_no_match = LogWrapperPattern(
            "1", AtFactPattern("1", "player", "cave")
        )
        result_no_match = metta.run(f"!(match &self {log_no_match.to_metta()} True)")
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
