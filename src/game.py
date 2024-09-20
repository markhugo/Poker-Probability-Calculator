# game.py

from itertools import combinations
from players import Dealer, Player
from cards import Hand, Deck

class Game:
    def __init__(self, player_names):
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.players = [Player(name) for name in player_names]
        self.community_cards = []

    # evaluates hands of each player
    def evaluate_hands(self):
        best_hands = {}
        for player in self.players:
            player_hand = Hand()
            player_hand.add(player.hole_cards + self.community_cards)
            best_hand = Hand()
            for hand_combination in combinations(player_hand.list(), 5):
                best_hand.add(max(hand_combination, key=lambda x: player_hand.rank_to_int(x.rank)))
            best_hands[player.name] = best_hand.evaluate()
        return best_hands

    def start_game(self):
        self.dealer.shuffle()
        # Deal hole cards
        self.dealer.deal_to_players(self.players)
        # Deal community cards (flop, turn, river)
        self.community_cards = self.dealer.deal_community_cards()
        
        ''' needs implementation later below
        self.deal_community_cards(1)  # Turn
        self.deal_community_cards(1)  # River
        '''

        return self.evaluate_hands()

