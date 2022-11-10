import random



def main():
  
  print('Answer "yes" if the number is even, otherwise answer "no"')
  right_answers = 0
  
  while right_answers < 3:
      random_number = random.randint(1, 100)
      print(random_number)
      answer = input('Your answer: ')
      if random_number % 2 == 0 and answer == 'yes':
          print('Correct!')
          right_answers += 1 
      elif random_number % 2 == 0 and answer == 'no':
        print('Wrong answer')
        break
      elif random_number % 2 != 0 and answer == 'no':
        print('Correct!')
        right_answers += 1
      elif random_number % 2 != 0 and answer == 'yes':
        print('Wrong answer')
        break
      if right_answers == 3:  
        print('Congratulations, ivan!')






