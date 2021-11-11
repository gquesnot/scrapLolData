from dataclasses import dataclass, field, asdict
from typing import Any, Union, List, Dict
from dacite import from_dict
import keyword

from my_dataclass.lolapi.matchtimeline.info import Info
from my_dataclass.lolapi.metadata import Metadata


@dataclass
class Matchtimeline:
    metadata: Metadata
    info: Info

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Matchtimeline":
        data = {k if k in keyword.kwlist else f"{k}_": v for k, v in data.items()}
        return from_dict(cls, data=data)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)