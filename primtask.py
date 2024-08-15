t = int(input().strip())
results = []

for _ in range(t):
    a = input().strip()

    if a.startswith("10"):
        suffix = a[2:]
        # Handle cases like "100", "1000", "100000", and "1002"
        if len(a)==3 and a[-1]!=0 and a!='101' and a!='100':
            results.append('YES')
        elif all(a[i] == "0" for i in range(2, len(a) - 1)) and a[-1] != '1':
            results.append('NO')

        elif len(suffix) > 0 and suffix.isdigit() and suffix[0] == '0':
            results.append('NO')
        elif all(a[i] == "0" for i in range(2, len(a) - 1) if a[i - 2:i + 1] == "10") and a != '101':
            results.append('YES')
        elif len(a) > 2 and a[-1] == '1':
            results.append("NO")
        elif suffix == '' or (suffix.isdigit() and suffix[0] != '0'):
            results.append("NO")
        else:
            results.append("NO")
    else:
        results.append("NO")

print("\n".join(results))
