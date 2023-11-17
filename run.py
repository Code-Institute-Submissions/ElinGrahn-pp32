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

    choose = input(' ')
    if choose == "r":
        print('the rules')
    elif choose == "s":
        print(start_game())
    else:
        print('You have to enter "r" or "s"')


intro_game()
