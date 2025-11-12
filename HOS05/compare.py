# Compare two lists
first = ['cats', 'dogs', 55]
second = ['dogs', 55, 'cats']
print(first == second)  # This will print False because the order is different

# Compare two dictionaries, order does not matter
first_dict = {'name': 'abc', 'species': 'human','age': 30}
second_dict = {'species': 'human', 'age': 30, 'name': 'abc'}
print(first_dict == second_dict)  # This will print True because the key-value pairs are the same