def solution(n, times):
    # 1. Search range
    left = 1
    right = max(times) * n  # worst case: slowest immigration officer handles everyone
    answer = right

    # 2. Binary search
    while left <= right:
        mid = (left + right) // 2  # candidate time

        # 3. Count how many people can be processed in 'mid' time
        people = 0
        for t in times:
            people += mid // t

        # 4. Check feasibility
        if people >= n:
            answer = mid      # mid is sufficient, try smaller time
            right = mid - 1
        else:
            left = mid + 1    # mid is insufficient, need more time

    return answer

print(solution(6, [7, 10]))
