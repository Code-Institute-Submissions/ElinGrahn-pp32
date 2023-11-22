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
            elif (restart == n):
                print('Okey bye!')
            else:
                print('You have to press y or n')


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