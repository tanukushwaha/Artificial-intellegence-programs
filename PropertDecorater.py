class Numbers:
    MULTIPLIER=1
    def __init__(self,x=1,y=2):
        self.x=x
        self.y=y
    def add(self):
        return self.x+self.y
    @classmethod
    def multiply(cls,a=2):
        return cls.MULTIPLIER*a
    @staticmethod
    def subtract(b=0,c=0):
        return b-c
    @property
    def value(self,x=0,y=0):
        print("\nprinting value")
        return tuple((self.x,self.y))
    @value.setter
    def value(self,m1):
        print("\nsetting value")
        self.x=m1[0]
        self.y=m1[1]
    @value.deleter
    def value(self):
        print("\ndeleting object")
        

s=Numbers()
print("Addition :",s.add())
print("multiplication :",Numbers.multiply(2))
print("Subtract : ",Numbers.subtract(3,1))
print("tuple : ",s.value)    

s.value=2,3
print(s.value)
print("x=",s.x,"y=",s.y)
del s.value




 
