def chewbaсca_number(x):
    x = str(x) 
    result = []
    
    for i, digit in enumerate(x):
        num = int(digit)
        if i == 0 and num == 9:
            result.append(str(num)) 
        else:
            result.append(str(min(num, 9 - num)))  
    
    return "".join(result)

x = int(input())

# Output the result
print(chewbaсca_number(x))
