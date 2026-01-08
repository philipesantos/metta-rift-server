from metta.definitions.definition import Definition
from metta.patterns.pattern import Pattern


class World:
    def __init__(self):
        self.definitions: list[Definition] = []

    def add_definition(self, definition: Definition):
        self.definitions.append(definition)

    def to_metta(self) -> str:
        line_break = "\n\n"
        definitions_metta = line_break.join(
            [definition.to_metta() for definition in self.definitions]
        )
        return f"{definitions_metta}{line_break}"
