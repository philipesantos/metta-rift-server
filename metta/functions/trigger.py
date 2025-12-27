from metta.event import Event
from metta.function import Function


class Trigger(Function):
    def __init__(self, event: Event, metta_code: str):
        self.event = event
        self.metta_code = metta_code


    @staticmethod
    def to_metta_usage(event: Event) -> str:
        return (
            f"(trigger {event.to_metta()})"
        )


    def to_metta_definition(self) -> str:
        formatted_metta_code = "\n".join("   " + line if line else line for line in self.metta_code.splitlines())
        return (
            f"(= (trigger {self.event.to_metta()})\n"
            f"{formatted_metta_code}\n"
            f")"
        )
