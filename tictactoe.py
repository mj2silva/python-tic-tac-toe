from Game import Game

welcome_message = '''
Welcome to mj2silva's Tic-Tac-Toe.

Please, select an option from the menu:

1. Play
2. About
3. Exit
'''

valid_options = [1, 2, 3]
not_valid_option_message = 'Not a valid option, please try again'


def print_error_message():
    print(not_valid_option_message)


def check_option(option, valid_options):
    try:
        int_option = int(option)
        return int_option in valid_options
    except:
        return False


def play_game():
    game = Game()
    game.start()


def show_info():
    info = '''
This is a game developed by mj2silva for learning purposes.
It was made with python3
You can find the source repo at https://github.com/mj2silva/python-tic-tac-toe
    '''
    print(info)
    char = input("Write B to go back or X to exit: ")
    if (char.upper() == 'B'):
        __main__()
    elif (char.upper() == 'X'):
        exit()


def show_main_menu():
    option_is_valid = False
    while (not option_is_valid):
        user_option_text = input('Write your option: ')
        option_is_valid = check_option(user_option_text, valid_options)
        if (not option_is_valid):
            print_error_message()
        else:
            option = int(user_option_text)
            if (option == 1):
                play_game()
            elif (option == 2):
                show_info()
            elif (option == 3):
                exit()


def __main__():
    print(welcome_message)
    show_main_menu()


__main__()
