alien_0 = {'color': 'green', 'points': 5}
alen_1 = {'color': 'yellow', 'points': 10}

aliens = [alien_0, alen_1]

# Accessing key, value
for i in aliens:
    for key, value in i.items():
        print("Key: ", key, "\t", "Value:", value)