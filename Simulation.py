from Environment.Map import *

class Simulation:
    
    def __init__(self, mapSize, agentCount, maxClock):
        self.mapSize = mapSize
        self.playerCount = playerCount
        self.maxLength = maxLength
        
        self.map = Map(mapSize)
        self.map.generateResources()
        self.map.generateAgents(playerCount)
        
        
        self.clockCount = 0
    
    def run(self):
        print('Simulation started')
        
        while (clockCount < self.maxLength):
            
            self.clockCount += 1
    
        print('Simulation complete')