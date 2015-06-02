import math
from Environment.Agent import Agent
from Environment.Link import Link
from Environment.Location import Location

class Node:
    count = 0

    upgradeExtractionEfficiency = 0.05
    extractionExponent = -4

    buildCost = 1000000    
    upgradeClockCost = 10000000
    
    importPowerEfficiency = 0.9
    exportPowerEfficiency = 0.8
    
    def __init__(self, location, initialOwnerNumber, clockCount, initialPower = 0):
        from Environment.Map import Map

        self.location = location
        Map.occupied[location.x,location.y,location.z] = 1 
        
        self.clock = 10
        self.lastTick = clockCount
        self.locks = []
        self.links = []
        self.extraction = 0 #resource to power function coefficient
        self.power = initialPower
        self.number = Node.count
        
        self.ownership = []
        
        for i in range(Agent.count):
            if (i == initialOwnerNumber):
                self.ownership.append(1.0)
            else:
                self.ownership.append(0.0)
                
        print('Node %d created at Location(%d, %d, %d) by Agent %d' % (self.number, self.location.x, self.location.y, self.location.z, initialOwnerNumber))
        Node.count += 1
        Map.nodes.append(self)
        
    def getOwnerNumber(self):
        most = 0.0
        agentNumber = 0
        
        for i in range(Agent.count):
            if (self.ownership[i] > most):
                most = self.ownership[i]
                agentNumber = i
                
        return agentNumber
        
    def buildNode(self, clockCount):
        from Environment.Map import Map
        
        self.power -= Node.buildCost;
        
        if (Map.occupied.sum() == (Map.size * Map.size * Map.size)):
            #print('Map full of Nodes!')
            return
        
        while (True): #search for random location within a distance of Link.maxLength from self.location
            newLocation = Location()
            if (newLocation.distance(self.location) <= Link.maxLength):
                if (Map.occupied[newLocation.x,newLocation.y,newLocation.z] == 0):
                    break            
                    
        newNode = Node(newLocation, self.getOwnerNumber(), clockCount)        
        newLink = Link(self, newNode)
        
    def upgradeClock(self):
        if (self.clock > 1):
            self.clock -= 0.1
            self.power -= Node.upgradeClockCost
            
            print('Node %d Clock Upgraded to %d' % (self.number, self.clock))

        
    def upgradeExtraction(self, power):
        self.extraction += Node.upgradeExtractionEfficiency * power 
        self.power -= power
        
        print('Node %d Extraction Upgraded to %f' % (self.number, self.extraction))
        
    def upgradeLinkThroughput(self, link, power):
        link.throughput += Link.upgradeThroughputEfficiency * power
        self.power -= power
        
        print('Node %d Upgraded Link %d Throughput to %f' % (self.number, link.number, link.throughput))
        
    def importPower(self):
        for link in self.links:
            if (link.nodeA.number == self.number):
                self.power += Node.importPowerEfficiency * link.powerBA #gets all power after 1 turn traveling link
                link.powerBA = 0
            elif (link.nodeB.number == self.number):
                self.power += Node.importPowerEfficiency * link.powerAB #gets all power after 1 turn traveling link
                link.powerAB = 0
        
    def exportPower(self, link, power):
        if (link.nodeA.number == self.number):
            link.powerAB += Node.exportPowerEfficiency * power
            self.power -= power
        elif (link.nodeB.number == self.number):
            link.powerBA += Node.exportPowerEfficiency * power
            self.power -= power
        else:
            print('Node not contained in Link given')
        
    def mineResources(self):
        from Environment.Map import Map
        
        resource = Location()
        for i in range(Map.size):
            for j in range(Map.size):
                for k in range(Map.size):
                    resource.x = i
                    resource.y = j
                    resource.z = k
                    
                    if (resource.isSame(self.location)):
                        miningYield = 1
                    else:
                        miningYield = resource.distance(self.location) ** Node.extractionExponent
                    #print('Node %d Mining Yield: %f' % (self.number, miningYield))
                    
                    if (Map.resources[i, j, k] != 0):
                        
                        if (Map.resources[i, j, k] - miningYield > 0):
                            self.power += self.extraction * miningYield
                            Map.resources[i, j, k] -= miningYield
                        else:
                            self.power += self.extraction * Map.resources[i, j, k]
                            Map.resources[i, j, k] = 0
                            print('Resource at Location(%d, %d, %d) exhausted' % (i, j, k))
                            print('Resources Left: %f' % (Map.resources.sum()))
                
    def tick(self, clockCount):
        if (abs(clockCount - self.lastTick) == math.ceil(self.clock)): #use abs() b/c of circular nature of clock
            self.mineResources()       
            self.importPower()
            
            #print('Node %d at gross power %f' % (self.number, self.power))
            
            if (self.power > Node.upgradeClockCost):
                self.upgradeClock()
           
            if (self.power > Node.buildCost):
                self.buildNode(clockCount)
                
            if (len(self.links) > 0):                
                exportPowerPortion = self.power / (4 * len(self.links))    
                for exportLink in self.links:
                    self.upgradeLinkThroughput(exportLink, exportPowerPortion)
                    self.exportPower(exportLink, exportPowerPortion)                    
                
            self.upgradeExtraction(self.power)
                        
            self.lastTick = clockCount
            