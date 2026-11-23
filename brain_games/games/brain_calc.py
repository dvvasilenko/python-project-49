import prompt
import random

def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def brain_calc(name):
    print('What is the result of the expression?')
    attempts_number = 1

    while attempts_number <= 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])

        if operator == '+':
            correct_answer = num1 + num2
        elif operator == '-':
            correct_answer = num1 - num2
        else:
            correct_answer = num1 * num2
        print(f'Question: {num1} {operator} {num2}')
        user_answer = prompt.string('Your answer: ')
        if user_answer.lstrip('-').isdigit() and int(user_answer) == correct_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print("Let's try again!")
            break
        attempts_number += 1
    print(f'Congratulations, {name}!')

def main():
    name = welcome_user()
    brain_calc(name)

if __name__ == '__main__':
    main()