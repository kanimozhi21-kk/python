'''def factorial(x):
      if x==2:
         return 2
      else:
            return(x*factorial(x-1))
num=2
print("the factorial of",num,"is",factorial(num))

def recursive_fibonacci(n):
      if n<=1:
         return n
      else:
            return(recursive_fibonacci(n-1)+recursive_fibonacci(n-2))
n_terms=10
#check
if n_terms<=0:
   print("invalid input ! please input a positive value")
else:
      print("fibonacci series:")
for i in range(n_terms):
     print(recursive_fibonacci(i))
'''
def factorial(x):
      if x==2:
          return 2
      else:
            return(x*factorial(x-1))
num=5
print("it is value",num,"is",factorial(num))

def recursive_fibonacci(n):
      if n<=1:
          return n
      else:
            return(recursive_fibonacci(n-1)+recursive_fibonacci(n-2))
n_terms=10

if n_terms<=0:
   print("invalid input please enter a positive value")
else:
      print("fibonacci")
for i in range(n_terms):
     print(recursive_fibonacci(i))




        
                

