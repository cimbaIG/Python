from immutable_card import ImmutableCard
from dataclasses import dataclass
from typing import List


# frozen=True to make data class immutable
# Even though both ImmutableCard and ImmutableDeck are immutable, the list 
# holding cards is not. You can therefore still change the cards in the deck!
@dataclass(frozen=True)
class ImmutableDeck:
    
    cards: List[ImmutableCard]
