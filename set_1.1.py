"""VISHWA PATEL - 20CE110
 Write a Python program to add member(s) in a set and clear a set"""
#creating a set
s1 = {1,2,3,4,5,6,7}
print("The original set is : ",s1)
#adding members in the set
s1.add("hello")
s1.add(200)
#printing the updated set
print("The updated set is : ",s1)
#clearing all the elements of set
s1.clear()
print("Cleared set is : ",s1)