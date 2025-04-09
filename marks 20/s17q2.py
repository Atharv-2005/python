'''Write a Python program to count frequency of each character in a given string using user
defined function.'''
string=input("Enter string ")
string1=string.lower()
count={}
for i in string1:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1

print(count)