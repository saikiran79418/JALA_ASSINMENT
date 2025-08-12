#16. Write a function to get the difference of largest and smallest value
import  array as arr
def diff():
    n = int(input("Enter number of elements: "))
    a = []
    for i in range(n):
        val = int(input(f"Enter element {i + 1}: "))
        a.append(val)
    m = arr.array('i', a)
    for j in range(len(m)):
        for k in range(0, len(m)-j-1):
            if m[k]>m[k+1]:
                m[k], m[k+1] = m[k+1], m[k]
    print(m)
    print("largest element is:", m[-1])
    print("smallest element is:", m[0])
    print("difference of largest and smallest:", m[-1]-m[0])
diff()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\4.16.py
#Enter number of elements: 3
#Enter element 1: 1
#Enter element 2: 2
#Enter element 3: 3
#array('i', [1, 2, 3])
#largest element is: 3
#smallest element is: 1
#difference of largest and smallest: 2