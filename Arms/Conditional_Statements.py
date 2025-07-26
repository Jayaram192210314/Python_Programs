#1Write a Python program to check if a given number is a palindrome or not using recursion
def isPalindrome(s):
	s = s.lower()
	l = len(s)
	if l < 2:
		return True
	elif s[0] == s[l - 1]:
		return isPalindrome(s[1: l - 1])
	else:
		return False
s = input()
ans = isPalindrome(s)
if ans:
	print("It is a Palindrome")
else:
	print("It is not a Palindrome")

#2Write a Python program to check if a given string is a valid password
a = input()
l, u, p, d = 0, 0, 0, 0
if (len(a) >= 8):
	for i in a:
		if (i.islower()):
			l+=1		
		if (i.isupper()):
			u+=1		
		if (i.isdigit()):
			d+=1		
		if(i=='@'or i=='$' or i=='_'or i=='#'):
			p+=1		
else:
	print("Given string is Invalid Password")
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(a)):
	print("Given string is Valid Password")
else:
	print("Given string is Invalid Password")

#3Write a Python program to find the roots of a quadratic equation
import cmath
a = int(input())
b = int(input())
c = int(input())
d = b*b - 4*a*c
sol1 = (-b + cmath.sqrt(d))/2*a
sol2 = (-b - cmath.sqrt(d))/2*a
print(f"The solution of the root is {sol1} and {sol2}")

#4Write a Python program to find the greatest common divisor (GCD) of three numbers
a = int(input())
b = int(input())
c = int(input())
print(f"Enter the two Number: {a}, {b} and {c}.")
if(a<b and a<c):
  n=a
elif(b<a and b<c):
  n=b
else:
  n=c
for i in range (1,n+1):
  if((a%i==0) and (b%i==0) and (c%i==0)):
    GCD=i
print(f"The GCD of two Numbers is {GCD}.")

#5Write a Python program to find the average of a list of numbers
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
sum = 0
for i in lst:
    sum = lst[i] + sum
avg = sum/n
print("The average of the elements in the list is ",avg)

#6Write a Python program to check if a given number is a perfect square or not
a = int(input())
print(f"Enter the Number: {a}")
flag =1
for i in range(1,a):
    if((i*i)==a):
        flag = 0
if(flag == 0):
    print("It is a Perfect Square.")
else:
        print("It is not a Perfect Square")
        
#7Write a Python program to find the largest prime number less than a given number

#8Write a Python program to check if a given string is a valid email address.
import re  
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')  
def emailValid(email):  
    if re.fullmatch(regex, email):  
      print("The given mail is valid")  
    else:  
      print("The given mail is invalid")  
emailValid("sachin.sharma@gmail.com")  
#9Write a Python program to find the sum of all even numbers in a list
lst = []
n = int(input("Enter number of elements : "))
sum=0
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
for i in range(0,n):
    if(lst[i]%2==0):
        sum = lst[i]+sum
print("Sum of Even Elements in the List:",sum)

#10Write a Python program to find the sum of all odd numbers in a list
lst = []
n = int(input("Enter number of elements : "))
sum=0
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
for i in range(0,n):
    if(lst[i]%2==1):
        sum = lst[i]+sum
print("Sum of Odd Elements in the List:",sum)

#11Write a Python program to check if a given number is divisible by 3 or 5
a = int(input("Enter the number:"))
if((a%3==0) and (a%5==0)):
    print("It is divisible by both 3 and 5")
elif (a%3==0):
    print("It is divisible by 3")
elif(a%5==0):
    print("It is divisible by 5")
else:
    print("It is neither divisible by 3 nor 5")

#12Write a Python program to check if a given character is a vowel or consonant
a = input()
print("Enter the Alphabet:{a}")
count = 0
for i in a:
    if((i=='a') or (i=='e') or (i =='i') or (i=='o') or (i== 'u')):
        print (f"It is an Vowel")
    else:
        print("It is a Consonent")

#13Write a Python program to check if a given string is a palindrome or not.
str = input()
a=0
for i in range(0, int(len(str)/2)):
	if str[i] != str[len(str)-i-1]:
		a=1
if(a==0):		
	print("It is Palindrome.")
else:
	print("It is not a Palindrome.")
    
#14Write a Python program to find the smallest of three numbers
a = int(input())
b = int(input())
c = int(input())
print(f"Entered Numbers are {a}, {b} and {c}")
if((a<b) and (a<c)):
    print(f"{a} is the smallest number.")
elif((b<a) and (b<c)):
    print(f"{b} is the smallest number.")
else:
    print(f"{c} is the smallest number")

#15Write a Python program to check if a given number is prime or not
a = int(input())
print(f"Enter the Number: {a}")
count = 0
if(a==0 or a==1):
    print(f"Please Enter a valid Number")
elif(a==2):
    print("2 is a Even Prime Number")
else:
    for i in range(2,a):
        if(a%i==0):
            count = count + 1
    if(count>0):
        print(f"{a} is not a Prime Number")
    else:
        print(f"{a} is a Prime Number")

#16Write a Python program to check if a number is even or odd.
a = int(input())
print(f"Entered Number: ")
if((a==0)):
    print(f"{a} is ZERO.")
elif(a%2==0):
    print(f"{a} is the Even number.")
else:
    print(f"{a} is the Odd number")

#17Write a Python program to check if a year is a leap year or not
a = int(input())
print(f"Entered Number: ")
if (a % 400 == 0): 
    print(f"{a} is a leap year.")
elif (a % 100 == 0):
    print(f"{a} is not a leap year.")
elif (a % 4 == 0):
    print(f"{a} is a leap year.")
else:
    print(f"{a} is not a leap year.")
#if(((year%4==0) && ((year%400==0) || (year%100!==0))  

#18Write a Python program to find the largest of three numbers
a = int(input())
b = int(input())
c = int(input())
print(f"Entered Numbers are {a}, {b} and {c}")
if((a>b) and (a>c)):
    print(f"{a} is the largest number.")
elif((b>a) and (b>c)):
    print(f"{b} is the largest number.")
else:
    print(f"{c} is the largest number")

#19Write a Python program to check if a number is positive, negative or zero
a = int(input())
print(f"Entered Number: ")
if((a==0)):
    print(f"{a} is ZERO.")
elif(a<0):
    print(f"{a} is the Negative Number.")
else:
    print(f"{a} is the Positive Number")
