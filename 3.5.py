#5. Write a program to print largest number among three numbers.
def lagest():
    large = 0
    for j in b:
        if j>large:
            large=j
    print("largest number is ",large)

a=int(input("enter the number:"))
b=[]
for i in range(a):
    b.append(int(input("enter three number:")))
print(b)
lagest()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\3.5.py
#enter the number:3
#enter three number:4
#enter three number:3
#enter three number:6
#[4, 3, 6]
#largest number is  6

#Process finished with exit code 0