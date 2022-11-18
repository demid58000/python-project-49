from random import randint

rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

        
def start_game():
    prime = '' 
    question = randint(0, 100)
    if IsPrime(question) == True:
        prime = 'yes'
    elif IsPrime(question) == False:
        prime = 'no'
    return (question, prime)
