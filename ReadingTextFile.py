#Enter the name of the file to reading the file
file_name=input("Enter file name to reading entire text file:")

#opening the file and storing it to file variable
file=open(file_name)

#reading the file and storing it to the a variable
a=file.read()

#printing the 'a' which will display the content of the file
print(a)

#closing the file
file.close()
