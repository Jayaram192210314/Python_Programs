date = input("Enter the date to be checked: ")
c=date.split("/")
b = list(map(int,c))
input_year=(b[2])
if(input_year%4 == 0):
    if(input_year%100 == 0):
        if(input_year%400 == 0):
            print("%d is Leap Year" %input_year)
        else:
            print("%d is not the Leap Year" %input_year)
    else:
        print("%d is the Leap Year" %input_year)
else:
    print("%d is not the Leap Year" %input_year)

x=input_year%4
if x!=0:
    print("Previous Leap year:", input_year-x)
else:
    print("Next leap year:", input_year+4)



pattern = "abba"
s = "dog cat cat dog"
mapping = {}
print(all(mapping.setdefault(char, word) == word for char, word in zip(pattern, s.split()) if mapping.get(char) == word))
"""
"""
nums = [1,3,5,4,7]
Max = 0
x = 0
j = 1
l = len(nums)
for i in range(0,l):
    if (nums[i] < nums[j]):
        j = j+1
        x += 1
        Max = max(Max, x)
    else:
        x = 0
print(f"The maximum subsequent array is: {Max+1}")

#pythogoreas triplet




def happy(n):
    temp=n
    sum=0
    while temp>0:
        digit=temp%10
        sum=digit**2+sum
        temp=temp//10
    return sum
    
# Main Program

num=int(input("Enter the number:"))
result=num
while result!=1 and result!=4:
    result=(happy(result))
if result==1:
    print("True")
elif result==4:
    print("False")



def find_added_letter(s, t):
    s_count = {}
    t_count = {}
    for char in s:
        s_count[char] = s_count.get(char, 0) + 1
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1
    for char in t_count:
        if char not in s_count or t_count[char] > s_count[char]:
            return char
print(find_added_letter("abcd", "abced")) 
print(find_added_letter("", "y"))  


string='''This is the most straightforward way to count the number
of lines in a text file in Python. The readlines() method reads all
lines from a file and stores it in a list. Next, use the len() function
to find the length of the list which is nothing but total lines present in a file.'''
str1=string.split(".")
str1.pop()
print("Number of lines: ",len(str1))
print("Number of words in each line:")
for i in range(len(str1)):
    words=str1[i].split()
    #print(words)
    print("Line",i+1,len(words))

#23.	Armstrong number
#24.	Harshad number
#25.	Happy number
#26.	strong number
#27.	buzz number
#28.	neon number
#29.	abundant number
#30.	narcissistic number                                                                                                                                          *                                                                                                                                                                          **                                                                                                                                                                                  ***                                                                                                                                                                       ****                                                                                                                                                                         *****
#33.	Print pascal triangle pattern nested for loop



#isomorphic
#pascal
#permutations and combinations
#Write a Python program to check if a given string is a valid password using a lambda function
#Write a Python program to find the length of the longest word in a given sentence using a reduce function
#Write a Python program to concatenate two lists using a generator function


