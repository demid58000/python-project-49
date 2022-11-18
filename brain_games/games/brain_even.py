from random import randint

  
rule = 'Answer "yes" if the number is even, otherwise answer "no".'

def start_game():
        question = randint(1, 100)
        if question % 2 == 0:
                even = 'yes'
        elif question % 2 != 0:
                even = 'no'
        return (question, even)


                
