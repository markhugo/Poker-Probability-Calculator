# deck.py
from cards import Card, Deck, Hand

class Dealer:
    # initialize the deck with 52 cards (4 suits, 13 ranks)
    def __init__(self, deck):
        self.deck = deck

    # get deck of cards
    def show_deck(self):
        return [str(card) for card in self.deck]

    # get number of cards in deck
    def get_total(self):
        print(len(self.deck))

    # shuffles the deck
    def shuffle(self):
        self.deck.shuffle()
    
    # deals a specified number of cards from deck
    def deal_to_players(self, players, num_cards=2):
        for player in players:
            player.hole_cards = [self.deck.deal() for _ in range(num_cards)]

    def deal_community_cards(self, flop=3):
        # for the flop
        return [self.deck.deal() for _ in range(flop)]
        

    # resets the deck to a full 52 cards and shuffles it
    def reset(self):
        self.__init__()
        self.shuffle()

# Player class
class Player:
    # initialize player
    def __init__(self, name):
        self.name = name
        self.hole_cards = []

    # mutator method
    def receives(self, card):
        self.hole_cards.append(card)

    # accessor method
    def show_cards(self):
        print(f"{self.name}: ", self.hole_cards)
