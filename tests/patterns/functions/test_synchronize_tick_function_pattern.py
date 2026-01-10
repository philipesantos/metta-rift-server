import unittest

from core.patterns.functions.synchronize_tick_function_pattern import (
    SynchronizeTickFunctionPattern,
)
from core.patterns.wrappers.stale_wrapper_pattern import StaleWrapperPattern
from core.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern
from core.patterns.facts.tick_fact_pattern import TickFactPattern
from tests.utils.metta import get_test_metta

from core.definitions.functions.exists_function_definition import (
    ExistsFunctionDefinition,
)
from core.definitions.functions.synchronize_tick_function_definition import (
    SynchronizeTickFunctionDefinition,
)
from tests.utils.utils import unwrap_first_match


class TestSynchronizeTickFunctionPattern(unittest.TestCase):
    def test_to_metta(self):
        synchronize_tick = SynchronizeTickFunctionPattern()
        self.assertEqual(synchronize_tick.to_metta(), f"(synchronize-tick)")


if __name__ == "__main__":
    unittest.main()
