# main.py

import random
# import utils
from deck import Deck # import the Deck class from the deck.py file
from hand import Hand # import the Hand class from hand.py file

def main():
    # create an instance of Deck
    deck = Deck() 

    # create and shuffle deck of cards
    deck.create_deck()
    deck.shuffle()
    
    # deal 2 hole cards (player and opponent) and 3 community cards (the flop)
    player_hole = deck.deal(2)
    opponent_hole = deck.deal(2)
    flop_cards = deck.deal(3)

    # displays hand
    print("Player's hole cards: ", player_hole)
    print("Opponent's hole cards: ", opponent_hole)
    print("Community Cards: ", flop_cards)
    
    # create each player's hand
    player_hand = Hand(player_hole + flop_cards)
    opponent_hand = Hand(opponent_hole + flop_cards)

    # evaluate each player's hand
    print("You have a " + list(player_hand.evaluate())[0] + "!")
    print("Opponent has a " + list(opponent_hand.evaluate())[0] + "!")


    # simulate poker rounds (monte-carlo)
'''
    # Simulate and print win probability
    wins_prob = simulate_win_probability(player_hands, opponent_hands, flop_community_cards)

    print(f"\nPlayer's win probability: {wins_prob[0] * 100:.2f}%")
    print(f"Opponent's win probability: {wins_prob[1] * 100:.2f}%")
'''
if __name__ == "__main__":
    main()
