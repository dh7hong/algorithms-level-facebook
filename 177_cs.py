import heapq
from math import inf

def solution(k, n, reqs):
    # Group requests by type (1..k)
    by_type = [[] for _ in range(k + 1)]
    for a, b, c in reqs:
        by_type[c].append((a, b))  # already sorted by a globally, still fine per type

    # Precompute waiting cost for each type with m mentors
    # wait_cost[t][m] valid for m=1..n (we'll only use feasible m)
    wait_cost = [[0] * (n + 1) for _ in range(k + 1)]

    def simulate(type_requests, m):
        """Return total waiting time for this type if it has m mentors."""
        heap = []  # mentor availability times (end times)
        total_wait = 0

        for a, b in type_requests:
            if len(heap) < m:
                # a mentor is free (not yet all mentors used)
                heapq.heappush(heap, a + b)
            else:
                earliest_end = heapq.heappop(heap)
                if earliest_end <= a:
                    # mentor becomes free before request -> no wait
                    start = a
                else:
                    # must wait
                    total_wait += earliest_end - a
                    start = earliest_end
                heapq.heappush(heap, start + b)

        return total_wait

    for t in range(1, k + 1):
        for m in range(1, n + 1):
            wait_cost[t][m] = simulate(by_type[t], m)

    # DP: distribute n mentors across k types, each >= 1
    # dp[i][j] = min wait using first i types with total j mentors
    dp = [[inf] * (n + 1) for _ in range(k + 1)]
    dp[0][0] = 0

    for i in range(1, k + 1):
        for total in range(1, n + 1):
            # assign m mentors to type i (at least 1)
            # remaining mentors go to first i-1 types
            for m in range(1, total + 1):
                if dp[i - 1][total - m] == inf:
                    continue
                dp[i][total] = min(dp[i][total], dp[i - 1][total - m] + wait_cost[i][m])

    # But we must ensure each type has at least 1 mentor:
    # dp formulation already enforces m>=1 for each type, because i starts at 1 and uses m>=1.
    # We need exactly n mentors total:
    return dp[k][n]

print(solution(2, 4, [[0, 5, 1], [1, 2, 1], [1, 3, 2], [3, 2, 1]]))  # expected output: 0
print(solution(3, 5, [[0, 3, 1], [1, 9, 2], [2, 6, 3], [3, 1, 1], [10, 2, 2]]))  # expected output: 0
print(solution(1, 3, [[0, 10, 1], [2, 5, 1], [5, 2, 1]]))  # expected output: 0
print(solution(2, 3, [[0, 3, 1], [1, 9, 2], [2, 6, 1], [3, 1, 2]]))  # expected output: 1
print(solution(4, 6, [[0, 2, 1], [1, 2, 2], [2, 2, 3], [3, 2, 4], [4, 2, 1], [5, 2, 2]]))  # expected output: 0
