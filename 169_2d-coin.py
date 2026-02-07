def solution(beginning, target):
    R, C = len(beginning), len(beginning[0])
    INF = 10**9
    answer = INF

    # Try all subsets of row flips
    for mask in range(1 << R):
        row_flip = [0] * R
        for r in range(R):
            if mask & (1 << r):
                row_flip[r] = 1

        col_flip = [0] * C
        valid = True

        for c in range(C):
            # Decide whether to flip column c based on row 0
            expected = beginning[0][c] ^ row_flip[0]
            if expected != target[0][c]:
                col_flip[c] = 1

            # Check consistency for all rows
            for r in range(R):
                current = beginning[r][c] ^ row_flip[r] ^ col_flip[c]
                if current != target[r][c]:
                    valid = False
                    break
            if not valid:
                break

        if valid:
            answer = min(answer, sum(row_flip) + sum(col_flip))

    return answer if answer != INF else -1
