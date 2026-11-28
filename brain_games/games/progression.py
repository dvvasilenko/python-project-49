import random

description = 'What number is missing in the progression?'

def generate_progression(start, step, length):
    progression = []
    for index in range(length):
        current_element = start + index * step
        progression.append(str(current_element))
    return progression

def progression_round():
    progression_length = 10
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    progression = generate_progression(start, step, progression_length)

    hidden_index = random.randint(0, progression_length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'

    expression = ' '.join(progression)
    return expression, correct_answer