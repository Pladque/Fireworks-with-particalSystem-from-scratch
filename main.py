import pygame, sys, random
import datetime
from classes import Particle, Firework
from colors import  *
from fireworksParticlesMaker import *
from brightness import get_bright

from pygame.locals import *
from pygame import mixer
pygame.init()
mainClock = pygame.time.Clock()

# Pygame screen and widnow ------------------------------------#
WIDTH = HEIGHT = 800
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((WIDTH, HEIGHT),0,32)

PARTICLES_DENSE = 150
firework_light = 0

# Time --------------------------------------------------------#
year = datetime.datetime.now().year
hour = datetime.datetime.now().hour

# Setting up Fireworks ----------------------------------------#
prepareParticles(PARTICLES_DENSE)
reset_TEMP_particles(PARTICLES_DENSE)
def reset_fireworks():  
    return[
        Firework([particles,particles2, particles3],[WIDTH / 2 + random.randint(-100,100) ,HEIGHT / 2 + random.randint(-100,100)], 0.5 + random.randint(-1,2)/2, 1),
        Firework([particles4,particles5, particles6],[WIDTH / 3+ random.randint(-100,100) ,HEIGHT / 2.7+ random.randint(-100,100)], 1.4 + random.randint(-1,2)/2, 3),
        Firework([particles7,particles8, particles9],[WIDTH / 1.5 + random.randint(-100,100),HEIGHT / 1.5+ random.randint(-100,100)], 3 + random.randint(-1,2)/2, 5),
        Firework([particles10,particles11, particles12],[WIDTH / 4.3 + random.randint(-100,100),HEIGHT / 3.1415 + random.randint(-100,100)], 1.8+ random.randint(-1,2)/2, 5),
        Firework([particles13,particles14, particles15, particles16],[WIDTH / 1.2 + random.randint(-100,100) ,HEIGHT / 5 + random.randint(-100,100)], 1.68+ random.randint(-1,2)/2, 2),
        Firework([particles17,particles18, particles19, particles20],[WIDTH / 8 + random.randint(-100,100) ,HEIGHT / 1.3 + random.randint(-100,100)], 0.3+ random.randint(-1,2)/2, 3),

        Firework([TWOparticles,TWOparticles2, TWOparticles3],[WIDTH / 1.5 + random.randint(-100,100) ,HEIGHT / 2.5 + random.randint(-100,100)], 4+ random.randint(-1,2)/2, 1),
        Firework([TWOparticles4,TWOparticles5, TWOparticles6],[WIDTH / 7+ random.randint(-100,100) ,HEIGHT / 2.7+ random.randint(-100,100)], 3.42+ random.randint(-1,2)/2, 3),
        Firework([TWOparticles7,TWOparticles8, TWOparticles9],[WIDTH / 1.5 + random.randint(-100,100),HEIGHT / 1.5+ random.randint(-100,100)], 0.2+ random.randint(-1,2)/5, 5),
        Firework([TWOparticles10,TWOparticles11, TWOparticles12],[WIDTH / 2.3 + random.randint(-100,100),HEIGHT / 3.1415 + random.randint(-100,100)], 4+ random.randint(-1,2)/2, 5),
        Firework([TWOparticles13,TWOparticles14, TWOparticles15, TWOparticles16],[WIDTH / 4 + random.randint(-100,100) ,HEIGHT / 5 + random.randint(-100,100)], 2.75+ random.randint(-1,2)/2, 2),
        Firework([TWOparticles17,TWOparticles18, TWOparticles19, TWOparticles20],[WIDTH / 7 + random.randint(-100,100) ,HEIGHT / 1.5 + random.randint(-100,100)], 3.2+ random.randint(-1,2)/2, 5),

        ]

def reset_temp_fireworks():
    return [
        Firework([TEMPparticles,TEMPparticles2, TEMPparticles3],[WIDTH / 4+ random.randint(-100,100) ,HEIGHT / 1.1+ random.randint(-100,100)], 0.3+ random.randint(-1,2)/2, 2),
        Firework([TEMPparticles4,TEMPparticles5, TEMPparticles6],[WIDTH / 3+ random.randint(-100,100) ,HEIGHT / 2.7+ random.randint(-50,50)], 0, 3),
        Firework([TEMPparticles7,TEMPparticles8, TEMPparticles9],[WIDTH / 1.5 + random.randint(-100,100),HEIGHT / 1.5+ random.randint(-100,100)], 0.7+ random.randint(-1,2)/2, 5),
        
        Firework([TEMPparticles10,TEMPparticles11, TEMPparticles12],[WIDTH / 4.3 + random.randint(-100,100),HEIGHT / 3.1415 + random.randint(-100,100)], 1+ random.randint(-1,2)/2, 5),
        Firework([TEMPparticles13,TEMPparticles14, TEMPparticles15, TEMPparticles16],[WIDTH / 1.2 + random.randint(-100,100) ,HEIGHT / 5 + random.randint(-100,100)], 0.2+ random.randint(-1,2)/2, 2),
        Firework([TEMPparticles17,TEMPparticles18, TEMPparticles19, TEMPparticles20],[WIDTH / 8 + random.randint(-100,100) ,HEIGHT / 1.3 + random.randint(-100,100)], 0.9+ random.randint(-1,2)/2, 3),
        ]

fireworks = reset_fireworks()
fireworks_to_enter_new_cycle = reset_temp_fireworks()
temp_fireworks_start = False

# Loop ------------------------------------------------------- #
while True:
    # Background --------------------------------------------- #
    screen.fill((0,0,get_bright(datetime.datetime.now().hour) + firework_light))
    firework_light -= 0.01

    if datetime.datetime.now().year != year:
    #if True:     
        is_alive = 0
        is_alive_2 = 0
        for firework in fireworks:
            firework.blowup(screen)
            if firework.just_blew_up():
                firework_light += firework.get_lightness()
                firework.play_sound()
            elif firework.if_died():
                firework_light -= firework.get_lightness()
            if firework.is_dead() is False:
                is_alive += 1
        # replaying all fireworks
        if is_alive is 0:
            firework_light = 0
            reset_particles(PARTICLES_DENSE)
            fireworks = reset_fireworks()
        # playing other fireworks while main restarting
        elif is_alive <=6:  
            temp_fireworks_start = True
        if temp_fireworks_start:
            for firework in fireworks_to_enter_new_cycle:
                firework.blowup(screen)
                if firework.just_blew_up():
                    firework_light += firework.get_lightness()
                    firework.play_sound()
                elif firework.if_died():
                    firework_light -= firework.get_lightness()
                if firework.is_dead() is False:
                    is_alive_2 += 1       
        if is_alive_2 is 0 and temp_fireworks_start is True:
            reset_TEMP_particles(PARTICLES_DENSE)
            fireworks_to_enter_new_cycle = reset_temp_fireworks()
            temp_fireworks_start = False   
    
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