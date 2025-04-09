n_str = input("Enter a number: ")
sum_of_digits = 0

for digit in n_str:
    if digit.isdigit():
        sum_of_digits += int(digit)

print("Sum of digits:", sum_of_digits)