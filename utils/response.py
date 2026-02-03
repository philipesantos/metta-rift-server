from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ResponseText:
    priority: int
    text: str
    raw: str


def parse_response_atom(atom_or_text: Any) -> ResponseText | None:
    if not isinstance(atom_or_text, str):
        return _parse_response_atom_obj(atom_or_text)
    return _parse_response_atom_text(atom_or_text)


def _parse_response_atom_obj(atom: Any) -> ResponseText | None:
    if not hasattr(atom, "get_children"):
        return None
    children = atom.get_children()
    if not children:
        return None
    if _atom_name(children[0]) != "Response":
        return None
    priority = _atom_to_int(children[1]) if len(children) > 1 else 0
    text_atom = children[2] if len(children) > 2 else None
    text = _render_text_atom(text_atom)
    raw = _atom_to_raw(text_atom)
    return ResponseText(priority=priority, text=text, raw=raw)


def _parse_response_atom_text(text: str) -> ResponseText | None:
    text = text.strip()
    if not text.startswith("(Response"):
        return None
    if not text.endswith(")"):
        return None
    body = text[1:-1].strip()
    if not body.startswith("Response"):
        return None
    rest = body[len("Response") :].strip()
    if not rest:
        return ResponseText(priority=0, text="", raw="")
    priority_token, text_expr = _split_first_token(rest)
    try:
        priority = int(priority_token)
    except ValueError:
        priority = 0
    text_expr = text_expr.strip()
    rendered = render_response_text(text_expr)
    return ResponseText(priority=priority, text=rendered, raw=text_expr)


def render_response_text(text_expr: str) -> str:
    if not text_expr:
        return ""
    if text_expr.startswith('"') and text_expr.endswith('"') and len(text_expr) >= 2:
        return text_expr[1:-1]
    return _format_text_atom(text_expr)


def _atom_name(atom: Any) -> str | None:
    if hasattr(atom, "get_name"):
        return atom.get_name()
    if hasattr(atom, "get_object"):
        obj = atom.get_object()
        if hasattr(obj, "value"):
            return str(obj.value)
        if hasattr(obj, "content"):
            return str(obj.content)
    return None


def _atom_to_int(atom: Any) -> int:
    if atom is None:
        return 0
    if hasattr(atom, "get_object"):
        obj = atom.get_object()
        if hasattr(obj, "value"):
            try:
                return int(obj.value)
            except (TypeError, ValueError):
                return 0
        if hasattr(obj, "content"):
            try:
                return int(obj.content)
            except (TypeError, ValueError):
                return 0
    if hasattr(atom, "get_name"):
        try:
            return int(atom.get_name())
        except (TypeError, ValueError):
            return 0
    try:
        return int(atom)
    except (TypeError, ValueError):
        return 0


def _atom_to_text(atom: Any) -> str:
    if atom is None:
        return ""
    if hasattr(atom, "get_object"):
        obj = atom.get_object()
        if hasattr(obj, "value"):
            return _format_text_atom(str(obj.value))
        if hasattr(obj, "content"):
            return _format_text_atom(str(obj.content))
    if hasattr(atom, "get_name"):
        return _format_text_atom(atom.get_name())
    if hasattr(atom, "get_children"):
        return _format_text_atom(str(atom))
    return _format_text_atom(str(atom))


def _render_text_atom(atom: Any) -> str:
    if atom is None:
        return ""
    if hasattr(atom, "get_children"):
        children = atom.get_children()
        if children:
            head = _atom_name(children[0])
            if head == "Text":
                parts = [_render_text_atom(child) for child in children[1:]]
                return "".join(part for part in parts if part)
            if head == "Cons":
                items = _collect_cons_list(atom)
                if items is not None:
                    return ", ".join(items)
    return _atom_to_text(atom)


def _collect_cons_list(atom: Any) -> list[str] | None:
    items: list[str] = []
    current = atom
    while True:
        if not hasattr(current, "get_children"):
            return None
        children = current.get_children()
        if not children:
            return None
        head = _atom_name(children[0])
        if head == "Nil":
            return items
        if head != "Cons" or len(children) < 3:
            return None
        items.append(_render_text_atom(children[1]))
        current = children[2]


def _atom_to_raw(atom: Any) -> str:
    if atom is None:
        return ""
    if hasattr(atom, "get_object"):
        obj = atom.get_object()
        if hasattr(obj, "value"):
            return str(obj.value)
        if hasattr(obj, "content"):
            return str(obj.content)
    if hasattr(atom, "get_name"):
        return atom.get_name()
    return str(atom)


def _strip_single_parens(text: str) -> str:
    if not text:
        return text
    trimmed = text.strip()
    if trimmed.startswith("(") and trimmed.endswith(")"):
        inner = trimmed[1:-1].strip()
        if inner and " " not in inner and "(" not in inner and ")" not in inner:
            return inner
    return text


def _format_text_atom(text: str) -> str:
    stripped = _strip_single_parens(text)
    if stripped is not text:
        return stripped
    trimmed = text.strip()
    if trimmed.startswith("(") and trimmed.endswith(")"):
        inner = trimmed[1:-1].strip()
        if inner and " " in inner and "(" not in inner and ")" not in inner:
            return ", ".join(inner.split())
    return text


def _split_first_token(text: str) -> tuple[str, str]:
    index = 0
    length = len(text)
    while index < length and text[index].isspace():
        index += 1
    start = index
    while index < length and not text[index].isspace() and text[index] != ")":
        index += 1
    return text[start:index], text[index:].strip()
