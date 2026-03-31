from core.definitions.function_definition import FunctionDefinition
from core.patterns.events.use_item_event_pattern import UseItemEventPattern
from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.patterns.facts.character_fact_pattern import CharacterFactPattern
from core.patterns.facts.response_fact_pattern import ResponseFactPattern
from core.patterns.functions.exists_function_pattern import ExistsFunctionPattern
from core.patterns.functions.trigger_function_pattern import TriggerFunctionPattern
from core.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern
from core.nlp.nl_spec import NLSpec, SlotSpec


class UseItemFunctionDefinition(FunctionDefinition):
    def __init__(self, character: CharacterFactPattern):
        self.character = character

    def to_metta(self) -> str:
        state_at_item = StateWrapperPattern(AtFactPattern("$what", self.character.key))
        use_event = UseItemEventPattern("$what")
        use_trigger = TriggerFunctionPattern(use_event)
        missing_item_response = ResponseFactPattern(
            100, '"You do not have that"'
        ).to_metta()
        # fmt: off
        return (
            f"(= (use ($what))\n"
            f"    (if {ExistsFunctionPattern(state_at_item).to_metta()}\n"
            f"        {use_trigger.to_metta()}\n"
            f"        {missing_item_response}\n"
            f"    )\n"
            f")"
        )
        # fmt: on

    def nl_spec(self):
        return NLSpec(
            intent="use",
            templates=(
                "use {item}",
                "activate {item}",
                "turn {item}",
                "turn on {item}",
            ),
            metta="(use ({item}))",
            slots={"item": SlotSpec("item")},
        )

    def doc_tooltip(self, signature: str) -> str | None:
        return "Uses a carried item by itself and triggers matching single-item effects."
