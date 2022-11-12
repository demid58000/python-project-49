import random
from brain_games.cli import welcome_user


def main():
  print('Welcome to the Brain Games!')
  name = welcome_user()
  game_points = 0
  print('What number is missing in the progression?')
  while game_points < 3:
    first_number = random.randint(1, 5)
    second_number = random.randint(15, 20)
    step = random.randint(1, 3)
    lst_ = []
  
  
    for i in range(first_number, second_number, step):
      lst_.append(i)
    
    random_index = random.randint(0, len(lst_) - 1)
    
  
    lst_[random_index] = '..'
    
    right_answer = lst_[random_index - 1] +step
    if random_index == 0:
      right_answer = lst_[1] - step
    
    
    string = " ".join(map(str, lst_))
    
    print(string)
    user_answer = int(input())
    if user_answer == right_answer:
      print('Correct!')
      game_points += 1
    else:
      print(f'{user_answer} is wrong answer ;(. Correct answer was {right_answer}.')
      print(f"Let's try again, {name}!")
      break
    if game_points == 3:
      print(f'Congratulations, {name}!')