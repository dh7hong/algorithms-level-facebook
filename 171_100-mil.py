def solution(e, starts):
    # Step 1: Count divisors for each number
    div_count = [0] * (e + 1)
    for i in range(1, e + 1):
        for j in range(i, e + 1, i):
            div_count[j] += 1

    # Step 2: Precompute best number from i to e
    best = [0] * (e + 2)
    best[e] = e

    for i in range(e - 1, 0, -1):
        if div_count[i] >= div_count[best[i + 1]]:
            best[i] = i
        else:
            best[i] = best[i + 1]

    # Step 3: Answer queries
    return [best[s] for s in starts]
