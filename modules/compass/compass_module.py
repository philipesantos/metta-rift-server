from core.definitions.facts.item_fact_definition import ItemFactDefinition
from core.definitions.functions.trigger_function_definition import TriggerFunctionDefinition
from core.definitions.wrappers.state_wrapper_definition import StateWrapperDefinition
from core.patterns.events.pickup_event_pattern import PickUpEventPattern
from core.patterns.events.move_event_pattern import MoveEventPattern
from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.patterns.facts.character_fact_pattern import CharacterFactPattern
from core.world import World
from modules.compass.functions.compass_directions_function_definition import (
    CompassDirectionsFunctionDefinition,
)
from modules.compass.side_effects.compass_module_on_move_print_directions import CompassModuleOnMovePrintDirections
from modules.compass.side_effects.compass_module_on_pickup_print_directions import (
    CompassModuleOnPickupPrintDirections,
)
from modules.module import Module


class CompassModule(Module):
    def __init__(self, character: CharacterFactPattern, compass_where: str):
        self.character: CharacterFactPattern = character
        self.compass_where: str = compass_where

    def apply(self, world: World) -> None:
        item_compass = ItemFactDefinition(
            key="compass",
            text_pickup="You got the compass",
            text_drop="You dropped the compass"
        )
        world.add_definition(item_compass)
        world.add_definition(CompassDirectionsFunctionDefinition())
        world.add_definition(
            StateWrapperDefinition(AtFactPattern(item_compass.key, self.compass_where))
        )
        world.add_definition(
            TriggerFunctionDefinition(
                MoveEventPattern("$from", "$to"), [
                    CompassModuleOnMovePrintDirections(self.character)
                ]
            )
        )
        world.add_definition(
            TriggerFunctionDefinition(
                PickUpEventPattern(item_compass.key, "$where"), [
                    CompassModuleOnPickupPrintDirections(self.character)
                ]
            )
        )
