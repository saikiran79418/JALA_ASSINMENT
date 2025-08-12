#10. Write a program to palindrome or not.
def palindrome():
    num = int(input("Enter a number: "))
    original_num = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    if original_num == reversed_num:
        print(original_num, "is a palindrome number")
    else:
        print(original_num, "is not a palindrome number")
palindrome()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\3.10.py
#Enter a number: 12321
#12321 is a palindrome number

#Process finished with exit code 0
