stack1=list(input())
mapping={')':'(', '}':'{', ']':'['}
stack=[]
for char in stack:
    if char in mapping:
        top_element=stack1.pop() if stack1 else '#'
        if mapping[char]!=top_element:
            print(False)
    else:
        stack.append(char)
print(not stack)
