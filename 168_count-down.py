def solution(target):
    INF = 10**9

    # All possible dart throws: (score, is_single_or_bull)
    throws = []

    # Singles
    for i in range(1, 21):
        throws.append((i, 1))

    # Doubles
    for i in range(1, 21):
        throws.append((2 * i, 0))
 
    # Triples
    for i in range(1, 21):
        throws.append((3 * i, 0))

    # Bull
    throws.append((50, 1))

    # dp[s] = (min_darts, max_single_or_bull)
    dp = [(INF, 0)] * (target + 1)
    dp[0] = (0, 0)

    for s in range(1, target + 1):
        for score, single_cnt in throws:
            if s - score >= 0:
                prev_darts, prev_singles = dp[s - score]
                cand = (prev_darts + 1, prev_singles + single_cnt)

                if cand[0] < dp[s][0]:
                    dp[s] = cand
                elif cand[0] == dp[s][0] and cand[1] > dp[s][1]:
                    dp[s] = cand

    return list(dp[target])
