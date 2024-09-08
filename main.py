# main.py

import random

# Basic Poker Hand Representations

# define the suits and ranks of a deck
suits = ['♠', '♥', '♦', '♣']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# create a deck of 52 cards
deck = []
for rank in ranks:
    for suit in suits:
        deck.append(rank + suit)

# test if deck is complete (should be 52 cards)
print(len(deck))

# shuffle the deck
random.shuffle(deck)

# deal 2 cards (a player's hand) and 5 community cards
player_hands = deck[:2]
opponent_hands = deck[2:4]
flop_community_cards = deck[4:7]

print("Player's hand: ", player_hands)
print("Opponent's hand: ", opponent_hands)
print("Flop Community cards: ", flop_community_cards)

# Evaluate Poker Hand

# evaluate pair (we'll expand hand evaluation later)
def is_pair(hand):
    # Extract the ranks from cards
    ranks = []
    for card in hand:
        ranks.append(card[:1])
    return len(set(ranks)) < len(ranks)

# Test if the player has a pair
player_and_community = player_hands + flop_community_cards
if is_pair(player_and_community):
    print("Player has a pair!")

# Simulating Poker Rounds (Monte Carlo)
def simulate_win_probability(player_hand, opponent_hand, flop_community_cards, num_simulations = 1000):
    player_wins = 0
    opp_wins = 0
    for _ in range(num_simulations):
        # shuffle a new deck and simulate remaining community cards
        deck = []
        for rank in ranks:
            for suit in suits:
                if rank + suit not in player_hand + opponent_hand + flop_community_cards:
                    deck.append(rank + suit)
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

# Simulate and print win probability
wins_prob = simulate_win_probability(player_hands, opponent_hands, flop_community_cards)

print(f"\nPlayer's win probability: {wins_prob[0] * 100:.2f}%")
print(f"Opponent's win probability: {wins_prob[1] * 100:.2f}%")

