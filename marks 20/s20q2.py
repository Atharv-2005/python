'''Write a Python program which accepts 6 integer values and prints “DUPLICATES” if any
of the values entered are duplicates otherwise it prints “ALL UNIQUE”.
Example: Let 5 integers are (32, 10, 45, 90, 45, 6) then output “DUPLICATES” to be printed.'''

numbers_str = input("Enter 6 numbers separated by spaces: ")
numbers = numbers_str.split()

if len(numbers) != 6:
    print("Please enter exactly 6 numbers.")
else:
    if len(set(numbers)) == len(numbers):
        print("ALL UNIQUE")
    else:
        print("DUPLICATES")