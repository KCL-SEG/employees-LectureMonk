"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

# Super employee class
class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

# Employee on a salary without bonus
class salary_employee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

# Employee on a contract without bonus
class contract_employee(Employee):
    def __init__(self, name, hours, hourly_rate):
        super().__init__(name)
        self.hours = hours
        self.hourly_rate = hourly_rate

# Employee on a salary with a bonus
# Assumes a bonus comission unless contracts specificed
class salary_employee_bonus(salary_employee):
    def __init__(self, name, salary, bonus, contracts=0):
        super().__init__(name, salary)
        self.contracts = contracts
        self.bonus = bonus

class contract_employee_bonus(contract_employee):
    def __init__(self, name, hours, hourly_rate, bonus, contracts=0):
        super().__init__(name, hours, hourly_rate)
        self.contracts = contracts
        self.bonus = bonus

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
