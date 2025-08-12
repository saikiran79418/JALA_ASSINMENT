#18. Write a program to remove the duplicate elements and return the new array
import  array as arr
def remdupnewarr():
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
    return s
res=remdupnewarr()
print(res)
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\4.18.py
#Enter number of elements: 4
#Enter element 1: 1
#Enter element 2: 2
#Enter element 3: 2
#Enter element 4: 3
#array('i', [1, 2, 3])

#Process finished with exit code 0
