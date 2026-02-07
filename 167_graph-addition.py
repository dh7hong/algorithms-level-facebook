def solution(commands):
    SIZE = 50
    N = SIZE * SIZE

    # Convert (r, c) -> 1D index
    def idx(r, c):
        return (r - 1) * SIZE + (c - 1)

    parent = [i for i in range(N)]
    value = [""] * N

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra == rb:
            return

        # Value priority: ra first
        if value[ra]:
            parent[rb] = ra
        else:
            parent[ra] = rb

    answer = []

    for cmd in commands:
        parts = cmd.split()

        if parts[0] == "UPDATE":
            if len(parts) == 4:
                r, c, v = int(parts[1]), int(parts[2]), parts[3]
                root = find(idx(r, c))
                value[root] = v
            else:
                v1, v2 = parts[1], parts[2]
                for i in range(N):
                    if value[find(i)] == v1:
                        value[find(i)] = v2

        elif parts[0] == "MERGE":
            r1, c1, r2, c2 = map(int, parts[1:])
            union(idx(r1, c1), idx(r2, c2))

        elif parts[0] == "UNMERGE":
            r, c = int(parts[1]), int(parts[2])
            target = idx(r, c)
            root = find(target)
            saved_value = value[root]

            members = [i for i in range(N) if find(i) == root]

            for m in members:
                parent[m] = m
                value[m] = ""

            value[target] = saved_value

        elif parts[0] == "PRINT":
            r, c = int(parts[1]), int(parts[2])
            root = find(idx(r, c))
            answer.append(value[root] if value[root] else "EMPTY")

    return answer
