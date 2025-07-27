import collections

q=collections.deque()
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
print(q)
print(q.pop())
print(q.pop())
print(q.pop())
