# Job Scheduling/Sequencing problem Using Greedy Technique
# The time complexity of this problem is O(n^2).

def JobScheduling(job, dline, profit, maxTime):
    
    n = len(job)

    for i in range(n):
        for k in range(n - 1 - i):
            if profit[k] < profit[k + 1]:
                profit[k], profit[k + 1] = profit[k + 1], profit[k]
                job[k], job[k + 1] = job[k + 1], job[k]
                dline[k], dline[k + 1] = dline[k + 1], dline[k]

    slot = [False] * maxTime
    OrgJob = ['-1'] * maxTime
    max_profit = 0 

    for i in range(n):
        for k in range(dline[i] - 1, -1, -1):
            if slot[k] is False: 
                slot[k] = True
                OrgJob[k] = job[i]
                max_profit += profit[i]
                break

    print("\nMaximum Profit: ", max_profit)
    print(OrgJob)

print("\nJOB SCHEDULING ALGORITHM - RUBAN GINO SINGH A URK20CS2001")

no_of_jobs = int(input("Enter the no of jobs: "))
job = list(map(chr, range(97, 97 + no_of_jobs)))
profit = list(map(int, input("\nEnter the profits: ").strip().split()))[:no_of_jobs]
dline = list(map(int, input("\nEnter the Deadlines: ").strip().split()))[:no_of_jobs]

JobScheduling(job, dline, profit, max(dline))