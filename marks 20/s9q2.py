'''
Write a Python program to create a dictionary from a string.
Sample String: ’Hello all’
Expected output: {'e': 1, 'o': 1, 'a': 1, 'l': 4, 'H': 1}
'''
user_defined_string = input("Enter a string: ")
char_counts = {}

for char in user_defined_string:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

print(char_counts)