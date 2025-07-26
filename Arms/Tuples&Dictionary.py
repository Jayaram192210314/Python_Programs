#Tuples and Dictionary
#Write a Python program to convert a dictionary to a list of tuples.
#Write a Python program to sort a given dictionary by its values.
#Write a Python program to find the frequency of all elements in a given dictionary.
#Write a Python program to find the keys with the maximum and minimum values in a given dictionary.
#Write a Python program to find the maximum and minimum values in a given dictionary.
#Write a Python program to remove a given key from a given dictionary.
#Write a Python program to check if a given value exists in a given dictionary.
#Write a Python program to concatenate two dictionaries.
#Write a Python program to check if a given key exists in a given dictionary.
#Write a Python program to find the length of a given dictionary.
a = {1:"jayaram",2:"vijay",3:"krishna",4:"karthick",5:"mahesh"}
print(len(a))

#Write a Python program to sort a given tuple in ascending order.
#Write a Python program to find the sum of all elements in a given tuple.
a = (1,2,3,4,5,6)
sum =0
for i in a:
  sum = sum + i
print(f"The sum of the numbers in tuple is {sum}")

#Write a Python program to convert a list of tuples to a list of lists.


#Write a Python program to check if a given element exists in a given tuple.
a = (12,3,4,5)
print(2 in a)

#Write a Python program to convert a tuple to a list.
tuple = (1, 2, 3)
print(type(tuple))
print(tuple)
list = list(tuple)
print(type(list))
print(list)

#Write a Python program to find the index of a given element in a given tuple.
a = (1,2,3,4,5)
print(a.index(4))

#Write a Python program to concatenate two tuples.
a = (1,2,3)
b = (4,5,6)
c = a + b
print(c)

#Write a Python program to find the maximum and minimum elements in a given tuple.
a = (1,2,3,4,5)
print(f"maximum number in tuple: {max(a)}")
print(f"minimum number in tuple: {min(a)}")

#Write a Python program to reverse a given tuple.
a = (9,8,6,5,1)
a.sort()
print(a)

#Write a Python program to find the length of a given tuple
a = (1,2,3,4,5)
print(len(a))