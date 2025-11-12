my_dict = {"name": "abc", "age": 30}

print(my_dict)

#Updating Values in Dictionary
my_dict["age"] = 31
print("Updated: ", my_dict)

#Adding
my_dict["city"] = "New York"
print("After Adding: ", my_dict)

#Deleting
del my_dict["age"]
print("After Deleting 'age': ", my_dict)