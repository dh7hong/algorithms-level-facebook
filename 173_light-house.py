import sys
sys.setrecursionlimit(10**7)

def solution(n, lighthouse):
    # Build adjacency list
    graph = [[] for _ in range(n + 1)]
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)

    # dp[u][0]: u is OFF
    # dp[u][1]: u is ON
    dp = [[0, 0] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    def dfs(u):
        visited[u] = True
        dp[u][1] = 1  # u is ON

        for v in graph[u]:
            if not visited[v]:
                dfs(v)

                # If u is OFF, v must be ON
                dp[u][0] += dp[v][1]

                # If u is ON, v can be ON or OFF
                dp[u][1] += min(dp[v][0], dp[v][1])

    # Run DFS from node 1 (tree is connected)
    dfs(1)

    return min(dp[1][0], dp[1][1])
