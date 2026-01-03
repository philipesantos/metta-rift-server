import unittest

from metta.atoms.at import At
from metta.atoms.wrappers.log import Log
from tests.utils.metta import get_test_metta

from tests.utils.utils import unwrap_first_match


class TestMettaAtomWrapperState(unittest.TestCase):
    def test_to_metta_usage(self):
        tick = "0"
        atom = At.to_metta_usage("0", "player", "glade")
        log_metta_usage = Log.to_metta_usage(tick, atom)
        self.assertEqual(log_metta_usage, f"(Log {tick} {atom})")

    def test_to_metta_definition(self):
        metta = get_test_metta()

        tick = 0
        atom = At.to_metta_usage("0", "player", "glade")

        metta.run(Log(str(tick), atom).to_metta_definition())

        log_metta_usage_tick = Log.to_metta_usage("$tick", "$atom")
        result_tick = metta.run(f"!(match &self {log_metta_usage_tick} $tick)")
        self.assertEqual(unwrap_first_match(result_tick), tick)

        log_metta_usage_atom = Log.to_metta_usage("$tick", "$atom")
        result_atom = metta.run(f"!(match &self {log_metta_usage_atom} $atom)")
        self.assertEqual(unwrap_first_match(result_atom), atom)

        log_metta_usage_no_match = Log.to_metta_usage(
            "1", At.to_metta_usage("1", "player", "cave")
        )
        result_no_match = metta.run(f"!(match &self {log_metta_usage_no_match} True)")
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
