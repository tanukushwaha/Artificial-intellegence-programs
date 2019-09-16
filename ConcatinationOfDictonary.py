#Defining the Dictionaries with key and values
dict1={1:100, 2:200}  
dict2={3:300, 4:400}  
dict3={5:500,6:600}  
dict4 = {}

#updating the above 3 dictionary in the dict4
for d in (dict1, dict2, dict3):
    dict4.update(d)

#printing the final result after concatination
print("Concatination of Dictionary ",dict4)  
