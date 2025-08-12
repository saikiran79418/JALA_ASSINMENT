#14. Write a method to find the second largest number in an array
import  array as arr
def remdup():
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
    print("second largest element is:", m[-2])
remdup()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\4.13.py
#Enter number of elements: 4
#Enter element 1: 55
#Enter element 2: 22
#Enter element 3: 77
#Enter element 4: 2
#array('i', [2, 22, 55, 77])
#second largest element is: 55

#Process finished with exit code 0
