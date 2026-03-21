from core.definitions.side_effect_definition import SideEffectDefinition
from core.patterns.events.use_item_event_pattern import UseItemEventPattern
from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.patterns.facts.character_fact_pattern import CharacterFactPattern
from core.patterns.facts.response_fact_pattern import ResponseFactPattern
from core.patterns.functions.exists_function_pattern import ExistsFunctionPattern
from core.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern


class CaveModuleOnUseFunctioningLantern(SideEffectDefinition):
    def __init__(self, character: CharacterFactPattern, cave_location: str):
        self.character = character
        self.cave_location = cave_location

    def to_metta(self, event: UseItemEventPattern) -> str:
        player_in_cave = StateWrapperPattern(
            AtFactPattern(self.character.key, self.cave_location)
        )
        visible_message = ResponseFactPattern(
            120, '"You raise the lantern and the cave comes into view."'
        )
        no_use_message = ResponseFactPattern(
            100, '"The lantern has no use here."'
        )
        # fmt: off
        return (
            f"(if {ExistsFunctionPattern(player_in_cave).to_metta()}\n"
            f"    {visible_message.to_metta()}\n"
            f"    {no_use_message.to_metta()}\n"
            f")\n"
        )
        # fmt: on
