def solution(s):
    result = []

    for x in s:
        stack = []
        count_110 = 0

        # Step 1: Remove all "110"
        for ch in x:
            stack.append(ch)
            if len(stack) >= 3 and stack[-3:] == ['1', '1', '0']:
                stack.pop()
                stack.pop()
                stack.pop()
                count_110 += 1

        # Remaining string
        remaining = ''.join(stack)

        # Step 2: Find insertion point
        insert_idx = remaining.rfind('0')

        # Step 3: Insert all "110"
        if insert_idx == -1:
            new_str = "110" * count_110 + remaining
        else:
            new_str = (
                remaining[:insert_idx + 1] +
                "110" * count_110 +
                remaining[insert_idx + 1:]
            )

        result.append(new_str)

    return result

example_input = ["1110", "100111100", "0111111010"]
print(solution(example_input)) 
# Output: ['1101', '100110110', '0110110111']
