original = [8, 20, -10, 55, -777]
modified = []

for i in original:
    if i < 0:
        i = abs(i)
    
    print(i)
    modified.append(i)

print("Original list:", original)
print("Modified list:", modified)