def build_tree(info, edges):
    """Build adjacency list for the tree"""
    tree = [[] for _ in range(len(info))]
    for parent, child in edges:
        tree[parent].append(child)
    return tree


def dfs(info, tree, sheep, wolves, candidates, result):
    """
    Depth-first search to collect sheep safely
    result: list with one element to track max sheep (mutable reference)
    """
    result[0] = max(result[0], sheep)

    for i, node in enumerate(candidates):
        next_sheep = sheep + (info[node] == 0)
        next_wolves = wolves + (info[node] == 1)

        # Stop if wolves can eat sheep
        if next_wolves >= next_sheep:
            continue

        # Update candidate nodes
        next_candidates = candidates[:i] + candidates[i + 1:]
        next_candidates.extend(tree[node])

        dfs(
            info,
            tree,
            next_sheep,
            next_wolves,
            next_candidates,
            result
        )


def solution(info, edges):
    tree = build_tree(info, edges)

    # result[0] will store max sheep count
    result = [0]

    # Start DFS from root
    dfs(
        info=info,
        tree=tree,
        sheep=1,          # root node always has sheep
        wolves=0,
        candidates=tree[0],
        result=result
    )

    return result[0]
