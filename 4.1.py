#arrays
#1. Write a function to add integer values of an array
from array import *
def arry():
    n = int(input("Enter number of elements: "))
    arr = []
    for i in range(n):
        val = int(input(f"Enter element {i + 1}: "))
        arr.append(val)
    val=array('i',arr)
    s=0
    for i in val:
        s+=i
    print("the sum of array is ",s)
arry()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\4.1.py
#Enter number of elements: 3
#Enter element 1: 1
#Enter element 2: 2
#Enter element 3: 3
#the sum of array is  6

#Process finished with exit code 0
