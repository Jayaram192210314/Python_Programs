#20Write a Python program to find the LCM of two numbers using a while loop.
a = int(input())
b = int(input())
print(f"Enter the two Number: {a}, {b}")
i=1
if(a<b):
  n=a
else:
  n=b
while(i<n+1):
  if((a%i==0) and (b%i==0)):
    GCD=i
  i = i +1  
LCM = (a*b)//GCD
print(f"The LCM of two Numbers is {LCM}")

#21Write a Python program to generate a Pascal's triangle using nested loops.

#22Write a Python program to check if a given string is a palindrome or not using a for loop.
str = input()
a=0
for i in range(0, int(len(str)/2)):
	if str[i] != str[len(str)-i-1]:
		a=1
if(a==0):		
	print("It is Palindrome.")
else:
	print("It is not a Palindrome.")

#23Write a Python program to find the first n Fibonacci numbers using a for loop.
a = int(input())
print(f"Enter the Number: {a}")
n1,n2 = 0,1
if (a<=0):
    print("Please enter the valid number")
elif(a==1):
    print(f"The Fibinacci Number: {n1}")
else:
    print("The Fibinacci Series: ")
    for i in range (0,a):
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3

#24Write a Python program to print the sum of digits of a given number using a while loop.
a = int(input())
print(f"Enter the Number: {a}")
sum,rem = 0,0
while(a!=0):
    rem = a % 10
    sum = sum + rem
    a = a / 10
print(f"The sum of the digits in the number: {int(sum)}")

#25Write a Python program to check if a given number is prime or not using a for loop.
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

#26Write a Python program to find the sum of all odd numbers between two given numbers using a while loop.
a= int(input())
b=int(input())
print(f"The lower limit and Upper limit of  the set is {a} and {b}")
sum =0
while(a<=b):
    if (a%2==1):
        sum = sum + a
    a=a+1
print(f"The sum of odd numbers in set is {sum}")

#27Write a Python program to find the GCD of two numbers using a for loop.
a = int(input())
b = int(input())
print(f"Enter the two Number: {a}, {b}")
if(a<b):
  n=a
else:
  n=b
for i in range (1,n+1):
  if((a%i==0) and (b%i==0)):
    GCD=i
print(f"The GCD of two Numbers is {GCD}")

#28Write a Python program to generate a multiplication table using nested loops.
a = int(input())
print(f"Enter the Table No: {a}")
for i in range (1,11):
    print(f"{a}*{i}={a*i}")

#29Write a Python program to find the factorial of a number using a for loop.
a = int(input())
print(f"Enter the number: {a}")
fact = 1
for i in range(1,a+1):
  fact = fact * i
print(f"The factorial of the Number is {fact}")

#30Write a Python program to find the sum of all even numbers between two given numbers using a while loop.
a= int(input())
b=int(input())
print(f"The lower limit and Upper limit of  the set is {a} and {b}")
sum =0
while(a<=b):
    if (a%2==0):
        sum = sum + a
    a=a+1
print(f"The sum of even numbers in set is {sum}")

#31Write a Python program to count the number of vowels in a given string using a for loop.
a = input()
print("Enter the string:{a}")
count = 0
for i in a:
    if((i=='a') or (i=='e') or (i =='i') or (i=='o') or (i== 'u')):
        count = count +1
print (f"The string consists {count} vowels.")

#32Write a Python program to check if a given number is a palindrome or not using a while loop.
a=int(input())
print(f"Enter the Number: {a}")
rev,rem = 0,0
n=a
while(a!=0):
  rem = a % 10
  rev = rev*10 + int(rem)
  a = a//10
if(n==rev):
  print(f"The given number {n} is Palindrome.")
else:
  print(f"The given number is {n} not a Palindrome")

#33Write a Python program to reverse a string using a for loop.
a = input()
k = a[::-1]
print(k)
#or

#34Write a Python program to print all the prime numbers within a given range using a for loop.
a = int(input())
b = int(input())
print(f"Enter the Lower and Higher Boundary: {a}, {b}")
for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            print(i)

#35Write a Python program to print the Fibonacci sequence up to a given number using a while loop.
a = int(input())
print(f"Enter the Number: {a}")
count = 0
n1,n2 = 0,1
if (a<=0):
    print("Please enter the valid number")
elif(a==1):
    print(f"The Fibinacci Number: {n1}")
else:
    print("The Fibinacci Series: ")
    while(count<a):
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count = count + 1

#36Write a Python program to find the factorial of a number using a while loop.
a = int(input())
print(f"Enter the Number: {a}")
b=a
fact = 1
while(a!=0):
    fact = fact * a
    a = a-1
print(f"The Factorial of the number {b} is {fact}.")

#37Write a Python program to print the multiplication table of a given number using a for loop.
a = int(input())
print(f"Enter the Table No: {a}")
for i in range (1,11):
    print(f"{a}*{i}={a*i}")

#38Write a Python program to find the sum of all the numbers in a list using a for loop.
lst = [1,2,3,4,5,6]
k=len(lst)
sum =  0
print(lst)
for i in range (0,k):
    sum = sum + lst[i]
print(f"The Sum of Elements in the list is {sum}.")

#39Write a Python program to print the numbers from 1 to 10 using a for loop.
for i in range (1,11):
    print (i)