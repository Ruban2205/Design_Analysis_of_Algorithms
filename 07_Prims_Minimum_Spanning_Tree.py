# Python program to implement Prim's Minimum Spanning Tree Algorithm. 

import sys

class Graph(): 
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")

        cost = 0
        for i in range(1, self.vertices):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
            cost += self.graph[i][parent[i]]

        print("\nTotal Minimum Cost is: ", cost)

    def minKey(self, key, mstSet): 
        minimum = sys.maxsize

        for v in range(self.vertices):
            if key[v] < minimum and mstSet[v] == False: 
                minimum = key[v]
                min_index = v
        return min_index

    def primMST(self):
        key = [sys.maxsize] * self.vertices
        parent = [None] * self.vertices
        key[0] = 0
        mstSet = [False] * self.vertices

        parent[0] = -1

        for cout in range(self.vertices):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.vertices):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

print("\nRUBAN GINO SINGH.A - URK20CS2001\nPRIM'S ALGORITHM FOR MINIMUM SPANNING TREE\n")

vertex = int(input("Enter the Vertex size: "))
MST = Graph(vertex)
MST.graph = eval(input("Enter the values: "))
print()
MST.primMST()

# [[0,2,0,6,0],[2,0,3,8,5],[0,3,0,0,7],[6,8,0,0,9],[0,5,7,9,0]]