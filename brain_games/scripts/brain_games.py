#!/usr/bin/zsh python
"""Main part of brain_games project."""
from brain_games.scripts.cli import welcome_user


def main():
    """Just main function."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
