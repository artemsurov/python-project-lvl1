#!/usr/bin/zsh python
"""Main part of brain_even project."""
from random import SystemRandom

from brain_games.scripts import brain_games

CONDITION_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'
WRONG_TEXT = """'{wrong_answer}' is wrong answer ;(.
             Correct answer was '{correct_answer}'"""


def check_right_answer(guessed_number: int):
    if guessed_number % 2 == 0:
        return 'yes'
    return 'no'


def check(user_answer: str, guessed_number):
    if user_answer not in ('no', 'yes'):  # noqa: WPS510
        return False, CONDITION_TEXT

    right_answer = check_right_answer(guessed_number)
    if user_answer == right_answer:
        return True, 'Correct!'

    return False, WRONG_TEXT.format(
        wrong_answer=user_answer,
        correct_answer=right_answer,
    )


def get_final_text(answer):
    if answer:
        final_text = 'Congratulations, {name}!'
    else:
        final_text = "Let's try again, {name}!"
    return final_text


def play_game():  # noqa: WPS210
    is_answer_correct = False
    accepted_answer_counter = 0
    cryptogen = SystemRandom()

    while accepted_answer_counter < 3:
        number = cryptogen.randrange(100)
        print('Question: {number}'.format(number=number))
        answer = input('Your answer: ')
        is_answer_correct, message = check(answer, number)
        print(message)
        if not is_answer_correct:
            break
        accepted_answer_counter += 1
    return is_answer_correct


def main():
    name = brain_games.welcome_user()
    print(CONDITION_TEXT)
    is_answer_correct = play_game()
    final_text = get_final_text(is_answer_correct)
    print(final_text.format(name=name))


if __name__ == '__main__':
    main()
