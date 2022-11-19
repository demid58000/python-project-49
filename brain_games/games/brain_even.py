from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_answer_and_question():
    question = randint(1, 100)
    if question % 2 == 0:
        even = 'yes'
    elif question % 2 != 0:
        even = 'no'
    return (question, even)
