from metta.atoms.character import Character
from metta.atoms.location import Location
from metta.atoms.route import Route
from metta.functions.function import Function
from utils.direction import Direction


class World:
    def __init__(self):
        self.functions: list[Function] = []
        self.characters: list[Character] = []
        self.locations: list[Location] = []
        self.routes: list[Route] = []

    def add_function(self, function: Function):
        self.functions.append(function)


    def add_character(self, character: Character):
        self.characters.append(character)


    def add_location(self, location: Location):
        self.locations.append(location)


    def add_route(self, location_from: Location, direction: Direction, locations_to: Location):
        self.routes.append(Route(location_from.key, direction.value, locations_to.key))
        self.routes.append(Route(locations_to.key, direction.opposite.value, location_from.key))


    def to_metta_definition(self) -> str:
        line_break = "\n\n"
        functions_metta = line_break.join([function.to_metta_definition() for function in self.functions])
        characters_metta = line_break.join([character.to_metta_definition() for character in self.characters])
        locations_metta = line_break.join([location.to_metta_definition() for location in self.locations])
        routes_metta = line_break.join([route.to_metta_definition() for route in self.routes])
        return (
            f"{functions_metta}{line_break}"
            f"{characters_metta}{line_break}"
            f"{locations_metta}{line_break}"
            f"{routes_metta}{line_break}"
        )