class Particle:
    def __init__(self, position, speed, ttl):
        self.position_x = position[0]
        self.position_y = position[1]
        self.speed_x = speed[0]
        self.speed_y = speed[1]
        self.ttl = ttl