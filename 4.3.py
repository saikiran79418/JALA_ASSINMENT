#3. Write a program to find the index of an array element
import array as arr
def index1():
    n = int(input("Enter number of elements: "))
    a= []
    for i in range(n):
        val = int(input(f"Enter element {i + 1}: "))
        a.append(val)
    m=arr.array('i',a)
    y=int(input("Enter an elements to find index: "))
    found=False
    for j in range(len(m)):
        if m[j]==y:
            found=True
    print("The index of the element is:",j)
    if not found:
        print("The index of the element is not found")
index1()
#out put
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\4.3.py
#Enter number of elements: 3
#Enter element 1: 1
#Enter element 2: 2
#Enter element 3: 3
#Enter an elements to find index: 3
#The index of the element is: 2

#Process finished with exit code 0

