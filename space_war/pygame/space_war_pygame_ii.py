import pygame
import random
import sys
import os
pygame.font.init()

#OOP
class Asteroid:
    def __init__(self,_x):
        self.x = _x
        self.y = 0

    def move(self):
        self.y += 1

class Spaceship:
    def __init__(self,_x,_y):
        self.x = _x
        self.y = _y

    def move(self, dir):
            if dir == "left":
                self.x -= 1
            elif dir == "right":
                self.x += 1

class Bullet:
    def __init__(self,_x,_y):
        self.x = _x
        self.y = _y

### GAME PARAMETERS
WIDTH = 13
HEIGHT = 20

probability = 20
FPS = 60
game_font = pygame.font.SysFont("arial", 40)
level = 1
game_status = True
asteroids = [Asteroid(7)]
player = Spaceship(6, 19)

# PyGame constants
SIZE = 30
LINE_WIDTH = 1
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)

### PYGAME SETUP
# initialize, create screen and clock
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH*(SIZE+LINE_WIDTH)+LINE_WIDTH,HEIGHT*(SIZE+LINE_WIDTH)+LINE_WIDTH))
SCREEN.fill(WHITE)
pygame.display.set_caption("Spacewar Game")
clock = pygame.time.Clock()

# create squares for grid
squares = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]
for y in range(HEIGHT):
    for x in range(WIDTH):
        squares[y][x] = pygame.Rect(x * (SIZE+LINE_WIDTH)+LINE_WIDTH, y * (SIZE+LINE_WIDTH)+LINE_WIDTH, SIZE, SIZE)

### IMAGES

ASTEROID = pygame.transform.rotate(pygame.image.load(os.path.join('data','asteroid.png')),90)
ASTEROID = pygame.transform.scale(ASTEROID,(SIZE,SIZE))

SPACESHIP = pygame.transform.scale(pygame.image.load(os.path.join('data','battleship.png')),(SIZE,SIZE))

ROCKET = pygame.transform.scale(pygame.image.load(os.path.join('data','bullet.png')),(SIZE,SIZE))

BACKGROUND = pygame.image.load(os.path.join('data','universe.jpg'))

def update_asteroids():
    for Asteroid in asteroids:
        Asteroid.x -= 1

def game_over(game_status):
    pass

while game_status:
    ### KEY EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Exit app when clicking quit button
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN: # Deal with keyboard input
            if event.key == pygame.K_LEFT:
                player.move("left")
            if event.key == pygame.K_RIGHT:
                player.move("right")

    ### SPAWNING ASTEROIDS
    #pass

    ### DRAW SQUARES
    # go through all squares and color them correctly
    for x in range(WIDTH):
        for y in range(HEIGHT):
            rect = squares[y][x]
            pygame.draw.rect(SCREEN, BLACK, rect)

    for Asteroids in asteroids:
        asteroid_rect = ASTEROID.get_rect(topleft = (Asteroids.x*(SIZE+LINE_WIDTH), Asteroids.y*(SIZE+LINE_WIDTH)))
        SCREEN.blit(ASTEROID,asteroid_rect)

    spaceship_rect = SPACESHIP.get_rect(topleft = (player.x*(SIZE+LINE_WIDTH), player.y*(SIZE+LINE_WIDTH)))
    SCREEN.blit(SPACESHIP,spaceship_rect)

    #Labels
    level_label = game_font.render(f"Level: {level}", 1, (255,255,255))
    SCREEN.blit(level_label, (7,0))

    # update screen (i.e. draw to screen)
    pygame.display.update()
    clock.tick(FPS) # sleep, 60 means time is chosen s.t. 60fps (frames per second)
