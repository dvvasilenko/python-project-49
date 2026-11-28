import prompt


def run_game(description, generate_round):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(description)
    attempts_number = 1
    
    while attempts_number <= 3:
        attempts_number += 1
        expression, correct_answer = generate_round()
        print(f'Question: {expression}')
        user_answer = input('Your answer: ')

        if user_answer != correct_answer:
            print(f"'{user_answer}' is the wrong answer ;(. The correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        
        print('Correct!')

    print(f'Congratulations, {name}!')