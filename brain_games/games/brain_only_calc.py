import random

from brain_games.scripts.game_logic import run_game

description = 'What is the result of the expression?'


def generate_round():
    
    operators = ['+', '-', '*']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(operators)

    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    expression = f"{num1} {operator} {num2}"
    return expression, str(correct_answer)


def play():
    run_game(description, generate_round)


if __name__ == '__main__':

    play()