print('welcome to the game of rock, paper and scissors!!!'.upper())
print()
# Getting the computers choice first which will return either 'Rock' 'Paper' or 'Scissors;
import random as rm
def get_computer_choice():
    random_number = rm.randint(1, 3)
    options = {1:'Paper', 2:'Rock', 3:'Scissors'}
    # selecting the computer's choice from the dictionary with the random numbers
    computer_choice = options[random_number]
    return computer_choice

# Taking the user input and return it.
def get_user_input():
    user_input = input('Enter your choice from either Rock, Paper or Scissors: ')
    # converting user input to the Title form e.g paper = Paper.
    user_input = user_input.title()
    return user_input

# determine and returns who wins or loose.
def get_result(user_choice, computer_choice):
    if computer_choice == user_choice:
        return 'draw'
    elif (user_choice == 'Scissors') and (computer_choice == 'Paper'):
        return 'win'
    elif (user_choice == 'Paper') and (computer_choice == 'Rock'):
        return 'win'
    elif (user_choice == 'Rock') and (computer_choice == 'Scissors'):
        return 'win'
    else:
        return 'lose'


play = 'y'
while play == 'y':
    computer_choice = get_computer_choice()
    # get input until user enters one of the options
    while True:
        user_choice = get_user_input()
        if user_choice in ['Paper', 'Rock', 'Scissors']:
            break
        else:
            print('Invalid!! please select a valid choice among Rock, Paper, and Scissors\n')
    result = get_result(user_choice, computer_choice)
        #printing result
    print(f'computer choice: {computer_choice}')
    print(f'Your choice: {user_choice}')
    if result == 'win':
        print('You win \nCongrats!!!\n'.upper())
    elif result == 'draw':
        print("It's a draw\nplay another round\n".upper())
    else:
        print('you lose. Try again\n'.upper())

    play = input('Would you like to play again? (if yes enter y) and (if no enter n): ')
    play = play.lower()
    print()