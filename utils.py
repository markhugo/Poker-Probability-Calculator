# utils.py

import random
from deck import Deck
from hand import Hand

# Simulating Poker Rounds (Monte Carlo)
def simulate_win_probability(player_hole, opponent_hole, flop_community_cards, num_simulations=1000):
    player_wins = 0
    opp_wins = 0
    for _ in range(num_simulations):
        # shuffle a new deck and simulate remaining community cards
        sim_deck = Deck()
        sim_deck.create_sim_deck(player_hole, opponent_hole, flop_community_cards)
        sim_deck.shuffle()
            
        # deal hands to other players (assuming 1 opponent for simplicity; will be expanded later)
        remaining_community = sim_deck.deal(2)

        # combine community cards with both hands
        player_final_hand = player_hole + flop_community_cards + remaining_community
        opponent_final_hand = opponent_hole + flop_community_cards + remaining_community

        # create and evaluateeach player's hand
        player_hand = Hand(player_final_hand)
        player_rank = player_hand.evaluate()
        opponent_hand = Hand(opponent_final_hand)
        opponent_rank = opponent_hand.evaluate()

        # increment each win for player
        if player_rank.get(list(player_rank)[0]) > opponent_rank.get(list(opponent_rank)[0]):
            player_wins+=1 
        else:
            opp_wins+=1
        
        wins = [player_wins, opp_wins]
    
    # calculate win probability
    win_prob = calc_win_prob(wins, num_simulations)
    return win_prob

# calculates win probability (needs implentation)    
def calc_win_prob(num_wins, num_simulations):
    return [win/num_simulations for win in num_wins]
