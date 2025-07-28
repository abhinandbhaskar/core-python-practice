s = "leEeetcode"
stack = []

for i in s:
    if stack and abs(ord(stack[-1]) - ord(i)) == 32:
        stack.pop()  
    else:
        stack.append(i)

result = ''.join(stack)
print(result) 

