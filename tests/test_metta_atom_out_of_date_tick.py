import unittest

from hyperon import MeTTa

from metta.atoms.current_tick import CurrentTick
from metta.atoms.out_of_date_tick import OutOfDateTick
from tests.utils import unwrap_first_match


class TestMettaAtomOutOfDateTick(unittest.TestCase):

    def test_to_metta_usage(self):
        out_of_date_tick_metta_usage = OutOfDateTick.to_metta_usage()
        self.assertEqual(out_of_date_tick_metta_usage, f"(OutOfDate Tick)")


    def test_to_metta_definition(self):
        metta = MeTTa()

        out_of_date_tick_metta_definition = OutOfDateTick().to_metta_definition()
        metta.run(out_of_date_tick_metta_definition)

        out_of_date_tick_metta_usage_tick = OutOfDateTick.to_metta_usage()
        result_match = metta.run(f"!(match &self {out_of_date_tick_metta_usage_tick} True)")
        self.assertEqual(unwrap_first_match(result_match), True)


if __name__ == "__main__":
    unittest.main()
