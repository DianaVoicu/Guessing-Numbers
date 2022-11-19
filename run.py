"""
Module random to generate a number between 1 - 10.
Sys and time allows us to manipulate the runtime of the letters.
Pyfiglet give us a font art for the title.
Colorama module for writing coloured text.
"""
import random
import sys
import time
import pyfiglet
import colorama
from colorama import Fore

colorama.init(autoreset=True)


def print_slow(string):
    """
    Print slowly the text on terminal
    """
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.04)


def start():
    """
    Introduction into the game
    Explain the rules of the games
    """
    main_title = pyfiglet.figlet_format("Guess the Number", font="standard")
    print(Fore.YELLOW + f'{main_title}')
    user_name = input('Enter you name:\n')
    print_slow(f'Hello {user_name.capitalize()}! Nice to meet you!\n')
    print_slow('I am thinking about a number between 1 - 10...\n')
    print_slow('You have to guess the number within three attempts\n')


def compare_num():
    """
    Generate a random number between 1 - 10.
    Input number from the user.
    Run a while loop 3 times in which the number typed by user is
    compared with a random number.
    If the numbers are not equal if statements will print hints to the user.
    Another while loop runs until the value inserted by the user is valid.
    """
    guess_num = random.randint(1, 10)
    count = 0

    while count < 3:
        while True:
            user_num = input(Fore.BLUE + 'Enter your guess:\n')
            if validation_int(user_num):
                break

        if guess_num == int(user_num):
            print(Fore.YELLOW + f'Good guess!!! The number was {guess_num}\n')
            break
        elif guess_num > int(user_num):
            print(Fore.BLUE + f'Number {user_num} is too low...\n')
            count += 1
        elif guess_num < int(user_num):
            print(Fore.BLUE + f'Number {user_num} is too high...\n')
            count += 1

    if count == 3:
        print(Fore.MAGENTA + 'Sorry! Out of guesses!')
        print(Fore.MAGENTA + f'My number was {guess_num}\n')

    play_again()


def validation_int(value):
    """
    Validate the user's input.
    Inside the try the value is convereted in integers.
    Raises ValueError if the value can't be converted or if the value is
    smaller than 1 or higher than 10.
    """
    try:
        user_int = int(value)
        if user_int > 10 or user_int < 1:
            raise ValueError(
                f'Not {user_int}. Please enter a number between 1 - 10.'
             )
    except ValueError as e_error:
        print(Fore.RED + f'Invalid data: {e_error}. Try again!')
        return False

    return True


def play_again():
    """
    Repeat the game if the user would like to continue by pressing 'y'.
    Stop the game if the user presses the key 'n'.
    Raise a TypeError if other key than 'y' or 'n' is pressed.
    """
    choice = input('Do you wish to play again? Y / N\n')
    try:
        if choice.lower() == 'y':
            compare_num()
        elif choice.lower() == 'n':
            print_slow('Bye bye! Thank you for playing with me!\n')
            exit()
        raise TypeError(
            f'Not sure what you mean by {choice}...Type Y / N'
            )
    except TypeError as e_error:
        print(Fore.RED + f'Type error: {e_error}.')
        play_again()


def main():
    """
    Run main program functions
    """
    start()
    compare_num()


main()
