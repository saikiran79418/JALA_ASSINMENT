#5. Write a function to remove a specific element from an array
import array as arr
def remove():
    n = int(input("Enter number of elements: "))
    a = []
    for i in range(n):
        val = int(input(f"Enter element {i + 1}: "))
        a.append(val)
    m = arr.array('i', a)
    y=int(input("Enter an elements to remove: "))
    if y in m:
        m.remove(y)
        print(m)
    else:
        print("Element not found")
remove()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\4.5.py
#Enter number of elements: 3
#Enter element 1: 1
#Enter element 2: 2
#Enter element 3: 3
#Enter an elements to remove: 3
#array('i', [1, 2])

#Process finished with exit code 0


