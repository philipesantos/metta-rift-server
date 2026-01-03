import unittest

from tests.utils.metta import get_test_metta

from metta.atoms.at import At
from metta.atoms.current_tick import CurrentTick
from metta.atoms.out_of_date_tick import OutOfDateTick
from metta.functions.exists import Exists
from metta.functions.synchronize_tick import SynchronizeTick
from tests.utils.utils import unwrap_first_match


class TestMettaFunctionSynchronizeTick(unittest.TestCase):

    def test_to_metta_usage(self):
        synchronize_tick_metta_usage = SynchronizeTick.to_metta_usage()
        self.assertEqual(synchronize_tick_metta_usage, f"(synchronize-tick)")


    def test_to_metta_definition(self):
        metta = get_test_metta()

        metta.run(Exists().to_metta_definition())
        metta.run(SynchronizeTick().to_metta_definition())
        metta.run(CurrentTick("0").to_metta_definition())

        synchronize_tick_metta_usage = SynchronizeTick.to_metta_usage()
        current_tick_metta_match_tick = CurrentTick.to_metta_usage("$tick")

        result_synchronize_tick_1 = metta.run(f"!{synchronize_tick_metta_usage}")
        self.assertEqual(result_synchronize_tick_1, [[]])

        result_match_tick_1 = metta.run(f"!(match &self {current_tick_metta_match_tick} $tick)")
        self.assertEqual(unwrap_first_match(result_match_tick_1), 0)

        metta.run(OutOfDateTick().to_metta_definition())

        result_synchronize_tick_2 = metta.run(f"!{synchronize_tick_metta_usage}")
        self.assertEqual(result_synchronize_tick_2, [[]])

        result_match_tick_2 = metta.run(f"!(match &self {current_tick_metta_match_tick} $tick)")
        self.assertEqual(unwrap_first_match(result_match_tick_2), 1)

        result_synchronize_tick_3 = metta.run(f"!{synchronize_tick_metta_usage}")
        self.assertEqual(result_synchronize_tick_3, [[]])

        result_match_tick_3 = metta.run(f"!(match &self {current_tick_metta_match_tick} $tick)")
        self.assertEqual(unwrap_first_match(result_match_tick_3), 1)



if __name__ == "__main__":
    unittest.main()
