class Node:
    def __init__(self, name, category, location):
        self.name = name
        self.category = category
        self.location = location
        self.edges = []
        
    def add_edge(self, node, time, cost):
        self.edges.append({'destination': node, 'time' : time, 'cost' : cost})
