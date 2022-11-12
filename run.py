import random
import sys, time


def print_slow(string):
    """
    Print slowly the text on terminal
    """
    for letter in string:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


def start():
    """
    Introduction into the game
    Explain the rules of the games
    """
    print_slow('Guess the Number Game!\n')
    name = input('Enter you name:\n')
    print_slow(f'Hello {name.capitalize()}! Nice to meet you!\n')
    print_slow('I am thinking about a number between 1-10 ...')
    print_slow('You have to guess the number within three attempts\n')


def compare_num():
    """
    Generate a random number between 1-10.
    Run a while loop 3 times in which the number typed by user is
    compared with a random number.
    If the numbers are not equal if statements will print hints to the user. 
    Another while loop runs until the value inserted by the user is valid.
    """
    guess_num = random.randint(1, 10)
    count = 0

    while count < 3:
        while True:
            user_num = input('Type your guess:\n')
            if validation_int(user_num):
                break

        if guess_num == int(user_num):
            break   
        elif guess_num > int(user_num):
            print(f'...Number {user_num} is too low\n')
            count += 1  
        elif guess_num < int(user_num):
            print(f'...Number {user_num} is too high\n')
            count += 1

    if count == 3:
        print(f'Sorry! Out of guesses! My number was {guess_num}\n')
    elif guess_num == int(user_num):
        print_slow(f'Good guess!!! The number was {guess_num}\n')

    play_again()
  
    
def validation_int(value):
    """
    Validate the user's input.
    Inside the try the value is convereted in integers.
    Raises ValueError if the value can't be converted or if the value is 
    smaller than 1 and higher than 10. 
    """
    try:
        user_int = int(value)
        if user_int > 10 or user_int < 1:
            raise ValueError(
                f'Please enter a number between 1-10'
            )
    except ValueError as e:
        print(f'Invalid data: {e}. Try again!')
        return False

    return True
    

def play_again():
    """
    Repeat the game if the user would like to continue by pressing 'y'.
    Stop the game if the user presses the key 'n'.
    Raise a TypeError if other key than 'y' or 'n' is pressed.
    """
    choice = input('Do you wish to play again? Y/N\n')
    try:
        if choice.lower() == 'y':
            compare_num()
        elif choice.lower() == 'n':
            print_slow('Bye bye! Thank you for playing with me!\n')
            exit()
        raise TypeError(
            print(f'Not sure what you mean by {choice}...Type Y / N')
        )
    except TypeError:
        play_again()


def main():
    """
    Run main program functions
    """
    start()
    compare_num()


main()