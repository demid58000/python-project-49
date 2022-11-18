import prompt


def welcome_user(prolog =''):
    print('Welcome to the Brain Games!')
    if prolog:
        print(f'{prolog}')
    name = prompt.string('May i have your name? ')
    print(f'Hello, {name}')
    return name


def answer(question):
    print(f'Question: {question}')
    answer = prompt.string('your answer: ')
    return answer

