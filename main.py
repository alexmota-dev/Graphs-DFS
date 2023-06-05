# code
import random

 
class Graph:
    def __init__(self, v):
        self.tempo = 0
        self.traversal_array = []
        self.v = v
        # numero de arestas
        # self.e = random.randint((self.v-1), 45)
        self.e = random.randint(self.v-1,self.v*(self.v-1)/2)
        # list de adjacencia
        self.grafo_lista = [[] for _ in range(v)]
        # matrix de adjacencia
        self.grafo_matrix = [[0 for _ in range(v)] for _ in range(v)]
 
    # function to create random graph
    def create_random_graph(self):
        # adicionar arestas até e
        for i in range(self.e):
            # Escolha src e dest de cada aresta aleatoriamente
            src = random.randrange(0, self.v)
            dest = random.randrange(0, self.v)
            # reescolha se src e dest são iguais ou src e dest já tem uma vantagem
            while src == dest and self.grafo_matrix[src][dest] == 1:
                src = random.randrange(0, self.v)
                dest = random.randrange(0, self.v)
            # adicionar a aresta ao gráfico
            self.grafo_lista[src].append(dest)
            self.grafo_matrix[src][dest] = 1
 
    # function for dfs
    def dfs(self):
        print(self)
        self.visited = [False]*self.v
        self.d = [0]*self.v
        self.f = [0]*self.v
 
        for node in range(self.v):
            if not self.visited[node]:
                self.traverse_dfs(node)
        print()
        print("Grafo Lista: ", self.grafo_lista)
        print()
        imprimirMatriz(self.grafo_matrix)
        print()
        print("DFS Traversal: ", self.traversal_array)
        print("O grafo tem", self.e, " arestas")
        print()
 
    def traverse_dfs(self, node):
        # marcando o node como visitado
        self.visited[node] = True
        # adicionando o node ao traversal
        self.traversal_array.append(node)
        # pegando o tempo de descobrimento
        self.d[node] = self.tempo
        # incremento o tempo em +1
        self.tempo += 1
        # passando pelos vizinhos
        for neighbour in self.grafo_lista[node]:
            # se um nó não for visitado
            if not self.visited[neighbour]:
                # marca a borda como borda de árvore
                print('Tree Edge:', str(node)+'-->'+str(neighbour))
                self.traverse_dfs(neighbour)
            else:
                if self.d[node] == self.d[neighbour] and self.f[node] == self.f[neighbour]:
                    print('Cross Edge:', str(node)+'-->'+str(neighbour))
                # when the parent node is traversed after the neighbour node
                # quando o nó pai é atravessado após o nó vizinho
                # neighbour é ancestral de node
                if self.d[node] > self.d[neighbour] and self.f[node] < self.f[neighbour]:
                    print('Back Edge:', str(node)+'-->'+str(neighbour))
                # when the neighbour node is a descendant but not a part of tree
                # quando o nó vizinho é descendente, mas não faz parte da árvore
                # neighbour é descendente de node
                elif self.d[node] < self.d[neighbour] and self.f[node] > self.f[neighbour]:
                    print('Forward Edge:', str(node)+'-->'+str(neighbour))
                # when parent and neighbour node do not have any ancestor and a descendant relationship between them
                # quando pai e nó vizinho não têm nenhum ancestral e uma relação descendente entre eles
                # node e neighbour são primos
                elif self.d[node] > self.d[neighbour] and self.f[node] > self.f[neighbour]:
                    print('Cross Edge:', str(node)+'-->'+str(neighbour))
            self.f[node] = self.tempo
            self.tempo += 1
 
def imprimirMatriz(matriz):
    for i in matriz:
        for x in i:
            print(x, end=", ")
        print()
if __name__ == "__main__":
    n = 4
    # grafoTeste = [[1,2,3],[4,5,6]]
    # imprimirMatriz(grafoTeste)
    g = Graph(n)
    g.create_random_graph()
    g.dfs()