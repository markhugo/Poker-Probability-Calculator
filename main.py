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
flop_community_cards = deck[2:5]

print("Player's hand: ", player_hands)
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
def simulate_win_probability(player_hand, flop_community_cards, num_simulations = 1000):
    wins = 0
    for _ in range(num_simulations):
        # shuffle a new deck and simulate other players' hands and remaining community cards
        deck = []
        for rank in ranks:
            for suit in suits:
                if rank + suit not in player_hand + flop_community_cards:
                    deck.append(rank + suit)
        random.shuffle(deck)
        
        # deal hands to other players (assuming 1 opponent for simplicity; will be expanded later)
        opponent_hand = deck[:2]
        remaining_community = deck[5:7]

        # combine community cards with both hands
        player_final_hand = player_hand + flop_community_cards + remaining_community
        opponent_final_hand = opponent_hand + flop_community_cards + remaining_community

        # evaluate both hands (for simplicity, we'll use a basic pair check)
        player_has_pair = is_pair(player_final_hand)
        opponent_has_pair = is_pair(opponent_final_hand)

        # simple evaluation: if player has a pair, and opponenet doesn't, count it as a win
        if player_has_pair and not opponent_has_pair:
            wins += 1
        
    # calculate win probability
    return wins / num_simulations

# Simulate and print win probability
win_prob = simulate_win_probability(player_hands, flop_community_cards)
print(f"Player's win probability: {win_prob * 100:.2f}%")

