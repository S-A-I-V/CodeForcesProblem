s=str(input(""))
char_set = set()
l, max_len = 0, 0
for r in range(len(s)):
    while s[r] in char_set:
        char_set.remove(s[l])
        l += 1
    char_set.add(s[r])
    max_len = max(max_len, r - l + 1)
print(max_len)
