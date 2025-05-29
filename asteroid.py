import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)
        vec1 = self.velocity.rotate(angle)
        vec2 = self.velocity.rotate(-angle)
        new_size = self.radius - ASTEROID_MIN_RADIUS
        new_asteroid1 = Asteroid(self.position[0], self.position[1], new_size)
        new_asteroid2 = Asteroid(self.position[0], self.position[1], new_size)
        new_asteroid1.velocity = vec1 * 1.2
        new_asteroid2.velocity = vec2 * 1.2

            

    def update(self, dt):
        self.position += self.velocity * dt