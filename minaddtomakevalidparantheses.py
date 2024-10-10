def minAddToMakeValid(s):
    """
    :type s: str
    :rtype: int
    """
    open_s = 0
    close_S = 0
    
    for char in s:
        if char == '(':
            open_s += 1  
        elif char == ')':
            if open_s > 0:
                open_s -= 1  
            else:
                close_S += 1
    return open_s + close_S

print(minAddToMakeValid("(())))"))
