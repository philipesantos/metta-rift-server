from core.definitions.function_definition import FunctionDefinition
from core.nlp.nl_spec import NLSpec
from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.patterns.facts.character_fact_pattern import CharacterFactPattern
from core.patterns.functions.trigger_function_pattern import TriggerFunctionPattern
from core.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern
from modules.cave.patterns.stay_still_event_pattern import StayStillEventPattern


class StayStillFunctionDefinition(FunctionDefinition):
    def __init__(self, character: CharacterFactPattern):
        self.character = character

    def to_metta(self) -> str:
        state_at_player = StateWrapperPattern(
            AtFactPattern(self.character.key, "$where")
        )
        stay_still_event = StayStillEventPattern("$where")
        stay_still_trigger = TriggerFunctionPattern(stay_still_event)
        # fmt: off
        return (
            f"(= (stay-still)\n"
            f"    (let $where (match &self {state_at_player.to_metta()} $where)\n"
            f"        {stay_still_trigger.to_metta()}\n"
            f"    )\n"
            f")"
        )
        # fmt: on

    def nl_spec(self):
        return NLSpec(
            intent="stay_still",
            templates=("stay still", "wait"),
            metta="(stay-still)",
            slots={},
        )

    def doc_tooltip(self, signature: str) -> str | None:
        return "Triggers wait or stay-still effects for the player's current location."
