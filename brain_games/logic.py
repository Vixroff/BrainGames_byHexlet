import prompt
from brain_games.cli import welcome_user


def play_round(question, correct_answer):
    print(f"Question: {question}")
    answer = prompt.string('Your answer: ')
    if correct_answer == answer:
        print('Correct!')
        return True
    else:
        print(f"{answer} is wrong answer ;(. \
Correct answer was {correct_answer}")
        return False


def play_game(game):
    name = welcome_user()
    print(game.GAME_TASK)
    count = 0
    while count != 3:
        question, correct_answer = game.game_task()
        if play_round(question, correct_answer):
            count += 1
        else:
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
