motorcycle = ['Honda', 'Yamaha', 'Suzuki']
del motorcycle[1]
print(motorcycle)

motorcycles = ['Honda', 'Yamaha', 'Suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
first_owned = motorcycles.pop(0)
print("The first owned motorcycle is a ",first_owned)

motorcycles = ['Honda', 'Yamaha', 'Suzuki']
motorcycles.remove('Suzuki')
print(motorcycles)