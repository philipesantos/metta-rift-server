def unwrap_atom(atom):
    if hasattr(atom, "get_object"):
        obj = atom.get_object()
        if hasattr(obj, "value"):
            return obj.value
        if hasattr(obj, "content"):
            return obj.content
        return obj
    if hasattr(atom, "get_name"):
        return atom.get_name()
    return atom


def unwrap_first_match(result):
    if not result:
        raise AssertionError("Expected match results, got empty list")
    if not result[0]:
        raise AssertionError("Expected first match to have bindings")
    return unwrap_atom(result[0][0])
