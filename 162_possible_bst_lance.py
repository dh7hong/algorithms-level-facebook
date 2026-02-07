import time


def decimal_to_binary(n):
    start = time.time()
    binary_str = ''    
    if n == 0:
        return '0'
    while n > 0:
        binary_str = str(n % 2) + binary_str
        n //= 2
    print(f"[decimal_to_binary] time = {time.time() - start:.6f}s")
    return binary_str


def is_power_of_two(n):
    start = time.time()
    if n == 2:
        return True
    while n > 2:
        if n % 2 != 0:
            return False
        n //= 2
    print(f"[is_power_of_two] time = {time.time() - start:.6f}s")
    return True


def solution(numbers):
    print("=== START solution ===")
    total_start = time.time()

    print("\n[Step 1] Decimal -> Binary conversion")
    t1 = time.time()
    binary_numbers = [decimal_to_binary(num) for num in numbers]
    print(f"[Binary conversion total] {time.time() - t1:.6f}s")

    result = []

    for idx, binary in enumerate(binary_numbers):
        print(f"\n--- Processing index {idx}, initial length={len(binary)} ---")

        # Padding
        pad_start = time.time()
        while True:
            length = len(binary)
            if is_power_of_two(length + 1):
                break
            binary = '0' + binary
        print(f"[Padding] final length={len(binary)}, time={time.time() - pad_start:.6f}s")

        n = len(binary)
        root = (n - 1) // 2

        if binary[root] == '0':
            print("[Root check] root is 0 -> invalid")
            result.append(0)
            continue

        call_counter = 0  # recursion counter

        def check_subtree(start, end):
            nonlocal call_counter
            call_counter += 1

            # printing many calls
            print(f"check_subtree({start}, {end})")

            if start >= end:
                return True

            root = (start + end) // 2

            if binary[root] == '0':
                scan_start = time.time()
                if '1' in binary[start:end+1]:
                    print(f"[Scan FAIL] range ({start},{end})")
                    return False
                print(f"[Scan OK] time={time.time() - scan_start:.6f}s")
                return True

            left = check_subtree(start, root - 1)
            if not left:
                return False

            right = check_subtree(root + 1, end)
            if not right:
                return False

            return True

        subtree_start = time.time()
        left = check_subtree(0, root - 1)
        right = check_subtree(root + 1, n - 1)
        print(f"[Subtree total time] {time.time() - subtree_start:.6f}s")
        print(f"[Recursive calls] {call_counter}")

        result.append(1 if left and right else 0)

    print(f"\n=== END solution | total time = {time.time() - total_start:.6f}s ===")
    return result

# test
numbers = [
    2**50 - 1,
    2**49 - 1,
    2**48 - 1,
    2**47 - 1
]
 
print(solution(numbers))  # Expected output: [1, 1, 0]
