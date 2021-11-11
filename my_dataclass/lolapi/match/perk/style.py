from dataclasses import dataclass, field, asdict
from typing import Any, List, Dict
from dacite import from_dict
import keyword

from my_dataclass.lolapi.match.perk.selection import Selection


@dataclass
class Style:
    selections: List[Selection]
    description: str = field(default="")
    style: int = field(default=0)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Style":
        data = {k if k in keyword.kwlist else f"{k}_": v for k, v in data.items()}
        return from_dict(cls, data=data)

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)