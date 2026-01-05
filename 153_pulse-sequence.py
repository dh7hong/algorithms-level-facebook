def solution(sequence):
    # We will track two cases:
    # 1) pulse starts with +1
    # 2) pulse starts with -1

    max_sum = 0

    cur1 = 0  # current max subarray sum for pulse starting with +1
    cur2 = 0  # current max subarray sum for pulse starting with -1

    for i, val in enumerate(sequence):
        # Apply pulse
        if i % 2 == 0:
            p1 = val        # +1 pulse
            p2 = -val       # -1 pulse
        else:
            p1 = -val
            p2 = val

        # Kadane's algorithm
        cur1 = max(p1, cur1 + p1)
        cur2 = max(p2, cur2 + p2)

        max_sum = max(max_sum, cur1, cur2)

    return max_sum

print(solution([1, -2, 3, -4, 5]))  # Example usage
print(solution([-1, -2, -3, -4]))  # Example usage