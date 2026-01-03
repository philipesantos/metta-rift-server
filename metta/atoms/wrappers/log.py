class Log:
    def __init__(self, atom: str):
        self.atom = atom

    @staticmethod
    def to_metta_usage(atom: str):
        return f"(Log {atom})"

    def to_metta_definition(self) -> str:
        return f"{self.to_metta_usage(self.atom)}"
