import math
import random
from brain_games.cli import welcome_user

def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    game_points = 0 
    
    
    while game_points < 3:
        first_number = random.randint(1, 100)
        second_number = random.randint(1, 100)
        nod = math.gcd(first_number, second_number)
        print(f'Question: {first_number} {second_number}')
        user_answer = int(input('Your answer: '))
        if user_answer == nod:
            print('Correct!')
            game_points += 1
        else:
            print(f'{user_answer} wrong answer ;(. Correct answer was {nod}.')
            print(f"Let's try again, {name}")
            break
        if game_points == 3:
            print(f'Congrats! {name}')