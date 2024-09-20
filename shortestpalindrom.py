def shortestPalindrome(s: str) -> str:
    if not s or len(s) == 1:
        return s

    def is_palindrome(sub_s: str) -> bool:
        return sub_s == sub_s[::-1]
    
    n = len(s)
    for i in range(n, 0, -1):
        if is_palindrome(s[:i]):
            break
    
    return s[i:][::-1] + s