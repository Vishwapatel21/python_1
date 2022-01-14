"""VISHWA PATEL - 20CE110
Write a Python program to add an item in a tuple."""
a1=input("enter first number :")
a2=input("enter second number :")
a3=input("enter third number :")
a4=input("enter fourth number :")
a5=input("enter fifth number :")

myNumber=(a1,a2,a3,a4,a5)
print("original tuple is : ",myNumber)
#type casting tuple into list to perform append function
L1=list(myNumber)
#adding element at the end of the list
L1.append(100)
#type casting list into tuple to get the final output in tuple
T1=tuple(L1)
print("updated tuple is : ",T1)