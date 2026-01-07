from metta.definitions.definition import Definition
from metta.patterns.pattern import Pattern


class World:
    def __init__(self):
        self.definitions: list[Definition] = []
        self.patterns: list[Pattern] = []

    def add_definition(self, definition: Definition):
        self.definitions.append(definition)

    def add_pattern(self, pattern: Pattern):
        self.patterns.append(pattern)

    def to_metta(self) -> str:
        line_break = "\n\n"
        definitions_metta = line_break.join(
            [definition.to_metta() for definition in self.definitions]
        )
        patterns_metta = line_break.join(
            [pattern.to_metta() for pattern in self.patterns]
        )
        return f"{definitions_metta}{line_break}{patterns_metta}{line_break}"
