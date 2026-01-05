from collections import Counter

def solution(a):
    freq = Counter(a)
    max_length = 0

    for k, cnt in freq.items():
        # Pruning: cannot beat current max
        if cnt * 2 <= max_length:
            continue

        pairs = 0
        i = 0
        n = len(a)

        while i < n - 1:
            # Check if we can form a valid pair with k
            if (a[i] == k and a[i+1] != k) or (a[i] != k and a[i+1] == k):
                pairs += 1
                i += 2
            else:
                i += 1

        max_length = max(max_length, pairs * 2)

    return max_length
