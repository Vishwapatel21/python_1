"""VISHWA PATEL - 20CE110
 Write a Python script to check whether a given key already exists in a dictionary."""

#declaring a dictionary
dict1={
    "abc":"cba",
    "marks":"good",
    "pretty":"beautiful"
}
#taking any key from the dictionary
t1="take"
#using if..in function to check whether given key is present in dictionary or not
if t1 in dict1:
    print(t1," is present")
else:
    print(t1," is absent")