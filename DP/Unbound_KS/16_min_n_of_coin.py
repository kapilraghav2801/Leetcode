def min_coin(coin, sum):
    n = len(coin)
    INF = float('inf')
    dp = [[INF] * (sum + 1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 0

    for i in range(1,n+1):
        for j in range(1,sum+1):
            if coin[i-1] <= j:
                dp[i][j] = min(dp[i-1][j], dp[i][j-coin[i-1]] + 1)
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][sum] if dp[n][sum] != INF else -1
    
coin = [1,2,3]
sum = 5
print(min_coin(coin,sum)) 


def coin_min_1D(coin, sum):
    n = len(coin)
    INF = float('inf')

    dp = [INF] * (sum + 1)
    dp[0] = 0

    for i in range(1, n+1):
        for j in range(1, sum + 1):
            if coin[i-1] <= j:
                dp[j] = min(dp[j], dp[j-coin[i-1]] + 1)

    return dp[sum] if dp[sum] != INF else -1

coin = [2,5,3,6]
sum = 10
print(coin_min_1D(coin,sum))


def min_pf_coins_AV(coin,sum):
    n = len(coin)
    INF = float('inf')
    dp = [[INF] * (sum+1) for _ in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 0

    for j in range(1,sum+1):
        if j % coin[0] == 0 :
            dp[1][j] = j // coin[0]

    for i in range(2, n+1):
        for j in range(1, sum+1):
            if coin[i-1] <= j:
                dp[i][j]  = min(dp[i-1][j], 1 + dp[i][j-coin[i-1]])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][sum]

coin = [1,2,3]
sum = 5
print(min_pf_coins_AV(coin,sum))



