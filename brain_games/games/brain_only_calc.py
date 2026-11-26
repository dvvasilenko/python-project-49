import random

def random_calculator():
    """Generate a random arithmetic expression and its result"""
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
    return expression, correct_answer

def main():
    random_calculator()

if __name__ == '__main__':
    main()