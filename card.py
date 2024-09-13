# card.py

class Card:
    # initiallize a card with a rank and suit
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # return a readable string representation of the card
    def __str__(self):
        return f"{self.rank} of {self.suit}"

    # return the official string representation of the card
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

    # compare two cards to see if they are equal
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    # allow cards to be used in sets or as dictionary keys
    def __hash__(self):
        return hash((self.rank), (self.suit))
