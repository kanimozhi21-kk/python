#reverse
'''num=int(input("enter the vaue"))
num1=num
k=0
while num1>0:
      k=(k*10)+num1%10
      num1//=10
if(num==k):
     print("it is palindrom")
else:
      print("it is not palindrom")

#armstrong
n=int(input("enter the vaue"))
n1=n
k=0
while n1>0:
      q=(n1%10)
      k=k+q**3
      n1//=10
if(n==k):
     print("it is armstrong")
else:
      print("it is not armstong")
'''
def reversedigit(num):
      rev=0
      while num>0:
            rev=rev*10+num%10
            num//=10
      return rev
def square(num):
      return(num*num)
def checkadamnum(num):
      a=square(num)
      b=square(reversedigit(num))
      if(b==reversedigit(a)):
          return True
      else:
            return False
num=12
if(checkadamnum(num)):
     print("it is adamnumber")
else:
      print("it is not adamnumber")

      
