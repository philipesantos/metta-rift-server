class Location:
    def __init__(self, key: str, desc: str):
        self.key = f"lc_{key}"
        self.desc = desc


    @staticmethod
    def to_metta_usage(key: str) -> str:
        return f"(Location {key})"


    def to_metta_definition(self) -> str:
        return (
            f"(: {self.key} Location)\n"
            f"{self.to_metta_usage(self.key)}"
        )
