from dataclasses import dataclass


@dataclass
class PlayingCard:

    rank: str
    suit: str

    # Dataclasses implement obj.__repr__() which returns a developer-friendly 
    # representation of obj. Dataclasses do not implement obj.__str__() which 
    # returns a user-friendly representation of obj.
    def __str__(self):
        return f'{self.suit}{self.rank}'
