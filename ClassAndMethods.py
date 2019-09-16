#creating class person 
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def set(self):
        self.name=input("Enter name: ")
        self.age=int(input("Enter Age: "))
    def get(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

#inheriting the methods of Person class by using super()        
class Student(Person):
    "Represents a students"
    def __init__(self,name='',age=0,rollno=1,marks1=0,marks2=0,marks3=0):
        super().__init__(name,age)
        self.rollno=rollno
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3

    def set(self):
        super().set()
        self.rollno=int(input("Enter roll no: "))
        self.marks1=int(input("Enter marks1: "))
        self.marks2=int(input("Enter marks2: "))
        self.marks3=int(input("Enter marks3: "))
      

    def get(self):
        super().get()
        print("rollno: ",self.rollno)
        print("marks1: ",self.marks1)
        print("marks2: ",self.marks2)
        print("marks3: ",self.marks3,"\n")
    def avg(self):
        return (self.marks1+self.marks2+self.marks3)/3
    def __del__(self):
        print("object is deleted")

#creating the object of Student class
s1=Student()
#calling the set()
s1.set()

#calling the get()
s1.get()

#printing the avg marks of the student
print("avg:",s1.avg())
del s1

        
                                                                                                                                                                                                                                                                                                                                                                                                    
