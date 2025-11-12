def numbers(limit):
    i = 0
    numbers = []

    while i < limit:
        numbers.append(i)
        i += 1

    return numbers

user_limit = int(input("Enter a limit: "))
print(numbers(user_limit))

def printme(str):
    print(str)
    return

printme("First call to user defined function")
printme("Second call to user defined function")