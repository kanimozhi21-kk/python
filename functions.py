'''def abc():
      print("name")
      print("place")
      print(123)
abc()
abc()

#passing parameter
def soul(b,c,a):
      print("hi",a,"to",b,"livewire",c)
a="name"
b="favoo"
c=1234
soul(a,b,c)
print(a)

#passing parameter
def example(fname):
      print(fname,"hello")
example("kani")
example("priya")
example("pavi")
example("anju")
example(123)

#two parameter passing
def funname (fname,lname):
      print(fname+""+lname)
a=input("enter the name1")
b=input("enter the name2")
funname(a,b)
'''
#keyword arguments
def my_func(*elements):
      print(elements[1])
      print(elements[2])
      print(elements[0])
my_func('an','df','ku')

def my_func(**values):
      print(values["name1"])
      print(values["name2"])
      print(values["name3"])
my_func(name1="swathi",name2="indhu",name3="swetha")

#rreturn function
def range(a,b):
      c=a+b
      return c
a=range(32,54)
print(a*10)
b=range(67,34)
print(b/10)

def func(a=32):
      print(a)
func(54)
func(343)
func()
def my_func(country="INDIA"):
      print("i am from",country)
my_func("paris")
my_func("south america")
my_func()
'''

def x(a):
     return a+2
print(x(52))

x=lambda a:a+15
print(x(92))
 
x=lambda a,b,c:a*b*c
print(x(2,3,4))

def myfunc(n):
      return lambda a:a*n
m=myfunc(45)
print(m(5))
print(m(4))

#mapping and fitering
data=[4,2,3]
result1=map(lambda x:x*5,data)
print(list(result1))
result2=filter(lambda x:x%3==0,data)
print(list(result2))

x=lambda a:a*2
print(x(9))

value=[2,3,4]
result=filter(lambda a:a%2==1,value)
print(list(result))

def a(x):
     return x*3
print(a(9))

a=lambda z:z*5
print(a(6))
'''


      
