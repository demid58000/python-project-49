import random

rule = "What number is missing in the progression?"

def start_game():
    first_number = random.randint(2, 10)
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
    question = " ".join(map(str, lst_))
    return (question, str(right_answer))
      
      
    
      
      
    