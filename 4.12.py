#12. Write a method to remove duplicate elements from an array
import  array as arr
def remdup():
    n = int(input("Enter number of elements: "))
    a = []
    for i in range(n):
        val = int(input(f"Enter element {i + 1}: "))
        a.append(val)
    m = arr.array('i', a)
    s=arr.array('i')
    for j in m:
        if j not in s:
            s.append(j)
    print(s)
remdup()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\4.12.py
#Enter number of elements: 3
#Enter element 1: 1
#Enter element 2: 1
#Enter element 3: 2
#array('i', [1, 2])
