class Employee:
    emp_raise_amt = 1.04  # 4% Raise amount to be applied on emp sal

    def __init__(self, firstName, lastName, sal):
        self.firstName = firstName
        self.lastName = lastName
        self.sal = sal

    def fullname(self):
        return f"{self.firstName} {self.lastName}"

    def email(self):
        return f"{self.firstName}.{self.lastName}@company.com"

    def apply_sal_raise(self):
        self.sal = self.sal * Employee.emp_raise_amt
        return self.sal


class Manager(Employee):
    def __init__(self, firstName, lastName, sal, project):
        super().__init__(firstName, lastName, sal)
        self.project = project

    def manager_project(self):
        return self.project


# Employee class objects
emp1 = Employee("Test", "User", 1)

print(emp1.fullname())  # Prints Full name
print(emp1.email())

# Update the employees salary
print("Raised Salary Amount is: ", emp1.apply_sal_raise())

# Manager Class Objects
mgr1 = Manager("Kanchan", "Manager", 2, "Testing_Project")
print(mgr1.manager_project())  # Prints the managers project name
print(mgr1.email())

# Now Raise the salary of manager as well
print("amount raise as per employee amt raise: ", mgr1.apply_sal_raise())

print(mgr1.fullname_use())
