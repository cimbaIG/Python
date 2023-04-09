from dataclasses import dataclass


# DataClass is created using the @dataclass decorator
@dataclass
class DataClassCard:
    rank: str
    suit: str
