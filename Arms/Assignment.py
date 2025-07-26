"""
a=int(input("Enter the Number"))
if(a>95):
 print("Grade: S")
else:
 if(a>75):
   print("Grade: A")
 else:
  if(a>50):
   print("Grade: B")
  else:
   print("Grade: C")
"""
"""
a = (input("Enter the Choice: "))
if(a=='A'):
 print ("Apple")
else:
  if(a=='B'):
   print ("Banana")
  else:
   if(a=='C'):
    print("Coconut")
    """
"""
a = (input("Enter the Choice: "))
if(a=='A'):
 print ("Apple")
elif(a=='B'):
 print ("Banana")
elif(a=='C'):
 print("Coconut")
 """
"""
a= int(input("Enter No.of Credits: "))
if(a>90):
    print("Senior Status")
elif(a>60 and a<90):
    print("Junior Status")
elif(a<60 and a>30):
    print("Sophomore Status")
else:
    print("Freshman Status")
"""
"""
lst = []
n = int(input("Enter number of elements : "))
sum=0
for i in range(0, n):
	ele = int(input())
	lst.append(ele)
for i in lst:
	if(i<100):
		sum = sum + i
print("Sum of Elements in the List:" + str(sum))
"""
"""
lst = []
n = int(input("Enter number of elements : "))
pos,neg=0,0
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
for i in lst:
    if(i<0):
        neg=neg+1
    else:
        pos=pos+1
print("Negative Elements in the List:",neg)
print("Positive Elements in the List:",pos)
"""
input = input("Enter numbers separated by a space: ")
num = [int(num) for num in input.split()]
print(" ".join(map(str, num)))
print("min=",min(num))
print("max=",max(num))