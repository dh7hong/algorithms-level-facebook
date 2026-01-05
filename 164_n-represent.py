def solution(N, number):
    if N == number:
        return 1

    # dp[k] = numbers that can be made using k Ns
    dp = [set() for _ in range(9)]

    for k in range(1, 9):
        # Concatenated number (e.g., 5, 55, 555)
        dp[k].add(int(str(N) * k))

        for i in range(1, k):
            for a in dp[i]:
                for b in dp[k - i]:
                    dp[k].add(a + b)
                    dp[k].add(a - b)
                    dp[k].add(a * b)
                    if b != 0:
                        dp[k].add(a // b)

        if number in dp[k]:
            return k

    return -1
