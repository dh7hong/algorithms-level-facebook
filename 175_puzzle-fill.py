from collections import deque

def solution(game_board, table):
    n = len(game_board)
    visited = [[False]*n for _ in range(n)]

    # Directions
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # Extract connected components
    def bfs(x, y, board, target):
        q = deque([(x, y)])
        visited[x][y] = True
        shape = [(0, 0)]
        origin_x, origin_y = x, y

        while q:
            cx, cy = q.popleft()
            for i in range(4):
                nx, ny = cx + dx[i], cy + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[nx][ny] and board[nx][ny] == target:
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        shape.append((nx - origin_x, ny - origin_y))
        return shape

    # Rotate shape 90 degrees
    def rotate(shape):
        return [(y, -x) for x, y in shape]

    # Normalize shape
    def normalize(shape):
        min_x = min(x for x, y in shape)
        min_y = min(y for x, y in shape)
        return sorted((x - min_x, y - min_y) for x, y in shape)

    # Step 1: extract empty spaces from game_board
    blanks = []
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0 and not visited[i][j]:
                blanks.append(normalize(bfs(i, j, game_board, 0)))

    # Step 2: extract blocks from table
    blocks = []
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not visited[i][j]:
                blocks.append(bfs(i, j, table, 1))

    used = [False] * len(blocks)
    answer = 0

    # Step 3: match blanks with blocks
    for blank in blanks:
        for i, block in enumerate(blocks):
            if used[i] or len(block) != len(blank):
                continue

            cur = block
            matched = False
            for _ in range(4):
                cur = rotate(cur)
                if normalize(cur) == blank:
                    used[i] = True
                    answer += len(blank)
                    matched = True
                    break

            if matched:
                break

    return answer
# test cases
game_board1 = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table1 = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
print(solution(game_board1, table1)) # Expected output: 14