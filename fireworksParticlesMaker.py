from classes import Particle
from random import randint
from colors import  *

# Global particles ----------------------------------------------------------#
particles = [] ;particles2 = []; particles3 = []
particles4 = []; particles5 = [] ;particles6 = []
particles7 = [] ;particles8 = [] ;particles9 = []
particles10 = [] ;particles11 = [] ;particles12 = []
particles13 = [] ;particles14 = [] ;particles15 = []; particles16 = []
particles17 = [] ;particles18 = [] ;particles19 = []; particles20 = []

TWOparticles = [] ;TWOparticles2 = []; TWOparticles3 = []
TWOparticles4 = []; TWOparticles5 = [] ;TWOparticles6 = []
TWOparticles7 = [] ;TWOparticles8 = [] ;TWOparticles9 = []
TWOparticles10 = [] ;TWOparticles11 = [] ;TWOparticles12 = []
TWOparticles13 = [] ;TWOparticles14 = [] ;TWOparticles15 = []; TWOparticles16 = []
TWOparticles17 = [] ;TWOparticles18 = [] ;TWOparticles19 = []; TWOparticles20 = []

TEMPparticles = [] ;TEMPparticles2 = []; TEMPparticles3 = []
TEMPparticles4 = []; TEMPparticles5 = [] ;TEMPparticles6 = []
TEMPparticles7 = [] ;TEMPparticles8 = [] ;TEMPparticles9 = []
TEMPparticles10 = [] ;TEMPparticles11 = [] ;TEMPparticles12 = []
TEMPparticles13 = [] ;TEMPparticles14 = [] ;TEMPparticles15 = []; TEMPparticles16 = []
TEMPparticles17 = [] ;TEMPparticles18 = [] ;TEMPparticles19 = []; TEMPparticles20 = []

# particle: speed, ttl, size, color, velocity = (-20,20)
DIVIDER_FOR_ALL_TTL = 2
def prepareParticles(PARTICLES_DENSE):
    ### Preparing Fireworks
    for _ in range(PARTICLES_DENSE):    #[speed_x, spped_y], ttl, size, color
        particles.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(20, 25)/DIVIDER_FOR_ALL_TTL,randint(2, 3), BLUE))
        particles2.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(20, 24)/DIVIDER_FOR_ALL_TTL, randint(1, 3), LIGHTBLUE))
        particles3.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(15, 20)/DIVIDER_FOR_ALL_TTL,randint(2, 2), CYAN))

        particles4.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(20, 25)/DIVIDER_FOR_ALL_TTL, randint(1, 2), PINK))
        particles5.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(20, 25)/DIVIDER_FOR_ALL_TTL, randint(1, 3)/2, MAROON))
        particles6.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(15, 20)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/3, LIGHTPINK))

        particles7.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(20, 25)/DIVIDER_FOR_ALL_TTL, randint(1, 2), YELLOW))
        particles8.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(25, 27)/DIVIDER_FOR_ALL_TTL, randint(1, 3)/2, YELLOWGREEN))
        particles9.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(23, 25)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/3, GOLD))

        particles7.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(20, 24)/DIVIDER_FOR_ALL_TTL, randint(1, 2), YELLOW))
        particles8.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(25, 28)/DIVIDER_FOR_ALL_TTL, randint(1, 3)/2, YELLOWGREEN))
        particles9.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(20, 23)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/3, GOLD))

        particles10.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(28, 33)/DIVIDER_FOR_ALL_TTL, randint(1, 2), YELLOW))
        particles11.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(26, 29)/DIVIDER_FOR_ALL_TTL, randint(1, 3)/2, WHITE))
        particles12.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(20, 25)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/3, GOLD))

        particles13.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(22, 26)/DIVIDER_FOR_ALL_TTL, randint(1, 2), PURPLE))
        particles14.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(21, 25)/DIVIDER_FOR_ALL_TTL, randint(1, 3)/2, DARKBLUE))
        particles15.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(23, 27)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/3, DARKCYAN))
        particles16.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(22, 27)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/2, DARKMAGENTA))

        particles17.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(25, 29)/DIVIDER_FOR_ALL_TTL, randint(1, 2)/2, WHITE))
        particles18.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(22, 25)/DIVIDER_FOR_ALL_TTL, randint(1, 3)/2, LIGHTGREEN))
        particles19.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(23, 27)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/3, GREENYELLOW))
        particles20.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(25, 28)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/2, GOLD))

        TWOparticles.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(25, 28)/DIVIDER_FOR_ALL_TTL,randint(2, 3), BLUE))
        TWOparticles2.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(22, 23)/DIVIDER_FOR_ALL_TTL, randint(1, 3), LIGHTBLUE))
        TWOparticles3.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(15, 20)/DIVIDER_FOR_ALL_TTL,randint(2, 2), CYAN))

        TWOparticles4.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(24, 27)/DIVIDER_FOR_ALL_TTL, randint(1, 2), PINK))
        TWOparticles5.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(23, 27)/DIVIDER_FOR_ALL_TTL, randint(1, 3)/2, MAROON))
        TWOparticles6.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(15, 20)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/3, LIGHTPINK))

        TWOparticles7.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(28, 33)/DIVIDER_FOR_ALL_TTL, randint(1, 2), YELLOW))
        TWOparticles8.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(27, 32)/DIVIDER_FOR_ALL_TTL, randint(1, 3)/2, YELLOWGREEN))
        TWOparticles9.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(26, 31)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/3, GOLD))

        TWOparticles7.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(20, 23)/DIVIDER_FOR_ALL_TTL, randint(1, 2), YELLOW))
        TWOparticles8.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(21, 28)/DIVIDER_FOR_ALL_TTL, randint(1, 3)/2, YELLOWGREEN))
        TWOparticles9.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(26, 29)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/3, GOLD))

        TWOparticles10.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(27, 33)/DIVIDER_FOR_ALL_TTL, randint(1, 2), YELLOW))
        TWOparticles11.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(24, 28)/DIVIDER_FOR_ALL_TTL, randint(1, 3)/2, WHITE))
        TWOparticles12.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(20, 24)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/3, GOLD))

        TWOparticles13.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(26, 32)/DIVIDER_FOR_ALL_TTL, randint(1, 2), PURPLE))
        TWOparticles14.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(26, 31)/DIVIDER_FOR_ALL_TTL, randint(1, 3)/2, DARKBLUE))
        TWOparticles15.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(26, 31)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/3, DARKCYAN))
        TWOparticles16.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(27, 32)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/2, DARKMAGENTA))

        TWOparticles17.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(26, 29)/DIVIDER_FOR_ALL_TTL, randint(1, 2)/2, WHITE))
        TWOparticles18.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(20, 25)/DIVIDER_FOR_ALL_TTL, randint(1, 3)/2, LIGHTGREEN))
        TWOparticles19.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(28, 32)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/3, GREENYELLOW))
        TWOparticles20.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(28, 32)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/2, GOLD))

