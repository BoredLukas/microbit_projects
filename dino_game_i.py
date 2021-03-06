from microbit import *
import random

status = "RUNNING"
time = 800
cactus_x_i = 4
bat_x_i = 4
dino_i = 3
dino_ii = 2
jump_time = 0
cactus_or_bat = 0
bat_i_or_bat_ii = 0

while True:

    #Dino

    #Jump
    if button_a.get_presses():
        jump_time = running_time()
        display.set_pixel(0, 2, 9)
        display.set_pixel(0, 4, 0)
        dino_i = 2
        dino_ii = 3

        #Jump_time_Start
        status = "JUMP"

    #Crouch
    elif button_b.is_pressed():
        display.set_pixel(0, 3, 0)
        display.set_pixel(0, 4, 9)
        dino_i = 4
        dino_ii = 4
        status = "CROUCH"

    if status == "CROUCH" and not button_b.is_pressed():
        status = "RUNNING"

    #Run
    if status == "RUNNING":
        display.set_pixel(0, 3, 9)
        display.set_pixel(0, 4, 9)
        dino_i = 3
        dino_ii = 4

    #Jump_time_Stop
    if status == "JUMP" and jump_time + time * 1.5 == running_time():
        status = "RUNNING"
        display.set_pixel(0, 2, 0)

    #Cactus and Bats

    if cactus_or_bat == 0:
        #Cactus
        if running_time() % time == 0:
            display.set_pixel(cactus_x_i, 4, 5)
            if cactus_x_i < 4:
                display.set_pixel(cactus_x_i+1, 4, 0)
            cactus_x_i -= 1
        if cactus_x_i == -1:
            cactus_x_i = 4
            cactus_or_bat = random.randint(-1, 2)
    else:
        #Bat
        if running_time() % time == 0:
            display.set_pixel(bat_x_i, 3, 5)
            if bat_x_i < 4:
                display.set_pixel(bat_x_i+1, 3, 0)
            bat_x_i -= 1
        if bat_x_i == -1:
            bat_x_i = 4
            cactus_or_bat = random.randint(-1, 2)

    #Easy-Time
    if running_time() < 20000:
        cactus_or_bat = 0
    else:
        cactus_or_bat = random.randint(-1, 2)

    """
    #Getting harder
    if running_time()

    #Game Over
    if cactus_x_i == dino_i or cactus_x_i == dino_ii or bat_x_i == dino_i or bat_x_i == dino_ii:
        display.scroll("Game Over")
        display.clear()
    """
    sleep(1)
#BACKUP
