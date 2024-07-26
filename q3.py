def knapsack(w,wt,val,n):
    dp=[0]*(w+1)
    for i in range(n):
        for we in range(w,wt[i]-1,-1):
            if wt[i]<=we:
                dp[we]=max(dp[we],dp[we-wt[i]]+val[i])
    return dp[w]

weights = [1, 2, 3]
values = [10, 15, 40]
capacity = 6
n=len(values)
print(knapsack(capacity,weights,values,n))