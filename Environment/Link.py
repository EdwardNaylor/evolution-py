import math

class Link:
    maxLength = 10
    count = 0
    
    upgradeThroughputEfficiency = 0.1
    
    def __init__(self, nodeA, nodeB):
        from Environment.Map import Map
        
        self.nodeA = nodeA
        self.nodeB = nodeB
        self.nodeA.links.append(self)
        self.nodeB.links.append(self)        
        
        self.bandwidth = 0
        self.throughput = 0
        self.length = nodeA.location.distance(nodeB.location)
        
        self.powerAB = 0
        self.powerBA = 0
        
        self.number = Link.count
        
        print('Link %d of length %f created by Agent %d from Node %d to Node %d' % (self.number, self.length, self.nodeA.getOwnerNumber(), self.nodeA.number, self.nodeB.number))
        Link.count += 1
        Map.links.append(self)