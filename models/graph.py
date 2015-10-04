from operator import itemgetter
import node
import path
import location
import Queue

class Graph:
   
    input_data = []
    
    
    def __init__(self, location_A, location_B):
        self.A = Node('A', 'user', location_A) 
        self.B = Node('B', 'user', location_B)
        
        self.uber_cost = get_uber_cost(location_A, location_B)
        self.uber_time = get_uber_time(location_A, location_B)
        pt_nodes = input_data
        my_graph = []
        for pt_node in pt_nodes: 
            a_cost = get_uber_cost(location_A, pt_node.location)
            if ( a_cost > uber_cost ):
                break
            b_cost = get_uber_cost(pt_node.location, location_B)
            if( b_cost > uber_cost ):
                break
            a_time = get_uber_time(location_A, pt_node.location)
            b_time = get_uber_time(pt_node.location, location_B)
            A.add_edge(pt_node, a_cost, a_time)
            pt_node.add_edge(B, b_cost, b_time)
            #ps this isn't going to work
            my_graph[pt_node.location] = {'node': pt_node, 'b_time':b_time}
        
        for this in list(my_graph.values()):
            for that in this['node'].edges:
                if this['b_time'] < my_graph[that['destination'].location]['b_time']:
                    #this is closer to b so you should never go to that after this
                    this['node'].edges.remove(that)                    
    
    def get_paths(self):
        all_paths = Queue.Queue()
        all_paths.put(Path([self.A]))
        final_paths = []
        
        while not all_paths.empty():
            path = all_paths.get()
            if ( path.last_node == self.B ):
                final_paths.append(path)
                break
            for edge in path.last_node.edges:
                if ( path.cost + edge['cost'] < self.uber_cost ):
                    all_paths.append(Path(path.nodes.append(edge['node']), path.cost + edge['cost']))
            all_paths.put(p)
        
        return final_paths

3. Find all paths on the graph that cost less than *uber*
    i. Recursive alg: to start, path =  {A}. After, node is next path ? in queue (?)
        (base case): node == B --> add path to list of final paths
        (else case): 
            a. get all of node's outbound edges
            b. for each edge
                if ( pathCost + edge.cost < uberCost ) --> add a new path to the queue that is current path + edge'

    
    def get_uber_cost(A, B):
        return 3
    
    def get_uber_time(A,B):
        return 7
    
       
