def remove_zeros(num):
    return int(''.join(d for d in str(num) if d != '0'))

a = int(input())
b = int(input())
c = a + b

a_no_zeros = remove_zeros(a)
b_no_zeros = remove_zeros(b)
c_no_zeros = remove_zeros(c)

if a_no_zeros + b_no_zeros == c_no_zeros:
    print("YES")
else:
    print("NO")
