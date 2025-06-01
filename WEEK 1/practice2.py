#Find the second largest number in a list
#Input: [4, 1, 9, 7, 9] → Output: 7
l= [4, 1, 9, 7, 9]
l1 = set(l)
l1 = list(l1)
l1.sort()
print(l1[len(l1) - 2])


# Check if a string is a palindrome
# Input: "madam" → Output: True
# Input: "hello" → Output: False
s='madam'
l=0
r=len(s)-1
is_palindrome=True
while l<r:
    if s[l]!=s[r]:
        is_palindrome=False
    l+=1
    r-=1
print(is_palindrome)

#Count the frequency of each character in a string
#Input: "banana" → Output: {'b':1, 'a':3, 'n':2}
s='banana'
d={}
for char in s:
    d[char]=d.get(char,0)+1
print(d)

#Merge two lists and remove duplicates
#Input: [1,2,3], [3,4,5] → Output: [1,2,3,4,5]
l1=[1,2,3]
l2=[3,4,5]
for i in l2:
    if i not in l1:
        l1.append(i)
    else:
        pass
print(l1)