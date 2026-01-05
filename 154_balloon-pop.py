def solution(a):
    n = len(a)
    
    # Arrays to track minimums from left and right
    left_min = [0] * n
    right_min = [0] * n

    # Build left minimums
    left_min[0] = a[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], a[i])

    # Build right minimums
    right_min[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        right_min[i] = min(right_min[i + 1], a[i])

    # Count balloons that can survive
    count = 0
    for i in range(n):
        if a[i] == left_min[i] or a[i] == right_min[i]:
            count += 1

    return count

print(solution([9, -1, -5]))  # Output: 3
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))  # Output: 6
print(solution([-36, -36, -36]))  # Output: 3