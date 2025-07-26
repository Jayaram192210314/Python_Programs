#Functions

#sample
def sorting(e):
  return len(e)
a = ['jayaram','mahesh','krishna','vasu']
a.sort(key=sorting)
print(a)

#LCM
"""
def lcm(a,b):
  if(a<b):
    n=a
  else:
    n=b
  for i in range (1,n+1):
    if((a%i==0) and (b%i==0)):
      GCD=i
  LCM = (a*b)//GCD
  print(f"The LCM of two Numbers is {LCM}")
a = int(input())
b = int(input())
print(f"Enter the two Number: {a}, {b}")
lcm(a,b)
"""

#Second Max
"""
def sor(n):
    lst=[]
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    print(lst)
    lst.sort(reverse=True)
    print(lst[1])
n = int(input())
print(f"Enter number of elements: {n}")
sor(n)
"""

#Removal of duplicates
"""
def rev(n):
    lst=[]
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    print(f"The list before the removal of duplicates :")
    print(lst)
    rev_lst = list(set(lst))
    print(f"The list after removal of duplicates :")
    print(rev_lst)
n = int(input())
print(f"Enter number of elements: {n}")
rev(n)
"""

# Write a Python program to find the square root of a number using the Newton-Raphson method
"""

"""

#ternary operator
"""
a = int(input())
b = int(input())
print(f"Entered Elements are {a}, {b}.")
k = a if a < b else b
print(f"The smallest element is {k}")
"""