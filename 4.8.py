#8. Write a function to find the minimum and maximum value of an array8.
import array as arr
def minmax():
    n = int(input("Enter number of elements: "))
    a = []
    for i in range(n):
        val = int(input(f"Enter element {i + 1}: "))
        a.append(val)
    m = arr.array('i', a)
    for j in range(len(m)):
        for k in range(0, len(m)-j-1):
            if m[k] > m[k+1]:
                m[k], m[k+1] = m[k+1], m[k]
    print(m)
    print("Minimum value: ", m[0])
    print("Maximum value: ", m[-1])
minmax()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\4.8.py
#Enter number of elements: 3
#Enter element 1: 5
#Enter element 2: 3
#Enter element 3: 7
#array('i', [3, 5, 7])
#Minimum value:  3
#Maximum value:  7

#Process finished with exit code 0

