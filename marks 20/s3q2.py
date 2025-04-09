''' Write a Python program to create a set with any 3 weekdays. Add single element to the set
and print it. Add multiple elements and print the set. '''

set1={'monday','tuesday','wednesday'}
print (set1)
set1.add('thuresday')
print("after adding one element to set1")
print(set1)
set1.update(['friday','saturday'])
print("after additng multiple values ")
print(set1)
