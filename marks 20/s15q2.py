#Write a Python program which prints fibonacci series of a number
n=int(input("Enter a number: "))
a=0
b=1
while a < n:
    print(a,end=" ")
    a,b=b,a+b 
