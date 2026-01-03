import unittest

from tests.utils.metta import get_test_metta

from metta.atoms.at import At
from metta.functions.exists import Exists
from tests.utils.utils import unwrap_first_match


class TestMettaFunctionExists(unittest.TestCase):

    def test_to_metta_usage(self):
        atom = "(Test Atom)"
        exists_metta_usage = Exists.to_metta_usage(atom)
        self.assertEqual(exists_metta_usage, f"(exists (Test Atom))")


    def test_to_metta_definition(self):
        metta = get_test_metta()

        exists_metta_definition = Exists().to_metta_definition()
        metta.run(exists_metta_definition)

        at_1 = At("0", "player", "glade")
        metta.run(at_1.to_metta_definition())

        at_2 = At("1", "player", "cave")
        metta.run(at_2.to_metta_definition())

        exists_metta_usage_at_1 = Exists.to_metta_usage(At.to_metta_usage(at_1.tick, at_1.what, at_1.where))
        result_exists_at_1 = metta.run(f"!{exists_metta_usage_at_1}")
        self.assertEqual(unwrap_first_match(result_exists_at_1), True)

        exists_metta_usage_at_2 = Exists.to_metta_usage(At.to_metta_usage(at_2.tick, at_2.what, at_2.where))
        result_exists_at_2 = metta.run(f"!{exists_metta_usage_at_2}")
        self.assertEqual(unwrap_first_match(result_exists_at_2), True)

        exists_metta_usage_not_exists = Exists.to_metta_usage(At.to_metta_usage("1", "player", "beach"))
        result_not_exists = metta.run(f"!{exists_metta_usage_not_exists}")
        self.assertEqual(unwrap_first_match(result_not_exists), False)


if __name__ == "__main__":
    unittest.main()
