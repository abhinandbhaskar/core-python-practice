import collections 
q=collections.deque()

q.append(10)
q.append(20)
q.append(30)
print(q)

print(q.popleft())
print(q.popleft())
print(q.popleft())