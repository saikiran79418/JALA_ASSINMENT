#8. Write a program to find Armstrong number or not
def armstrong():
    a=int(input("enter a number:"))
    s=0
    b=str(a)
    print(b)
    for i in b:
        s=s+(int(i))**3
    print(s)
    if s==a :
        print("the number is an armstrong number",a)
    else:
        print("the number is not an armstrong number",a)
armstrong()

#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\3.8.py
#enter a number:153
#153
#153
#the number is an armstrong number 153

#Process finished with exit code 0


