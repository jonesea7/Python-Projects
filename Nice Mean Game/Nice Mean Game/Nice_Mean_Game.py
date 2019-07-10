#
# Python:   3.7
#
# Author:   Edmund Alyn Jones
#
# Purpose:  The Tech Academy - Python Course, Creating our first program together.
#           Demonstratin how to pass variables from function to function.
#           while producing a functional game.
#
#           Remember, myFunction(myVariable) means we add the variable.
#           Return variable implies we are calling the variable back to the invoked function.


def start(nice=0,mean=0,nice=""):
    #get user's name
    #this line establishes the var called name and sets it equal to the function describeGame
    name = describeGame(name)
    #here we have three variables set up in conjunction with the function called niceMean
    nice,mean,name = niceMean(nice,mean,name)

def describeGame(name):
    """
        Check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing agian and continue the game.
    """



 






if __name__ == "__main__":
    start()
