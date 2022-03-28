### IMPORT MODULE
import random
import os
import time
 
## GAME PARAMETERS
WIDTH = 8
HEIGHT = 16
Asteroids = []
timer = 0
frame_time = 40 #Time one frame is shown
fps = 50

### UTILITY FUNCTIONS
def clear():
## CLEARS CONSOLE
    if os.name == 'nt': os.system('cls') # Windows
    else: os.system('clear') # Unix

### MODEL FUNCTIONS
def add_random_asteroids(Asteroids, given_prob, WIDTH):
    for i in range(WIDTH):
        spawn_prob = random.randint(0, 100)
        if spawn_prob <= given_prob:
            asteroid_x = i
            Asteroids.append([asteroid_x, 0])
    return Asteroids

def move_and_remove_asteroids(Asteroids_list, HEIGHT):
    Asteroids_ii = []
    for asteroid in Asteroids_list:
        asteroid[1] += 1             ##Y Coordinate of Asteroid
        if asteroid[1] < HEIGHT:
            Asteroids_ii.append(asteroid)
    return Asteroids_ii

### VIEW FUNCTIONS
def display(Asteroids, HEIGHT, WIDTH):
    display = []
    for i in range(HEIGHT):
        display.append([])
        for b in range(WIDTH):
            display[i].append(' ')
    for asteroid_xy in Asteroids:
        display[asteroid_xy[1]][asteroid_xy[0]] = 'o'
    return display

### GAME LOOP
'''
##while True:
add_random_asteroids(Asteroids, 30, WIDTH)
print(Asteroids)
move_and_remove_asteroids(Asteroids)
print(Asteroids)
'''
while True:
    start_time = time.time()
    clear()
    Asteroids_d_show = add_random_asteroids(Asteroids, 30, WIDTH)
    Asteroids_d_show = move_and_remove_asteroids(Asteroids, HEIGHT)
    display_show = display(Asteroids_d_show, HEIGHT, WIDTH)
    for line in display_show:
        print(line)
        stop_time = time.time()
        if stop_time - start_time < frame_time:
            code_pause = frame_time - (stop_time - start_time)
            time.sleep(code_pause / 10000)
    ### UPDATE MODEL
    # here call model functions to update 
    
    ### UPDATE VIEW
    # here call view-functions
    