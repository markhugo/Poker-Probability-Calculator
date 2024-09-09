# deck.py
from collections import Counter
import random

class Deck:
    def __init__(self):
        self.cards = self.create_deck()

    # creates a standard deck of 52 cards
    def create_deck(self):
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return [rank + suit for rank in ranks for suit in suits]
    
    def create_sim_deck(self, player_hand, opponent_hand, community_cards):
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        return [rank + suit for rank in ranks for suit in suits if rank + suit not in player_hand + opponent_hand + community_cards]

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
    def deal(self, num):
        dealt_cards = self.cards[:num]
        self.cards = self.cards[num:]
        return dealt_cards


    # resets the deck to a full 52 cards and shuffles it
    def reset(self):
        self.cards = self.create_deck()
        self.shuffle_deck()



