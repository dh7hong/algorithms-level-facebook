from collections import deque

def solution(n, roads, sources, destination):
    # 1. Build adjacency list
    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    # 2. Distance array (initialize with -1 = unreachable)
    distance = [-1] * (n + 1)

    # 3. BFS from destination
    queue = deque()
    queue.append(destination)
    distance[destination] = 0

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

    # 4. Build result for sources
    return [distance[src] for src in sources]


# Example usage:
print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))  # Output: [1, 2]
print(solution(5, [[1, 2], [1, 4], [2, 4], [3, 4], [3, 5]], [5, 4, 3, 2, 1], 1))  # Output: [3, 2, 2, 1, 0]
print(solution(7, [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]], [6, 7, 4], 1))  # Output: [4, 4, 3]
