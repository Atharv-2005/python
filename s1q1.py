#Write a Python function to check whether a number is in a given range
num1=int(input("Enter number "))
start=int(input("Range start from: = "))
end=int(input("Range end at:= "))
if (start <= num1 <= end):
    print("Given number is in range: ")
else:
    print("Given number is not in range: ")

