'''Write a Python program which finds sum of digits of a number. [20 M]
Example n=130 then output is 4 (1+3+0).'''
n=input("Enter number: ")
sum=0
for digit in n:
    if digit.isdigit():
        sum=sum+int(digit)

print("sum of digits is = ",sum)