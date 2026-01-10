import unittest

from core.definitions.wrappers.stale_wrapper_definition import StaleWrapperDefinition
from core.definitions.wrappers.state_wrapper_definition import StateWrapperDefinition
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


class TestSynchronizeTickFunctionDefinition(unittest.TestCase):
    def test_to_metta(self):
        metta = get_test_metta()

        metta.run(ExistsFunctionDefinition().to_metta())
        metta.run(SynchronizeTickFunctionDefinition().to_metta())
        metta.run(StateWrapperDefinition(TickFactPattern("0")).to_metta())

        synchronize_tick = SynchronizeTickFunctionPattern()
        tick_state_match_tick = StateWrapperPattern(TickFactPattern("$tick"))

        result_synchronize_tick_1 = metta.run(f"!{synchronize_tick.to_metta()}")
        self.assertEqual(result_synchronize_tick_1, [[]])

        result_match_tick_1 = metta.run(
            f"!(match &self {tick_state_match_tick.to_metta()} $tick)"
        )
        self.assertEqual(unwrap_first_match(result_match_tick_1), 0)

        metta.run(StaleWrapperDefinition("Tick").to_metta())

        result_synchronize_tick_2 = metta.run(f"!{synchronize_tick.to_metta()}")
        self.assertEqual(result_synchronize_tick_2, [[]])

        result_match_tick_2 = metta.run(
            f"!(match &self {tick_state_match_tick.to_metta()} $tick)"
        )
        self.assertEqual(unwrap_first_match(result_match_tick_2), 1)

        result_synchronize_tick_3 = metta.run(f"!{synchronize_tick.to_metta()}")
        self.assertEqual(result_synchronize_tick_3, [[]])

        result_match_tick_3 = metta.run(
            f"!(match &self {tick_state_match_tick.to_metta()} $tick)"
        )
        self.assertEqual(unwrap_first_match(result_match_tick_3), 1)


if __name__ == "__main__":
    unittest.main()
