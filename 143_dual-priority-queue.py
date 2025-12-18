def solution(operations):
    queue = []

    for op in operations:
        command, num = op.split()
        num = int(num)

        if command == 'I':
            # Insert the element directly.
            queue.append(num)

        elif command == 'D' and queue:
            if num == 1:
                # Delete the maximum element
                max_val = max(queue)
                queue.remove(max_val)
            elif num == -1:
                # Delete the minimum element
                min_val = min(queue)
                queue.remove(min_val)

    # Check if queue is empty
    if queue:
        return [max(queue), min(queue)]
    else:
        return [0, 0]

# Test cases
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))  # [0,0]
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))  # [333, -45]
