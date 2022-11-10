import random


def start():
    """
    Introduction into the game
    Explain the rules of the games
    """
    print('Guess the Number')
    name = input('Enter you name:\n')
    print(f'Hello {name}! Nice to meet you!\n')
    print('I am thinking about a number between 1-10...')
    print(f'You have to guess the number within three tries')

# Generating a random integer between 1-10
guess_num = random.randint(1,10)

def input_num():
    """
    Comparing the user's number with the random one
    Count three tries for the user to insert the correct number
    """
    
    count = 0
    while count < 3 :
        user_num = input('Type your guess:\n')
        if guess_num == int(user_num):
            print(f'Good guess!!! The number was {guess_num}')
            count += 1    
        elif guess_num > int(user_num):
            print(f'...Number {user_num} is too low')
            count += 1  
        elif guess_num < int(user_num):
            print(f'...Number {user_num} is too high')
            count += 1
    if count == 3:
        print(f'Sorry! Out of guesses! My numer was {guess_num}')



# def validation_num():
#     try:
#         num = int('user_num')
#         if num > 10:
#             raise ValueError
#     except ValueError:
#         print('Please enter a number between 1-10') 
    


def main():
    start()
    input_num()
main()