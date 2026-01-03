class Log:
    def __init__(self, tick: str, atom: str):
        self.tick = tick
        self.atom = atom

    @staticmethod
    def to_metta_usage(tick: str, atom: str):
        return f"(Log {tick} {atom})"

    def to_metta_definition(self) -> str:
        return f"{self.to_metta_usage(self.tick, self.atom)}"
