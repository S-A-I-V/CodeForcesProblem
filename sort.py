def solve():
    n, q = map(int, input().split())
    a = input().strip()
    b = input().strip()
    
    cnt = [0] * 26
    v = [cnt[:]] 
    for i in range(n):
        cnt[ord(a[i]) - ord('a')] += 1
        cnt[ord(b[i]) - ord('a')] -= 1
        v.append(cnt[:])  
    results = []
    for _ in range(q):
        l, r = map(int, input().split())
        l -= 1  

        op = 0
        for i in range(26):
            op += abs(v[l][i] - v[r][i])
        results.append(op // 2)

    for result in results:
        print(result)

def main():
    TCS = int(input())
    for _ in range(TCS):
        solve()

if __name__ == "__main__":
    main()
