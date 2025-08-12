#11. Program to check whether a number is EVEN or ODD using switch
def switch():
    a=int(input("enter a number:"))
    match(a%2):
        case 0:
            print("the number is even",a)
        case 1:
            print("the number is odd",a)
switch()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\3.11.py
#enter a number:3
#the number is odd 3

#Process finished with exit code 0
#here there no switch case in python.
