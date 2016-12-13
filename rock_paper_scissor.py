import random

"""
this function is used to convert computer generated
random num to name for comparison
"""
def numtoname(num):
    if num == 0:
        return 'Rock'
    elif num == 1:
        return 'Paper'
    elif num == 2:
        return 'Scissors'

"""
this function converts the outcome of comparison back
to user understandable name
"""
def nametonum(name):
    if name == 'Rock':
        return 0
    elif name == 'Paper':
        return 1
    elif name == 'Scissors':
        return 2

"""
this function does comp selection as player 2
"""
def compinp():        
    play2num = random.randint(0, 2)
    play2 = numtoname(play2num)
    print ('Computer selects: ', play2)
    return play2

"""
this function takes player inp
"""
def playinp():
    play1 = input('Player 1 selects: ')
    trial = tries(play1)
    count = 0

    while ((trial is False) and (count < 2)):
        play1 = input('Player 1 selects: ')
        trial = tries(play1)
        count += 1
        
    if trial is False:
        print('You tried too many times!')
        return None
    else:
        return play1

"""
a new game is always started by this function
This is the main function
"""
def new_game():
    playnew = 'Y'
    while playnew is 'Y':
        play1 = playinp()
        if play1 is not None:
            play2 = compinp()
            rps(play1, play2)
        playnew = input('Do you want to play another game? (Y/N): ')

    print('Thanks for playing!')

'''
this function checks for user input
'''
def tries(play1):
    if (play1 != "Rock") and (play1 != "Paper") and (play1 != "Scissors"):
        print('Please select a proper input. Try again!')
        return False
    else:
        return True

'''
this function is the brain of the code, that computes the outcome
after user and comp selection
'''
def rps(play1, play2):
    play1 = nametonum(play1)
    play2 = nametonum(play2)

    if (play1 - play2) == -2:
        print('Player 1 wins!')
    elif (play1 - play2) == -1:
        print('Computer wins!')
    elif (play1 - play2) == 0:
        print('Its a tie!')
    elif (play1 - play2) == 1:
        print('Player 1 wins!')
    elif (play1 - play2) == 2:
        print('Computer wins!')


new_game()
