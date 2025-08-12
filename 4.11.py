#11. Write a program to find the common values between two arrays
import  array as arr
def common():
    n = int(input("Enter number of elements: "))
    a = []
    s=[]
    for i in range(n):
        val = int(input(f"Enter element {i + 1}: "))
        new=int(input(f"Enter new element {i + 1}: "))
        s.append(new)
        a.append(val)
    m = arr.array('i', a)
    r=arr.array('i',s)
    c=[]
    for j in range (len(m)):
        for k in range (len(r)):
            if m[j]==r[k] and m[j] not in c:
                c.append(m[j])
    print("common elements are",c)
common()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\4.11.py
#Enter number of elements: 3
#Enter element 1: 1
#Enter new element 1: 2
#Enter element 2: 3
#Enter new element 2: 5
#Enter element 3: 4
#Enter new element 3: 3
#common elements are [3]

#Process finished with exit code 0

