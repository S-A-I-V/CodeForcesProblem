'''
s is a string, it has ?

t is a substrning, we can obtain it by either removing some letters from s, or if there is only one window, then push it there
if len t <= len(? in s) replacing is possible otherwise no
'''
t = int(input())
reqlist=[]
for _ in range(t):
    s = input().strip()
    t = input().strip()
    
    t_pointer = 0
    t_length = len(t)
    s_length = len(s)
    possible = True
    
    s_list = list(s)

    for i in range(s_length):
        if t_pointer < t_length and (s_list[i] == t[t_pointer] or s_list[i] == '?'):
            if s_list[i] == '?':
                s_list[i] = t[t_pointer]
            t_pointer += 1
        elif s_list[i] == '?':
            s_list[i] = 'a' 
    
    if t_pointer == t_length:

        reqlist.append("YES")
        reqlist.append(''.join(s_list))
    else:
        reqlist.append("NO")
for i in reqlist:
    print(i)