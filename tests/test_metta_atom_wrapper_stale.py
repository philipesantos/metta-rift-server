import unittest

from metta.atoms.tick import Tick
from metta.atoms.wrappers.stale import Stale
from tests.utils.metta import get_test_metta

from tests.utils.utils import unwrap_first_match


class TestMettaAtomWrapperStale(unittest.TestCase):

    def test_to_metta_usage(self):
        what = Tick.__name__
        stale_metta_usage = Stale.to_metta_usage(what)
        self.assertEqual(stale_metta_usage, f'(Stale {what})')


    def test_to_metta_definition(self):
        metta = get_test_metta()

        what = Tick.__name__

        metta.run(Stale(what).to_metta_definition())

        stale_metta_usage_atom = Stale.to_metta_usage("$what")
        result_atom = metta.run(f"!(match &self {stale_metta_usage_atom} $what)")
        self.assertEqual(unwrap_first_match(result_atom), what)

        state_metta_usage_no_match = Stale.to_metta_usage("Other")
        result_no_match = metta.run(f"!(match &self {state_metta_usage_no_match} True)")
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
