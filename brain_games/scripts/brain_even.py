import prompt
import random

def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def brain_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempts_number = 1
    
    while attempts_number <= 3:
        
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')

        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f"{user_answer} is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

        attempts_number += 1

    print(f'Congratulations, {name}!')

def main():
    name = welcome_user()
    brain_even(name)

if __name__ == '__main__':
    main()


