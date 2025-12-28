class OutOfDateTick:
    @staticmethod
    def to_metta_usage() -> str:
        return f"(OutOfDate Tick)"


    def to_metta_definition(self) -> str:
        return (
            f"{self.to_metta_usage()}"
        )
