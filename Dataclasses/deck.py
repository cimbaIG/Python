from dataclasses import dataclass
from playing_card import PlayingCard
from typing import List


@dataclass
class Deck:
    
    cards: List[PlayingCard]