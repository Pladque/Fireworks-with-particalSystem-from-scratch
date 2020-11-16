import pygame, sys, random
import datetime
 
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
from classes import Particle, Firework
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
PARTICLES_DENSE = 50
do_it_once = True

year = datetime.datetime.now().year
hour = datetime.datetime.now().hour


for _ in range(PARTICLES_DENSE):
    particles.append(Particle([random.randint(-10,10) / 10000, random.randint(-10,10) / 10000], random.randint(10, 18), random.randint(1, 2)))

fireworks = [Firework(particles,[WIDTH / 2 + random.randint(-10,10),HEIGHT / 2 + random.randint(-10,10)], 0.5)]
 
# Loop ------------------------------------------------------- #
while True:
    # Background --------------------------------------------- #
    screen.fill((0,0,get_bright(datetime.datetime.now().hour)))
    

    #if datetime.datetime.now().year != year:
    if True:     
        for firework in fireworks:
            firework.blowup(screen)
        
    
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
    mainClock.tick(50)