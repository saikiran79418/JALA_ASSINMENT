#2. Write a function to calculate the average value of an array of integers
import array as arr
def avg():
    n = int(input("Enter number of elements: "))
    a = []
    for i in range(n):
        val = int(input(f"Enter element {i + 1}: "))
        a.append(val)
    m=arr.array('i',a)
    s=0
    for i in m:
        s+=i
        avg=s/n
    print(f"The average is: {avg}")
avg()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\4.2.py
#Enter number of elements: 3
#Enter element 1: 1
#Enter element 2: 2
#Enter element 3: 3
#The average is: 2.0

#Process finished with exit code 0
