# deck.py
import random
from cards import Card, Hand

class Dealer:
    # initialize the deck with 52 cards (4 suits, 13 ranks)
    def __init__(self):
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.deck = [Card(rank, suit) for suit in suits for rank in ranks]

    """
    def create_sim_deck(self, player_hand, opponent_hand, community_cards):
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return [rank + suit for rank in ranks for suit in suits if rank + suit not in player_hand + opponent_hand + community_cards]
    """

    # get deck of cards
    def show_deck(self):
        return [str(card) for card in self.deck]

    # get number of cards in deck
    def get_total(self):
        print(len(self.deck))

    # shuffles the deck
    def shuffle(self):
        random.shuffle(self.deck)
    
    # deals a specified number of cards from deck
    def deal(self):
        return self.deck.pop() if self.deck else None

    # resets the deck to a full 52 cards and shuffles it
    def reset(self):
        self.__init__()
        self.shuffle()

# Player class
class Player:
    # initialize player
    def __init__(self, name):
        self.name = name
        self.hole_cards = Hand()

    # mutator method
    def receives(self, card):
        self.hole_cards.add(card)

    # accessor method
    def show_cards(self):
        print(f"{self.name}: ", self.hole_cards)
