# code
import random

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.tempo = 0

class Vertice:
    def __init__(self, nome, vizinhos):
        self.d = None
        self.f = None
        self.color = None
        self.pai = None
        self.nome = nome
        self.vizinhos = vizinhos

def DFS_visit(G, vertice):
    G.tempo = G.tempo + 1
    vertice.d = G.tempo
    vertice.color = "GRAY"
    i = 0
    for existe in vertice.vizinhos:
        if existe == 1:
            vizinho = G.vertices[i]
            if vizinho.color == "WHITE":
                vizinho.pai = vertice
                DFS_visit(G, vizinho)
        i=i+1
    vertice.color = "BLACK"
    G.tempo = G.tempo + 1
    vertice.f = G.tempo
    
def DFS(G):
    for vertice in G.vertices:
        vertice.color = "WHITE"
        vertice.pai = None
    G.tempo = 0
    for vertice in G.vertices:
        if vertice.color == "WHITE":
            DFS_visit(G, vertice)

def imprimirMatriz(matriz):
    for x in matriz:
        print(x.nome, end= " ")
        print(x.d, end=" ")
        print(x.f, end=" ")
        print()
            

if __name__ == "__main__":
    n = 4
    # Exemplo Site IME
    # v0 = Vertice(0, [0,0,0,0,0,1,0,1])
    # v1 = Vertice(1, [0,0,0,0,0,1,0,0])
    # v2 = Vertice(2, [0,1,0,0,0,0,0,0])
    # v3 = Vertice(3, [0,0,0,0,1,0,1,0])
    # v4 = Vertice(3, [1,0,0,0,0,0,0,1])
    # v5 = Vertice(3, [0,0,1,0,0,0,0,1])
    # v6 = Vertice(3, [0,0,0,1,1,0,0,0])
    # v7 = Vertice(3, [1,0,0,0,0,0,0,0])

    # Exemplo Rennan
    v0 = Vertice("u", [0,1,0,1,0,0])
    v1 = Vertice("v", [0,0,0,0,1,0])
    v2 = Vertice("w", [0,0,0,0,1,1])
    v3 = Vertice("x", [0,1,0,0,0,0])
    v4 = Vertice("y", [0,0,0,1,0,0])
    v5 = Vertice("z", [0,0,0,0,0,1])

    g = Grafo([v0,v1,v2,v3,v4,v5])
    DFS(g)

    print(v0.d)
    print(v0.f)


    # imprimirMatriz(g.vertices)
    