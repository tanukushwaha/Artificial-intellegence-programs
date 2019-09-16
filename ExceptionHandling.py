try:
    x=int(input("Please enter a intger number: "))
except ValueError:
    print("That was not valid number Try again")
try:
    fh=open("testfile","x")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can't find file or data")
else:
    print("Written content in the file successfully")
    fh.close()
try:
    a=(1,2,3,4,5)
    print(a[7])
except IndexError:
    print("Error : wrong index Try Again")
try:
    a=10/0
    print(a)
except ZeroDivisionError:
    print("Error Cannot divide by zero")
try:
    print("Undefind variable",b)
except NameError:
    print("Undefined variable")
