#9. Write a program to find the prime or not.
def primeornot():
    num = int(input("Enter a number: "))
    if num <= 1:
        print(num, "is not a prime number")
    else:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):  # Check till square root of num
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, "is a prime number")
        else:
            print(num, "is not a prime number")
primeornot()

#out put
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\3.9.py
#Enter a number: 6
#6 is not a prime number

#Process finished with exit code 0
