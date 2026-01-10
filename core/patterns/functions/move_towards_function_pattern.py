from core.patterns.function_pattern import FunctionPattern
from utils.direction import Direction


class MoveTowardsFunctionPattern(FunctionPattern):
    def __init__(self, direction: Direction):
        self.direction = direction

    def to_metta(self) -> str:
        # fmt: off
        return f"(move-towards ({self.direction.value}))"
        # fmt: on
