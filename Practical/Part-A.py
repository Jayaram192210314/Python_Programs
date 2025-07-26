#1)Given an array of integer nums and an integer target, return indices of the two numbers such that they
#add up to the target. You may assume that each input would have exactly one solution, and you may
#not use the same element twice. You can return the answer in any order.
#Test Case 1: Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Test Case 2: Input: nums = [3,2,4], target = 6
#Output: [1,2]
nums = [2,7,11,13]
t = int(input("Enter the Target:"))
l=len(nums)
for i in range (0,l):
    for j in range (0,l):
       sum = nums[i] + nums[j]
       if(sum == t):
        a=i
        b=j
if(a<b):
  print(a,b)
else:
  print(b,a)
#2)Given an integer x, return true if x is a palindrome and false otherwise.
#Test Case 1: Input: x = 121
#Output: true
#Test Case 2: Input: -121
#Output:false
  t = int(input("Enter the input:"))
rem = 0
rev = 0
num = t
if(num<0):
    print("False")
elif(num>0):
     while(t!=0):
        rem = t % 10
        rev = rev*10 + rem
        t = t//10
if(num == rev):
    print("True")
else:
    print("False")
#3)Write a function to find the longest common prefix string amongst an array of strings. If there is no
#common prefix, return an empty string ””.
#Test Case 1: Input: strs = [“flower”,“flow”,“flight”]
#Output: ”fl”
#Test Case 2: Input: strs = [“dog”,“racecar”,“car”]
#Output: ””
def longest_common_prefix(strs):
    if not strs:
        return ""
    strs.sort()
    first_str = strs[0]
    last_str = strs[-1]
    common_prefix = []
    for i in range(len(first_str)):
        if i < len(last_str) and first_str[i] == last_str[i]:
            common_prefix.append(first_str[i])
        else:
            break
    return "".join(common_prefix)
strs1 = ["flower", "flow", "flight"]
output1 = longest_common_prefix(strs1)
print(f"Test Case 1: {output1}")  
strs2 = ["dog", "racecar", "car"]
output2 = longest_common_prefix(strs2)
print(f"Test Case 2: {output2}") 
#4)Given a string s containing just the characters ’(’, ’)’, ’’, ’’, ’[’ and ’]’, determine if the input string is
#valid. An input string is valid if: Open brackets must be closed by the same type of brackets. Open
#brackets must be closed in the correct order. Every close bracket has a corresponding open bracket of
#the same type.
#Test Case 1: Input: s = ”()[]”
#Output: true
#Test Case 2: Input: s = ”(]”
#Output: false
def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            continue
    return not stack
s1 = "()[]"
output1 = is_valid(s1)
print(f"Test Case 1: {output1}")  # Output: True
s2 = "(]"
output2 = is_valid(s2)
print(f"Test Case 2: {output2}")  # Output: False
#5)You are given the two sorted lists, list 1 and list 2. Merge the two lists into one sorted list. The list
#should be made by splicing together the elements of the first two lists. Return the merged list.
#Test Case 1: Input: list1 = [1,2,4], list2 = [1,3,4]
#Output: [1,1,2,3,4,4]
#Test Case 2: Input: list1 = [], list2 = [0]
#Output: [0]
def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list
list1_1 = [1, 2, 4]
list2_1 = [1, 3, 4]
output1 = merge_sorted_lists(list1_1, list2_1)
print(f"Test Case 1: {output1}")
list1_2 = []
list2_2 = [0]
output2 = merge_sorted_lists(list1_2, list2_2)
print(f"Test Case 2: {output2}")
#6)Given an integer array of nums and an integer value, remove all occurrences of val in nums in place. The
#order of the elements may be changed. Then, return the number of elements in nums that are not equal
#to value. Consider the number of elements in nums which are not equal to val be k, to get accepted, you
#need to do the following things: Change the array nums such that the first k elements of nums contain
#the elements which are not equal to val. The remaining elements of nums are not essential, nor is the
#size of nums. Return k.
#Test Case 1: Input: nums = [3,2,2,3], val = 3
#Output: 2, nums = [2,2, , ]
#Test Case 2: Input: nums = [0,1,2,2,3,0,4,2], val = 2
#Output: 5, nums = [0,1,4,0,3, , , ]
def remove_element(nums, val):
    if not nums:
        return 0
    left, right = 0, 0
    while right < len(nums):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1
        right += 1
    return left
