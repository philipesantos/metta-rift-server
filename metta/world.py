from metta.atoms.at import At
from metta.atoms.character import Character
from metta.atoms.current_at import CurrentAt
from metta.atoms.location import Location
from metta.atoms.route import Route
from metta.atoms.wrappers.state import State
from metta.atoms.tick import Tick
from metta.function import Function
from utils.direction import Direction


class World:
    def __init__(self, tick: Tick):
        self.functions: list[Function] = []
        self.characters: list[Character] = []
        self.locations: list[Location] = []
        self.routes: list[Route] = []
        self.ats: list[At] = []
        self.current_ats: dict[str, CurrentAt] = {}
        self.tick = tick


    def add_function(self, function: Function):
        self.functions.append(function)


    def add_character(self, character: Character):
        self.characters.append(character)


    def add_location(self, location: Location):
        self.locations.append(location)


    def add_route(self, location_from: Location, direction: Direction, locations_to: Location):
        self.routes.append(Route(location_from.key, direction.value, locations_to.key))
        self.routes.append(Route(locations_to.key, direction.opposite.value, location_from.key))


    def add_at(self, at: At, current: bool):
        self.ats.append(at)
        if current:
            self.current_ats[at.what] = CurrentAt(at.what, at.where)


    def to_metta_definition(self) -> str:
        line_break = "\n\n"
        functions_metta = line_break.join([function.to_metta_definition() for function in self.functions])
        characters_metta = line_break.join([character.to_metta_definition() for character in self.characters])
        locations_metta = line_break.join([location.to_metta_definition() for location in self.locations])
        routes_metta = line_break.join([route.to_metta_definition() for route in self.routes])
        ats_metta = line_break.join([at.to_metta_definition() for at in self.ats])
        current_ats_metta = line_break.join([current_at.to_metta_definition() for current_at in self.current_ats.values()])
        tick_state_metta = State(self.tick.to_metta_definition()).to_metta_definition()
        return (
            f"{functions_metta}{line_break}"
            f"{characters_metta}{line_break}"
            f"{locations_metta}{line_break}"
            f"{routes_metta}{line_break}"
            f"{ats_metta}{line_break}"
            f"{current_ats_metta}{line_break}"
            f"{tick_state_metta}{line_break}"
        )