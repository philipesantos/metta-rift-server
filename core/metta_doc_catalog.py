from dataclasses import dataclass

from core.definitions.function_definition import FunctionDefinition

SExprNode = str | tuple["SExprNode", ...]


@dataclass(frozen=True)
class MettaDocEntry:
    id: str
    head: str
    signature: str
    source_metta: str
    kind: str


def build_metta_doc_catalog(world) -> list[MettaDocEntry]:
    definitions = getattr(world, "definitions", None)
    if definitions is None:
        return []

    entries: list[MettaDocEntry] = []
    for definition in definitions:
        if not isinstance(definition, FunctionDefinition):
            continue
        metta = definition.to_metta()
        for signature, source_metta in _extract_function_definitions(metta):
            head = _signature_head(signature)
            entry_id = f"doc:{len(entries) + 1}"
            entries.append(
                MettaDocEntry(
                    id=entry_id,
                    head=head,
                    signature=signature,
                    source_metta=source_metta,
                    kind="trigger" if head == "trigger" else "function",
                )
            )
    return entries


def resolve_metta_doc_ids(
    metta_query: str, metta_docs: list[MettaDocEntry]
) -> tuple[str, ...]:
    query = metta_query.strip()
    if query.startswith("!"):
        query = query[1:].strip()
    if not query:
        return ()

    try:
        query_node, end = _parse_expr(query, 0)
    except ValueError:
        return ()
    if _skip_whitespace(query, end) != len(query):
        return ()

    matched_ids = tuple(
        entry.id
        for entry in metta_docs
        if _pattern_matches(_parse_signature(entry.signature), query_node)
    )
    if matched_ids:
        return matched_ids

    head = _expr_head(query_node)
    if head is None:
        return ()
    return tuple(entry.id for entry in metta_docs if entry.head == head)


def _extract_function_definitions(metta: str) -> list[tuple[str, str]]:
    definitions: list[tuple[str, str]] = []
    for start, end in _top_level_expression_ranges(metta):
        expression = metta[start:end]
        if not expression.startswith("(="):
            continue
        index = _skip_whitespace(expression, 2)
        if index >= len(expression) or expression[index] != "(":
            continue
        signature, _ = _extract_balanced_expression(expression, index)
        definitions.append((signature, expression))
    return definitions


def _signature_head(signature: str) -> str:
    node = _parse_signature(signature)
    head = _expr_head(node)
    if head is None:
        raise ValueError(f"Invalid MeTTa signature: {signature}")
    return head


def _parse_signature(signature: str) -> SExprNode:
    node, end = _parse_expr(signature, 0)
    if _skip_whitespace(signature, end) != len(signature):
        raise ValueError(f"Invalid MeTTa signature: {signature}")
    return node


def _expr_head(node: SExprNode) -> str | None:
    if not isinstance(node, tuple) or not node:
        return None
    head = node[0]
    if isinstance(head, tuple):
        return None
    return head


def _pattern_matches(pattern: SExprNode, value: SExprNode) -> bool:
    if isinstance(pattern, str):
        if pattern.startswith("$"):
            return True
        return pattern == value
    if not isinstance(value, tuple) or len(pattern) != len(value):
        return False
    return all(_pattern_matches(left, right) for left, right in zip(pattern, value))


def _top_level_expression_ranges(metta: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    depth = 0
    start: int | None = None
    in_string = False
    escaping = False

    for index, char in enumerate(metta):
        if in_string:
            if escaping:
                escaping = False
            elif char == "\\":
                escaping = True
            elif char == '"':
                in_string = False
            continue

        if char == '"':
            in_string = True
            continue

        if char == "(":
            if depth == 0:
                start = index
            depth += 1
            continue

        if char != ")":
            continue

        if depth == 0:
            continue

        depth -= 1
        if depth == 0 and start is not None:
            ranges.append((start, index + 1))
            start = None

    return ranges


def _extract_balanced_expression(text: str, start: int) -> tuple[str, int]:
    if text[start] != "(":
        raise ValueError("Balanced expression must start with '('.")

    depth = 0
    in_string = False
    escaping = False

    for index in range(start, len(text)):
        char = text[index]
        if in_string:
            if escaping:
                escaping = False
            elif char == "\\":
                escaping = True
            elif char == '"':
                in_string = False
            continue

        if char == '"':
            in_string = True
            continue

        if char == "(":
            depth += 1
            continue

        if char != ")":
            continue

        depth -= 1
        if depth == 0:
            return text[start : index + 1], index + 1

    raise ValueError("Unbalanced MeTTa expression.")


def _parse_expr(text: str, index: int) -> tuple[SExprNode, int]:
    index = _skip_whitespace(text, index)
    if index >= len(text):
        raise ValueError("Unexpected end of MeTTa expression.")

    if text[index] == "(":
        return _parse_list(text, index)
    if text[index] == '"':
        return _parse_string(text, index)
    return _parse_atom(text, index)


def _parse_list(text: str, index: int) -> tuple[SExprNode, int]:
    items: list[SExprNode] = []
    index += 1
    while True:
        index = _skip_whitespace(text, index)
        if index >= len(text):
            raise ValueError("Unclosed MeTTa list.")
        if text[index] == ")":
            return tuple(items), index + 1
        item, index = _parse_expr(text, index)
        items.append(item)


def _parse_string(text: str, index: int) -> tuple[str, int]:
    start = index
    index += 1
    escaping = False
    while index < len(text):
        char = text[index]
        if escaping:
            escaping = False
        elif char == "\\":
            escaping = True
        elif char == '"':
            return text[start : index + 1], index + 1
        index += 1
    raise ValueError("Unclosed MeTTa string.")


def _parse_atom(text: str, index: int) -> tuple[str, int]:
    start = index
    while index < len(text) and text[index] not in {" ", "\n", "\t", "(", ")"}:
        index += 1
    return text[start:index], index


def _skip_whitespace(text: str, index: int) -> int:
    while index < len(text) and text[index].isspace():
        index += 1
    return index
