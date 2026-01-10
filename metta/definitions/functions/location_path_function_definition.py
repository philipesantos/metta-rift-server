from metta.definitions.function_definition import FunctionDefinition
from metta.patterns.facts.at_fact_pattern import AtFactPattern
from metta.patterns.functions.location_path_function_pattern import (
    LocationPathFunctionPattern,
)
from metta.patterns.wrappers.state_wrapper_pattern import StateWrapperPattern
from utils.type import Type


class LocationPathFunctionDefinition(FunctionDefinition):
    def to_metta(self) -> str:
        state_at_match = StateWrapperPattern(AtFactPattern("$what", "$where"))
        # fmt: off
        return (
            f"(= (location-path ($what))\n"
            f"    (let $where (match &self {state_at_match.to_metta()} $where)\n"
            f"        (case (get-type $where) (\n"
            f"            ({Type.LOCATION.value} (Cons $where (Nil)))\n"
            f"            ($_ (Cons $where {LocationPathFunctionPattern('$where').to_metta()}))\n"
            f"        ))\n"
            f"    )\n"    
            f")"
        )
        # fmt: on
