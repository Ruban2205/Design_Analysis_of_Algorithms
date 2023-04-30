# Dynamic Programming solution for 0/1 Knapsack problem 
# Time complexity of 0/1 Knapsack problem is O(nW) where, n is the number of items and W is the capacity of knapsack. where each entry requires θ(1) time to compute.

def zero_one_knapsack(capacity, weight, profit, n):
    dp = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1): 
        for j in range(capacity + 1): 
            
            if i == 0 or j == 0: 
                dp[i][j] = 0
                

            elif weight[i-1] <= j:
                dp[i][j] = max(profit[i-1] + dp[i-1][j-weight[i-1]], dp[i-1][j])

            else: 
                dp[i][j] = dp[i-1][j]

    return dp[n][j]

print("\nDYNAMIC PROGRAMMING - 0/1 KNAPSACK PROBLEM")
print("RUBAN GINO SINGH.A\n")
weight = list(map(int, input("Weight: ").split()))
profit = list(map(int, input("Profit: ").split()))
capacity = int(input("Capacity: "))
n = len(profit)
print("Maximum KnapSack Value: ", zero_one_knapsack(capacity, weight, profit, n))