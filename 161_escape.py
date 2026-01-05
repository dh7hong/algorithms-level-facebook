def solution(n, m, x, y, r, c, k):
    # Manhattan distance
    dist = abs(x - r) + abs(y - c)

    # Feasibility check
    if dist > k or (k - dist) % 2 != 0:
        return "impossible"

    # Direction order for lexicographical priority
    directions = [
        ('d', 1, 0),
        ('l', 0, -1),
        ('r', 0, 1),
        ('u', -1, 0)
    ]

    answer = []
    cx, cy = x, y
    remaining = k

    for _ in range(k):
        for ch, dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            # Check grid boundary
            if not (1 <= nx <= n and 1 <= ny <= m):
                continue

            # Remaining distance if we move here
            remaining_dist = abs(nx - r) + abs(ny - c)

            # Check if feasible
            if remaining_dist <= remaining - 1:
                answer.append(ch)
                cx, cy = nx, ny
                remaining -= 1
                break

    return ''.join(answer)
