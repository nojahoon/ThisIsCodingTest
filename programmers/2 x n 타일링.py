def solution(n):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    dp[1] = 2

    if n == 1:
        return dp[0]
    elif n == 2:
        return dp[1]
    else:
        for i in range(2, n):
            dp[i] = (dp[i - 2] + dp[i - 1]) % 1000000007
        return dp[n - 1]