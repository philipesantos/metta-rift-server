class CurrentTick:
    def __init__(self, tick: str):
        self.tick = tick


    @staticmethod
    def to_metta_usage(tick: str):
        return f'(Current Tick {tick})'


    def to_metta_definition(self) -> str:
        return (
            f'{self.to_metta_usage(self.tick)}'
        )
