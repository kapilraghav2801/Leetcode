def count_subset(arr,sum):
    n = len(arr)

    dp = [[0] * (sum+1) for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if arr[i-1] <= j:
                dp[i][j]  = dp[i-1][j] + dp[i-1][j-arr[i-1]]

            else:
                dp[i][j] = dp[i-1][j]


    return dp[n][sum]

# arr = [2,3,5,6,8,10]
# sum = 10
arr = [1,1,1,1]
sum = 2

print(count_subset(arr,sum))