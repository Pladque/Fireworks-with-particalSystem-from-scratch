from random import randint
class Particle:
    def __init__(self, position, speed, ttl, size):
        self.position_x = position[0]
        self.position_y = position[1]
        self.speed_x = speed[0]
        self.speed_y = speed[1]
        self.ttl = ttl
        self.size = size
        self.velocity_x = randint(-10,10) / 10000
        self.velocity_y = randint(-10,10) / 10000