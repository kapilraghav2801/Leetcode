def lcs(X, Y, n, m):

    # Base Condition
    if n == 0 or m == 0:
        return 0

    # Choice diagram
    if X[n-1] == Y[m-1]:
        return 1 + lcs(X, Y, n-1, m-1)

    else:
        return max(
            lcs(X, Y, n-1, m),
            lcs(X, Y, n, m-1)
        )
lcs("abcde", "ace", 5, 3)

#Memoization

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp =[[-1] * (m + 1) for _ in range(n+1)]

        def lcs(text1, text2, n, m):
            if n == 0 or m  == 0:
                return 0

            if dp[n][m] != -1:
                return dp[n][m]
            
            if text1[n-1] == text2[m-1]:
                dp[n][m] = 1 + lcs(text1, text2, n-1, m-1)

            else:
                dp[n][m] = max(
                    lcs(text1, text2, n-1, m),
                    lcs(text1, text2, n, m-1)
                )
            return dp[n][m]

        return lcs(text1, text2, n, m)

#Bottom Up
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [[0] * (m+1) for _ in range(n+1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]

                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]
