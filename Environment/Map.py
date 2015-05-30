import numpy as np
from Environment.Agent import *

class Map:
    
    def __init__(self, size):
        self.size = size
        self.resources = np.zeros((self.size, self.size, self.size)) #3d floating point matrix
        self.nodes = []
        self.links = []
        self.agents = []
        
        self.sysclk = 1
        
        print('Map created')
        
    def generateAgents(self, count):
        for i in range(count):
            a = Agent(i)
            self.agents.append(a)
    
    def generateResources(self):
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    self.resources[i,j,k] = 100;
        
        print('Resources generated')
    
