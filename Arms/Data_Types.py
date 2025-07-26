#Data types

#union
a = {"jk","mm"}
b = {"vj","jk"}
result = a.union(b)
print(result)

#Descending
"""
def sorting(e):
  return len(e)
a = ['jayaram','mahesh','krishna','vasu']
a.sort(key=sorting,reverse = True)
print(a)
"""

#Removal of occurences
"""
a=int(input())
print(f"Enter the Number: {a}")
lst=[]
print("Enter the Elements in the List")
for i in range (0,5):
  ele = int(input())
  lst.append(ele)
print(f"The Elements in the List: {lst} ")
lst = [ele for ele in lst if ele != a]
print ("List after element removal is : " + str(lst))
"""

#intersection
"""
lst = {'1','2','3','4','5'}
lst1 = {'1','2','3','7','8'}
def inter(lst, lst1):
    lst3 = [value for value in lst if value in lst1]
    return lst3
lst = {'1','2','3','4','5'}
lst1 = {'1','2','3','7','8'}
#z = lst.intersection(lst1)
#print(z)    
print(inter(lst, lst1))   
"""

#length of string
"""
a =input()
print(f"Enter the string: {a}")
k = len(a)
print(f"The length of the string is {k}")
"""
"""
a = 'LEO'
b = 'DAS'
print(f"Before concentate {a} {b}")
print(f"After concentate {a+b}")
"""

#tuple to list
"""
tuple = (1, 2, 3)
print(type(tuple))
print(tuple)
list = list(tuple)
print(type(list))
print(list)
"""