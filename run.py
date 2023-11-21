import random
from words import words


def random_word(words):
    word = random.choice(words)

    return word


def letters():
    word = random_word(words)
    get_letters = set(word)
    used_letters = set()

    while len(get_letters) > 0:
        print('letters that have been used: ', ''.join(used_letters))   
        word_list = [letter if letter in used_letters else '-' for letter in word] 
        print('current word: ', ''.join(word_list))
        user_input = input('Guess a letter: ')
        if user_input in used_letters:
            used_letters.add(user_input)
            if user_input in get_letters:
                get_letters.remove(user_input)
        elif user_input in used_letters:
            print('You have already used that letter. ')
        else:
            print('Invalid input, try again')


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
            print(letters())
            break
        else:
            print('You have to enter "r" or "s"')
            continue


intro_game()