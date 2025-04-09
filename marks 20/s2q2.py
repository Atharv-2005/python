'''Write a Python program to perform given operations on set. 
a. check whether 2 sets are equal or not
b. Symmetric difference
c. Intersection of sets
d. Find maximum and the minimum value in a set'''

set1={1,2,3,4,5,6}
set2={5,6,4,7,8,9}
if(set1 == set2):
    print("two sets are equal")
else:
    print("sets are not equal")

print("symmetric diffrence is = ",set1^set2)
print("intersection of two set = ",set1 & set2)
print(f"maximum and minimum from set1 = {max(set1)} , {min(set1)}")
print(f"maximum and minimum from set2 = {max(set2)} , {min(set2)}")