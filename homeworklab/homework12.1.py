def count_ways(n):
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        if i % 3 == 0:
            dp[i] += dp[i // 3]

    return dp[n]


n = 10  # change number
ways = count_ways(n)
print(ways)