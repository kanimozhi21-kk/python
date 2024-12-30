'''basket={'apple','orange','mango','cherry','apple'}
print(basket)
print('berry' in basket)
print('apple' in basket)
a=set('kanimozhi')
b=set('karmegakuzhali')

print("letters in abut not in b",b-a,a-b)
print('both aor b',a|b)
print("letters in both a and b",a&b)

#set checking
a={x for x in 'kanimozhi' if x in 'anusri'}
print(a)
'''
#dictionaries
dic={'name':'kani','age':'20'}
print(dic['name'])

dic['guide']=32#add
print(dic)
print(list(dic))
print(sorted(dic))
print('guido'  not in dic)
print('guide' in dic)

a=dict([('mani',54),('arun',24),('anith',25),('pranav',23)])
print(a)
dist={x:x-2 for x in (4,3,5)}
print(dist)

a=dict(a=17,b=22,c=32)
print(a)