from itertools import product

def solution(clockHands):
    n = len(clockHands)
    INF = 10**9

    # Directions: self + 4-neighbors
    dirs = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]

    def apply(board, r, c, times):
        """Rotate (r,c) and its neighbors 'times' times (mod 4)."""
        if times % 4 == 0:
            return
        t = times % 4
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n:
                board[nr][nc] = (board[nr][nc] + t) % 4

    best = INF

    # Enumerate all possible rotation counts (0..3) for the first row
    for first_row_moves in product(range(4), repeat=n):
        board = [row[:] for row in clockHands]
        moves = 0

        # Apply first row decisions
        for c in range(n):
            t = first_row_moves[c]
            moves += t
            apply(board, 0, c, t)

        # For each next row, force the row above to become 0
        for r in range(1, n):
            for c in range(n):
                # board[r-1][c] needs to become 0
                need = (-board[r-1][c]) % 4
                moves += need
                apply(board, r, c, need)

        # Check if last row is all zeros
        if all(board[n-1][c] == 0 for c in range(n)):
            best = min(best, moves)

    return best
# test cases
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))  # expected output: 0
print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))  # expected output: 23
print(solution([[3, 2, 1], [2, 1, 0], [1, 0, 3]]))  # expected output: 23
print(solution([[0, 3, 0], [3, 0, 3], [0, 3, 0]]))  # expected output: 12
print(solution([[1, 2, 3], [0, 1, 2], [3, 0, 1]]))  # expected output: 23