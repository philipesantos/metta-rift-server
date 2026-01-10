from metta.definitions.function_definition import FunctionDefinition
from metta.patterns.facts.character_fact_pattern import CharacterFactPattern


class InventoryFunctionPattern(FunctionDefinition):
    def __init__(self, character: CharacterFactPattern):
        self.character = character

    def to_metta(self) -> str:
        return (
            f"(= (inventory)\n"
            f"    (match &self (State (At $what {self.character.key}))\n"
            f"        $what\n"
            f"    )\n"
            f")\n"
        )
