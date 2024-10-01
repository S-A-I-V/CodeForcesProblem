import math

def lcm_string(s, t):
    len_s, len_t = len(s), len(t)
    lcm_len = (len_s * len_t) // math.gcd(len_s, len_t)
    if s * (lcm_len // len_s) == t * (lcm_len // len_t):
        return s * (lcm_len // len_s)
    else:
        return -1

q = int(input())
for _ in range(q):
    s = input()
    t = input()
    print(lcm_string(s, t))
