#Write a Python program to find the repeated items of a tuple 
tup=('a','b','c','a','b','d','e','f')
repeted=set(item for item in tup if tup.count(item) > 1)
print(repeted)
