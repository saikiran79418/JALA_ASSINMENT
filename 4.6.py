#6. Write a function to copy an array to another array
import array as arr
def copy():
    n = int(input("Enter number of elements: "))
    a = []
    for i in range(n):
        val = int(input(f"Enter element {i + 1}: "))
        a.append(val)
    m = arr.array('i', a)
    y=arr.array('i',m)
    print(f"original array: {m}")
    print(f"new copied array: {y}")
copy()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\4.6.py
#Enter number of elements: 3
#Enter element 1: 1
#Enter element 2: 1
#Enter element 3: 1
#original array: array('i', [1, 1, 1])
#new copied array: array('i', [1, 1, 1])

#Process finished with exit code 0
