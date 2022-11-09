import random
from brain_games.cli import welcome_user



def calc():
    name = welcome_user()
    sign = ['+', '*', '-' ]
    print('What is the result of the expression?')
    
    game_points = 0
    
    while game_points < 3:
      first_number = random.randint(1, 100)
      second_number = random.randint(1, 100)
      sign_ = random.choice(sign)
      print(f'Question: {first_number} {sign_} {second_number}')
      user_answer = int(input('Your answer: '))
      if sign_ == '+':
        right_answer = first_number + second_number
        if right_answer == user_answer:
          game_points += 1
          print('Correct!')
        else:
          return f'{user_answer} is wrong answer ;(. Correct answer was {right_answer}'
          break
      elif sign_ == '-':
          right_answer = first_number - second_number
          if right_answer == user_answer:
            game_points += 1
            print('Correct!')
          else:
            return f'{user_answer} is wrong answer ;(. Correct answer was {right_answer}'
            break
      elif sign_ == '*':
          right_answer = first_number * second_number
          if right_answer == user_answer:
            game_points += 1
            print('Correct!')
          else:
            return f'{user_answer} is wrong answer ;(. Correct answer was {right_answer}'
            break
        
      
      if game_points == 3:
        return f'Congrats! {name}'
      
          


             


