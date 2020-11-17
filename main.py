import pygame, sys, random
import datetime
 
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
from classes import Particle, Firework
from colors import  *
from fireworksParticlesMaker import *
from brightness import get_bright
pygame.init()
WIDTH = HEIGHT = 800
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)


PARTICLES_DENSE = 200
do_it_once = True

year = datetime.datetime.now().year
hour = datetime.datetime.now().hour

prepareParticles(PARTICLES_DENSE)
def reset_fireworks():
    return[
        Firework([particles,particles2, particles3],[WIDTH / 2 + random.randint(-50,50) ,HEIGHT / 2 + random.randint(-50,50)], 0.5, 1),
        Firework([particles4,particles5, particles6],[WIDTH / 3+ random.randint(-50,50) ,HEIGHT / 2.7+ random.randint(-50,50)], 1.5, 3),
        Firework([particles7,particles8, particles9],[WIDTH / 1.5 + random.randint(-50,50),HEIGHT / 1.5+ random.randint(-50,50)], 3, 5),
        Firework([particles10,particles11, particles12],[WIDTH / 4.3 + random.randint(-50,50),HEIGHT / 3.1415 + random.randint(-50,50)], 1.8, 5),
        Firework([particles13,particles14, particles15, particles16],[WIDTH / 1.2 + random.randint(-50,50) ,HEIGHT / 5 + random.randint(-50,50)], 1.68, 2),

        Firework([TWOparticles,TWOparticles2, TWOparticles3],[WIDTH / 1.5 + random.randint(-50,50) ,HEIGHT / 2.5 + random.randint(-50,50)], 4, 1),
        Firework([TWOparticles4,TWOparticles5, TWOparticles6],[WIDTH / 7+ random.randint(-50,50) ,HEIGHT / 2.7+ random.randint(-50,50)], 3.2, 3),
        Firework([TWOparticles7,TWOparticles8, TWOparticles9],[WIDTH / 1.5 + random.randint(-50,50),HEIGHT / 1.5+ random.randint(-50,50)], 0.2, 5),
        Firework([TWOparticles10,TWOparticles11, TWOparticles12],[WIDTH / 2.3 + random.randint(-50,50),HEIGHT / 3.1415 + random.randint(-50,50)], 5, 5),
        Firework([TWOparticles13,TWOparticles14, TWOparticles15, TWOparticles16],[WIDTH / 4 + random.randint(-50,50) ,HEIGHT / 5 + random.randint(-50,50)], 3, 2)
        ]

firework_light = 0
fireworks = reset_fireworks()
# Loop ------------------------------------------------------- #
while True:
    # Background --------------------------------------------- #
    screen.fill((0,0,get_bright(datetime.datetime.now().hour) + firework_light))
    firework_light -= 0.01

    #if datetime.datetime.now().year != year:
    if True:     
        all_dead = True
        for firework in fireworks:
            firework.blowup(screen)
            if firework.just_blew_up():
                firework_light += firework.get_lightness()
            elif firework.if_died():
                firework_light -= firework.get_lightness()
            if firework.is_dead() is False:
                all_dead = False
        # replaying all fireworks
        if all_dead:
            firework_light = 0
            reset_particles(PARTICLES_DENSE)
            fireworks = reset_fireworks()

        
    
    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                

    pygame.display.update()
    mainClock.tick(100)