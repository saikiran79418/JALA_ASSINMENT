#Define the local and Global variables with the same name and print both variables and
#understand the scope of the variables

name="sai" #global variable

def display():
    name="sai"
    print("local variable",name)
print("global variable",name)
display()
print("after calling display print global variable ",name)

#understand scope
#Global variable is declared outside of any function and can be accessed anywhere in the file.

#Local variable is declared inside a function and is accessible only within that function.

#If a local variable has the same name as a global one, it shadows (overrides) the global variable inside the function scope.

#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\1.4.py
#global variable sai
#local variable sai
#after calling display print global variable  sai

#Process finished with exit code 0
