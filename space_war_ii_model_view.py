### IMPORT MODULE
import random
 
## GAME PARAMETERS
# State parameters of game such as WIDTH or HEIGHT of matrix.
# Use capital letters to indicate that this are parameter with fixed values instead of variables!


### UTILITY FUNCTIONS
# utility functions that are of general use, e.g. to manipulate strings


### MODEL FUNCTIONS
# here write all functions that belong to the game's model/logic


### VIEW FUNCTIONS
# Here write all functions that belong to the game's view.
# When porting you game from e.g. normal python (console app) to mirco:bit, only these functions have to be adapted/rewritten




def add_random_asteroids(L):
    asteroid_x = random.randint(-1, 5)
    L.append([asteroid_x, 0])
    return L

def move_and_delete_asteroids(L):
    pass

Asteroids = []
frame = 40 #Time one frame is shown
fps = 50

### GAME LOOP

##while True:
add_random_asteroids(Asteroids)
add_random_asteroids(Asteroids)
print(Asteroids)
print(Asteroids[1])
    ### UPDATE MODEL
    # here call model functions to update 
    
    ### UPDATE VIEW
    # here call view-functions
    