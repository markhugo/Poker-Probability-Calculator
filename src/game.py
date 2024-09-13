# game.py

from itertools import combinations
from players import Dealer, Player
from cards import Hand

class Game:
    def __init__(self, player_names):
        self.dealer = Dealer()
        self.players = [Player(name) for name in player_names]
        self.community_cards = Hand()

    # evaluates hands of each player
    def evaluate_hands(self):
        best_hands = {}
        for player in self.players:
            player_hand = player.hole_cards + self.community_cards
            best_hand = Hand()
            for hand_combination in combinations(player_hand, 5):
                best_hand.add(max(hand_combination, key=lambda x: player.hole_cards.rank_to_int(x.rank)))
            best_hands[player.name] = best_hand.evaluate()
        return best_hands

    def start_game(self):
        self.dealer.shuffle()
        # Deal hole cards
        for player in self.players:
            player.receives(self.dealer.deal())
            player.receives(self.dealer.deal())
        # Deal community cards (flop, turn, river)
        self.community_cards.add(self.dealer.deal())  # Flop
        self.community_cards.add(self.dealer.deal())
        self.community_cards.add(self.dealer.deal())
        
        ''' needs implementation later below
        self.deal_community_cards(1)  # Turn
        self.deal_community_cards(1)  # River
        '''

        return self.evaluate_hands()

