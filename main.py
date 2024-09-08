# main.py

import random
# import utils
from deck import Deck # import the Deck class from the deck.py file

def main():
    # create an instance of Deck
    deck = Deck() 

    # create and shuffle deck of cards
    deck.create_deck()
    deck.shuffle()
    
    # deal 2 cards (a player's hand) and 3 community flop cards
    player_hands = deck.deal(2)
    opponent_hands = deck.deal(2)
    flop_cards = deck.deal(3)

    # displays hand
    print("Player's hand: ", player_hands)
    print("Opponent's hand: ", opponent_hands)
    print("Community Cards: ", flop_cards)
    """
    # Evaluate Poker Hand

    # evaluate pair (we'll expand hand evaluation later)
    def is_pair(hand):
        # Extract the ranks from cards
        ranks = [card[:1] for card in hand]
        return len(set(ranks)) < len(ranks)

    # Test if the player has a pair
    player_and_community = player_hands + flop_community_cards
    if is_pair(player_and_community):
        print("Player has a pair!")

    # simulate poker rounds (monte-carlo)

    # Simulate and print win probability
    wins_prob = simulate_win_probability(player_hands, opponent_hands, flop_community_cards)

    print(f"\nPlayer's win probability: {wins_prob[0] * 100:.2f}%")
    print(f"Opponent's win probability: {wins_prob[1] * 100:.2f}%")
"""
if __name__ == "__main__":
    main()
