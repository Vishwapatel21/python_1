"""VISHWA PATEL - 20CE110
Write a Python program to create an intersection, Union, difference of sets."""
s1 = {1,2,3,4,5,6,7,8,9,0}
s2 = {2,4,6,8}
print("Set A is : ",s1)
print("Set B is : ",s2)
#intersection of set -  we use & operator
s3 = s1 & s2
print("Intersection of set A and B is : ",s3)
#union of set - we use | operator
s3 = s1 | s2
print("Union of set A and B is : ",s3)
#difference of set
#s1-s2 gives elements which are present in s1 but not in s2
s3 = s1 - s2
print("Elements present in set A but not in set B are : ",s3)
#s2-s1 gives elements which are present in s2 but not in s1
s3 = s2 - s1
print("Elements present in set B but not in set A are : ",s3)
