def solution(n, vertex):
    # Step 1: Build an adjacency list representation of the graph.
    graph = [[] for _ in range(n + 1)]
    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    # Step 2: Initialize distances (-1 for unvisited nodes)
    distance = [-1] * (n + 1)
    distance[1] = 0  # Distance from node 1 to itself is 0

    # Step 3: BFS using a list as queue (less efficient but acceptable)
    queue = [1]  # Start with node 1

    while queue:
        current = queue.pop(0)  # Pop from front (O(n) complexity)

        # Visit all neighbors of the current node
        for neighbor in graph[current]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

    # Step 4: Find the maximum distance value
    max_dist = max(distance)

    # Step 5: Count how many nodes have the maximum distance
    return distance.count(max_dist)

# Test example provided
print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
# Expected output: 3
