#4. Define a static variable and change within the class
class MyClass:
    static_var=input("enter a string:")
    @classmethod
    def static_method(cls,value):
        cls.static_var=value
print(MyClass.static_var)
MyClass.static_method(input("enter a string:"))
print(MyClass.static_var)
#output
#C:\static_python_assessment\.venv\Scripts\python.exe C:\static_python_assessment\5.4.py
#enter a string:saikiran
#saikiran
#enter a string:change in class level
#change in class level

#Process finished with exit code 0


