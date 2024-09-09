# hand.py

from collections import Counter

rank_order = {'1': 1,'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

class Hand:
    def __init__(self, cards):
        # Store the hand
        self.cards = cards
        
        # Sort cards by rank for easier evaluation
        self.sorted_by_rank = sorted(cards, key=lambda card: rank_order[card[0]])
        self.ranks = [card[0] for card in self.sorted_by_rank]
        self.suits = [card[1] for card in self.sorted_by_rank]
        self.rank_counts = Counter(self.ranks)
    
    # evaluate all hands
    def evaluate(self):
        if self.is_flush() and self.is_straight():
            if self.ranks[-1] == 'A':
                return {"Royal Flush": 10}
            return {"Straight Flush": 9}
        elif self.is_four_of_a_kind():
            return {"Four of a Kind": 8}
        elif self.is_full_house():
            return {"Full House": 7}
        elif self.is_flush():
            return {"Flush": 6}
        elif self.is_straight():
            return {"Straight": 5}
        elif self.is_three_of_a_kind():
            return {"Three of a Kind": 4}
        elif self.is_two_pair():
            return {"Two Pair": 3}
        elif self.is_one_pair():
            return {"One Pair": 2}
        else:
            return {"High Card": 1}


    # helper methods for evaluating hands
    def is_flush(self):
        return len(set(self.suits)) == 1

    def is_straight(self):
        rank_values = [rank_order[rank] for rank in self.ranks]
        return rank_values == list(range(rank_values[0], rank_values[0] + 5))

    def is_four_of_a_kind(self):
        return 4 in self.rank_counts.values()

    def is_full_house(self):
        return 3 in self.rank_counts.values() and 2 in self.rank_counts.values()

    def is_three_of_a_kind(self):
        return 3 in self.rank_counts.values()

    def is_two_pair(self):
        return list(self.rank_counts.values()).count(2) == 2

    def is_one_pair(self):
        return 2 in self.rank_counts.values()

    def high_card(self):
        return max(self.cards, key=lambda card: rank_order[card[0]])

    def __repr__(self):
        return f"Hand({self.cards})"
