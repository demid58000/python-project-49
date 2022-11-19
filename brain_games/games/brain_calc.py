import random

rule = "What is the result of the expression?"


def generate_answer_and_question():
    sign = ['+', '*', '-']
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    sign_ = random.choice(sign)
    question = f'{first_number} {sign_} {second_number}'
    if sign_ == '+':
        right_answer = first_number + second_number
    elif sign_ == '-':
        right_answer = first_number - second_number
    elif sign_ == '*':
        right_answer = first_number * second_number
    return (question, str(right_answer))
