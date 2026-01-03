from hyperon import MeTTa


_SHARED_METTA = MeTTa()


def get_test_metta():
    """Return a shared MeTTa instance with an empty top-level space."""
    space = _SHARED_METTA.space()
    atoms = space.get_atoms() or []
    for atom in atoms:
        space.remove_atom(atom)
    return _SHARED_METTA
