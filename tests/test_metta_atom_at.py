import unittest

from tests.utils.metta import get_test_metta

from metta.atoms.at import At
from tests.utils.utils import unwrap_first_match


class TestMettaAtomAt(unittest.TestCase):
    def test_to_metta_usage(self):
        tick = 0
        what = "player"
        where = "glade"
        at_metta_usage = At.to_metta_usage(str(tick), what, where)
        self.assertEqual(at_metta_usage, f"(At {str(tick)} {what} {where})")

    def test_to_metta_definition(self):
        metta = get_test_metta()

        tick = 0
        what = "player"
        where = "glade"

        at_metta_definition = At(str(tick), what, where).to_metta_definition()
        metta.run(at_metta_definition)

        at_metta_usage_tick = At.to_metta_usage("$tick", what, where)
        result_tick = metta.run(f"!(match &self {at_metta_usage_tick} $tick)")
        self.assertEqual(unwrap_first_match(result_tick), tick)

        at_metta_usage_what = At.to_metta_usage(str(tick), "$what", where)
        result_what = metta.run(f"!(match &self {at_metta_usage_what} $what)")
        self.assertEqual(unwrap_first_match(result_what), what)

        at_metta_usage_where = At.to_metta_usage(str(tick), what, "$where")
        result_where = metta.run(f"!(match &self {at_metta_usage_where} $where)")
        self.assertEqual(unwrap_first_match(result_where), where)

        at_metta_usage_no_match = At.to_metta_usage(str(tick), what, "cave")
        result_no_match = metta.run(f"!(match &self {at_metta_usage_no_match} True)")
        self.assertEqual(result_no_match, [[]])


if __name__ == "__main__":
    unittest.main()
