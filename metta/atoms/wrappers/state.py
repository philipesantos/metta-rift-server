class State:
    def __init__(self, atom: str):
        self.atom = atom

    @staticmethod
    def to_metta_usage(atom: str):
        return f"(State {atom})"

    def to_metta_definition(self) -> str:
        return f"{self.to_metta_usage(self.atom)}"
