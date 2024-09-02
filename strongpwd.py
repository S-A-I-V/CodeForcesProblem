def calculate_time(s):
    # Calculate the time to type the string s
    time = 2  # time to type the first character
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            time += 1
        else:
            time += 2
    return time

def solve():
    t = int(input())
    for _ in range(t):
        s = input()
        max_time = 0
        best_string = ""
        
        for i in range(len(s) + 1):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                new_s = s[:i] + ch + s[i:]
                new_time = calculate_time(new_s)
                if new_time > max_time:
                    max_time = new_time
                    best_string = new_s
        
        print(best_string)
solve()
