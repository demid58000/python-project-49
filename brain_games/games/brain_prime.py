from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def generate_answer_and_question():
    prime = ''
    question = randint(0, 100)
    if is_prime(question) is True:
        prime = 'yes'
    elif is_prime(question) is False:
        prime = 'no'
    return (question, prime)
