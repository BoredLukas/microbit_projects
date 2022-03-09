from microbit import *
import random

y = 0
time = 500
a = 0

while True:

    #Dino
    #Sprung
    if button_a.get_presses():
        display.set_pixel(0, 2, 9)
        display.set_pixel(0, 3, 9)
        display.set_pixel(0, 4, 0)
        sleep(time)
        display.set_pixel(0, 2, 0)
    #Ducken
    if button_b.is_pressed():
        display.set_pixel(0, 3, 0)
        display.set_pixel(0, 4, 9)
    #Laufen
    else:
        display.set_pixel(0, 3, 9)
        display.set_pixel(0, 4, 9)

    #Kaktus
    display.set_pixel(4, 4, 5)

    #sleep
    while a <= time:
        #Dino
        #Sprung
        if button_a.get_presses():
            display.set_pixel(0, 2, 9)
            display.set_pixel(0, 3, 9)
            display.set_pixel(0, 4, 0)
            sleep(time)
            display.set_pixel(0, 2, 0)
            a += 1
            sleep(1)
        #Ducken
        if button_b.is_pressed():
            display.set_pixel(0, 3, 0)
            display.set_pixel(0, 4, 9)
            a += 1
            sleep(1)
        #Laufen
        else:
            display.set_pixel(0, 3, 9)
            display.set_pixel(0, 4, 9)
            a += 1
            sleep(1)
    a = 0

    display.set_pixel(4, 4, 0)
    for i in range(3, -1, -1):
        display.set_pixel(i, 4, 5)
        display.set_pixel(i + 1, 4, 0)

        #sleep
        while a <= time:
            #Dino
            #Sprung
            if button_a.get_presses():
                display.set_pixel(0, 2, 9)
                display.set_pixel(0, 3, 9)
                display.set_pixel(0, 4, 0)
                sleep(time)
                display.set_pixel(0, 2, 0)
                a += 1
                sleep(1)

            #Ducken
            if button_b.is_pressed():
                display.set_pixel(0, 3, 0)
                display.set_pixel(0, 4, 9)
                a += 1
                sleep(1)

            #Laufen
            else:
                display.set_pixel(0, 3, 9)
                display.set_pixel(0, 4, 9)
                a += 1
                sleep(1)
        a = 0
    display.set_pixel(0, 4, 0)

