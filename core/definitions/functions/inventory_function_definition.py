from core.definitions.function_definition import FunctionDefinition
from core.patterns.facts.character_fact_pattern import CharacterFactPattern
from core.nlp.nl_spec import NLSpec


class InventoryFunctionPattern(FunctionDefinition):
    def __init__(self, character: CharacterFactPattern):
        self.character = character

    def to_metta(self) -> str:
        # fmt: off
        return (
            f"(= (inventory)\n"
            f"    (match &self (State (At $what {self.character.key}))\n"
            f"        $what\n"
            f"    )\n"
            f")"
        )
        # fmt: on

    def nl_spec(self):
        return NLSpec(
            intent="inventory",
            templates=("inventory", "show inventory", "what do i have"),
            metta="(inventory)",
            slots={},
        )
