from microbit import*
from datetime import datetime

compass.calibrate()

steps = 0
mode = 1

now = datetime.now()

h = now.hour

def on_forever():
    degrees = input.compass_heading()
    if degrees < 45:
        microbit.Image.ARROW_N
    elif degrees < 135:
        microbit.Image.ARROW_E
    elif degrees < 225:
        microbit.Image.ARROW_S
    elif degrees < 315:
        microbit.Image.ARROW_W
    else:
        microbit.scroll("You're lost")

"""
while True:
    if accelerometer.was_gesture('shake'):
        steps += 1
    if button_a.is_pressed():
        display.scroll(steps)
"""

on_forever()

while True:
    if pin_logo.is_touched:
        mode += 1
        if mode > 3:
            mode = 0
    if accelerometer.was_gesture('shake'):
        steps += 1
    if mode == 1:
        if h == 1:
            microbit.display.set_pixel(2,2,9)
            microbit.display.set_pixel(3,1,9)
            microbit.display.set_pixel(3,0,9)
        if h == 2:
            microbit.display.set_pixel(2,2,9)
            microbit.display.set_pixel(3,1,9)
            microbit.display.set_pixel(4,1,9)
        if h == 3:
            microbit.display.set_pixel(2,2,9)
            microbit.display.set_pixel(3,2,9)
            microbit.display.set_pixel(4,2,9)
        if h == 4:
            microbit.display.set_pixel(2,2,9)
            microbit.display.set_pixel(3,3,9)
            microbit.display.set_pixel(4,3,9)
        if h == 5:
            microbit.display.set_pixel(2,2,9)
            microbit.display.set_pixel(3,3,9)
            microbit.display.set_pixel(3,4,9)
        if h == 6:
            microbit.display.set_pixel(2,2,9)
            microbit.display.set_pixel(2,3,9)
            microbit.display.set_pixel(2,4,9)
        if h == 7:
            microbit.display.set_pixel(2,2,9)
            microbit.display.set_pixel(1,3,9)
            microbit.display.set_pixel(1,4,9)
        if h == 8:
            microbit.display.set_pixel(2,2,9)
            microbit.display.set_pixel(1,3,9)
            microbit.display.set_pixel(0,3,9)
        if h == 9:
            microbit.display.set_pixel(2,2,9)
            microbit.display.set_pixel(1,2,9)
            microbit.display.set_pixel(0,2,9)
        if h == 10:
            microbit.display.set_pixel(2,2,9)
            microbit.display.set_pixel(1,1,9)
            microbit.display.set_pixel(0,1,9)
        if h == 11:
            microbit.display.set_pixel(2,2,9)
            microbit.display.set_pixel(1,1,9)
            microbit.display.set_pixel(1,1,9)
        if h == 12:
            microbit.display.set_pixel(2,2,9)
            microbit.display.set_pixel(2,1,9)
            microbit.display.set_pixel(2,0,9)
    elif mode == 2:
        display.scroll(steps, loop = True)
    else:
        on_forever()
