#3. Program to equal operator and not equal operators
def ope():
    for i in range(1,8):
        if(i==4): # here we can use != operator also.
            print("i is equal to 4",i)
            continue
        else:
            print("i is not equal to ",i)
ope()

#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\3.3.py
#i is not equal to  1
#i is not equal to  2
#i is not equal to  3
#i is equal to 4 4
#i is not equal to  5
#i is not equal to  6
#i is not equal to  7

#Process finished with exit code 0