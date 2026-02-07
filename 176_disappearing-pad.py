def solution(board, aloc, bloc):
    ROWS, COLS = len(board), len(board[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def in_range(r, c):
        return 0 <= r < ROWS and 0 <= c < COLS

    def dfs(ar, ac, br, bc, turn):
        """
        Returns (can_win, moves)
        turn = 0 -> A's turn
        turn = 1 -> B's turn
        """
        # Current player position
        cr, cc = (ar, ac) if turn == 0 else (br, bc)

        # If current position has no platform, current player already lost
        if board[cr][cc] == 0:
            return False, 0

        can_win = False
        min_win_moves = float('inf')
        max_lose_moves = 0

        for dr, dc in directions:
            nr, nc = cr + dr, cc + dc
            if not in_range(nr, nc) or board[nr][nc] == 0:
                continue

            # Move
            board[cr][cc] = 0
            if turn == 0:
                opp_can_win, moves = dfs(nr, nc, br, bc, 1)
            else:
                opp_can_win, moves = dfs(ar, ac, nr, nc, 0)
            board[cr][cc] = 1

            if not opp_can_win:
                can_win = True
                min_win_moves = min(min_win_moves, moves + 1)
            else:
                max_lose_moves = max(max_lose_moves, moves + 1)

        if can_win:
            return True, min_win_moves
        else:
            return False, max_lose_moves

    return dfs(aloc[0], aloc[1], bloc[0], bloc[1], 0)[1]