nums1 = [3, 2, 2, 3]
val1 = 3
output1 = remove_element(nums1, val1)
print(f"Test Case 1: {output1}, nums = {nums1[:output1]}") 
nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
val2 = 2
output2 = remove_element(nums2, val2)
print(f"Test Case 2: {output2}, nums = {nums2[:output2]}")  
#7)Given two strings, needle and haystack, return the index of the first occurrence of needle in a haystack,
#or -1 if the needle is not part of the haystack.
#Test Case 1: Input: haystack = “sadbutsad”, needle = “sad”
#Output: 0
#Test Case 2: Input: haystack = “leetcode”, needle = “leeto”
#Output: -1
def strStr(haystack, needle):
    index = haystack.find(needle)
    return index
haystack1 = "sadbutsad"
needle1 = "sad"
output1 = strStr(haystack1, needle1)
print(f"Test Case 1: {output1}")  
haystack2 = "leetcode"
needle2 = "leeto"
output2 = strStr(haystack2, needle2)
print(f"Test Case 2: {output2}")  
#8)Given a sorted array of distinct integers and a target value, return the index if the target is found. If
#not, return the index where it would be if inserted in order. You must write an algorithm with O(log n)
#runtime complexity.
#Test Case 1: Input: nums = [1,3,5,6], target = 5
#Output: 2
#Test Case 2: Input: nums = [1,3,5,6], target = 2
#Output: 1
def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left 
nums1 = [1, 3, 5, 6]
target1 = 5
output1 = search_insert(nums1, target1)
print(f"Test Case 1: {output1}")  
nums2 = [1, 3, 5, 6]
target2 = 2
output2 = search_insert(nums2, target2)
print(f"Test Case 2: {output2}")  
#9)Given a string s consisting of words and spaces, return the length of the last word in the string. A word
#is a maximal substring consisting of non-space characters only.
#Test Case 1: Input: s = “Hello World”
#Output: 5
#Test Case 2: Input: s = “ fly me to the moon ”
#Output: 4
def length_of_last_word(s):
    words = s.split()
    if words:
        return len(words[-1])
    else:
        return 0
s1 = "Hello World"
output1 = length_of_last_word(s1)
print(f"Test Case 1: {output1}")  
s2 = " fly me to the moon "
output2 = length_of_last_word(s2)
print(f"Test Case 2: {output2}") 
#10)You are given a large integer represented as an integer array of digits, where each digit [i] is the ith digit
#of the integer. The digits are ordered from most significant to least significant in left-to-right order. The
#large integer does not contain any leading 0s. Increment the large integer by one and return the resulting
#array of digits.
#Test Case 1: Input: digits = [1,2,3]
#Output: [1,2,4]
#Test Case 2: Input: digits = [4,3,2,1]
#Output: [4,3,2,2]
def increment_large_integer(digits):
    n = len(digits)
    carry = 1
    for i in range(n - 1, -1, -1):
        current_sum = digits[i] + carry
        digits[i] = current_sum % 10
        carry = current_sum // 10
    if carry:
        digits.insert(0, carry)
    return digits
digits1 = [1, 2, 3]
output1 = increment_large_integer(digits1)
print(f"Test Case 1: {output1}") 
digits2 = [4, 3, 2, 1]
output2 = increment_large_integer(digits2)
print(f"Test Case 2: {output2}") 
#11)Given two binary strings a and b, return their sum as a binary string.
#Test Case 1: Input: a = “11”, b = “1”
#Output: “100”
#Test Case 2: Input: a = “1010”, b = “1011”
#Output: “10101”
def add_binary(a, b):
    result = ""
    carry = 0
    a = a.zfill(max(len(a), len(b)))
    b = b.zfill(max(len(a), len(b)))
    for i in range(len(a) - 1, -1, -1):
        bit_sum = int(a[i]) + int(b[i]) + carry
        result = str(bit_sum % 2) + result
        carry = bit_sum // 2
    if carry:
        result = "1" + result
    return result
