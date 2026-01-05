def solution(n, results):
    # graph[i][j] = 1 means i beats j
    graph = [[0] * (n + 1) for _ in range(n + 1)]

    # record given results
    for a, b in results:
        graph[a][b] = 1

    # Floyd–Warshall (transitive closure)
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

    # count players whose rank is determinable
    answer = 0
    for i in range(1, n + 1):
        known = 0
        for j in range(1, n + 1):
            if graph[i][j] or graph[j][i]:
                known += 1
        if known == n - 1:
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))  # Output: 2
print(solution(4, [[1, 2], [2, 3], [3, 4], [4, 1]]))  # Output: 0
print(solution(3, [[1, 2], [2, 3], [1, 3]]))  # Output: 3
print(solution(6, [[1, 5], [3, 4], [5, 4], [4, 2], [4, 6]]))  # Output: 1