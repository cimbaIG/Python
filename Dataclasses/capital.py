from position import Position
from dataclasses import dataclass


@dataclass(frozen=True)
class Capital(Position):
    
    country: str = "Some country"
