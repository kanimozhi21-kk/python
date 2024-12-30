#string
#upper
text="activate windows"
print(text.upper())
#lower
text="ACTIVATE WINDOWS"
print(text.lower())
#oppsite swapcasetype
text="MAke A SENtence"
print(text.swapcase())
#split
a="hello-world"
print(a.split("-"))
b="livewire"
print(b.split("i"))
c="kanimozhi"
print(c.split("m"))
#capitalize
text="hello world"
print(text.capitalize())
#replace
text="web page"
print(text.replace("page","development"))
a="welcome"
print(a.replace("welcome to all","everyone"))
#concatenate
a="well"
b="development"
c=a+"..."+b
print(c)
m="computer"
n="science"
p=m+"<"+"3"+">"+n
print(p)
#format
txt="I am {} and i am 4 {}"
name="magesh"
num="55"
print(txt.format(name,num))
a="i am {}"
name="malu"
print(a.format(name))
type="python is {} language"
fix="high level"
print(type.format(fix))
