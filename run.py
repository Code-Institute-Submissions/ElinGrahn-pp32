import random
from words import words

random_word = random.choice(words)

for x in random_word:
    print('_', end='')


def start_game(incorrect):
    if(incorrect == 0):
        print('\n+------')
        print('  |     |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('======')
    elif(incorrect == 1):
        print('\n+------')
        print('  |     |')
        print('  |     o')
        print('  |')
        print('  |')
        print('  |')
        print('======')
    elif(incorrect == 2):
        print('\n+------')
        print('  |     |')
        print('  |     o')
        print('  |     |')
        print('  |')
        print('  |')
        print('======')
    elif(incorrect == 3):
        print('\n+------')
        print('  |     |')
        print('  |     o')
        print('  |    /|')
        print('  |')
        print('  |')
        print('======')
    elif(incorrect == 4):
        print('\n+------')
        print('  |     |')
        print('  |     o')
        print('  |    /|\\')
        print('  |')
        print('  |')
        print('======')
    elif(incorrect == 5):
        print('\n+------')
        print('  |     |')
        print('  |     o')
        print('  |    /|\\')
        print('  |    /')
        print('  |')
        print('======')
    elif(incorrect == 6):
        print('\n+------')
        print('  |     |')
        print('  |     o')
        print('  |    /|\\')
        print('  |    / \\')
        print('  |')
        print('======')
        print('\nWould you like to restart the game? y/n')

        while True:
            restart = input('')
            if (restart == y):
                print(intro_game())
                break
            elif (restart == n):
                print('Okey bye!')
                break
            else:
                print('You have to press y or n')
                continue


def guess_letters(guessed_letters):
    counter = 0
    right_guess = 0

    for char in random_word:
        if(char in guessed_letters):
            print(random_word[counter], end=' ')
            right_guess += 1
        else:
            print(' ', end=' ')
        counter += 1
        return right_guess

def printLines():
    print('\r')
    for char in random_word:
        print('\u203E', end=' ')
    

word_lenght = len(random_word)
wrong_guesses = 0
used_letters = []
correct_guesses = 0


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
            print(letters())
            break
        else:
            print('You have to enter "r" or "s"')
            continue


intro_game()