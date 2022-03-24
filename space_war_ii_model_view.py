### IMPORT MODULE
import random
import os
 
## GAME PARAMETERS
# State parameters of game such as WIDTH or HEIGHT of matrix.
# Use capital letters to indicate that this are parameter with fixed values instead of variables!
WIDTH = 8
Asteroids = []
frame = 40 #Time one frame is shown
fps = 50

### UTILITY FUNCTIONS
# utility functions that are of general use, e.g. to manipulate strings
def clear():
## CLEARS CONSOLE
## NOTE that there are different commands for Windows and Unix-based system (Mac and Linux)
    if os.name == 'nt': os.system('cls') # Windows
    else: os.system('clear') # Unix

### MODEL FUNCTIONS
# here write all functions that belong to the game's model/logic
def add_random_asteroids(L, probability, WIDTH):
    for i in range(WIDTH):
        rate = random.randint(0, 100)
        if rate <= probability:
            asteroid_x = i
            L.append([asteroid_x, 0])
    return L

def move_and_delete_asteroids(L):
    pass


### VIEW FUNCTIONS
# Here write all functions that belong to the game's view.
# When porting you game from e.g. normal python (console app) to mirco:bit, only these functions have to be adapted/rewritten

### GAME LOOP

##while True:
add_random_asteroids(Asteroids, 10, WIDTH)
print(Asteroids)
##print(Asteroids[1])
    ### UPDATE MODEL
    # here call model functions to update 
    
    ### UPDATE VIEW
    # here call view-functions
    