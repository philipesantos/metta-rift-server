import unittest

from metta.patterns.events.move_event_pattern import MoveEventPattern
from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.patterns.wrappers.log_wrapper_pattern import LogWrapperPattern
from tests.utils.metta import get_test_metta

from tests.utils.utils import unwrap_first_match


class TestLogWrapperPattern(unittest.TestCase):
    def test_to_metta_usage(self):
        tick = "0"
        pattern = MoveEventPattern("glade", "cave")
        log = LogWrapperPattern(tick, pattern)
        self.assertEqual(log.to_metta(), f"(Log {tick} {pattern.to_metta()})")


if __name__ == "__main__":
    unittest.main()
