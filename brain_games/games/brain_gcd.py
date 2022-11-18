import math
import random


rule = 'Find the greatest common divisor of given numbers.'

def start_game():
    
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        right_answer = math.gcd(first_number, second_number)
        question = f'Question: {first_number} {second_number}'
        
        # if right_answer == nod:
        #     your_answer = right_answer
            
        # elif your_answer != nod:
        #     return
        return (question, str(right_answer))

            
            
        