from parser import parser
import heapq

pars = parser()
pars.parser()
pars.assing_connection()
# distance = {}
# for i in pars.hubs:
#     if i.is_start:
#         distance[i.name] = 0
#     else:
#         distance[i.name]= float("inf")
# print(distance)
class graph:
    def build_graph(self , other):
        graph = {}
        for i in other.hubs:
            graph[i] = i.connection.neigh
        return graph


g = graph()
# print(g.build_graph(pars))

class path_finding():

    def __init__(self, g):
        self.graph = g.build_graph(pars)
        self.i = 0
    def c(self):
        self.i +=1
        return self.i  
    def find_parent(self, target , parents):
        path  = []
        node = target
        while node is not None:
            path.append(node)
            node = parents[node]
        path.reverse()
        return path

    def dijkstra(self, start, end):
        distance = pars.calcule_distance()
        parent = {}
        queue = [(0,self.c(), start)]
        parent [start] = None
        while queue:
            dis , _, hub = heapq.heappop(queue)
            for neigh in self.graph[hub]:
                new_cost = neigh.cost
                new_dis = dis + new_cost
                if new_dis < distance[neigh]:
                    parent[neigh] = hub
                    distance[neigh] = new_dis
                    heapq.heappush(queue, (new_dis,self.c(), neigh))
        if distance[end] == float("inf"):
            return None
        return self.find_parent(end, parent)     
    
        
path = path_finding(g)

print(path.dijkstra(pars.hubs[0], pars.hubs[4]))