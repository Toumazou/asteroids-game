# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, sys
pygame.init()
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock() # initialize the clock before the main loop, usually after creating the display surface
dt = 0

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    running = True
    while running:

        #1. Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #2. Update
        dt = clock.tick(60) / 1000 # seconds passed used to smooth movement
        updatable.update(dt)
        for item in asteroids:
            if item.collide_with(player) == True:
                log_event("player_hit")
                print("Game over !")
                sys.exit()
            for shot in shots:
                if shot.collide_with(item) == True:
                    log_event("asteroid_shot")
                    shot.kill()
                    item.split()

        #3. Draw in an invinsible surfact (the black buffer)
        screen.fill((0,0,0))
        for item in drawable:
            item.draw(screen)

        #4. Flip to swap the black buffer with the visible window (front buffer)
        pygame.display.flip()
        log_state()

# Below line ensures the main() function is only called when this file is run directly; it won't run if it's imported as a module. It's considered the "pythonic" way to structure an executable program in Python. Technically, the program will work fine by just calling main(), but you might get an angry letter from Guido van Rossum if you don't.
if __name__ == "__main__":
    main()
