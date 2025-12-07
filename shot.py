import pygame
import circleshape 
from constants import *

class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

