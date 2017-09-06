12  # Python Classes learning


class Employee():

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@company.com'.format(first, last)


emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)


emp_1.first = 'Xan'
emp_1.last = 'Caperton'
emp_1.email = 'capertja@gmail.com'
emp_1.pay = 50000

emp_2.first = 'Xan'
emp_2.last = 'Caperton'
emp_2.email = 'capertja@gmail.com'
emp_2.pay = 50000
