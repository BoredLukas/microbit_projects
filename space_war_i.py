from microbit import *
import random

space_ship_x = 2
space_ship_x_ii = 0
asteroid_x = 0
asteroid_y = 0
asteroid_count = 0
first = 1
frame_time_ms_ii = 0
frame_time_single = 40
game_status = False
time = 400
score = 0
level = 1

def space_ship_move(space_ship_x, indicator):
    if indicator == 1:
        space_ship_x -= 1
        if space_ship_x < 0:
            space_ship_x = 4
    else:
        space_ship_x += 1
        if space_ship_x > 4:
            space_ship_x = 0
    return space_ship_x

def add_asteroid():
    pass

while True:
    if pin_logo.is_touched():
        game_status = True
    while game_status:

        # Spaceship

        display.set_pixel(space_ship_x, 4, 9)

        if button_a.get_presses():
            space_ship_x_ii = space_ship_x
            space_ship_x = space_ship_move(space_ship_x, 1)
            display.set_pixel(space_ship_x, 4, 9)
            display.set_pixel(space_ship_x_ii, 4, 0)

        if button_b.get_presses():
            space_ship_x_ii = space_ship_x
            space_ship_x = space_ship_move(space_ship_x, -1)
            display.set_pixel(space_ship_x, 4, 9)
            display.set_pixel(space_ship_x_ii, 4, 0)

        #Asteroids

        frame_time_ms = running_time()
        if frame_time_ms == 0:
            frame_time_ms = 1

        if frame_time_ms % time == 0:

            #asteroid_count += 1

            if not first == 1:
                asteroid_y += 1
                if asteroid_y == 5:
                    asteroid_y = 0
                    asteroid_x = random.randint(0, 4)
                    asteroid_count -= 1
                display.set_pixel(asteroid_x, asteroid_y, 3)
                display.set_pixel(asteroid_x, asteroid_y, 0)
                first = 0

        score = score + 1
        if score % 10 == 0:
            level = level + 1
            time = time - 20

        frame_time_ms_ii = running_time()
        if frame_time_ms_ii - frame_time_ms < frame_time_single:
            frame_time_rest = frame_time_ms_ii - frame_time_ms
            sleep(frame_time_rest)

        # Ende

        if space_ship_x == asteroid_x and asteroid_y == 4:
            display.clear()
            display.scroll("Game Over")
            level = 1
            time = 400
            score = 0
            game_status = False
