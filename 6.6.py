#6. Matching a String Against a Regular Expression With matches()
import re
s = "saikiran"
pattern = r"[A-Za-z0-9]+"
if re.fullmatch(pattern, s):
    print("String matches the pattern")
else:
    print("String does not match the pattern")
#output
#in python there is no matches() and wehave only re.fullmatch()
#C:\static_python_assessment\.venv\Scripts\python.exe C:\static_python_assessment\6.6.py
#String matches the pattern

#Process finished with exit code 0
