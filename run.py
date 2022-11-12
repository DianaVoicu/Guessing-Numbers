import random


def start():
    """
    Introduction into the game
    Explain the rules of the games
    """
    print('Guess the Number')
    name = input('Enter you name:\n')
    print(f'Hello {name}! Nice to meet you!\n')
    print('I am thinking about a number between 1-10 ...')
    print('You have to guess the number within three tries')



def compare_num():
    """
    Generate a random number between 1-10.
    Run a while loop for 3 times in which the number typed by user is
    compared with a random number.
    If the numbers are not equal if statements will print hints to the user. 
    Another while loop runns until the value inserted by the user is valid, it has to be 
    a number between 1-10.
    
    """
    guess_num = random.randint(1,10)
    count = 0

    while count < 3 :
        while True:
            user_num = input('Type your guess:\n')
            if validation_int(user_num):
                break
        if guess_num == int(user_num):
            break   
        elif guess_num > int(user_num):
            print(f'...Number {user_num} is too low')
            count += 1  
        elif guess_num < int(user_num):
            print(f'...Number {user_num} is too high')
            count += 1

    if count == 3:
        print(f'Sorry! Out of guesses! My number was {guess_num}')
    elif guess_num == int(user_num):
        print(f'Good guess!!! The number was {guess_num}')
  
    
def validation_int(value):
    """
    Validate the user's input.
    Inside the try the value is convereted in integers.
    Raises ValueError if the value can't be converted or if the value is 
    smaller than 1 and higher than 10. 
    
    """
    try:
        user_int = int(value)
        if user_int > 10 or user_int <= 1:
            raise ValueError (
                f'Please enter a number between 1-10'
            )
    except ValueError as e:
        print(f'Invalid data: {e}. Try again!')
        return False

    return True
    


def main():
    start()
    compare_num()
main()