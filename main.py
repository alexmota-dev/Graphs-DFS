# code
import random
 
 
class Graph:
    def __init__(self, v):
        self.tempo = 0
        self.traversal_array = []
        self.v = v
        # numero de arestas
        # self.e = random.randint((self.v-1), 45)
        self.e = 9
        # list de adjacencia
        self.grafo_lista = [[] for _ in range(v)]
        # matrix de adjacencia
        self.grafo_matrix = [[0 for _ in range(v)] for _ in range(v)]
 
    # function to create random graph
    def create_random_graph(self):
        # adicionar arestas até e
        for i in range(self.e):
            # choose src and dest of each edge randomly
            src = random.randrange(0, self.v)
            dest = random.randrange(0, self.v)
            # re-choose if src and dest are same or src and dest already has an edge
            while src == dest and self.grafo_matrix[src][dest] == 1:
                src = random.randrange(0, self.v)
                dest = random.randrange(0, self.v)
            # add the edge to graph
            self.grafo_lista[src].append(dest)
            self.grafo_matrix[src][dest] = 1
 
    # function for dfs
    def dfs(self):
        self.visited = [False]*self.v
        self.d = [0]*self.v
        self.f = [0]*self.v
 
        for node in range(self.v):
            if not self.visited[node]:
                self.traverse_dfs(node)
        print()
        print("DFS Traversal: ", self.traversal_array)
        print()
 
    def traverse_dfs(self, node):
        # mark the node visited
        self.visited[node] = True
        # add the node to traversal
        self.traversal_array.append(node)
        # get the starting time
        self.d[node] = self.tempo
        # increment the time by 1
        self.tempo += 1
        # traverse through the neighbours
        for neighbour in self.grafo_lista[node]:
            # if a node is not visited
            if not self.visited[neighbour]:
                # marks the edge as tree edge
                print('Tree Edge:', str(node)+'-->'+str(neighbour))
                # dfs from that node
                self.traverse_dfs(neighbour)
            else:
                # when the parent node is traversed after the neighbour node
                if self.d[node] > self.d[neighbour] and self.f[node] < self.f[neighbour]:
                    print('Back Edge:', str(node)+'-->'+str(neighbour))
                # when the neighbour node is a descendant but not a part of tree
                elif self.d[node] < self.d[neighbour] and self.f[node] > self.f[neighbour]:
                    print('Forward Edge:', str(node)+'-->'+str(neighbour))
                # when parent and neighbour node do not have any ancestor and a descendant relationship between them
                elif self.d[node] > self.d[neighbour] and self.f[node] > self.f[neighbour]:
                    print('Cross Edge:', str(node)+'-->'+str(neighbour))
            self.f[node] = self.tempo
            self.tempo += 1
 
 
if __name__ == "__main__":
    n = 5
    g = Graph(n)
    g.create_random_graph()
    g.dfs()