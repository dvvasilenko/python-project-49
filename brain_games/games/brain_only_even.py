import random
from brain_games.scripts.game_logic import run_game

description = 'Answer "yes" if the number is even, otherwise answer "no".'

def generate_round():
    expression = random.randint(1, 100)
    if expression % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return expression, correct_answer

def play():
    run_game(description, generate_round)

if __name__ == '__main__':
    play()