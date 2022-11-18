import prompt


def welcome_user(rule):
    print('Welcome to the brain games!')
    name = prompt.string('May i have your name?')
    print(f'Hello, {name}')
    print(rule)
    return name


def answer(question):
    print(f'Question: {question}')
    answer = prompt.string('your answer: ')
    return answer

