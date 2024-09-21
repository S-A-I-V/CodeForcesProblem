def normalize(login):
    return login.lower().replace('o', '0').replace('1', '1').replace('l', '1').replace('i', '1')
s = input().strip()
n = int(input())
existing_logins = [input().strip() for _ in range(n)]

normalized_s = normalize(s)
for login in existing_logins:
    if normalize(login) == normalized_s:
        print("No")
        break
else:
    print("Yes")