bt3=['kani','priya','anju']
bt4=['pavi','yash']
print(bt3,bt4)
print(type(bt4))

bt4.append('3sha')
print(bt4)

bt3.extend(bt4)
print(bt3)

bt3.insert(6,'narmadha')
print(bt3)

bt3.remove('narmadha')
print(bt3)

bt3.pop()                                                                
print(bt3)

bt3.reverse()
print("reverse list:",bt3)

print(bt3.index("priya"))

bt3.sort()
print(bt3)

bt=bt3.copy()
print("copied list:",bt)

bt.clear()
print(bt)
print(bt3)

#example
a=[]
print(any(a))
for x in range(10):
     a.append(x*2)
print(a)

a=[x*3 for x in range(7)]
print(a)

a=[x**2 for x in range(7) if x%3==0]
print(a)

a=[x+y for x in ['new','mew','helo']for y in ['a','b']]
print(a)





