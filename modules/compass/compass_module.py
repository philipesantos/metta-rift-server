from core.definitions.facts.item_fact_definition import ItemFactDefinition
from core.definitions.wrappers.state_wrapper_definition import StateWrapperDefinition
from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.world import World
from modules.module import Module


class CompassModule(Module):
    def __init__(self, compass_where: str):
        self.compass_where: str = compass_where

    def apply(self, world: World) -> None:
        item_compass = ItemFactDefinition(
            "compass", "You got the compass", "You dropped the compass"
        )
        world.add_definition(item_compass)
        world.add_definition(
            StateWrapperDefinition(AtFactPattern(item_compass.key, self.compass_where))
        )
