from dataclasses import dataclass, field
from playing_card import PlayingCard
from typing import List


@dataclass
class Deck:
    
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
    SUITS = '♣ ♢ ♡ ♠'.split()
    
    @staticmethod
    def make_french_deck():
        return [PlayingCard(r, s) for s in Deck.SUITS for r in Deck.RANKS]
    
    # cards: List[PlayingCard] = Deck.make_french_deck()
    # Don’t do this! This introduces one of the most common anti-patterns in 
    # Python: using mutable default arguments. The problem is that all 
    # instances of Deck will use the same list object as the default value of 
    # the .cards property. This means that if, say, one card is removed from 
    # one Deck, then it disappears from all other instances of Deck as well. 
    # Actually, data classes try to prevent you from doing this, and the code 
    # above will raise a ValueError.
    # Instead, data classes use something called a default_factory to handle 
    # mutable default values. To use default_factory (and many other cool 
    # features of data classes), you need to use the field() specifier:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)
    # The field() specifier is used to customize each field of a data class 
    # individually. You will see some other examples later. For reference, 
    # these are the parameters field() supports:
    #   default: Default value of the field
    #   default_factory: Function that returns the initial value of the field
    #   init: Use field in .__init__() method? (Default is True.)
    #   repr: Use field in repr of the object? (Default is True.)
    #   compare: Include the field in comparisons? (Default is True.)
    #   hash: Include the field when calculating hash()? (Default is to use the 
    #         same as for compare.)
    #   metadata: A mapping with information about the field
    