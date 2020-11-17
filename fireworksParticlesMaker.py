from classes import Particle
from random import randint
from colors import  *

particles = [] ;particles2 = []; particles3 = []
particles4 = []; particles5 = [] ;particles6 = []
particles7 = [] ;particles8 = [] ;particles9 = []
particles10 = [] ;particles11 = [] ;particles12 = []
particles13 = [] ;particles14 = [] ;particles15 = []; particles16 = []

TWOparticles = [] ;TWOparticles2 = []; TWOparticles3 = []
TWOparticles4 = []; TWOparticles5 = [] ;TWOparticles6 = []
TWOparticles7 = [] ;TWOparticles8 = [] ;TWOparticles9 = []
TWOparticles10 = [] ;TWOparticles11 = [] ;TWOparticles12 = []
TWOparticles13 = [] ;TWOparticles14 = [] ;TWOparticles15 = []; TWOparticles16 = []

def prepareParticles(PARTICLES_DENSE):
    ### Preparing Fireworks
    for _ in range(PARTICLES_DENSE):    #[speed_x, spped_y], ttl, size, color
        particles.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(20, 39),randint(2, 3), BLUE))
        particles2.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(20, 24), randint(1, 3), LIGHTBLUE))
        particles3.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(10, 20),randint(2, 2), CYAN))

        particles4.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(20, 39), randint(1, 2), PINK))
        particles5.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(20, 38), randint(1, 3)/2, MAROON))
        particles6.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(10, 20), randint(1, 1)/3, LIGHTPINK))

        particles7.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(20, 39), randint(1, 2), YELLOW))
        particles8.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(20, 35), randint(1, 3)/2, YELLOWGREEN))
        particles9.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(20, 40), randint(1, 1)/3, GOLD))

        particles7.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(20, 24), randint(1, 2), YELLOW))
        particles8.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(20, 28), randint(1, 3)/2, YELLOWGREEN))
        particles9.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(20, 32), randint(1, 1)/3, GOLD))

        particles10.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(20, 39), randint(1, 2), YELLOW))
        particles11.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(20, 35), randint(1, 3)/2, WHITE))
        particles12.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(20, 40), randint(1, 1)/3, GOLD))

        particles13.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(20, 39), randint(1, 2), PURPLE))
        particles14.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(20, 35), randint(1, 3)/2, DARKBLUE))
        particles15.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(20, 40), randint(1, 1)/3, DARKCYAN))
        particles16.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(20, 32), randint(1, 1)/2, DARKMAGENTA))

        TWOparticles.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(20, 39),randint(2, 3), BLUE))
        TWOparticles2.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(20, 24), randint(1, 3), LIGHTBLUE))
        TWOparticles3.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(10, 20),randint(2, 2), CYAN))

        TWOparticles4.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(20, 39), randint(1, 2), PINK))
        TWOparticles5.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(20, 38), randint(1, 3)/2, MAROON))
        TWOparticles6.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(10, 20), randint(1, 1)/3, LIGHTPINK))

        TWOparticles7.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(20, 39), randint(1, 2), YELLOW))
        TWOparticles8.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(20, 35), randint(1, 3)/2, YELLOWGREEN))
        TWOparticles9.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(20, 40), randint(1, 1)/3, GOLD))

        TWOparticles7.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(20, 24), randint(1, 2), YELLOW))
        TWOparticles8.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(20, 28), randint(1, 3)/2, YELLOWGREEN))
        TWOparticles9.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(20, 32), randint(1, 1)/3, GOLD))

        TWOparticles10.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(20, 39), randint(1, 2), YELLOW))
        TWOparticles11.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(20, 35), randint(1, 3)/2, WHITE))
        TWOparticles12.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(20, 40), randint(1, 1)/3, GOLD))

        TWOparticles13.append(Particle([randint(-10,10) / 100, randint(-10,10) / 100], randint(20, 39), randint(1, 2), PURPLE))
        TWOparticles14.append(Particle([randint(-10,10) / 10, randint(-10,10) / 10], randint(20, 35), randint(1, 3)/2, DARKBLUE))
        TWOparticles15.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(20, 40), randint(1, 1)/3, DARKCYAN))
        TWOparticles16.append(Particle([randint(-10,10) / 1000, randint(-10,10) / 1000], randint(20, 32), randint(1, 1)/2, DARKMAGENTA))

def reset_particles(PARTICLES_DENSE):
    particles = [] ;particles2 = []; particles3 = []
    particles4 = []; particles5 = [] ;particles6 = []
    particles7 = [] ;particles8 = [] ;particles9 = []
    particles10 = [] ;particles11 = [] ;particles12 = []
    particles13 = [] ;particles14 = [] ;particles15 = []; particles16 = []

    TWOparticles = [] ;TWOparticles2 = []; TWOparticles3 = []
    TWOparticles4 = []; TWOparticles5 = [] ;TWOparticles6 = []
    TWOparticles7 = [] ;TWOparticles8 = [] ;TWOparticles9 = []
    TWOparticles10 = [] ;TWOparticles11 = [] ;TWOparticles12 = []
    TWOparticles13 = [] ;TWOparticles14 = [] ;TWOparticles15 = []; TWOparticles16 = []

    prepareParticles(PARTICLES_DENSE)

