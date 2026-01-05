def solution(s):
    n = len(s)
    if n == 0:
        return 0

    max_len = 1  # at least one character is a palindrome

    # helper function to expand around center
    def expand(left, right):
        nonlocal max_len
        while left >= 0 and right < n and s[left] == s[right]:
            max_len = max(max_len, right - left + 1)
            left -= 1
            right += 1

    for i in range(n):
        # odd-length palindromes (center at i)
        expand(i, i)

        # even-length palindromes (center between i and i+1)
        expand(i, i + 1)

    return max_len

print(solution("babad"))  # Output: 3 ("bab" or "aba")
print(solution("cbbd"))   # Output: 2 ("bb")
print(solution(""))       # Output: 0
print(solution("a"))      # Output: 1 ("a")