import heapq

def solution(numbers):
    INF = 10**15

    keypad = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        0:(3,1)
    }

    # build distance table
    dist = [[INF]*10 for _ in range(10)]

    for s in range(10):
        pq = [(0, s)]
        dist[s][s] = 1

        while pq:
            cost, u = heapq.heappop(pq)
            if cost > dist[s][u]:
                continue

            x1, y1 = keypad[u]
            for v in keypad:
                if u == v:
                    continue
                x2, y2 = keypad[v]
                dx, dy = abs(x1-x2), abs(y1-y2)

                if dx+dy == 1:
                    w = 2
                elif dx == 1 and dy == 1:
                    w = 3
                else:
                    continue

                if dist[s][v] > cost + w:
                    dist[s][v] = cost + w
                    heapq.heappush(pq, (dist[s][v], v))

    dp = [[INF]*10 for _ in range(10)]
    dp[4][6] = 0

    for ch in numbers:
        t = int(ch)
        new_dp = [[INF]*10 for _ in range(10)]

        for l in range(10):
            for r in range(10):
                if dp[l][r] == INF:
                    continue
                cur = dp[l][r]

                # forced rules
                if l == t:
                    new_dp[l][r] = min(new_dp[l][r], cur + 1)
                elif r == t:
                    new_dp[l][r] = min(new_dp[l][r], cur + 1)
                else:
                    if t != r:
                        new_dp[t][r] = min(new_dp[t][r], cur + dist[l][t])
                    if t != l:
                        new_dp[l][t] = min(new_dp[l][t], cur + dist[r][t])

        dp = new_dp

    return min(min(row) for row in dp)
