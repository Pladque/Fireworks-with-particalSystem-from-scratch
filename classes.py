from random import randint
from colors import  *
import pygame
from pygame import mixer
class Particle:
    def __init__(self, speed, ttl, size, color, velocity = (-20,20)):
        self.speed_x = speed[0]
        self.speed_y = speed[1]
        self.ttl = ttl
        self.size = size
        self.color = color
        self.velocity_x = randint(velocity[0],velocity[1]) / 1000
        self.velocity_y = randint(velocity[0],velocity[1]) / 1000

        self.position_x , self.position_y = 0,0

class  Firework:
    def __init__(self, particles, position, delay = 0, lightness = 0):
        self.shapes = particles
        self.position_x = position[0]
        self.position_y = position[1]
        self.delay = delay
        self.lightness = lightness

        self.ready_to_blow_up = True
        self.already_died = False
        self.sound = mixer.Sound('FireworkSound.wav')
        
        for x,shape in enumerate(self.shapes):
            for y, particle in enumerate(shape):
                self.shapes[x][y].position_x = self.position_x
                self.shapes[x][y].position_y = self.position_y 


    def blowup(self, screen):
        if self.delay <= 0:
            self.ready_to_blow_up = False
            for shape in self.shapes:
                rem = []
                for particle in shape:
                    particle.position_x += particle.speed_x
                    particle.position_y += particle.speed_y

                    particle.speed_x += particle.velocity_x
                    particle.speed_y += particle.velocity_y
                    particle.velocity_y += 0.0005           #making falling overtime

                    particle.ttl -= 0.1
                    particle.size *= abs((100000 - particle.ttl) / 100000)   #making smaler over time

                    pygame.draw.circle(screen, particle.color, [int(particle.position_x), int(particle.position_y)], int(particle.size))

                    if particle.ttl <= 0:
                        rem.append(particle)

                for to_rem in rem:
                    shape.remove(to_rem)
        else: self.delay -= 0.02

    def get_lightness(self):
        return self.lightness

    def just_blew_up(self):
        return self.ready_to_blow_up and self.delay<=0

    def play_sound(self):
        self.sound.play()

    def if_died(self):
        if self.already_died is False:
            for shape in self.shapes:
                if shape != []: return False
            self.already_died = True
            return True
        return False

    def is_dead(self):
        for shape in self.shapes:
            if shape != []: return False
        return True
                    