from math import gcd
import random


GAME_TASK = 'Find the greatest common divisor of given numbers.'


def game_task():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    question = f"{number1} {number2}"
    correct_answer = str(gcd(number1, number2))
    return question, correct_answer
