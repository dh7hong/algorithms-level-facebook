def solution(enroll, referral, seller, amount):
    # 1. Map each person to their recruiter
    parent = {}
    for e, r in zip(enroll, referral):
        parent[e] = r

    # 2. Initialize profit dictionary
    profit = {name: 0 for name in enroll}

    # 3. Process each sale
    for s, a in zip(seller, amount):
        money = a * 100  # profit from selling toothbrushes
        cur = s

        while cur != "-" and money > 0:
            commission = money // 10      # 10% commission
            keep = money - commission     # remaining profit

            profit[cur] += keep
            cur = parent[cur]             # move to recruiter
            money = commission            # pass commission upward

    # 4. Return profits in enroll order
    return [profit[name] for name in enroll]

print(solution(
    ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
    ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
    ["young", "john", "tod", "emily", "mary"],  
    [12, 4, 2, 5, 10]   
))  # Output: [360, 958, 108, 0, 450, 18, 180, 1080]