from operator import itemgetter
from node import Node
from path import Path
from location import Location
import Queue
from random import randint

class Graph:
    input_data = [Node('oak grove', 'mbta', Location('malden', 'ma')),
                  Node('north station', 'mbta', Location('boston', 'ma'))]
    
    
    def __init__(self, location_A, location_B):
        self.A = Node('A', 'user', location_A) 
        self.B = Node('B', 'user', location_B)
        
        self.uber_cost = self.get_uber_cost(2, 2)
        self.uber_time = self.get_uber_time(location_A, location_B)
        pt_nodes = Graph.input_data
        my_graph = {}
        last = None
        for pt_node in pt_nodes: 
            a_cost = self.get_uber_cost(location_A, pt_node.location)
            if ( a_cost > self.uber_cost ):
                break
            b_cost = self.get_uber_cost(pt_node.location, location_B)
            if( b_cost > self.uber_cost ):
                break
            time_to_a = self.get_uber_time(location_A, pt_node.location)
            time_to_b = self.get_uber_time(pt_node.location, location_B)
            self.A.add_edge(pt_node, a_cost, time_to_a)
            pt_node.add_edge(self.B, b_cost, time_to_b)
            #ps this isn't going to work
            my_graph[pt_node.location] = {'node': pt_node, 'time_to_b':time_to_b}
        
        for this in list(my_graph.values()):
            for that in this['node'].edges:
                if that['destination'].location == self.B.location:
                    break
                if this['time_to_b'] < my_graph[that['destination'].location]['time_to_b'] :
                    this['node'].edges.remove(that)           


    def get_paths(self):
        all_paths = Queue.Queue()
        all_paths.put(Path([self.A]))
        final_paths = []
        
        while not all_paths.empty():
            path = all_paths.get()
            print path.last_node.name
            if path.last_node == self.B:
                final_paths.append(path)
                break
            for edge in path.last_node.edges:
                if ( path.cost + edge['cost'] < self.uber_cost ):
                    new_path = Path(path.nodes, path.cost)
                    new_path.add_node(edge['destination'], edge['cost'])
                    all_paths.put(new_path)
        return final_paths
    
    def get_uber_cost(self, A,B):
        return randint(0,9)
    
    def get_uber_time(self, A,B):
        return randint(0,9)
    
       
