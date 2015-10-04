class Path:
    def __init__(self, nodes=[], cost=0):
        self.nodes = nodes
        self.cost = cost
        
    def add_node(n, c):
        self.nodes.append(n)
        self.cost = self.cost + c
        