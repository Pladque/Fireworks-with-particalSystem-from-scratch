import pygame, sys, random
import datetime
 
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
from classes import Particle
from brightness import get_bright
pygame.init()
WIDTH = HEIGHT = 800
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)
 
# a particle is...
# a thing that exists at a location
# typically moves around
# typically changes over time
# and typically disappears after a certain amount of time
 
# [loc, velocity, timer]
particles = []
    
year = datetime.datetime.now().year
hour = datetime.datetime.now().hour
 
# Loop ------------------------------------------------------- #
while True:
    # Background --------------------------------------------- #
    screen.fill((0,0,get_bright(datetime.datetime.now().hour)))

    #if datetime.datetime.now().year != year:
    if True:
        
        particles.append(Particle([WIDTH / 2,HEIGHT / 2], [random.randint(-10,10) / 100, random.randint(-10,10) / 100], random.randint(4, 6)))
        rem = []
        for particle in particles:
            particle.position_x += particle.speed_x
            particle.position_y += particle.speed_y
            particle.ttl -= 0.1
            particle.speed_x += particle.speed_x /10
            pygame.draw.circle(screen, (255, 255, 255), [int(particle.position_x), int(particle.position_y)], int(particle.ttl))
            if particle.ttl <= 0:
                rem.append(particles.index(particle))
            
        for to_rem in rem:
            particles.pop(to_rem)
    
    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)