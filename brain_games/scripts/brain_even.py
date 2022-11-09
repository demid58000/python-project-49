import random
#from brain_games.cli import name




def is_even():
  #name = welcome_user()
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
        return'Wrong answer'
        break
      elif random_number % 2 != 0 and answer == 'no':
        print('Correct!')
        right_answers += 1
      elif random_number % 2 != 0 and answer == 'yes':
        return 'Wrong answer'
        break
      if right_answers == 3:  
        return f'Congratulations, name!'
def main():
    pass


if __name__ == "__main__":
    main()

print(is_even())


