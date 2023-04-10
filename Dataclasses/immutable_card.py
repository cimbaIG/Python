from dataclasses import dataclass


# frozen=True to make data class immutable
# Even though both ImmutableCard and ImmutableDeck are immutable, the list 
# holding cards is not. You can therefore still change the cards in the deck!
@dataclass(frozen=True)
class ImmutableCard:
    
    rank: str
    suit: str
