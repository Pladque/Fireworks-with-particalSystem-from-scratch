from random import randint
import pygame
class Particle:
    def __init__(self, speed, ttl, size):
        self.speed_x = speed[0]
        self.speed_y = speed[1]
        self.ttl = ttl
        self.size = size
        self.velocity_x = randint(-20,20) / 1000
        self.velocity_y = randint(-20,20) / 1000

class  Firework:

    def __init__(self, particles, position, delay = 0):
        self.shapes = [particles]
        self.delay = delay
        self.position_x = position[0]
        self.position_y = position[1]

        for shape in self.shapes:
                rem = []
                for particle in shape:
                    particle.position_x = self.position_x
                    particle.position_y = self.position_y 


    def blowup(self, screen):
        if self.delay <= 0:
            for shape in self.shapes:
                rem = []
                for particle in shape:
                    particle.position_x += particle.speed_x
                    particle.position_y += particle.speed_y
                    particle.ttl -= 0.1
                    particle.speed_x += particle.velocity_x
                    particle.speed_y += particle.velocity_y
                    particle.ttl -= 0.1
                    pygame.draw.circle(screen, (255, 255, 255), [int(particle.position_x), int(particle.position_y)], int(particle.size))
                    if particle.ttl <= 0:
                        rem.append(particle)

                for to_rem in rem:
                    shape.remove(to_rem)
        else: self.delay -= 0.02
