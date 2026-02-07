def solution(n):
    MOD = 1000000007

    dp = [0] * (n + 1)
    h = [0, 0, 0]

    dp[0] = 1
    if n >= 1:
        dp[1] = 1
    if n >= 2:
        dp[2] = 3
    if n >= 3:
        dp[3] = 10

    for i in range(4, n + 1):
        dp[i] += dp[i - 1]
        dp[i] += dp[i - 2] * 2
        dp[i] += dp[i - 3] * 5
        dp[i] %= MOD

        h[(i - 4) % 3] = (h[(i - 4) % 3] + dp[i - 4]) % MOD

        dp[i] += (h[0] + h[1] + h[2]) * 2
        dp[i] += h[i % 3] * 2
        dp[i] %= MOD

    return dp[n]

# test cases
print(solution(3))  # actual output: 10
print(solution(4))  # actual output: 23
print(solution(5))  # actual output: 62
