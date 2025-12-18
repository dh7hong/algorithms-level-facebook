def solution(n, computers):
    # Create a visited list to track visited computers
    visited = [False] * n

    def dfs(node):
        # Mark the current node as visited
        visited[node] = True
        
        # Visit all connected computers recursively
        for connected_node in range(n):
            if computers[node][connected_node] == 1 and not visited[connected_node]:
                dfs(connected_node)

    network_count = 0  # Number of networks found

    for i in range(n):
        # If computer 'i' is not visited, it's a new network
        if not visited[i]:
            dfs(i)
            network_count += 1

    return network_count

# Test cases
print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))  # Expected output: 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))  # Expected output: 1
