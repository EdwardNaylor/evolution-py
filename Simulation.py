import math
from Environment.Map import Map
from Environment.Agent import Agent
from Environment.Link import Link

class Simulation:
    maxClock = 0
    
    def __init__(self, mapSize, agentCount, maxClock):
        Map.size = mapSize
        Link.maxLength = math.floor(Map.size / 2.5)
        Agent.count = agentCount
        Simulation.maxClock = maxClock
        
        Simulation.map = Map()
        Simulation.map.generateResources()
        Simulation.map.generateAgents()
        
        self.clockCount = 0
    
    def run(self):
        print('Simulation begun')
        
        while (True):
            if (self.clockCount >= Simulation.maxClock):
                print('Max Clock %d reached' % (Simulation.maxClock))
                break
            elif (Simulation.map.occupied.sum() >= (Map.size * Map.size * Map.size)):
                print('All Locations Occupied')
                break
            elif (Simulation.map.resources.sum() <= 0):
                print('All Resources Depleted')
                break            
            
            Simulation.map.tick(self.clockCount)            
            self.clockCount += 1
            
        print('Simulation complete')