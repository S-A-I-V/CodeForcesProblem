# t = list(map(int, input("").split()))
# target=int(input(""))
# len_t=len(t)

# for i in range(1, len_t):
#     j=i-1
#     if t[i]+t[j]==target:
#         print(i,j)
#         break
#2sum 


t = list(map(int, input("").split()))
target = int(input(""))
len_t = len(t)

for i in range(len_t):
    for j in range(i + 1, len_t):
        if t[i] + t[j] == target:
            print(i, j)
            break
