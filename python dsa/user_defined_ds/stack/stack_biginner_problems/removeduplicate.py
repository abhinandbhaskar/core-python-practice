'''Easy Way USing logic'''
# s="abbsscabab"
# x=set(s)
# c="".join(x)
# print(c)


s="aaaabbsscababgghhhhh"
stack=[]
for i in s:
    if i in stack:
        pass
    else:
        stack.append(i)
result="".join(stack)
print(result)


