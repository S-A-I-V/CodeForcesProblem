def is_even(number):
    """
    Check if the given number is even and print 'YES' if it is, otherwise print 'NO'.
    
    Parameters:
    number (int): The integer to check for evenness.
    """
    if number % 2 == 0 and number!=2:
        print('YES')
    else:
        print('NO')
w = int(input("\n"))
is_even(w)