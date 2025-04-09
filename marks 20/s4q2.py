''' Write a function to calculate the sum of numbers from 0 to n.'''
n=int(input("Enter a number"))
sum=0
for i in range(n+1):
    sum=sum+i

print(f"sum of number 0 to {n} = {sum}")