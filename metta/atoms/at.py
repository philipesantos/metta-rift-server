class At:
    def __init__(self, tick: str, what: str, where: str):
        self.tick = tick
        self.what = what
        self.where = where


    @staticmethod
    def to_metta_usage(tick: str, what: str, where: str) -> str:
        return f'(At {tick} {what} {where})'


    def to_metta_definition(self) -> str:
        return (
            f"{self.to_metta_usage(self.tick, self.what, self.where)}"
        )
