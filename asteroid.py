import pygame
import circleshape 
import random
from constants import *
from logger import log_event

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        rotation_1 = self.velocity.rotate(angle)
        rotation_2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid_1 = Asteroid(self.position.x, self.position.y,new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y,new_radius)
        new_asteroid_1.velocity = rotation_1 * 1.2
        new_asteroid_2.velocity = rotation_2 * 1.2


