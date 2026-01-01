import random

import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x,y,radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)


    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        asteroid_one_vector = pygame.Vector2(0,1)
        asteroid_two_vector = pygame.Vector2(0,1)

        rotated_asteroid_one =  asteroid_one_vector.rotate(random.uniform(20,50))
        rotated_asteroid_two = asteroid_two_vector.rotate(random.uniform(-20,-50))
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)


        asteroid_one.velocity = rotated_asteroid_one * (self.velocity.magnitude() * 1.2)
        asteroid_two.velocity = rotated_asteroid_two * (self.velocity.magnitude() * 1.2)




