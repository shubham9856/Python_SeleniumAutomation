# Class name should start with capital letter
class Employee:
    # Class Variables
    no_of_emp = 0
    sal_raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'  # Auto create email using instance data

        # Update the variable at class level to keep the count of instance method executed
        Employee.no_of_emp += 1

    def full_data(self):
        return f"{super()}\nName: {self.first} {self.last} \nPay: {self.pay}"

    def salary_raise(self):
        self.pay = self.pay * self.sal_raise_amt  # it will update the emp object pay value
        return self.pay  # Return updated pay value


emp1 = Employee("Test", "User", 50000)
emp2 = Employee("Alice", "Mark", 70000)

print("Employee 2 name:", emp2.first)

print(emp2.__dict__)
print("Number of employee objects created are:", Employee.no_of_emp)

print(f"use of super: {emp1.full_data()}")  # Super returns the object of the parent class

# Get the sal raise for emp objects employees
print(emp1.salary_raise())
print(emp1.__dict__)
