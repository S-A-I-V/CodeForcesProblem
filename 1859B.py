def solve():
    t = int(input())
    results = []
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()

        if a[0] == a[-1]:
            results.append("-1")
        else:
            b = [a[0]]
            c = []
            for i in range(1, n):
                if a[i] != a[0]:
                    c = a[i:]
                    break
            
            results.append(f"{len(b)} {len(c)}")
            results.append(" ".join(map(str, b)))
            results.append(" ".join(map(str, c)))
    
    print("\n".join(results))

def main():
    solve()

if __name__ == "__main__":
    main()
