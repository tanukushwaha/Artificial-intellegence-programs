def iscumulative(lists):
    sum1=[]
    length=len(lists)
    
    sum1=[sum(lists[0:x+1])for x in range(0,length) ]
    return sum1
a=[]
n=int(input("Enter the number of elements in the lists: "))
for x in range(0,n):
    element=int(input("Enter element "+str(x+1)+":"))
    a.append(element)
print(a)

print("Result after cumulative sum of the list: ",iscumulative(a))
    

