# deck.py
import random
from card import Card

class Deck:
    # initialize the deck with 52 cards (4 suits, 13 ranks)
    def __init__(self):
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]

    """
    def create_sim_deck(self, player_hand, opponent_hand, community_cards):
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return [rank + suit for rank in ranks for suit in suits if rank + suit not in player_hand + opponent_hand + community_cards]
    """

    # get deck of cards
    def show_deck(self):
        print(self.cards)

    # get number of cards
    def get_total(self):
        print(len(self.cards))

    # shuffles the deck
    def shuffle(self):
        random.shuffle(self.cards)
    
    # deals a specified number of cards from deck
    def deal(self):
        return self.cards.pop() if self.cards else None 

    # resets the deck to a full 52 cards and shuffles it
    def reset(self):
        self.__init__()
        self.shuffle()



