import random
from words import words
import os

random_word = random.choice(words)


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    # stackoverflow


def start_game(incorrect):
    # Shaun Halverson
    """
    The different stages of the hangman until it is complete
    """
    if (incorrect == 6):
        print('\n +------')
        print('  |     |')
        print('  |')
        print('  |')
        print('  |')
        print('  |')
        print('======')
    elif (incorrect == 5):
        print('\n +------')
        print('  |     |')
        print('  |     o')
        print('  |')
        print('  |')
        print('  |')
        print('======')
    elif (incorrect == 4):
        print('\n +------')
        print('  |     |')
        print('  |     o')
        print('  |     |')
        print('  |')
        print('  |')
        print('======')
    elif (incorrect == 3):
        print('\n +------')
        print('  |     |')
        print('  |     o')
        print('  |    /|')
        print('  |')
        print('  |')
        print('======')
    elif (incorrect == 2):
        print('\n +------')
        print('  |     |')
        print('  |     o')
        print('  |    /|\\')
        print('  |')
        print('  |')
        print('======')
    elif (incorrect == 1):
        print('\n +------')
        print('  |     |')
        print('  |     o')
        print('  |    /|\\')
        print('  |    /')
        print('  |')
        print('======')
    elif (incorrect == 0):
        print('\n +------')
        print('  |     |')
        print('  |     o')
        print('  |    /|\\')
        print('  |    / \\')
        print('  |')
        print('======')
        print('\nYou lost :( the word was {}'.format(random_word))
        print('\nWould you like to restart the game? y/n')

        while True:
            """
            The player can choose to restart the game if they want to or not
            """
            restart = input('')
            if (restart == "y"):
                print(intro_game())
                break
            elif (restart == "n"):
                print('Okey bye!')
                break
            else:
                print('You have to press y or n')
                continue


def the_game():
    word_lenght = len(random_word)
    wrong_guesses = 6
    used_letters = []
    stop_game = False
    # Abdul Seyd
    display = ["_" for _ in range(word_lenght)]
    while not stop_game:
        print(display)
        current_guess = input('Guess a letter:\n')
        if current_guess not in random_word:
            # Shaun Halverson
            used_letters.append(current_guess)
            print('Letters used: {}'.format(used_letters))  # Show used letters
            wrong_guesses -= 1
            print(start_game(wrong_guesses))
            continue
        elif current_guess in random_word:
            used_letters.append(current_guess)
            for position in range(word_lenght):
                current_letter = random_word[position]
                if current_guess == current_letter:
                    print('Correct!')
                    display[position] = current_guess
                    continue
        else:
            print('Invalid input')
            continue
        if "_" not in display:
            print('Congrats! You got the word!')
            restart = input('Would you like to play again? Press y or n\n')
            if restart == "y":
                clear_terminal()
                print(intro_game())
                break
            elif (restart == "n"):
                print('Okey bye!')
                break
            else:
                print('You have to press y or n')
                continue


def intro_game():
    print('Welcome to hangman!')
    print('If you want to see the rules, press "r"')
    print('If you want to start the game, press "s"')

    while True:
        choose = input(' ')
        if (choose == "r"):
            print('In this game you will guess a word letter by letter')
            print('Each time you guess a new letter you will be able '
                  'to see which letters have been used and if you are correct')
            print('For each incorrect guess the hangman will become '
                  'more and more complete')
            print('Once the hangman is completed you have lost the game')
            print('Start new game press"s". Exit press "e"')
            continue
        elif (choose == "e"):
            print('okey...')
            intro_game()
            break
        elif (choose == "s"):
            clear_terminal()
            print(the_game())
            break
        else:
            print('You have to enter "r" or "s"')
            continue


intro_game()
