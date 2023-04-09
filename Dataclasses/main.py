from dataclass_card import DataClassCard
from regular_card import RegularCard
from position import Position
from playing_card import PlayingCard
from deck import Deck
from collections import namedtuple
from dataclasses import fields


if __name__ == "__main__":
    
    # Instantiate dataclass
    queen_of_hearts = DataClassCard('Q', 'Hearts')
    
    # Print dataclass attributes
    print(queen_of_hearts.rank, queen_of_hearts.suit)
    # Print dataclass instance
    print(queen_of_hearts)
    # We can even compare data class instances out of the box
    print(queen_of_hearts == DataClassCard("Q", "Hearts"))
    
    print()
    
    # Now let's instantiate an instance using regular class
    queen_of_hearts = RegularCard("Q", "Hearts")
    # We can still print attributes in standard way
    print(queen_of_hearts.rank, queen_of_hearts.suit)
    # We cannot print regular class object data out of the box a we can when 
    # data class is used. This is because data class implements .__repr__()
    # method to provide a nice string representation and .__eq__() method that
    # can do basic object comparisons.
    # To achieve the same using regular class, we have to implement __repr__() 
    # and __eq__() in RegularCard class.
    print(queen_of_hearts)
    print(queen_of_hearts == RegularCard("Q", "Hearts"))
    
    # Alternatives to data classes - tuple or dict!
    queen_of_hearts_tuple = ('Q', 'Hearts')
    queen_of_hearts_dict = {'rank': 'Q', 'suit': 'Hearts'}
    # However, we have to remember that queen_of_hearts_... variable represents
    # a card. Moreover, for a tuple we need to remember the order of attributes.
    # If we use dict, we have to make sure that attribute names are consistent.
    # In the case of tuple, we also cannot access the values by names.
    
    print()
    
    # The better alternative is to use namedtuple. For instance:
    NamedTupleCard = namedtuple("NamedTupleCard", ['rank', 'suit'])
    queen_of_hearts = NamedTupleCard("Q", "Hearts")
    print(queen_of_hearts.rank, queen_of_hearts.suit)
    print(queen_of_hearts)
    print(queen_of_hearts == NamedTupleCard("Q", "Hearts"))
    # By design, the namedtuple is a regular tuple. It is hard to add default 
    # values to some of the fields in a namedtuple and it is by nature 
    # immutable. For instance, the following will raise 
    # AttributeError: can't set attribute.
    # card = NamedTupleCard('7', 'Diamonds')
    # card.rank = '9'
    # If you need that your data structure behave like a tuple, then use named 
    # tuples as they are great alternative!
    
    print()
    
    # Instantiate Position instance
    pos = Position('Oslo', 10.8, 59.9)
    # Print instance data
    print(pos)
    print(f'{pos.name} is at {pos.lat}°N, {pos.lon}°E.')
    
    print()
    
    # Use default values in dataclass (this works exactly as we had specified 
    # the default values in the definition of the .__init__() method of a 
    # regular class).
    print(Position('Null Island'))
    print(Position('Greenwich', lat=51.8))
    print(Position('Vancouver', -123.1, 49.3))
    
    print()
    
    # Adding methods to dataclass
    oslo = Position('Oslo', 10.8, 59.9)
    vancouver = Position('Vancouver', -123.1, 49.3)
    print(f"Distance from {oslo.name} to {vancouver.name} is " \
          + f"{oslo.distance_to(vancouver)} km.")
    
    print()
    
    # More flexible data classes
    # Instantiate objects of PlayingCard and Deck data classes.
    queen_of_hearts = PlayingCard('Q', 'Hearts')
    print(queen_of_hearts)
    ace_of_spades = PlayingCard('A', 'Spades')
    print(ace_of_spades)
    two_cards = Deck([queen_of_hearts, ace_of_spades])
    print(two_cards)
    
    print()
    
    # Advanced default values
    print(Deck())
    print()
    # Use .fields() function to retrieve metadata from dataclass
    print(fields(Position))
    print()
    print(fields(Position)[2].metadata['unit'])