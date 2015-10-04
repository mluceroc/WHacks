class Path:
    def __init__(self, nodes=[], cost=0):
        self.nodes = nodes
        self.cost = cost
        if self.nodes:
            self.last_node = self.nodes[-1]

        
    def add_node(self, n, c):
        self.nodes.append(n)
        self.cost = self.cost + c
        self.last_node = n
