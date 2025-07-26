def index(nums,k):
    for x in nums:
        for j in nums:
            if ((x+j)==k):
                a = nums.index(x)
                b = nums.index(j)
    if(a<b):
        return(a,b)
    else:
        return(b,a)
nums = [2,7,11,15]
k = 9
print(index(nums,k))
nums = [3,2,4]
k = 6
print(index(nums,k))


def hamming(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
n1 = 0b00000000000000000000000000001111
print(hamming(n1))
n2 = 0b00000000000000000000000010000000
print(hamming(n2))


def hamming(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count
x = int(input("Enter the Number:"))
lst = []
for i in range(0,x+1):
    lst.append(hamming(i))
print(lst)


def capital(word):
    if word == word.upper() or word == word.capitalize():
        print("true")
    else:
        print("false")
word = "USA"
capital(word)
word = "FlaG"
capital(word)
word = "Google"
capital(word)
word = "jayaram"
capital(word)


nums = [5]
nums1 = (sorted(nums))
a = len(nums)
sum = 0
k = int(input("Enter the Number:"))
if k<2:
    for x in nums1:
        sum = sum + x
    y = sum/k
    print(y)
else:
    for i in range(1,a-1):
        sum = sum + nums[i]
    y = sum/k
    print(y)


def add(nums1,nums2):
    a = len(nums1)
    lst = []
    for i in range(0,a):
        k = nums1[i] + nums2[i]
        if (k>=10):
            nums1[i + 1] = nums1[i+1] + 1
            lst.append(0) 
        else:
            lst.append(k)
    print(lst)
nums1 = [2,4,3]
nums2 = [5,6,4]
add(nums1,nums2)
nums1 = [0]
nums2 = [0]
add(nums1,nums2)


def spiral_matrix(n):
    mat = [[0] * n for _ in range(n)]  
    t,l = 0,0
    b,r = n - 1, n - 1
    num = 1  
    while num <= n * n:
        for i in range(l, r + 1):
            mat[t][i] = num
            num += 1
        t += 1
        for i in range(t, b + 1):
            mat[i][r] = num
            num += 1
        r -= 1
        for i in range(r, l - 1, -1):
            mat[b][i] = num
            num += 1
        b -= 1
        for i in range(b, t - 1, -1):
            mat[i][l] = num
            num += 1
        l += 1
    return mat
n = int(input("Enter the Number:"))
matrix = spiral_matrix(n)
for row in matrix:
    print(row)


from itertools import permutations
def com(s):
    all = ["".join(comb)for comb in permutations(s, 3)]
s = "ADOBECODEBANC"
t = "ABC"
if s.find(t):
    print(t)
else:
    print("None")
com(s)