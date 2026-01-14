from core.definitions.facts.item_fact_definition import ItemFactDefinition
from core.definitions.wrappers.state_wrapper_definition import StateWrapperDefinition
from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.world import World
from modules.module import Module


class CaveEntranceModule(Module):
    def __init__(self, rock_location: str):
        self.rock_location = rock_location

    def apply(self, world: World) -> None:
        crescent_rock = ItemFactDefinition(
            key="crescent_rock",
            text_pickup="You pick up a crescent-moon rock.",
            text_drop="You drop the crescent-moon rock.",
        )
        world.add_definition(crescent_rock)
        world.add_definition(
            StateWrapperDefinition(AtFactPattern(crescent_rock.key, self.rock_location))
        )
