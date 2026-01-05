def solution(scores):
    wanho_att, wanho_peer = scores[0]
    wanho_sum = wanho_att + wanho_peer

    # 1. Sort by attitude DESC, peer ASC
    scores.sort(key=lambda x: (-x[0], x[1]))

    max_peer = 0
    valid_sums = []

    for att, peer in scores:
        # If dominated
        if peer < max_peer:
            # Check if Wanh is dominated
            if att == wanho_att and peer == wanho_peer:
                return -1
            continue

        # Valid employee
        max_peer = max(max_peer, peer)
        valid_sums.append(att + peer)

    # 2. Rank calculation
    valid_sums.sort(reverse=True)

    rank = 1
    for total in valid_sums:
        if total > wanho_sum:
            rank += 1
        elif total == wanho_sum:
            return rank

    return rank