def check(subtree):
    if len(subtree) == 1:
        return True

    mid = len(subtree) // 2
    root = subtree[mid]

    left = subtree[:mid]
    right = subtree[mid + 1:]

    # If root is dummy (0), it cannot have real children
    if root == '0':
        if '1' in left or '1' in right:
            return False

    return check(left) and check(right)

def is_valid_tree(binary):
    return check(binary)

def solution(numbers):
    answer = []

    for num in numbers:
        binary = bin(num)[2:]  # remove '0b'

        # Find smallest full binary tree size (2^k - 1)
        length = 1
        while length < len(binary):
            length = length * 2 + 1

        # Pad with leading zeros
        padded = binary.zfill(length)

        answer.append(1 if is_valid_tree(padded) else 0)

    return answer

# test
numbers = [
    2**50 - 1,
    2**49 - 1,
    2**48 - 1,
    2**47 - 1
]
 
print(solution(numbers))  # Expected output: [1, 1, 0]
