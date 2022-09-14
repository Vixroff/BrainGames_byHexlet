import random


GAME_TASK = 'What number is missing in the progression?'


def game_task():
    start_digit = random.randint(1, 20)
    count_digits = random.randint(5, 10)
    digits = [start_digit * i for i in range(1, count_digits + 1)]
    missed_index = random.randint(0, len(digits) - 1)
    correct_answer = str(digits[missed_index])
    digits[missed_index] = '..'
    question = ' '.join(str(digit) for digit in digits)
    return question, correct_answer


if __name__ == '__main__':
    game_task()