a1 = "11"
b1 = "1"
output1 = add_binary(a1, b1)
print(f"Test Case 1: {output1}") 
a2 = "1010"
b2 = "1011"
output2 = add_binary(a2, b2)
print(f"Test Case 2: {output2}")  
#12)Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The
#returned integer should be non-negative as well. It would help if you did not use any built-in exponent
#function or operator.
#Test Case 1: Input: x = 4
#Output: 2
#Test Case 2: Input: x = 8
#Output: 2
def my_sqrt(x):
    if x == 0:
        return 0
    left, right = 1, x
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    return right
x1 = 4
output1 = my_sqrt(x1)
print(f"Test Case 1: {output1}") 
x2 = 8
output2 = my_sqrt(x2)
print(f"Test Case 2: {output2}") 
#13)You are climbing a staircase. It takes n steps to reach the top. Each time, you can climb either 1 or 2
#steps. In how many distinct ways can you rise to the top?
#Test Case 1: Input: n = 3
#Output: 3
#Test Case 2: Input: n =5
#Output: 8
def climb_stairs(n):
    if n <= 2:
        return n
    ways = [0] * (n + 1)
    ways[1] = 1
    ways[2] = 2
    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
    return ways[n]
n1 = 3
output1 = climb_stairs(n1)
print(f"Test Case 1: {output1}")  
n2 = 5
output2 = climb_stairs(n2)
print(f"Test Case 2: {output2}")  
#14)Given the head of a sorted list, delete all duplicates so each element appears only once. Return the linked
#list sorted as well.
#Test Case 1: Input: head = [1,1,2]
#Output: [1,2]
#Test Case 2: Input: head = [1,1,2,3,3]
#Output: [1,2,3]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def delete_duplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head
def print_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result
head1 = ListNode(1, ListNode(1, ListNode(2)))
result1 = delete_duplicates(head1)
print(f"Test Case 1: {print_list(result1)}")  
head2 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))
result2 = delete_duplicates(head2)
print(f"Test Case 2: {print_list(result2)}")  
#15)You are given two integer arrays, nums1, and nums2, sorted in non-decreasing order, and two integers,
#m, and n, representing the number of elements in nums1 and nums2, respectively. Merge nums1 and
#nums2 into a single array, num1 sorted in non-decreasing order.
#Test Case 1: Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
#Output: [1,2,2,3,5,6]
#Test Case 2: Input: nums1 = [1], m = 1, nums2 = [], n = 0
#Output: [1]
def merge(nums1, m, nums2, n):
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
nums1_1 = [1, 2, 3, 0, 0, 0]
m1 = 3
nums2_1 = [2, 5, 6]
n1 = 3
merge(nums1_1, m1, nums2_1, n1)
print(f"Test Case 1: {nums1_1}")  
nums1_2 = [1]
m2 = 1
nums2_2 = []
n2 = 0
merge(nums1_2, m2, nums2_2, n2)
print(f"Test Case 2: {nums1_2}")  
#16)Given an integer numRows, return the first numRows of Pascal’s triangle. In Pascal’s triangle, each
#number is the sum of the two numbers directly above it
#Test Case 1: Input: numRows = 5
#Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#Test Case 2: Input: numRows = 1
#Output: [[1]]
def pascals(numRows):
    if numRows == 0:
        return []
    triangle = [[1]]
    for i in range(1, numRows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle
numRows1 = 5
output1 = pascals(numRows1)
print(f"Test Case 1: Input: numRows = {numRows1}\nOutput: {output1}")
numRows2 = 1
output2 = pascals(numRows2)
print(f"Test Case 2: Input: numRows = {numRows2}\nOutput: {output2}")
#17)maximize your profit by choosing a single day to buy one stock and a different day to sell that stock in
#the future. Return the maximum profit you can achieve from this transaction. If you cannot accomplish
#any profit, return 0.
#Test Case 1: Input: prices = [7,1,5,3,6,4]
#Output: 5
#Test Case 2: Input: [7,6,4,3,1]
#Output: 0
def max_profit(prices):
    if not prices or len(prices) == 1:
        return 0
    max_profit = 0
    min_price = prices[0]
    for price in prices[1:]:
        profit = price - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, price)
    return max_profit
