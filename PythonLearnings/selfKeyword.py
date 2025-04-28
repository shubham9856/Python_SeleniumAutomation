class Person:
    def __init__(self, name, age):
        # Instance Variables assigned to self keyword to access within the class
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, My Name is {self.name} and I am {self.age} years old"


# Creating class object
person1 = Person("Alice", 24)

print(person1.greet())
