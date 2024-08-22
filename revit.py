n = input().strip()
if n[0] == '-':
    reversed_number = '-' + n[:0:-1].lstrip('0')
else:
    reversed_number = n[::-1].lstrip('0')

if reversed_number == '' or reversed_number == '-':
    print('0')
print(reversed_number)


