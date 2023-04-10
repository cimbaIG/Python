from dataclasses import dataclass, field
from playing_card import PlayingCard, SUITS, RANKS
from typing import List


@dataclass
class Deck:
    
    @staticmethod
    def make_french_deck():
        return [PlayingCard(r, s) for s in SUITS for r in RANKS]
    
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
    
    # We can also add our own __repr__() inside Deck dataclass (although it 
    # exists by default).
    def __repr__(self):
        # Note the !s specifier in the {card!s} format string. It means that we 
        # explicitly want to use the str() representation of each PlayingCard. 
        # With the new .__repr__(), the representation of Deck is easier on the 
        # eyes. However, it comes at a cost. You’re no longer able to recreate 
        # the deck by executing its representation. Often, you’d be better off 
        # implementing the same representation with .__str__() instead.
        cards = ', '.join(f'{card!s}' for card in self.cards)
        return f'{self.__class__.__name__}({cards})'
    