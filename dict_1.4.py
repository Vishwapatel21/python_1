"""VISHWA PATEL - 20CE110
Write a Python script to add a key to a dictionary."""
dict1 = {
    "add" : "+",
    "subtract" : "-",
    "multiply" : "*",
}
print("The dictionary is : ",dict1)
#creating new dictionary with remaining elements
update_dict1 = {
    "divide" : "%",
    "modulo" : "/"
}
#using update function to add the elements to the previous dictionary
dict1.update(update_dict1)
print("updated dictionary is : ",dict1)