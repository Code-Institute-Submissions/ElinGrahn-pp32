import random
from words import words


def random_word(words):
    word = random.choice(words)

    return word


def start_game():
    print(' +----')
    print(' |   |')
    print(' |')
    print(' |')
    print(' |')
    print('===')


def intro_game():
    print('Welcome to hangman!')
    print('If you want to see the rules, press "r"')
    print('If you want to start the game, press "s"')

    while True:
        choose = input(' ')
        if choose == "r":
            print('the rules')
            print('Start new game press"s". Exit press "e"')
            continue
        elif choose == "e":
            print('okey...')
            intro_game()
            break
        elif choose == "s":
            print(start_game())
            break
        else:
            print('You have to enter "r" or "s"')
            continue


intro_game()
