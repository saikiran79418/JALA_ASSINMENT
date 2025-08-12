#12. Print gender (Male/Female) program according to given M/F using switch
def switch():
    gender = input("Enter gender (M/F): ").upper()  # Convert to uppercase

    match gender:
        case "M":
            print("Gender: Male")
        case "F":
            print("Gender: Female")
        case _:
            print("Invalid input")
switch()
#output
#C:\internship_python_assinment\.venv\Scripts\python.exe C:\internship_python_assinment\3.12.py
#Enter gender (M/F): m
#Gender: Male

#Process finished with exit code 0
#in python there is no switch case