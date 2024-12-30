'''stack=[2,45,4,5]
print(stack)

stack.append(56)
print(stack)

stack.append(90)
print(stack)

stack.append(440)
print(stack)

stack.pop()
print(stack)
'''
#queue
from collections import deque
queue=deque(["apple","orange","mango","kiwi"])
print(queue)

queue.append('mango')
print(queue)

queue.popleft()
print(queue)

#del
a=[1,2,3,4,5,6,7,8,9,0]
print(a)
del a[4]
print(a)

del a[:-5]
print(a)

del a[:]
print(a)
