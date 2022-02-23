from microbit import *
import random

a = 2
b = 0
c = 0
d = 0
i = 0
x = False
time = 400
count = 0
level = 1

while True:
    if pin_logo.is_touched():
        x = True
    while x:

        # Spaceship

        display.set_pixel(a, 4, 9)

        if button_a.get_presses():
            b = a
            a -= 1
            if a < 0:
                a = 4
            display.set_pixel(a, 4, 9)
            display.set_pixel(b, 4, 0)

        if button_b.get_presses():
            b = a
            a += 1
            if a > 4:
                a = 0
            display.set_pixel(a, 4, 9)
            display.set_pixel(b, 4, 0)

        # Asteroiden

        c = random.randint(0, 4)

        display.set_pixel(c, 0, 3)

        x = 0

        while x <= time:

            sleep(1)

            if button_a.get_presses():
                b = a
                a -= 1
                if a < 0:
                    a = 4
                display.set_pixel(a, 4, 9)
                display.set_pixel(b, 4, 0)

            if button_b.get_presses():
                b = a
                a += 1
                if a > 4:
                    a = 0
                display.set_pixel(a, 4, 9)
                display.set_pixel(b, 4, 0)

            x += 1

        for i in range(1, 5, 1):
            display.set_pixel(c, i, 3)
            d = i
            d -= 1
            display.set_pixel(c, i, 3)
            display.set_pixel(c, d, 0)

            x = 0

            while x <= time:

                sleep(1)

                if button_a.get_presses():
                    b = a
                    a -= 1
                    if a < 0:
                        a = 4
                    display.set_pixel(a, 4, 9)
                    display.set_pixel(b, 4, 0)

                if button_b.get_presses():
                    b = a
                    a += 1
                    if a > 4:
                        a = 0
                    display.set_pixel(a, 4, 9)
                    display.set_pixel(b, 4, 0)

                x += 1
        count = count + 1
        if count%10 == 0:
            level = level + 1
            time = time - 20

        display.set_pixel(c, 4, 0)

        # Ende

        if a == c and i == 4:
            display.clear()
            display.scroll("Game Over")
            level = 1
            time = 400
            count = 0
            x = False
