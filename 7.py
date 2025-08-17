#A, B and C are classes
#A is a super class. B is a sub class of A. C is a sub class of B.
#Create three methods in each class, 2 methods are specific to each class and third
#method (override method) should be in all three Classes A, B and C
#Create a class with main method. Create an object for each class A, B and C in main
#method and call every method of each class using its own object/instance.
#Call an overridden method with super class reference to B and C class’s objects
#Runtime Polymorphism with Data Members/Instance variables, Repeat the above
#process only for data members
# Superclass A
class A:
    def __init__(self):
        self.data = "Data in A"

    def a_method1(self):
        print("Method 1 in Class A")

    def a_method2(self):
        print("Method 2 in Class A")

    def show(self):  # Overridden method
        print("Show method in Class A")


# Subclass B (inherits A)
class B(A):
    def __init__(self):
        super().__init__()
        self.data = "Data in B"  # Overrides instance variable

    def b_method1(self):
        print("Method 1 in Class B")

    def b_method2(self):
        print("Method 2 in Class B")

    def show(self):  # Overridden method
        print("Show method in Class B")


# Subclass C (inherits B)
class C(B):
    def __init__(self):
        super().__init__()
        self.data = "Data in C"  # Overrides instance variable

    def c_method1(self):
        print("Method 1 in Class C")

    def c_method2(self):
        print("Method 2 in Class C")

    def show(self):  # Overridden method
        print("Show method in Class C")


# Main simulation
if __name__ == "__main__":
    # Objects for each class
    objA = A()
    objB = B()
    objC = C()

    print("---- Calling methods with their own objects ----")
    objA.a_method1()
    objA.a_method2()
    objA.show()

    objB.b_method1()
    objB.b_method2()
    objB.show()

    objC.c_method1()
    objC.c_method2()
    objC.show()

    print("\n---- Runtime polymorphism with methods ----")
    ref: A  # Superclass reference

    ref = objB
    ref.show()  # Calls B's version

    ref = objC
    ref.show()  # Calls C's version

    print("\n---- Runtime polymorphism with data members ----")
    ref = objB
    print(ref.data)  # Will show B's data

    ref = objC
    print(ref.data)  # Will show C's data
#output
#C:\static_python_assessment\.venv\Scripts\python.exe C:\static_python_assessment\7.py
#---- Calling methods with their own objects ----
#Method 1 in Class A
#Method 2 in Class A
##Show method in Class A
#Method 1 in Class B
#Method 2 in Class B
#Show method in Class B
#Method 1 in Class C
#Method 2 in Class C
#Show method in Class C

#---- Runtime polymorphism with methods ----
#Show method in Class B
#Show method in Class C

#---- Runtime polymorphism with data members ----
#Data in B
#Data in C

#Process finished with exit code 0
