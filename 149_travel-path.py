def solution(tickets):
    # Build a graph where each departure has a list of arrivals
    from collections import defaultdict
    graph = defaultdict(list)
    
    # Sort tickets to ensure lexical order when popping
    for a, b in sorted(tickets):
        graph[a].append(b)

    route = []  # final path

    def dfs(airport):
        # Explore until there are no tickets left from this airport
        while graph[airport]:
            # Always pop the smallest lexical destination
            next_airport = graph[airport].pop(0)
            dfs(next_airport)
        # When no more moves, add to route
        route.append(airport)

    # Start from ICN
    dfs("ICN")
    
    # Reverse the route because we append after visiting
    return route[::-1]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))  # Expected: ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))  # Expected: ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]