#7. Write a function to insert an element at a specific position in the array
import array as arr
def insert():
    n = int(input("Enter number of elements: "))
    a = []
    for i in range(n):
        val = int(input(f"Enter element {i + 1}: "))
        a.append(val)
    m = arr.array('i', a)
    y=int(input("Enter an elements to insert: "))
    l=int(input("Enter the position to insert: "))
    q=m.insert(l,y)
    print(f"Original array: {m}")
    print(f"New inserted array: {q}")
insert()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\4.7.py
#Enter number of elements: 3
#Enter element 1: 1
#Enter element 2: 2
#Enter element 3: 3
#Enter an elements to insert: 10
#Enter the position to insert: 1
#Original array: array('i', [1, 10, 2, 3])
#New inserted array: None

#Process finished with exit code 0