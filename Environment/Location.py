import random
import math

class Location:
    
    def __init__(self, x = -1, y = -1, z = -1):
        from Environment.Map import Map
        
        if (x == -1 and y == -1 and z == -1): #random location with Map.size
            self.x = random.randint(0, Map.size-1)
            self.y = random.randint(0, Map.size-1)
            self.z = random.randint(0, Map.size-1)
        else: #location passed in
            self.x = x
            self.y = y
            self.z = z
            
    def distance(self, otherLocation):
        dx = otherLocation.x - self.x
        dy = otherLocation.y - self.y
        dz = otherLocation.z - self.z
        
        mag = dx * dx + dy * dy + dz * dz
        
        return math.sqrt(mag)
        
    def isSame(self, otherLocation):
        if (self.x == otherLocation.x and self.y == otherLocation.y and self.z == otherLocation.z):
            return True
        else:
            return False