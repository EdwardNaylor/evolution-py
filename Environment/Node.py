class Node:
    maxLength = 10
    powerOnThreshold = 30
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.clock = 10
        self.locks = []
        self.extraction = 0
        self.power = 0