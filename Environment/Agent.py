class Agent:
    count = 0
    
    def __init__(self, number):
        from Environment.Map import Map
        
        self.number = number
        
        print('Agent %d created' % (self.number))
        Map.agents.append(self)
