# Write a Python program to accept the strings which contains all vowels.
def allvowels(s) :
    return set('aeiou') <= set(s.lower())

string=input("Enter string")
if(allvowels(string)):   
    print(f"{string} contain all vowels")
else: 
    print(f"{string } dose not contain all vowels")