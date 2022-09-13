import random
import operator


GAME_TASK = 'What is the result of the expression?'


def game_task():
    number1 = random.randint(1, 30)
    number2 = random.randint(1, 30)
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    operator_symb = random.choice(list(operators))
    question = f"{number1} {operator_symb} {number2}"
    correct_answer = str(operators.get(operator_symb)(number1, number2))
    return question, correct_answer
