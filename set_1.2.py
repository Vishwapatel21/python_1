"""VISHWA PATEL - 20CE110
 Write a Python program to remove an item from a set if it is present in the set."""
s1 = {1,2,3,4,5,6,7,8,9,0}
print("The set is : ",s1)
#removing an item from the set
s1.remove(4)
s1.remove(5)
#printing the updated set
print("The updated set is : ",s1)
#s1.remove(15) #will throw an error as 15 is not present in set
