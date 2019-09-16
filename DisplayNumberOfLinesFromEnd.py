fname=input("Enter file name to be displayed: ")
f=open(fname)
line_count=0
num=int(input("Enter no of lines to be displayed from end: "))
line=f.readline()
while line!='':
    line=f.readline()
    line_count=line_count+1
n=(line_count-num)
f.close()
f1=open(fname)
p=f1.readline()
while(n!=1):
    p=f1.readline()
    n=n-1
print(f1.read())
f1.close()