def prepareTEMPParticles(PARTICLES_DENSE):
    ### Preparing Fireworks
    for _ in range(PARTICLES_DENSE): 
        TEMPparticles.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(25, 30)/DIVIDER_FOR_ALL_TTL,randint(2, 3), BLUE))
        TEMPparticles2.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(22, 24)/DIVIDER_FOR_ALL_TTL, randint(1, 3), LIGHTBLUE))
        TEMPparticles3.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(10, 20)/DIVIDER_FOR_ALL_TTL,randint(2, 2), CYAN))

        TEMPparticles4.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(26, 32)/DIVIDER_FOR_ALL_TTL, randint(1, 2), PINK))
        TEMPparticles5.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(26, 32)/DIVIDER_FOR_ALL_TTL, randint(1, 3)/2, MAROON))
        TEMPparticles6.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(15, 20)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/3, LIGHTPINK))

        TEMPparticles7.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(25, 30)/DIVIDER_FOR_ALL_TTL, randint(1, 2), YELLOW))
        TEMPparticles8.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(25, 31)/DIVIDER_FOR_ALL_TTL, randint(1, 3)/2, YELLOWGREEN))
        TEMPparticles9.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(25, 32)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/3, GOLD))

        TEMPparticles10.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(25, 31)/DIVIDER_FOR_ALL_TTL, randint(1, 2), YELLOW))
        TEMPparticles11.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(24, 29)/DIVIDER_FOR_ALL_TTL, randint(1, 3)/2, WHITE))
        TEMPparticles12.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(22, 26)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/3, GOLD))

        TEMPparticles13.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(21, 27)/DIVIDER_FOR_ALL_TTL, randint(1, 2), PURPLE))
        TEMPparticles14.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(20, 25)/DIVIDER_FOR_ALL_TTL, randint(1, 3)/2, DARKBLUE))
        TEMPparticles15.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(25, 32)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/3, DARKCYAN))
        TEMPparticles16.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(25, 32)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/2, DARKMAGENTA))

        TEMPparticles17.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(22, 26)/DIVIDER_FOR_ALL_TTL, randint(1, 2)/2, WHITE))
        TEMPparticles18.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(21, 25)/DIVIDER_FOR_ALL_TTL, randint(1, 3)/2, LIGHTGREEN))
        TEMPparticles19.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(25, 32)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/3, GREENYELLOW))
        TEMPparticles20.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(25, 32)/DIVIDER_FOR_ALL_TTL, randint(1, 1)/2, GOLD))

def reset_particles(PARTICLES_DENSE):
    particles = [] ;particles2 = []; particles3 = []
    particles4 = []; particles5 = [] ;particles6 = []
    particles7 = [] ;particles8 = [] ;particles9 = []
    particles10 = [] ;particles11 = [] ;particles12 = []
    particles13 = [] ;particles14 = [] ;particles15 = []; particles16 = []
    particles17 = [] ;particles18 = [] ;particles19 = []; particles20 = []
    

    TWOparticles = [] ;TWOparticles2 = []; TWOparticles3 = []
    TWOparticles4 = []; TWOparticles5 = [] ;TWOparticles6 = []
    TWOparticles7 = [] ;TWOparticles8 = [] ;TWOparticles9 = []
    TWOparticles10 = [] ;TWOparticles11 = [] ;TWOparticles12 = []
    TWOparticles13 = [] ;TWOparticles14 = [] ;TWOparticles15 = []; TWOparticles16 = []
    TWOparticles17 = [] ;TWOparticles18 = [] ;TWOparticles19 = []; TWOparticles20 = []

    prepareParticles(PARTICLES_DENSE)

def reset_TEMP_particles(PARTICLES_DENSE):
    TEMPparticles = [] ;TEMPparticles2 = []; TEMPparticles3 = []
    TEMPparticles4 = []; TEMPparticles5 = [] ;TEMPparticles6 = []
    TEMPparticles7 = [] ;TEMPparticles8 = [] ;TEMPparticles9 = []

    TEMPparticles10 = [] ;TEMPparticles11 = [] ;TEMPparticles12 = []
    TEMPparticles13 = [] ;TEMPparticles14 = [] ;TEMPparticles15 = []; TEMPparticles16 = []
    TEMPparticles17 = [] ;TEMPparticles18 = [] ;TEMPparticles19 = []; TEMPparticles20 = []

    prepareTEMPParticles(PARTICLES_DENSE)