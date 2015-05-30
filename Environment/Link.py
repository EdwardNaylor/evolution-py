class Link:
    maxLength = 10
    
    def __init__(self, nodeA, nodeB):
        self.nodeA = nodeA
        self.nodeB = nodeB
        self.bandwidth = 0
        self.throughput = 0
        