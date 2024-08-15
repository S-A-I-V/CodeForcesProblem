def check_template_match(n, a, strings):
    results = []
    for s in strings:
        if len(s) != n:
            results.append("NO")
            continue
        
        num_to_char = {}
        char_to_num = {}
        is_valid = True
        
        for i in range(n):
            num = a[i]
            char = s[i]
            
            if num in num_to_char:
                if num_to_char[num] != char:
                    is_valid = False
                    break
            else:
                num_to_char[num] = char
            
            if char in char_to_num:
                if char_to_num[char] != num:
                    is_valid = False
                    break
            else:
                char_to_num[char] = num
        
        if is_valid:
            results.append("YES")
        else:
            results.append("NO")
    
    return results

def main():
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        m = int(input())
        strings = [input().strip() for _ in range(m)]
        results.extend(check_template_match(n, a, strings))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
