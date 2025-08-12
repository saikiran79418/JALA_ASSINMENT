#15. Write a method to find number of even number and odd numbers in an array
import  array as arr
def eveodd():
    n = int(input("Enter number of elements: "))
    a = []
    for i in range(n):
        val = int(input(f"Enter element {i + 1}: "))
        a.append(val)
    m = arr.array('i', a)
    for j in m:
        if j%2==0:
            print("even numbers",j)
        else:
            print("odd numbers",j)
eveodd()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\4.15.py
#Enter number of elements: 3
#Enter element 1: 1
#Enter element 2: 2
#Enter element 3: 3
#odd numbers 1
#even numbers 2
#odd numbers 3

#Process finished with exit code 0