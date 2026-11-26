from brain_games.cli import welcome_user
from brain_games.games.brain_only_calc import random_calculator

name = welcome_user()

def game_logic(name):
    print('Welcome to the Brain Games!')
    print('What is the result of the expression?')
    attempts_number = 1

    # What game to play


    while attempts_number <= 3:
        attempts_number += 1
        expression, correct_answer = random_calculator()
        
        print(f'Question: {expression}')
        
        user_answer = input('Your answer: ')
        
        if user_answer.lstrip('-').isnumeric() and correct_answer == int(user_answer):
            print('Correct!')
        else:
            print('Wrong answer ;(. Please try again.')
            break

    print(f'Congratulations, {name}!')

def main():
    game_logic(name)

if __name__ == '__main__':
    main()