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

    def get_pay(self):
        return self.salary

    def get_contract(self):
        return str(super().__str__()) + " works on a monthly salary of " + str(self.salary)

    def __str__(self):
        return  str(self.get_contract()) + ".  Their total pay is " + str(self.get_pay()) + "."

# Employee on a contract without bonus
class contract_employee(Employee):
    def __init__(self, name, hours, hourly_rate):
        super().__init__(name)
        self.hours = hours
        self.hourly_rate = hourly_rate

    def get_pay(self):
        return self.hours * self.hourly_rate
    
    def get_contract(self):
        return str(super().__str__()) + " works on a contract of " + str(self.hours) + " hours at " + str(self.hourly_rate) + "/hour"

    def __str__(self):
        return str(self.get_contract()) + ".  Their total pay is " + str(self.get_pay()) + "."

# Employee on a salary with a bonus
# Assumes a bonus comission unless contracts specificed
class salary_employee_bonus(salary_employee):
    def __init__(self, name, salary, bonus, contracts=1):
        super().__init__(name, salary)
        self.contracts = contracts
        self.bonus = bonus

    def get_pay(self):
        return self.salary + (self.bonus*self.contracts)

    def __str__(self):
        if self.contracts == 1:
            return str(super().get_contract()) + " and receives a bonus commission of " + str(self.bonus) + ".  Their total pay is " + str(self.get_pay()) + "."
        else:
            return str(super().get_contract()) + " and receives a commission for " + str(self.contracts) + " contract(s) at " + str(self.bonus) + "/contract.  Their total pay is " + str(self.get_pay()) + "."

class contract_employee_bonus(contract_employee):
    def __init__(self, name, hours, hourly_rate, bonus, contracts=1):
        super().__init__(name, hours, hourly_rate)
        self.contracts = contracts
        self.bonus = bonus

    def get_pay(self):
        return (self.hours * self.hourly_rate) + (self.bonus * self.contracts)
    
    def __str__(self):
        if self.contracts == 1:
            return str(super().get_contract()) + " and receives a bonus commission of " + str(self.bonus) + ".  Their total pay is " + str(self.get_pay()) + "."
        else:
            return str(super().get_contract()) + " and receives a commission for " + str(self.contracts) + " contract(s) at " + str(self.bonus) + "/contract.  Their total pay is " + str(self.get_pay()) + "."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = salary_employee('Billie',4000)
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = contract_employee('Charlie',100,25)
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = salary_employee_bonus('Renee',3000,200,4)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = contract_employee_bonus('Jan',150,25,220,3)
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = salary_employee_bonus('Robbie',2000,1500)
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = contract_employee_bonus('Ariel',120,30,600)
