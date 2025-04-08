#Write a python program to check if a string is a Palindrome or not
string=input("Enter string ")
revstring=string[::-1]
if revstring == string:
    print("string is palindrom")
else:
    print("String is not palindrom")