'''

luckydiv
'''
n=int(input())
# purelucky number
# digits = [int(digit) for digit in n]
def is_lucky_number(num):
    return all(digit in '47' for digit in str(num))

def is_almost_lucky(n):
    lucky_numbers = [i for i in range(1, 1001) if is_lucky_number(i)]
    for lnum in lucky_numbers:
        if n % lnum == 0:
            return True
    return False

if is_almost_lucky(n):
    print("YES")
else:
    print("NO")
