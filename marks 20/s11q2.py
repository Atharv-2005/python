'''Write a Python program to accept string and remove the characters which have odd index
values of a given string using user defined function'''
def remove_odd(s):
  result = ""
  for i in range(0, len(s), 2):
    result += s[i]
  return result

text = input("Enter a string: ")
modified_text = remove_odd(text)
print("Result:", modified_text)