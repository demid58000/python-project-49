import random


def is_even():
  print('Answer "yes" if the number is even, otherwise answer "no"')
  right_answers = 0
  while right_answers < 3:
      random_number = random.randint(1, 100)
      print(random_number)
      if random_number % 2 == 0 and input('Your answer:') == 'yes':
          print('Correct!')
          right_answers += 1
      elif random_number % 2 != 0 and input('Your answer:') == 'no':
          print('Correct!')
          right_answers += 1
      elif random_number % 2 == 0 and input('Your answer:') == 'no':
          print('"no" is wrong answer ;(. Correct answer was "no"')
          print("Let's try again, Bill!")
          break
      elif random_number % 2 !=0 and input('Your answer:') == 'yes':
          print('"no" is wrong answer ;(. Correct answer was "no"')
          print("Let's try again, Bill!")
          break
      if right_answers == 3:
        return 'Congratulations, alt!'


