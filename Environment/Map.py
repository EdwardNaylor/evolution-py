import numpy as np
from Environment.Agent import Agent
from Environment.Node import Node
from Environment.Location import Location

class Map:
    size = 0
    agentCount = 0
    startingNodePower = 0.01
    
    def __init__(self):
        Map.resources = np.zeros((Map.size, Map.size, Map.size)) #3d floating point matrix
        Map.occupied = np.zeros((Map.size, Map.size, Map.size))
        Map.nodes = []
        Map.links = []
        Map.agents = []
                
        print('Map created')
        
    def generateAgents(self):
        for i in range(Agent.count):
            agent = Agent(i)
            self.generateStartingNode(agent)
            
    def generateStartingNode(self, agent):
        #need to verify location is not occupied
        node = Node(Location(), agent.number, 0, Map.startingNodePower) #create node in random location owned by agent
    
    def generateResources(self):
        for i in range(Map.size):
            for j in range(Map.size):
                for k in range(Map.size):
                    Map.resources[i,j,k] = 100;
        
        print('Resources generated')
        
    def tick(self, clockCount):
        
        for n in range(len(Map.nodes)):
            Map.nodes[n].tick(clockCount)