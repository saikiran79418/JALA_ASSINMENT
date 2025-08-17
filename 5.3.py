#3. Define a static variable and change within the instance
class change:
    static_var=input("enter a string:")
obj1=change()
obj2=change()
obj1.static_var=input("enter a string:")
print(obj1.static_var)
print(obj2.static_var)
#output
#C:\static_python_assessment\.venv\Scripts\python.exe C:\static_python_assessment\5.3.py
#enter a string:saikiran
#enter a string:change in instance level
#change in instance level
#saikiran

#Process finished with exit code 0
