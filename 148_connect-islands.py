def solution(n, costs):
    # Helper function to find the root (leader) of a node in the disjoint set
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])  # Path compression
        return parent[x]
    
    # Helper function to union two sets (connect two nodes)
    def union(parent, a, b):
        rootA = find(parent, a)
        rootB = find(parent, b)
        if rootA < rootB:
            parent[rootB] = rootA
        else:
            parent[rootA] = rootB
    
    # Step 1: Sort all bridge costs by ascending cost
    costs.sort(key=lambda x: x[2])

    # Step 2: Initialize parent list for Union-Find
    parent = [i for i in range(n)]

    total_cost = 0  # Final answer
    for a, b, cost in costs:
        # Check if a and b are in the same set (would create a cycle)
        if find(parent, a) != find(parent, b):
            union(parent, a, b)     # Connect them
            total_cost += cost      # Add this cost to total

    return total_cost

print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))  # Expected output: 4