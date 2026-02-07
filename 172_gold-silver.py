def solution(a, b, g, s, w, t):
    # Binary search range:
    # minimum time = 0
    # maximum time = very large value (safe upper bound)
    left, right = 0, 10**15
    answer = right

    # Binary search on time
    while left <= right:
        mid = (left + right) // 2  # candidate time

        # Total amount deliverable within 'mid' time
        total_gold = 0
        total_silver = 0
        total_combined = 0  # gold + silver together

        # Check each city's contribution
        for i in range(len(g)):
            # One round trip takes 2 * t[i]
            trip_time = 2 * t[i]

            # Number of full round trips possible
            trips = mid // trip_time

            # If remaining time allows one extra one-way trip
            if mid % trip_time >= t[i]:
                trips += 1

            # Maximum weight transportable from this city
            max_transport = trips * w[i]

            # Gold and silver that can be delivered individually
            gold = min(g[i], max_transport)
            silver = min(s[i], max_transport)

            total_gold += gold
            total_silver += silver

            # Total minerals (gold + silver) that can be delivered
            total_combined += min(g[i] + s[i], max_transport)

        # Check if requirements are satisfied
        if total_gold >= a and total_silver >= b and total_combined >= a + b:
            answer = mid          # feasible -> try smaller time
            right = mid - 1
        else:
            left = mid + 1        # not feasible -> need more time

    return answer
