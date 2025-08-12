#4. Write a function to test if array contains a specific value
import array as arr
def test():
    n = int(input("Enter number of elements: "))
    a = []
    for i in range(n):
        val = int(input(f"Enter element {i + 1}: "))
        a.append(val)
    m = arr.array('i', a)
    y=int(input("Enter a specific value: "))
    contains=False
    for j in m:
        if j==y:
            contains=True
            break
    if contains==True:
        print(f"Element {y} is  contained in array.")
    else:
        print(f"Element {y} is not contained in array.")
test()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\4.4.py
#Enter number of elements: 3
#Enter element 1: 1
#Enter element 2: 2
#Enter element 3: 3
#Enter a specific value: 4
#Element 4 is not contained in array.

#Process finished with exit code 0
