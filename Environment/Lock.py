class Lock:
    
    def __init__(self, size):
        self.size = size
        self.resources = np.zeros((self.size, self.size, self.size)) #3d floating point matrix
        self.nodes = []
        self.links = []
        self.agents = []
        
        self.sysclk = 1
    
    def generateResources(self):
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    self.resources[i,j,k] = 100;
    
