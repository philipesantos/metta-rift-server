import unittest

from hyperon import MeTTa

from metta.atoms.current_at import CurrentAt
from tests.utils.utils import unwrap_first_match


class TestMettaAtomCurrentAt(unittest.TestCase):

    def test_to_metta_usage(self):
        what = "player"
        where = "glade"
        current_at_metta_usage = CurrentAt.to_metta_usage(what, where)
        self.assertEqual(current_at_metta_usage, f"(Current At {what} {where})")


    def test_to_metta_definition(self):
        metta = MeTTa()

        what = "player"
        where = "glade"

        current_at_metta_definition = CurrentAt(what, where).to_metta_definition()
        metta.run(current_at_metta_definition)

        current_at_metta_usage_what = CurrentAt.to_metta_usage("$what", where)
        result_what = metta.run(f"!(match &self {current_at_metta_usage_what} $what)")
        self.assertEqual(unwrap_first_match(result_what), what)

        current_at_metta_usage_where = CurrentAt.to_metta_usage(what, "$where")
        result_where = metta.run(f"!(match &self {current_at_metta_usage_where} $where)")
        self.assertEqual(unwrap_first_match(result_where), where)

        current_at_metta_usage_no_match = CurrentAt.to_metta_usage(what, "cave")
        result_no_match = metta.run(f"!(match &self {current_at_metta_usage_no_match} True)")
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
