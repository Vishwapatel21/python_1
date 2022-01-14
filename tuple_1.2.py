"""VISHWA PATEL - 20CE110
Write a Python program to create a tuple with numbers and print one item. """
#taking input values from user
a1=input("enter first number :")
a2=input("enter second number :")
a3=input("enter third number :")
a4=input("enter fourth number :")
a5=input("enter fifth number :")



myNumber=(a1,a2,a3,a4,a5)
print(myNumber)
#printing number present on the second position
secondNumber=myNumber[1]
print("The second element of tuple is : ",secondNumber)
