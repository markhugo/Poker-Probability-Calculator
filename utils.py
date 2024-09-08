# utils.py

import random

# create deck
def create_deck():


def deal_hands(players, deck):
    hands = [deck[:2] for player in players]

# Simulating Poker Rounds (Monte Carlo)
def simulate_win_probability(player_hand, opponent_hand, flop_community_cards, num_simulations = 1000):
    player_wins = 0
    opp_wins = 0
    for _ in range(num_simulations):
        # shuffle a new deck and simulate remaining community cards
        deck = [rank + suit for rank in ranks for suit in suits if rank + suit not in player_hand + opponent_hand + flop_community_cards]
        random.shuffle(deck)
            
        # deal hands to other players (assuming 1 opponent for simplicity; will be expanded later)
        remaining_community = deck[:3]

        # combine community cards with both hands
        player_final_hand = player_hand + flop_community_cards + remaining_community
        opponent_final_hand = opponent_hand + flop_community_cards + remaining_community

        # evaluate both hands (for simplicity, we'll use a basic pair check)
        player_has_pair = is_pair(player_final_hand)
        opponent_has_pair = is_pair(opponent_final_hand)

        # simple evaluation: if player has a pair, and opponenet doesn't, count it as a win
        if player_has_pair and not opponent_has_pair:
            player_wins += 1
        if opponent_has_pair and not player_has_pair:
            opp_wins += 1
            
        wins = [player_wins, opp_wins]
    # calculate win probability
    win_prob = [win/num_simulations for win in wins]
    return win_prob