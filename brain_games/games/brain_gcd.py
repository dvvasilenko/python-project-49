import random

description = 'Find the greatest common divisor of given numbers.'
def gcd_round():
    
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    expression = f'{a} {b}'
    
    if b == 0:
        correct_answer = a

    while b != 0:
        a, b = b,  a % b
    correct_answer = str(a)
    return expression, correct_answer