# Dynamic Programming Solution for Travelling Salesman Problem 
# Time Complexity = O(n^2*2^n)

from sys import maxsize
from itertools import permutations

no_of_vertex = 4

def sales_man(graph, starting_point):
    vertex = []

    for i in range(4):
        if i != starting_point:
            vertex.append(i)
    min_path = maxsize

    next_permutation = permutations(vertex)

    for i in next_permutation:
        current_pathProfit = 0
        k = starting_point

        for j in i:
            current_pathProfit += graph[k][j]
            k = j
        current_pathProfit += graph[k][starting_point]
        min_path = min(min_path, current_pathProfit)
    
    return min_path

print("\nRUBAN GINO SINGH.A - URK20CS2001")
print("TRAVELLING SALES MAN PROBLEM - DYNAMMIC PROGRAMMING SOLUTION\n")

graph = eval(input("Enter a Graph: "))
# [[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
starting_point = int(input("Enter the starting point: "))

if starting_point >= 4: 
    print("Please enter starting point < 4!! Since no of vertex is 4")
else: 
    print("\n")
    print("The Taken Graph is: ", graph)
    print("The starting point is: ", starting_point)
    print("The Number of Vertex is: ", no_of_vertex)
    print("The best path that a sales man should take is: ", sales_man(graph, starting_point))    