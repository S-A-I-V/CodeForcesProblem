def solve():
    n = int(input())
    s = input()
    
    ct = 0  # Counter for unmatched '('
    cost = 0
    v = []  # Stack to store indices of unmatched '('

    for i in range(n):
        if s[i] == '(':
            ct += 1
            v.append(i)
        elif s[i] == ')':
            ct -= 1
            cost += i - v[-1]
            v.pop()
        else:  # s[i] == '_'
            if ct > 0:
                # Treat '_' as ')'
                ct -= 1
                cost += i - v[-1]
                v.pop()
            else:
                # Treat '_' as '('
                ct += 1
                v.append(i)

    return(cost)
def main():
    TCS = int(input())
    result=[]
    for _ in range(TCS):
        result.append(solve())
    for i in result:
        print(i)
if __name__ == "__main__":
    main()
