import unittest

from core.definitions.facts.location_fact_definition import LocationFactDefinition
from core.definitions.functions.inventory_function_definition import (
    InventoryFunctionPattern,
)
from core.definitions.functions.trigger_function_definition import (
    TriggerFunctionDefinition,
)
from core.definitions.side_effects.on_event_print import OnEventPrint
from core.metta_doc_catalog import build_metta_doc_catalog, resolve_metta_doc_ids
from core.patterns.events.use_event_pattern import UseEventPattern
from core.patterns.facts.character_fact_pattern import CharacterFactPattern
from core.world import World
from modules.statues.functions.statues_helpers_function_definition import (
    StatuesHelpersFunctionDefinition,
)


class FakeWorldWithoutDefinitions:
    def to_metta(self) -> str:
        return "(= (look) Empty)\n\n"


class TestMettaDocCatalog(unittest.TestCase):
    def test_builds_docs_for_single_function_definition(self):
        world = World()
        world.add_definition(InventoryFunctionPattern(CharacterFactPattern("player", "John")))

        docs = build_metta_doc_catalog(world)

        self.assertEqual(len(docs), 1)
        self.assertEqual(docs[0].head, "inventory")
        self.assertEqual(docs[0].signature, "(inventory)")
        self.assertEqual(docs[0].kind, "function")
        self.assertEqual(
            docs[0].tooltip,
            "Lists the items and containers the player is currently carrying.",
        )
        self.assertIn("(= (inventory)\n", docs[0].source_metta)

    def test_builds_docs_for_multi_function_definition(self):
        world = World()
        world.add_definition(StatuesHelpersFunctionDefinition())

        docs = build_metta_doc_catalog(world)
        signatures = {doc.signature for doc in docs}

        self.assertEqual(len(docs), 4)
        self.assertIn("(statue-has-any-rune ($statue))", signatures)
        self.assertIn("(all-statues-filled)", signatures)
        self.assertIn("(statues-solved)", signatures)
        self.assertIn("(statue-filled-message ($statue $statue_name))", signatures)
        self.assertEqual(
            {
                doc.signature: doc.tooltip
                for doc in docs
            }["(all-statues-filled)"],
            "Returns True if every statue already holds a rune.",
        )

    def test_returns_empty_docs_when_world_has_no_definitions_attribute(self):
        self.assertEqual(build_metta_doc_catalog(FakeWorldWithoutDefinitions()), [])

    def test_excludes_function_like_code_emitted_by_non_function_definitions(self):
        world = World()
        world.add_definition(LocationFactDefinition("glade", "You are in the glade."))

        docs = build_metta_doc_catalog(world)

        self.assertEqual(docs, [])

    def test_resolves_generic_function_signature_against_specific_call(self):
        world = World()
        world.add_definition(InventoryFunctionPattern(CharacterFactPattern("player", "John")))

        docs = build_metta_doc_catalog(world)

        self.assertEqual(resolve_metta_doc_ids("!(inventory)", docs), ("doc:1",))

    def test_resolves_multiple_trigger_docs_for_same_specific_call(self):
        world = World()
        world.add_definition(
            TriggerFunctionDefinition(
                UseEventPattern("oil", "lantern"),
                [OnEventPrint("Ready.")],
            )
        )
        world.add_definition(
            TriggerFunctionDefinition(
                UseEventPattern("oil", "lantern"),
                [OnEventPrint("Already ready.")],
            )
        )

        docs = build_metta_doc_catalog(world)

        self.assertEqual(
            resolve_metta_doc_ids("!(trigger (Use oil lantern))", docs),
            ("doc:1", "doc:2"),
        )

    def test_startup_trigger_docs_only_include_explicit_trigger_definitions(self):
        from core.world_builder import build_world

        docs = build_metta_doc_catalog(build_world())
        startup_docs = [
            doc for doc in docs if doc.signature == "(trigger (Startup))"
        ]

        self.assertEqual(len(startup_docs), 2)

    def test_resolves_generic_trigger_signature_against_specific_query(self):
        world = World()
        world.add_definition(
            TriggerFunctionDefinition(
                UseEventPattern("$what", "$with_what"),
                [OnEventPrint("Fallback.")],
            )
        )

        docs = build_metta_doc_catalog(world)

        self.assertEqual(
            resolve_metta_doc_ids("!(trigger (Use oil lantern))", docs),
            ("doc:1",),
        )

    def test_returns_empty_doc_ids_for_malformed_query(self):
        world = World()
        world.add_definition(InventoryFunctionPattern(CharacterFactPattern("player", "John")))

        docs = build_metta_doc_catalog(world)

        self.assertEqual(resolve_metta_doc_ids("!(inventory", docs), ())


if __name__ == "__main__":
    unittest.main()
