def solution(begin, target, words):
    # First, check if target word is in the words list; if not, return 0.
    if target not in words:
        return 0

    visited = set()  # Track visited words to avoid cycles.
    queue = [(begin, 0)]  # Use a list as a simple queue. Each element: (word, steps).

    while queue:
        current_word, steps = queue.pop(0)  # Pop the first element from the queue.

        # If we've reached our target, return the number of steps taken.
        if current_word == target:
            return steps

        # Check all possible next words from the words list.
        for word in words:
            if word not in visited:
                # Count how many letters are different.
                diff = sum(1 for a, b in zip(current_word, word) if a != b)

                if diff == 1:
                    visited.add(word)  # Mark as visited.
                    queue.append((word, steps + 1))  # Append to queue with incremented steps.

    # If the target word is not reachable, return 0.
    return 0

# Test the solution with given examples.
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # Expected output: 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))         # Expected output: 0
