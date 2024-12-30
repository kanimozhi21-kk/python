#slice
string="wonderful land"
s1=slice(3,5)
s2=slice(2,6,3)
s3=slice(-2,-6,-4)
print("stringslicing")
print(string[s1])
print(string[s2])
print(string[s3])
#simple
b="wonderful land"
print(b[2:6])
#start to slice
b="wonderful land"
print(b[:5])
#slice to end
b="hello world"
print(b[2:])

b="wonderful make"
print(b[::2])
#negative indexing
b="hello world"
print(b[-4:-1])
#reverse string
a="happy sunday"
print(a[::-1])