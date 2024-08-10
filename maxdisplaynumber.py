'''
7 section display
battery can power max n sections
two-1
three-7
four-4, 11
five-5, 71
six-9, 77, 111
seven- 711
'''
def max_display_number(n):
    if n % 2 == 0:
        return '1' * (n // 2)
    else:
        return '7' + '1' * ((n - 3) // 2)

n = int(input())
print(max_display_number(n))