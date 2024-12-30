'''#syntax error
x=65
if x==4:   
   print(x)

#runtime and name error
print(x)

#type error
x="4"
y=78
z=x+y
print(z)

#index error
x=['good','happy','smile']
print(x[5])

#attributes error
x="pooja"
x.reverse()
'''
#logical error
def fact(n):
      r=1
      for x in range(1,n+1):
           r=r*i
      return r
print(fact(n))
'''
#print(x)
try:
    print(x)
except:
       print("an error occured")

try:
    c=a+10
except NameError:
        print("variable a in not defined")
except:
       print("something went wrong")

try:
    print(w)
except:
        print("something went wrong")
else:
      print("nothing went wrong")

try:
    x=5
    print(x)
except:
        print("something went wrong")
finally:
     print("the 'try except' is finished")

#raise exception
a='hello'
assert a=="bala"
'''



