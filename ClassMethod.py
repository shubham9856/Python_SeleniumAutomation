class MyClass:
    @classmethod
    def class_method(cls):
        print("From Class Method")

    def instance_method(self):
        print("From Instance Method")


# Accessing class Method without creating object
MyClass.class_method()

# Accessing Instance Method (Need to create object first)
obj = MyClass()
obj.instance_method()

# With class method we can avoid creating object and then accessing the method
obj.class_method()
