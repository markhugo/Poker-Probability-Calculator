# game.py

from itertools import combinations
from deck import Deck
from hand import Hand

class Game:
    def __init__(self, player_names):
        self.deck = Deck()
        self.players = [Player(name) for name in player_names]
        self.community_cards = []

    def deal_community_cards(self, num):
        for _ in range(num):
            self.community_cards.append(self.deck.deal())

    def evaluate_hands(self):
        best_hands = {}
        for player in self.players:
            player_hand = player.hand.cards + self.community_cards
            best_hand = Hand()
            for hand_combination in combinations(player_hand, 5):
                best_hand.add_card(max(hand_combination, key=lambda x: player.hand.rank_to_int(x.rank)))
            best_hands[player.name] = best_hand.evaluate()
        return best_hands

    def start_game(self):
        self.deck.shuffle()
        # Deal hole cards
        for player in self.players:
            player.receive_card(self.deck.deal())
            player.receive_card(self.deck.deal())
        # Deal community cards (flop, turn, river)
        self.deal_community_cards(3)  # Flop
        self.deal_community_cards(1)  # Turn
        self.deal_community_cards(1)  # River

        return self.evaluate_hands()

# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def receive_card(self, card):
        self.hand.add_card(card)

    def show_cards(self):
        print(f"{self.name}: {self.hand}")