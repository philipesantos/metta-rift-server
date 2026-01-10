from hyperon import MeTTa

from metta.definitions.facts.character_fact_definition import CharacterFactDefinition
from metta.definitions.facts.item_fact_definition import ItemFactDefinition
from metta.definitions.facts.location_fact_definition import LocationFactDefinition
from metta.definitions.facts.route_fact_definition import RouteFactDefinition
from metta.definitions.wrappers.log_wrapper_definition import LogWrapperDefinition
from metta.definitions.wrappers.state_wrapper_definition import StateWrapperDefinition
from metta.patterns.events.drop_event_pattern import DropEventPattern
from metta.patterns.events.pickup_event_pattern import PickUpEventPattern
from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.patterns.facts.tick_fact_pattern import TickFactPattern
from metta.patterns.functions.synchronize_tick_function_pattern import (
    SynchronizeTickFunctionPattern,
)
from metta.world import World
from metta.patterns.events.move_event_pattern import MoveEventPattern
from metta.definitions.functions.exists_function_definition import (
    ExistsFunctionDefinition,
)
from metta.definitions.functions.move_to_function_definition import (
    MoveToFunctionDefinition,
)
from metta.definitions.functions.move_towards_function_definition import (
    MoveTowardsFunctionDefinition,
)
from metta.definitions.functions.synchronize_tick_function_definition import (
    SynchronizeTickFunctionDefinition,
)
from metta.definitions.functions.trigger_function_definition import (
    TriggerFunctionDefinition,
)
from metta.definitions.side_effects.on_move_update_at import OnMoveUpdateAt
from metta.definitions.side_effects.on_move_update_tick import OnMoveUpdateTick
from utils.direction import Direction


def main():
    metta = MeTTa()
    metta_code = build_world().to_metta()

    print(metta_code)
    print(metta.run(metta_code))

    print("\n--- MeTTa Console ---")
    print("Type 'exit' to quit.")

    while True:
        user_query = input(">> ")

        if user_query.strip().lower() in ("exit", "quit"):
            break

        print(metta.run(user_query))
        print(metta.run(f"!{SynchronizeTickFunctionPattern().to_metta()}"))


def build_world():
    character_player = CharacterFactDefinition(key="player", name="John")

    location_glade = LocationFactDefinition(key="glade", desc="You are in the Glade.")
    location_cave = LocationFactDefinition(key="cave", desc="You are in the cave.")
    location_boat = LocationFactDefinition(key="boat", desc="You are in the boat.")
    location_plane = LocationFactDefinition(key="plane", desc="You are in the plane.")
    location_cabin = LocationFactDefinition(key="cabin", desc="You are in the cabin.")
    location_camping_site = LocationFactDefinition(
        key="camping_site", desc="You are in the camping site."
    )
    location_monolith = LocationFactDefinition(
        key="monolith", desc="You are in the monolith."
    )
    location_path_1 = LocationFactDefinition(
        key="path_1", desc="You are in the path 1."
    )
    location_path_2 = LocationFactDefinition(
        key="path_2", desc="You are in the path 2."
    )
    location_path_3 = LocationFactDefinition(
        key="path_3", desc="You are in the path 3."
    )
    location_path_4 = LocationFactDefinition(
        key="path_4", desc="You are in the path 4."
    )
    location_path_5 = LocationFactDefinition(
        key="path_5", desc="You are in the path 5."
    )
    location_path_6 = LocationFactDefinition(
        key="path_6", desc="You are in the path 6."
    )
    location_path_7 = LocationFactDefinition(
        key="path_7", desc="You are in the path 7."
    )
    location_path_8 = LocationFactDefinition(
        key="path_8", desc="You are in the path 8."
    )
    location_path_9 = LocationFactDefinition(
        key="path_9", desc="You are in the path 9."
    )

    world = World()

    world.add_definition(ExistsFunctionDefinition())
    world.add_definition(MoveToFunctionDefinition(character_player.to_pattern()))
    world.add_definition(MoveTowardsFunctionDefinition(character_player.to_pattern()))
    world.add_definition(SynchronizeTickFunctionDefinition())

    world.add_definition(
        TriggerFunctionDefinition(
            MoveEventPattern("$from", "$to"),
            [OnMoveUpdateAt(character_player.to_pattern()), OnMoveUpdateTick()],
        )
    )

    world.add_definition(character_player)

    world.add_definition(location_glade)
    world.add_definition(location_cave)
    world.add_definition(location_boat)
    world.add_definition(location_plane)
    world.add_definition(location_cabin)
    world.add_definition(location_camping_site)
    world.add_definition(location_monolith)
    world.add_definition(location_path_1)
    world.add_definition(location_path_2)
    world.add_definition(location_path_3)
    world.add_definition(location_path_4)
    world.add_definition(location_path_5)
    world.add_definition(location_path_6)
    world.add_definition(location_path_7)
    world.add_definition(location_path_8)
    world.add_definition(location_path_9)

    add_route(world, location_glade, Direction.SOUTH, location_path_1)
    add_route(world, location_path_1, Direction.WEST, location_path_2)
    add_route(world, location_path_2, Direction.SOUTH, location_cave)
    add_route(world, location_path_1, Direction.EAST, location_path_3)
    add_route(world, location_path_3, Direction.EAST, location_boat)
    add_route(world, location_glade, Direction.WEST, location_path_9)
    add_route(world, location_path_9, Direction.WEST, location_monolith)
    add_route(world, location_glade, Direction.NORTH, location_path_4)
    add_route(world, location_path_4, Direction.NORTH, location_path_5)
    add_route(world, location_path_5, Direction.EAST, location_path_6)
    add_route(world, location_path_6, Direction.EAST, location_plane)
    add_route(world, location_path_5, Direction.NORTH, location_path_7)
    add_route(world, location_path_7, Direction.WEST, location_path_8)
    add_route(world, location_path_8, Direction.WEST, location_cabin)
    add_route(world, location_path_7, Direction.NORTH, location_camping_site)

    world.add_definition(
        StateWrapperDefinition(AtFactPattern(character_player.key, location_glade.key))
    )

    world.add_definition(StateWrapperDefinition(TickFactPattern("1")))

    return world


def add_route(
    world: World,
    location_from: LocationFactDefinition,
    direction: Direction,
    locations_to: LocationFactDefinition,
):
    world.add_definition(
        RouteFactDefinition(location_from.key, direction.value, locations_to.key)
    )
    world.add_definition(
        RouteFactDefinition(
            locations_to.key, direction.opposite.value, location_from.key
        )
    )


if __name__ == "__main__":
    main()
