#Write a Python program to calculate the average of numbers in a given list.
numbers_str = input("Enter numbers separated by spaces: ")
numbers_list = [float(num) for num in numbers_str.split()]
average = sum(numbers_list) / len(numbers_list)
print("Average:", average)