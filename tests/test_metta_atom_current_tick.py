import unittest

from hyperon import MeTTa

from metta.atoms.current_tick import CurrentTick
from tests.utils import unwrap_first_match


class TestMettaAtomCurrentTick(unittest.TestCase):

    def test_to_metta_usage(self):
        tick = 0
        current_tick_metta_usage = CurrentTick.to_metta_usage(tick)
        self.assertEqual(current_tick_metta_usage, f"(Current Tick {tick})")


    def test_to_metta_definition(self):
        metta = MeTTa()

        tick = 0

        current_tick_metta_definition = CurrentTick(str(tick)).to_metta_definition()
        metta.run(current_tick_metta_definition)

        current_tick_metta_usage_tick = CurrentTick.to_metta_usage("$tick")
        result_tick = metta.run(f"!(match &self {current_tick_metta_usage_tick} $tick)")
        self.assertEqual(unwrap_first_match(result_tick), tick)

        current_tick_metta_usage_no_match = CurrentTick.to_metta_usage("1")
        result_no_match = metta.run(f"!(match &self {current_tick_metta_usage_no_match} True)")
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
