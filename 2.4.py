#4. Program for relational operators (<,<==, >, >==)
def operators():
    a=int(input("enter a:"))
    b=int(input("enter b:"))
    if a>b:
        print(" here a is larger a>b")
    elif a<b:
        print("here b is larger a<b")
    elif a<=b:
        print("here a is either lower or equal a<=b")
    else:
        print("here b is lower or equal is a>=b")
operators()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\2.4.py
#enter a:10
#enter b:5
# here a is larger a>b

#Process finished with exit code 0

#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\2.4.py
#enter a:5
#enter b:10
#here b is larger a<b

#Process finished with exit code 0

#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\2.4.py
#enter a:22
#enter b:22
#here a is either lower or equal a<=b

#Process finished with exit code 0
# in python we don't have any <== and >== only we have <= and >=.

