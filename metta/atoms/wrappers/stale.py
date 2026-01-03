class Stale:
    def __init__(self, what: str):
        self.what = what

    @staticmethod
    def to_metta_usage(what: str):
        return f"(Stale {what})"

    def to_metta_definition(self) -> str:
        return f"{self.to_metta_usage(self.what)}"
