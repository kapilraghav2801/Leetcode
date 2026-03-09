def coin_max_2D(coin,sum):
    
    n = len(coin)

    dp = [[0] * (sum + 1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1,n+1):
        for j in range(1, sum+1):
            if coin[i-1] <= j:
                dp[i][j]  = dp[i-1][j] + dp[i][j-coin[i-1]]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][sum]
coin = [2,5,3,6]
sum = 10
print(coin_max_2D(coin,sum))

def coin_max_1D(coin, sum):
    n = len(coin)

    dp = [0] * (sum + 1)
    dp[0] = 1

    for i in range(1, n+1):
        for j in range(1, sum + 1):
            if coin[i-1] <= j:
                dp[j] = dp[j] + dp[j - coin[i-1]]

    return dp[sum]

coin = [2,5,3,6]
sum = 10
print(coin_max_1D(coin,sum))












