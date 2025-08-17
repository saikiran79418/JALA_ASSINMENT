#1. Create a class with PRIVATE fields, private method and a main method. Print the fields
#in main method. Call the private method in main method.
#Create a sub class and try to access the private fields and methods from sub class.
class A:
    def __init__(self):
        # Private fields
        self.__name = "Sai"
        self.__age = 21

    # Private method
    def __display(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

    # Simulating main method
    def main_method(self):
        # Accessing private fields inside the class
        print("Accessing private fields in main method:")
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")

        # Calling private method inside the class
        print("Calling private method inside main method:")
        self.__display()


# Subclass of A
class B(A):
    def access_private(self):
        print("Trying to access private members from subclass...")

        # These will cause AttributeError
        try:
            print(self.__name)
        except AttributeError as e:
            print(e)

        try:
            self.__display()
        except AttributeError as e:
            print(e)


# Create object of A and call main method
objA = A()
objA.main_method()

print("\n--- From Subclass ---")
objB = B()
objB.access_private()
#output
#C:\static_python_assessment\.venv\Scripts\python.exe C:\static_python_assessment\8.1.py
#Accessing private fields in main method:
#Name: Sai
#Age: 21
#Calling private method inside main method:
#Name: Sai, Age: 21

#--- From Subclass ---
#Trying to access private members from subclass...
#'B' object has no attribute '_B__name'
#'B' object has no attribute '_B__display'

#Process finished with exit code 0

