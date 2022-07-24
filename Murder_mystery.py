# A program called Mystery murder
# It randomly picks a choice
# And then runs the code to find the actual murderer
# Based on the the suspect, weapon and location
import random

def computer_pick():
    """A function that gets the computer choices randomly"""
    room = ['ballroom', 'billiards room', 'gallery', 'dinning room']
    computer_choice = random.choice(room)
    return computer_choice


def names():
    """Randomly choose a suspect"""
    names = ['Mr. Kalehoff', 'Mrs, Sparr', 'Mr. Van Cleve', 'Mr. Parkes']
    suspect = random.choice(names)
    return suspect


def user_input():
    weapon = input('Pls choose the weapon that was used in the murder case from (poison, pool stick, trophy, knife): ')
    weapon = weapon.lower()
    return weapon


def solve_murder_case(room, weapon, suspect):
    if (room == "ballroom") and (suspect == 'Mr. Kalehoff') and (weapon == "poison"):
        solved = True
        return solved
    elif (room == "billiards room") and (suspect == 'Mrs. Sparr') and (weapon == "pool stick"):
        solved = True
        return solved
    elif (room == "gallery") and (suspect == 'Mr. Van Cleve') and (weapon == "trophy"):
        solved = True
        return solved
    elif (room == "dinning room") and (suspect == 'Mr. Parkes') and (weapon == "knife"):
        solved = True
        return solved
    else:
        solved = False
        return solved

play = 'y'
# Loops through the functions so it runs over and over again at a controlled rate.

while play == 'y':
   # Make sure the user inputs the expected value
    while True:
        weapon = user_input()
        if weapon in ['poison', 'pool stick', 'trophy', 'knife']:
            break
        else:
            print("Not among the weapons in sight, pls choose from the options!")
    
    # Calling and assigning the functions    
    room = computer_pick()
    suspect = names()
    outcome = solve_murder_case(computer_pick, user_input, suspect)
    message = suspect + " did it in the " + room + " with the " + weapon +"!"


    print(f"The murder took place in the {room}")
    print(f'The suspect of the murder case is {suspect}')
    print(f'The weapon you chose was {weapon}')

    if outcome:
        print(message, '\n')
    else:
        print('Sorry the weapon you chose is inconsistent with the suspect and room.\nThe case is not solved yet, It\'s a mystery!\n')
    play = input('Would you like to continue? (y for yes and n for no): ')
    play = play.lower()
