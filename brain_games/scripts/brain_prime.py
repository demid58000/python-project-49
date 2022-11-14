from sympy import *
import random
from brain_games.cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    game_points = 0
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    while game_points < 3:
        number = random.randint(1, 100)
        is_prime = isprime(number)
        print(number)
        user_answer = input()
        if user_answer == 'yes' and is_prime == True:
            print("Correct!")
            game_points += 1
        elif user_answer == 'yes' and is_prime == False:
            print(f'{user_answer} is wrong answer ;(. Correct answer was no.')
            print(f"Let's try again, {name}!")
            break
        elif user_answer == 'no' and is_prime == True:
            print(f'{user_answer} is wrong answer ;(. Correct answer was yes.')
            print(f"Let's try again, {name}!")
            break
        elif user_answer == 'no' and is_prime == False:
            print('Correct')
            game_points += 1
        if game_points == 3:
            print(f'Congratulations, {name}!')
            
            

        # if is_prime == True:
        #     print('Correct!')
        #     game_points += 1
        # else:
        #     print(f'{user_answer} is wrong answer ;(. Correct answer was {right_answer}.')
        #     print(f"Let's try again, {name}!")
        #     break
        # if game_points == 3:
        #     print(f'Congratulations, {name}!')




