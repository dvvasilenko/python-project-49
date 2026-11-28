from brain_games.scripts.game_logic import run_game
from brain_games.games.progression import description, progression_round


def play():
    
    run_game(description, progression_round)


if __name__ == '__main__':

    play()