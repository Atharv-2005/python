#Write a Python program to find the length of a string without using built-in function
def strinlength(s):
    c=0
    for _ in (s):
        c+=1
    return c 

string=input("Enter stinng ")
print(f"length of {string} is = {strinlength(string)}")
