'''num=int(input("enter the value:"))
#for i in num:
value=num
a=0
while num>0:
      a=(a*10)+num%10
      num//=10
print(a)
if (value==a):
      print(a,"is palindrome")
else:
      print("is not palindrome")

#armstrong
num=153
v=num

a=0
while v>0:
      k=v%10
      a=a+k**3
      v//=10
#print(num)
if(num==a):
     print("it is armstrong")
else:
      print("it is not armstrong")

'''

#adam number
def reversedigit(num):
      rev=0
      while(num>0):
            rev=rev*10+num%10
            num//=10
      return rev
def square(num):
      return(num*num)
def checkadamnumber(num):
      a=square(num)
      b=square(reversedigit(num))
      if(b==reversedigit(a)):
           return True
      else:
            return False
num=12
if(checkadamnumber(num)):
     print("it is adam number")
else:
      print("it is not adamnumber")
     