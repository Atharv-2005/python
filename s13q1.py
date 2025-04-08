'''Write a Python program to create a tuple of n numbers and print maximum, minimum, and
sum of elements in a tuple'''
n=int(input("Enter size of tuple "))
nums=[]
for i in range(n):
    num=float(input(f"Enter num {i+1}: "))
    nums.append(num)

t = tuple(nums)
print("tuple is = ",t)
print(" maximimum from given tuple is = ",max(t))
print(" minimum from given tuple is = ",min(t) )
print("sum of the tuple = ",sum(t))