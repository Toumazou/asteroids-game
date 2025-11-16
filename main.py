# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
pygame.init()
from constants import *
from logger import log_state
from player import Player

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock() # initialize the clock before the main loop, usually after creating the display surface
dt = 0

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    running = True
    while running:
        #1. Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #2. Update
        dt = clock.tick(60) / 1000
        player.update(dt)

        #3. Draw
        screen.fill((0,0,0))
        player.draw(screen)

        #4. Flip
        pygame.display.flip()
        log_state()

# Below line ensures the main() function is only called when this file is run directly; it won't run if it's imported as a module. It's considered the "pythonic" way to structure an executable program in Python. Technically, the program will work fine by just calling main(), but you might get an angry letter from Guido van Rossum if you don't.
if __name__ == "__main__":
    main()
