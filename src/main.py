# main.py

# from utils import simulate_win_probability
from game import Game

def main():
    # Example usage
    game = Game(['Mark', 'Emmy'])
    game.start_game()
    
    # print players' cards
    for player in game.players:
        player.show_cards()
    
    # Print community cards
    print("Community Cards:", game.community_cards)

    #
    # Print hands evaluation
    print("\nPlayer Hands Evaluation:")
    for player, hand in game.evaluate_hands().items():
        print(f"{player}: {hand}")

    '''
    # simulate poker rounds (monte-carlo)
    wins_prob = simulate_win_probability(player_hole, opponent_hole, flop_cards)
    
    # print win
    print(f"\nPlayer's win probability: {wins_prob[0] * 100:.2f}%")
    print(f"Opponent's win probability: {wins_prob[1] * 100:.2f}%")
    '''

if __name__ == "__main__":
    main()
