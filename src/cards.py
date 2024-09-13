# cards.py

from collections import Counter

# Card class
class Card:
    # initiallize a card with a rank and suit
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # return a readable string representation of the card
    def __str__(self):
        return f"{self.rank}{self.suit}"

    # return the official string representation of the card
    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

    # allow cards to be used in sets or as dictionary keys
    def __hash__(self):
        return hash((self.rank), (self.suit))


# Hand class
class Hand:
    def __init__(self):
        """Initialize an empty hand."""
        self.hand = []

    def add(self, card):
        """Add a card to the hand."""
        self.hand.append(card)

    def show(self):
        return [str(card) for card in self.hand]

    def evaluate(self):
        """Evaluate the strength of the best possible 5-card hand from up to 7 cards."""
        #if len(self.hand) < 5:
        #   return "Not enough cards to evaluate."

        best_hand = None
        best_hand_rank = None
        # Evaluate all combinations of 5 cards out of up to 7 cards
        from itertools import combinations
        for hand_combination in combinations(self.hand, 5):
            hand_rank = self.rank_hand(hand_combination)
            if best_hand_rank is None or hand_rank > best_hand_rank:
                best_hand_rank = hand_rank
                best_hand = hand_combination

        return self.hand_rank_to_string(best_hand_rank)

    def rank_hand(self, hand):
        """Rank the given 5-card hand and return a rank value."""
        rank_counts = Counter(card.rank for card in hand)
        suit_counts = Counter(card.suit for card in hand)
        sorted_ranks = sorted(set(self.rank_to_int(card.rank) for card in hand), reverse=True)

        is_flush = len(suit_counts) == 1
        is_straight = self.is_straight(sorted_ranks)
        rank_counts_values = sorted(rank_counts.values(), reverse=True)

        # Hand ranking logic
        if is_flush and is_straight:
            return 8 if sorted_ranks[0] == 14 and sorted_ranks[-1] == 10 else 7  # Straight Flush or Royal Flush
        if rank_counts_values[0] == 4:
            return 6  # Four of a Kind
        if rank_counts_values[0] == 3 and rank_counts_values[1] == 2:
            return 5  # Full House
        if is_flush:
            return 4  # Flush
        if is_straight:
            return 3  # Straight
        if rank_counts_values[0] == 3:
            return 2  # Three of a Kind
        if rank_counts_values[0] == 2 and rank_counts_values[1] == 2:
            return 1  # Two Pair
        if rank_counts_values[0] == 2:
            return 0  # One Pair

        return -1  # High Card

    def is_straight(self, ranks):
        """Check if the hand is a straight."""
        if len(ranks) < 5:
            return False
        rank_set = set(ranks)
        return len(rank_set) == 5 and max(rank_set) - min(rank_set) == 4

    def rank_to_int(self, rank):
        """Convert rank to integer value for comparison."""
        if rank == 'A':
            return 14
        if rank == 'K':
            return 13
        if rank == 'Q':
            return 12
        if rank == 'J':
            return 11
        return int(rank)

    def hand_rank_to_string(self, rank):
        """Convert rank value to a hand strength string."""
        ranks = {
            8: "Royal Flush",
            7: "Straight Flush",
            6: "Four of a Kind",
            5: "Full House",
            4: "Flush",
            3: "Straight",
            2: "Three of a Kind",
            1: "Two Pair",
            0: "One Pair",
            -1: "High Card"
        }
        return ranks.get(rank, "Unknown Hand")