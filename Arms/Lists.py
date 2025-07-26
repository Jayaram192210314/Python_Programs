#List
#Write a Python program to find the kth smallest element in a given list.
def find_k_smallest(arr, n, k):  
    for i in range(0, n):  
        for j in range(0,n-i-1):  
            if arr[j] > arr[j+1]:  
                arr[j], arr[j+1] = arr[j], arr[j+1]  
                  
    return arr[k-1]   
arr = [7, 10, 4, 3, 20, 15]  
n = len(arr)  
k = 3  
print("kth smallest array element is:", find_k_smallest(arr, n, k))  

#Write a Python program to find the difference between two lists.
li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35]
temp3 = []
for element in li1:
	if element not in li2:
		temp3.append(element)
print(temp3)

#Write a Python program to find the intersection of two lists.
def Intersection(lst1, lst2):
	return set(lst1).intersection(lst2)
lst1 = [ 4, 9, 1, 17, 11, 26, 28, 28, 26, 66, 91]
lst2 = [9, 9, 74, 21, 45, 11, 63]
print(Intersection(lst1, lst2))

#Write a Python program to find the union of two lists.
def Union(lst1, lst2):
	final_list = sorted(lst1 + lst2)
	return final_list
lst1 = [23, 15, 2, 14, 14, 16, 20 ,52]
lst2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(Union(lst1, lst2))

#Write a Python program to find the common elements between two lists.
def common_member(a, b): 
	a_set = set(a)
	b_set = set(b)
	if len(a_set.intersection(b_set)) > 0:
		return(a_set.intersection(b_set)) 
	else:
		return("no common elements")
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_member(a, b))

#Write a Python program to find the first n Fibonacci numbers and store them in a list.
n = int(input("Enter the Number:"))
n1 = 0
n2 = 1
l = []
l.append(n1)
l.append(n2)
for i in range(0,n-2):
  n3 = n1 +n2
  l.append(n3)
  n1=n2
  n2=n3
print(l)

#Write a Python program to find the largest subsequence sum in a given list of integers.


#Write a Python program to merge two sorted lists into a single sorted list.
test_list1 = [1, 5, 6, 9, 11]
test_list2 = [3, 4, 7, 8, 10]
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2))
res = sorted(test_list1 + test_list2)
print ("The combined sorted list is : " + str(res))

#Write a Python program to remove all even numbers from a given list.
def remove_even(x):
    for i in x[:]:
        if (i % 2) == 0:
            x.remove(i)
    return x
a = [12, 15, 7, 9]
print(remove_even(a))

#Write a Python program to find the maximum and minimum elements in a given list.
test_list1 = [1, 3, 4, 5, 2, 6]
test_list2 = [3, 4, 8, 3, 10, 1]
print ("The original list 1 is : " + str(test_list1))
print ("The original list 2 is : " + str(test_list2)) 
max_all = max(test_list1 + test_list2)
min_all = min(test_list1 + test_list2)
print ("The maximum of both lists is : " + str(max_all))
print ("The minimum of both lists is : " + str(min_all))

#Write a Python program to shuffle a given list.
import random
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)

#Write a Python program to concatenate two lists.
list_1 = [1, 'a']
list_2 = [1, 2, 3]
list_2.extend(list_1)
print(list_2)
#(or)
list_1 = [1, 'a']
list_2 = [3, 4, 5]
list_joined = list_1 + list_2
print(list_joined)
#(or)
list_1 = [1, 'a']
list_2 = range(2, 4)
list_joined = [*list_1, *list_2]
print(list_joined)

#Write a Python program to sort a given list in ascending order.
alphabets = ['a','e','d','c','b'] 
alphabets.sort() 
print(alphabets) 
random_numbers = [2,5,6,1,8,3] 
random_numbers.sort() 
print(random_numbers)

#Write a Python program to find the frequency of all elements in a given list.
test_list1 = [4, 6, 8, 9, 10]
test_list2 = [4, 6, 6, 5, 8, 10, 4, 9, 8, 10, 1]
print("The original list 1 : " + str(test_list1))
print("The original list 2 : " + str(test_list2))
res = {key: test_list2.count(key) for key in test_list1}
print("Lists elements Frequency : " + str(res))

#Write a Python program to find the index of a given element in a given list.
fruits = ["apple", "banana","cherry","apple"] 
print(fruits.index("apple"))

#Write a Python program to reverse a given list.
"Reversing a list using slicing technique"
def Reverse(lst):
	new_lst = lst[::-1]
	return new_lst
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))
#(or)
lst = [10, 11, 12, 13, 14, 15]
lst.reverse()
print("Using reverse() ", lst)
print("Using reversed() ", list(reversed(lst)))

#Write a Python program to remove duplicates from a given list.
duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
print(list(set(duplicate)))
#(or)
input_list = [1, 2, 3, 2, 6, 3, 5, 3, 7, 8]
mylist = list(dict.fromkeys(input_list))
print(mylist)

#Write a Python program to find the smallest number in a given list.
list1 = [10, 20, 4, 45, 99]
list1.sort(reverse=True)
print("Smallest element is:", list1[-1])

#Write a Python program to find the second largest number in a given list.
list1 = [10, 20, 4, 45, 99]
new_list = set(list1)
new_list.remove(max(new_list))
print(max(new_list))

#Write a Python program to find the sum of all elements in a given list.
total = 0
list1 = [11, 5, 17, 18, 23]
for ele in range(0, len(list1)):
	total = total + list1[ele]
print("Sum of all elements in given list: ", total)