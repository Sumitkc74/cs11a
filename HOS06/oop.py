class Employee:
    # pass

    emp_count = 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + '@company.com'
        self.pay = pay
        Employee.emp_count += 1

    def showinfo(self):
        return '{} {}, {}'.format(self.first, self.last, self.email)

emp1 = Employee('Elloit', 'Anderson', 7000)
emp2 = Employee('Jean', 'Gray', 8000)

print(emp1.showinfo())
print("Total Employees: ", Employee.emp_count)

# emp1 = Employee()
# emp2 = Employee()
# print(emp1)
# print(emp2)

# emp1.first = 'Elloit'
# emp1.last = 'Anderson'
# emp1.email = 'elloit.anderson@gmail.com'
# emp1.pay = 7000

# emp2.first = 'Jean'
# emp2.last = 'Gray'
# emp2.email = 'jean.gray@gmail.com'
# emp2.pay = 8000

