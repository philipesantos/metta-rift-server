class Character:
    def __init__(self, key: str, name: str):
        self.key = f"{key}"
        self.name = name

    @staticmethod
    def to_metta_usage(key: str, name: str) -> str:
        if " " in name:
            name = f'"{name}"'
        return f"(Character {key} {name})"

    def to_metta_definition(self) -> str:
        return f"(: {self.key} Character)\n{self.to_metta_usage(self.key, self.name)}"
