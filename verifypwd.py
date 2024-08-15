def solve():
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input())
        password = input().strip()

        # Split into digits and letters
        digits = ''
        letters = ''
        digit_part = True
        
        for ch in password:
            if ch.isdigit():
                if not digit_part:
                    results.append("NO")
                    break
                digits += ch
            else:
                digit_part = False
                letters += ch
        else:
            # Check if digits and letters are sorted
            if digits == ''.join(sorted(digits)) and letters == ''.join(sorted(letters)):
                results.append("YES")
            else:
                results.append("NO")
    
    print("\n".join(results))

solve()
