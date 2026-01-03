import unittest

from metta.atoms.tick import Tick
from tests.utils.metta import get_test_metta

from tests.utils.utils import unwrap_first_match


class TestMettaAtomTick(unittest.TestCase):
    def test_to_metta_usage(self):
        tick = 0
        tick_metta_usage = Tick.to_metta_usage(str(tick))
        self.assertEqual(tick_metta_usage, f"(Tick {tick})")

    def test_to_metta_definition(self):
        metta = get_test_metta()

        tick = 0

        tick_metta_definition = Tick(str(tick)).to_metta_definition()
        metta.run(tick_metta_definition)

        tick_metta_usage_tick = Tick.to_metta_usage("$tick")
        result_tick = metta.run(f"!(match &self {tick_metta_usage_tick} $tick)")
        self.assertEqual(unwrap_first_match(result_tick), tick)

        tick_metta_usage_no_match = Tick.to_metta_usage("1")
        result_no_match = metta.run(f"!(match &self {tick_metta_usage_no_match} True)")
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
