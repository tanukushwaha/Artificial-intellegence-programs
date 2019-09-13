#program for checking if char is vowel or not
def isVowel(char):
    if(len(char)==1):
       all_vowels='AEIOUaeiou'
    return char in all_vowels
str=input("Enter only one character to check that entered char is vowel or not: ")
if str.isdigit():
    print("Entered char is digit")
ch=isVowel(str)
if(ch==True):
    print("Entered char is vowel")
else:
    print("Entered char is not a vowel")
