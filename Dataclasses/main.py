from dataclass_card import DataClassCard


if __name__ == "__main__":
    
    # Instantiate dataclass
    queen_of_hearts = DataClassCard('Q', 'Hearts')
    
    # Print dataclass attributes
    print(queen_of_hearts.rank, queen_of_hearts.suit)
    # Print dataclass instance
    print(queen_of_hearts)
    # We can even compare data class instances out of the box
    print(queen_of_hearts == DataClassCard("Q", "Hearts"))