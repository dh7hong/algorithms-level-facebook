def solution(temperature, t1, t2, a, b, onboard):
    INF = 10**15
    n = len(onboard)

    # Temperature bounds in constraints
    MIN_T, MAX_T = -10, 40
    SIZE = MAX_T - MIN_T + 1

    def idx(temp):
        return temp - MIN_T

    def in_range(temp, time):
        if onboard[time] == 1:
            return t1 <= temp <= t2
        return True

    outdoor = temperature

    # dp for current minute
    dp = [INF] * SIZE
    start = outdoor  # indoor at time 0 equals outdoor
    if not in_range(start, 0):
        # problem guarantees solvable, so this shouldn't happen
        return -1
    dp[idx(start)] = 0

    for time in range(n - 1):
        ndp = [INF] * SIZE

        for temp in range(MIN_T, MAX_T + 1):
            cur_cost = dp[idx(temp)]
            if cur_cost == INF:
                continue
            if not in_range(temp, time):
                continue

            # 1) AC OFF: move 1 step toward outdoor
            if temp < outdoor:
                nxt = temp + 1
            elif temp > outdoor:
                nxt = temp - 1
            else:
                nxt = temp
            if in_range(nxt, time + 1):
                ndp[idx(nxt)] = min(ndp[idx(nxt)], cur_cost)

            # 2) AC ON HOLD: keep same temperature, cost b
            nxt = temp
            if in_range(nxt, time + 1):
                ndp[idx(nxt)] = min(ndp[idx(nxt)], cur_cost + b)

            # 3) AC ON MOVE: change by +1 or -1, cost a
            for nxt in (temp - 1, temp + 1):
                if MIN_T <= nxt <= MAX_T and in_range(nxt, time + 1):
                    ndp[idx(nxt)] = min(ndp[idx(nxt)], cur_cost + a)

        dp = ndp

    # answer: min cost among valid temps at last time
    ans = INF
    last = n - 1
    for temp in range(MIN_T, MAX_T + 1):
        if in_range(temp, last):
            ans = min(ans, dp[idx(temp)])
    return ans
# test cases
print(solution(28,18,26,10,8,[0,0,1,1,1,1,1]))  # expected output: 40