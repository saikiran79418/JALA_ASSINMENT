#17. Write a method to verify if the array contains two specified elements(12,23)
import array as arr
def check_elements():
    n = int(input("Enter number of elements: "))
    a = []
    for i in range(n):
        val = int(input(f"Enter element {i+1}: "))
        a.append(val)
    m = arr.array('i', a)
    has_12 = False
    has_23 = False
    for num in m:
        if num == 12:
            has_12 = True
        if num == 23:
            has_23 = True
    if has_12 and has_23:
        print("Array contains both 12 and 23.")
    else:
        print("Array does not contain both 12 and 23.")
check_elements()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\4.17.py
#Enter number of elements: 4
#Enter element 1: 1
#Enter element 2: 12
#Enter element 3: 23
#Enter element 4: 4
#Array contains both 12 and 23.

#Process finished with exit code 0

