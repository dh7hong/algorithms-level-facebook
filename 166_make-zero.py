def solution(a, edges):
    n = len(a)

    # Impossible if total sum is not zero
    if sum(a) != 0:
        return -1

    # Build graph
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n
    parent = [-1] * n
    order = []

    # 1️. Build traversal order using stack (DFS)
    stack = [0]
    visited[0] = True

    while stack:
        node = stack.pop()
        order.append(node)
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                parent[nxt] = node
                stack.append(nxt)

    # 2. Process nodes in reverse order (post-order)
    total_cost = 0

    for node in reversed(order):
        if parent[node] != -1:
            total_cost += abs(a[node])
            a[parent[node]] += a[node]

    return total_cost