prices1 = [7, 1, 5, 3, 6, 4]
output1 = max_profit(prices1)
print(f"Test Case 1: Input: prices = {prices1}\nOutput: {output1}")
prices2 = [7, 6, 4, 3, 1]
output2 = max_profit(prices2)
print(f"Test Case 2: Input: prices = {prices2}\nOutput: {output2}")
#18)A phrase is a palindrome if it reads the same forward and backward after converting all uppercase letters
#into lowercase letters and removing all non-alphanumeric characters. Alphanumeric characters include
#letters and numbers. Given a string s, return true if it is a palindrome or false otherwise.
#Test Case 1: Input: s = “A man, a plan, a canal: Panama”
#Output: true
#Test Case 2: Input: s = “race a car”
#Output: false
def is_palindrome(s):
    clean_s = ''.join(c.lower() for c in s if c.isalnum())
    return clean_s == clean_s[::-1]
s1 = "A man, a plan, a canal: Panama"
output1 = is_palindrome(s1)
print(f"Test Case 1: Input: s = \"{s1}\"\nOutput: {output1}")
s2 = "race a car"
output2 = is_palindrome(s2)
print(f"Test Case 2: Input: s = \"{s2}\"\nOutput: {output2}")
#19)Given a non-empty array of integers nums, every element appears twice except for one. Find that single
#one. You must implement a solution with a linear runtime complexity and use only constant extra space.
#Test Case 1: Input: nums = [2,2,1]
#Output: 1
#Test Case 2: Input: nums = [4,1,2,1,2]
#Output: 4
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
nums1 = [2, 2, 1]
output1 = single_number(nums1)
print(f"Test Case 1: Input: nums = {nums1}\nOutput: {output1}")
nums2 = [4, 1, 2, 1, 2]
output2 = single_number(nums2)
print(f"Test Case 2: Input: nums = {nums2}\nOutput: {output2}")
#20)Write a function that takes the binary representation of an unsigned integer and returns the number of
#’1’ bits it has (also known as the Hamming weight).
#Test Case 1: Input: n = 00000000000000000000000000001011
#Output: 3
#Test Case 2: Input: n = 00000000000000000000000010000000
#Output: 1
def hamming_weight(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
n1 = 0b00000000000000000000000000001011
output1 = hamming_weight(n1)
print(f"Test Case 1: Input: n = {bin(n1)}\nOutput: {output1}")
n2 = 0b00000000000000000000000010000000
output2 = hamming_weight(n2)
print(f"Test Case 2: Input: n = {bin(n2)}\nOutput: {output2}")
#21)Given an integer n, return an array ans of length n + 1 such that for each i (0 ¡= i ¡= n), ans[i] is the
#number of 1’s in the binary representation of i.
#Test Case 1: Input: n = 2
#Output: [0,1,1]
#Test Case 2: Input: n = 5
#Output: [0,1,1,2,1,2]
def move_zeros(nums):
    non_zero_index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
            non_zero_index += 1
nums1 = [0, 1, 0, 3, 12]
move_zeros(nums1)
print(f"Test Case 1: Input: nums = {nums1}\nOutput: {nums1}")
nums2 = [0]
move_zeros(nums2)
print(f"Test Case 2: Input: nums = {nums2}\nOutput: {nums2}")
#22)Given an array nums containing n distinct numbers in the range [0, n], return the only number in the
#range that is missing from the array.
#Test Case 1: Input: nums = [3,0,1]
#Output: 2
#Test Case 2: Input: nums = [9,6,4,2,3,5,7,0,1]
#Output: 8
def word_pattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    char_to_word = {}
    word_to_char = {}
    for char, word in zip(pattern, words):
        if char not in char_to_word and word not in word_to_char:
            char_to_word[char] = word
            word_to_char[word] = char
        elif char_to_word.get(char) != word or word_to_char.get(word) != char:
            return False
    return True
pattern1 = "abba"
s1 = "dog cat cat dog"
output1 = word_pattern(pattern1, s1)
print(f"Test Case 1: Input: pattern = \"{pattern1}\", s = \"{s1}\"\nOutput: {output1}")
pattern2 = "abba"
s2 = "dog cat cat fish"
output2 = word_pattern(pattern2, s2)
print(f"Test Case 2: Input: pattern = \"{pattern2}\", s = \"{s2}\"\nOutput: {output2}")
#23)Given an integer array nums, move all 0’s to the end of it while maintaining the relative order of the
#non-zero elements. Note that you must do this in-place without making a copy of the array.
#Test Case 1: Input: nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]
#Test Case 2: Input: nums = [0]
#Output: [0]
def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
s1 = ["h", "e", "l", "l", "o"]
reverse_string(s1)
print(f"Test Case 1: Input: s = {s1}\nOutput: {s1}")
s2 = ["H", "a", "n", "n", "a", "h"]
reverse_string(s2)
print(f"Test Case 2: Input: s = {s2}\nOutput: {s2}")
#24)Given a pattern and a string s, find if s follows the same pattern. Here follow means a full match, such
#that there is a bijection between a letter in pattern and a non-empty word in s.
#Test Case 1: Input: pattern = ”abba”, s = ”dog cat cat dog”
#Output: true
#Test Case 2: Input: pattern = ”abba”, s = ”dog cat cat fish”
#Output: false
def reverse_vowels(s):
    vowels = set("aeiouAEIOU")
    s = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and s[left].lower() not in vowels:
            left += 1
        while left < right and s[right].lower() not in vowels:
            right -= 1
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)
s1 = "hello"
output1 = reverse_vowels(s1)
print(f"Test Case 1: Input: s = \"{s1}\"\nOutput: \"{output1}\"")
s2 = "leetcode"
output2 = reverse_vowels(s2)
print(f"Test Case 2: Input: s = \"{s2}\"\nOutput: \"{output2}\"")
#25)Given an integer n, return true if it is a power of three. Otherwise, return false. An integer n is a power
#of three if an integer x exists such that n == 3x.
#Test Case 1: Input: n = 27
#Output: true
#Test Case 2: Input: n = 0
#Output: false
import math
n = int(input("Enter the Number:"))
x = n//2
flag =1
if(n==3):
    flag =0
for i in range(0,x):
    if(pow(3,i)==n):
        flag = 0
        break
if(flag==0):
    print("true")
else:
    print("false")
#26)Given an integer n, return true if it is a power of four. Otherwise, return false. An integer n is a power
#of four, if an integer x exists such that n == 4x.
#Test Case 1: Input: n = 16
#Output: true
#Test Case 2: Input: n = 5
#Output: false
import math
n = int(input("Enter the Number:"))
x = n//2
flag =1
if(n==4):
    flag =0
for i in range(0,x):
    if(pow(4,i)==n):
        flag = 0
        break
if(flag==0):
    print("true")
else:
    print("false")
#27)Write a function that reverses a string. The input string is given as an array of characters s. You must
#modify the input array in place with O(1) extra memory.
#Test Case 1: Input: s = [”h”,”e”,”l”,”l”,”o”]
#Output: [”o”,”l”,”l”,”e”,”h”]
#Test Case 2: Input: s = [”H”,”a”,”n”,”n”,”a”,”h”]
#Output: [”h”,”a”,”n”,”n”,”a”,”H”]
s = ["h","e","l","l","o"]
s.reverse()
print(s)