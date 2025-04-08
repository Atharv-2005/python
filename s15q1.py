'''Write a Python program to create tuple of n numbers, print the first half values of tuple in
one line and the last half values of tuple on next line.'''
n=int(input("Enter size of tuple "))
nums=[]
for i in range(n):
    num=float(input(f"Enter {i+1} element "))
    nums.append(num)

t=tuple(nums)
print(t)

length=len(t)
half=length//2 #for integer division " // "used 

print("First half",end=" ")
for i in range(half):
    print(t[i],end=" ")
print()
print("second half",end=" ")
for i in range(half,length):
    print(t[i],end=" ")
print()