from core.definitions.facts.container_fact_definition import ContainerFactDefinition
from core.definitions.facts.item_fact_definition import ItemFactDefinition
from core.definitions.facts.location_fact_definition import LocationFactDefinition
from core.definitions.facts.route_block_fact_definition import RouteBlockFactDefinition
from core.definitions.functions.trigger_function_definition import TriggerFunctionDefinition
from core.definitions.side_effects.on_event_print import OnEventPrint
from core.definitions.wrappers.state_wrapper_definition import StateWrapperDefinition
from core.patterns.events.use_event_pattern import UseEventPattern
from core.patterns.facts.at_fact_pattern import AtFactPattern
from core.world import World
from modules.cabin.side_effects.cabin_module_on_use_unlock import (
    CabinModuleOnUseUnlock,
)
from modules.module import Module


class CabinModule(Module):
    def __init__(
        self,
        path_location: LocationFactDefinition,
        cabin_location: LocationFactDefinition,
        key_container: ContainerFactDefinition,
    ):
        self.path_location = path_location
        self.cabin_location = cabin_location
        self.key_container = key_container

    def apply(self, world: World) -> None:
        cabin_key = ItemFactDefinition(
            key="cabin_key",
            name="Cabin key",
            text_enter="You see a small metal key.",
            text_examine="A small iron key with the word 'Cabin' faintly etched into its surface.",
            text_look="Inside, a small metal key.",
            text_drop="You drop the cabin key.",
            text_pickup="You pick up the cabin key.",
        )
        world.add_definition(cabin_key)
        world.add_definition(
            StateWrapperDefinition(AtFactPattern(cabin_key.key, self.key_container.key))
        )

        world.add_definition(
            RouteBlockFactDefinition(
                self.path_location.key,
                self.cabin_location.key,
                "The cabin is locked. You need a key.",
            )
        )
        world.add_definition(
            StateWrapperDefinition(
                AtFactPattern(self.cabin_location.key, self.path_location.key)
            )
        )
        world.add_definition(
            TriggerFunctionDefinition(
                UseEventPattern("cabin_key", "cabin"),
                [
                    CabinModuleOnUseUnlock(self.path_location.key, self.cabin_location.key),
                    OnEventPrint("You unlock the cabin door."),
                ],
            )
        )
