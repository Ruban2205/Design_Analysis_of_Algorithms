# Floyd's All pair shortest path algorithm 

print("\nRUBAN GINO SINGH.A - URK20CS2001 | Floyd's All pair Shortest Path Algorithm\n")

INF = float('inf')
def printmatrix(m):
    row, column = len(m), len(m[0])

    for i in range(row):
        for j in range(column):
            print(m[i][j], end=" ")
        print()

vertices, edges = map(int, input("\nEnter the number of Vertices and Edges: ").split())
m=[[None]*vertices for i in range(vertices)]

for i in range(vertices):
    for j in range(vertices): 
        if i == j: 
            m[i][j] = 0
        else: 
            m[i][j] = INF

print()

for i in range(edges):
    source, destination, weight = map(int, input("Enter Source, Destination and Weight: ").split())
    m[source][destination] = weight

print("\nMatrix 1: ")
printmatrix(m)

print("\n----------\n")

for k in range(vertices):
    for i in range(vertices):
        for j in range(vertices):
            if m[i][k] + m[k][j] < m[i][j]:
                m[i][j] = m[i][k] + m[k][j]
print("Matrix 2: ")
printmatrix(m)




# Enter the number of Vertices and Edges: 4 7

# Enter Source, Destination and Weight: 0 2 3
# Enter Source, Destination and Weight: 0 3 7
# Enter Source, Destination and Weight: 1 2 2
# Enter Source, Destination and Weight: 1 0 8
# Enter Source, Destination and Weight: 2 0 5
# Enter Source, Destination and Weight: 2 3 1
# Enter Source, Destination and Weight: 3 0 2

# Matrix 1:
# 0 inf 3 7
# 8 0 2 inf
# 5 inf 0 1
# 2 inf inf 0

# ----------

# Matrix 2:
# 0 inf 3 4 
# 5 0 2 3
# 3 inf 0 1
# 2 inf 5 0