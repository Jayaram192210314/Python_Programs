a="super kings"
b="chennai"
c= "10"
d= "a"
#indexing
print(a[0])
#slicing
print(a[0:4])
print(a[:3])
print(a[0:])
#concentation
print(a + b)
#repetation
print(a*2)
#membership
print("e" in a)
#1)capitalize
print(a.capitalize())
#2)Upper case
print(a.upper())
#3)Lower case
print(a.lower())
#4)title
print(a.title())
#5)split
print(a.split())
#6)count the substring
print(a.count("kings"))
#7)Replace with new word
print(a.replace("super", "hyper"))
#8)alphabet check
print(a.isalpha())
print(d.isalpha())
#10)Digit are not
print(a.isdigit())
print(c.isdigit())
#11)minimum in a
print(min(a))
#12)length of a
print(len(b))
#13)maximum of a
print(max(a))
#14)Starts wuth
print(a.startswith("s"))
#15)Ends with
print(a.endswith("i"))
#16)find
k=a.find("chennai")
if(k==-1):
  print("false")
else:
  print("true")
l=a.find("super")
if(l==0):
  print("true")
else:
  print("false")