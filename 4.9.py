#9. Write a function to reverse an array of integer values
import  array as arr
def reverse():
    n = int(input("Enter number of elements: "))
    a = []
    for i in range(n):
        val = int(input(f"Enter element {i + 1}: "))
        a.append(val)
    m = arr.array('i', a)
    s=m[::-1]
    print(m)
    print(s)
reverse()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\4.9.py
#Enter number of elements: 4
#Enter element 1: 1
#Enter element 2: 2
#Enter element 3: 3
#Enter element 4: 4
#array('i', [1, 2, 3, 4])
#array('i', [4, 3, 2, 1])

#Process finished with exit code 0