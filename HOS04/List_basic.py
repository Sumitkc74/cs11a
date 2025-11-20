list1 = ['physics', 'chemistry', 1997, 2000] # This is a list
list2 = [1, 2, 3, 4, 5 ]               # Another list

print("list1[0]: ", list1[0])           # Accessing first element
print("list2[1:5]: ", list2[1:5])       # Accessing elements from index 1 to 4

print(f"Value before update: {list2}")  # Displaying original list
list2[2] = 10                           # Updating the third element
print(f"Value after update: {list2}")   # Displaying updated list

list1.append(2020)                       # Adding an element to the end of the list
print("New list:", list1)

list1.insert(0, 'Python')               # Inserting an element at the beginning
print("After inserting:", list1)

