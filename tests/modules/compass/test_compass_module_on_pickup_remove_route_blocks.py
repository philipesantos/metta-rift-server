import unittest

from core.definitions.facts.route_fact_definition import RouteFactDefinition
from core.patterns.events.pickup_event_pattern import PickUpEventPattern
from core.patterns.facts.character_fact_pattern import CharacterFactPattern
from core.patterns.facts.route_block_fact_pattern import RouteBlockFactPattern
from core.patterns.functions.trigger_function_pattern import TriggerFunctionPattern
from core.world import World
from modules.compass.compass_module import CompassModule
from tests.utils.metta import get_test_metta


class TestCompassModuleOnPickupRemoveRouteBlocks(unittest.TestCase):
    def test_pickup_compass_removes_all_route_blocks(self):
        metta = get_test_metta()

        world = World()
        world.add_definition(RouteFactDefinition("glade", "north", "cave"))
        world.add_definition(RouteFactDefinition("glade", "south", "beach"))
        world.add_definition(RouteFactDefinition("cave", "east", "plane"))
        CompassModule(CharacterFactPattern("player", "John"), "glade").apply(world)
        metta.run(world.to_metta())

        # Add an extra block not created by compass location logic to confirm global cleanup.
        metta.run('(RouteBlock cave plane "Temporary blockade.")')

        pickup_trigger = TriggerFunctionPattern(PickUpEventPattern("compass", "glade"))
        metta.run(f"!{pickup_trigger.to_metta()}")

        route_block = RouteBlockFactPattern("$from", "$to", "$reason")
        result = metta.run(f"!(match &self {route_block.to_metta()} True)")
        self.assertEqual(result, [[]])


if __name__ == "__main__":
    unittest.main()
