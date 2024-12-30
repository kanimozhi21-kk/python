
#simple for
for x in range(12):
     print("run this time",x)

'''#for and break
for x in range(10):
          if x==8:
             break
          print(x)

#for else
for x in range(6):
     print(x)
     if x==5:
         break
else:
      print("loop ended")

#for using string
string="good day"
for x in string:
     print(x)
'''
#collection in for loop
collection=['hii',2,'well']
for x in collection:
     print(x)

#nested in for loop 
color=["red","sweet","tasty"]
fruits=['cherry','plums','apple']
veg=['brinjal','ladies finger','potato']
for a in color:
     for b in fruits:
          for c in veg:
               print(a,b,c)

#list in for loop
lists=[['a','b','c'],['d','e','f',],['g','h','i']]
for l in lists:
     print(l)
     for x in l:
          print(x)
     

#continue statement
fruits=['apple','cherry','banana','mango']
for x in fruits:
     if x=="grapes":
        continue
     print(x)

#increase value
for x in range(4,76,6):
     print(x)
