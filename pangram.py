#practical 3 A
def ispangram(strr):
    
    lists='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for i in lists:
        if i in strr:
            return True
        else:
            return False
        
    
#string="The quick brown fox jumps over the lazy dog"
string=input("Enter sentence to check sentence is pangram or not: ")
ls=ispangram(string)
if(ls==True):
    print("sentence is pangram")
else:
    print("sentence is not a pangram")
    
        





    
