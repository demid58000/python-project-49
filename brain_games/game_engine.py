from brain_games.cli import answer, welcome_user

max_points = 3


def game_run(game):
    player_name = welcome_user(game.rule)
    

    start_score = 0

    while start_score < max_points:
        question, right_answer = game.start_game()
        your_answer = answer(question)
        if your_answer != right_answer:
            print(f'{your_answer} is wrong answer')
            print(f'correct answer was {right_answer}')
            print(f"Let's try again, {player_name}!")
            return
        elif your_answer == right_answer:
            print('Correct!')
            start_score += 1
    print(f'Congratulation, {player_name}')




