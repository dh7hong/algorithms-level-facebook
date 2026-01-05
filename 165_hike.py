import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))

    gates_set = set(gates)
    summits_set = set(summits)

    INF = float('inf')
    intensity = [INF] * (n + 1)
    pq = []

    # Multi-source start from all gates
    for g in gates:
        intensity[g] = 0
        heapq.heappush(pq, (0, g))

    while pq:
        curr_intensity, node = heapq.heappop(pq)

        if curr_intensity > intensity[node]:
            continue

        # Do not expand from summits
        if node in summits_set:
            continue

        for nxt, weight in graph[node]:
            new_intensity = max(curr_intensity, weight)
            if new_intensity < intensity[nxt]:
                intensity[nxt] = new_intensity
                heapq.heappush(pq, (new_intensity, nxt))

    # Choose best summit
    best_summit = None
    best_intensity = INF

    for s in sorted(summits):
        if intensity[s] < best_intensity:
            best_intensity = intensity[s]
            best_summit = s

    return [best_summit, best_intensity]
