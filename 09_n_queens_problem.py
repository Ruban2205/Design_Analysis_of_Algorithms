# N Queens Problem - Python Implementation

print("\nRUBAN GINO SINGH.A - URK20CS2001 -- N Queens Algorithm\n")

N = int(input("Enter the Number of Queens: "))
board = [[0]*N for i in range(N)]

def is_queen(i, j):
    for k in range(0, N):
        if board[i][k] == 1 or board[k][j] == 1:
            return True

    for k in range(0, N):
        for l in range(0, N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False

def queen(n):
    if n == 0: 
        return True
    
    for i in range(0, N):
        for j in range(0, N):
            if (not(is_queen(i, j))) and (board[i][j] != 1):
                board[i][j] = 1
                if queen(n-1) == True: 
                    return True
                board[i][j] = 0
    return False
queen(N)

for i in board:
    print(i)