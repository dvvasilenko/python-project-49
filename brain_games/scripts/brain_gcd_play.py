from brain_games.scripts.game_logic import run_game
from brain_games.games.brain_gcd import description, gcd_round


def play():
    
    run_game(description, gcd_round)


if __name__ == '__main__':

    play()