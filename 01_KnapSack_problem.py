# Fractional Knapsack problem using greedy technique
# The time complexity of the fractional knapsack problem is O(NlogN)

class Objects: 
    def __init__(self, weight, profit): 
        self.weight = weight
        self.profit = profit 
        self.ratio = profit / weight

    def __lt__(self, other):
        return self.ratio < other.ratio

class fractionalKnapsack: 
    def maxValue(weight, profit, capacity): 
        value = []
        for i in range(len(weight)): 
            value.append(Objects(weight[i], profit[i]))

        value.sort(reverse=True)

        totalValue = 0
        
        for i in value: 
            crtWeight = int(i.weight)
            crtProfit = int(i.profit)
            if capacity - crtWeight >= 0: 
                capacity -= crtWeight
                totalValue += crtProfit
            else: 
                fraction = capacity/crtWeight
                totalValue += crtProfit * fraction
                capacity = int(capacity - crtWeight * fraction)
                break
        return totalValue

if __name__ == "__main__": 
    print("\nRUBAN GINO SINGH A URK20CS2001 - Fractional Knapsack")
    wt = list(map(int, input("Weight: ").split()))
    pro = list(map(int, input("Profit: ").split()))
    cap = int(input("Enter the capacity: "))

    print("Fractional KnapSack Value: ", fractionalKnapsack.maxValue(wt,pro,cap))
