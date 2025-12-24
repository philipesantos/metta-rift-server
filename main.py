from hyperon import MeTTa

from metta.atoms.character import Character
from metta.atoms.location import Location
from metta.atoms.route import Route
from metta.atoms.world import World
from metta.functions.compare_newer import CompareNewer
from metta.functions.current import Current
from metta.functions.current_tick import CurrentTick
from metta.functions.exists import Exists
from metta.functions.move_to import MoveTo
from metta.functions.move_towards import MoveTowards
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


def build_world():
    character_player = Character(
        key="player",
        name="John"
    )

    location_glade = Location(
        key="glade",
        desc="You are in the Glade. There are two pathways, one north, other south."
    )

    location_cave = Location(
        key="cave",
        desc="You are in the cave. There is a pathway east."
    )

    location_path_1 = Location(
        key="path_1",
        desc="Forked path, you can go east or west."
    )

    world = World()

    world.add_function(CompareNewer())
    world.add_function(Current())
    world.add_function(CurrentTick())
    world.add_function(Exists())
    world.add_function(MoveTo(character_player))
    world.add_function(MoveTowards(character_player))

    world.add_character(character_player)

    world.add_location(location_glade)
    world.add_location(location_cave)
    world.add_location(location_path_1)

    world.add_route(location_glade, Direction.SOUTH, location_path_1)
    world.add_route(location_path_1, Direction.SOUTH, location_cave)

    return world


if __name__ == "__main__":
    main()