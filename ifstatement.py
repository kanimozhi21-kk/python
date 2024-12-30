'''
a=30
b=33
c=a**b
print("the age is",c)
if(a<=c):
     print("age is greater than of 30")
else:
      print("age is less than of 25")
      print("a is",a)

b=5
h=12
p=b*h
print("the value is",p)
if(p>20):
    print("b is greater than of number10")
    print("b is",p)
elif(p>8):
     print("b is greater than of number 6")
     print("b is",p)
elif(h>4):
     print("n is les than of 7")
     print("b is ",h)
else:
      print("not valid")
'''
#nested if
age=15
place="chennai"
course="python"
if(age>18):
     if(place=="chennai"):
          if(course=="python"):
                print("you will be vote")
          else:
                print("sorry your place is not supported")
     else:
           print("your age is not supported")
else:
      print("your course is not supported")
