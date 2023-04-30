# Python program to implement Krushal Minimum Spanning Tree Algorithm

print("\nRUBAN GINO SINGH.A - URK20CS2001 | Kruskal Minimum Spanning Tree\n")

class Graph: 
    def __init__(self, vertices, arr): 
        self.V = vertices
        self.graph = arr

    def find(self, parent, i): 
        if parent[i] == i: 
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]: 
            parent[yroot] = xroot
        else: 
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self): 
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item:item[2])
        parent = []
        rank = []

        for node in range(self.V): 
            parent.append(node)
            rank.append(0)
        while e < self.V - 1: 
            u, v, w, = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y: 
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        minimumCost = 0

        print("\nEdges in the Constructed MST")

        for u, v, weight in result: 
            minimumCost += weight
            print("%d -> %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree: ", minimumCost)

vertex = int(input("Enter the Vertex size: "))
arr = eval(input("Enter the Graph: "))
g = Graph(vertex, arr)
g.KruskalMST() 

# [[0,1,10],[0,2,6],[0,3,5],[1,3,15],[2,3,4]]