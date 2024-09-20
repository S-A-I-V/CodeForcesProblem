def encrypt_message(n, m, c, a, b):
    for i in range(n - m + 1):
        for j in range(m):
            a[i + j] = (a[i + j] + b[j]) % c
    return a

n, m, c = map(int, input().split())
a=list(map(int, input().split()))
b=list(map(int, input().split()))


output=encrypt_message(n, m, c, a, b)
print(output)