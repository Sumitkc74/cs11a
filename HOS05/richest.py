income = {'Alice': 120000, 
          'Bob': 100000, 
          'Jeff': 200000,
          'Apiwat': 999998,
          'Diana': 999999}

highest = max(income, key=income.get)
print("The richest person is:", end='')
print(highest + " with $" + str(income[highest]))

lowest = min(income, key=income.get)
print("The least richest person is: ", end='')
print(lowest + " with $" + str(income[lowest]))