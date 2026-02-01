from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class SlotSpec:
    slot_type: str


@dataclass(frozen=True)
class NLSpec:
    intent: str
    templates: tuple[str, ...]
    metta: str
    slots: Mapping[str, SlotSpec]
