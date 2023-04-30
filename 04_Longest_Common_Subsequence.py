# Dynamic Programming implementation of LCS Problem 

def LCS(string1, string2):
    m = len(string1)
    n = len(string2)

    arr = [[None]*(n+1) for i in range(m+1)] 

    for i in range(m+1): 
        for j in range(n+1):
            if i == 0 or j == 0:
                arr[i][j] = 0
            elif string1[i-1] == string2[j-1]:
                arr[i][j] = arr[i-1][j-1]+1
            else: 
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])

    return arr[m][n]

print("\nRUBAN GINO SINGH A - URK20CS2001")
print("LEAST COMMON SUBSEQUENCE\n")

string1 = input("Enter first String: ")
string2 = input("Enter second String: ")

print("Length of LCS is: ", LCS(string1, string2))