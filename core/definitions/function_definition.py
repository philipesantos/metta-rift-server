from abc import ABC

from core.definitions.definition import Definition


class FunctionDefinition(Definition, ABC):
    def doc_tooltip(self, signature: str) -> str | None:
        return None
