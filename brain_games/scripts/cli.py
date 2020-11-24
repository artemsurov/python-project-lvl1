"""Module for cli command."""
import prompt


def welcome_user():
    """Acquaint functon."""
    name = prompt.string('May I have your name? ')
    print('Hello, {name}!'.format(name=name))
