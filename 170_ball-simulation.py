def solution(n, m, x, y, queries):
    # Initial possible range - only the final position
    r1 = r2 = x
    c1 = c2 = y

    # Process queries in reverse order
    for command, dx in reversed(queries):
        if command == 0:  # original: move left -> reverse: move right
            c2 = min(m - 1, c2 + dx)
            if c1 != 0:
                c1 += dx
        elif command == 1:  # original: move right -> reverse: move left
            c1 = max(0, c1 - dx)
            if c2 != m - 1:
                c2 -= dx
        elif command == 2:  # original: move up -> reverse: move down
            r2 = min(n - 1, r2 + dx)
            if r1 != 0:
                r1 += dx
        elif command == 3:  # original: move down -> reverse: move up
            r1 = max(0, r1 - dx)
            if r2 != n - 1:
                r2 -= dx

        # If the range is invalid, no possible starting point
        if r1 > r2 or c1 > c2:
            return 0

    # Number of valid starting positions
    return (r2 - r1 + 1) * (c2 - c1 + 1)
