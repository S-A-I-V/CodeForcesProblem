def longest_repeated_substring_length(s: str) -> int:
    n = len(s)
    max_len = 0
    
    for length in range(1, n):
        seen = set()
        for start in range(n - length + 1):
            substring = s[start:start + length]
            if substring in seen:
                max_len = length
            else:
                seen.add(substring)
    
    return max_len

user_input = input()

result = longest_repeated_substring_length(user_input)
print(result)
