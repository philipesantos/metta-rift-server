import unittest

from metta.atoms.tick import Tick
from metta.atoms.wrappers.state import State
from tests.utils.metta import get_test_metta

from tests.utils.utils import unwrap_first_match


class TestMettaAtomWrapperState(unittest.TestCase):
    def test_to_metta_usage(self):
        atom = Tick.to_metta_usage("0")
        state_metta_usage = State.to_metta_usage(atom)
        self.assertEqual(state_metta_usage, f"(State {atom})")

    def test_to_metta_definition(self):
        metta = get_test_metta()

        atom = Tick.to_metta_usage("0")

        metta.run(State(atom).to_metta_definition())

        state_metta_usage_atom = State.to_metta_usage("$atom")
        result_atom = metta.run(f"!(match &self {state_metta_usage_atom} $atom)")
        self.assertEqual(unwrap_first_match(result_atom), atom)

        state_metta_usage_no_match = State.to_metta_usage(Tick.to_metta_usage("1"))
        result_no_match = metta.run(f"!(match &self {state_metta_usage_no_match} True)")
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
