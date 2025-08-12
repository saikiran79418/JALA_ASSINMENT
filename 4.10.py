#10. Write a function to find the duplicate values of an array
import  array as arr
def duplicate():
    n = int(input("Enter number of elements: "))
    a = []
    for i in range(n):
        val = int(input(f"Enter element {i + 1}: "))
        a.append(val)
    m = arr.array('i', a)
    s=arr.array('i')
    for j in range(len(m)):
        for k in range(j+1, len(m)):
            if m[j]==m[k]:
                s.append(m[k])
                print(m)
                print(s)
duplicate()
#out put
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\4.10.py
#Enter number of elements: 3
#Enter element 1: 1
#Enter element 2: 2
#Enter element 3: 2
#array('i', [1, 2, 2])
#array('i', [2])

#Process finished with exit code 0

