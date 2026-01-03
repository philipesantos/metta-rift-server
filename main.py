from hyperon import MeTTa

from metta.atoms.at import At
from metta.atoms.character import Character
from metta.atoms.location import Location
from metta.atoms.tick import Tick
from metta.world import World
from metta.events.move_event import MoveEvent
from metta.functions.exists import Exists
from metta.functions.move_to import MoveTo
from metta.functions.move_towards import MoveTowards
from metta.functions.synchronize_tick import SynchronizeTick
from metta.functions.trigger import Trigger
from metta.side_effects.on_move_update_at import OnMoveUpdateAt
from metta.side_effects.on_move_update_tick import OnMoveUpdateTick
from utils.direction import Direction


def main():
    metta = MeTTa()
    metta_code = build_world().to_metta_definition()

    print(metta_code)
    print(metta.run(metta_code))

    print("\n--- MeTTa Console ---")
    print("Type 'exit' to quit.")

    while True:
        user_query = input(">> ")

        if user_query.strip().lower() in ("exit", "quit"):
            break

        print(metta.run(user_query))
        print(metta.run(f"!{SynchronizeTick.to_metta_usage()}"))


def build_world():
    character_player = Character(
        key="player",
        name="John"
    )

    location_glade = Location(
        key="glade",
        desc="You are in the Glade."
    )

    location_cave = Location(
        key="cave",
        desc="You are in the cave."
    )

    location_boat = Location(
        key="boat",
        desc="You are in the boat."
    )

    location_plane = Location(
        key="plane",
        desc="You are in the plane."
    )

    location_cabin = Location(
        key="cabin",
        desc="You are in the cabin."
    )

    location_camping_site = Location(
        key="camping_site",
        desc="You are in the camping site."
    )

    location_monolith = Location(
        key="monolith",
        desc="You are in the monolith."
    )

    location_path_1 = Location(
        key="path_1",
        desc="You are in the path 1."
    )

    location_path_2 = Location(
        key="path_2",
        desc="You are in the path 2."
    )

    location_path_3 = Location(
        key="path_3",
        desc="You are in the path 3."
    )

    location_path_4 = Location(
        key="path_4",
        desc="You are in the path 4."
    )

    location_path_5 = Location(
        key="path_5",
        desc="You are in the path 5."
    )

    location_path_6 = Location(
        key="path_6",
        desc="You are in the path 6."
    )

    location_path_7 = Location(
        key="path_7",
        desc="You are in the path 7."
    )

    location_path_8 = Location(
        key="path_8",
        desc="You are in the path 8."
    )

    location_path_9 = Location(
        key="path_9",
        desc="You are in the path 9."
    )

    tick = Tick("1")

    world = World(tick)

    world.add_function(Exists())
    world.add_function(MoveTo(character_player))
    world.add_function(MoveTowards(character_player))
    world.add_function(SynchronizeTick())

    world.add_function(Trigger(
        MoveEvent("$from", "$to"),
        [
            OnMoveUpdateAt(character_player),
            OnMoveUpdateTick()
        ]
    ))

    world.add_character(character_player)

    world.add_location(location_glade)
    world.add_location(location_cave)
    world.add_location(location_boat)
    world.add_location(location_plane)
    world.add_location(location_cabin)
    world.add_location(location_camping_site)
    world.add_location(location_monolith)
    world.add_location(location_path_1)
    world.add_location(location_path_2)
    world.add_location(location_path_3)
    world.add_location(location_path_4)
    world.add_location(location_path_5)
    world.add_location(location_path_6)
    world.add_location(location_path_7)
    world.add_location(location_path_8)
    world.add_location(location_path_9)

    world.add_route(location_glade, Direction.SOUTH, location_path_1)
    world.add_route(location_path_1, Direction.WEST, location_path_2)
    world.add_route(location_path_2, Direction.SOUTH, location_cave)
    world.add_route(location_path_1, Direction.EAST, location_path_3)
    world.add_route(location_path_3, Direction.EAST, location_boat)
    world.add_route(location_glade, Direction.WEST, location_path_9)
    world.add_route(location_path_9, Direction.WEST, location_monolith)
    world.add_route(location_glade, Direction.NORTH, location_path_4)
    world.add_route(location_path_4, Direction.NORTH, location_path_5)
    world.add_route(location_path_5, Direction.EAST, location_path_6)
    world.add_route(location_path_6, Direction.EAST, location_plane)
    world.add_route(location_path_5, Direction.NORTH, location_path_7)
    world.add_route(location_path_7, Direction.WEST, location_path_8)
    world.add_route(location_path_8, Direction.WEST, location_cabin)
    world.add_route(location_path_7, Direction.NORTH, location_camping_site)

    world.add_at(At("0", character_player.key, location_glade.key), True)

    return world


if __name__ == "__main__":
    main()