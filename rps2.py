# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    # convert name to number using if/elif/else
    # don't forget to return the result!
    
    """
    converts the string name into a number between 0 and 4
    """
    
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Not a valid name!"

def number_to_name(number):
    # delete the following pass statement and fill in your code below
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    
    """
    converts a number in the range 0 to 4 into its corresponding name as a string
    """
    
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Not a valid number!"
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    # print a blank line to separate consecutive games
    
    print

    # print out the message for the player's choice
    
    print ("Player chooses", player_choice)

    # convert the player's choice to player_number using the function name_to_number()
    
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    
    import random
    comp_number = random.randrange(4)

    # convert comp_number to comp_choice using the function number_to_name()
    
    comp_name = number_to_name(comp_number)
    
    # print out the message for computer's choice
    
    print ("Computer chooses", comp_name)

    # compute difference of comp_number and player_number modulo five
    
    who_wins = (player_number - comp_number) % 5
    diff_selection = player_number - comp_number

    # use if/elif/else to determine winner, print winner message
    
    if diff_selection == 0 and who_wins == 0:
        print ("Player and computer tie!")
    elif diff_selection == 1 and who_wins == 1:
        print ("Player Wins!")
    elif diff_selection == 2 and who_wins == 2:
        print ("Player Wins!")
    elif diff_selection == 3 and who_wins == 3:
        print ("Computer Wins!")
    elif diff_selection == 4 and who_wins == 4:
        print ("Computer Wins!")
    elif diff_selection == -1 and who_wins == 4:
        print ("Computer Wins!")
    elif diff_selection == -2 and who_wins == 3:
        print ("Computer Wins!")
    elif diff_selection == -3 and who_wins == 2:
        print ("Player Wins!")
    elif diff_selection == -4 and who_wins == 1:
        print ("Player Wins!")

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("ock")
"""
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
"""
# always remember to check your completed program against the grading rubric
