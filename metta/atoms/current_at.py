class CurrentAt:
    def __init__(self, what: str, where: str):
        self.what = what
        self.where = where

    @staticmethod
    def to_metta_usage(what: str, where: str) -> str:
        return f"(Current At {what} {where})"

    def to_metta_definition(self) -> str:
        return f"{self.to_metta_usage(self.what, self.where)}"
