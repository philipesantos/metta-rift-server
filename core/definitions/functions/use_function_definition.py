from core.definitions.function_definition import FunctionDefinition
from core.patterns.events.use_event_pattern import UseEventPattern
from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.patterns.facts.character_fact_pattern import CharacterFactPattern
from core.patterns.functions.exists_function_pattern import ExistsFunctionPattern
from core.patterns.functions.trigger_function_pattern import TriggerFunctionPattern
from core.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern


class UseFunctionDefinition(FunctionDefinition):
    def __init__(self, character: CharacterFactPattern):
        self.character = character

    def to_metta(self) -> str:
        state_at_player = StateWrapperPattern(
            AtFactPattern(self.character.key, "$where")
        )
        state_at_item = StateWrapperPattern(AtFactPattern("$what", self.character.key))
        state_at_target = StateWrapperPattern(AtFactPattern("$with_what", "$where"))
        use_event = UseEventPattern("$what", "$with_what")
        use_trigger = TriggerFunctionPattern(use_event)
        # fmt: off
        return (
            f"(= (use ($what $with_what))\n"
            f"    (let $where (match &self {state_at_player.to_metta()} $where)\n"
            f"        (if {ExistsFunctionPattern(state_at_item).to_metta()}\n"
            f"            (if {ExistsFunctionPattern(state_at_target).to_metta()}\n"
            f"                {use_trigger.to_metta()}\n"
            f'                "There is nothing to use that on"\n'
            f"            )\n"
            f'            "You do not have that"\n'
            f"        )\n"
            f"    )\n"
            f")"
        )
        # fmt: on
